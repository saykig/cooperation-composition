# Current state — R10

19 September 2026. Main mathematical question and R08 equilibrium concept unchanged.

| Item | Standing |
|---|---|
| Move selected blockers to the front | Proved by suffix-product inclusion |
| At most d+1 prefix in affine dimension d | Proved using finite Helly; strict sets and d=0 covered |
| Two-prefix iff criterion on rational segments | Proved, including degenerate/constant/empty-product cases |
| Polynomial-bit segment selection | Proved reduction to established root isolation, separate from implementation |
| Exact selector and certificate checker | Implemented, standard-library rational arithmetic; no sampled decisions |
| Exhaustive small-order comparison | 96 instances / 1,752 permutations; no disagreement |
| Independent quadratic oracle comparison | 240 cases; no disagreement |
| Additional edge/metamorphic checks | 105 passed; preserved first receipt remains 2,271 checks |
| Sharpness | Proved d=0,1; exact hull certificates plus AM-GM establish d=2,3 |
| All-d tightness | Open; bounded d=4 witness search inconclusive |
| Formal verification | Not performed |
| Historical novelty | Unresolved; borrowed Helly, Sturm and fast root machinery credited |

The minimum robust fine is exactly 0 on successful selection, B on certified
rejection, under the declared R08 assumptions. Different pair witnesses must not
be conflated into one universally failing model. Earlier receipts were not rewritten.

**Recommended next attack:** obtain a general weighted-AM-GM sharpness construction
for d≥4, or identify the first dimension at which the strategic product structure
improves Helly's bound. Keep the game fixed and seek rational certificates. A
parallel future literature task should establish whether this specific prefix
reduction already appears in robust sequencing, before any novelty claim.
