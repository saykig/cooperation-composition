# General sharpness theorem with dimension-dependent admissible payoffs

19 September 2026. Handwritten proof, not Lean checked. All sender labels in this
file are ZERO-BASED to keep the formulas short. R08's strategic game and favorable
sequential-equilibrium selection are unchanged.

## Theorem

For every integer d≥0 there is a rational polytope P of ACTUAL affine dimension d,
with n=d+2 senders and rational admissible parameters, on which:

1. one prefix of length d+1 sustains the all-silent/C target at zero enforcement
   throughout P; every completion of that prefix does so;
2. every prefix of length at most d can be defeated by a compatible model in P
   making every one of its cascade inequalities STRICT.

Thus R10's d+1 prefix bound is sharp for every d when receiver payoffs may depend
on d. The statement does not require one model defeating all shorter prefixes.
It does not establish sharpness with a common fixed receiver threshold τ<1.
The construction below specifies τ_d→1 explicitly. It also uses the least possible
number of senders: R10's n−1 bound rules out needing d+1 when n<d+2 and d≥1.

For d=0 take a singleton p=(1/4,1/4), r=(1/4,1/4), τ=2/3. A first sender is at a
favorable tie, and the empty prefix does not block anything. Henceforth d≥1.

## Rational parameters and the common affine slice

Put m=d+1≥2, n=m+1, and

    C=m(m+1)/2,
    κ=1/[8m(C+1)],       γ=1/[2(C+1)],
    ε=γ/[m(m+1)],        q=1−ε,
    τ=1−εκ/2.

Use B=1, A=τ/(1−τ), η_i=1, k_i=r_i, where

    r_i=q^(m−i)  (i=0,...,m−1),      r_m=q^(m+1).

For a deficit vector x=(x_1,...,x_m), set

    p0=1−εκ,        p_i=1−ε x_i  (1≤i≤m),
    Σ_{i=1}^m i x_i=C.                                      (A)

Equivalently Σ i p_i=qC. All points used below have κ≤x_i≤C. Thus
0<1−εC≤p_i≤1−εκ<τ<1, including p0, because εC<1. All parameters and points are
rational. The lower and upper bounds are uniform for each fixed dimension, so
finite hulls are compact and stay strictly within the permitted probability box.

## Universal successful prefix

Use the canonical prefix (0,1,...,m−1). If every one of its m inequalities were
strict at p, then

    product_{k=j+1}^m p_k > q^(m−j),       j=0,...,m−1.

Multiplying gives product_{k=1}^m p_k^k > q^C. But weighted AM-GM and (A) imply

    product_{k=1}^m p_k^k ≤ (Σ k p_k/C)^C=q^C.

Contradiction. This proves success throughout the ENTIRE affine slice within the
positive box, not just at its vertices. Equality remains a blocker under the
unchanged favorable-tie convention. The last sender's cost is positive and below
one and does not alter this successful-prefix argument.

## Defeating any prefix of length m−1

We construct x for each ordered distinct prefix α=(a_1,...,a_{m−1}). Its labels
belong to {0,...,m}. The construction is allowed to depend on α: these are separate
compatible-model witnesses for a universal statement about candidate protocols.

### Case I: a_1=i>0

Set y_i=C/i and all other y_j=0. Then Σ j y_j=C. Define

    x_j=(1−κ)y_j+κ.                                        (B)

At every step of the prefix, the only possibly large deficit has already been
removed. Each remaining variable deficit, and the fixed deficit of sender 0,
is κ. At most m senders remain, so the sum S of the remaining deficits is at most
mκ. The relevant threshold exponent h is m−i for sender i<m and m+1 for sender m;
in every case h≥1. Therefore S≤h−γ. Also κ≤x_j≤C and Σ j x_j=C.

### Case II: a_1=0

Read the later labels of α, recording only NEW RUNNING MAXIMA. Start at 0 and
append terminal label m if it has not already appeared as a record. Write the
resulting strictly increasing list as

    0=b_0<b_1<...<b_s=m,       Δ_l=b_l−b_{l−1}.

There are at most m−2 later prefix labels, so s≤m−1. Define a raw deficit vector
u supported on the record labels by u_{b_l}=Δ_l, with all other coordinates zero.
Its total deficit is Σu=m and its weighted sum is

    W=Σ_l b_l Δ_l
     = C + Σ_l Δ_l(Δ_l−1)/2 ≥ C+1.                         (C)

