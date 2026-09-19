# R10 research log

## 19 September — revalidation and segment proof

Inspected live main `6478ff2`, destination origin, repository instructions and
working-ground ledgers. The active objective requested the two-prefix theorem,
but no such theorem or selector existed in the checkout. R09 supplied the stable
cascade criterion and the earlier NP upper bound. No branch created.

Proved finite Helly plus relative-order move-to-front, including strict inequalities
and favorable ties. Derived at most d+1 prefix and exact two-prefix selection for
segments. Wrote a self-contained Radon/Helly proof and kept the bit-complexity
reduction distinct from local implementation performance.

Implemented standard-library rational polynomials, gcd/square-free reduction,
Sturm isolation, portable sign certificates, pair enumeration and checking. Initial
receipt: 2,271 checks, 96 exhaustive-order instances, 240 independent historical
quadratic comparisons. Tangencies, shared/endpoint roots, narrow cells, ties and
degenerate segments passed. Milestone `ce06375` committed and pushed. This is
progress beyond R09, not a reclassification of its historical evidence.

## 19 September — dimension sharpness, after segment completion

Investigated the tempting stronger dimension-independent two-prefix reduction.
A weighted-AM-GM plane supplies a universal successful triple. Exact rational
search found witnesses for all twelve pairs; finite set cover reduced the witness
family to a triangle. Thus the stronger reduction is FALSE already at n=4,d=2.
The proof uses a universal inequality on the hull, not vertex-only game testing.

The same construction found a dimension-three hull with 12 vertices certifying
that all 60 ordered triples fail but a four-prefix succeeds. An analogous bounded
dimension-four search left 20 missing witnesses; recorded as inconclusive, with
no complexity or nonexistence conclusion. No strategic-model changes were made.

Added 105 tests for irrational/shared roots, relabeling, parameter reversal,
large endpoint denominators and invalid inputs. An optimized Python run preserved
all original test counts and certificate contents. The code uses explicit checks,
not assertions removable under optimization. Original receipt remains untouched.

Completed source notes, manuscript, current-state summary and goal audit. The next
attack is general within-game sharpness, not segment hardness (now polynomial).
