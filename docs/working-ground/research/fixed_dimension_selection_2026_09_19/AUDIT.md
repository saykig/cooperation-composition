# R12 gate audit

19 September 2026. Gate closed. First milestone: `0f94556`.

- Fixed-dimension V/H complexity proof: written, including bit encoding and ties.
- Polygon V-input selector: implemented with rational witnesses and explicit
  exact-backend emptiness certificates.
- Independent closed barycentric/cvc5 versus intrinsic/Z3 selection: passed on
  14 fixtures and 84 exhaustive full orders.
- External proof kernel: **not present**. CPC covering trust remains explicit.
- Additional direct full-order/Sturm replay: 132 direct full-order comparisons,
  42 prior-Sturm comparisons, saved-bundle replay and narrow-polygon witness passed.
- Three rational AM-GM certificates provide independent solver-free emptiness
  proofs for the central triangle, tangent polygon and changing-blocker examples.
- Source-grounded research note, assumptions, proof, smallest vertex-test
  counterexample, novelty limits, performance and next attack: completed.
- Separate sharpness investigation: report and exact evidence delivered; checked
  against the R11 formulas. No general fixed-threshold or novelty claim.

## Requirement-to-artifact map

| Requested gate | Artifact and exact scope |
|---|---|
| Fixed-dimension theorem | `math/THEOREM.md`: V/H inputs, bit lengths, strict signs, affine reduction, d=0, n=1; written proof |
| Polygon selector | `experiments/selector.py`: V form, actual d≤2; successful prefix/order or every-prefix rational witnesses |
| Checkable emptiness | two-query exact-backend replay bundle with CPC skeleton; solver trust disclosed; `math/CERTIFICATES.md` adds three solver-free AM-GM examples |
| Established backend | pinned Z3 NLSAT and cvc5 coverings; no new multivariate algebra engine |
| Independent check | different solver, original-vertex closed domain, reverse suffix encoding, exhaustive full orders; prior Sturm comparisons |
| Required edge cases | sharp triangle, vertex-miss rectangle/segment, tangencies/ties, tiny open regions, degeneracies, duplicates, input/certificate corruption |
| Separate sharpness agent | `side_investigation/REPORT.md` and exact replay; improvements stay ansatz-scoped |

## Deliberate limits

No all-d software claim; no practical scalability claim; no inference of hardness;
no claim that the AM-GM certificate format is complete; no external proof-kernel
replay; no full R08 strategic formalization; no general fixed-threshold sharpness;
no historical or publication novelty claim. These are stated limits, not hidden
unresolved steps in the fixed-dimension decision proof.

The broad research question stays unchanged. R08's independent strategic check is
the recommended next confidence experiment; growing dimension is the subsequent
algorithmic frontier. This gate makes no new task automatically.
