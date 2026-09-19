"""Separate barycentric encoding, backward suffix recursion, cvc5 coverings.

Does not import primary geometry or formula builder. The solver's covering
lemmas remain trusted: CPC output may contain `trust` steps. This is exact
independent solver replay, NOT a small-kernel formal proof.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import cvc5


def build(data, prefix, timeout=0, proofs=False):
    s = cvc5.Solver()
    s.setLogic('QF_NRA')
    s.setOption('nl-cov-force', 'true')
    if timeout:
        s.setOption('tlimit-per', str(timeout))
    if proofs:
        s.setOption('produce-proofs', 'true')
        s.setOption('check-proofs', 'true')
        s.setOption('proof-check', 'eager')
    K = cvc5.Kind
    real = lambda x: s.mkReal(str(F(x)))
    add = lambda xs: real(0) if not xs else xs[0] if len(xs) == 1 else s.mkTerm(K.ADD, *xs)
    mul = lambda a, b: s.mkTerm(K.MULT, a, b)
    vertices = data['vertices']
    variables = [s.mkConst(s.getRealSort(), 'w'+str(i)) for i in range(len(vertices)-1)]
    weights = variables + [s.mkTerm(K.SUB, real(1), add(variables))]
    assertions = [s.mkTerm(K.GEQ, w, real(0)) for w in weights]
    n = len(data['r'])
    p = [add([mul(w, real(v[i])) for w, v in zip(weights, vertices)]) for i in range(n)]
    order = list(prefix)+[i for i in range(n) if i not in prefix]
    tail = real(1)
    inequalities = []
    for position in range(n-1, -1, -1):
        i = order[position]
        if position < len(prefix):
            inequalities.append(s.mkTerm(K.GT, tail, real(data['r'][i])))
        tail = mul(p[i], tail)
    assertions.extend(reversed(inequalities))
    for a in assertions:
        s.assertFormula(a)
    query = '(set-logic QF_NRA)\n' + ''.join('(declare-const '+str(w)+' Real)\n' for w in variables)
    query += ''.join('(assert '+str(a)+')\n' for a in assertions)+'(check-sat)\n'
    return s, query


def feasible(data, prefix, timeout=0):
    s, _ = build(data, prefix, timeout)
    answer = s.checkSat()
    if answer.isUnknown():
        raise RuntimeError('Incomplete cvc5 decision: '+str(answer))
    return answer.isSat()


def emptiness_certificate(data, prefix, timeout=0):
    s, query = build(data, prefix, timeout, proofs=True)
    result = s.checkSat()
    if not result.isUnsat():
        raise RuntimeError('Independent emptiness check failed: '+str(result))
    proof = s.getProof()[0]
    stack, seen, counts = [proof], set(), Counter()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        counts[str(node.getRule())] += 1
        stack.extend(node.getChildren())
    cpc = s.proofToString(proof).decode()
    return {'kind': 'exact-backend-emptiness', 'cvc5_version': cvc5.__version__,
            'query': query, 'proof_cpc': cpc,
            'proof_sha256': hashlib.sha256(cpc.encode()).hexdigest(),
            'rules': dict(sorted(counts.items())),
            'trust': 'cvc5 covering leaves; no external CPC kernel replay; independent Z3 decision'}
