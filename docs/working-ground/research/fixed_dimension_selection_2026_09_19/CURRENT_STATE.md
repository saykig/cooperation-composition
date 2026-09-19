# R12 current state

19 September 2026. First milestone.

**Written proof:** rational V/H inputs admit polynomial-bit decision and order
selection for each fixed affine dimension. Strict inequalities and affine
degeneracies are included. This specializes existing effective real algebraic
geometry after R10's short-prefix theorem.

**Implemented:** V-input polygon/segment/point selector, rational defeating
witnesses, and success bundles checked by two exact solvers with different
encodings. CPC proof skeletons retain trusted nonlinear steps. These are
backend-replay certificates, not solver-free multivariate proofs.

**Exact checks so far:** 14 fixtures against 84 exhaustive full orders; corrupted
certificates and out-of-scope inputs rejected. Independent sharpness investigation
proved two scoped improvements and supplied its own exact checks. No Lean proof.

**Before closing this gate:** finish the independent certificate replay audit,
check the primary full-order answers directly against the independent method,
cross-check segment cases with the prior Sturm checker, and finalize the note and
ledgers. These checks target correlated-error and representation risks, not a
larger undirected example count.

Main question unchanged. Growing dimension remains unresolved; prefix sharpness
does not imply hardness. The next confidence priority remains R08's strategic
bridge, before claiming a fully formalized enforcement result.
