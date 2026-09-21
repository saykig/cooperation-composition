# R16 exact replay

Standard-library Python 3; no numerical optimizer, external solver or tolerance.
From this directory:

```sh
python3 foundation_audit.py > /tmp/r16-foundation.json
cmp foundation_receipt.json /tmp/r16-foundation.json
python3 check_codec.py > /tmp/r16-codec.json
python3 -O check_codec.py > /tmp/r16-codec-O.json
cmp codec_receipt.json /tmp/r16-codec.json
cmp /tmp/r16-codec.json /tmp/r16-codec-O.json
python3 check_tree.py > /tmp/r16-tree.json
python3 -O check_tree.py > /tmp/r16-tree-O.json
cmp tree_receipt.json /tmp/r16-tree.json
cmp /tmp/r16-tree.json /tmp/r16-tree-O.json
python3 check_queries.py > /tmp/r16-queries.json
python3 -O check_queries.py > /tmp/r16-queries-O.json
cmp query_receipt.json /tmp/r16-queries.json
cmp /tmp/r16-queries.json /tmp/r16-queries-O.json
```

The codec test rewrites `sample.bin` deterministically. Other retained receipts
are only replaced when explicitly redirected above their paths. Checks use
explicit exceptions rather than removable Python assertions. Generated cache
files are ignored by the repository.

* Foundation: tangent identities/gaps, pairwise packing distinctions, product
  asymmetry, nonconvex support failure and favorable tie boundary. The many
  packing-pair checks enumerate code distinctions; they are not separate numerical
  optimizations over each hull. Tangent inequalities cover the hulls analytically.
* Codec: all 947 small combinatorial-code range/round-trip controls, 63 exact
  vertex-to-halfspace continuum sandwich checks, source-order invariance,
  malformed stream rejection and false inclusion/source controls. Sources include
  points, axis-aligned and oblique segments, corners with 60-bit coordinate
  precision, a rational parabola, a box, and seeded rational point clouds.
* Queries: 4,608 rational order/cost queries for four sources, with one known
  first sender and two uncertain coordinates. Quadratic maximization on rational
  segments is exact. There are also three explicit strict/tie controls. These
  are soundness checks for the bracket, not arbitrary-order optimizer benchmarks.
* Trees: 168 rational-cost tree tables, n=1..7 and alphabets of size 2 or 3,
  compared with exhaustive global label enumeration. Twenty-four have no compatible
  assignment; the other tables enumerate 2,500 compatible assignments in total.

These computations support the written statements. They do not prove asymptotic
rates, arbitrary-n equilibrium existence, historical priority, or the accuracy of
the model for a real institution. The new implementation is not represented as
the missing historical R15 executable.