The identity follows by comparing the endpoint b_l repeated Δ_l times with the
sum of the consecutive integers b_{l−1}+1,...,b_l. At least one Δ_l≥2, since the
m positive integers are partitioned into at most m−1 blocks. This is the strict
slack that a random search was failing to exploit.

Normalize and move slightly toward the all-ones vector:

    y_j=C u_j/W,           x_j=(1−κ)y_j+κ.                 (D)

Then Σ j x_j=C and κ≤x_j≤C. Consider a step ending in label i<m and let R be the
largest positive label encountered so far, with R=0 just after the initial sender.
Every raw record deficit at a label at most R has already been removed; none at a
larger label has. Thus the total raw deficit still present is exactly m−R. Since
R≥i, the normalized remaining deficit is at most (m−i)C/W. The added κ component
involves at most m coordinates. Writing h=m−i≥1 gives

    S ≤ (1−κ)h C/W+κm
      ≤ h − h/(C+1)+κm
      ≤ h − 7/[8(C+1)]
      ≤ h−γ.                                              (E)

If the current sender is m, then all raw deficits have already been removed;
the remaining sum is at most mκ, whereas its exponent is h=m+1. Again S≤h−γ.
Including m as an artificial final record creates no new strategic constraint:
it only specifies where the raw deficit is placed. If m is actually visited,
all subsequent nonrecord steps still satisfy (E).

## From deficit slack to strict product inequalities

The preceding cases give S≤h−γ at every prefix step, with 1≤h≤m+1. All factors
are 1−ε times a nonnegative deficit and lie in (0,1). The elementary product bound
and the second-order Taylor upper bound give

    product_remaining (1−ε x_i) ≥ 1−εS,
    (1−ε)^h ≤ 1−hε + h(h−1)ε²/2.

For the second inequality, integrate f''(t)=h(h−1)(1−t)^(h−2)≤h(h−1) on [0,ε];
h=1 is an equality. The first follows by induction from (1−a)(1−b)≥1−a−b.
The fixed sender 0 uses deficit κ in this notation. Therefore

    product_remaining p_i − r_current
      ≥ εγ − m(m+1)ε²/2
      = εγ/2 > 0.                                        (F)

This is a uniform rational positive slack, not an asymptotic o(ε) argument.
It proves the original strict cascade inequalities for EVERY length-(m−1)
prefix. No numerical optimization or generic-position assumption enters this proof.

## Actual dimension and the finite hull

Include the center x*=(1,...,1), and, for j=1,...,m−1, include

    x^(j)=x*+(1/4)e_j−[j/(4m)]e_m.

They satisfy (A), remain within [κ,C]^m, and their differences are independent:
the first m−1 coordinates give a diagonal matrix with diagonal 1/4. Their images
under the affine map x↦p therefore span dimension m−1=d.

Let P be the convex hull of these m dimension-spanning points and the point
constructed in (B) or (D) for EVERY ordered prefix of length m−1. This is a finite
rational polytope. It lies in the two independent affine constraints p0=1−εκ and
Σ i p_i=qC, so its dimension is at most m−1; the spanning points give equality.
The AM-GM argument proves success everywhere in P. Every shorter prefix α can be
extended to one of length m−1; its earlier suffix products depend only on the
already-removed set, so the witness for that extension also defeats α. This includes
the empty prefix, whose conjunction is vacuously true on nonempty P.

The same proof works on the larger explicit compact polytope

    {p: p0=1−εκ, Σ i p_i=qC,
         1−εC≤p_i≤1−εκ for i=1,...,m}.

No factorial list is needed to describe that H-polytope. The finite-hull version
makes each shorter-prefix witness an explicitly retained compatible point. ∎

## Scope of the theorem

This establishes arbitrary-d sharpness, not just a pattern in isolated dimensions.
Its dependence on d is explicit: both q and τ approach one, with

    1−τ = 1/[32 m²(m+1)(C+1)²].

This is a sufficient choice, not a claim that this rate is necessary. Costs and
receiver payoffs vary with d but are fixed within each constructed game. The
strategic rules, target, intervention/fine meaning and equilibrium concept do not
change. The fixed-threshold question is treated separately in
[FIXED_THRESHOLD.md](FIXED_THRESHOLD.md), including a limitation of this particular
uniform-AM-GM construction. Sharpness gives no computational-hardness conclusion.
