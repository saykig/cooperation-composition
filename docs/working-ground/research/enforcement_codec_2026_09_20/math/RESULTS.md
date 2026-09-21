# Operational compression of enforcement interfaces

20 September 2026. New written derivations in this run, conditional on the
R08/R13 game-to-cascade characterization. No proof-assistant verification.

## 0. Inherited model; no strategic assumption has been changed

Fix receiver payoffs A,B>0 and tau=A/(A+B)<1. A block has n labelled senders.
In each actual model their private Bernoulli facts are independent, with positive
probabilities p_i<tau. A positive sender may disclose its authenticated fact at
cost k_i>0; reward for receiver action D is eta_i>0. Set r_i=k_i/eta_i>0.
Target: an all-silent sequential equilibrium ending with C, with favorable ties.
Players know their actual model. The institution chooses one pure order and fine
for its entire analyst-side uncertainty family. Enforcement is a credible uniform
receiver fine; its implementation cost and welfare are not being optimized.

For a nonempty compact convex family P in (0,tau)^n and an order pi,

    L_j^pi(p) = sum_{l>j} log p_{pi_l},
    m_pi(P,r) = max_{p in P} min_j [L_j^pi(p)-log r_{pi_j}],
    M(P,r) = min_pi m_pi(P,r).

The final L is zero. The inherited theorem says E(pi,r)=B if m_pi>0, otherwise
0; optimized enforcement is B if M>0, otherwise 0. The feasible-fine set is an
upward interval beginning at that value. A margin is a logarithm of a continuation-
probability/cost-ratio comparison, NOT a monetary fine, expected deviation gain,
entropy or welfare measure.

An independent attachment R changes the family to P x R and retains the same
all-facts complementary-evidence payoff form. All combined orders are allowed.
This is independent selection of model parameters, not permission to ignore
additional shared constraints.

## 1. Audit of the preceding exact interface result

For w>=0 put H_P(w)=max_{p in P} sum_i w_i log p_i. Define

    D(P)={x>=0: exists p in P with x<=p},
    K(P)={z in R^n: exists p in P with z<=log p}.

Compactness makes these downward sets closed (D also bounded). Concavity of each
log makes K convex: interpolated p dominates the interpolation of the log images.
Positive directions determine K by convex separation; directions with a negative
coordinate have infinite support. Hence D(P)=D(Q) iff H_P=H_Q on w>=0.

For an isolated order, the vector of nonconstant L_j has its own closed convex
downward hull. Strict cascade queries recover its interior, and the hull is the
closure of that interior. Its nonnegative supports are H_P(w) with w increasing
along the order and with the first weight zero. Taking every order therefore
recovers exactly the directions min_i w_i=0. Appending one known sender as a
possible first sender makes every original direction available. Thus the
preceding semantic minimality and one-sender-context argument remain valid.

The earlier upper-restriction revision theorem also remains valid: if x belongs
to P but not Q, impose p<=x. Nonemptiness distinguishes an empty Q slice. Otherwise
sum log p has a strict gap below its value at x on the compact Q slice, so a
contextual query distinguishes the revised families.

Two limits remain unchanged: the result concerns ALL order/cost queries, not
minimality for one optimized value alone; and arbitrary nonconvex families cannot
be replaced by their support-function convexification.

## 2. The error quantity has an exact operational meaning

Define the directed discrepancy

    Delta+(P,Q)=max_{w in [0,1]^n} [H_P(w)-H_Q(w)].                 (2.1)

It is nonnegative because w=0 is allowed. Set Delta(P,Q)=max(Delta+(P,Q),
Delta+(Q,P)). This is a metric on the D(P) equivalence classes. The triangle
inequality follows by splitting H_P-H_R through H_Q.

### Theorem A — exact contextual margin discrepancy

Fix any rho in (0,tau). Then

    Delta+(P,Q)
      = sup_{pi,r>0} [m_pi(P x {rho},r)-m_pi(Q x {rho},r)]         (2.2)
      = sup_{R,pi,r>0} [m_pi(P x R,r)-m_pi(Q x R,r)],              (2.3)

where R ranges over nonempty compact convex independent attachments of arbitrary
finite size. Positive rational ratios give the same SUPREMUM. No actual random
information device or sender payoff transfer is introduced by these tests.

