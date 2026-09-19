# Sources and novelty boundary

Inspected 19 September 2026. This is a bounded construction gate, not a new broad
novelty survey. The earlier signaling, hard-evidence, robust optimization, Helly
and exact-root sources remain in R08–R10 and were not treated as new discoveries.

## Numerical candidate generation

- [SciPy 1.13.1 SLSQP documentation](https://docs.scipy.org/doc/scipy-1.13.1/reference/optimize.minimize-slsqp.html)
  was inspected for the actual optimizer used. It documents scalar minimization,
  stopping tolerance and iterations. Our code supplies analytical derivatives.
  A successful numerical status is retained as numerical evidence, not a proof.
- [SciPy 1.13.1 HiGHS linear-programming documentation](https://docs.scipy.org/doc/scipy-1.13.1/reference/optimize.linprog-highs.html)
  was inspected for the dual-weight search. It specifies objective/constraint
  signs, bounds and result fields. We do not trust floating-point marginals as
  exact dual certificates: weights are rationalized and the resulting support
  bound is recomputed exactly.

## Borrowed elementary mathematics

Concavity of logarithm supplies its supporting affine upper bound. The support
problem is a continuous knapsack problem, solved by budget exchanges between
ratios. Weighted AM-GM supplies the universal successful-prefix bound. The
logarithm's atanh series with a geometric tail bound supplies rational enclosing
intervals. Bernoulli/product and second-order Taylor inequalities turn linear
deficit slack into a strict multiplicative margin. These are established facts;
short derivations needed for the certificates are given in the mathematical notes.

The Boyd–Vandenberghe author site and indexed convexity materials were found, but
fetches of the book slides and EE364A convex-functions PDF timed out. We do NOT
claim to have inspected their full text in this gate or use a failed fetch as
source verification. The local certificate argument is self-contained.

## Relation to prior results

R10's finite Helly/move-to-front theorem provides the d+1 UPPER bound. This phase
constructs instances attaining it; it does not prove a new Helly theorem. The
key construction uses running maxima of a prefix to form consecutive blocks,
with the elementary identity

    Σ b_l(b_l−b_{l−1}) = m(m+1)/2 + Σ Δ_l(Δ_l−1)/2.

The surplus from at least one skipped label supplies room for all required strict
inequalities. No new terminology is needed for this identity. Its use in this
particular robust-disclosure construction has not been checked for historical
priority. The theorem is a locally developed written proof, not an established
novelty claim, independent external replay or Lean theorem.

The fixed-threshold obstruction concerns the SPECIAL uniform-AM-GM/geometric-cost
family. It cannot be imported into arbitrary games or arbitrary constrained
probability families. R08 already supplies a counterexample to such an overreach.

Sharpness is a lower bound on the length of an existence certificate within the
game. It is not an NP-hardness reduction or a lower bound on running time. The next
algorithmic question remains exact selection beyond rational segments.
