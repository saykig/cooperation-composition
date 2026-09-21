# Gate 1 — independent foundation audit

21 September 2026. Baseline: `a863070`. Written proofs and new exact checks;
not a Lean proof, independent human review, or replay of the missing R15 code.
Read: the canonical north star, R13 primitive audit, R14 formal scope, R15 results,
verification ledger and formalization backlog. Historical evidence is preserved.

## Strongest established statement

R15 Theorems A/B and the rational sandwich survive, under their stated nonempty,
compact, convex, strictly positive families and independent product composition.
The following strengthened precision statement makes the gate explicit. Write
`m(P,r)=max_p min_j(log suffix_j(p)-log r_j)` for a fixed order.
For any positive ratio vectors r,s,

    |m(P,r)-m(P,s)| <= max_j |log r_j-log s_j|.

Consequently, if `delta=Delta+(P,Q)>0`, one known sender and REAL ratios attain
`m(P,r)=delta/2`, `m(Q,r)=-delta/2`. For every `0<a<delta/2`, POSITIVE RATIONAL
ratios distinguish the same families with both margins of magnitude greater
than a. The supremum over rational queries equals delta. This does not claim
attainment of the supremum by rational queries.

Proof of the displayed bound: every coordinate changes by at most the right
side; minima and maxima preserve this bound. Positive rational vectors are dense
in log coordinates. Perturb the real attaining ratios by less than `delta/2-a`.
This supplies the strict rational separation needed for arbitrary-code packing.

## Re-derivation of the five foundations

1. **Operational discrepancy.** For each simplex vector lambda, the weighted
   suffix sums have coordinate weights in [0,1]. Sion's compact concave/linear
   minimax applies: probabilities range over a compact convex family, logarithms
   are finite continuous concave functions, and lambda ranges over a compact
   simplex. Thus m is the minimum of the weighted-log support minus weighted log
   costs. Independent attachments add a support term identical on both sides.
   Every objective differs by at most Delta+, so the minima do as well. This
   also proves a bound for optimized orders; it does not prove optimized equality.
2. **Attainment.** A nonzero maximizing weight can be scaled to max weight one.
   Sort its coordinates and put a known sender first. Set lambda to successive
   weight differences and put zero mass on the final position. These nonnegative
   masses sum to one. At a support maximizer p*, choose every log ratio equal to
   its suffix log product minus z. Every coordinate margin at p* is z. The
   weighted support upper bounds every competing minimum by z, and the Q support
   upper bounds it by z-delta. The upper bound from item 1 forces equality on Q.
   Choose z=delta/2. At delta=0, sufficiently high costs produce a common constant
   final-position blocker and discrepancy zero. The added sender's probability
   need not enter any support weight: its weight is zero, and it can have any
   fixed admissible probability. Equal/zero weights cause no difficulty.
3. **Products.** `H_(P1 x P2)(w1,w2)=H_P1(w1)+H_P2(w2)`. The weight domain is
   a product of boxes, so maximization separates exactly. The *directed* errors
   add. The symmetric metric is the maximum of the two directional sums.
4. **Packing.** For the R15 parabola, `n_k dot(v_k-v_j)=(x_k-x_j)^2` exactly.
   With `w_i=n_ki v_ki/T`, the log objective's gradient at v_k is n_k/T.
   Its concave tangent bounds every convex combination omitting v_k by its value
   at v_k minus h²/T. It also proves v_k maximizes the objective on EVERY hull
   containing it. Hence arbitrary two different optional-vertex subsets differ
   in a directed support by at least h²/T; nesting of the hulls is unnecessary.
   Choosing spacing so this exceeds 2 gamma, with strict slack for rational
   costs, forces different codewords. There are 2^m subsets, so worst-case
   fixed-length storage is at least m bits; variable lengths up to b provide
   only 2^(b+1)-1 words. The actual finite construction uses tau>3/5. For another
   fixed nontrivial box inside (0,tau), place a scaled positive concave patch
   strictly inside that box; constants change, not the exponent. If ell=u there
   is no such packing. Affine dimension zero/one needs a separate rate.
5. **Sandwich.** Nonnegative rational convex weights establish each vertex
   domination; linearity extends them to the hull. Coordinatewise logarithm and
   positive weights give `0<=H_P(w)-H_Q(w)<=log(1+eta) sum_i w_i`, and hence
   `Delta+<=n log(1+eta)<=n eta`. No logged-vertex approximation is used. The
   source must actually be supplied to the verifier, and its entire list covered.
   A certificate relative to one source does not establish the claim for another.

The strategic interpretation remains R13's existential sequential-equilibrium
theorem, with favorable sender and receiver ties. R14 proves its primitive
belief/receiver/continuation bridge, not the full backward existence theorem.
No new game assumptions or new strategic theorem are claimed here.

## Small counterexamples and strict boundaries

* **Symmetric errors need not add.** One-coordinate point blocks P1={1/2},
  Q1={1/4}, P2={1/4}, Q2={1/2} have symmetric error log 2 each, while the product
  has symmetric error log 2, not 2 log 2. Directed addition is correct.
* **beta=gamma is insufficient for the stated one-sided interval decoder.**
  P={1/2}, Q={1/4}, known first sender rho=1/2, ratios (1/4,1/4), tau=3/4.
  True margin is log 2, decoded margin zero, and beta=gamma=log 2. The interval
  [0,log 2] forces REFINE although the true query is gamma-separated. Use
  beta<gamma for guaranteed completeness on |m|>=gamma. This is a boundary
  clarification, not a contradiction of R15, which already used strict beta.
* **Nonconvex support is insufficient in two uncertain coordinates.** Retain
  R15's a=(9/16,1/4), b=(1/9,9/16) and their geometric mean g=(1/4,3/8).
  Adding g to {a,b} changes no positive log support, but the query with known
  sender first and ratios (9/100,1/3,1/10) changes from blocked to cascading.
  Dimension one cannot exhibit this particular failure: the maximum probability
  dominates every smaller probability for all suffix tests. Do not use minimax
  on a nonconvex unlabelled union.
* **Singletons are not constant-bit objects.** Even in one coordinate, varying
  its value over a fixed positive interval gives Theta(log(1/gamma)) contextual
  bits. There is no isolated one-sender probability query (its suffix is empty);
  the added sender is essential for observing that coordinate.
* **Refinement is not source recovery.** Equal downward hulls can conceal
  different upper-restricted slices. Example P={(1/2,1/2)} and
  Q=conv{(1/4,1/4),(1/2,1/2)} have the same interface. Restrict both coordinates
  to <=1/3: P becomes empty, Q does not. Even an exact downward interface cannot
  implement this revision.

## Evidence, literature, gaps, next attack

`experiments/foundation_audit.py` checks product/sign counterexamples, all pairs
of the 256 optional-vertex hulls with m=8, rational tangent gaps, the nonconvex
query, and the boundary example with Fraction arithmetic. It is a new independent
finite check, not a replacement receipt for R15's unavailable executable.
The arbitrary-family statements above are written proofs.

The support/minimax machinery is established mathematics. The strategic
calibration is inherited R15, not a new discovery. R15's geometric bit bound must
also be compared with Bronshtein's *metric entropy*, which counts bits rather
than only vertices; see the new source notes.

Remaining assurance gaps: R08 full existence in Lean; R15 operational and
sandwich bridges in Lean; independent human proof review. No defect was found in
the five stated foundations. The bit question remains, with an essential scope
clarification: specify a total composition-error budget and access to the source.
Next bounded attack: define the four costs and test unbounded repeated reuse
before asserting a finite reusable rate.
