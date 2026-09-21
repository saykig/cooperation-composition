"""Exact finite fidelity checks: R14 definitions versus R13's recursive game.

This is computational model-translation evidence, not the arbitrary-n Lean proof.
No Z3 dependency: only the independent primitive game module is imported.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT.parent / 'game_cascade_audit_2026_09_19/experiments/game.py'
spec = importlib.util.spec_from_file_location('r13_primitive_game', GAME)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Game = module.Game


def check(ok, message):
    if not ok:
        raise ValueError(message)


def posterior(g, q, h, own=None):
    coords = list(g.p)
    for j, a in enumerate(h):
        i = g.order[j]
        coords[i] = F(1) if a else g.p[i] * (1-q[h[:j]]) / (1-g.p[i]*q[h[:j]])
    if own is not None:
        coords[g.order[len(h)]] = F(own)
    return {x: math.prod(p if b else 1-p for p, b in zip(coords, x)) for x in g.states}


def weight(g, q, h, a, x, y):
    j = len(h)
    if y[:j] != h or y[j] != a:
        return F(0)
    out = F(1)
    for t in range(j+1, g.n):
        if x[g.order[t]]:
            out *= q[y[:t]] if y[t] else 1-q[y[:t]]
        elif y[t]:
            return F(0)
    return out


def payoff(g, q, rho, h, a):
    mu = posterior(g, q, h, 1)
    expected = sum(mu[x] * sum(weight(g, q, h, a, x, y)*rho[y] for y in g.terminals)
                   for x in g.states)
    i = g.order[len(h)]
    return g.eta[i]*expected - (g.k[i] if a else 0)


def main():
    counts = dict(profiles=0, posterior_comparisons=0, normalized_kernels=0,
                  path_expectation_comparisons=0, sender_gain_comparisons=0,
                  cascade_gain_comparisons=0)
    for n in range(1, 5):
        orders = sorted({tuple(range(n)), tuple(reversed(range(n)))})
        for order in orders:
            g = Game([F(i+1, n+3) for i in range(n)],
                     [F(i+1, 7) for i in range(n)],
                     [F(i+2, 3) for i in range(n)], A=3, B=1, order=order)
            for mode in range(4):
                q = {h: (F(mode) if mode < 2 else
                         F((3*sum(h)+len(h)+mode) % 5, 4)) for h in g.nodes}
                counts['profiles'] += 1
                for h in g.nodes + g.terminals:
                    own_options = (None, 0, 1) if h in q else (None,)
                    for own in own_options:
                        got = posterior(g, q, h, own)
                        # Different perturbation exponents at different information sets.
                        expected = g.belief(q, h, own=own,
                            powers={node: 1+(len(node)+sum(node)) % 3 for node in g.nodes})
                        check(all(got[x] == expected.get(x, 0) for x in g.states), 'Bayes limit mismatch')
                        counts['posterior_comparisons'] += 1
                rhos = [{y: F(all(y)) for y in g.terminals},
                        {y: F((sum(y)+2*y[0]) % 4, 3) for y in g.terminals}]
                for h in g.nodes:
                    for x in g.states:
                        for a in (0, 1):
                            masses = {y: weight(g, q, h, a, x, y) for y in g.terminals}
                            check(sum(masses.values()) == 1 and min(masses.values()) >= 0, 'Kernel failure')
                            counts['normalized_kernels'] += 1
                            for rho in rhos:
                                value = sum(masses[y]*rho[y] for y in g.terminals)
                                check(value == g.d_probability(x, h+(a,), q, rho), 'Recursive tree mismatch')
                                counts['path_expectation_comparisons'] += 1
                    for rho in rhos:
                        gain = payoff(g, q, rho, h, 1)-payoff(g, q, rho, h, 0)
                        check(gain == g.sender_gain(q, rho, h), 'Primitive sender gain mismatch')
                        counts['sender_gain_comparisons'] += 1
                    i = g.order[len(h)]
                    cascade = -g.k[i] if not all(h) else (
                        g.eta[i]*math.prod(g.p[g.order[t]]*q[(1,)*t] for t in range(len(h)+1, n))-g.k[i])
                    check(cascade == g.sender_gain(q, rhos[0], h), 'Derived cascade mismatch')
                    counts['cascade_gain_comparisons'] += 1
    files = [Path(__file__), GAME] + sorted((ROOT / 'lean').glob('*.lean'))
    identities = {('R13/game.py' if p == GAME else str(p.relative_to(ROOT))):
                  hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    print(json.dumps(dict(status='exact finite model-fidelity checks passed', counts=counts,
                         source_sha256=identities,
                         limits='Designed profiles at n=1..4; not exhaustive over behavioral profiles or a proof for arbitrary n.'),
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
