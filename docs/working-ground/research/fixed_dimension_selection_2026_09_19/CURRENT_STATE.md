# R12 current state

19 September 2026. Gate closed with explicit exact-backend trust.

**Written proof:** rational V/H inputs admit polynomial-bit decision and order
selection for each fixed affine dimension. Strict inequalities and affine
degeneracies are included. This specializes existing effective real algebraic
geometry after R10's short-prefix theorem.

**Implemented:** V-input polygon/segment/point selector, rational defeating
witnesses, and success bundles checked by two exact solvers with different
encodings. CPC proof skeletons retain trusted nonlinear steps. These are
backend-replay certificates, not solver-free multivariate proofs.

**Exact checks:** 14 retained bundles replayed; 84 original plus 48 transformed
full orders compared directly across independent methods; 42 comparisons with the
prior Sturm checker; a genuine polygon strip narrower than 10^-30; three portable
rational AM-GM success certificates. Corrupted certificates and out-of-scope inputs
are rejected. Normal and optimized Python agree. The independent sharpness review
proved two scoped improvements, with 2,955 exhaustive-prefix checks, 20 larger
controls and 29 two-sided threshold checks. No Lean proof or external CPC kernel.

The completion claim is a proved procedure, implemented exact decisions and
auditable outputs at the declared trust level. It is not a fully formalized
strategic theorem or a general solver-free multivariate certificate implementation.

Main question unchanged. Growing dimension remains unresolved; prefix sharpness
does not imply hardness. The next confidence priority remains R08's strategic
bridge, before claiming a fully formalized enforcement result.
