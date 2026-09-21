# R16 — optimal bits for certified enforcement interfaces

21 September 2026. Baseline `a863070`; foundation milestone `6b59f0e`.
Written research results with exact rational executable evidence, not Lean proofs.

**The planar storage logarithm is removable:** for one compressed convex block
in a fixed positive probability box, reusable all-order/all-cost contextual
representation bits are `Theta(gamma^-1/2)`. An explicit rational multiscale codec
achieves this rate. A verifier with the original source can check its domination
sandwich with zero additional witness bits and polynomial work in input length
and 1/gamma. Source storage, expansion memory and query work are separate costs.

**Unlimited reuse has a different answer:** a fixed finite summary cannot preserve
all gamma-separated decisions under arbitrarily many independent repetitions.
Repeated products amplify any discarded interface distinction. For at most k
repetitions the optimal planar per-code rate is `Theta(sqrt(k/gamma))`.

The classical geometric rate belongs to convex metric-entropy theory. The
enforcement metric, contextual attainment and product law are inherited R15.
The new work audits these foundations, supplies a uniform rational bit codec,
states the necessary composition/audit contract, and extends error budgeting to
finite labelled trees. Candidate originality is explicitly qualified in the
source notes; no historical priority claim is made.

## Gate reports and proofs

| Gate | Strongest result | Evidence / qualification |
|---|---|---|
| [1: foundation audit](math/FOUNDATION_AUDIT.md) | Five R15 foundations survive; rational separation and strict boundaries explicit | Written re-derivation; 32,847 exact checks; historical R15 executable still missing |
| [2: bit model](math/BIT_MODEL.md) | Separate R, C, verification/query T and update U; unlimited-repeat impossibility | Written proof; source access and total composition budget declared |
| [3: planar rate](math/PLANAR_RATE.md) | Matching Theta(gamma^-1/2) bits, actual binary codec and source-readable rational check | 63 continuum sandwich checks, 1,637 codec controls; 4,608 contextual queries plus 3 tie controls |
| [Conditional gates](math/EXTENSIONS.md) | Fixed-d matching entropy rate; label-selection direct sum; tree error budget | Higher-d effective but inefficient written construction; 168 tree checks over 2,500 compatible assignments |
| [Literature and candidate theorem](sources/NOTES.md) | Geometric rate borrowed; narrow enforcement contract candidate | Primary-source comparison, uncertainty and Lean plan explicit |

Each gate records counterexamples/failed routes, exact evidence, literature,
remaining gaps, effect on the central question and a bounded next attack.

## What is implemented

`experiments/codec.py` encodes arbitrary rational planar vertex lists to a binary
multiscale rank stream and decodes it to rational convex-hull generators.
`experiments/verify.py` independently checks both source-relative inclusions using
full downward polygons; it imports no encoder geometry. The sample binary is
345 bytes at epsilon=1/128. This is an asymptotic-rate construction with loose
constants, not a claim to outperform R15's practical codec on every fixture.
The current format has a precision-dependent fixed length and is not instance
optimal for points/segments; direct endpoint coding gives their logarithmic rate.

The contextual query checker implements the known-first-sender, two-uncertain-
coordinate case. It does not implement arbitrary-order optimization. The tree
checker computes error budgets, not strategic order selection. All normal and
optimized Python mathematical receipts agree. The workflow adds repository CI
replay; local execution is the evidence recorded here, not an already completed
external CI or independent proof-kernel replay.

## Remaining work

Optimal verification/query/update tradeoffs under restricted computation remain
open, as do all-cost optimized-value-only minimality, practical higher-dimensional
codecs, and general revisions without source recovery. None changes the matching
finite-budget storage theorem. Source-free authenticated proofs require a separate
trust model. Full continuous enforcement frontiers were not begun.

The next bounded assurance attack is the R08/R14 target-existence formalization,
then the R15 rational-sandwich to contextual-interval bridge and tensor-collision
corollary. Avoid formalizing easy coding identities before that strategic chain.

See [replay instructions](experiments/README.md) and [manifest](VERIFICATION.json).
