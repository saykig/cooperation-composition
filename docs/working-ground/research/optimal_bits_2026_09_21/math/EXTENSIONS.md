# Conditional gates — fixed dimension and labelled trees

21 September 2026. Written proofs; only the finite tree budget calculation is
implemented here. The higher-dimensional codec below is effective but deliberately
not claimed efficient. No continuous fine frontier beyond 0-or-B is introduced.

## 1. Fixed-dimensional optimal bits

Fix ambient n, affine dimension bound d<=n, and a nontrivial positive box strictly
below tau. In Gate 2's one-approximate-block model,

    R*(gamma) = Theta(gamma^(-(d-1)/2)),  d>=2,
    R*(gamma) = Theta(log(1/gamma)),      d=0 or d=1.

The class may be restricted to exact affine dimension d for the same worst-case
rates. The lower bound is the R15 positive curved-patch packing for d>=2,
embedded in n dimensions with remaining coordinates fixed. For d=0 use rational
singletons with one varying coordinate, with multiplicative separation >exp(2gamma).
For exact dimension one attach a short fixed segment in a different coordinate
when n>=2, or use intervals with a varying upper endpoint when n=1. A known
first sender detects these endpoints. The number of choices is Omega(1/gamma),
so the lower bound is logarithmic. Points and segment endpoints give the upper
bound by direct downward coordinate rounding.

Here is a uniform, finite-codebook construction proving the higher-dimensional
upper bound without a hidden per-source dictionary.

**Intrinsic rational codebook.** In a fixed bounded cube in R^d, enumerate all
convex hulls of nonempty subsets of a rational grid of mesh h. Greedily retain
the first one, then each hull whose Hausdorff distance from every retained hull
exceeds h. All pairwise distance decisions terminate: squared Euclidean distance
from a rational vertex to a rational polytope is decidable by rational quadratic
programming (or enumerate faces and solve their least-squares projections).
Maximum directed distance between polytopes is attained at a vertex, since
distance to a convex set is convex. Thus no real oracle is needed.

This is a finite deterministic algorithm fixed once and for all, indexed by
dyadic h. Its output is an h-cover of all grid hulls. Every convex compact set
in a slightly smaller cube is within O_d(h) of a grid hull: round a finite
approximating set, or use all grid cells meeting the set and their corners.
Bronshtein's Hausdorff entropy bound implies that the retained h-separated
codebook has at most `exp(O_d(h^(-(d-1)/2)))` members. Indeed a cover by h/3 balls
can contain at most one such separated center per ball. Its index therefore
costs O_d(h^(-(d-1)/2)) bits. The entire codebook is computed by the fixed decoder,
not transmitted as uncharged source-dependent advice. Runtime can be enormous.

**Unknown affine span.** Represent a d-dimensional family as a translated
isometric image of a bounded intrinsic convex set, padding lower-dimensional
ones if needed. Quantize the n translation and nd orthonormal-frame entries to
precision O(h); exact orthogonality of the rounded frame is unnecessary.
The resulting map perturbs every bounded intrinsic point by O_(n,d)(h).
These headers cost O(nd log(1/h)) bits. Combined with an intrinsic codebook
index, they specify a rational ambient polytope C with
`d_H,infinity(P,C)<=epsilon` for h a sufficiently small fixed multiple of epsilon.
One can select a suitable header and index by finite search and exact distance
testing, even though the existence proof used a real orthonormal frame.

**Recover one-sided assurance.** Put Q=C-epsilon*(1,...,1).
Every q in Q is dominated by a nearby point of P. Conversely every p in P is
dominated by q+2epsilon for a q in Q. For epsilon<ell/4 all Q coordinates are
at least ell-2epsilon>0. Thus

    D(Q) subset D(P) subset (1+2epsilon/(ell-2epsilon))D(Q),
    Delta+(P,Q) <= 2n epsilon/(ell-2epsilon).

Choose epsilon a small constant times gamma. For d>=2 the O(log(1/epsilon))
orientation/position headers are absorbed in the power-law term. Arbitrary affine
orientation, thin sets and dimension degeneracy therefore do not reintroduce the
logarithmic multiplier. The decoded family can have higher affine dimension;
no fixed-intrinsic-dimension query runtime is inferred from this encoding.

