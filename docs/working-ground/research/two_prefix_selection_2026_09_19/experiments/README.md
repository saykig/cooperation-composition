# Exact selector, certificates and measured evidence

Python standard library only, using `fractions.Fraction`. No solver, floating-point
root finder, sampled feasibility grid or third-party environment is required.
JSON numbers for probabilities/cost ratios should be rational strings such as
`"1/3"`; sender labels in executable output are **zero-based**. Mathematical notes
use one-based labels. Input is `{"a":[...],"b":[...],"r":[...],"tau":"2/3"}`.
The optional `tau` defaults to 2/3. Positive endpoints must lie strictly below it;
ratios must be positive. Degenerate segments and n=1 are accepted.

From this directory:

```sh
python3 selector.py input.json > certificate.json
python3 selector.py input.json certificate.json
python3 check.py > /tmp/r10-check.json
python3 additional_checks.py > /tmp/r10-additional.json
python3 sharpness.py > /tmp/r10-sharpness.json
```

`select()` returns either a prefix, full order and success certificate, or a list
of EVERY ordered pair with its own rational strict witness. Rejection uses the
proved two-prefix theorem; a witness for a pair need not defeat every completion.
The checker validates certificates without rerunning selection or root isolation.
It shares rational polynomial arithmetic with the selector, so it is not a fully
independent trusted kernel. A separate historical quadratic oracle supplies
independent n=3 cross-checks. No proof assistant was run.

## Certificate format and continuum coverage

- `constant_blocker`: an original constraint is a nonpositive constant.
- `witness`: one rational t∈[0,1] makes every specified inequality strictly positive.
- `sign_cover`: ordered rational intervals isolate ALL interior roots of the
  square-free product of the nonconstant constraints, with endpoint factors stripped;
  rational samples and original-polynomial signs cover every complementary cell.

The verifier reconstructs all constraints from the input. It recomputes Sturm
counts to prove the root cover complete and checks sample placement/signs. A root
is itself a zero of at least one original constraint, so it cannot meet strict
cascade inequalities. A feasible endpoint would have a feasible neighboring cell.
This is why finite sign certificates cover the full segment, including arbitrarily
narrow cells and tangencies.

The subdivision algorithm terminates: each cut is a checked nonroot chosen from
finitely many distinct rational candidates, with a contraction bounded away from
one for fixed degree. Distinct roots have positive separation, and all remaining
roots lie strictly inside (0,1). Repeated subdivision therefore isolates each and
moves its bracket away from both endpoints. There is no recursion-depth cutoff or
numerical tolerance; the stack is iterative. Large inputs can still be expensive.

## Receipts and scope

The first receipt `results.json` is preserved from milestone `ce06375`:

- **2,271 checks**, including 96 complete comparisons with exhaustive permutation
  verification (1,752 full orders), and 240 separate comparisons with R09's
  independently implemented quadratic interval oracle.
- Twelve named game fixtures: midpoint, changing blocker/shared root, modelwise
  success without a common order, tangency, endpoint roots, extremely narrow
  feasible interval, degenerate success/rejection, constant-coordinate tie,
  empty-product tie and both one-sender outcomes.
- The narrow fixture has a strict feasible interval of width (5/2)·10^-30 for its
  specified pair, found by exact signs. It retains a rational witness and checks
  its exact bound. Cost denominators are of order 10^60.
- Algebraic sign stress cases, JSON roundtrips and deliberate corruption of roots,
  samples, signs, orders, witnesses and pair coverage.
- Observed elapsed time approximately **9.01 seconds** on the recorded Python
  version. This is one workload, not an asymptotic claim.

`additional-results.json` adds shared irrational roots, double irrational roots,
parameter reversal, sender relabeling, invalid-input rejection, and large rational
ENDPOINT denominators of order 10^60. It retains 105 checks and its separate timing.

`sharpness-results.json` retains the exact d=1 control, the d=2 triangle certificate,
and the d=3 five-sender certificate with 12 rational vertices and all 60 rejected
three-prefixes. Rational affine-rank checks establish actual dimension, not ambient
sender count. A bounded d=4 search remains explicitly inconclusive. Search is used
to find candidate rational witnesses; AM-GM and exact substitutions certify the
successful hull examples. The full search/check took approximately 2.08 seconds.

Normal and `python3 -O` runs of `check.py` gave identical counts and certificate
contents (timings naturally differ). Checks use explicit exceptions, not removable
Python assertions. The additive final audit records the optimized-run comparison.
Source hashes bind each retained receipt to the code it exercised.

The polynomial-BIT theorem is a reduction to established root-isolation algorithms
in [the proof](../math/THEOREM.md). This elementary Sturm implementation is not an
implementation of the cited fast algorithm, and no optimized bit bound for this
code is asserted. Exhaustive permutation comparison is a test oracle only; the
selector never enumerates full orders.
