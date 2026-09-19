# Current state — R11

19 September 2026. Main question and R08 game/equilibrium concept unchanged.

| Claim/artifact | Evidence and standing |
|---|---|
| All 20 missing dimension-four prefixes can be defeated at original parameters | Exact rational witnesses; numerical optimization used only to locate them |
| Individual maximum-minimum-log-margin brackets | Exact tangent/linear-support/log-series certificates; largest gap 4.6197·10^-8 |
| For every d, some admissible game/family needs exactly d+1 prefix senders | Complete written proof with explicit rational parameters and witnesses |
| Actual dimension and all shorter prefixes | Written affine-rank and extension arguments; finite exact falsification checks |
| Fixed q=4/5 cannot make the uniform-AM-GM ansatz sharp for all d | Written singleton-blocker obstruction for m≥11 |
| Any fixed τ<1 eventually blocks this ansatz, regardless of q | Written bound; at τ≤2/3 the obstruction holds for every m≥2 |
| All-d sharpness in arbitrary families with fixed τ=2/3 | OPEN; neither proved nor disproved by the ansatz obstruction |
| Software checks | 23,115 exhaustive prefix cases and 75 larger-m controls; all passed exact inequalities |
| Formal proof / independent kernel replay | NOT performed; shared Python arithmetic is not an independent trusted kernel |
| Historical novelty | Unresolved; no new AM-GM, Helly or optimization theorem claimed |
| Computational hardness | Not established or implied |

**Gate outcome:** a general construction AND proved limitations of the original
construction. No additional isolated dimension is being used as a substitute for
the arbitrary-d proof. The main question remains unchanged.

**Next algorithmic attack:** exact common-order selection on rational polygons
(affine dimension two). R10 bounds the candidate prefix length by three, so the
remaining task is an exact multivariate strict-feasibility/certificate method,
with bit complexity separated from numerical optimization. Do not infer hardness
from the prefix lower bound. The fixed-threshold question is a distinct side question.
