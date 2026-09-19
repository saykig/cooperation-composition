"""Replay certificates, explicitly trusting exact solvers for emptiness only.

Rejection is checked with Fraction arithmetic and convex weights, without SMT.
Success rebuilds both formulas and repeats two exact decisions. CPC text is an
auditable proof skeleton, not a replacement for those trusted decisions.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def witness(data, prefix, record):
    vertices = [[F(x) for x in v] for v in data['vertices']]
    p = [F(x) for x in record['point']]
    n = len(data['r'])
    require(len(p) == n, 'Witness dimension')
    total, combination, ids = F(0), [F(0)]*n, set()
    for item in record['weights']:
        i, w = item['vertex'], F(item['weight'])
        require(type(i) is int and 0 <= i < len(vertices) and i not in ids, 'Vertex index')
        require(w >= 0, 'Negative convex weight')
        ids.add(i)
        total += w
        combination = [a+w*b for a, b in zip(combination, vertices[i])]
    require(total == 1 and combination == p, 'Witness outside stated convex hull')
    for j, i in enumerate(prefix):
        remaining = [p[h] for h in range(n) if h not in prefix[:j+1]]
        require(math.prod(remaining) > F(data['r'][i]), 'Cascade is not strict')


def verify(data, result, timeout=0):
    from geometry import Domain
    from selector import digest, formula
    dom = Domain(data)
    require(result['schema'] == 1 and result['input_sha256'] == digest(data), 'Input binding')
    require(result['dimension'] == dom.d, 'Affine dimension')
    if result['status'] == 'positive':
        limit = min(dom.d+1, max(1, dom.n-1))
        expected = {a for k in range(1, limit+1)
                    for a in itertools.permutations(range(dom.n), k)}
        seen = set()
        for entry in result['rejected']:
            prefix = tuple(entry['prefix'])
            require(prefix in expected and prefix not in seen, 'Candidate prefix coverage')
            witness(data, prefix, entry['witness'])
            seen.add(prefix)
        require(seen == expected and result['fine'] == 'B', 'Missing rejected prefix')
        return {'accepted': True, 'kind': 'rational-witnesses', 'prefixes': len(seen)}
    require(result['status'] == 'zero', 'Unknown result status')
    prefix, order = result['prefix'], result['order']
    require(prefix and len(set(prefix)) == len(prefix)
            and all(type(i) is int and 0 <= i < dom.n for i in prefix), 'Malformed prefix')
    require(sorted(order) == list(range(dom.n)) and order[:len(prefix)] == prefix, 'Order completion')
    cert = result['certificate']
    require(cert['kind'] == 'exact-backend-emptiness', 'Certificate kind')
    require(hashlib.sha256(cert['proof_cpc'].encode()).hexdigest() == cert['proof_sha256'], 'CPC integrity')
    import z3
    from independent import build
    s, query = build(data, prefix, timeout, proofs=True)
    require(query == cert['query'], 'Independent formula binding')
    require(s.checkSat().isUnsat(), 'Independent exact emptiness replay failed')
    # check-proofs=eager/lazy checks the regenerated proof, except trusted leaves.
    s.getProof()
    z = z3.SolverFor('QF_NRA')
    if timeout:
        z.set(timeout=timeout)
    z.add(*formula(dom, prefix)[1])
    require('(set-logic QF_NRA)\n'+z.sexpr()+'\n(check-sat)\n' == result['z3_query'], 'Primary formula binding')
    require(z.check() == z3.unsat, 'Primary exact emptiness replay failed')
    return {'accepted': True, 'kind': 'two-exact-backend-replay',
            'formal_kernel': False, 'saved_CPC': 'integrity checked; proof skeleton retained for audit'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('instance', type=Path)
    p.add_argument('certificate', type=Path)
    p.add_argument('--timeout-ms', type=int, default=0)
    a = p.parse_args()
    print(json.dumps(verify(json.loads(a.instance.read_text()),
                            json.loads(a.certificate.read_text()), a.timeout_ms), indent=2))
