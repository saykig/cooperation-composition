# Exact, reproducible R09 checks

Python 3 standard library only. From this directory:

    python3 check.py > /tmp/r09-replay.json
    python3 -O check.py > /tmp/r09-replay-optimized.json
    python3 explore.py > /tmp/r09-search-replay.json

Do not overwrite the retained results. `results.json` binds both source-file
hashes; normal and optimized execution produced identical output. Explicit failure
checks remain active with -O. No numerical solver, sampled maximum or tolerance
is used. `search-results.json` retains the seeded conjecture-killing search; it
found a greedy and antimatroid candidate within 42 trials.

The 15,653 checks comprise:

- 4,374 direct continuation-game recursions versus suffix inequalities;
- 4,374 singleton/segment consistency checks;
- 5,328 direct adaptive-tree game checks against the all-positive-path permutation
  (all 12 trees for each of 60 three-sender fixtures, and all 576 trees for each
  of eight four-sender fixtures);
- 533 sampled exact adjacent-swap implications and 1,000 known-model score checks;
- 44 exact fixture, certificate, projection, and negative-control checks.

The three-sender segment oracle is exact over the entire continuum: restrict the
parameter interval by the second sender's strict linear condition, then maximize
the first sender's quadratic product at endpoints and any concave stationary
point. Strictly positive maxima on the closure yield feasible interior points
unless the strict linear interval is empty. This is not a parameter grid scan.

The certificate fixture checks membership by a rational convex combination,
nonnegative normalized weights, the supporting hyperplane at both vertices, and
the exponent-cleared rational product identity. A wrong certificate is rejected.
The helper is not a general-purpose proof certificate parser or membership solver.

Finite checks corroborate the written proofs; they are not Lean verification,
a general complexity proof, empirical validation, or a replay of R08's unavailable
historical experiment code. The general root-isolation algorithm in T8 is a written
reduction to established machinery, not implemented here.
