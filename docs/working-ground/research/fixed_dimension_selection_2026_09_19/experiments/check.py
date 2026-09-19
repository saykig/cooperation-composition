"""Independent exhaustive-order comparison and certificate corruption controls."""
import argparse
import copy
import hashlib
import itertools
import json
import platform
import time
from pathlib import Path
import cvc5
import z3
from fixtures import cases, instance
from geometry import Domain
from independent import feasible
from selector import select, decide, margins
from verify import verify, require
from fractions import Fraction as F


def run(output=None):
    started = time.monotonic()
    rows, artifacts = [], {}
    orders = 0
    for name, (data, expected, length) in cases().items():
        t = time.monotonic()
        result = select(data, 30000)
        require(result['status'] == expected, name+': expected outcome')
        if length is not None:
            require(len(result['prefix']) == length, name+': minimum prefix')
        verify(data, result, 30000)
        successful = []
        for order in itertools.permutations(range(len(data['r']))):
            # Full-order feasibility, independent of the Helly prefix reduction,
            # independent geometry representation, independent solver algorithm.
            good = not feasible(data, order, 30000)
            successful.append(good)
            orders += 1
        require(any(successful) == (expected == 'zero'), name+': exhaustive order mismatch')
        if name == 'triangle_three':
            require(len(result['rejected_before_success']) == 16, 'All 4 singletons and 12 pairs defeated')
        if name.startswith('vertex_miss'):
            for v in data['vertices']:
                require(not all(x > 0 for x in margins(list(map(F,v)), list(map(F,data['r'])), (0,1,2))), 'Vertex should block')
        if name == 'narrow_segment':
            w, _ = decide(Domain(data), (0,1))
            require(w is not None, 'Tiny open interval missed')
            tt = F(w['coordinates'][0])
            require(F(1,2) < tt < F(1,2)+F(5,2*10**30), 'Witness must be in tiny interval')
        rows.append({'name': name, 'dimension': result['dimension'], 'status': expected,
                     'prefix': result.get('prefix'), 'full_orders': len(successful),
                     'successful_full_orders': sum(successful),
                     'seconds': round(time.monotonic()-t, 6),
                     'cpc_bytes': len(result.get('certificate',{}).get('proof_cpc',''))})
        artifacts[name] = {'input': data, 'result': result}
        print(name, rows[-1]['seconds'], flush=True)

    # The positive case's witnesses are intentionally different. There is no
    # common bad model: r1>=p2 or r2>=p1 whenever p1+p2=7/10.
    q = artifacts['distinct_witnesses']['result']['rejected']
    require(q[0]['witness']['point'] != q[1]['witness']['point'], 'Quantifier witness distinction')

    # Certificate corruption: omit coverage, alter strict witness, alter formula,
    # corrupt CPC bytes, or detach the certificate from its input.
    corruptions = 0
    for name, edit in [
        ('distinct_witnesses', lambda r: r['rejected'].pop()),
        ('distinct_witnesses', lambda r: r['rejected'][0]['witness']['point'].__setitem__(0,'1/2')),
        ('point_tie', lambda r: r['certificate'].__setitem__('query','(check-sat)\n')),
        ('point_tie', lambda r: r['certificate'].__setitem__('proof_cpc','false')),
        ('point_tie', lambda r: r.__setitem__('input_sha256','0'*64)),
        ('point_tie', lambda r: r.__setitem__('order',[0,0,0])),
    ]:
        artifact = artifacts[name]
        r = copy.deepcopy(artifact['result']); edit(r)
        try:
            verify(artifact['input'], r, 30000)
        except ValueError:
            corruptions += 1
        else:
            raise AssertionError('Corrupted certificate accepted')

    invalid = [instance([],['1/2']), instance([['0']],['1/2']),
               instance([['2/3']],['1/2']), instance([['1/2']],['0']),
               {'vertices': [[0.5]], 'r':['1/2'], 'tau':'2/3'},
               instance([['1/5']*3,['2/5','1/5','1/5'],['1/5','2/5','1/5'],['1/5','1/5','2/5']],['1/10']*3)]
    for data in invalid:
        try:
            Domain(data)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid/out-of-scope input accepted')
    receipt = {'evidence': 'exact rational witnesses + two solver decisions; no external proof kernel',
               'python': platform.python_version(), 'system': platform.system(), 'machine': platform.machine(),
               'z3': z3.get_version_string(), 'cvc5': cvc5.__version__,
               'fixtures': rows, 'exhaustive_full_orders': orders,
               'corruption_rejections': corruptions, 'invalid_rejections': len(invalid),
               'seconds': round(time.monotonic()-started, 6),
               'sources': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(Path(__file__).parent.glob('*.py'))}}
    if output:
        output.mkdir(parents=True, exist_ok=True)
        (output/'results.json').write_text(json.dumps(receipt,indent=2)+'\n')
        (output/'certificates.json').write_text(json.dumps(artifacts,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
    return receipt


if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path)
    run(p.parse_args().output)
