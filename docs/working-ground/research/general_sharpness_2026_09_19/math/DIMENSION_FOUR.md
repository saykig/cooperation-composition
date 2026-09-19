# Resolution of all twenty dimension-four prefixes

19 September 2026. The historical receipt at R10 commit `807791b` is preserved.
Its twenty missing prefixes all begin with zero-based sender 0 (sender 1 in the
mathematical notes). They were missing search witnesses, not proved obstructions.

## The optimization problem

Keep the EXACT previous construction parameters:

    m=5, n=6, q=4/5, p0=999/1000, τ=9999/10000,
    r_i=q^(5−i) for 0≤i<5, r_5=1/1000,
    p1+2p2+3p3+4p4+5p5=12,      0<p_i<τ.

For each recorded prefix α of length four maximize

    min_j f_j(p),   f_j(p)=log(product_{k not in α[:j+1]} p_k/r_{α_j}).

Equivalently maximize t subject to t≤f_j(p), the affine equation and bounds.
Every f_j is concave, so this is convex optimization in the standard sense.
The strict upper box is open: “optimal margin” means its SUPREMUM. Numerical
optimization uses the closed upper cap. Blending a candidate with the uniform
point q moves it strictly inside without changing the affine equation. The
certified upper bound below applies to the entire original slice, independent
of optimizer convergence and its small numerical lower bound on probabilities.

SLSQP locates a candidate; four coordinates are rationalized and the fifth is
solved from the affine equation EXACTLY. Rational products then certify every
strict cascade inequality. All twenty candidates pass. No rational witness is
certified by solver status or a sampled parameter grid.

## Certified optimal-margin brackets

For a positive rational candidate z and rational weights λ_j≥0 summing to one,
concavity gives, for every admissible p,

    min_j f_j(p) ≤ Σ_j λ_j f_j(p)
                 ≤ Σ_j λ_j f_j(z) + g·(p−z),

where g_i=Σ_{j: i remains after j} λ_j/z_i for variable i=1,...,5.
The fixed p0 contributes no derivative. Maximize g·p over the CLOSED linear slice
0≤p_i≤τ, Σ i p_i=12. This is continuous knapsack: allocate the weighted budget in
decreasing order of g_i/i, stopping at each cap. The exact rational optimum gives
a valid upper bound on the true margin supremum. Optimality of this greedy linear
support calculation follows by exchanging budget from a lower ratio to a higher
one until at least one bound becomes tight.

Weights are located by a small numerical dual LP and then made rational. They
need only be nonnegative and sum to one for the proof; numerical dual optimality
is not trusted. A lower bound is min_j f_j(z). Logarithms are enclosed rationally
using x=2^k y, 1≤y<2, and

    log y = 2 Σ_{l≥0} u^(2l+1)/(2l+1),   u=(y−1)/(y+1)∈[0,1/3).

After N terms the omitted positive remainder is at most
2u^(2N+1)/((2N+1)(1−u²)). The same series bounds log 2. Signs of k are handled by
interval multiplication; all rounding is outward and rational. Thus both ends of
each recorded bracket, including the small gap, are proved bounds—not floating
point confidence estimates.

## Individual outcomes

Labels here are one-based; JSON uses zero-based labels. Values below are readable
decimal displays of the exact rational bounds retained in the receipt.

| Prefix | Lower bound | Upper bound |
|---|---:|---:|
| 1,2,3,4 | .012422519998 | .012422522466 |
| 1,2,3,5 | .009924559529 | .009924580522 |
| 1,2,4,3 | .034477109471 | .034477133626 |
| 1,2,4,5 | .019751618739 | .019751640703 |
| 1,2,4,6 | .034477109471 | .034477133626 |
| 1,2,5,3 | .037216147720 | .037216191385 |
| 1,2,5,4 | .037216147720 | .037216191385 |
| 1,2,5,6 | .037216147720 | .037216191385 |
| 1,3,2,5 | .039155292936 | .039155316785 |
| 1,3,4,2 | .045408417837 | .045408442944 |
| 1,3,4,5 | .029483045876 | .029483068792 |
| 1,3,4,6 | .045408417837 | .045408442944 |
| 1,3,5,2 | .039116808526 | .039116852377 |
| 1,3,5,4 | .039116808526 | .039116852377 |
| 1,3,5,6 | .039116808526 | .039116852377 |
| 1,4,2,5 | .063808576599 | .063808622796 |
| 1,4,3,5 | .063808576599 | .063808622796 |
| 1,4,5,2 | .063783623545 | .063783669741 |
| 1,4,5,3 | .063783623545 | .063783669741 |
| 1,4,5,6 | .063783623545 | .063783669741 |

The largest certified gap is 0.000000046197. Every lower bound is strictly
positive. The failure of random search therefore established no limitation of
this dimension-four instance. Different prefixes may use different rational
models. The executable and receipt preserve each separately.
