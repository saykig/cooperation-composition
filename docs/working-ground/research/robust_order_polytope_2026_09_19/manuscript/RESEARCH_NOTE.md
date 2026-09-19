# One disclosure order for a jointly constrained family

R09, September 19, 2026. Written proofs with exact finite checks. No formal
verification, independent review, empirical validation or novelty claim.

The central question remains: **when can one sequential disclosure order sustain
a fixed arrangement across every compatible model, and which shared constraints
must be retained to determine enforcement?** The useful result is a certificate
for that universal statement, together with sharp failures of cheaper summaries.

## Model and scope

We retain R08's complementary-evidence game. Each of n senders privately sees one
independent binary fact, positive with probability p_i. A positive sender may
provide its authenticated certificate at cost k_i>0. All senders benefit by η_i>0
if a receiver chooses D. The target is silence and C. D pays the receiver B when
all facts are positive, and −A otherwise; a fine e is charged for choosing D.
Assume every p_i<A/(A+B). The actual p is known to players, but the institution
must choose one order for all p in a nonempty compact convex set P.

Write r_i=k_i/η_i. R08 proves that an order π permits a disclosure cascade exactly
when, at every position j,

    r_{π_j} < product_{l>j} p_{π_l}.

Otherwise some sender blocks completion. Weak inequalities permit silence at ties.
The minimum fine for each order/model is consequently either zero or B. This
binary enforcement result is inherited; intermediate fines cannot alter the
receiver's complete-evidence decision. We have not generalized it to arbitrary
payoffs or evidence systems.

## Strongest theorem: one weighted certificate replaces changing blockers

For a fixed order define

    f_j(p)=Σ_{l>j} log p_{π_l}−log r_{π_j}.

**Theorem.** The order works at zero fine throughout P if and only if there are
nonnegative weights λ_j summing to one such that

    Σ_j λ_j f_j(p) ≤ 0 for every p∈P.

Thus some common order works if and only if some order admits these weights.
The weights do not select different orders in different models. They combine
constraints in a proof; the actual blocker can change with p.

