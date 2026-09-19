# Sources and interpretation audit

Inspected 19 September 2026. This phase audits an existing game; it makes no new
literature-gap or historical-novelty claim.

1. **R08 declared source:** `sequential_disclosure_2026_09_09/manuscript/RESEARCH_NOTE.md`,
   §5 Model, Receiver lemma and Theorem; §6 quantifiers for shared uncertainty.
   Re-read from current repository state at parent `a166031`. The audit preserves
   the message sets, observation structure, timing, payoff location of the fine,
   independence, strict prior bound, positive costs and target-existence criterion.
   Its detailed proof is additive; the historical note and receipt are unchanged.

2. **Kreps and Wilson (1982), Sequential Equilibria**, *Econometrica* 50,
   863–894. [Author institution record](https://www.gsb.stanford.edu/faculty-research/publications/sequential-equilibrium),
   [publication DOI](https://doi.org/10.2307/1912767). The record confirms sequential
   rationality with beliefs at off-path information sets. The archived original
   PDF could not be retrieved in this run; do not imply the full original was read.

3. **Giacomo Bonanno, Game Theory**, author-hosted
   [text](https://faculty.econ.ucdavis.edu/faculty/bonanno/PDF/GT_book.pdf),
   Chapter 12, Definition 12.1.1 (printed p.445) and Definition 12.2.1 (p.449).
   The author's exposition specifies consistency through limits of completely
   mixed profiles and their Bayesian beliefs; sequential equilibrium adds
   sequential rationality. This is the exact definition used here. In particular,
   perturbing profiles need not themselves be equilibria. We borrow this standard
   definition, not the game-specific posterior factorization or enforcement result.

4. **Z3 author documentation:**
   [Z3 Internals](https://z3prover.github.io/papers/z3internals.html), nonlinear
   real arithmetic. The supplementary arbitrary-mixed finite-game checker uses
   pinned Z3 4.15.3.0 QF_NRA. A real-variable best-reply system is not a numerical
   mixture grid. Solver answers remain trusted executable evidence, not a Lean
   or external kernel proof.

The hard-evidence/sequential-disclosure literature recorded in R08 remains relevant
to eventual novelty assessment. It is not used as a substitute for reconstructing
this game's own primitives. No general persuasion theorem is claimed or needed
for the audit.
