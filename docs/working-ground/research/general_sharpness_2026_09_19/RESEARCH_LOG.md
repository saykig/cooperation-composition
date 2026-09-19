# Research log — R11 general sharpness gate

## September 19: authoritative-state audit and optimization

Started from clean main `807791b`. Re-read live R10 sharpness notes, executable and
receipt, the project instructions and ledgers. Confirmed all twenty unresolved
four-prefixes begin with sender 0 in executable indexing. No archived source was
rewritten and no branch was created.

The configured Python runtimes lacked SciPy. Installed pinned NumPy/SciPy in a
temporary environment outside the repository. Formulated a convex hypograph
problem for each minimum log margin, then made candidates rational and solved
the last coordinate from the affine equation. All twenty strict witnesses passed.
Added global upper bounds using rational tangent weights, exact continuous-knapsack
support and rational logarithm enclosures. The widest optimal-margin bracket is
4.6197·10^-8. This closes the individual cases without a search-failure inference.

The first push encountered independently published repository verification-ledger
and CI commits. Read the new instructions, preserved those commits, and rebased
only the unpublished local milestone onto them. No force-push or branch creation.
The resulting milestone `5518615` was pushed. The new instruction requires each
phase to update VERIFICATION.md; the completion milestone does so and adds R11
replay steps without broadening the existing Lean coverage claim.

## September 19: a general construction

The structure of prefixes starting with 0 suggested working with deficits near
one. Nonzero first senders can absorb the affine deficit budget immediately. For
prefixes beginning with 0, later running maxima partition labels into consecutive
blocks. Any prefix that is one sender too short leaves at least one block of size
two, giving a positive surplus in its weighted deficit sum. Normalize that vector,
mix slightly with the all-ones vector, and choose a dimension-dependent rational
ε to preserve all strict inequalities after converting deficits into probabilities.

Completed a proof with actual dimension d, a universal successful (d+1)-prefix,
explicit defeating witnesses for every shorter prefix, and a uniform rational
product margin. Both q_d and τ_d approach one; their formulas are part of the
statement. Tested every relevant prefix for m=2,...,7 (23,115 cases), plus 75
structured/random cases through m=100. These tests did not replace the proof.

## September 19: kill overgeneralizations

Proved that the original q=4/5 uniform-AM-GM ansatz has a singleton blocker for
m≥11, even if the threshold is increased. Proved a second ansatz-specific bound:
for fixed τ<1, it has a singleton blocker for all sufficiently large m regardless
of q, and for τ≤2/3 this holds for every m≥2. Retained R08's τ=2/3 counterexample
to any attempt to turn this into a universal one-prefix theorem for the game.

The gate therefore earns a general sharpness theorem, while leaving arbitrary
families at fixed τ=2/3 open. No segment-hardness, vertex-only success, adaptation
or other settled branch was reopened. The next algorithmic target is exact
selection beyond segments. Novelty and proof-assistant verification remain separate.
