# Mathematical dependencies

**Status: not yet fixed.**

The application paper is still determining which mathematical results it actually
needs. No theorem, model, or external mathematical framework should currently be
treated as a committed dependency simply because it may later be useful.

When a result becomes necessary for the paper, add an entry with:

1. **Statement used** — the precise mathematical claim.
2. **Assumptions** — conditions under which it holds.
3. **Application mapping** — how Ukraine-case variables/structures correspond to
   those assumptions.
4. **Evidence status** — written proof, formal proof, exact computation, numerical
   evidence, etc.
5. **Paper dependency** — the exact hypothesis, inference, model, or section that
   relies on it.
6. **Limitations** — what the theorem does not establish about the real case.

The purpose of this file is to keep the application intellectually honest without
turning this repository back into a mathematical provenance archive.
