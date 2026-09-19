# Fixed affine dimension: exact selection is polynomial-time

19 September 2026. Written proof, not a proof-assistant result. The strategic
interpretation is conditional on R08's game-to-cascade theorem. The algebraic
decision theorem below can also be read on its own as a theorem about products.

## Objects, encoding and conclusion

There are n≥1 senders, rational ratios r_i>0, and rational 0<τ<1. Let P be a
nonempty compact convex polytope contained in (0,τ)^n, of **actual affine
dimension** d. In the R08 game, private Bernoulli facts are independent within
each model p; P constrains the possible model parameters jointly. Players know
p. The institution chooses one order before resolving which p applies. The
target and favorable equilibrium ties are as in R08. A positive fine has the
same receiver-payoff threshold B>0 throughout this family.

For a distinct ordered prefix α=(i_1,...,i_k), set

    g_j^α(p) = ∏_{h∉{i_1,...,i_j}} p_h − r_{i_j},
    F_α = {p∈P : g_1^α(p)>0,...,g_k^α(p)>0}.

An empty product is 1. Call α successful exactly when F_α is empty. Every
completion of a successful prefix sustains the target throughout P. Equality
g_j=0 blocks a cascade, so replacing > by ≥ changes the question.

**Input encodings.** Either:

* V: an explicit list of M rational vectors whose convex hull is P. Duplicates,
  nonextreme points and affine dependencies are allowed.
* H: an explicit rational inequality system Ap≤b whose solution set is P;
  rational equalities can be entered as two inequalities.

Integers are binary; a rational is a signed binary numerator and positive binary
denominator. L denotes the total explicit input bit length, including n, all
matrix/list entries, τ and the r_i. This is not an oracle, circuit or implicit
exponentially long vertex-list model. Domain promises can be checked by rational
linear programming in the H representation and by inspecting the V coordinates.

**Theorem 1.** For each fixed nonnegative integer D, on these inputs with d≤D,
existence of a successful full order can be decided in L^{O_D(1)} bit operations.
A successful prefix of length at most min(n,d+1), and thus a full order, can be
returned within that bound. Consequently the R08 minimum robust fine is computed
exactly: 0 if such an order exists, and B otherwise.

The exponent may depend on D. This is not a fixed-parameter tractability claim
of the form f(D)L^c, nor a polynomial-time result when dimension grows. It is
also not a worst-case running-time guarantee for our particular SMT software.

## Proof

**1. Find the actual affine hull.** In V form, rational Gaussian elimination on
vertex differences finds a basis T and p⁰ with p=p⁰+Tx, x∈R^d. Determinant bounds
give polynomial bit length for the basis, inverse pivot system and transformed
coordinates. In H form, solve rational LPs: for each row find its maximum slack.
Rows whose slack is identically zero are affine equations of P. Their intersection
is aff(P): averaging a slack-positive feasible point for each remaining row gives
a point strict in every remaining row, hence a relative neighborhood in that
intersection. Rational elimination then gives the same parameterization.
Nonemptiness, boundedness and coordinate extrema can also be checked by LP.

**2. Describe the intrinsic polytope.** Substitution gives a rational H description
Q⊂R^d directly from H input. For V input with d≥1, enumerate d affinely independent
vertices, form their supporting hyperplane, and retain it when all vertices lie
on one side. Every facet occurs: a facet of a d-dimensional polytope contains d
affinely independent vertices. At most M^d candidates are needed. Determinants
again have polynomial bit length for fixed d. Their intersection is Q. Redundant
facets are harmless. For d=0, Q is a single point and requires no inequalities.

**3. Only polynomially many prefixes.** R10's move-to-front lemma and finite
Helly theorem imply

    some full order succeeds ⇔ some α with |α|≤min(n,d+1) succeeds.

Briefly, the cascade set of a position is convex since its defining inequality
is a strict superlevel inequality for a sum of logarithms. An empty intersection
has an empty subintersection of at most d+1 such sets. Moving those senders to
the front in their relative order only adds factors in (0,1) to their suffix
products; it preserves emptiness. This is a recap, not a new Helly theorem.

There are at most Σ_{k≤D+1} n^k candidates. A slight implementation refinement
uses K=min(d+1,max(1,n−1)): if any r_i≥1, its singleton succeeds; otherwise the
last full-order inequality 1>r_i is automatic and can be omitted before Helly.

**4. Each decision uses only d real variables.** For each α test

    ∃x∈R^d : x∈Q and every g_j^α(p⁰+Tx)>0.                 (E)

