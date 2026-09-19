# Exact robust-order alternative and polytope certificate

## Model and inherited result

Use precisely R08: n≥2 independent Bernoulli facts in each actual model;
positive priors p_i; one sender sees each bit and can disclose only its positive
certificate, at cost k_i>0; sender reward η_i>0 for receiver action D; receiver
payoffs B>0 for D when all facts are positive and −A otherwise, with a uniform
fine e for D. Target: complete silence and C. Players know p. The institution
chooses ONE order and fine, not a model-indexed order. Sequential-equilibrium
existence and favorable ties are retained. Let r_i=k_i/η_i>0 and let P be a
nonempty compact convex subset of (0,τ)^n, τ=A/(A+B)<1.

R08's backward-induction theorem says an order π requires B rather than zero
exactly when every position j satisfies

    product_{l>j} p_{π_l} > r_{π_j}.                     (1)

A blocker is a weakly reversed inequality. All later statements specialize this
benchmark; they are not results about arbitrary sequential evidence games.
Positive costs and strict receiver preference after incomplete evidence are vital.

## T1: convex alternative, for any n

Define concave continuous functions on P

    f_j(p)=sum_{l>j} log p_{π_l} − log r_{π_j},
    m_π(P)=max_{p∈P} min_j f_j(p).

The empty sum is zero. Then exactly one of these alternatives holds:

1. m_π>0: some p makes every inequality (1) strict, so robust fine is B.
2. m_π≤0: π works with zero fine, and there exists λ∈Δ_n such that

       sum_j λ_j f_j(p) ≤ 0  for every p∈P.             (2)

Consequently some common zero-fine order exists iff there are π and λ satisfying
(2). This replaces a model-dependent disjunction of blockers by ONE weighted
log-product inequality. It is not a demand for one universally blocking sender.

Proof. min_j f_j=min_{λ∈Δ} Σλ_j f_j. The integrand is concave continuous in p and
linear in λ, and both sets are compact convex. The compact convex-concave minimax
theorem gives

    m_π = min_{λ∈Δ} max_{p∈P} Σλ_j f_j(p).

The minimum is attained. Thus m_π≤0 is equivalent to (2). m_π>0 is exactly strict
cascade feasibility. R08 supplies the equilibrium interpretation. ∎

The strict sign matters: zero margin is deterrence under favorable tie selection.
This is an application of established minimax/convex alternatives, not a new
minimax theorem. Without convexity of P, the universal weighted certificate can
be stronger than the absence of a cascade and this proof does not apply.

## T2: finite certificate for a polytope

Let P=conv(V)⊂(0,τ)^n. For an order and λ define

    w_{π_l}=sum_{j<l}λ_j,       c=Σ_j λ_j log r_{π_j}.

A zero-fine order exists iff there are π, λ∈Δ_n, and z∈P satisfying

    Σ_i w_i log z_i ≤ c,                               (3)
    Σ_i (w_i/z_i)(v_i−z_i) ≤ 0  for every v∈V.         (4)

Proof of sufficiency. Concavity of log gives
Σw_i log p_i ≤ Σw_i log z_i+Σ(w_i/z_i)(p_i−z_i).
The last term is nonpositive on P by (4), so (2) follows. Necessity: take λ from
T1 and a maximizer z of its weighted-log objective. The first-order optimality
condition on convex P is exactly (4); the maximum obeys (3). ∎

For an H-representation P={p:Hp≤h, Ep=d}, replace (4) by a normal-cone witness

    w/z = H^T μ+E^T ν,  μ≥0,  μ_a(H_a z−h_a)=0.

Together with feasibility of z, this checks the same supporting hyperplane.
No full-dimensionality or strict Slater point is needed for a polytope's normal
cone description. Zero weights, including w_{π_1}=0, are allowed.

This is a finite REAL certificate. It is not a proved polynomial-bit rational
certificate in every boundary instance. If z,λ,r are rational, (3) can be checked
exactly by clearing denominators in the exponents and comparing rational products.
A numerical near-zero margin is not an exact certificate.

For a supplied order, maximizing t subject to p∈P and t≤f_j(p) is convex
optimization. It avoids enumerating models or equilibria. This gives standard
approximation methods with suitable numerical regularity; it does NOT establish
a polynomial-time exact zero test, nor polynomial-time selection among orders.

## A rational certificate for R08's switching blocker

R08 has order (1,2,3), r=(7/50,2/5,1/10), and
p=(13/20,17/20−5s/4,s), s∈[1/5,13/20]. Set

    λ=(7/10,3/10,0), z=(13/20,7/20,2/5).

Then w=(0,7/10,1), w/z=(0,2,5/2). This normal is orthogonal to the segment's
direction (0,−5/4,1), so (4) holds with equality at both vertices. Moreover

    z_2^7 z_3^10 = (7/50)^7 (2/5)^3,

which is (3) after multiplying logarithms by ten. Thus the entire continuum is
certified by rational arithmetic, though neither one sender nor independent
coordinate maxima explain the robustness. λ is a proof weight, not an actual
randomization by an institution or sender.

## T3: exact enforcement and boundary structure

Let M(P)=min_π m_π(P). Then optimized robust fine is zero iff M(P)≤0 and B otherwise.
In this benchmark there is NO intermediate positive enforcement level; this is
inherited from the receiver's complete/incomplete certificate dichotomy in R08.

For fixed r,B and compact P varying Hausdorff-continuously inside a common positive
box, each m_π and their finite minimum M are continuous (compact maximum theorem).
Hence the B-region is open and the zero-region closed. Discontinuities can only
occur at M=0, and occur there exactly when points with M>0 approach. A zero margin
alone need not be a discontinuity. This is lower semicontinuity of the binary value.

With a fixed finite parametric polytope description and polynomial coefficients,
the condition is semialgebraic: write (1) as polynomial product inequalities,
quantify p, and take a finite disjunction over permutations. Real quantifier
elimination therefore gives a finite semialgebraic partition with values 0/B.
This is an exact existence result, not an efficient algorithm or a linear-boundary
claim. It does not justify importing complexity results for different scheduling
objectives. Exact variable-n decision complexity remains open in this run.
