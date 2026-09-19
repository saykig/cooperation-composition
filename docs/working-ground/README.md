# Working ground

The research trajectory behind Cooperation & Enforcement, beginning August 13,
2026. This area collects the mathematical questions, proofs, counterexamples,
literature notes, experiments and changes of direction in one place.

- [Research progress](PROGRESS.md)
- [Decisions, failures and corrections](DECISIONS.md)
- [How to revisit and extend the work](RECOVERY.md)
- [Verification ledger](VERIFICATION.md)
- [Formalization backlog](FORMALIZATION_BACKLOG.md)

## Research phases

| Date | Research |
|---|---|
| August 13, 2026 | [Partial knowledge and causal foundations](research/foundations/manuscript/RESEARCH_NOTE.md) |
| August 13, 2026 | [Revision, provenance and mechanism versions](research/clarification_2026_08_13/RECOMMENDATION.md) |
| August 14, 2026 | [Shared information budgets and incentives](research/information_incentives_2026_08_14/manuscript/RESEARCH_NOTE.md) |
| August 14, 2026 | [Partial certificates and enforcement](research/partial_certificate_frontier_2026_08_14/manuscript/RESEARCH_NOTE.md) |
| August 14, 2026 | [Disclosure discontinuity boundaries](research/disclosure_boundaries_2026_08_14/manuscript/RESEARCH_NOTE.md) |
| August 14, 2026 | [Optimized gates and recovery](research/optimized_gate_recovery_2026_08_14/manuscript/RESEARCH_NOTE.md) |
| September 9, 2026 | [Sequential disclosure and compatible uncertainty](research/sequential_disclosure_2026_09_09/manuscript/RESEARCH_NOTE.md) |

Each phase includes its available mathematical development, source notes,
experiments, evidence and limitations. The latest phase returns to the composition
question through sequential hard evidence: it derives an exact disclosure-order
criterion and shows that preserving a shared constraint on uncertain local
probabilities can change the robust enforcement requirement even after optimizing
the disclosure order. Novelty and empirical validity remain open. The earlier
large revision experiment remains unrun.

Use the progress and decision ledgers to add later work and corrections. Keep
mathematical proofs, numerical checks and formal verification clearly distinguished.

## Latest result — R09, September 19

[Robust disclosure orders over polytopes](research/robust_order_polytope_2026_09_19/README.md)
gives an exact certificate for a common zero-fine order, sharp counterexamples to
vertex/local-summary shortcuts, and a no-adaptation result for the AND benchmark.
The historical R09 result is preserved; R10 below resolves its next segment-selection attack.

## Latest result — R10, September 19

[Two-prefix selection](research/two_prefix_selection_2026_09_19/manuscript/RESEARCH_NOTE.md)
proves that a common zero-fine order on a rational segment exists exactly when
a prefix of at most two senders works. Selection is polynomial in input bit size.
An implemented exact selector returns checkable success or all-pair rejection
certificates. The dimension-d bound d+1 is proved and attained for d=0,1,2,3;
R11 below establishes the general construction with dimension-dependent payoffs.

## Latest result — R11, September 19

[General sharpness](research/general_sharpness_2026_09_19/manuscript/RESEARCH_NOTE.md)
constructs, for every d, a rational d-dimensional family requiring a prefix of
exactly d+1 senders. The proof specifies thresholds approaching one. It separately
resolves all twenty missing dimension-four witnesses and proves why fixed-q and
fixed-threshold versions of this particular construction fail. Arbitrary-family
sharpness at fixed τ=2/3 remains open. The next algorithmic target is exact
selection over rational polygons; sharpness does not imply hardness.
