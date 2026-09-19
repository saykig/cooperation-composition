# R10 — two-prefix selection on rational segments

19 September 2026. Continues R09 without changing the strategic model.

- [Complete proof and bit-complexity reduction](math/THEOREM.md)
- [Exact selector and certificate checker](experiments/selector.py)
- [Regression and exhaustive-order checks](experiments/check.py)
- [First execution receipt](experiments/results.json)

A successful full order exists on a rational segment iff a successful ordered
prefix of length at most two exists. Helly plus a move-to-front argument reduces
selection to polynomially many univariate strict-sign decisions. The executable
uses exact rational Sturm certificates; its performance is not the complexity
proof. The completed sharpness investigation establishes tight examples through
affine dimension three; higher dimensions remain open.
Historical R08/R09 results and receipts are preserved.

- [Research note](manuscript/RESEARCH_NOTE.md)
- [Within-game sharpness and its limits](math/SHARPNESS.md)
- [Reproduction instructions](experiments/README.md)
- [Sources and novelty boundary](sources/NOTES.md)
- [Current state](CURRENT_STATE.md) · [research log](RESEARCH_LOG.md)
- [Rejected approaches](REJECTED_APPROACHES.md) · [completion audit](AUDIT.md)
