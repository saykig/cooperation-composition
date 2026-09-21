# How much information must an enforcement interface retain?

**Research date:** 20 September 2026. **Source repository inspected:**
`saykig/cooperation-enforcement`, `c0311bd227e200cbb131815f9515763e23551c85`.
The repository was not modified in this run.

**Status:** new written derivations and executed exact computations. The strategic
interpretation inherits R08/R13. No new Lean or Palomar proof, independent human
review, empirical validation, or historical-priority certification.

## The result in plain language

The preceding run identified what a reusable enforcement summary must preserve.
This run turns that into an operational compression result:

1. There is an exact error measure whose value is the largest change the summary
   can cause in a contextual incentive-margin query. It is not an arbitrary
   geometric proxy. One additional sender is enough to attain the worst case.
2. Those directed errors add exactly across independent components. Attaching
   exact components of any size adds no further error.
3. In a fixed-dimensional convex class, the required storage has a power-law
   lower bound and an upper bound with the same exponent, apart from a logarithmic
   factor. This is not a constant-size universal dashboard.
4. A working planar encoder and independent rational checker implement the guarantee.
   The decoder returns zero fine, full fine or "refine", rather than silently
   turning approximation into a false exact guarantee.
5. Shared scenario labels can be retained as explicit interfaces and composed
   safely. Erasing the labels can invent a profitable cascade.

The general geometric approximation rate is established mathematics. The
candidate research contribution is the exact connection to enforcement queries,
compositional error accounting and proof-carrying coding, not a new theory of
convex approximation.

[Complete statements and proofs](math/RESULTS.md) provide the assumptions and
scope. [Source comparison](sources/NOTES.md) records what was actually inspected.

## What is being held fixed

The current game is unchanged: each sender privately sees one independent
Bernoulli fact and may pay to report positive evidence; all facts are needed
before the receiver prefers the non-target action; the fine is imposed on that
action. Actual model probabilities are known to players. The institution chooses
one disclosure order and fine across its uncertain family of models.

The objective is existence of the target equilibrium, with favorable ties, not
all-equilibria cooperation, coalition stability, social welfare or the cost of
providing credible enforcement. The fine is still 0 or B in this benchmark.

We preserve all order/cost-ratio queries and permitted attachments. This also
preserves optimization over orders, but the lower bound is not claimed minimal
for the single optimized scalar answer alone.

## The operational metric

For a compact convex probability family P, write

    H_P(w)=max_{p in P} sum_i w_i log p_i.

The coarsest exact independent-composition interface is the downward hull of P,
equivalently this entire support profile. The previous proof survives audit.

Define

    Delta+(P,Q)=max_{0<=w_i<=1}(H_P(w)-H_Q(w)).

Theorem A proves that this equals the supremum of

    true signed cascade margin - summary's signed cascade margin

over all permitted contextual order/cost queries. Just one known-probability
attached sender suffices. It is a logarithmic incentive measure, not a utility,
fine, Shannon-information or welfare unit.

Theorem B proves

    Delta+(P1 x P2,Q1 x Q2)=Delta+(P1,Q1)+Delta+(P2,Q2).

Consequently one compressed block's error remains the same under any exact
independent attachment, and multiple compressed blocks have an additive budget.
This gives sharper accounting than a bound growing with every sender in a large
exact context.

If the summary is one-sided and its error is at most beta, the true margin lies
between the decoded margin and decoded margin+beta. An order is certified safe
when that whole interval is nonpositive. A strictly positive optimized lower
margin certifies that every order needs B. Otherwise refine. All queries at least
gamma from the boundary are answered correctly when beta<gamma.

## Size versus margin

For fixed bounds 0<ell<u<tau and fixed sender count/affine dimension d>=2:

    achievable reusable storage:
        O(gamma^{-(d-1)/2} log(1/gamma)) bits;
    necessary in the worst case:
        Omega(gamma^{-(d-1)/2}) bits.

Constants depend on the fixed dimension and probability bounds. The upper bound
imports classical convex-body approximation and charges rational grid precision.
The lower bound uses a family of rational exposed paraboloid patches and converts
its separations into actual opposing margin decisions with one attached sender.
It applies to arbitrary deterministic self-contained encodings whose decoders
must answer every gamma-separated query, not only to point-list encodings.

