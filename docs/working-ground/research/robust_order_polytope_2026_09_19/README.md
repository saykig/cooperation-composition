# R09 — Robust disclosure orders over polytopes

September 19, 2026. Start with the [research note](manuscript/RESEARCH_NOTE.md).

The strongest result is a necessary-and-sufficient weighted log-product certificate
for a common zero-fine order in R08's benchmark. Vertex-only evaluation fails;
a supporting-hyperplane certificate is finite and exact. Full pairwise feasible
regions suffice for three senders but fail at four. General order-selection
complexity remains open; rational-segment existence is in NP.

- [Brief](BRIEF.md), [current state](CURRENT_STATE.md), [author audit](AUDIT.md).
- [Characterization and certificates](math/CHARACTERIZATION.md).
- [Small counterexamples and sharp projection boundary](math/COUNTEREXAMPLES.md).
- [Ordering, adaptation and log-space structure](math/ORDER_AND_ADAPTATION.md).
- [Exact segment complexity boundary](math/COMPLEXITY_BOUNDARY.md).
- [Experiments](experiments/README.md): 15,653 exact checks, standard-library Python.
- [Primary-source comparison](sources/NOTES.md).
- [Rejected approaches](REJECTED_APPROACHES.md), [research log](RESEARCH_LOG.md).

No NP-hardness, global greedy solution, formal verification or novelty is claimed.
The central research question remains unchanged. Read the exact game assumptions
before transporting any result to another evidence or equilibrium model.
