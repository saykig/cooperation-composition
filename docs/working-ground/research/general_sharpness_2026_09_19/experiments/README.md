# Reproducing this construction gate

All labels in code/JSON are zero-based. The dimension-four outcome table converts
them to one-based labels. Previous phase files and receipts are preserved.

## Candidate optimization and exact margin certification

Use Python with the pinned packages in `requirements.txt` (NumPy 2.0.2,
SciPy 1.13.1); the recorded run used Python 3.9.6. An environment can be created
outside the checkout. From this directory:

```sh
python resolve_prefixes.py > /tmp/r11-prefixes.json
```

It reads the EXACT twenty unresolved prefixes from R10's saved receipt. Each
maximum-minimum-log-margin problem is convex. SLSQP searches the closed upper box
with a numerical positive lower bound; a rationalized candidate is placed strictly
inside the true box and checked against the exact affine equation. A tangent
certificate bounds the full original-domain supremum, so neither the artificial
numerical lower bound nor the optimizer stopping status is trusted for correctness.
A dual LP supplies candidate weights; exact continuous-knapsack support and rational
log-series intervals produce the rigorous upper bound.

`prefix-results.json` stores all 20 rational witnesses, exact product margins,
rational lower/upper bounds, tangent weights/gradients/support vertices, numerical
solver points/status/residuals, versions and source hashes. The maximum certified
supremum gap is 4.6197·10^-8. All twenty strict witnesses are positive by exact
arithmetic. The numerical discovery plus certification took about 0.43 seconds
on the recorded machine; this is not an asymptotic claim.

## General construction and exact finite falsification

These commands require only the Python standard library:

```sh
python3 check_construction.py > /tmp/r11-construction.json
python3 verify_results.py > /tmp/r11-verification.json
```

`construction.py` implements the explicit formulas of
[GENERAL_CONSTRUCTION.md](../math/GENERAL_CONSTRUCTION.md). It handles every
ordered prefix via either an initial nonzero-label absorber or running-record
blocks. Each checked witness satisfies probability bounds, the affine equation,
a uniform linear slack and a strictly positive rational product slack.

`construction-results.json` records:

- all **23,115** length-(m−1) prefixes for m=2,...,7;
- 75 further structured/random prefix controls at m=8,10,20,50,100;
- exact affine ranks for the dimension-spanning points through d=9;
- exact threshold-product identities and finite fixed-q obstruction controls;
- selected rational examples and source hashes.

The run took about 6.55 seconds. The arbitrary-d theorem is the written proof;
these finite tests can expose bugs but cannot prove it. Random prefix selection
in the higher-dimensional controls does not decide an existence question.

`verify_results.py` rechecks every stored dimension-four witness and optimal-margin
bracket, source identities, four deliberate corruptions, seven exact log-identity
controls, fixed-threshold inequalities and the inherited R08 singleton witnesses.
The replay does NOT require NumPy or SciPy and does not rerun optimization. It
shares rational certificate routines with the producer; this is not an independent
trusted kernel. No Lean or external formal replay was performed.

## Limitations

No numerical solver is used to prove the arbitrary-d construction or the ansatz
obstructions. No floating-point tolerance decides whether a rational cascade is
strict. Formalization and historical novelty remain unresolved. Exact source
hashes bind receipts to code; timings need not reproduce bit-for-bit across machines.
The new CI steps rerun these specific programs and do not upgrade the unformalized
mathematical statements to proof-assistant results.
