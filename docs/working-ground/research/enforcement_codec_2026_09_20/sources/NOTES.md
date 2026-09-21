# Targeted source comparison — September 20, 2026

This is a bounded comparison, not a systematic historical-priority audit.

## Existing mathematical foundations

- Diakonikolas and Yannakakis, *Succinct Approximate Convex Pareto Curves*:
  compact epsilon-convex Pareto representations and minimum-size questions.
  https://www.cs.columbia.edu/~ilias/papers/convex-pareto.html
- Daskalakis, Diakonikolas and Yannakakis, *How Good is the Chord Algorithm?*:
  succinct convex-curve approximation and comparison with optimal representations.
  https://epubs.siam.org/doi/10.1137/13093875X
- Arya, da Fonseca and Mount, *On the Combinatorial Complexity of Approximating
  Polytopes*: source for the classical
  `O(epsilon^{-(d-1)/2})` vertex-approximation rate used in the upper bound.
  https://arxiv.org/html/1604.01175v4
- Arya and Mount, *Optimal Volume-Sensitive Bounds for Polytope Approximation*:
  cross-check on classical worst-case approximation rates.
  https://arxiv.org/abs/2303.09586
- Rahul Arya et al., *Optimal Bound on the Combinatorial Complexity of
  Approximating Polytopes*: removes a logarithm for a different face-complexity
  measure; it does not automatically remove the rational encoding logarithm here.
  https://arxiv.org/abs/1910.14459

Earlier working-ground phases already compare information bottleneck,
decision-preserving representations, BCE/information-structure comparison,
abstract-domain completeness and the strategic disclosure literature.

## Candidate contribution to test

Do not claim generic Pareto compression or convex approximation as new. The
narrower package whose priority remains to be established is:

1. exact equality between directed representation discrepancy and worst contextual
   enforcement-margin error;
2. exact error addition under independent strategic composition;
3. enforcement-calibrated representation-size lower bounds;
4. a proof-carrying rational codec with zero/full/refine semantics; and
5. a finite shared-label interface rule with a failure example when the interface
   is erased.
