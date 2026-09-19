"""Standard-library replay of saved numerical candidates and rational certificates."""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import copy,hashlib,json
from exact import require,ratios,margin_certificate,log_bounds,rank
from construction import parameters,dimension_points,check_witness

HERE=Path(__file__).resolve().parent
OLD=HERE.parents[1]/'two_prefix_selection_2026_09_19/experiments/sharpness-results.json'


def verify_entry(entry):
    p=list(map(F,entry['rational_witness']));tau=F(9999,10000)
    r=[F(4,5)**(5-i) for i in range(5)]+[F(1,1000)]
    require(len(p)==6 and p[0]==F(999,1000) and all(0<x<tau for x in p))
    require(sum(i*p[i] for i in range(1,6))==12)
    require(all(x>1 for x in ratios(p,r,entry['prefix'])))
    lam=list(map(F,entry['certificate']['weights']))
    actual=margin_certificate(p,r,entry['prefix'],lam,tau,F(12))
    require(actual==entry['certificate'])
    require(F(actual['log_margin_lower'])>0 and F(actual['certified_gap'])<F(47,10**9))


def main():
    paths=[HERE/'prefix-results.json',HERE/'construction-results.json']
    hashes=0
    for path in paths:
        receipt=json.loads(path.read_text())
        for name,digest in receipt['source_sha256'].items():
            source=OLD if name=='sharpness-results.json' else HERE/name
            require(hashlib.sha256(source.read_bytes()).hexdigest()==digest,'source mismatch: '+name)
            hashes+=1
    first=json.loads(paths[0].read_text());old=json.loads(OLD.read_text())
    require([e['prefix'] for e in first['results']]==old['higher_dimensions'][1]['missing_prefixes'])
    for entry in first['results']:verify_entry(entry)
    # Rejection of wrong bounds, witness values and purported support certificates.
    tampered=0
    for key in ['p','upper','gradient','weights']:
        e=copy.deepcopy(first['results'][0])
        if key=='p':e['rational_witness'][1]='0'
        elif key=='upper':e['certificate']['supremum_upper']='0'
        elif key=='gradient':e['certificate']['gradient'][0]='0'
        else:e['certificate']['weights']=['1']*4
        try:verify_entry(e)
        except ValueError:tampered+=1
        else:raise ValueError('accepted corruption: '+key)
    # Exact log identities and order bounds; no floating-point log oracle used.
    identities=0
    for x in [F(1,1000000),F(1,7),F(1,2),F(1),F(2),F(7),F(1000000)]:
        lo,hi=log_bounds(x);a,b=log_bounds(1/x)
        require(lo<=hi and hi-lo<F(1,10**10))
        require(lo+a<=0<=hi+b)
        if x<1:require(hi<0)
        if x==1:require(lo==hi==0)
        if x>1:require(lo>0)
        identities+=1
    # Finite exact controls for the fixed-threshold construction obstruction.
    threshold_checks=0
    for m in range(2,101):
        C=F(m*(m+1),2)
        require(C/(C-m+1)<=F(3,2))
        require(F(2,3)**(m-1)*C/(C-m+1)<=1)
        threshold_checks+=1
    # Counterexample to overgeneralizing the ansatz obstruction: R08 has no
    # universal singleton even at tau=2/3 (witnesses can differ).
    r=[F(7,50),F(2,5),F(1,10)]
    for i,s in enumerate([F(17,50),F(13,20),F(1,5)]):
        p=[F(13,20),F(17,20)-5*s/4,s]
        require(all(0<x<F(2,3) for x in p))
        require(prod(p[j] for j in range(3) if j!=i)>r[i])
    # General construction controls: both cases, record gaps, terminal record.
    for prefix in [(0,1,2,3),(0,5,3,1),(0,3,2,4),(4,0,5,1)]:
        check_witness(5,prefix)
    print(json.dumps({'status':'passed','saved_prefix_certificates':len(first['results']),
          'source_hashes_checked':hashes,'corruptions_rejected':tampered,
          'log_identity_controls':identities,'fixed_threshold_checks':threshold_checks,
          'preserved_R08_quantifier_controls':3,'general_construction_controls':4,
          'receipt_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
          'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Exact arithmetic replay of specific certificates and controls; no proof-assistant or independent-kernel claim.'},indent=2))

if __name__=='__main__':main()