For a planar component this is a square-root law in 1/gamma, up to the logarithm.
For points and segments, one or two endpoints already specify the convex family;
approximating those coefficients costs O(n log(1/gamma)). A nonlinear support
optimum at an interior point does not make every interior model necessary to store.

The higher-dimensional encoder is a written existence/construction result, not
an implemented fast algorithm. The planar rational encoder is implemented. General
rounding can raise affine dimension, so a downstream fixed-dimension solver's
complexity must not be inherited automatically.

## The prototype and its certificate

The encoder extracts the monotone convex Pareto chain, places nodes according
to arclength and slope variation, and rounds them downward onto a rational grid.
The two sources of approximation loss yield a certified multiplicative sandwich:

    D(decoded) subset D(original) subset (1+epsilon)D(decoded).

The decoded points represent their CONVEX HULL, not a list of isolated scenarios.
This is necessary: even two stored endpoints may have a weighted-log optimum at
an interior mixture.

Two independent certificate verifiers were implemented. The first stores
per-input-point domination witnesses. The improved compact version retains only
per-decoded-point lower witnesses and reconstructs the entire positive-normal
boundary itself. It checks every source vertex against that boundary without
importing the encoder, using only rational arithmetic.

On a 1,025-vertex convex input at epsilon=1/256:

| Object | Canonical JSON bytes |
|---|---:|
| Original input | 35,771 |
| Reusable 12-vertex summary | 399 |
| First working certificate | 42,642 |
| Improved compact certificate | 657 |

The 1,056-byte improved summary-plus-certificate does not include verifier code
or the original source needed during audit. This is a fixture, not an optimal
compression benchmark. The source is retained for future revision and replay.

With two cost ratios 1/10 and an attached sender of known probability 1/2, the
actual decoder gives:

| Attached sender's cost ratio | Certified answer |
|---|---|
| 1/5 | zero fine, order (attached, first original, second original) |
| 3/20 | full fine B=1 |
| 22/125 | refine |

The last case is an actual tie in the source family. The compressed representation
does not pretend it can resolve it exactly. Its margin-error upper bound is
1/128; that is not an error bar of 1/128 on the fine.

## Shared interfaces

For finitely many matched labels s, retain a conditional interface for each P_s.
If blocks combine independently conditional on s, their wired uncertainty is
union_s(P_s x R_s). Keep that union; do not replace it by a convex hull. The margin
error is bounded by max_s of the sums of conditional block errors.

The exact counterexample uses label-specific probabilities (9/16,1/4) and
(1/9,9/16). Each label blocks a different stage. Their geometric midpoint
(1/4,3/8) permits the cascade, but adding it changes none of the aggregated support
maxima. The label-free support summary therefore cannot certify the true union.

This is a concrete limited shared-interface extension, not permission to apply
the independent-product rule to arbitrary connections. The preceding impossibility
for arbitrary future upper-bound revisions remains in force.

## Evidence

The original exact suite in this run passed 19,264 checks, including 228 encoder
instances, 1,368 independent weighted-product comparisons, 360 decoder queries,
and supporting algebraic/metric/lower-bound controls. The compact-certificate
addition passed 250 valid-bundle comparisons and 250 rejection controls. Normal
and Python -O executions produced identical receipts for both suites.

The compact dense-fixture certificate verifies 1,025 source and 12 decoded
vertices, using 13,325 rational plane evaluations. These finite checks are not
proofs of the continuum, minimax, geometric approximation, or game theory.
The code inherits the cascade criterion and is not a full equilibrium solver.

See [reproduction and trust boundary](experiments/README.md). All sources, receipts,
fixtures and both verifier versions are included. No old result count is promoted
as new evidence.

## Next attack

Keep the same compression/enforcement question. The next goal is a sharper
proof-carrying interface: resolve the constructive logarithmic storage gap and
quantify certificate and query costs, first for planar components with a finite
shared interface. Compare with convex-body metric entropy and minimum convex
Pareto approximation before treating the logarithm as a new open problem.

In parallel within that confidence gate, formalize the rational sandwich and its
contextual margin guarantee, keeping the still-unformalized R08/R13 strategic
bridge explicit. Do not claim a small source-relative certificate makes the
original arbitrary input inspectable without reading it.

Applications to cooperation, bargaining or institutional design require a
separate argument that the chosen arrangement is desirable and the enforcement
instrument is credible and worth its cost. None of those empirical or normative
claims follows from this mathematical compression result alone.