# Gate 2 — four costs and the composition contract

21 September 2026. Written results, conditional on the audited R13/R15 bridge.

## Input, precision and queries

Fix the number n of labelled coordinates and rational constants
`0<ell<u<tau<1`. Input is a nonempty rational vertex list V, interpreted as
P=conv(V) inside [ell,u]^n. Its explicit length is L bits and N records; coordinate
numerators/denominators have at most B bits each. Redundancy is permitted.
Gamma is a positive dyadic accuracy request (small enough relative to the fixed
box); its encoding is charged. All real logarithms are mathematical semantics,
not free machine words. A uniform deterministic encoder emits a finite binary
string, decoded by one fixed algorithm; there is no uncharged source-dependent
dictionary, real oracle, or advice table. Randomized/cryptographic models are
outside this note.

The principal query class is every rational positive cost-ratio vector and every
order, with arbitrary exact independent rational V-polytope attachments. Their
dimension, vertex count and coordinate precision are part of the query input.
The mathematical discrepancy guarantee also holds for arbitrary compact convex
attachments, but no algorithm on an unspecified real-set oracle is claimed. Return
0 or B only when justified; always answer when |m|>=gamma. At m=0 favorable ties
give true fine zero, but an approximation may return REFINE. Optimized queries
replace m by min over orders and require a witnessing order for a zero answer.
The bit lower bound below is for the ALL-ORDER class, not optimized-only queries.
For one fixed optimized query known at encoding time, one answer bit suffices
with unrestricted encoder work; this is a different task from all future costs.

## Costs are a tradeoff, not four independent free minima

* `R*(gamma)`: infimum worst-case reusable query-payload bits over uniform
  schemes satisfying this query contract. Query decoder has no source access.
* `C*(gamma;L,N,B,R,Tv)`: minimum worst-case *additional* source-binding witness
  bits for a specified payload scheme and verification time budget Tv. A
  certificate which conveys extra query information is charged to R as well.
* `T*=(Tv,Tq)`: verification and query bit-operation costs, parameterized by the
  input, payload, certificate, gamma, query length and context size. They are
  distinct: even arbitrarily large exact contexts need no extra payload bits,
  but certainly need query computation. There is no meaningful bound T(gamma)
  alone for unbounded input or query lengths.
* `U*(gamma -> gamma'; L,operation)`: additional communication and computation
  to refine accuracy or apply a declared update. State source availability and
  charge new source data. It is not automatically defined for arbitrary revision.

If the verifier has the source and unrestricted computation, `C*=0`: it can
decide the two rational polytope domination inclusions itself. In fixed ambient
dimension it can do so in time polynomial in L and the *expanded* decoded
polytope size, using rational linear programming. The planar construction below
also supplies a elementary rational checker with no supplied witnesses. This
does not mean verification is free, nor does it give zero-witness assurance to a
source-free recipient. After an audit, downstream users need either trust in
that audit or its source and replay; cryptographic authentication is a different
model. An unauthenticated code/certificate alone cannot prove its relationship
to an unseen arbitrary source: the same received bytes can be paired with a
different source for which the assertion is false.

The R15 all-source-vertex inspection argument remains an Omega(N) record lower
bound on some inputs (even with a witness). It is not a universal Omega(L) bit
lower bound, and not a certificate-bit lower bound. Fast local witness formats
may depend on B and log N; no gamma-only optimum for those formats is asserted.

## The composition contract changes the answer

**A. One approximate block, arbitrary exact attachments.** The optimal rate
established below applies. Exact attachments contribute zero discrepancy.

**B. Finitely many approximate blocks, declared budget.** Assign local directed
error bounds beta_i with `sum beta_i<gamma`. This guarantees all composed queries
with |m|>=gamma are answered by the certified bracket. Repeated occurrences are
charged repeatedly. If up to k copies of the same code may be used, encode it
to local error below gamma/k. In fixed dimension d>=2 the optimal per-code rate
for this repeat budget is `Theta((k/gamma)^((d-1)/2))`; the lower bound uses the
same R15 packing at separation >2gamma/k and tensor amplification. For n=2 the
exponent is 1/2. This is storage for a shared reusable code, not k transmitted
copies; if the protocol transmits it k times those transmissions are charged.

**C. Unlimited independent repeated occurrences, fixed final gamma.** No finite
worst-case code length is possible, even for singleton sources in one coordinate.

Proof. Suppose distinct interfaces P,Q share a code and let
`delta=Delta+(P,Q)>0`, reversing the pair if needed. Product addition gives
`Delta+(P^k,Q^k)=k delta`. Choose k with k delta>2gamma and use the one-sender
attainment plus rational perturbation from Gate 1. One rational query has opposite
answers on these two repeated products, both more than gamma from zero. A
deterministic composition/query procedure receives identical strings and identical
query/context data in the two cases, so cannot answer correctly in both. Thus
the code must be injective on exact downward interfaces. Rational singletons
already supply infinitely many of these, precluding finite worst-case length.
Variable finite per-input exact descriptions remain possible, but are unbounded
as input precision grows. Allowing REFINE on this amplified separated query
would violate the completeness contract. Source recovery would change the model.

This impossibility is a new stated consequence of R15, not a new product law or
a new geometric lower bound. It resolves the ambiguity in “reusable under
composition”; there is no unconditional gamma-only finite rate in model C.

## Refinement and named updates

With source access, re-encode at gamma', paying the new payload and computation;
no delta-only optimal update theorem is claimed. Without the source, a lossy code
cannot promise arbitrary further refinement: a code collision is separated by
some sufficiently fine contextual query. Even retaining the EXACT downward hull
does not support arbitrary upper restrictions, by Gate 1's singleton/segment
empty-slice example. Empty families need an explicit tag if revision is admitted.
Adding/removing named premises also needs provenance, independently of geometry.

## Gate report

Strongest result: models A/B admit finite rates; model C has infinite worst-case
storage. Failed conjecture: unlimited reuse for a fixed local accuracy; the
smallest family obstruction uses one-coordinate rational singleton inputs and
one contextual sender. Evidence: written collision/amplification proof and Gate 1
exact product controls. Literature: communication/metric-entropy counting is
borrowed; enforcement distinguishability and exact products are inherited R15.
Gaps: optimal time/certificate tradeoffs under stronger verifier restrictions,
optimized-only all-cost minimality, and genuinely incremental source updates.
The central question narrows to an explicit finite-budget contract; it does not
pivot. Next attack: remove the planar storage logarithm under that contract.
