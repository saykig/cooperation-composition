"""Exact replay of the two bounded sharpness refinements; no external packages."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import prod
import hashlib
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def improved_witness(m, prefix):
    C = F(m * (m + 1), 2)
    kappa = epsilon = 1 / (2 * m * (C + 1))
    q = 1 - epsilon
    tau = 1 - epsilon * kappa / 2
    raw = [F(0)] * m
    if prefix[0] != 0:
        raw[prefix[0] - 1] = C / prefix[0]
    else:
        last = 0
        for i in prefix[1:]:
            if i > last:
                raw[i - 1] = F(i - last)
                last = i
        if last < m:
            raw[m - 1] = F(m - last)
        W = sum((i + 1) * x for i, x in enumerate(raw))
        require(W >= C + 1, 'record surplus')
        raw = [C * x / W for x in raw]
    x = [(1 - kappa) * y + kappa for y in raw]
    p = [1 - epsilon * kappa] + [1 - epsilon * y for y in x]
    r = [q ** (m - i) for i in range(m)] + [q ** (m + 1)]
    require(sum((i + 1) * y for i, y in enumerate(x)) == C, 'deficit slice')
    require(sum(i * p[i] for i in range(1, m + 1)) == q * C, 'probability slice')
    require(all(kappa <= y <= C for y in x), 'deficit bounds')
    require(all(0 < y < tau for y in p), 'admissible probabilities')
    remaining = set(range(m + 1))
    for i in prefix:
        remaining.remove(i)
        h = m - i if i < m else m + 1
        S = sum(kappa if j == 0 else x[j - 1] for j in remaining)
        require(h - S >= F(h, 2) / (C + 1), 'step-dependent linear slack')
        margin = prod(p[j] for j in remaining) - r[i]
        require(margin >= epsilon * h / (4 * (C + 1)), 'quantitative strict margin')


def threshold_predicate(m, tau):
    C = F(m * (m + 1), 2)
    return tau ** (m - 1) * C > C - (m - 1)


def threshold_replay(m):
    C = F(m * (m + 1), 2)
    i = m - 1
    lo, hi = F(0), F(1)
    for _ in range(20):
        mid = (lo + hi) / 2
        if threshold_predicate(m, mid):
            hi = mid
        else:
            lo = mid
    require(not threshold_predicate(m, lo), 'lower rational obstruction')
    require(threshold_predicate(m, hi), 'upper rational possibility')
    tau = hi
    p0_lower = (C - i) / (C * tau ** (m - 2))
    p0 = (p0_lower + tau) / 2
    require(0 < p0 < tau, 'fixed coordinate')
    q = tau * (C - i) / C
    delta = min(tau / 2, tau * i / (2 * (C - i)))
    halvings = 0
    while p0 * (tau - delta) ** (m - 1) <= q:
        delta /= 2
        halvings += 1
        require(halvings < 200, 'construction replay cap, not decision oracle')
    p = [p0] + [tau - delta] * m
    p[i] = delta * (C - i) / i
    require(all(0 < value < tau for value in p), 'threshold witness bounds')
    require(sum(j * p[j] for j in range(1, m + 1)) == q * C, 'threshold witness slice')
    require(prod(p[j] for j in range(m + 1) if j != i) > q, 'strict singleton witness')
    return {'m': m, 'tau_below': str(lo), 'tau_above': str(hi), 'delta_halvings': halvings}


def main():
    exhaustive = 0
    for m in range(2, 7):
        for prefix in permutations(range(m + 1), m - 1):
            improved_witness(m, prefix)
            exhaustive += 1
    larger = 0
    for m in (8, 12, 20, 40, 80):
        controls = [tuple(range(m - 1)), tuple(range(1, m)),
                    tuple([0] + list(range(m, 2, -1))),
                    tuple(range(m, 1, -1))]
        for prefix in controls:
            require(len(prefix) == m - 1, 'prefix length')
            improved_witness(m, prefix)
            larger += 1
    threshold = [threshold_replay(m) for m in range(2, 31)]
    result = {
        'status': 'passed exact rational replay',
        'scope': 'finite support for written S1/S2 proofs, not formal verification',
        'exhaustive_prefix_checks': exhaustive,
        'exhaustive_m_range': [2, 6],
        'larger_structured_prefix_checks': larger,
        'larger_m_values': [8, 12, 20, 40, 80],
        'threshold_boundary_checks': threshold,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