After multiplying positive rational denominators, these are integer polynomial
sign conditions, degrees at most n−1 (and at most one for facets). For fixed d,
each expanded polynomial has at most binom(n+d,d) monomials. Expanding at most n
affine factors has polynomial coefficient bit lengths: multiplying denominators
adds their bit lengths; at most (d+1)^n contributions to a coefficient add only
O(n log(d+1)) bits beyond product sizes. Thus the number, degree and coefficient
bit length of polynomials in (E) are all polynomial in L for fixed d.

Apply established effective quantifier elimination for integer polynomials in a
fixed number of variables. Specifically, Basu–Pollack–Roy's block-elimination
bound, stated with integer bit-size control in Basu's survey Theorem 2.27, with
one existential block of size d and no free variables, is polynomial in those
parameters when d is fixed. Strict signs and degeneracies are covered. Combining
it with the candidate bound proves the decision and order-output claim. ∎

The effective real-algebraic theorem is **borrowed**. The new-to-this-record
deduction is applying it after the existing prefix reduction and affine reduction.
No historical novelty is asserted. A barycentric encoding with M−1 variables is
useful for an independent checker but would NOT justify this complexity proof
when M grows; intrinsic dimension reduction is essential.

## Lemma 2: strict witnesses can be rational and relatively interior

For every prefix, F_α is nonempty iff it contains a rational point of relint(P).

Proof. The forward direction is the only issue. Let p∈F_α, and choose a rational
q∈relint(P), for example the mean of a finite spanning vertex list. For sufficiently
small ε>0, (1−ε)p+εq remains in F_α by continuity of finitely many strict inequalities
and belongs to relint(P). In intrinsic coordinates an open neighborhood of this
point is feasible. Rational points are dense there. The reverse is immediate. ∎

This permits the primary solver to make all intrinsic facet inequalities strict.
It does not change the game's ties: the cascade inequalities were already strict.
In d=0 the point is its own relative interior and direct rational substitution
decides everything. The lemma fails for arbitrary weak cascade inequalities:
feasibility could then live only on a boundary. It needs no generic position,
transversality, positive margin promise, or lower bound on the width of a feasible
region. Tangencies are legitimate exact no-cascade decisions.

## Executable procedure and proof of its output contracts

The executable supports V inputs of actual d≤2. Exact elimination and a planar
convex hull produce intrinsic halfspaces. Z3's QF_NRA/NLSAT procedure decides each
prefix. For SAT it obtains exact real algebraic coordinates, refines them to
rationals until every facet and cascade inequality is strict, and exports convex
weights in the original vertex list. Lemma 2 plus openness of the chosen solution
proves that refinement terminates. Carathéodory supplies at most d+1 positive
weights; an exhaustive exact linear solve over such subsets finds them.

For UNSAT a second encoding uses p=Σλ_v v with λ_v≥0 and Σλ_v=1, eliminates one
weight, and constructs suffix products backwards along an arbitrary completion.
cvc5 independently decides this closed-domain formula and exports its proof
skeleton. The original and independent feasible sets agree by Lemma 2 and the
suffix definition. On acceptance, the empty F_α proves that every completion works.

If no prefix succeeds, the result contains a rational defeating point for EVERY
enumerated prefix. A checker verifies convex membership and all strict products
using only rational arithmetic, then verifies complete candidate coverage. By
Theorem 1's prefix reduction, no full order succeeds. The points can differ.
There need not exist any single model defeating every full order.

**Exact-backend certificate contract.** A success bundle binds the input, prefix,
full order, both SMT-LIB queries and cvc5 CPC proof skeleton. Its checker rebuilds
both queries and redecides emptiness with the two backends. Some cvc5 nonlinear
covering steps remain trusted, and the checker does not run an external CPC proof
kernel on the saved skeleton. This is a checkable exact-backend replay certificate,
NOT a solver-free algebraic or proof-assistant certificate. Trusted components are
explicit in `experiments/README.md`. Rational rejection certificates are stronger
in this respect: they need no SMT solver for their mathematical checks.

No finite sampling, tolerance or timeout returns an emptiness conclusion. A solver
`unknown`, timeout or disagreement raises an error and leaves the task incomplete.
The implementation's unbounded mathematical procedure assumes correct terminating
QF_NRA backends; limited-time execution is an honest partial run of that procedure.
The fixed-dimension bit-complexity theorem does not depend on these implementation
heuristics, CPC proof sizes, independent barycentric variable counts, or measured
runtime.
