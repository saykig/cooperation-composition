# Small exact failures and the information that survives

All examples use A=2, B=1, η_i=1 and costs r_i, unless stated otherwise. Probabilities
lie strictly below 2/3. Labels in prose are 1-based.

## C1: vertex-only testing fails, minimally at three senders

Let P be the segment between (1/2,1/5,3/5) and (1/2,3/5,1/5), and
r=(3/20,1/10,1/10). Order (1,2,3) is deterred at BOTH vertices because p2 p3=3/25
is below 3/20. At the midpoint (1/2,2/5,2/5), all senders satisfy
r_i<product_{j≠i}p_j. Thus EVERY order cascades there. Testing all vertices with
one common order would falsely report zero instead of the exact robust fine 1.

This is the smallest sender count for failure of fixed-order vertex evaluation:
with two senders, the only nonconstant constraint is p_last>r_first, a linear
inequality; the last sender condition is constant. A nonempty polytope with a
violating point has a violating vertex. Three senders permit the interior maximum
of a product. Only a segment (two vertices) is needed.

This does not contradict T2: a supporting-hyperplane certificate checked at vertices
is different from evaluating the ORIGINAL strategic condition only at vertices.

## C2: largest cost/reward first is not a robust greedy rule

Take segment endpoints a=(3/5,1/2,1/10), b=(3/10,1/10,3/10) and
r=(11/50,13/50,7/25). Descending r gives (3,2,1), which cascades already at a:
7/25<3/10, 13/50<3/5, 11/50<1.
Order (1,2,3) works throughout: p2 p3=(1/2−2t/5)(1/10+t/5)
=1/20+3t/50−2t²/25 has maximum 49/800<11/50.
This refutes this specific simple greedy rule, not every conceivable greedy method.

## C3: successful orders need not be a poset's extensions or antimatroid words

Use the singleton polytope p=(1/10,3/5,1/2), r=(4/25,1/2,8/25).
Every permutation EXCEPT (1,3,2) works with zero fine. For that order,
3/10>4/25, 3/5>8/25, and 1>1/2. Any order starting with 2 or 3 is blocked
immediately; (1,2,3) is blocked at sender 2 by equality p3=r2.

A poset allowing five of the six permutations on three labels imposes no mandatory
pair precedence (both orientations of every pair occur), hence allows all six:
contradiction. For an antimatroid/basic-word representation, the successful prefixes
make every subset feasible, yet the missing permutation also has all those feasible
prefixes. The same prefix-set argument rules out representing EXACTLY these words
as the basic words of an ordinary set-system greedoid. This does not rule out a
richer history-dependent state or useful partial-order dominance rules.

## T4: which local summaries suffice?

For a fixed order only the projection of P onto all coordinates except its first
sender appears in (1). Therefore the collection of exact (n−1)-coordinate projected
sets determines every order's answer. In particular, FULL pairwise feasible regions
suffice for three senders. Pairwise ranges/covariances or separate product maxima
are not the same object as those feasible regions.

No fixed lower-order projection summary suffices as n grows. More sharply, for
any n≥3 and 1≤k≤n−2, let 0<l<u<τ and

    Q=[l,u]^n,
    P={p∈Q: Σp_i≤n l+k(u−l)}.

P and Q have identical projections onto EVERY k coordinates: extend any such
coordinates by l elsewhere. But for any n−1 coordinates in P their product is
at most h^(n−1), where h=l+k(u−l)/(n−1)<u (AM–GM). Choose all r_i strictly
between h^(n−1) and u^(n−1). Every order on P is blocked by its first sender.
At Q's all-u corner EVERY order cascades. Their optimized fines are 0 and B.

For n=4,k=2,l=1/4,u=1/2 choose r_i=1/10:
h^3=(5/12)^3=125/1728<1/10<1/8=u³. These two rational polytopes have identical
full pairwise projections yet opposite robust answers. Together with sufficiency
for n=3, four is the smallest sender count for failure of FULL pairwise projections.

These are exact information-loss impossibility results, not NP-hardness proofs.
All (n−1)-projections are sufficient in general; all (n−2)-projections can fail.
A particular query may retain much less, for example its T2 certificate.