The source-readable checker can again decide the two inclusions with no extra
witnesses, once the codebook has been expanded. This proves an information rate,
not a practical higher-dimensional encoder or verifier.

## 2. Finite shared labels and their bit price

For q named labels retain emptiness exactly and encode each nonempty P_s at a
local error beta_s. Never replace the table by max_s H_(P_s). If compatible
attachments have errors e_s, the wired error is at most
`max_(compatible s)(beta_s+e_s)`. This is inherited R15's per-branch proof.

For q planar entries, equal beta gives O(q beta^-1/2) bits plus label/framing
metadata and q emptiness bits. If labels are fixed public consecutive indices,
the equal-accuracy format needs no arbitrary label-name precision overhead.
If the query/composition class includes a selector context which retains exactly
one label (other attachment slices are empty), the rate is also
Omega(q gamma^-1/2): choose an independent R15 packing in each entry. Any two
distinct tables differ in some entry, select it, and use its rational contextual
separator. Counting gives the product packing. Without such label selection,
this direct-sum lower bound is not asserted; an unobservable label may be redundant.

## 3. Tree-structured finite interfaces

Let a finite tree have nodes v, disjoint sender blocks, and a finite label on
every edge. A local table assigns a compact convex family P_(v,a) to each tuple
a of incident edge labels, or marks it incompatible. For a globally compatible
edge assignment sigma, conditional uncertainty is the product of all local
families. The actual uncertainty is the UNION of these products. This expresses
analyst-side coupling; private bits are still independent in each actual model.
The approximated table must retain exactly the same compatibility mask.

Suppose every local lower approximation has certified directed error
e_v(a). Define

    E = max_(compatible sigma) sum_v e_v(sigma restricted to v).

For EVERY order and rational cost vector, including arbitrary exact independent
attachments,

    0 <= m(P_wired)-m(Q_wired) <= E.

The same bound holds after minimizing over a common set of orders. Proof: apply
R15 product addition and its margin bound for each fixed sigma; its branch error
is the displayed sum. Take the maximum over the identical finite compatible
assignments on each side. Minima over the identical orders preserve inequalities.
There is no minimax interchange across the nonconvex union.

Compute E exactly by a max-sum tree recursion. Root the tree. For a nonroot v
and parent-edge label a, send

    message_v(a) = max_(compatible child-edge labels b)
        [e_v(a,b) + sum_child w message_w(b_w)].

Impossible choices have value minus infinity. At the root maximize the analogous
expression without a parent label. Induction on subtrees proves equality with
the global compatible-assignment maximum. This is standard tree dynamic
programming applied to the already proved enforcement error rule. Runtime is
polynomial in the explicitly listed local table sizes and edge alphabets;
high-degree implicit tables are not free. The empty global family receives an
explicit incompatibility answer, not a finite error or an invented model.

This recursion computes the **error budget**, not the optimal disclosure order
or the full enforcement margin. Scalar messages for errors are sufficient here;
scalar positive-support messages for all strategic queries need not be, as R15's
nonconvex example shows. New cross-tree constraints require a new interface and
can invalidate the guarantee. Cycles permit the same global inequality but lose
this simple tree recursion; no treewidth-independent algorithm is claimed.

## Gate report

Strongest established results: fixed-d matching information rates with an
effective decoder; optional label-selection direct-sum lower bound; exact
tree-computable certified error budget. Failed shortcuts: quantizing ambient
vertices then assuming intrinsic dimension is preserved; claiming all labels
always require separate information; replacing tree error messages by complete
strategic summaries. Evidence: written proofs; exact exhaustive comparison of
the tree recurrence on the committed fixtures. Higher-dimensional codebook search
has not been implemented or benchmarked. Literature: classical convex entropy,
stars-and-bars counting and max-sum elimination supply the generic ingredients;
R15 supplies the enforcement calibration. Remaining work: practical d>=3 codecs,
time/certificate tradeoffs, label minimization under restricted observations, and
strategic formalization. The main question remains stable and its finite-budget
storage component is resolved. Next bounded attack: formalize the R15 sandwich
to contextual interval theorem after completing R08 target existence; do not
broaden to continuous enforcement frontiers merely because the bit gate closed.
