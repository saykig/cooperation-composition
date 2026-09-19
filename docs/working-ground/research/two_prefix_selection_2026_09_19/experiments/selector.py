"""Exact rational-segment selector. Standard library only; sender indices start at 0.
Certificates are portable JSON. verify() does not rerun selection or isolation.
"""
from fractions import Fraction as F
from itertools import permutations
import json
import sys


def require(ok, message='invalid certificate'):
    if not ok:
        raise ValueError(message)


def poly(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p or [F(0)])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return poly(out)


def ev(p, x):
    out = F(0)
    for c in reversed(p):
        out = out*x+c
    return out


def divrem(p, q):
    require(q != (0,), 'division by zero')
    a = list(p)
    out = [F(0)] * max(1, len(p)-len(q)+1)
    while len(a) >= len(q) and a != [0]:
        k = len(a)-len(q)
        c = a[-1]/q[-1]
        out[k] = c
        for j in range(len(q)):
            a[k+j] -= c*q[j]
        a = list(poly(a))
    return poly(out), poly(a)


def deriv(p):
    return poly([i*p[i] for i in range(1, len(p))])


def monic(p):
    return poly([x/p[-1] for x in p]) if p != (0,) else p


def gcd(p, q):
    while q != (0,):
        p, q = q, divrem(p, q)[1]
    return monic(p)


def root_poly(gs):
    h = (F(1),)
    for g in gs:
        if len(g) > 1:
            h = mul(h, g)
    if len(h) > 1:
        h = monic(divrem(h, gcd(h, deriv(h)))[0])
        for x in (F(0), F(1)):
            if ev(h, x) == 0:
                h = divrem(h, (-x, F(1)))[0]
    return monic(h)


def sturm(h):
    if len(h) == 1:
        return [h]
    seq = [h, deriv(h)]
    while True:
        rem = divrem(seq[-2], seq[-1])[1]
        if rem == (0,):
            return seq
        # Positive scaling controls coefficient growth without changing signs.
        seq.append(poly([-c/abs(rem[-1]) for c in rem]))


