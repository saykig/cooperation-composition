# Portable rational certificates for three difficult successes

19 September 2026. Written specialization of weighted AM-GM, with a rational
checker in `experiments/additional_checks.py`. This supplements the general
exact-backend certificate contract; it does not replace it for arbitrary inputs.

Let α be a prefix, a_j nonnegative integers not all zero, and z_i>0 rational.
Define e_i=Σ_{j:i not yet visited at step j} a_j and W=Σ_i e_i. Suppose

    Σ_i e_i p_i/z_i ≤ W              at EVERY input vertex,
    ∏_i z_i^{e_i} ≤ ∏_j r_{α_j}^{a_j}.                       (C)

Then α succeeds on the entire hull. Indeed, the first inequality is linear, so
it holds throughout the hull. For W>0, weighted AM-GM gives

    ∏_i (p_i/z_i)^{e_i} ≤ (Σ_i e_i p_i/(W z_i))^W ≤ 1.

If every prefix inequality were strict, multiplying them with the a_j weights
would give ∏_i p_i^{e_i}>∏_j r_{α_j}^{a_j}, contradicting (C). For W=0, both
products over coordinates are one, and the same contradiction is direct. Thus
the check needs only rational powers, sums and comparisons. The mathematical
trust is the short AM-GM proof and its implementation, not an SMT oracle.

Three explicit certificates (sender numbers in this prose start at 1):

| Fixture | Prefix | Weights a | Relevant center coordinates | Linear support |
|---|---|---|---|---|
| R10 sharp triangle | (1,2,3) | (1,1,1) | z₂=z₃=z₄=4/5 | p₂+2p₃+3p₄=24/5 |
| tangent polygon | (1) | (1) | z₂=z₃=2/5 | p₂+p₃=4/5 |
| R08 changing blocker | (1,2) | (7,3) | z₂=7/20, z₃=2/5 | 20p₂+25p₃=17 |

Each has equality in the product bound. These cover exact zero-margin successes,
including the three-prefix triangle, with solver-free sufficient certificates.
Checking vertices here is sound because the SUPPORT inequality is linear. It is
not the false procedure of testing nonlinear cascade feasibility at vertices.
No completeness or polynomial-size theorem for this rational AM-GM format is
claimed. It is a useful independent audit format, borrowed from ordinary weighted
AM-GM and the existing R09/R10 support-certificate perspective.