The proof uses the compact concave–convex minimax theorem: the worst common
cascade margin is max_p min_j f_j(p), and equals min_λ max_p Σλ_j f_j(p).
The functions are concave and continuous in p, linear in λ. A positive margin
means a compatible cascade; a nonpositive margin yields the certificate. This
is a specialization of [Sion's established theorem](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf),
not a claim of new minimax mathematics.

For P=conv(V), this universal certificate itself has a finite witness. Let
w_{π_l}=Σ_{j<l}λ_j. There must exist z∈P such that

    Σ_i w_i log z_i ≤ Σ_j λ_j log r_{π_j},
    Σ_i (w_i/z_i)(v_i−z_i) ≤ 0 for every vertex v∈V.

Concavity bounds the log objective by its tangent at z, proving sufficiency.
Maximizing the weighted objective and using its first-order condition proves
necessity. With a halfspace description the second line is a polyhedral normal-
cone certificate. Exact rational weights and z permit a rational product check
by clearing exponent denominators. General existence is a finite real certificate;
polynomial-length rational certificates at every boundary have not been proved.
See [T1–T3 and the complete proof](../math/CHARACTERIZATION.md).

This is more than another numerical frontier. A proposed order has a convex
verification problem and, when feasible, a structural proof. R08's changing-blocker
segment has the exact witness λ=(7/10,3/10,0), z=(13/20,7/20,2/5). Its supporting
normal is (0,2,5/2), and its product inequality holds with equality.

## The smallest failure of vertex evaluation

Let P join (1/2,1/5,3/5) and (1/2,3/5,1/5), with
r=(3/20,1/10,1/10). At both endpoints order (1,2,3) is blocked because
p2 p3=3/25<3/20. At the midpoint, p2 p3=4/25>3/20 and every order cascades.
The robust optimum is B even though the same order passes both vertices.

Three senders are minimal for this failure: with two, the only nonconstant
cascade inequality is linear in the last sender's probability. The nonlinearity
appears as a product with three senders. The replacement theorem still uses the
vertices, but checks a supporting linear inequality there rather than checking
the original game only at those points.

## How much shared information must survive?

For an order beginning with sender i, p_i disappears from every suffix. Hence the
exact projection of P onto the other n−1 coordinates suffices. Collecting all such
projections determines every order. For three senders, full pairwise feasible
regions therefore suffice—unlike separate coordinate intervals.

That conclusion stops at four senders. Take Q=[1/4,1/2]^4 and
P={p∈Q:Σp_i≤3/2}, with r_i=1/10. Every pair projection is the same square for
P and Q. In P, any three coordinates have product at most (5/12)^3<1/10,
so the first sender blocks every order. Q admits its all-1/2 corner, where every
order cascades. Optimized fines are zero and B despite identical pairwise regions.

The same construction proves a general sharp boundary: all (n−1)-projections
suffice, while all (n−2)-projections can fail. This is an information-loss
impossibility theorem, not computational NP-hardness. A query-specific certificate
can of course be much smaller than retaining every projection.
[Proofs and counterexamples](../math/COUNTEREXAMPLES.md).

## Order structure and adaptation

Largest cost/reward first fails on a small rational segment. Nevertheless, a
valid adjacent-exchange rule survives: when r_i p_i≥r_j p_j throughout P,
placing i immediately before j can only remove cascading models. Uniform score
ranking therefore gives a provably optimal sorted order. Without a stable ranking,
this is a local rule, not a general greedy solution.

The successful orders need not be linear extensions of a partial order or basic
words of an antimatroid/greedoid. One three-sender fixture admits exactly five of
the six permutations, while all subsets occur as successful prefixes. The missing
word cannot be captured by those set-based feasibility structures. The standard
antimatroid framework is described in [Berendsohn's primary paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/LIPIcs.ESA.2025.104/LIPIcs.ESA.2025.104.pdf).

Deterministic adaptive ordering offers no improvement in this benchmark. Once
any sender stays silent, complete certification is impossible and further reports
cannot induce D. Every adaptive public tree has only one all-positive path; its
order has exactly the same cascade condition at each model. This proves equality
of optimal fixed and adaptive enforcement for every n. It does not cover hidden
future randomization, additional signals, revisits or multiple sufficient evidence
sets. [Ordering and adaptation proofs](../math/ORDER_AND_ADAPTATION.md).

## Computation, complexity and prior art

The new standalone code passes 15,653 exact rational checks, including direct
continuation-game recursion, adaptive trees, a rational continuum certificate,
and negative controls. These corroborate the proofs. The old R08 count is only a
retained summary; its executable was unavailable, so no historical replay is claimed.
No Lean check was added for these new theorems.

For a rational line segment P and a supplied order, cascade feasibility reduces
to signs of univariate polynomials with total degree O(n²). Established exact
root-isolation algorithms give polynomial-time verification. Thus existence of
a common zero-fine order on a rational segment is in NP. NP-hardness remains
unproved; the general-polytope exact bit complexity remains open. The proof uses
[Sagraloff–Mehlhorn's root-isolation machinery](https://arxiv.org/pdf/1308.4088v2).
The [complexity note](../math/COMPLEXITY_BOUNDARY.md) states the reduction and limits.

Scheduling supplies a log-space translation, but standard lateness minimization
has the wrong objective here. Reliability and stochastic Boolean evaluation expose
the single-AND-path structure, but do not themselves model strategic disclosure.
Robust optimization provides certificates and warns against importing hardness
across different quantifiers. The [source audit](../sources/NOTES.md) records these
comparisons and the already substantial costly-disclosure and payments literature.
Novelty of the combined specialization is unestablished.

## Decision and next attack

Keep the central question unchanged. We have earned an exact robust certificate,
a sharp representation lower bound and a no-adaptation theorem in the benchmark;
we have not settled common-order selection complexity. Existing convex mathematics
settles verification more directly than a new general theory would.

**Next attack:** determine the complexity of finding a robust zero-fine order when
P is a single rational line segment and n varies. Verification is now polynomial,
so aim either for a polynomial selection algorithm exploiting suffix structure or
an explicit NP-hardness reduction. Start with that smallest unresolved class,
not arbitrary evidence networks. This advances the same question while keeping
its remaining obstacle precise.
