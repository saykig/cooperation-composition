# A short-prefix certificate for robust disclosure orders

19 September 2026 — Cooperation & Enforcement, R10.

## Finding in plain language

A successful order need not rely on one sender who always stops disclosure. Which
sender stops it can change with the model. Nevertheless, when the admissible
probabilities lie on one line segment, it is enough to find **two senders to put
first**. If those two cannot both want to continue under any compatible model,
the rest of the order can be filled arbitrarily.

This converts the search over n! orders into n(n−1) exact tests. It resolves the
rational-segment selection problem left open in R09. It does not discard the
shared probability constraint or replace it with separate ranges.

## Exact statement and assumptions

Retain R08's independent private binary facts within each model, authenticated
positive evidence, positive disclosure costs k_i, rewards η_i>0, receiver payoffs
B and −A, target complete silence/C, and existence of a sequential equilibrium
with favorable ties. Players know the model; the institution chooses one order
for the whole family. Set r_i=k_i/η_i and τ=A/(A+B). Let

    p(t)=a+t(b−a), 0≤t≤1,    a,b∈(0,τ)^n.

For n≥2, a common zero-fine order exists if and only if some ordered pair of
distinct senders (i,j) has no parameter t satisfying BOTH

    product_{h≠i} p_h(t)>r_i,
    product_{h≠i,j} p_h(t)>r_j.

Put that pair first and complete the order arbitrarily. If no pair works, the
minimum robust fine is B; otherwise it is zero. This is the inherited binary
fine structure, not a new continuous fine frontier. Products over no senders
are one. Constant coordinates, a=b and ties are included; n=1 is a direct test.

**Proof mechanism.** In any fixed order, each strict cascade inequality defines
a convex set of probability vectors: take logarithms and use concavity. A
successful order means these sets have empty intersection. On a segment, finite
Helly selects at most two sets whose intersection is already empty. Moving their
senders to the front in their original relative order only reduces the relevant
suffix products: previously earlier, unselected senders become extra factors
below one. Thus those two senders still cannot both continue. A one-sender
certificate may be padded with any second sender. The reverse implication is
immediate because later inequalities cannot rescue an already impossible cascade.

The same reasoning in affine dimension d gives a prefix of at most d+1. If all
r_i<1, the last inequality is automatic and the bound improves to min(d+1,n−1).
A ratio at least one gives an immediate singleton blocker.

See [the complete proof](../math/THEOREM.md), including strictness, favorable ties,
all boundary cases, the move-to-front inclusion and a self-contained finite Helly
argument. There is no outstanding proof gap in these stated results. They have
not been checked in a proof assistant or independently reviewed.

## Exact algorithm and what its certificates establish

With rational input, each pair gives two rational univariate polynomials. Their
strict positivity is decided by square-free preprocessing, exact root isolation
and signs in every complementary root cell. At a root at least one inequality
is an equality, which blocks disclosure under favorable ties. Endpoint feasibility
is covered by continuity; degenerate segments yield constant polynomials.

A successful output gives a pair, full order and a checkable sign certificate.
A rejection gives EVERY ordered pair its own rational witness. This has the form
“for every pair, some model defeats its prefix,” not “one model defeats all orders.”
The preserved two-sender quantifier example makes that distinction unavoidable.

There are polynomially many pairs, each of degree O(n), with polynomial coefficient
bit lengths. Established polynomial-bit root isolation therefore gives a
polynomial-bit selection algorithm. This complexity statement is separate from
the software, which uses elementary rational Sturm subdivision. The software's
certificate checker reconstructs constraints and validates root counts and signs;
it does not enumerate the full orders. Exhaustive orders are used only for tests.

The first receipt retains 2,271 checks: 96 exhaustive-order comparisons covering
1,752 permutations, 240 independent historical quadratic-oracle comparisons and
named boundary fixtures. Another 105 checks cover irrational roots, symmetry,
large endpoint denominators and malformed instances. The narrow-cell fixture
has width (5/2)·10^-30 and a checked rational witness. These are computational
checks, not substitutes for the proof. [Reproduction instructions](../experiments/README.md)
distinguish the observed timings from bit complexity.

## Trying to kill a stronger conclusion

Could two senders suffice even beyond segments? No. The smallest sender-count
counterexample has four senders and a triangle of models. Let

    r=(64/125,16/25,4/5,1/100), A=999, B=1, η_i=1,
    v1=(99/100,1/100,9/10,299/300),
    v2=(99/100,3/4,49/50,209/300),
    v3=(99/100,47/50,63/100,13/15).

Every pair is defeated at one of these three vertices. But throughout their hull,

    p2+2p3+3p4=24/5,
    p2 p3² p4³ ≤ (4/5)^6

by weighted AM-GM. Multiplying the first three strict cascade inequalities for
order (1,2,3,4) would give the opposite strict inequality. Hence the triple works,
while no pair does. This is a universal analytic certificate on the entire
triangle plus finite exact witnesses for the lower bound. It does not revive
R09's invalid shortcut of testing only vertices for successful orders.

The dimension bound is also attained at d=3 by a five-sender hull with 12 rational
vertices: all 60 ordered triples have strict witnesses, and weighted AM-GM certifies
a successful four-prefix. The d=1 sharp example is the inherited changing-blocker
segment. General tightness for d≥4 remains open; a bounded search at d=4 was
inconclusive. [Sharpness proof and receipts](../math/SHARPNESS.md) record the scope.

## Existing mathematics and the remaining question

Finite Helly supplies the small empty-intersection certificate; the product
monotonicity lemma turns it into a short protocol prefix. Sturm theory supplies
checkable exact signs, and Sagraloff–Mehlhorn's root-isolation theorem supplies
the polynomial-bit upper bound. These foundations are borrowed, not new theorems
of geometry or algebra. See the [inspected source notes](../sources/NOTES.md), which
also connect to R08/R09's signaling, hard-evidence and robust-optimization audits.
Historical novelty of this particular application remains unresolved.

The central research question should **remain unchanged**. Its segment-selection
subproblem is now solved rather than a candidate hardness problem. One tractable
next attack is to settle whether the d+1 prefix bound is sharp for every d in this
same game, using a general weighted-AM-GM construction or an exact obstruction.
The present construction is a concrete starting point. This should precede any
broader model, network extension or claim that a new mathematical foundation is
needed. The current progress is a theorem and an exact decision procedure using
established mathematics.