**Upper bound.** Concave minimax gives

    m_pi(P,r)=min_{lambda in simplex}
        [H_P(w^pi(lambda))-sum_j lambda_j log r_{pi_j}],
    w^pi_{pi_l}=sum_{j<l}lambda_j.

Every component of w belongs to [0,1]. For an attachment, H separates into the
sum of block supports. The attachment term cancels in comparing P and Q at any
lambda. The two objectives differ by at most Delta+(P,Q); taking minima proves
the upper bound. The same argument bounds optimized M differences, but equality
for optimized-only queries is not asserted.

**Attainment/lower bound.** If Delta+=0 the upper bound and cost queries with a
uniform immediate blocker give equality zero. Otherwise homogeneity allows a
maximizing weight w with max_i w_i=1. Put the known sender first and sort original
senders by nondecreasing w. Successive weight differences define lambda>=0 whose
sum is one and whose last entry is zero. Pick p* maximizing H_P(w).
For any real z define every log ratio in this combined order by

    log r_j = L_j(p*)-z, including the final log ratio -z.

At p*, all margin coordinates equal z. The lambda-weighted objective is at most
z throughout P, so m_pi(P x {rho},r)=z. On Q it is at most z-Delta+; hence its
minimum coordinate is at most that value. Thus the difference is at least Delta+.
The upper bound proves equality. With z=Delta+/2 the two answers have margins
+Delta+/2 and -Delta+/2. Rational r approximations preserve any slightly smaller
strict margin, by continuity in log r. QED.

This is more than a Lipschitz bound: a discrepancy of this size can be detected by
one actual query in the declared contextual class. The distinguishing order and
ratios may depend on P,Q. It is not a claim about a fixed real institution.

### Theorem B — exact product law and context independence

For independent block pairs,

    Delta+(P1 x P2,Q1 x Q2)=Delta+(P1,Q1)+Delta+(P2,Q2).            (2.4)

Indeed H products add and the weight box splits into two independent boxes, so
the maxima separate. Thus Delta(P1 x P2,Q1 x Q2) is the maximum of the two sums of
directed discrepancies, and is at most Delta(P1,Q1)+Delta(P2,Q2). In particular

    Delta+(P x R,Q x R)=Delta+(P,Q).

Attaching any number of EXACT components adds no approximation error. Compressing
several components accumulates their directed errors additively. This sharpens
the previous bound (total sender count minus one) times a normalized profile error.
The previous normalized distance is still valid; it obscures this precise resource
accounting. Directional errors are essential: symmetric errors need not add exactly.

### Corollary — a decision rule with an honest refinement region

If D(Q) subset D(P) and Delta+(P,Q)<=beta, then for every independent context,
order and cost vector,

    m_Q <= m_P <= m_Q+beta,       M_Q <= M_P <= M_Q+beta.           (2.5)

Hence m_Q+beta<=0 certifies that the specified order works. M_Q>0 certifies that
no order works. Otherwise do not classify by rounding: refine the interface or
return an inconclusive answer. If all queries with |margin|>=gamma must be
answered, beta<gamma suffices. For optimized success an actual order must be
returned. Query-optimization error, if any, must be added separately.

## 3. An exact rational certificate for compression

Let P=conv(V) and Q=conv(W) be positive rational polytopes, with eta>0 rational.
Suppose the certificate supplies

    for every w in W: p_w in P with w<=p_w,
    for every v in V: q_v in Q with v<=(1+eta)q_v.                 (3.1)

Each witness is a rational convex combination of input or decoded vertices.
Then convexity and downward closure give

    D(Q) subset D(P) subset (1+eta)D(Q),                          (3.2)
    0<=H_P(w)-H_Q(w)<=log(1+eta)||w||_1,
    Delta+(P,Q)<=n log(1+eta)<=n eta.                            (3.3)

These are universal inequalities, established by vertex certificates rather than
by checking a probability grid. A verifier needs only rational signs, convex
weights and coverage of every vertex. No logarithm or nonlinear solver is needed
to validate (3.2). The theorem converting that sandwich to (3.3) uses monotonicity
of log; it is a written proof in this run.

Do not interpret Q as a sample whose logged vertex values alone determine H_Q.
It represents ALL convex combinations. For the two-point segment joining
(1/4,1/2) and (1/2,1/4), maximum xy is 9/64 at (3/8,3/8), not the vertex value 1/8.
Keeping just the maximum of logged vertices changes the represented object.

