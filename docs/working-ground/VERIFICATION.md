# Verification ledger

**Last structural audit:** September 19, 2026.

This file records what kind of evidence exists for each mathematical phase. It is
deliberately conservative. A written proof, an exact finite computation, a
numerical optimizer, and a proof-assistant check establish different things.

## Vocabulary

- **Written proof** — an informal mathematical proof is recorded in the phase.
  It may still contain a human error.
- **Exact check** — finite examples, exhaustive searches, rational arithmetic or
  certificate verification were recomputed without floating-point tolerance.
  This can falsify and independently check formulas on the declared cases; it is
  not a proof of an arbitrary continuum statement unless the certificate itself
  covers that continuum.
- **Numerical check** — floating-point optimization or sampling supports the
  calculation. Residuals and failures must remain visible. This is not proof.
- **Lean checked** — the named formal statements compiled in Lean without
  `sorry`/custom axioms beyond the explicitly recorded standard dependencies.
  This verifies the formal statement, not that it faithfully models the intended
  strategic situation.
- **Independent kernel / external replay** — the same formal statement has been
  replayed by a separate checker or external registry. **None of the current
  thesis results has this status yet.**
- **Open / unrun** — proposed work or a claim not yet covered by one of the above.

Never write simply "verified" in this repository. State **what was verified and
by which method**.

## Phase matrix

| Phase | Main mathematical content | Computation | Formal proof status | Main remaining verification gap |
|---|---|---|---|---|
| R01 foundations | relational compatibility, gluing, replacement and stochastic/causal extensions | exhaustive finite relation/kernel checks; signature enumeration | **Lean checked:** selected relational core in `foundations/lean/Compatibility.lean` | finite DAG normalization, stochastic marginal/intervention theorem and full query-signature results are not formalized |
| R02 clarification | provenance-sensitive revision and mechanism-version examples | exact small probes; retained 32/0/20 counts | none | the larger 96-record experiment was specified but never run; general revision theory is not proved |
| R03 information incentives | shared information budgets, six-branch benchmark, disclosure benchmark, tree/KL identities | exact arithmetic plus NumPy/SciPy optimization and independent original-cell checks | **Lean checked:** four narrow algebraic/disclosure lemmas | game-to-formula derivation, KL duality, tree gluing, PBE correspondence and full Theorems A–G are not formalized |
| R04 partial certificates | three-state robust frontier, cost profiles, upper-image composition, disclosure obstruction | exact finite queries plus numerical original-cell checks | **Lean checked:** six profile/disclosure/determinant lemmas | entropy/conjugacy, complete game equilibrium and network elimination remain written proofs |
| R05 disclosure boundaries | information-only discontinuity criterion and full boundary classification | exact rational witnesses plus numerical source-law optimization | **Lean checked:** fixed-information disclosure game and threshold bridge | global continuity classification, KL family optimization and overlapping-certificate theorem are not formalized |
| R07 optimized gate recovery | optimized discontinuity counterexample and compact recovery boundary | **2,025 exact rational checks** with separate producer/receiver roles | none | counterexample, full-information smoothing theorem and recovery statements remain written proofs; the general recovery principle is borrowed optimization theory |
| R08 sequential disclosure | exact disclosure-cascade/order criterion and shared-family vs separate-range enforcement gap | historical **4,802 exact rational checks** are documented, but the originating executable was not retained; R13 adds a separate independent primitive-game suite | none | R13 supplies a complete written strategic audit; formalization and the original historical executable remain missing |
| R09 robust order polytope | minimax certificate, projection boundary, ordering/adaptation results, fixed-order segment verification | **15,653 exact rational checks**; replayable Python suite | none | minimax specialization, projection impossibility and no-adaptation theorem remain written proofs |
| R10 two-prefix selection | move-to-front lemma, Helly dimension bound, polynomial segment selector and sharpness through d=3 | exact certificate selector/checker, exhaustive small-order comparisons and retained receipts | none | the central R08→R10 theorem chain is not yet proof-assistant checked; current Python selector/checker share arithmetic code and are not an independent trusted kernel |
| R11 general sharpness | **Written proof:** arbitrary-d sharpness with dimension-dependent thresholds; fixed-q and fixed-threshold obstructions for the uniform-AM–GM ansatz | 20 numerical optimizations followed by exact rational witnesses and certified supremum brackets; 23,115 exhaustive-prefix checks plus 75 higher-dimensional controls; exact certificate replay | none | arbitrary-d theorem and strategic fidelity remain unformalized; fixed τ=2/3 sharpness outside this ansatz and historical novelty remain open |
| R12 fixed-dimensional selection | **Written proof:** polynomial-bit decision/order output at fixed affine dimension; two scoped sharpness refinements | 14 saved bundles replayed; 132 direct full-order comparisons with independent cvc5 encoding, 42 prior-Sturm comparisons, three rational AM-GM success certificates; exact side-refinement checks | none; general emptiness uses solver-trusted replay, not an external CPC kernel | R08 strategic bridge remains unformalized; growing dimension unresolved; no complete solver-free polygon certificate format claimed |
| R13 independent strategic audit | **Complete written primitive derivation:** unique consistent beliefs, full mixed continuation conditions, both directions of R08 and attained fine 0 or B | 3,324 exhaustive pure profiles; 139 mixed real-arithmetic decisions; 142 constructed assessments; 312 polynomial-tremble belief checks; normal/optimized receipts agree | none; exact mixed solver retains backend trust | arbitrary-n game proof remains informal; fixed-order suite is not an exhaustive check of adaptive policies |

R06 was a preservation/trajectory phase and introduced no new mathematical claim.

## Continuous integration

`.github/workflows/research-verification.yml` reruns every retained executable
research suite that is suitable for CI and rechecks the existing Lean sources.
A green workflow means those specific programs/formal files passed at that commit.
It does **not** upgrade written theorems outside their coverage.

R08's original 4,802-check receipt remains non-replayable: no executable was
retained when the phase was transferred. R13 now supplies a SEPARATE independent
primitive-game suite and detailed derivation. Its counts/evidence must not be
presented as replay of the original historical checks.

## Why Lean, not "more languages"

Changing Python to Julia or Rust does not make mathematics true. Use another
implementation when it reduces a specific correlated-error risk.

Current priorities:

1. **Lean:** formalize the thesis-bearing R08→R10 chain.
2. **Independent exact checker:** a small Rust verifier for R10 certificates would
   be useful because the current Python verifier shares polynomial arithmetic with
   the producer.
3. **Julia:** use only if future convex/numerical work benefits materially from its
   optimization ecosystem; it would remain numerical evidence.
4. **Palomar:** consider only after a stable research theorem has a complete,
   fidelity-reviewed Lean statement and proof. Palomar is an external registry and
   replay layer for Lean-verified mathematics, not a substitute for building the
   formal proof in this repository.

See [FORMALIZATION_BACKLOG.md](FORMALIZATION_BACKLOG.md) for the order of work.
