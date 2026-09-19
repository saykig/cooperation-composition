"""Exact regression, exhaustive small-order comparisons and portable receipts."""
import copy
from fractions import Fraction as F
from itertools import permutations
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import random
import time
from selector import (constraints, decide, ev, instance, mul, poly, require,
                      select, verify, verify_sign)

HERE = Path(__file__).resolve().parent
counts = {}

def check(ok, label):
    require(ok, label)
    counts[label] = counts.get(label, 0)+1


def data(a, b, r, tau='2/3'):
    return dict(a=list(map(str, a)), b=list(map(str, b)), r=list(map(str, r)), tau=tau)


def full_polys(d, order):
    # Independent backward suffix construction; not constraints(prefix).
    a, b, r = instance(d)
    suffix = (F(1),)
    gs = []
    for i in reversed(order):
        g = list(suffix)
        g[0] -= r[i]
        gs.append(poly(g))
        suffix = mul(suffix, (a[i], b[i]-a[i]))
    return list(reversed(gs))


def compare(d):
    out = select(d)
    check(verify(d, out), 'selector_certificate')
    good = []
    for order in permutations(range(len(d['a']))):
        gs = full_polys(d, order)
        cert = decide(gs)
        fails = verify_sign(gs, cert)
        check(fails == (cert['kind'] == 'witness'), 'full_order_certificate')
        if not fails:
            good.append(order)
    check(bool(good) == (out['status'] == 'success'), 'exhaustive_selection_agreement')
    if good:
        check(tuple(out['order']) in good, 'returned_order_successful')
    return out


def must_reject(d, out, label):
    try:
        verify(d, out)
    except (ValueError, KeyError, TypeError, IndexError, ZeroDivisionError):
        check(True, label)
    else:
        raise ValueError('accepted tampered certificate: '+label)


