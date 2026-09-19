"""Exact NLSAT prefix selector; emptiness requires independent cvc5 replay.

Rational witnesses have solver-free checkers. Emptiness certificates contain a
CPC proof skeleton, and explicitly retain solver trust for its covering leaves.
No unknown/timeout can become a mathematical answer. Sender indices are 0-based.
"""
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import z3
from geometry import Domain


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def prefixes(n, d):
    for k in range(1, min(d+1, max(1, n-1))+1):
        yield from itertools.permutations(range(n), k)


def margins(p, r, prefix):
    remaining = set(range(len(p)))
    out = []
    for i in prefix:
        remaining.remove(i)
        out.append(math.prod(p[j] for j in sorted(remaining))-r[i])
    return out


def formula(domain, prefix):
    x = [z3.Real('x'+str(i)) for i in range(domain.d)]
    q = lambda v: z3.RealVal(str(v))
    p = [q(b)+sum(q(c[i])*t for c, t in zip(domain.basis, x))
         for i, b in enumerate(domain.base)]
    conditions = [q(f[0])+sum(q(a)*t for a, t in zip(f[1:], x)) > 0
                  for f in domain.facets]
    remaining = set(range(domain.n))
    for i in prefix:
        remaining.remove(i)
        product = z3.RealVal(1)
        for j in sorted(remaining):
            product *= p[j]
        conditions.append(product > q(domain.r[i]))
    return x, conditions


def decide(domain, prefix, timeout=0):
    x, conditions = formula(domain, prefix)
    solver = z3.SolverFor('QF_NRA')
    if timeout:
        solver.set(timeout=timeout)
    solver.add(*conditions)
    query = '(set-logic QF_NRA)\n'+solver.sexpr()+'\n(check-sat)\n'
    result = solver.check()
    if result == z3.unknown:
        raise RuntimeError('Incomplete Z3 decision: '+solver.reason_unknown())
    if result == z3.unsat:
        return None, query
    values = [solver.model().eval(t, model_completion=True) for t in x]
    precision = 8
    while True:
        t = []
        for a in values:
            v = a.approx(precision) if z3.is_algebraic_value(a) else a
            t.append(F(v.numerator_as_long(), v.denominator_as_long()))
        if domain.contains(t, strict=True) and all(v > 0 for v in margins(domain.point(t), domain.r, prefix)):
            return {'coordinates': list(map(str, t)),
                    'point': list(map(str, domain.point(t))),
                    'weights': domain.weights(t)}, query
        precision *= 2  # open strict solution set ensures eventual rational witness


def select(data, timeout=0):
    from independent import emptiness_certificate
    dom = Domain(data)
    rejected = []
    for prefix in prefixes(dom.n, dom.d):
        witness, query = decide(dom, prefix, timeout)
        if witness is None:
            certificate = emptiness_certificate(data, prefix, timeout)
            return {'schema': 1, 'input_sha256': digest(data), 'dimension': dom.d,
                    'status': 'zero', 'prefix': list(prefix),
                    'order': list(prefix)+[i for i in range(dom.n) if i not in prefix],
                    'certificate': certificate, 'z3_query': query,
                    'rejected_before_success': rejected, 'z3_version': z3.get_version_string()}
        rejected.append({'prefix': list(prefix), 'witness': witness})
    return {'schema': 1, 'input_sha256': digest(data), 'dimension': dom.d,
            'status': 'positive', 'fine': 'B', 'rejected': rejected,
            'z3_version': z3.get_version_string()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('instance', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--timeout-ms', type=int, default=0)
    args = parser.parse_args()
    result = select(json.loads(args.instance.read_text()), args.timeout_ms)
    text = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
