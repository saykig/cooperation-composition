# Research north star: justified accumulation of partial knowledge

Adopted by the user on 13 August 2026. This is the living purpose of this research, distinct from Bellman's programme-wide north star. Bellman is its current home and a source of reusable mathematics; its existing architecture does not prescribe the research outcome.

## Purpose

Understand mathematically how partial knowledge can accumulate into a richer understanding of a system, while preserving the dependencies and assumptions needed to justify its conclusions—and allowing that understanding to be revised.

Combining descriptions should support additional justified consequences where possible, expose incompatibility where necessary, and make clear which conclusions change or cease to be supported when assumptions or mechanisms change. Combining descriptions does not manufacture independent evidence. Mathematical guarantees are conditional on explicit premises; empirical adequacy requires separate justification.

Better real-world decisions are the long-term motivation. Strategic actors, scientific hypothesis formation, general world models and compression are possible applications or techniques, not required subjects of this research or its first paper.

## Working research question

Given partial knowledge and a declared class of operations, what must be retained so that combining, revising and intervening on models produces justified conclusions and reveals which earlier conclusions no longer hold?

This wording is revisable in light of mathematical evidence and user clarification. A narrower paper question must earn its place by advancing this purpose.

## Three levels to keep distinct

1. **Research north star:** cumulative understanding that remains justified as knowledge and models change.
2. **Paper question:** one precise, bounded mathematical problem with stated objects, assumptions, operations and an attainable claim. Its selection remains open.
3. **Current clarification goal:** compare credible candidate questions, perform targeted literature checks and minimal discriminating probes, and deliver a justified recommendation with an executable next-experiment specification. Do not automatically begin the larger programme on completion.

## What counts as progress

- An explicit connection to established theory that provides a needed capability.
- A sound composition or revision rule with a useful domain of applicability.
- A counterexample identifying an essential dependency, assumption or interface restriction.
- A method that identifies which conclusions survive a change and which must be withdrawn or recomputed.
- A justified experiment that distinguishes candidate foundations or exposes a substantive remaining obstacle.

Novelty is optional. A rigorous synthesis, useful specialization, reproducible method or negative result can advance the research. Neither a new universal algebra nor publication readiness is presumed.

## Mathematical discipline

Specify what each component may observe, expose or change: named inputs and outputs, allowed intervention targets, and shared dependencies. Distinguish epistemic coupling between mechanism choices from shared physical randomness and dependence between evidence sources.

Soundness means no unsupported conclusions relative to declared premises. Exactness means preserving the designated answers of the detailed reference representation. A vacuous sound answer is not enough: assess useful inferential content as well.

Revision may rightly invalidate old conclusions. Initially consider adding or withdrawing a constraint and replacing a named mechanism; changes in variable meaning require further treatment. Finite acyclic models and exact arithmetic are provisional test settings, not the research ceiling.

Compare existing information/valuation algebra, compatibility, causal abstraction and observational-completeness results where relevant. A literature gap is not established by a terminology difference. Do not require compression to become the central problem.

## Relationship to Bellman and the research record

Treat existing Bellman components as candidates for reuse, later use or eventual supersession. Do not force the research into them. Changes to active architecture require a subsequent justified decision; historical evidence remains recoverable and is not silently rewritten.

The completed first investigation is indexed by [CURRENT_STATE.md](CURRENT_STATE.md), with its [research note](manuscript/RESEARCH_NOTE.md). Those results are starting evidence, not constraints on the next question. Keep subsequent clarification work explicitly dated and separate; retain sources, proofs, rejected alternatives and actual computational evidence.

Keep this file as the canonical statement of research purpose. Current-state notes describe what has been earned and what is next; manuscript files develop particular arguments. Link to this statement rather than maintaining competing copies.

## Current operating constraint

The research-clarification phase is uncommitted exploration: no Git commits, pushes, new branches, destructive cleanup or architecture migration. Save reviewable working notes separately from completed evidence. This temporary constraint follows the user's current request and can be changed by subsequent instruction.

