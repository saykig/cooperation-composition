# Ordering structure, adaptation and useful compression

## T5: a valid adjacent-exchange rule

Suppose i,j are adjacent, followed by a suffix with probability product Q.
The two local strict cascade requirements are equivalent to

    Q > T_ij := max(r_i/p_j,r_j)          for order i,j,
    Q > T_ji := max(r_j/p_i,r_i)          for order j,i.

If r_i p_i≥r_j p_j, then r_i/p_j≥r_j/p_i and r_i/p_j≥r_i, so T_ij≥T_ji.
All other cascade inequalities are unchanged by swapping i,j: earlier suffixes
contain both and later suffixes contain neither. Thus putting i before j under
this condition can only REMOVE cascading models, never add one.

If the score dominance r_i p_i≥r_j p_j holds throughout P, the swap is uniformly
safe. For a polytope this condition is linear and is checked at its vertices or
by an LP. This is an actual pairwise structural rule, unlike an assumption that
all strategic constraints are pairwise.

**Corollary (stable-score greedy class).** If there is an order σ for which
r_{σ1}p_{σ1}≥...≥r_{σn}p_{σn} for every p∈P, then σ is pointwise at least as
protective as every other order, by repeated adjacent swaps. In this class,
there is a common zero-fine order iff

    for every p∈P, there is i with r_i ≥ product_{j≠i}p_j.

The right side can be checked by one convex maximum of the minimum of the n
concave log-product margins. The equivalence between modelwise choice and one
institutional order is EARNED by stable scores here, not assumed generally.

Stable scores are sufficient, not necessary. With only partial uniform dominance,
the proved operation is an ADJACENT swap. Moving a nonadjacent sender can cross
incomparable senders and change their suffix incentives; no global linear-extension
optimality theorem is inferred from that local rule. Successful orders are not in
general all extensions of a poset, as C3 shows. No general efficient greedy
algorithm is proved.

For fixed p, write q_i=−log p_i and d_i=−log(r_i p_i). Reversing the disclosure
order turns cascade constraints into scheduling completion times C_i<d_i with
processing times q_i. This is a useful scheduling translation. The institution
wants at least ONE deadline violation in every model, whereas standard maximum-
lateness minimization wants to avoid lateness. Its due dates also depend on the
uncertain processing times. Therefore deterministic EDD/Lawler results and robust
min–max-regret hardness do not directly solve this problem. Importing their sign
or objective would reverse the intended institutional protection.

## T6: deterministic adaptive ordering cannot improve this benchmark

A policy may choose each next uncalled sender from the previous public certificate/
silence history; each sender is called exactly once. The policy is fixed before
p is known to the institution, has no additional signals, and does not randomize.
Every such decision tree has a unique all-positive-certificate path, inducing
one permutation π⁺. Then for every p and fine, its minimum fine is exactly that
of the fixed order π⁺. Hence its robust minimum and the optimum over adaptive
policies equal those for fixed orders.

Proof. After any silence, one certificate can never be obtained. In any consistent
assessment the probability of its fact being positive is at most its prior:
negative types always stay silent; positive types do so with probability ≤1;
unobserved bits are independent of earlier history and identity choices based
only on that history. Thus the incomplete-evidence receiver prefers C, and further
costly reports cannot induce D. All incentive-relevant continuations therefore
lie on the unique all-positive branch. Along it independence leaves future
positive-fact probabilities unchanged and R08's backward induction applies with
π⁺. If every suffix inequality is strict, the first positive sender initiates a
cascade. If one fails weakly, select silence there and completion is blocked;
select silence on the other histories as well. At B, select C after complete
certification. These choices are sequentially consistent using independent type-
contingent report trembles, including each history of the fixed public tree. ∎

This is a one-successful-path consequence of the receiver's AND rule, not a general
no-value-of-adaptation theorem. To gain from adapting to messages one must escape
at least one premise: e.g. multiple sufficient certificate sets, additional signals,
revisits, or a changed receiver objective. None is asserted sufficient by itself.
A public lottery selecting a fully revealed tree BEFORE any report also cannot
help the all-silent robust target: each positive-probability realized tree must
work for every model. Concealed future randomization is a different game and is
not covered. No necessary/sufficient gain theorem for those extensions is claimed.

## T7: a convex log-space object behind the certificates

Let D(P)={x∈R^n: x≤log p coordinatewise for some p∈P}. This downward closure is
closed and convex for compact convex positive P. Closedness follows by taking
convergent subsequences of the witnessing p's. For convexity, if x≤log p,y≤log q,
then θx+(1−θ)y≤log(θp+(1−θ)q), by coordinatewise concavity of log; the arithmetic
mixture lies in P. No claim that log(P) itself is convex is needed.

Every cascade region is an intersection of open halfspaces in x with nonnegative
normals. Its intersection with log(P) is nonempty iff its intersection with D(P)
is nonempty. Therefore D(P), or the relevant chain projections of it, is sufficient
for every order query with fixed costs. T1 is convex separation of these objects.

Equivalently one may discard coordinatewise dominated probability vectors: all
cascade inequalities are increasing. This agrees with the ordinary monotone
coupling of independent Bernoulli bits and with series-system reliability products.
It is not a license to replace P by its coordinatewise upper corner unless that
corner is actually compatible. The projection lower bound in T4 shows why merely
retaining low-order marginal feasible sets can still lose the answer.