## 4. Explicit small encoder in two coordinates

Input is a vertex list for a convex P subset [ell,u]^2, with 0<ell<=u<tau<1.
Let 0<eta<=1 be a rational requested multiplicative accuracy. For bit-size
asymptotics take eta dyadic and fix ell,u,tau; arbitrary rational parameter encoding
lengths must otherwise be charged separately.

Extract the NE Pareto convex chain, ordered with x increasing and y decreasing.
It is enough to retain this chain: every input point is dominated by a chain point.
Let s be cumulative L1 arclength along it, with total L<=2(u-ell). Along an edge

    dx/ds=a,       dy/ds=a-1,       0<=a<=1.

Concavity of the chain makes a nonincreasing. Set delta=ell eta/4 and
K=max(1,ceil sqrt(L/(4 delta))). Mark both endpoints, every arclength-grid crossing
s=jL/K, and every vertex where floor(K a) changes between its incident edges.
There are at most 2K+2 marked points. A singleton is treated directly.

Between consecutive marked points, length is at most L/K and the variation of a
is at most 1/K. Parameterize the chord by that same arclength. Both coordinates of
the true chain exceed their chord coordinates by the same amount. At a fraction t
of a subchain of length l, the gap equals

    l t(1-t) (mean slope before - mean slope after)
       <= l * slope variation /4 <= L/(4K^2)<=delta.              (4.1)

This proves uniform coordinatewise domination by the convex hull of marked points
up to additive delta. It covers corners: large slope changes occur at marked
vertices, not inside a retained subchain.

Round every marked coordinate downward to an integer multiple of delta and take
the convex hull. Remove dominated/redundant rounded vertices if desired. Rounded
points are dominated by actual points of P, and any actual point is dominated by
a convex combination of rounded points plus 2delta in both coordinates. Every
rounded coordinate is at least ell-delta. Consequently

    p <= [1+2delta/(ell-delta)] q <= (1+eta) q,

because eta<=1. Thus the rational certificate of Section 3 exists.

### Size and algorithm result

The reusable decoded polytope uses at most

    2 max(1,ceil sqrt(L/(ell eta)))+2                             (4.2)

grid vertices; each coordinate is an integer bounded by u/delta. For fixed
ell,u,tau and dyadic eta this is

    O(eta^(-1/2)) vertices,
    O(eta^(-1/2) log(1/eta)) bits.                               (4.3)

Since beta<=2eta, this is O(gamma^(-1/2)log(1/gamma)) bits at a fixed fraction of
a requested contextual margin gamma. The encoder is rational and polynomial in
the explicit input length and 1/eta; it is implemented. This is not a claim of
instance-optimal compression or of a new generic convex-curve approximation rate.

## 5. Higher-dimensional storage bound (written, not implemented)

Fix n, d>=2, ell,u,tau and consider rational convex polytopes of affine dimension
d in [ell,u]^n. Classical convex-body approximation yields an inscribed polytope
with O_d((diam(P)/delta)^((d-1)/2)) vertices and Hausdorff error delta in the affine
span. The same vertex bound suffices if one starts with a general approximant:
project each vertex into P, increasing error by at most a constant factor.

Round those vertices downward on a delta grid as above, adjusting constants to
allow both approximation and rounding. The resulting rational Q obeys (3.2).
Hence the reusable representation has, for fixed parameters,

    O(gamma^(-(d-1)/2) log(1/gamma)) bits                         (5.1)

with contextual directed margin error at most gamma/2. Before absorbing n and
box bounds in constants, vertex count is
O_d((n sqrt(n)(u-ell)/(ell gamma))^((d-1)/2)); a vertex uses
O(n log(nu/(ell gamma))) bits, plus parameter headers.

For rational V-input, the two domination inclusions have rational LP witnesses.
A finite, potentially impractical encoder can enumerate bounded-size grid
polytopes and check the inclusions. No polynomial-time encoder in high dimension
is claimed here. Quantization can raise affine dimension, so efficient downstream
fixed-dimension selection does not automatically follow for this general encoding.
The implemented planar encoder has no such ambient-dimension issue.

