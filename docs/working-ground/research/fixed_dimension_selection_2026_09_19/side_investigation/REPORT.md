# Independent sharpness side investigation

19 September 2026. Main game, equilibrium concept and research question unchanged.
This is a bounded independent review of R11, not a new research frontier.
The two results below are written proofs, supported by exact rational replay;
neither is Lean checked and historical novelty is unclaimed.

## Outcome and recommendation

More isolated dimensions would add little: R11 already proves every dimension.
Tightening the twenty numerical optimum brackets would likewise not strengthen
existence or the arbitrary-dimensional proof. Two analytic improvements are more
informative:

1. R11's fixed-threshold singleton obstruction is **sharp for that particular
   ansatz**, when its free parameters may be chosen. Its exact threshold approaches
   one at rate 2/m². This is not a universal obstruction for the game.
2. The explicit general construction can use a larger perturbation and provide a
   stronger uniform cascade margin. Its sufficient threshold deficit improves
   from order m^-7 to order m^-6. This remains far from the necessary ansatz
   threshold deficit of order m^-2 and does not resolve fixed-threshold sharpness.

The algorithmic work on exact selection beyond segments should retain priority.
If another sharpness gate is eventually authorized, investigate whether the
remaining parameter-rate gap is intrinsic to the witness construction or only to
its product estimate. Do not fill that gap with additional random dimensions.

## S1. Exact threshold for avoiding the distinguished singleton obstruction

Use precisely R11's uniform-AM-GM ansatz. Let m≥2, C=m(m+1)/2, i=m−1, and

    0<p_0<τ<1,   0<p_k<τ (1≤k≤m),
    Σ_{k=1}^m k p_k=qC,   0<q<τ,   r_i=q.

Other ratios are as in R11. Put T=p_0 ∏_{1≤k≤m,k≠i}p_k. Sender i can initiate
a strict cascade when placed first exactly when T>q. We ask whether this ONE
inequality can be met for some q and compatible p; it is not the all-prefix test.

**Proposition.** For fixed m, τ and p_0, there exist q and compatible variable
coordinates with T>q if and only if

    p_0 τ^(m−2) C/(C−i)>1.                            (1)

Allowing p_0 to vary in (0,τ), this is possible if and only if

    τ>τcrit(m):=((C−i)/C)^(1/(m−1)).                   (2)

**Necessity.** For every j≠i, the other m−2 variable factors are at most τ,
so T≤p_0 τ^(m−2)p_j. Multiplying by j and summing yields

    T(C−i) ≤ p_0 τ^(m−2) Σ_{j≠i}j p_j
            < p_0 τ^(m−2)qC.

The second inequality is strict since p_i>0. Thus T>q implies (1). Since p_0<τ,
(1) implies (2). Equality at the critical threshold is an obstruction too;
favorable ties cannot be counted as a strict cascade witness.

**Sufficiency.** Set q=τ(C−i)/C. For δ>0 choose

    p_j=τ−δ for j≠i, j≥1;
    p_i=δ(C−i)/i.

The affine budget holds exactly. For sufficiently small δ all coordinates are
strictly between zero and τ, and

    T=p_0(τ−δ)^(m−1) → p_0 τ^(m−1)>τ(C−i)/C=q

by (1). Therefore a sufficiently small positive δ gives a strict witness. When
m, τ and p_0 are rational, q and a sufficiently small dyadic δ are rational too.
For (2), first choose p_0 strictly between (C−i)/(Cτ^(m−2)) and τ. ∎

**Quantitative implication.** Let x=(m−1)/C. Then

    log τcrit=log(1−x)/(m−1),   m²(1−τcrit)→2.

For example τcrit(2)=2/3 and τcrit(3)=sqrt(2/3). The limit follows from
−x/(1−x)≤log(1−x)≤−x and (1−exp(−y))/y→1. Thus even the best q and p_0 in this
ansatz require thresholds approaching one. The old sufficient singleton bound is
not merely a loose estimate after optimizing these two parameters.