---

## September 20, 2026 clarification — interoperable decision-making programme

This section **adds to rather than replaces** the August 13 north star above.

The earlier purpose remains valid: justified conclusions must survive combination,
revision and intervention only when their required assumptions and dependencies
have been preserved.

The broader programme is now clearer.

### Broader programme

The long-term objective is to build **reusable mathematics for consequential
decision-making under uncertainty, strategic interaction and changing information**.

“Universal” does not mean one equation that predicts war, cooperation, bargaining
or any other complex outcome. It means that the underlying mathematical pieces
should be reusable across different domains when their declared assumptions and
interfaces match.

The intended architecture is closer to interoperable mathematical components:

- one component may represent uncertainty and belief revision;
- another may represent dynamics and state change;
- another may represent strategic interaction;
- another may represent incentives and enforcement;
- another may represent bargaining, commitment or institutions;
- composition rules determine when these pieces can be connected safely; and
- compression rules determine what information can be discarded without changing
  the decisions or guarantees the connected system is supposed to preserve.

The substantive variables can change across security, AI governance, biosecurity,
corporate coordination or other domains. The goal is that the mathematical
interfaces do not have to be reinvented from first principles every time.

### Current proving ground

The present thesis uses **cooperation and enforcement under connected information
structures** as the proving ground for this broader programme.

The current paper-level question remains approximately:

> How do connected information structures determine the incentives or enforcement
> required to sustain a specified cooperative arrangement?

The newer R15 compression work adds a deeper interface question:

> What is the smallest representation of an interacting system that preserves the
> enforcement decisions we need and remains valid under the compositions we intend
> to perform?

This does not replace the cooperation/enforcement question. It explains what a
reusable component would need to expose so that enforcement calculations can be
carried from one connected setting into another without rebuilding the entire
model.

### What interoperability should eventually mean

A mathematical component is genuinely reusable only if it states:

1. what information and assumptions it consumes;
2. what decision-relevant object it exposes;
3. which conclusions that object preserves;
4. how approximation error propagates;
5. what shared dependencies must remain visible when components are connected; and
6. when a downstream operation asks for information that the component has already
   discarded and therefore requires refinement or source recovery.

The R15 result is the first explicit enforcement-specific step in this direction:
it identifies a reusable information interface, an operational error measure and
composition rules inside the current benchmark.

### Domain relationship

War, deterrence and security are important analytical applications because they
stress-test decisions made under uncertainty, incomplete information, strategic
reaction and consequential incentives. They are **not** intended to be the
mathematical boundary of the programme.

The same underlying architecture should be testable in other domains, including
AI-lab coordination, biosecurity, institutional bargaining and other cooperation
problems, provided the corresponding components and assumptions are made explicit.

### Long-term trajectory

The intended research trajectory is:

```
reusable representations of uncertainty and strategic structure
    -> reliable composition of decision components
    -> better reasoning about incentives, enforcement and bargaining
    -> better-designed interventions and institutions
    -> potentially more robust cooperation and consequential decision-making
```

The final step is a motivation, not a theorem. Mathematical stability of a
cooperative arrangement does not establish that the arrangement is desirable,
peace-promoting, efficient or worth its enforcement cost. Those claims require
separate normative and empirical arguments.

### Research discipline for this broader programme

Do not broaden the model merely to make the programme sound universal. Generality
must be earned by a theorem, construction, counterexample or interface that
survives a declared change of domain or operation.

Conversely, do not dismiss an ambitious direction merely because neighboring
literatures contain some of its ingredients. Use existing mathematics aggressively.
The relevant novelty question is whether prior work actually supplies the
representation, composition rule, guarantee or impossibility result needed by the
programme under matching assumptions.

The cooperation/enforcement benchmark remains the active proving ground until a
new abstraction earns a broader formulation.
