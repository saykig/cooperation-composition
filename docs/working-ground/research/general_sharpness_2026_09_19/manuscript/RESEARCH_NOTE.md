# The short-prefix bound is sharp in every dimension

19 September 2026 — Cooperation & Enforcement, R11.

## Result

For every dimension d there is a rational family of admissible models in the
existing sequential hard-evidence game whose shortest successful prefix has
exactly d+1 senders. The family has actual affine dimension d and only d+2 senders.
Receiver payoffs and disclosure costs may depend on d; the receiver threshold
approaches one in the construction. The game, target, sender information, timing
and favorable sequential-equilibrium concept are unchanged.

A “successful prefix” means that its cascade inequalities cannot all be strict
under any compatible model, so any completion to a full order sustains the target.
The claim is about that robust certificate length, not a game in which other
senders are removed. Every shorter candidate prefix has its OWN defeating model.
There is no inference that one model defeats all orders.

This matches R10's Helly/move-to-front upper bound. It does not establish hardness
of finding an order or historical novelty of the construction.

## What happened to the twenty missing cases?

All twenty are feasible at the original six-sender, q=4/5 parameters. Their minimum
log cascade margins were optimized individually. Numerical candidates were then
made rational, with the affine equality enforced exactly. Every required product
inequality is strictly positive by rational arithmetic.

For each prefix, a separate concave-tangent certificate gives a global upper bound
on its optimal margin. Rational log-series enclosures make both ends rigorous.
The largest gap is below 4.7·10^-8, and all lower bounds are positive. Thus the
previous search failure told us about the search, not an obstruction. The complete
[twenty-row outcome table and certificate argument](../math/DIMENSION_FOUR.md)
retain the original parameters and distinguish the numerical and exact steps.

## Why the general construction works

Write m=d+1. Put the probability vectors on one weighted affine slice with
m variable coordinates and one fixed coordinate. Weighted AM-GM then prevents all
m inequalities of the canonical prefix from being strict simultaneously. This
proves that prefix succeeds throughout the slice and throughout every hull inside it.

The hard part is defeating EVERY shorter prefix, including unusual permutations.
Use small probability deficits: p_i=1−εx_i. If the first sender is not sender 0,
put nearly all the deficit budget on that sender; once it is removed, the remaining
probabilities are high enough to support continuation.

For a prefix beginning with sender 0, read its later labels and keep only new
running maxima. These divide 1,...,m into consecutive blocks. Because the prefix
is too short, at least one block has length two or more. If b_l are block endpoints
and Δ_l their lengths, the exact surplus is

    Σ b_l Δ_l − m(m+1)/2 = Σ Δ_l(Δ_l−1)/2 ≥ 1.

Place raw deficits at those endpoints, normalize to the required budget, and mix
slightly toward the all-ones vector to keep all probabilities strictly below one.
The surplus makes every required remaining-deficit sum strictly smaller than its
threshold. An explicit small rational ε turns these linear inequalities into the
original strict product inequalities with a uniform positive margin. This is an
exact construction, not a first-order numerical approximation.

The [complete proof](../math/GENERAL_CONSTRUCTION.md) supplies the rational formulas,
both prefix cases, all shorter-prefix extensions, the AM-GM inequality, actual
dimension witnesses and the finite rational hull. For d≥1 it chooses

    C=m(m+1)/2, κ=1/[8m(C+1)], γ=1/[2(C+1)],
    ε=γ/[m(m+1)], q=1−ε, τ=1−εκ/2.

Every constructed cascade witness has product-minus-cost margin at least εγ/2.
The dimension-spanning points establish dimension d independently of any random
search. The d=0 case is a singleton with a favorable tie. No proof gap is known
in the stated written argument; it has not been checked in Lean or externally.

## The fixed-threshold distinction is substantive

The theorem permits τ to depend on dimension. It does NOT settle all-dimensional
sharpness with τ=2/3 fixed.

There are two proved limitations of the PARTICULAR uniform-AM-GM/geometric-cost
construction, not of arbitrary games:

- Keeping q=4/5 creates a universally blocking singleton from m=11 onward. The
  weighted deficit budget eventually exceeds what a profitable first report permits.
- For any fixed τ<1, this construction has a singleton blocker in sufficiently
  large dimensions, whatever q is chosen. At τ≤2/3 it has one for every m≥2.

The second bound follows by comparing the product for sender m−1 with
q τ^(m−1) C/(C−m+1). When the multiplier is at most one, that sender blocks all
models when placed first. R08's changing-blocker example at τ=2/3 does not have
this special affine/cost structure, and prevents a universal one-prefix conclusion.
See the [separate fixed-threshold proof](../math/FIXED_THRESHOLD.md).

These obstructions explain why allowing q and τ to vary with dimension matters
for this construction. They do not show that thresholds approaching one are
necessary for EVERY possible sharpness example; that broader question remains open.

## Evidence, borrowed mathematics and next attack

The arbitrary-d statement is a written proof using established AM-GM, product and
Taylor bounds. Its explicit witness formulas passed exact checks on every relevant
prefix for m=2,...,7: 23,115 cases. Another 75 structured/random controls reached
m=100. Exact affine-rank and threshold checks accompany them. Finite testing
supports the implementation; it is not the proof for arbitrary dimension.

The [source notes](../sources/NOTES.md) distinguish existing mathematical machinery
from this application and document the optimizer interfaces inspected. The
[verification ledger](../../../VERIFICATION.md) labels the theorem unformalized.
The Python checker shares exact routines with the producer and is not an independent
trusted kernel. Historical novelty remains unresolved.

The construction gate is complete, and the main question should stay unchanged.
The next algorithmic target is **exact selection over rational polygons**: R10
reduces the search to at most three-sender prefixes, but those prefixes require
exact multivariate strict-feasibility certificates. Analyze that task directly;
neither sharpness nor a failed numerical search establishes computational hardness.
