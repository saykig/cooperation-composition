# Sources and borrowed machinery

September 20, 2026. This phase formalizes the existing R13 bridge. It does not
claim a new equilibrium concept, a new independence theorem, or publication novelty.

1. **Game specification and written proof:** R13's
   [independent audit](../../game_cascade_audit_2026_09_19/math/AUDIT.md), sections
   1–4, at parent commit `c0311bd`. The primitives and equilibrium interpretation
   are unchanged. Sections 5–6 contain the backward construction and minimum-fine
   theorem, which remain outside the present formal bridge.

2. **Sequential-equilibrium interpretation:** R13's
   [source notes](../../game_cascade_audit_2026_09_19/sources/NOTES.md) record the
   consulted author exposition by Bonanno, *Game Theory*, Definitions 12.1.1 and
   12.2.1, and the Kreps–Wilson publication record. R14 uses the same definition:
   limits of completely mixed feasible profiles, not limits of equilibria.
   These source notes are not upgraded into a claim of a new full-paper reading.

3. **Finite distributivity:** the pinned Mathlib source
   [`Fintype.prod_sum`](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Algebra/BigOperators/Ring/Finset.lean)
   changes the sum over all Boolean states of a product of coordinate factors
   into the product of their two-point sums. This standard identity proves prior
   normalization, Bayesian factorization, and the future-state expectation. Its
   premises and implementation were inspected locally at that exact revision.

4. **Continuity and limits:** the same pinned Mathlib's `Tendsto.div`, finite
   product convergence, `tendsto_nhds_unique`, and
   [`tendsto_one_div_add_atTop_nhds_zero_nat`](https://github.com/leanprover-community/mathlib4/blob/0df444a360eaa60ab8c11dca51a86af692955474/Mathlib/Analysis/SpecificLimits/Basic.lean)
   supply established analysis. The game-specific step is proving the limiting
   silent-message denominator stays positive. Zero-probability report factors are
   cancelled while the profiles are completely mixed, before limits are taken.

5. **Trust boundary:** Lean 4.33.1, Mathlib commit
   `0df444a360eaa60ab8c11dca51a86af692955474`. The verifier compiles fresh local
   objects against that revision and checks every named local definition, abbreviation,
   lemma and theorem against the allowed dependency list `propext`,
   `Classical.choice`, `Quot.sound`. It rejects missing audits and `sorryAx`.
   No external registry, second kernel or independent human model review is claimed.

The probability and real-analysis machinery is borrowed. The formal specialization
and strategic statement map are this phase's contribution to project assurance.