def main():
    start = time.perf_counter()
    eps = F(1, 10**30)
    fixtures = {
        'midpoint': data(['1/2','1/5','3/5'], ['1/2','3/5','1/5'], ['3/20','1/10','1/10']),
        'changing_blocker_shared_root': data(['13/20','3/5','1/5'], ['13/20','3/80','13/20'], ['7/50','2/5','1/10']),
        'modelwise_success_no_common_order': data(['1/10','3/5'], ['3/5','1/10'], ['2/5','3/10']),
        'tangency': data(['1/2','3/5','1/5'], ['1/2','1/5','3/5'], ['4/25','2/5','1/10']),
        'endpoint_roots': data(['1/2','3/5','1/5'], ['1/2','1/5','3/5'], ['3/25','3/5','1/10']),
        'narrow_interval_large_denominator': data(['1/2','3/5','1/5'], ['1/2','1/5','3/5'], [F(4,25)-eps**2,'2/5','1/10']),
        'degenerate_success_tie': data(['1/2','1/2'], ['1/2','1/2'], ['1/2','1/10']),
        'degenerate_rejection': data(['1/2','1/2'], ['1/2','1/2'], ['1/4','1/4']),
        'constant_coordinate_zero_polynomial': data(['1/5','1/2'], ['3/5','1/2'], ['1/2','1/10']),
        'empty_product_tie': data(['1/5','1/2'], ['3/5','1/2'], ['1/10','1']),
        'one_sender_tie': data(['1/2'], ['1/2'], ['1']),
        'one_sender_cascade': data(['1/3'], ['1/2'], ['1/2']),
    }
    receipts = {}
    for name, d in fixtures.items():
        before = time.perf_counter()
        out = compare(d)
        # JSON roundtrip is part of certificate portability.
        check(verify(d, json.loads(json.dumps(out))), 'json_roundtrip')
        pair = [0, 1] if len(d['a']) > 1 else [0]
        gs = constraints(d, pair)
        pc = decide(gs)
        check(verify_sign(gs, pc) == (pc['kind'] == 'witness'), 'fixture_prefix')
        receipts[name] = dict(input=d, result=out, specified_prefix=pair,
                              prefix_certificate=pc, elapsed_seconds=time.perf_counter()-before)
    check(receipts['midpoint']['result']['status'] == 'rejection', 'preserved_midpoint')
    check(receipts['changing_blocker_shared_root']['result']['status'] == 'success', 'preserved_changing_blocker')
    m = receipts['modelwise_success_no_common_order']
    check(m['result']['status'] == 'rejection', 'preserved_quantifiers')
    check(len({e['certificate']['t'] for e in m['result']['pairs']}) == 2, 'different_pair_witnesses')
    narrow = receipts['narrow_interval_large_denominator']['prefix_certificate']
    check(narrow['kind'] == 'witness', 'narrow_not_missed')
    t = F(narrow['t'])
    check(F(1,2) < t < F(1,2)+5*eps/2, 'narrow_exact_witness_bound')
    check(receipts['tangency']['prefix_certificate']['kind'] == 'sign_cover', 'tangent_zero_is_blocker')

    # Scalar sign-oracle stress cases not all arising as product-minus-cost.
    # Their scope is explicitly algebraic, not new strategic examples.
    algebraic = [([(0,), (1,)], False), ([(1,), (2,)], True),
                 ([(-F(1,4),1,-1), (1,)], False),
                 ([(0,1), (1,-1)], True),
                 ([(0,0,1), (0,1)], True),
                 ([(0,1), (0,-1)], False),
                 ([(-eps,1), (2*eps,-1)], True),
                 ([(F(1,4),-1,1), (-F(1,4),1,-1)], False)]
    for gs, answer in algebraic:
        c = decide(gs)
        check(verify_sign(gs,c) == answer, 'algebraic_sign_stress')

    rng = random.Random(19092027)
    for n, repetitions in [(2,30),(3,35),(4,15),(5,3),(6,1)]:
        for _ in range(repetitions):
            a = [F(rng.randrange(1,13),20) for i in range(n)]
            b = [F(rng.randrange(1,13),20) for i in range(n)]
            r = [F(rng.randrange(1,16),100) for i in range(n)]
            compare(data(a,b,r))

    # Independent historical quadratic interval oracle for n=3.
    oldpath = HERE.parents[1]/'robust_order_polytope_2026_09_19/experiments/explore.py'
    spec = importlib.util.spec_from_file_location('r09_explore', oldpath)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    for _ in range(40):
        a = tuple(F(rng.randrange(1,13),20) for i in range(3))
        b = tuple(F(rng.randrange(1,13),20) for i in range(3))
        r = tuple(F(rng.randrange(1,16),50) for i in range(3))
        for order in permutations(range(3)):
            d = data(a,b,r)
            actual = decide(full_polys(d,order))['kind'] == 'witness'
            check(actual == old.segment_bad(a,b,r,order), 'independent_quadratic_oracle')

    d = fixtures['modelwise_success_no_common_order']
    out = select(d)
    bad = copy.deepcopy(out); bad['pairs'].pop()
    must_reject(d,bad,'reject_missing_pair')
    bad = copy.deepcopy(out); bad['pairs'][0]['certificate']['t'] = '1'
    must_reject(d,bad,'reject_wrong_witness')
    d = fixtures['changing_blocker_shared_root']
    out = select(d)
    bad = copy.deepcopy(out); bad['order'] = [0,0,0]
    must_reject(d,bad,'reject_wrong_order')
    # Mutate a sign-cover certificate directly; verifier must reject.
    gs = constraints(d,[0,1]); c = decide(gs)
    for label, mutate in [('missing_root', lambda x: x['root_intervals'].pop()),
                          ('false_sign', lambda x: x['signs'][0].__setitem__(0, 1)),
                          ('missing_sample', lambda x: x['samples'].pop())]:
        bad = copy.deepcopy(c); mutate(bad)
        try:
            verify_sign(gs,bad)
        except ValueError:
            check(True,'reject_'+label)
        else:
            raise ValueError('accepted '+label)
    report = dict(status='passed', counts=counts, total_checks=sum(counts.values()),
                  fixtures=receipts, python=platform.python_version(),
                  elapsed_seconds=time.perf_counter()-start,
                  source_sha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in [HERE/'selector.py',HERE/'check.py',oldpath]},
                  scope='Exact checks; not formal verification or performance complexity proof.')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
