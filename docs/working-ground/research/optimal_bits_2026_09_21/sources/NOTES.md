# Literature comparison and priority boundary — September 21, 2026

Primary sources inspected online during this run:

1. E. M. Bronshtein, *epsilon-entropy of convex sets and functions*, Siberian
   Mathematical Journal 17 (1976), 393–398, DOI 10.1007/BF00967858.
   [Original publisher-linked bibliographic record](https://www.mathnet.ru/eng/smj4021).
   The record establishes author/title/year; the Russian original proof was not
   independently translated or reconstructed in this run.
2. R. J. Gardner, M. Kiderlen and P. Milanfar, *Convergence of algorithms for
   reconstructing convex bodies and directional measures*, Annals of Statistics
   34 (2006), 1331–1374.
   [Author-hosted extended paper](https://faculty.gardner.wwu.edu/GKMExtendedversion.pdf),
   Proposition 5.4, PDF page 15; [arXiv record](https://arxiv.org/abs/math/0608011).
   This explicitly states Bronshtein's matching Hausdorff entropy order
   epsilon^(-(d-1)/2) for all compact convex subsets of a bounded ball. It counts
   logarithms of cover cardinality, so it directly addresses information bits.
   No smoothness or nonempty interior assumption is needed for that class.
3. I. Diakonikolas and M. Yannakakis, *Succinct Approximate Convex Pareto Curves*,
   SODA 2008. [Author page and abstract](https://www.cs.columbia.edu/~ilias/papers/convex-pareto.html).
   Their optimization-oracle and minimum-cardinality Pareto approximation problem
   is relevant to the frontier, but vertex count alone is different from arbitrary
   binary encoding length and source-relative enforcement assurance. Only this
   abstract was read anew here; do not claim a full-paper priority exclusion.

The targeted search also sought multiscale/dyadic/Faber–Schauder convex-curve
coding. It did not produce a source establishing priority for this exact rational
frontier implementation. Failure to find such a source is not evidence of novelty.
The tent expansion, integer composition enumeration and metric-entropy principle
are standard ingredients. R16 supplies a self-contained proof instead of relying
on an unverified assertion about a specific earlier coder.

## What the comparison settles

The generic geometric logarithmic gap was already settled by classical entropy,
although R15's specific vertex-list encoder retained a logarithm. R16's planar
construction removes it using a uniform rational bitstream. Its higher-dimensional
existence/finite algorithm imports the entropy theorem openly. Neither geometric
rate is claimed original. The meaningful assurance questions are the query
semantics, composition budget, source binding and computation model.

## CANDIDATE ORIGINAL THEOREM — budget-sensitive certified enforcement interface

This label concerns the following combined enforcement-specific statement,
not a claim to have discovered convex entropy, the R15 metric, or product addition.

**Exact statement and assumptions.** Under R13's independent hard-evidence game,
favorable existential equilibrium selection, rational compact convex source
families in a fixed positive box, all contextual order/cost queries, a uniform
deterministic codec, and a source-readable exact verifier:

* planar self-contained query bits plus additional certificate bits have minimax
  rate Theta(gamma^-1/2), attained with a rational domination sandwich and zero
  additional witnesses when verification work is allowed;
* up to k independent repeated uses of the same payload change this per-payload
  rate to Theta((k/gamma)^1/2); unlimited repetition forces unbounded worst-case
  bits, even on one-coordinate rational singletons;
* finite tree-labelled conditional products inherit the certified margin interval
  with the exact max-sum budget E defined in `math/EXTENSIONS.md` (the budget is
  exact as an aggregation of local bounds; actual strategic error can be smaller).

**Proof.** Gate 1 gives rational contextual distinguishability; Gate 2 gives the
collision/amplification argument and audit model; Gate 3 gives the rational
multiscale upper bound and source-readable check; audited R15 packing gives the
lower bound; `EXTENSIONS.md` proves the finite-label/tree assurance. These are
complete written arguments, with adversarial boundary controls in the experiments.

**Closest known results and borrowed ingredients.** Bronshtein settles the
geometric information rate. R15 already proves operational discrepancy,
one-sender attainment, product addition and finite shared-label safety.
Concavity, dyadic interpolation, stars-and-bars and tree elimination are borrowed
elementary methods. The candidate contribution is making the achievable bit rate
and its impossibility boundary agree with a declared enforcement/audit contract.

**Priority uncertainty.** This package may be best viewed as a synthesis and
corollary of established geometry plus R15 rather than a publishable original
theorem. No independent literature expert or human proof reviewer has assessed
priority. Decision-preserving coding, approximate abstraction and compositional
verification may contain equivalent contracts under other terminology. Do not
promote this candidate label into a novelty claim.

**Lean plan.** First finish the R08/R14 assessment predicate and both backward
existence arguments. Next define H and the directed discrepancy; prove rational
domination implies its bound, the contextual margin inequality via the established
minimax statement, and the rational-query continuity/attainment bridge. Prove
product addition and derive the repeat-collision impossibility. Then formalize
finite branch max/min interval transport and the tree budget induction. The
binary encoder and entropy bound are lower priority than this thesis-bearing
assurance chain. No large Lean development was started in this run.
