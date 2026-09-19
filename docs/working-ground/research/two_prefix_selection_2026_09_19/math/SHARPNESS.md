# How sharp is the prefix bound inside this game?

19 September 2026. The strategic game is unchanged. These are different legitimate
parameter instances, not new signal spaces, actions or equilibrium concepts.

## Dimension zero and one

A nonempty model family cannot have a successful empty prefix. A singleton with
a blocker therefore attains the dimension-zero bound one.

The inherited R08 segment attains the dimension-one bound two. Its successful
prefix is (1,2), as already proved. No single sender can be a successful prefix:

- For sender 1, p_2 p_3 at s=17/50 is 289/2000 > 7/50.
- For sender 2, p_1 p_3 at s=13/20 is 169/400 > 2/5.
- For sender 3, p_1 p_2 at s=1/5 is 39/100 > 1/10.

These may be different models. They refute a universal one-sender prefix while
leaving the successful two-sender prefix intact. The new exact implementation
also generates and checks rational witness certificates for all three singleton
rejections. R08's changing-blocker example was not newly discovered here.

## Dimension two: three senders in the prefix really are necessary

Use four senders, η_i=1, B=1, A=999, hence τ=999/1000, and

    r=(64/125,16/25,4/5,1/100),     q=4/5.

Let P be the convex hull of these three rational vectors:

    v1=(99/100, 1/100, 9/10, 299/300),
    v2=(99/100, 3/4, 49/50, 209/300),
    v3=(99/100, 47/50, 63/100, 13/15).

Every coordinate is strictly between 0 and τ. All points satisfy

    p1=99/100,       p2+2p3+3p4=24/5.

The determinant in coordinates (p2,p3) of (v2−v1,v3−v1) is −1371/5000,
so this is exactly a two-dimensional triangle.

**Successful triple, continuum proof.** Weighted AM-GM gives throughout P

    p2 p3^2 p4^3 ≤ ((p2+2p3+3p4)/6)^6 = (4/5)^6.

If all first three inequalities of order (1,2,3,4) were strict, then multiplying

    p2 p3 p4 > q^3,       p3 p4 > q^2,       p4 > q

would contradict that bound. Thus (1,2,3) is a successful prefix. Equality is safe
under favorable ties; no strict inequality was replaced by a weak one.

**Every pair fails.** This table gives a witness vertex at which both prefix
inequalities are strict. Exact positive margins are retained in the JSON receipt.

| Prefix | Witness | Prefix | Witness |
|---|---|---|---|
| (1,2) | v2 | (1,3) | v3 |
| (1,4) | v2 | (2,1) | v1 |
| (2,3) | v1 | (2,4) | v1 |
| (3,1) | v3 | (3,2) | v3 |
| (3,4) | v3 | (4,1) | v2 |
| (4,2) | v2 | (4,3) | v3 |

A successful singleton would remain successful after appending a second sender,
so none exists either. The optimum certificate length is exactly three. This is
minimal in sender count: with at most three senders and all r_i<1 the last
inequality is automatic, so a successful full order already has a successful
prefix of length at most two. If r_i≥1, a successful singleton exists instead.

This kills the stronger conjecture that two-prefix selection extends to arbitrary
convex uncertainty families in the same game. It does NOT disprove the segment
theorem, and pair rejection is still not one universally failing model.

## Dimension three: a checked four-prefix example

The same weighted-AM-GM construction was tested with five senders. Set q=4/5,
τ=9999/10000, p1=999/1000, and r=(q^4,q^3,q^2,q,1/1000). Search for rational
points on

    p2+2p3+3p4+4p5=10q.

For any convex hull of such points, multiplying the first four inequalities of
(1,2,3,4,5) contradicts the weighted-AM-GM bound product_{i=1}^4 p_{i+1}^i≤q^10.
The retained exact vertices have affine rank three. For EVERY one of the 60
ordered three-sender prefixes, a retained vertex makes its three inequalities
strict. Thus four is necessary and sufficient on this explicitly specified hull.
The vertex list and all exact margins are in
[sharpness-results.json](../experiments/sharpness-results.json); the reusable checker
verifies bounds, affine constraints, rank, threshold identity and every witness.
This is an exact finite certificate paired with the universal analytic proof,
not a probabilistic conclusion from search.

## Limits of the sharpness search

A bounded search for the analogous dimension-four / six-sender construction left
20 of the 360 four-sender prefixes without found witnesses after 30,000 draws
(3,428 admissible samples). This is INCONCLUSIVE. It proves neither a shorter
reduction nor nonexistence of a sharp example. The search samples candidates to
FIND witnesses only; it never substitutes a grid for an exact continuum decision.

We have established sharpness for d=0,1,2,3, including a small explicit triangle,
and ruled out a dimension-independent bound of two or three. General sharpness
for all d≥4 remains unresolved in this run. No model change was used to manufacture
sharpness. The main research question should remain unchanged; the next bounded
attack is either a general sharpness construction or exact selection/certificates
for rational polygons, where there are only O(n^3) candidate prefixes but
multivariate exact feasibility is a separate bit-complexity problem.

**Parameter-specific limit.** The d=2 and d=3 examples deliberately specify receiver
thresholds near one, which are allowed by R08's general A,B model. They do not
establish sharpness if one additionally fixes the illustrative A=2,B=1 (τ=2/3)
throughout every example. No signal, message, timing, target or equilibrium rule
changed. Whether a fixed upper probability threshold permits a smaller universal
prefix bound is an additional open question, not a claimed result.
