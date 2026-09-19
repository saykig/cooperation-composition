# Fixed-dimensional uncertainty permits exact disclosure-order selection

19 September 2026. Written mathematics plus exact computational evidence; no
new proof-assistant result or historical novelty claim.

## What is now settled

The number of senders can grow while the uncertain model family occupies a fixed
number of dimensions. In that setting, exact order selection is polynomial-time
under an explicit rational polytope encoding. The exponent may depend on dimension.
This closes the theoretical polygon-tractability question, conditional on R08's
strategic characterization. It does not settle growing dimension or guarantee
fast practical solvers.

The main question remains: when does one order sustain the target for every
compatible model, and which shared constraints must be retained to determine
enforcement? Fixing uncertainty dimension supplies a substantive positive answer.
It does not erase the strategic importance of those constraints.

## Precise result and its mathematical source

Let P⊂(0,τ)^n be a nonempty compact rational polytope, 0<τ<1, with rational
positive cost/reward ratios r_i. P constrains independent Bernoulli parameters
across possible models; it does not introduce dependence between private bits
inside a model. Players know their model. The institution chooses a single pure
order for the whole family, under R08's target and favorable tie convention.

For prefix α=(i₁,...,i_k), define its defeating set by the strict inequalities

    ∏_{h not in {i₁,...,i_j}} p_h > r_{i_j},   j=1,...,k, p∈P.

An empty set certifies that every completion of α works. R10 proves that some
successful order exists exactly when some successful prefix of length ≤d+1
exists, where d is actual affine dimension. Its ingredients are finite Helly
and moving selected senders to the front, which decreases their suffix products.

**Theorem.** On explicit binary-rational vertex-list or linear-inequality inputs
of total bit length L, exact selection is possible in L^{O_D(1)} bit operations
whenever d≤D is fixed. A successful order can be returned. The minimum robust fine
in this benchmark is exactly 0 on success and B otherwise.

