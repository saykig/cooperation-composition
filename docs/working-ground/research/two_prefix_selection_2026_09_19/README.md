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
proof. Higher-dimensional sharpness investigation is in progress at this milestone.
Historical R08/R09 results and receipts are preserved.
