# Gate 3 — the planar logarithm is removable

21 September 2026. Complete written constructive proof; new rational executable
checks supplement it. Not Lean checked. The geometric rate is classical metric
entropy, not claimed as a new discovery.

## Matching theorem and its scope

Fix `0<ell<u<tau<1` rational. For rational convex planar inputs in [ell,u]^2,
all rational order/cost queries, one compressed block with arbitrary exact
independent attachments, and the correctness/completeness contract of Gate 2,

    R*(gamma) = Theta(gamma^(-1/2)).

A uniform rational encoder attains the upper bound, with polynomial computation
in explicit input length and 1/gamma. Its decoded polytope satisfies a rational
domination sandwich. A verifier with the source can check the sandwich in
polynomial time in input length and 1/gamma with **zero additional witness bits**.
Therefore the infimum of total transmitted payload plus certificate bits in
this source-readable model has the same Theta rate. This statement places no
optimality claim on verification/query time, expanded working memory, or
source-free certificates. Source retention is not included in the transmitted
payload, and would add L bits if it must also be stored or sent.

For arbitrary unbounded repetition the finite rate is false; see Gate 2.
The lower bound is audited R15, using a positive concave patch inside this box.
It applies to all encoders, not merely vertex lists. The construction below
proves that “each selected vertex needs log(1/gamma) bits” is not a valid lower
bound on arbitrary codes: multiscale positions and precision can be encoded
jointly. Cardinality and coordinate precision are both charged in the code.

## 1. One scalar curvature sequence represents both coordinates

Extract the nondominated concave NE chain of P, with endpoints v0,v1. A singleton
uses a constant chain. For a nontrivial chain let s be L1 arclength and
t=s/L in [0,1]. Let v(t)=(x(t),y(t)). Then

    y(t)=x(t)+y(0)-x(0)-Lt,
    0<=x'(t)<=L,   x' is nonincreasing,   L<=2(u-ell)<2.

Thus both coordinates are concave and have the same midpoint surplus. For
I_jk=[k 2^-j,(k+1)2^-j], let phi_jk be its unit-height triangular tent and put

    c_jk=x(mid I_jk)-(x(left I_jk)+x(right I_jk))/2 >= 0.

These are rational for rational polygon input. Piecewise-linear interpolation
on the depth-J dyadic grid has the exact identity

    v_J(t)=(1-t)v0+t v1 + (1,1) sum_(j<J,k) c_jk phi_jk(t).

Let mu=-d x' be the nonnegative slope-variation measure, of total mass at most L.
On an interval of length h, its midpoint surplus equals the integral of a
nonnegative triangular kernel bounded by h/4 against mu restricted to that
interval. Hence

    sum_k c_jk <= L 2^-j/4 <= 2^-j.

This also follows directly by summing the before/after mean-slope differences
on disjoint intervals; atoms at endpoints have zero kernel weight. Arbitrarily
sharp corners, horizontal limits and very steep y(x) slopes are covered.
The coordinatewise interpolation remainder is nonnegative and at most
`2*2^-J`, a deliberately loose bound from the coordinate Lipschitz constant 2.

## 2. Quantize at scale-dependent precision

Choose dyadic epsilon=2^-b, b>=1, with epsilon<ell/2. Put

    j0=floor(b/2),   J=b+3,
    a_j=1+|j-j0|,
    delta_j=2^(-b-4-2 ceil(log2 a_j)),
    z_jk=floor(c_jk/delta_j),
    S_j=floor(2^-j/delta_j),  M_j=2^j.

Round the four endpoint coordinates downward to multiples of epsilon/8.
Replace c_jk by delta_j z_jk. The reconstructed polygonal path q(t) is below
the true path v(t) in BOTH coordinates. At a fixed t at most one tent at each
level is nonzero. Since

    sum_(j<J) delta_j
      <= epsilon/16 * (1+2 sum_(a>=2) a^-2)
      < 3 epsilon/16,

endpoint rounding, coefficient rounding and interpolation tail give

    0 <= v_i(t)-q_i(t) < epsilon/8+3epsilon/16+epsilon/4 < epsilon.

Only the coarser bound `sum a^-2<2` is needed for that displayed inequality.
All numbers are dyadic. A common denominator has exponent
`O(b+log b)` before multiplying dyadic tent values; reconstructed coordinates
have O(b+log b) bits as well since J=O(b). No real slopes are transmitted.

Define Q as the convex hull of all depth-J decoded path points. Rounding may
destroy concavity/monotonicity of the PATH; the decoder must take this convex
hull. Every path point is dominated by its true P point, and D(P) is convex,
so D(Q) is contained in D(P). Every P point is dominated by some true chain
point, and q(t) belongs to Q. Therefore

    D(Q) subset D(P) subset (1+eta)D(Q),
    eta=epsilon/(ell-epsilon),
    Delta+(P,Q)<=2 log(1+eta)<=2 eta<=4 epsilon/ell.