**Scope.** Above τcrit, only this particular singleton is shown defeatable.
Other singletons, longer prefixes, actual dimension and full sharpness can still
fail. Below τcrit the obstruction applies to this affine budget and geometric
cost pattern; it proves nothing universal about arbitrary uncertainty families.
No R11 artifact or receipt is overwritten.

## S2. Less conservative parameters for R11's general construction

Retain R11's witness formulas, running-record argument, canonical prefix,
dimension-spanning points and finite hull. Replace only its two small parameters by

    κ=ε=1/[2m(C+1)],   q=1−ε,   τ=1−εκ/2,
    r_j=q^(m−j) (j<m),   r_m=q^(m+1).

As before p_0=1−εκ and p_j=1−εx_j, with Σ j x_j=C and κ≤x_j≤C.
R11's raw deficits y are blended as x_j=(1−κ)y_j+κ. All probabilities lie in
(0,τ): εC<1 and p_j≤1−εκ<τ. The affine budget and weighted AM-GM success proof
are unchanged. The dimension-spanning points still lie in [κ,C]^m.

**Proposition.** Every prefix of length m−1 has the R11 rational witness, and at
each step, with threshold exponent h=m−j for sender j<m and h=m+1 for sender m,

    product_remaining p_k − r_j ≥ εh/[4(C+1)]
                                ≥ 1/[8m(C+1)²]>0.       (3)

**Proof.** Write S for the remaining total deficit, including κ if sender 0
remains. When the first sender is positive, the large raw deficit has already
been removed and S≤mκ. The same bound applies at sender m after all raw record
deficits have been removed. Since h≥1 and C+1≥4, in these cases

    h−S ≥ h/[2(C+1)].

In the remaining running-record case, R11 establishes W≥C+1 and R≥j. Retaining
the factor h instead of replacing it with one gives

    S≤(1−κ)h C/W+κm
     ≤h−h/(C+1)+1/[2(C+1)]
     ≤h−h/[2(C+1)].

The product lower bound and second-order binomial upper bound used in R11 imply

    product_remaining p_k−(1−ε)^h
    ≥ε(h−S)−h(h−1)ε²/2
    ≥εh(1/[2(C+1)]−mε/2)
    =εh/[4(C+1)].

Here h≤m+1, the empty product convention is harmless, and all inequalities
remain strict at the final positive lower bound. This proves (3). The R11 hull,
affine-rank and extension arguments now give sharpness in every d=m−1 using
these replacement parameters. ∎

The new receiver-threshold deficit is

    1−τ=1/[8m²(C+1)²],

which is 4(m+1) times the previous sufficient deficit. The uniform guaranteed
product margin is m+1 times the previous bound. These are proved guarantees,
not estimated optimizer performance or claims of optimal parameter choice.
This refinement does not approach a fixed τ<1 as m grows.

## Evidence, sources and limitations

`check.py` uses only Python standard-library rational arithmetic. It checks the
improved witness and its quantitative bound for every length-(m−1) prefix for
m=2,...,6, then checks selected structured prefixes in larger dimensions. It also
constructs rational witnesses immediately above the S1 threshold and verifies
the exact rational obstruction predicate immediately below it. No sampled grid
decides feasibility. `results.json` records counts, input ranges and source hash;
finite replay supports the all-m written proofs but cannot replace them.

The construction, weighted AM-GM argument, record-deficit identity and prior
product/Taylor estimates are borrowed directly from
[R11's complete construction](../../general_sharpness_2026_09_19/math/GENERAL_CONSTRUCTION.md).
The initial inequality sharpened in S1 is R11's
[fixed-threshold bound H](../../general_sharpness_2026_09_19/math/FIXED_THRESHOLD.md).
No new AM-GM, Helly, root-isolation or convex-optimization theorem is claimed.
No new external literature claim is made by this side investigation. A separate
novelty search and independent formal replay have not been performed.
