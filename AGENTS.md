# Cooperation & Enforcement — project instructions

## Repository scope

This repository is the application and proving ground for the Ukraine-focused
European-security paper.

Use it for:

- empirical evidence and source assessment;
- Ukraine-specific hypotheses and interpretation;
- application-specific modelling and simulations;
- methods and operationalization;
- concise mathematical statements actually used by the paper.

Do **not** use this repository as the home for broad theorem development,
mathematical provenance, formal-verification trails, or reusable mathematical
research that is not yet part of the application.

## Mathematical dependencies

The paper's mathematical dependencies are currently unresolved.

Do not pin, import, or present a mathematical theorem as a dependency merely because
it is interesting or potentially relevant. A result becomes an application
dependency only when the paper actually uses it.

When that happens, record in this repository:

- the exact mathematical statement used;
- its assumptions;
- how application quantities map to those assumptions;
- its evidence/verification status;
- what substantive claim in the paper depends on it.

Keep proofs, discovery logs, failed approaches, and general theorem provenance out
of this repository unless they are necessary to understand an application-specific
derivation.

## Working practice

- Do not create branches unless the user instructs you to.
- Commit and push coherent milestones.
- Preserve empirical uncertainty and distinguish evidence from interpretation.
- Treat simulations as tests of declared assumptions, not as empirical proof.
- Keep the paper centered on Ukraine unless the user explicitly expands the case
  scope.
- Do not let the degree requirement limit the broader mathematical research
  programme; this repository is only the application paper.
