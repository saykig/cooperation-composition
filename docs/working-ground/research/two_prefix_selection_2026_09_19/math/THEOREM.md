# Short prefixes and exact segment selection

19 September 2026. New handwritten proofs, conditional on R08's established
backward-induction characterization. No changed strategic or equilibrium model.

## Assumptions and meaning of a certificate

There are n≥1 senders (n=1 is an algorithmic boundary case), independent positive
Bernoulli facts within each actual model, one costly authenticated positive report
per sender, rewards η_i>0 and costs k_i>0, and r_i=k_i/η_i. Receiver payoffs and
fine are exactly R08: B>0, A>0, τ=A/(A+B), and p belongs to a nonempty compact
convex P contained in (0,τ)^n. Players know p; the institution chooses one pure
order for the whole family. Sequential-equilibrium existence, the all-silent/C
target and favorable ties are unchanged. A family couples parameters across
models, not the independent private facts inside an actual model.

For an ordered prefix α=(i_1,...,i_m), define

    G_j^α(p) = product_{i not in {i_1,...,i_j}} p_i − r_{i_j}.

A **successful prefix** here means there is no p∈P with all m values strictly
positive. Consequently EVERY completion of that prefix is a successful full
order. This is a sufficient partial-protocol certificate, not a requirement that
every prefix of a successful order is successful. Empty products equal 1. The
empty prefix cannot succeed on nonempty P.

R08 says a full order fails at p iff all its G_j are strictly positive. Equality
is a blocker: at a sender tie choose silence, and earlier costly reports cannot
complete the evidence. If all inequalities are strict, backward induction forces
the positive-type cascade. At fine e<B complete evidence induces D; at e=B choose
C also at complete evidence. Thus the optimized robust fine remains exactly 0
if a successful order exists, and B otherwise.

## Lemma 1: move the certificate to the front

Fix an order π and selected positions j_1<...<j_m. Move their senders to the front
in that relative order, leaving all other senders afterward in any order. For
selected sender π_{j_s}, its new suffix contains its OLD suffix plus precisely
those formerly earlier, unselected senders. No formerly later sender is lost.
Therefore its new suffix product equals the old product times a product of
numbers in (0,1), and is at most the old product. It follows that

    {p: G_s^α(p)>0} ⊆ {p: G_{j_s}^π(p)>0}.

An empty intersection of the selected old strict-positive sets remains empty
after moving them forward. In particular the resulting prefix succeeds,
regardless of its completion. This inclusion is weak, sufficient even at ties;
it never converts a weak blocker into a profitable deviation.

## Theorem 2: the dimension bound

If P has affine dimension d and some successful order exists, a successful prefix
of length at most min(n,d+1) exists. The converse holds by completion.

Proof. For a successful π let C_j={p∈P:G_j^π(p)>0}. These are convex: positivity
is equivalent to sum_{l>j} log p_{π_l}>log r_{π_j}, a strict superlevel set of a
concave continuous function, intersected with convex P. No closedness assumption
is needed for FINITE Helly. Identify aff(P) with R^d. The intersection of all C_j
is empty. By Helly's theorem some at most d+1 of them already have empty
intersection (or take all if n≤d+1). Lemma 1 moves those senders to the front.
For d=0, P is a singleton, so at least one C_j itself is empty; the same argument
works without invoking positive-dimensional Helly. ∎

This borrows Helly's theorem; the order-specific step is Lemma 1. It asserts a
short prefix, not an uncertainty witness of size d+1, nor d+1 vertices sufficient
to evaluate the original strategic conditions. It does not assert tightness.

## Corollary 3: two-prefix theorem on a segment

Let P={a+t(b−a):0≤t≤1} with rational a,b and positive rational r. For n≥2 a
successful order exists iff SOME ordered distinct pair (i,j) satisfies

    there is NO t∈[0,1] with
    product_{h≠i} p_h(t)>r_i AND product_{h≠i,j} p_h(t)>r_j.       (S)

Indeed d≤1 gives a prefix of length ≤2. A successful length-one prefix can be
extended by any second sender while retaining its first inequality, so enumerating
all ordered pairs is sufficient. Conversely a pair satisfying (S) is a successful
prefix. This includes a=b, constant coordinates and n=2: the second product is
then the empty product 1. For n=1 check the sole constant 1−r_1 directly.

If every pair is rejected, the quantifiers are

    for every ordered pair (i,j), there exists t_{ij} making BOTH strict.

Together with Corollary 3 this rejects every successful full order. It does NOT
say there is one t making every pair or every full order fail. Nor need a pair's
witness make its arbitrarily chosen completion cascade.

## Exact sign algorithm and correctness

For a pair form the two rational polynomials in (S), denoted g_1,g_2. A constant
nonpositive polynomial immediately certifies success, including an identically
zero polynomial. Otherwise take the square-free part H of the product of all
nonconstant g's. Strip any factors t and t−1 from H. Isolate all its roots in (0,1)
with disjoint rational brackets, none having a root endpoint. Every root of H is
a root of some g, so at that point strict conjunction fails. Between consecutive
roots each g has a constant sign. Check one rational sample in EVERY complementary
open cell. If all g's are positive in a cell, return that rational t as a witness.
If none are, the isolated-root cover and sample signs certify success. A strictly
feasible endpoint would, by continuity, imply an adjacent strictly feasible cell;
endpoint roots themselves fail strictness. If H is constant there is one cell.
Repeated roots (tangencies), shared roots and endpoint roots require no genericity
assumption. The gcd/square-free step preserves the zero set; original g's, not H,
are used to determine signs.

The certificate checker reconstructs g and H, verifies each bracket contains one
root by Sturm variation, verifies brackets are ordered/nonoverlapping and their
count equals the total interior-root count, and checks each sample lies between
consecutive root brackets and has the reported signs. Together these facts account
for the continuum, including inside brackets: the only sign change boundaries
are the unique enclosed roots. A rational witness is checked simply by substituting
it into BOTH original inequalities. No sampled grid decides feasibility.

## Polynomial-bit complexity — separate from measured software performance

Encode every endpoint, ratio and τ as a binary rational; n is part of the input.
There are n(n−1) pairs. Their polynomial degrees are at most n−1 and n−2, and the
product has degree at most 2n−3. Multiplying rational linear factors, clearing
denominators, gcd and square-free preprocessing have polynomial bit complexity
and polynomial output coefficient lengths in the total input size L. For example,
a common denominator is the product of the input denominators; coefficient sums
have at most 2^n terms, adding O(n) bits beyond products of input numerators.
Standard coefficient bounds for rational gcd factors keep their bit lengths
polynomial. Rational root separation bounds give polynomial-bit isolating
endpoints and samples. Apply an established polynomial-bit univariate isolation
algorithm, e.g. Sagraloff–Mehlhorn's integer square-free result, after preprocessing.
Rational sign substitution at all O(n) cells is polynomial. Thus all ordered pairs
can be decided, with certificates, in polynomial BIT time. This upgrades R09's NP
upper bound to membership in P on rational segments; no hardness conjecture remains
for that class unless P=NP.

This is a reduction to established root machinery, not a complexity analysis of
our particular Python implementation. The executable uses elementary exact Sturm
subdivision and rational Euclidean arithmetic, not ANewDsc. It is intended for
small/moderate inputs; no optimized bit bound or production performance guarantee
is claimed for that code. Its timing receipts measure only their declared cases.
