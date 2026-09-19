# R12 — Fixed-dimension selection and exact polygon replay

Research date: 19 September 2026. Main question and R08 game unchanged.

**Brief.** Turn R10's dimension bound into a carefully encoded complexity theorem,
then implement an auditable exact selector for rational polygons, segments and
points. Keep general sharpness refinements in a separate bounded investigation.

- [Theorem and algorithm correctness](math/THEOREM.md)
- [Current state](CURRENT_STATE.md)
- [Research note](manuscript/RESEARCH_NOTE.md)
- [Experiments and trust boundary](experiments/README.md)
- [Sources](sources/NOTES.md)
- [Independent sharpness investigation](side_investigation/REPORT.md)
- [Completion audit](AUDIT.md)

The core conclusion is polynomial-time **decision and order selection for each
fixed affine dimension**, with dimension-dependent exponent. The executable uses
two established exact algebraic backends. Its emptiness certificates require
solver trust; its rejection witnesses have solver-free rational checks. These
are different assurance levels and neither formalizes the R08 strategic bridge.