At d=0 one point suffices; at d=1 two endpoints specify the convex family before
rounding. Those cases cost O(n log(1/gamma)) bits for fixed bounds. Thus a sampled
model envelope with many points is not intrinsically necessary even if its
log-support optimum lies in the segment's interior.

**Borrowed ingredient:** the convex-body vertex approximation exponent. The
contribution under investigation is its strategic operational calibration,
compositional error accounting and independently checkable encoding.

## 6. A matching power-law information lower bound

First give explicit constants in two coordinates. Let

    x_j=1/4+(3/20)j/(m+1),  j=0,...,m+1,
    v_j=(x_j,3/5-x_j^2).

Keep endpoints; optionally include each of the m internal vertices. The convex
hulls give 2^m families in [1/4,3/5]^2 with identical separate coordinate ranges.
For any optional index k, let n_k=(2x_k,1). Then

    n_k dot (v_k-v_j)=(x_k-x_j)^2 >= h^2,  j!=k,
    h=3/[20(m+1)].                                               (6.1)

Normalize the positive weights w_i=(n_k)_i(v_k)_i by their sum
T=3/5+x_k^2<=19/25. Concavity of weighted log, with gradient n_k/T at v_k, gives

    H_in(w)-H_out(w)>=h^2/T>=9/[304(m+1)^2].                      (6.2)

This holds for every hull containing v_k versus any such hull omitting it, not
only for pairs differing in one vertex. Theorem A converts the support gap to a
single attached-sender query whose margins have opposite signs and magnitudes
at least a constant times h^2. Positive rational cost ratios can realize a
slightly smaller separation.

Therefore any deterministic SELF-CONTAINED summary whose fixed decoder answers
ALL contextual order/cost queries with |margin|>=gamma, without abstaining on
such queries, needs Omega(gamma^(-1/2)) bits in the worst case. This lower bound
applies to arbitrary encodings, not just vertex lists. Variable-length codes
change the counting bound by at most an additive constant. An always-abstaining
decoder does not meet the task.

### General d>=2 construction

Use d-1 coordinates x in a small positive cube, and define

    v(x)=(x,3/5-||x||^2/(d-1)).

All coordinates can be kept in [1/4,3/5]. Fix d+1 rational baseline graph points
whose affine span has dimension d, outside a smaller optional grid patch.
For example with a=1/4 and s=1/(100d), use x0=(a,...,a), x0+s e_i for all i,
and x0+2s e_1; optional points lie in [a+3s,a+4s]^(d-1).
The nonzero second difference in the e_1 direction proves the lifted baseline's
affine dimension is d.

For distinct grid points x,y,

    (2x/(d-1),1) dot (v(x)-v(y)) = ||x-y||^2/(d-1).

With grid spacing h, there are Omega_d(h^(-(d-1))) independent optional vertices.
The same weighted-log tangent and Theorem A give margin separations c_d h^2.
Thus, for n=d (or after appending fixed coordinates), every decoder meeting the
above query requirement needs

    Omega_d(gamma^(-(d-1)/2)) bits.                              (6.3)

Together (5.1) and (6.3) match the exponent and leave a logarithmic gap in our
constructive storage result. We do NOT assert a sharp constant, an optimal
certificate bit count, or optimized-value-only minimality.

## 7. Shared interfaces: retain the coupling label

Let s range over a known finite interface set. Conditional on s, block families
P_s and R_s are independently selectable and compact convex. The actual wired
family is union_s (P_s x R_s). This union need not be convex.

Retain the LABELLED map s -> H_{P_s}, rather than max_s H_{P_s}. For each order,

    m_pi(wired)=max_s m_pi(P_s x R_s).

If block approximations have directed errors e_{P,s},e_{R,s}, the wired margin
error is at most max_s(e_{P,s}+e_{R,s}). Taking minimum over the same orders
preserves this bound. The decoder never takes a minimax exchange across the
nonconvex union. Empty/incompatible labels must be retained explicitly and matched.
The result extends to a finite fixed family of labels by the same argument.

### Exact counterexample to erasing the label

Let the two labels specify point families

    a=(9/16,1/4),       b=(1/9,9/16).

Add a known sender first, with rho=1/2. Ratios for that first sender and the next
original sender are 9/100 and 1/3; the final ratio is 1/10. Label a fails the
second cascade condition; label b fails the first. Both are safely blocked.

