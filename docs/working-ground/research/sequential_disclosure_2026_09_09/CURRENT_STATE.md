# Current state — sequential disclosure and compatible uncertainty

**Date:** September 9, 2026

## Established in this phase

- Universal robustness is monotone in the family of information structures that
  must all be tolerated: enlarging that family cannot reduce the required fine.
- For fixed obedience inequalities, convex mixtures of already-admissible
  information kernels do not change the universal minimum fine.
- The proposed simultaneous all-silent multi-sender obstruction does not work in
  the declared unilateral-deviation model: one sender's deviation reaches a
  solo-message history, so joint-message restrictions do not supply the desired
  incompatibility.
- In the declared sequential complementary-evidence game, the minimum fine for
  any disclosure order has an exact closed-form criterion.
- A shared constraint on uncertain local probabilities can change the optimized
  robust enforcement answer. The supplied three-sender family needs fine 0; its
  separate-range relaxation needs fine 1.

## Not established

- Historical or publication novelty.
- A general theorem for arbitrary hard-evidence games, correlated private facts,
  coalitional deviations, on-path disclosure, multiple receivers, or unknown-law
  players.
- Empirical relevance to a real institution.
- Formal verification in Lean or another proof assistant.

## Strongest open direction

Characterize which sequential disclosure orders sustain a fixed arrangement
across every model in a jointly constrained uncertainty family, and determine
which shared dependencies must be retained to compute the enforcement threshold
correctly.

Rectangular uncertainty is already solved by the upper corner. The next useful
case should impose a declared shared structure such as a compact polytope and seek
a checkable necessary-and-sufficient certificate or a complexity result, rather
than merely restating optimization over all permutations and laws.