The proof first reduces to d affine coordinates, enumerates at most
Σ_{k≤D+1} n^k prefixes, and tests each strict polynomial system. Degrees are ≤n−1
and expanded coefficient lengths are polynomial for fixed d. Existing effective
quantifier elimination supplies the remaining bit-complexity result. See the
[full proof](../math/THEOREM.md) and
[Basu's survey, Theorem 2.27](https://arxiv.org/pdf/1409.1534).
The algebraic machinery is borrowed; the contribution of this gate is the careful
specialization and implementation. Affine reduction is essential: using one
variable per listed vertex would not prove fixed-dimension tractability.

Strictness is not a numerical detail. Equality blocks the cascade. A continuity
and relative-interior argument proves that every defeating model can be replaced
by a rational relative-interior model. This justifies searching strict intrinsic
halfspaces while independently checking the original closed convex hull. It also
handles points, segments, redundant vertices and tangencies without genericity
assumptions or tolerance thresholds.

## Small counterexample: vertices still do not decide success

This is the previously established R09 obstruction, retained as a regression,
not rediscovered as a new result. Take three senders, τ=2/3,

    r=(3/20,1/10,1/10),
    P=conv{(1/2,1/5,3/5), (1/2,3/5,1/5)}.

Order (1,2,3) succeeds at both vertices: its first suffix product is 3/25<3/20.
At the midpoint (1/2,2/5,2/5), that product is 4/25>3/20, the next is 2/5>1/10,
and the final empty product is 1>1/10. Indeed every order fails there, since every
sender's first-position product exceeds its ratio and removing more factors only
increases products. The family needs fine B despite the common vertex-success
order. A two-dimensional rectangle obtained by varying p₁ from 49/100 to 51/100
has the same failure, so this is not only a degenerate-polygon issue.

Three senders and dimension one are minimal for this **fixed-order vertex test**
failure. At dimension zero there is only one model. With at most two senders the
only nonconstant cascade condition for any fixed order is affine, and its last
condition is constant. If that fixed order succeeds at every vertex, it succeeds
throughout the hull. This minimality statement does not exchange the quantifiers
“one common order” and “a possibly different order at each vertex.”

The stronger two-prefix conjecture is already false in R10's four-sender triangle.
This gate reproduces that example: every singleton and pair has an exact witness,
but prefix (1,2,3) succeeds. We retain all witnesses and a rational weighted-AM–GM
certificate for the entire triangle.

## What the executable certifies

The selector accepts rational vertex lists of actual dimension at most two.
It returns either a successful prefix and full order with an emptiness bundle,
or a defeating rational convex combination for every candidate prefix. These
may be different models. The two-sender segment p₁+p₂=7/10 with
r=(2/5,3/10) confirms the distinction: no common order works, although every
individual model has a successful order.

Primary decisions use Z3 QF_NRA/NLSAT on intrinsic polygon inequalities. A separate
implementation uses original barycentric weights, reverse suffix recursion and
cvc5 cylindrical coverings. The latter exhausts full orders on small cases,
independently of the prefix reduction. The backend techniques are established;
see [Z3's author documentation](https://z3prover.github.io/papers/z3internals.html)
and [Kremer et al.'s cvc5 paper](https://theory.stanford.edu/~barrett/pubs/KRB%2B22.pdf).

The first receipt covers 14 designed instances and 84 exhaustive full orders.
The additional audit replays saved bundles, compares both methods directly on
those 84 orders plus 48 reordered/redundant-vertex variants, and agrees with the
older independent Sturm checker on 42 segment/point orders. It includes exact
ties, tangencies, a narrow polygon strip of width below 10^-30, endpoint roots,
constant conditions and one-sender boundary cases. Corrupted certificates and
invalid/out-of-scope inputs are rejected. Normal and optimized Python agree.

These counts are finite evidence, not the general proof. The first fixture run
took about 2.05 seconds and the additional audit about 2.23 seconds on the recorded
machine. They are not scalability measurements. No timeout or unknown is treated
as a mathematical answer.

**Trust matters.** Rational rejection witnesses need only arithmetic and convex
weights to check. General emptiness bundles require replay with exact backends;
cvc5's saved CPC skeleton still contains trusted nonlinear steps. We do not claim
external CPC-kernel verification. For the triangle, tangent polygon and changing
blocker, an additional [weighted-AM–GM format](../math/CERTIFICATES.md) supplies
short rational, solver-free sufficient certificates. These three proofs do not
establish completeness of that certificate format for all empty defeating sets.

## Unexpected useful refinement, kept separate

The independent [sharpness review](../side_investigation/REPORT.md) found two
analytic improvements rather than more isolated dimensions. Put C=m(m+1)/2 in
R11's uniform-AM–GM construction. After optimizing its free parameters, its
distinguished singleton can be defeated exactly when

    τ > ((C−m+1)/C)^(1/(m−1)).

The threshold deficit is asymptotic to 2/m². This characterizes ONE singleton
obstruction within that ansatz, not full sharpness or arbitrary games. Separately,
κ=ε=1/[2m(C+1)] preserves general sharpness, improves the sufficient receiver
threshold deficit to order m^-6, and increases the guaranteed product margin by
factor m+1. Complete proofs and rational replay are provided. The gap between
necessary order m^-2 and sufficient order m^-6 is a possible later construction
question; it does not delay selection or prove growing-dimension hardness.

## Recommendation and remaining obstacles

Keep the central research question unchanged. Its fixed-dimensional algorithmic
part is settled by existing algebraic machinery plus the project-specific prefix
reduction. Do not market polygon feasibility or the SMT methods as new mathematics.
Historical novelty of the specialized order reduction remains unclaimed.

The most valuable **next attack** is an independent rederivation of R08's complete
sequential-equilibrium-to-cascade bridge, followed by a scoped formalization. All
later enforcement interpretations depend on it. The first experiment should
enumerate full history/type strategies in the three-sender game, including ties,
and compare actual sequential incentives with the claimed strict-product criterion;
reusing that formula as the “game checker” would not be independent evidence.

After that confidence gate, the tractable paper question is: **what is the exact
complexity of common-order selection when the dimension of a rational H-polytope
is part of the input?** Seek a structural algorithm or a valid hardness reduction,
not an inference from the sharp d+1 prefix bound. A complete small-kernel polygon
certificate checker and sharpness at a fixed receiver threshold remain separate
obstacles. None requires changing the main game or adding networks/senders beyond
the current order-selection model.
