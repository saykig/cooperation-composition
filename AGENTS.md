# Cooperation & Enforcement project instructions

## Repository boundary — September 21, 2026

This repository is the application and proving ground for the Ukraine-focused CEES
paper: empirical evidence, case interpretation, application-specific modelling and
evaluation. `https://github.com/saykig/decision-interfaces` is now canonical for
future theorem development, proofs, verification and mathematical provenance.
This handoff supersedes the former instruction to put all project research here.

For application work, use this checkout and verify origin points to
`saykig/cooperation-enforcement` before committing or pushing. For mathematical
foundation work, use the separate decision-interfaces checkout and its own origin;
never repoint this remote. Read the foundation
[research programme](https://github.com/saykig/decision-interfaces/blob/91bfb6fc58ff33959e6f5c9029c8a3e32c789509/RESEARCH_PROGRAMME.md)
for the ownership and citation contract.

Cite foundation results using a full 40-character decision-interfaces commit SHA,
exact file/result, assumptions and evidence status. Treat upgrades as explicit
changes to application dependencies. Mathematical results are conditional on their
premises; Ukraine hypotheses require separate empirical support.

Preserve all existing mathematical files and history here for later user-directed
cleanup. Route new reusable mathematical results and corrections to the foundation
repository, then cite them here. Both README files are reserved for the user's own
revision; do not change them as part of this handoff. Their existing research
ownership language predates the boundary recorded here.

## Working practice

- Do not create branches unless the user instructs you to.
- Commit and push coherent milestones regularly. Respect any task-specific
  request to review changes before committing or pushing.
- Preserve other chats' uncommitted work; stage only the current task's changes.
- The research home is `docs/working-ground/`. Read its README, PROGRESS.md and
  DECISIONS.md before continuing the trajectory. Keep those ledgers current.
- Read the canonical north star at
  `docs/working-ground/research/foundations/NORTH_STAR.md`. Preserve the August 13
  statement and its September 20 clarification: the broader programme concerns
  interoperable mathematics for consequential decision-making, while
  cooperation/enforcement is the current proving ground rather than the final
  domain boundary.
- Record corrections and failed approaches without erasing prior mathematical
  findings. Distinguish assumptions, proofs, computations and formal verification.
- For every new mathematical phase, update `docs/working-ground/VERIFICATION.md`
  in decision-interfaces, where that phase now belongs.
  Never write simply "verified": state the exact theorem/artifact and whether the
  evidence is a written proof, exact computation, numerical check, Lean proof, or
  independent external replay. Unformalized current mathematics must stay labelled
  as such.
- The historical research chronology starts August 13, 2026 as supplied by the
  author. Do not infer altered publication dates or verification timestamps.
- Do not add a separate provenance archive. Keep research directly organized in
  the working-ground area, with its source notes and necessary evidence.