def variation(seq, x):
    signs = [1 if v > 0 else -1 for p in seq if (v := ev(p, x)) != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def count(seq, a, b):
    return variation(seq, a)-variation(seq, b)


def isolate(h):
    """Sturm subdivision, nonroot rational cuts; no floating point/grid tests."""
    seq = sturm(h)
    stack = [(F(0), F(1))]
    intervals = []
    while stack:
        a, b = stack.pop()
        n = count(seq, a, b)
        if n == 0:
            continue
        if n == 1 and a > 0 and b < 1:
            intervals.append((a, b))
            continue
        # At most degree(h) of these distinct cuts can be roots.
        for m in range(2, len(h)+3):
            c = a+(b-a)/m
            if ev(h, c) != 0:
                break
        else:
            raise ArithmeticError('nonroot cut not found')
        stack.extend([(c, b), (a, c)])
    return sorted(intervals)


def signs(gs, t):
    return [int(v > 0)-int(v < 0) for g in gs for v in [ev(g, t)]]


def decide(gs):
    """Decide whether all gs can be STRICTLY positive on [0,1]."""
    gs = list(map(poly, gs))
    for i, g in enumerate(gs):
        if len(g) == 1 and g[0] <= 0:
            return {'kind': 'constant_blocker', 'index': i}
    h = root_poly(gs)
    intervals = isolate(h)
    samples = ([F(1, 2)] if not intervals else
               [intervals[0][0]/2] +
               [(u[1]+v[0])/2 for u, v in zip(intervals, intervals[1:])] +
               [(intervals[-1][1]+1)/2])
    ss = [signs(gs, t) for t in samples]
    for t, s in zip(samples, ss):
        if all(v > 0 for v in s):
            return {'kind': 'witness', 't': str(t)}
    return {'kind': 'sign_cover',
            'root_intervals': [[str(a), str(b)] for a, b in intervals],
            'samples': [str(t) for t in samples], 'signs': ss}


def verify_sign(gs, cert):
    """Check certificate; returns True for feasible strict conjunction."""
    gs = list(map(poly, gs))
    kind = cert['kind']
    if kind == 'witness':
        t = F(cert['t'])
        require(0 <= t <= 1 and all(ev(g, t) > 0 for g in gs))
        return True
    if kind == 'constant_blocker':
        i = cert['index']
        require(type(i) is int and 0 <= i < len(gs))
        require(len(gs[i]) == 1 and gs[i][0] <= 0)
        return False
    require(kind == 'sign_cover')
    require(all(not (len(g) == 1 and g[0] <= 0) for g in gs))
    h = root_poly(gs)
    seq = sturm(h)
    ivs = [(F(a), F(b)) for a, b in cert['root_intervals']]
    for a, b in ivs:
        require(0 < a < b < 1 and ev(h, a) != 0 and ev(h, b) != 0)
        require(count(seq, a, b) == 1)
    require(all(a[1] <= b[0] for a, b in zip(ivs, ivs[1:])))
    require(len(ivs) == count(seq, F(0), F(1)))
    ts = list(map(F, cert['samples']))
    require(len(ts) == len(ivs)+1)
    # Samples provably cover ALL complementary root cells, not a sampled grid.
    for i, t in enumerate(ts):
        lo = ivs[i-1][1] if i else F(0)
        hi = ivs[i][0] if i < len(ivs) else F(1)
        require(lo <= t <= hi and 0 < t < 1 and ev(h, t) != 0)
    actual = [signs(gs, t) for t in ts]
    require(actual == cert['signs'])
    require(all(not all(s > 0 for s in row) for row in actual))
    # Roots of h kill strictness; omitted roots at 0/1 do too. If an endpoint
    # were strictly feasible, continuity would make an adjacent cell feasible.
    return False


def instance(data):
    a, b, r = (tuple(F(x) for x in data[key]) for key in ('a', 'b', 'r'))
    tau = F(data.get('tau', '2/3'))
    require(len(a) == len(b) == len(r) and len(a) >= 1, 'dimension mismatch')
    require(0 < tau < 1 and all(0 < x < tau for x in a+b), 'probability bounds')
    require(all(x > 0 for x in r), 'positive costs required')
    return a, b, r


def constraints(data, prefix):
    a, b, r = instance(data)
    n = len(a)
    require(len(set(prefix)) == len(prefix) and all(type(i) is int and 0 <= i < n for i in prefix))
    remaining = set(range(n))
    gs = []
    for i in prefix:
        remaining.remove(i)
        g = (F(1),)
        for j in sorted(remaining):
            g = mul(g, (a[j], b[j]-a[j]))
        g = list(g)
        g[0] -= r[i]
        gs.append(poly(g))
    return gs


def candidates(n):
    return [(0,)] if n == 1 else list(permutations(range(n), 2))


def select(data):
    n = len(instance(data)[0])
    rejected = []
    for prefix in candidates(n):
        cert = decide(constraints(data, prefix))
        if cert['kind'] != 'witness':
            return {'status': 'success', 'prefix': list(prefix),
                    'order': list(prefix)+[i for i in range(n) if i not in prefix],
                    'certificate': cert}
        rejected.append({'prefix': list(prefix), 'certificate': cert})
    return {'status': 'rejection', 'pairs': rejected}


def verify(data, result):
    n = len(instance(data)[0])
    if result['status'] == 'success':
        prefix, order = result['prefix'], result['order']
        require(tuple(prefix) in candidates(n))
        require(order[:len(prefix)] == prefix and sorted(order) == list(range(n)))
        require(not verify_sign(constraints(data, prefix), result['certificate']))
    else:
        require(result['status'] == 'rejection')
        entries = result['pairs']
        require([tuple(e['prefix']) for e in entries] == candidates(n))
        for e in entries:
            require(verify_sign(constraints(data, e['prefix']), e['certificate']))
    return True


if __name__ == '__main__':
    # python selector.py input.json [certificate.json]
    with open(sys.argv[1]) as f:
        data = json.load(f)
    if len(sys.argv) == 3:
        with open(sys.argv[2]) as f:
            result = json.load(f)
        verify(data, result)
        print('certificate verified')
    else:
        result = select(data)
        verify(data, result)
        print(json.dumps(result, indent=2))
