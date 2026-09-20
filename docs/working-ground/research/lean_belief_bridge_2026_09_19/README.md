# R14 — Lean belief and continuation bridge

Started 19 September 2026. Belief milestone checked 20 September; the receiver
and continuation part of the goal remains active.

Formalize R13 for arbitrary finite sender counts from independent Nature draws,
feasible history-dependent behavior, transcript likelihoods and Bayesian
conditioning. Prove unique consistent beliefs, existence and uniqueness of
off-path limits, receiver best replies and sender continuation gains. Do not
replace the strategic derivation with assumed suffix inequalities.

The game and main research question are unchanged. Growing-dimension complexity
is outside this gate. Full sequential-equilibrium existence beyond this bridge
will be itemized explicitly, not silently claimed.

## Proof architecture under development

1. Finite binary state masses and normalization from independent Nature draws.
2. Conditional action likelihoods: type zero cannot report; positive types use
   their behavioral probability at the observed earlier transcript.
3. Factorization and normalization of Bayes conditioning under fully mixed play.
4. A continuous posterior extension, explicit fully mixed perturbations, and
   uniqueness of every consistent off-path limit.
5. Receiver payoff comparisons from the posterior all-positive probability.
6. Finite continuation-tree expectations, then the sender deviation gain.

Every formal theorem will be mapped to its strategic interpretation and assumptions.
Only standard Lean/Mathlib axioms will be accepted; no admitted proofs or custom
axioms may support a completed milestone.

## Completed belief milestone

`lean/Beliefs.lean` and `lean/Transcripts.lean` compile with Lean 4.33.1 and the
pinned Mathlib revision. A fresh-build [receipt](results/lean_beliefs_2026_09_20.json)
audits all 64 local declarations: only `propext`, `Classical.choice`, and
`Quot.sound` appear. This includes actual transcript/private-type conditioning,
one global consistency sequence, and uniqueness against arbitrary converging
fully mixed strategies. It is not a complete sequential-equilibrium proof.

See the [formal statement map](math/FORMAL_SCOPE.md) for assumptions and gaps.

Replay from a built matching Mathlib cache:

```sh
python3 lean/verify.py --packages /path/to/.lake/packages --modules Beliefs Transcripts
```

The verifier builds fresh local objects in a temporary directory and audits every
local definition and theorem. Caches and build outputs are not committed.
