# Completion audit

19 September 2026. First executable/proof milestone: `9df1f77`.

| Requirement | Authoritative evidence | Assessment |
|---|---|---|
| Reconstruct declared game | `math/AUDIT.md` §1 against R08 §5 at parent `a166031` | same primitives, timing, actions, observations, fine incidence and target |
| Beliefs and consistency | §2: factorization, positive denominators, uniqueness and explicit fully mixed sequence | complete written argument including off-path histories |
| Independent continuation derivation | §3–4 receiver payoffs and tree enumeration before suffix tests | no assumed continuation formula |
| Both directions | §5 rules out all mixing on strict branch; constructs consistent equilibrium on weak branch | arbitrary-n written proof |
| Fine exactly 0 or B | §6 gives full feasible-fine set including B | attained minimum under original ties |
| Small-game checker | `game.py`, `mixed.py`, `check.py`, `results.json` | two/three senders, selected four, off-path plans, arbitrary real mixing and boundary cases |
| Independence | formula only in comparison function `historical_prediction` | no data flow from formula to solvers; beliefs also checked with separate polynomial limits |
| Falsification | mixed-rescue tests, noncredible threat rejection, tie controls | original theorem survives; all-equilibria overstatement refuted |
| Downstream implications | `IMPLICATIONS.md` | no algebraic correction; original strategic scope retained |
| Replay | pinned exact backend, Fraction arithmetic, normal/optimized receipts agree excluding time | original source hashes retained; old R08 receipt untouched |
| Records and scope | research/verification ledgers and formalization backlog | main question/game preserved; no growing-dimension work |

The arbitrary-n proof is informal, not Lean checked. Mixed queries trust Z3;
rational payoff/tremble evaluation does not need SMT. No independent human review,
external proof-kernel replay or novelty claim is asserted. Full formalization is
a subsequent confidence goal, not a missing step in the requested written audit.
No known proof gap remains under the stated original assumptions.