Their coordinatewise geometric mean is g=(1/4,3/8). It satisfies

    g1*g2=3/32>9/100,       g2=3/8>1/3.

So it cascades. But log g is the midpoint of log a and log b, so g adds NOTHING to
max_s H_{P_s}. A support-only aggregate cannot distinguish the safe labelled union
from the family additionally containing this unsafe model. This is not a defect
of the conditional interface: it is precisely why the label cannot be discarded.

These labels constrain analyst-side feasible models; they are not necessarily
messages revealed to the players. No new private-bit correlation is assumed.
Arbitrary new cross-block constraints or future upper-bound revisions are outside
this fixed-interface theorem and still require the original model or richer slices.

## 8. What verification costs; no hidden free certificate

The payload for future queries is small. The implemented proof certificate of
its relationship to an arbitrary input list is not guaranteed small. It supplies
one domination witness for every source vertex and every decoded vertex. The
independent verifier rereads the original input and checks rational combinations.
No claim is made that a hash alone proves the connection.

A simple audit lower bound explains a part of this cost. In the model of a
deterministic verifier with random access to an explicit untrusted vertex list
and no separately authenticated commitment, some valid inputs force it to inspect
every listed vertex. If it leaves an entry unread, replace that entry by a legal
vertex outside the claimed expanded downward hull and reuse the same certificate.
The execution is unchanged but acceptance is false. This is an Omega(N) input-
inspection lower bound, not an Omega(N)-bit proof-certificate lower bound. Succinct
cryptographic proof systems would change the trust model and are not used here.

## 9. Proof and novelty status

Theorems A and B, the rational sandwich, the planar encoder analysis, the
quantitative lower construction and finite shared-interface guarantee are written
proofs from this run. The general upper bound explicitly imports established
convex-body approximation. The underlying equilibrium theorem is inherited from
R08/R13; these computations do not re-prove it. The novel-candidate package is the
OPERATIONALLY CALIBRATED, COMPOSITIONAL compression theorem, not Pareto fronts,
support functions, or the classical geometric approximation exponent.

The remaining logarithmic gap and verification/query costs are explicit. No
complete Lean proof, independent human review or historical-priority certification
was executed. Future evidence should be appended rather than editing prior receipts.

## 10. Additive improvement: compact proof certificate, not a repeated source list

The first working verifier used one upper-domination witness per input vertex.
A second construction eliminates those N stored witnesses in two coordinates.

Suppose decoded points q_1,...,q_m are ordered with strictly increasing x,
strictly decreasing y, and nonpositive consecutive cross products (a concave
upper chain). Then D(conv(q)) is exactly the nonnegative set satisfying

    x <= (q_m)_1,   y <= (q_1)_2,
    ((q_j)_2-(q_{j+1})_2) x + ((q_{j+1})_1-(q_j)_1) y
       <= ((q_j)_2-(q_{j+1})_2)(q_j)_1
          +((q_{j+1})_1-(q_j)_1)(q_j)_2   for j=1,...,m-1.

Proof: each sloping inequality is the halfspace below a chain segment. Ordered
nonincreasing slopes make the piecewise-linear upper boundary the minimum of
these line extensions and the top cap, restricted by the right cap. Every
point satisfying the inequalities is below a chain point (or below the first
horizontal cap), so it is dominated. The reverse inclusion follows because all
chain points satisfy all those inequalities. A singleton reduces to two caps.

The standalone compact verifier checks the chain conditions, reconstructs these
planes itself, and tests every input vertex against their (1+eta)-scaled bounds.
It stores only the m lower-inclusion witness combinations. This proves the same
sandwich without trusting the encoder's hull algorithm. Proof payload size is
O(m) rational records, not O(N+m); their actual rational bit lengths are charged.
It still inspects the original input and uses O(Nm) rational plane evaluations.
The original source is not erased, and no compact-time audit of arbitrary input
is promised.

On the dense fixture, canonical JSON sizes are:

    original input                  35,771 bytes
    reusable compressed payload        399 bytes
    first working certificate       42,642 bytes
    improved compact certificate       657 bytes

Thus the improved payload plus certificate is 1,056 canonical JSON bytes for
this fixture, excluding verifier code and the original source required at audit.
The comparison is not a general optimal-compression benchmark. Both receipts
are retained; the improvement is recorded rather than concealing the first cost.