# What is and is not proved at a fixed receiver threshold

19 September 2026. This note prevents construction-specific obstructions from
being misreported as universal bounds for the game.

## Two different quantifiers

The general theorem proves

    for every d, there EXIST admissible payoffs/τ_d and a d-dimensional family
    whose shortest successful prefix has length d+1.

It does NOT prove

    for one preassigned τ (e.g. 2/3), for every d there EXISTS such a family.

Nor does it disprove the latter. Our τ_d approaches one; the explicit formula is
part of the theorem rather than an omitted admissibility condition.

## The original fixed-q construction eventually cannot work

Consider the uniform-AM-GM ansatz with labels 0,...,m, p0∈(0,1),
Σ_{k=1}^m k p_k=qC, C=m(m+1)/2, and r_i=q^(m−i) for i<m. Put i=m−1, whose ratio
is r_i=q. If that sender could initiate when placed first, then

    p0 product_{1≤k≤m,k≠i} p_k > q.

Because p0<1, the product over the other VARIABLE coordinates also exceeds q.
Using 1−x≤−log x and −log q≤(1−q)/q gives

    Σ_{k≠i}(1−p_k) < −log q ≤ (1−q)/q.

Consequently the affine deficit budget would satisfy

    (1−q)C = Σ k(1−p_k)
            < i + m(1−q)/q.                              (G)

Thus if the reverse weak inequality holds, i alone universally blocks disclosure;
this ansatz cannot require more than one sender in its successful prefix.

For q=4/5, the sufficient obstruction condition is

    m(m+1)/10 ≥ m−1+m/4.

It holds for every m≥11: after multiplying by 20 the difference is
2m²−23m+20, positive at m=11 and strictly increasing thereafter. Hence the EXACT
fixed-q ansatz used in R10 cannot establish all-dimensional sharpness, even if
one is free to raise the upper threshold. This does not affect m=5: all twenty
previously missing prefixes there have now been certified defeated.

The proof of −log q≤(1−q)/q is the integral bound
−log q=∫_q^1 dt/t≤(1−q)/q. These are analytic inequalities, not sampled numerics.

## Stronger limitation of this ansatz at fixed τ

Suppose additionally every p_k<τ<1, allowing q to vary arbitrarily with m.
Let T=p0 product_{1≤k≤m,k≠i}p_k, again i=m−1. For EACH j≠i,

    T < τ^(m−1) p_j.

Multiply by j and sum over j∈{1,...,m}\{i}. This yields

    T < τ^(m−1) q C/(C−i).                               (H)

Thus if τ^(m−1) C/(C−m+1)≤1, sender m−1 is a universally successful singleton,
independently of q. For every integer m≥2,

    C/(C−m+1) ≤ 3/2,

because C≥3(m−1) is equivalent to (m−2)(m−3)≥0. For ANY fixed τ<1, the sufficient
obstruction condition therefore holds for all sufficiently large m. In particular
at τ≤2/3 it holds for EVERY m≥2. The uniform-AM-GM/geometric-cost ansatz cannot
produce sharpness at fixed τ=2/3 in any of these dimensions, whatever q is chosen.

This is a limitation of the ANSATZ. Its hypotheses include the special affine
budget Σ k p_k=qC and the matching ratio r_{m−1}=q. Arbitrary games/families need
not satisfy them. Indeed the inherited R08 changing-blocker segment at τ=2/3
requires two senders; it uses nonuniform equality coordinates and different ratios.
So turning (H) into a universal one-prefix claim would contradict a retained
example. No such claim is made.

## Implication and next step

Parameter dependence is real: a fixed q fails eventually, and within this ansatz
any fixed τ also fails eventually. Our general theorem avoids both obstructions
with dimension-dependent rational q and τ. Whether OTHER affine families and
cost profiles achieve all-d sharpness at τ=2/3 remains open.

The requested general construction gate is therefore closed by a theorem plus
precise construction limitations. The next algorithmic question is exact order
selection beyond segments. Neither this lower bound on prefix length nor the
ansatz obstruction establishes NP-hardness.
