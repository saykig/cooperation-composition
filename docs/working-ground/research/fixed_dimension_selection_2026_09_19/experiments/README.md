# Exact polygon selection

Install `requirements.txt` in a separate environment. Nothing is rounded to a
floating-point tolerance. A normal run of `check.py --output <new-directory>`
produces a receipt and complete instance/certificate bundles. `python -O check.py`
must give the same mathematical results; checks use explicit exceptions, not
Python assertions that disappear under optimization.

For an individual instance:

```sh
python selector.py input.json --output certificate.json
python verify.py input.json certificate.json
```

Input has `vertices` (a nonempty list of rational coordinate lists), `r` (positive
ratios) and `tau` (strictly between zero and one). Use integer or rational strings,
for example `"3/20"`; floats are rejected. Every input coordinate must satisfy
0<p_i<τ. Actual affine dimension must be at most two. Sender indices start at 0.
Redundant vertices, points and collinear inputs are supported; empty families,
invalid game parameters and higher dimensions are rejected explicitly.

`status=zero` returns a prefix, a full order, and an **exact-backend emptiness
certificate**. `status=positive` returns `fine=B` and a distinct rational witness
for every candidate prefix. This does not assert one model defeats every order.
`--timeout-ms` bounds an individual backend decision; timeout/unknown/disagreement
raises an error, never an answer. No practical polynomial-time bound is claimed.

## What must be trusted

| Claim | Evidence/check | Trust remaining |
|---|---|---|
| A prefix is defeated | original-vertex convex weights and strict products | Python integers/Fraction, small checker and input interpretation; no SMT solver |
| A prefix succeeds | reconstructed intrinsic NLSAT query AND independent closed barycentric cvc5 query are UNSAT | both exact solver implementations; primary geometry; independent encoding; platform |
| Saved CPC proof | full proof skeleton, digest and rule inventory retained; cvc5 internally checks regenerated proof | some covering steps are `TRUST`; saved text is not replayed by an external kernel |
| Some short prefix suffices | R10 written proof, recapitulated in this phase | informal Helly/move-to-front proof |
| Fine is 0 or B | R08 written strategic theorem | equilibrium modeling and game-to-cascade bridge, still unformalized |

The success checker **re-solves** the obligations. It is not the small solver-free
certificate checker used for R10 segments. The CPC digest checks file integrity,
not logical validity. The independent exact decision is the acceptance basis.
Do not call this external CPC verification or Lean verification. A portable
solver-free multivariate emptiness certificate remains future work, not a hidden
assumption of this implementation.

## Independence and fixtures

The primary uses rational affine reduction, polygon halfspaces, and forward
remaining-set products. The independent implementation imports none of that
geometry/formula code: it uses original convex weights, a closed domain, reverse
suffix recursion, and cvc5's covering strategy. One weight is substituted as one
minus the others. This reduces unnecessary equality elimination while retaining
an independent representation. It enumerates **full orders**, bypassing the
prefix theorem in the finite comparison.

The first retained run covers 14 designed instances and all 84 corresponding
full orders: the sharp triangle, a true two-dimensional vertex-miss rectangle,
a tangent polygon, a strict interval narrower than 10^-29, changing blockers,
separate witnesses, point/segment degeneracies, duplicates, endpoint/constant
ties, n=1, and six input/certificate failure controls of each kind. The narrow
interval defeats a specified prefix; another singleton succeeds on that instance.
Do not misreport that fixture as rejection of every order.

The actual run was about two seconds on the recorded machine. This is a fixture
measurement, not a scalability benchmark. See `evidence/results.json` for exact
versions, timings and source identities, and `evidence/certificates.json` for
replayable complete outputs. No old phase artifacts are modified.

Run `python additional_checks.py` for saved-bundle replay, 132 direct full-order
comparisons (including 48 transformed triangle orders), 42 comparisons with R10's
independent Sturm implementation, the narrow polygon, and three solver-free
AM-GM certificates. `evidence/additional-results.json` records this audit. Its
baseline source hashes are bound to milestone `0f94556`; resolve that identity
explicitly if later repairs change the baseline executable. Do not rewrite old
receipts to claim they tested new code.

## Failed implementation approaches retained as lessons

* Comparing Z3 `to_smt2()` strings failed because temporary internal expression
  identifiers can change between reconstructions. Stable SMT expressions are now
  used for binding; rebuilding the mathematics remains required.
* Retaining a redundant barycentric equality made the initial triangle check
  unnecessarily slow. Eliminating one weight reduced it to two variables.
* Requiring cvc5 CPC output with no trusted steps aborted on a nonlinear covering
  lemma. We retain the explicit solver trust instead of calling that a formal proof.
* Requesting Lazard lifting on the installed wheel emitted a missing-CoCoA
  fallback warning. Current receipts use the default regular covering configuration;
  no claim of running Lazard lifting is made.