Q is positive and below u<tau. Choosing epsilon<=ell gamma/16 gives error at
most gamma/4. In practice take the largest dyadic satisfying this bound and
epsilon<ell/2. The strict margin completeness budget has ample slack.

## 3. Encode identities and amplitudes together

At level j the nonnegative integer sequence z has length M_j and sum at most S_j.
There are exactly `binom(M_j+S_j,M_j)` such sequences, by stars and bars.
Encode its lexicographic or combinatorial rank in

    B_j=ceil(log2 binom(M_j+S_j,M_j))

bits. The decoder knows M_j,S_j from b. This encodes all locations, zero runs and
amplitudes, not just their values conditional on a free frontier identity.
Unused ranks are rejected. Four endpoint integers use O(b) bits. Transmit b
with a self-delimiting integer code of O(log b) bits; all other level lengths
are determined. The decoder is a fixed finite algorithm, not a per-epsilon
nonuniform lookup table. Ranking/unranking weak compositions uses integer
binomial coefficients and has polynomial cost in M_j+S_j and its bit lengths.

Here is the bit estimate, including the quantization overhead. Write
K=epsilon^-1/2 and k=j-j0. Up to absolute constants,

    M_j ~ K 2^k,
    S_j <= C K (1+|k|)^2 2^-k.

Use `log binom(M+S,M)<=min{M log(e(1+S/M)), S log(e(1+M/S))}`.
For k<=0 the first bound is
`O(K 2^k (1+|k|+log(1+|k|)))`.
For k>=0 the second bound is
`O(K (1+k)^3 2^-k)` (monotonicity in S allows using its upper bound).
Both sum to O(K) over all integers k. Rounding up adds only J=O(b) bits.
Consequently total storage is O(epsilon^-1/2)=O(gamma^-1/2).

The expanded grid contains 2^J+1=O(1/epsilon) points. This particular codec
optimizes *bits*, not decoded vertex count or running time. It can subsequently
remove hull redundancies, but no O(epsilon^-1/2) expanded-size claim is needed.

## 4. Verification and enforcement queries

Decode to rational Q, compute its NE hull independently, and check
`D(Q) subset D(P) subset (1+eta)D(Q)` with exact rational arithmetic. In two
dimensions the downward hull is determined by its top/right caps and sloping
edge inequalities, including the singleton case. Test every decoded vertex in
D(P) and every original source vertex in the scaled D(Q). No encoder-provided
frontier, arclength, slope, witness or success flag is trusted. The verifier can
compute both hulls itself. Straight pairwise vertex/plane checks take
`O(Nm)` arithmetic evaluations after hull construction, where m=O(1/epsilon);
bit cost is polynomial in L, 1/epsilon and b. Space for the expansion is charged
to computation, not falsely hidden inside R.

For decisions use the lower family Q and rational outer family (1+eta)Q.
For a fixed order, if the outer margin is <=0 return zero; if the lower margin
is >0 return B; otherwise REFINE. For optimized queries use minima over the
SAME orders and return an outer-success order. The bracket width is <=2 log(1+eta)
for one planar block, even with arbitrary exact attachments (R15). This rule is
sound and complete for |true margin|>=gamma with the chosen error budget.
The expanded upper family is a mathematical margin bound, not an assertion that
probabilities above tau belong to the strategic game; if desired intersect its
downward set with the original known box. Query signs can be decided through
rational polynomial inequalities in suffix products; there is no free exact-log
oracle. Exact real-algebraic decision and order enumeration give a terminating
algorithm. Optimal Tq, especially with many senders, is NOT established here.

## 5. Gate report, failed attacks and remaining work

Strongest result: matching planar total-payload rate in the explicitly
source-readable audit model, with an explicit polynomial-work rational codec.
Failed conjecture: the coordinate-precision logarithm is an information-theoretic
necessity. The multiscale rank code disproves it. Other failed shortcuts: retain
only logged vertices; assume coefficient rounding preserves concavity; claim the
expanded output is as small as the bitstream; call C=0 source-free proof.

Exact evidence is recorded in `experiments/codec_receipt.json`: binary round
trips, exact continuum sandwich checks, degenerate/frontier/corner fixtures,
corruption rejection, and code-length calculations. These finite checks do not
prove the asymptotic theorem. The geometric rate is already supplied abstractly
by Bronshtein's entropy theorem; this proof makes the rational coding and
source-relative assurance explicit. See source notes for the precise comparison.

Remaining gaps: implementation diversity/human proof audit; optimal Tv/Tq;
short certificates under more restrictive verifiers; optimized-only lower
bounds; fine-grained refinement cost. Central question retained, with the
planar storage logarithm closed. Next bounded attack: fixed-dimensional entropy
encoding and enforcement-specific labelled/tree composition, not a new generic
geometric rate claim.
