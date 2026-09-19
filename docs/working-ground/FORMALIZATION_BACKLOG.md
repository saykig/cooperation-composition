# Formalization and independent-check backlog

The goal is not to formalize every exploratory calculation. Formal verification
should attack the assumptions on which later results depend and the claims most
likely to enter the thesis.

## Priority 0 — thesis-bearing chain

### 1. R08 game-to-cascade theorem

Formalize the finite sequential hard-evidence game far enough to prove the bridge

```
profitable all-positive disclosure cascade
iff
k_{pi_j} < eta_{pi_j} * product_{l>j} p_{pi_l}
for every position j
```

including favorable ties and the claim that the minimum fine is 0 or B in the
declared benchmark. This is the highest-value target because R09 and R10 inherit
this characterization.

**Current status:** written proof + historical exact checks; no Lean proof.

### 2. R10 move-to-front and short-prefix theorem

Formalize:

- suffix-product monotonicity under moving selected senders earlier;
- the move-to-front lemma;
- the finite Helly reduction to at most `min(n,d+1)` selected constraints;
- the segment corollary that a successful order exists iff a successful ordered
  prefix of length at most two exists.

Use an existing Mathlib Helly theorem if its hypotheses match exactly; otherwise
formalize the finite convex-family argument stated in `math/THEOREM.md`.
Do not formalize the software implementation as if that proved the game theorem.

**Current status:** written proof + exact selector checks; no Lean proof.

### 3. R10 exact algorithm statement

After the structural theorem is formalized, formalize only the mathematical
correctness specification of the certificate classes (constant blocker, strict
rational witness, complete sign cover). The Python implementation can remain a
program tested against that specification.

**Current status:** exact executable certificates, not a proof assistant.

## Priority 1 — independent implementation

### Rust certificate verifier for R10

Write a small independent verifier using arbitrary-precision integers/rationals.
It should parse the committed JSON certificate, reconstruct the pair polynomials,
check rational witnesses and independently implement Sturm-count/sign-cover
validation.

Do **not** share code or generated polynomial routines with the Python selector.
The point is implementation diversity, not speed.

**Current status:** not implemented.

### R12 polygon certificate boundary

R12 now supplies a different-backend, different-encoding exact replay (Z3 intrinsic
coordinates versus cvc5 original convex weights), plus independent Sturm checks
on segment slices. General success bundles still trust exact algebraic backends;
the CPC skeletons are not externally kernel-checked. Three special weighted-AM–GM
certificates are checked with rational arithmetic and a short written proof.

A general solver-free polygon emptiness checker is not implemented. Formalizing
the small AM-GM sufficiency statement would be tractable, but would certify only
that certificate format and would not close the more consequential R08 strategic
gap. Keep the priority order above. See
[R12's certificate statement](research/fixed_dimension_selection_2026_09_19/math/CERTIFICATES.md).

## Priority 2 — useful but not currently thesis-critical

- R09: formalize the weighted-certificate **sufficiency** and projection
  counterexamples before attempting the full Sion/minimax derivation.
- R07: formalize the model-specific optimized-jump counterexample only if it
  remains in the final paper. The abstract recovery theorem is established
  parametric optimization and is lower priority.
- R03–R05: extend existing Lean files only when the corresponding theorem survives
  into the final thesis. Existing formalizations already check the most
  error-prone algebraic bridges.

## External replay / Palomar

No result is currently recorded here as Palomar-registered.

A Palomar submission should be considered only when all of the following hold:

1. the theorem is stable enough to appear in the paper;
2. a small human-auditable Lean statement matches the informal theorem;
3. the Lean proof is complete and axiom-audited;
4. the game/model fidelity has been reviewed separately;
5. the exact public commit is frozen for external replay.

External registration would strengthen confidence in the formal proof artifact.
It would still not establish novelty, empirical relevance, or that the strategic
model is the right representation of a real institution.
