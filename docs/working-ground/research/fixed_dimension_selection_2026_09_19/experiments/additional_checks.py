"""Direct full-order, older Sturm, symmetry and portable AM-GM certificate audit."""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import time
from fixtures import cases
from geometry import Domain
from independent import feasible
from selector import decide, select
from verify import verify, require

ROOT = Path(__file__).resolve().parent


def amgm(data, prefix, weights, center):
    """Rational check of a sufficient weighted AM-GM emptiness certificate.

    No solver or geometry reduction. The proof is in math/CERTIFICATES.md.
    This checker does not claim to find such certificates for every empty set.
    """
    n = len(data['r'])
    require(len(prefix) == len(weights) and len(center) == n, 'AM-GM shape')
    require(len(set(prefix)) == len(prefix) and all(type(i) is int and 0 <= i < n for i in prefix), 'AM-GM prefix')
    require(all(type(a) is int and a >= 0 for a in weights) and any(weights), 'AM-GM weights')
    z = list(map(F, center))
    require(all(v > 0 for v in z), 'AM-GM center')
    e = [sum(a for j, a in enumerate(weights) if h not in prefix[:j+1]) for h in range(n)]
    W = sum(e)
    bound = math.prod(v**k for v, k in zip(z, e))
    threshold = math.prod(F(data['r'][i])**a for i, a in zip(prefix, weights))
    require(bound <= threshold, 'AM-GM product bound')
    for v in data['vertices']:
        require(sum(k*F(p)/zz for k, p, zz in zip(e, v, z)) <= W, 'AM-GM supporting inequality')
    return True


def run(output=None):
    start = time.monotonic()
    spec = importlib.util.spec_from_file_location('r10_sturm', ROOT.parents[1]/'two_prefix_selection_2026_09_19/experiments/selector.py')
    old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
    direct, sturm = 0, 0
    # Recheck retained bundles themselves, not merely freshly generated outputs.
    saved = json.loads((ROOT/'evidence/certificates.json').read_text())
    receipt = json.loads((ROOT/'evidence/results.json').read_text())
    for name, expected in receipt['sources'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Milestone source changed: resolve original identity at 0f94556 before replay')
    for artifact in saved.values():
        verify(artifact['input'], artifact['result'], 30000)
    for name, (data, _, _) in cases().items():
        dom = Domain(data)
        for order in itertools.permutations(range(dom.n)):
            witness, _ = decide(dom, order, 30000)
            require((witness is not None) == feasible(data, order, 30000), 'Direct full-order mismatch '+name)
            direct += 1
            if dom.d <= 1:
                # Choose segment extrema from original vertices, independently of
                # primary basis/halfspace construction.
                endpoints = sorted(data['vertices'], key=lambda v: tuple(map(F,v)))
                sd = {'a':endpoints[0], 'b':endpoints[-1], 'r':data['r'], 'tau':data['tau']}
                gs = old.constraints(sd, order)
                cert = old.decide(gs)
                good = old.verify_sign(gs, cert)
                require(good == (witness is not None), 'Independent Sturm mismatch '+name)
                sturm += 1

    # True polygon with a narrow strict strip: width is controlled algebraically,
    # not inferred from the output's floating-point location.
    narrow = copy.deepcopy(cases()['vertex_miss_polygon'][0])
    eps = F(1,10**30)
    narrow['r'] = [str(F(4,25)-eps**2), '2/5', '1/10']
    w, _ = decide(Domain(narrow), (0,1), 30000)
    require(w is not None and feasible(narrow,(0,1),30000), 'Narrow polygon missed')
    p = list(map(F,w['point']))
    require(F(2,5) < p[2] < F(2,5)+eps, 'Narrow polygon witness outside exact strip')
    # Geometry changes: vertex reversal, redundancy, sender permutation.
    tri = cases()['triangle_three'][0]
    transformations = []
    for perm in ([3,2,1,0], [1,2,3,0]):
        transformed = {'vertices': [[v[i] for i in perm] for v in reversed(tri['vertices'])],
                       'r':[tri['r'][i] for i in perm], 'tau':tri['tau']}
        transformed['vertices'].append(transformed['vertices'][0][:])
        result = select(transformed,30000)
        require(result['status']=='zero' and len(result['prefix'])==3, 'Symmetry/duplicate changed sharpness')
        verify(transformed,result,30000)
        good = []
        for order in itertools.permutations(range(4)):
            a = decide(Domain(transformed),order,30000)[0] is None
            b = not feasible(transformed,order,30000)
            require(a==b,'Transformed full-order mismatch')
            good.append(a)
        require(sum(good)==1,'Transformed unique successful order')
        transformations.append({'permutation':perm, 'full_orders':len(good), 'successful':sum(good)})

    portable = {
        'triangle_three': {'prefix':[0,1,2], 'weights':[1,1,1], 'center':['99/100','4/5','4/5','4/5']},
        'tangent_polygon': {'prefix':[0], 'weights':[1], 'center':['1/2','2/5','2/5']},
        'changing_blocker': {'prefix':[0,1], 'weights':[7,3], 'center':['13/20','7/20','2/5']},
    }
    for name, certificate in portable.items():
        require(amgm(cases()[name][0], **certificate), 'Portable AM-GM certificate')
    bad = copy.deepcopy(portable['triangle_three']); bad['center'][1]='81/100'
    try:
        amgm(tri,**bad)
    except ValueError:
        pass
    else:
        raise AssertionError('Corrupted AM-GM bound accepted')

    report={'evidence':'exact backend replay plus independent Sturm and rational AM-GM certificates',
            'retained_bundles_replayed':len(saved), 'milestone':'0f94556',
            'direct_full_order_comparisons':direct, 'independent_Sturm_comparisons':sturm,
            'narrow_polygon':{'input':narrow, 'prefix':[0,1], 'witness':w},
            'symmetry_comparisons':transformations, 'portable_AMGM_certificates':portable,
            'seconds':round(time.monotonic()-start,6),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if output:
        output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path)
    run(p.parse_args().output)
