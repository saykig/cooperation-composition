"""Recheck saved receipts and certificate CLI, without re-running discovery searches."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
from selector import require, constraints, verify_sign, verify
from sharpness import certify
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent

def read(name):
    return json.loads((HERE/name).read_text())


def main():
    checked=0
    old=HERE.parents[1]/'robust_order_polytope_2026_09_19/experiments/explore.py'
    receipts={name:read(name) for name in ['results.json','additional-results.json','sharpness-results.json']}
    for d in receipts.values():
        require(d['status']=='passed')
        for name,digest in d['source_sha256'].items():
            path=old if name=='explore.py' else HERE/name
            require(hashlib.sha256(path.read_bytes()).hexdigest()==digest, 'source identity mismatch: '+name)
            checked+=1
    first=receipts['results.json']
    for f in first['fixtures'].values():
        verify(f['input'],f['result'])
        gs=constraints(f['input'],f['specified_prefix'])
        require(verify_sign(gs,f['prefix_certificate']) == (f['prefix_certificate']['kind']=='witness'))
        checked+=2
    additional=receipts['additional-results.json']
    verify(additional['large_endpoint_input'],additional['result']);checked+=1
    sharp=receipts['sharpness-results.json']
    s=sharp['segment_sharpness']
    for e in s['rejected_singletons']:
        require(verify_sign(constraints(s['input'],e['prefix']),e['certificate']));checked+=1
    require(not verify_sign(constraints(s['input'],s['successful_pair']),s['certificate']));checked+=1
    hulls=[sharp['dimension_two']]+[x['certificate'] for x in sharp['higher_dimensions'] if x['status']=='certified']
    for c in hulls:
        vertices=[list(map(F,v)) for v in c['vertices']]
        require(certify(c['n']-1,vertices,list(map(F,c['r'])),F(c['tau']))==c)
        checked+=1
    # Exercise both CLI generation and checking, including a success and rejection.
    for name in ['changing_blocker_shared_root','modelwise_success_no_common_order']:
        f=first['fixtures'][name]
        with tempfile.TemporaryDirectory(prefix='r10-audit-') as tmp:
            inp=Path(tmp)/'input.json';out=Path(tmp)/'certificate.json'
            inp.write_text(json.dumps(f['input']))
            generated=subprocess.check_output([sys.executable,str(HERE/'selector.py'),str(inp)],text=True)
            require(json.loads(generated)==f['result']);out.write_text(generated)
            message=subprocess.check_output([sys.executable,str(HERE/'selector.py'),str(inp),str(out)],text=True)
            require(message.strip()=='certificate verified')
            checked+=2
    # The optional optimized-run receipt is compared when supplied, not assumed.
    optimized=None
    if len(sys.argv)>1:
        opt=json.loads(Path(sys.argv[1]).read_text())
        require(opt['counts']==first['counts'] and opt['source_sha256']==first['source_sha256'])
        for name,f in first['fixtures'].items():
            require({k:v for k,v in f.items() if k!='elapsed_seconds'} ==
                    {k:v for k,v in opt['fixtures'][name].items() if k!='elapsed_seconds'})
        optimized={'counts_identical':True,'certificates_identical':True,
                   'checks':opt['total_checks'],'python':opt['python']}
    print(json.dumps({'status':'passed','audit_checks':checked,'optimized_run':optimized,
                      'receipt_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in receipts},
                      'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'scope':'Source identities, saved certificates, hull certificates and CLI; handwritten proofs require mathematical review.'},indent=2))

if __name__=='__main__':main()
