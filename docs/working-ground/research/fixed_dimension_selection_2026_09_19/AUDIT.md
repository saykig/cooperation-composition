# R12 gate audit

19 September 2026. First milestone; not yet closed.

- Fixed-dimension V/H complexity proof: written, including bit encoding and ties.
- Polygon V-input selector: implemented with rational witnesses and explicit
  exact-backend emptiness certificates.
- Independent closed barycentric/cvc5 versus intrinsic/Z3 selection: passed on
  14 fixtures and 84 exhaustive full orders.
- External proof kernel: **not present**. CPC covering trust remains explicit.
- Additional direct full-order/Sturm replay and final source/result synthesis:
  pending before closing the gate.
- Separate sharpness investigation: report and exact evidence delivered; checked
  against the R11 formulas. No general fixed-threshold or novelty claim.
