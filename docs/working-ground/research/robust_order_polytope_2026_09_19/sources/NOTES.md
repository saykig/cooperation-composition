# Primary-source comparison — September 19, 2026

This is a targeted audit, not a claim of complete literature coverage. “Read” below
means the specified passage, not necessarily the entire work. URLs and reading
scope are retained; remote PDF bytes are not vendored or claimed to be immutable.

## Results actually used

**Sion (1958), On general minimax theorems**, Theorem 3.4, printed p.174.
[Original paper](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf).
Read the theorem and its hypotheses. Compact convex sets and the concave/linear
integrand in T1 satisfy them. The weighted-blocker alternative is a direct
specialization; the max–min exchange itself is borrowed. The order is fixed during
this exchange, so it does not erase the institutional/common-order quantifier.

**Boyd, Kim, Vandenberghe and Hassibi (2007), A Tutorial on Geometric Programming**,
[author PDF](https://stanford.edu/~boyd/papers/pdf/gp_tutorial.pdf), introductory
monomial definitions and convex transformations. Products/logarithms are standard
optimization machinery. Our concave-log constraints over an arbitrary H-polytope
are directly convex in p; arbitrary signed polytope inequalities need not become
a standard geometric program under a log substitution. T2's tangent proof is
provided explicitly. The full Boyd–Vandenberghe book PDF repeatedly failed to open;
its indexed first-order condition (4.21) was visible, but no full-book reading is
claimed and the proof does not rely on an unchecked quotation.

**Sagraloff and Mehlhorn, Computing Real Roots of Real Polynomials**, arXiv:1308.4088v2,
[primary PDF](https://arxiv.org/pdf/1308.4088v2), §1.1 Theorem 2, PDF p.4.
Read the polynomial bit bound for integer square-free inputs. Clearing denominators
and taking the square-free part of the product of the nonconstant g_j yields a
polynomial-sized root-isolation input in T8. Isolating these roots permits rational
sign-cell sampling. The numerical implementation in this research only handles
the three-sender quadratic case, not that general algorithm.

**Basu (2014), Algorithms in Real Algebraic Geometry: A Survey**,
[author paper](https://arxiv.org/pdf/1409.1534), §2.1 Theorem 2.1.
Read the quantifier-elimination statement and input-complexity distinctions.
The finite semialgebraic phase conclusion in T3 follows from this established
machinery after returning to polynomial product inequalities. This does not give
a practical solver or establish NP membership for arbitrary H-polytopes.

## Close structures that do not automatically solve this question

**Lawler (1973), Optimal Sequencing of a Single Machine Subject to Precedence
Constraints**, [publisher abstract](https://doi.org/10.1287/mnsc.19.5.544).
Only abstract/model scope inspected. It minimizes the maximum nondecreasing
completion cost with known processing times. Our reversed-log scheduling translation
instead seeks a guaranteed deadline violation under joint uncertainty, with
linked processing times/deadlines. Its algorithm and complexity cannot simply be
imported with the objective reversed. The adjacent-exchange proof in T5 is direct.

**Buchheim and Kurtz, Robust Combinatorial Optimization under Convex and Discrete
Cost Uncertainty**, [author survey PDF](https://optimization-online.org/wp-content/uploads/2017/09/6199.pdf),
§2 and §3.1. Read the uncertainty-model and complexity discussion. Uncertainty
representation affects computational difficulty; standard min–max linear-cost
hardness is not a reduction for our min-order/max-model/min-blocker feasibility
query. This literature supplies a comparison framework, not an NP-hardness result
for this benchmark. A proper reduction remains necessary.

**Berendsohn (2025), Optimal Antimatroid Sorting**,
[primary conference paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/LIPIcs.ESA.2025.104/LIPIcs.ESA.2025.104.pdf),
§2, pp.104:3–4. Read the prefix/basic-word definition, monotone precedence systems
and the three-letter obstruction. C3's five successful orders violate that
representation. Its prefix-set argument also rules out ordinary set-system
matroid/greedoid basic words. Richer states are not excluded; applying antimatroid
sorting to these orders without proving the axioms would be unjustified.

**Hellerstein, Kletenik, Liu and Witter, Adaptivity Gaps for the Stochastic Boolean
Function Evaluation Problem**, [author PDF](https://arxiv.org/pdf/2208.03810),
introduction and problem/formula definitions. Their cost is paid to evaluate a
Boolean function of independent bits; our reports are strategic. This is useful
machinery and a warning that multiple successful branches can support adaptation,
not a theorem about our game. T6 proves the narrower single-AND-path equivalence.

**Barlow and Proschan, Mathematical Theory of Reliability**, chapter 6,
[publisher chapter summary](https://doi.org/10.1137/1.9781611971194.ch6).
Only the series-system optimization scope was inspected. Suffix products are
series reliability quantities. Independent uniform coupling directly proves our
coordinatewise monotonicity; reliability terminology adds no missing equilibrium
argument. Generic network threshold cascades are not being assumed equivalent
to this backward-induction chain.

## Direct strategic-literature boundary

**Kartik, Lee and Suen, Multi-Sender Disclosure with Costs**,
[January 2026 author version](https://arxiv.org/html/2601.10048v1), §5.2 Proposition 5.
Read the sequential-reporting extension and comparative statics. It already treats
how a later informed sender changes the earlier sender's disclosure threshold.
Our query instead holds an arrangement fixed and demands one order for an entire
jointly constrained parameter family. We do not claim that disclosure cascades,
sequential timing, or costly reporting are new.

**Dughmi, Niazadeh, Psomas and Weinberg, Persuasion and Incentives Through the Lens
of Duality**, [author PDF](https://arxiv.org/pdf/1909.10584).
Read introductory model and payments/duality scope; R08's fuller comparison is
retained. This is prior art for information and incentive optimization, not a
source for the specific AND-certificate robust-order theorem. No payment novelty
claim is made.

## What may remain

The useful package here is a precise translation: common robust disclosure orders
admit weighted log-product certificates; local projection loss has a sharp n−1
versus n−2 boundary; and deterministic adaptation collapses in the AND benchmark.
The mathematics behind each component is elementary or established. A publication
priority claim for this combination is unestablished. The unsolved selection
complexity, especially on rational segments, is a narrower candidate paper question.
Existing literature has not been shown to settle it, and absence of a found match
is not evidence of novelty.
