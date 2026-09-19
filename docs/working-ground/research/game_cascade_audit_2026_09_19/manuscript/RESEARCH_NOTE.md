# R08 survives an independent strategic audit

19 September 2026. Complete written audit with reproducible exact checks.
No new Lean proof, independent human review or historical novelty claim.

The original all-silent existence criterion and the minimum-fine result survive
reconstruction from the extensive game's primitives. The key missing detail was
not the backward algebra but the beliefs at zero-probability histories. The
[complete derivation](../math/AUDIT.md) now proves that every behavioral profile
has a unique consistent belief system, derives receiver behavior and full mixed
continuation incentives, and only then obtains the original suffix-product test.

The independent checker enumerates states, message paths and information-set
deviations. Exact polynomial trembles handle off-path beliefs. Exhaustive pure
plans and arbitrary-mixed exact feasibility agree with the theorem on the declared
two-, three- and selected four-sender cases. These are new checks, not a replay
claim for the unavailable historical R08 executable.

The existence quantifier matters: at a sender tie, a silent equilibrium can
coexist with disclosing equilibria. An exact two-sender mixed example is supplied.
This refutes a stronger uniqueness interpretation but does not correct R08's
actual existential statement. R09–R12 need no algebraic changes; their strategic
interpretations retain the original assumptions. See the
[dependency audit](../IMPLICATIONS.md) and [completion audit](../AUDIT.md).

## Exact theorem and scope

Nature draws n≥2 independent Bernoulli bits with 0<p_i<τ=A/(A+B), A,B>0. Each
sender sees only its own bit and earlier public messages and acts once in fixed
order π. Type zero can only be silent; type one can pay k_i>0 for an authenticated
positive certificate. Sender reward is η_i>0 when the receiver chooses D, minus
its own report cost. The receiver acts after all messages, obtaining B−e from D
if every bit is positive and −A−e otherwise; C gives zero. The fine is paid by
the receiver. Actual p is known to players; family uncertainty is institutional.

The target is complete silence followed by C ON PATH, permitting credible
off-path continuation reports. Under sequential equilibrium with favorable ties,
the feasible-fine set is exactly

    [0,∞) if some j has k_{π_j} ≥ η_{π_j}∏_{ℓ>j}p_{π_ℓ};
    [B,∞) if every such inequality is strictly reversed.

Empty products equal one. This is an arbitrary-n written theorem, not an inference
from finite tests. The minimum B is attained because C is an allowed best reply
at the complete-certificate receiver tie.

## Why the independent derivation works

Condition on a fixed transcript. A sender's message likelihood depends on its
own bit and the earlier messages, which are already fixed. Multiplication by the
independent prior therefore separates across bits. A reported bit is certainly
positive. A silent sender's bit has posterior

    p_i(1−q_i)/(1−p_i q_i) ≤ p_i,

where q_i is its positive type's reporting probability at the observed history.
An unvisited bit retains its prior. The denominators are bounded below by 1−p_i>0,
so the formula extends continuously even when a previous report has zero equilibrium
probability. Every behavioral profile has exactly one consistent belief system;
an explicit fully mixed sequence realizes it, independently of tremble speeds.
The standard consistency definition is documented in the
[author-hosted text, Chapter 12](https://faculty.econ.ucdavis.edu/faculty/bonanno/PDF/GT_book.pdf).

At any incomplete terminal transcript, a missing bit has posterior below τ. Hence
C is strictly optimal. Below B the receiver strictly chooses D only at the complete
transcript. After any silence, further reports therefore waste their positive costs.

At an all-report prefix, let a_j be the current positive type's disclosure
probability. Full state/path enumeration gives the report-minus-silence gain

    η_{π_j}∏_{ℓ>j}(p_{π_ℓ}a_ℓ)−k_{π_j}.

The endogenous a_ℓ cannot be omitted at the outset. If every original inequality
is strict, backward induction forces a_n=1, then all preceding a_j=1. The first
positive sender reports, ruling out the target even with arbitrary mixing. If a
weak failure exists, choose its rightmost position as the blocker, choose reporting
at later all-report histories, and silence earlier and after any past silence.
Every information-set action is optimal; the explicit beliefs prove consistency.
At B, receiver C everywhere makes silence strictly optimal for every sender.

## Exact warning about ties

Take p₁=p₂=1/2, A=2, B=1, η₁=η₂=1, k₁=1/4, k₂=1 and e=0. After a first report,
the second positive sender is indifferent and can report with probability 1/2.
The first sender then has gain (1/2)(1/2)−1/4=0. Its report probability can be 0
or 1 in sequential equilibrium. Thus both silent and disclosing equilibria exist.
The complete beliefs and strategies are checked, not only these two arithmetic
equalities. This is a minimal n=2 counterexample within R08's scope to the stronger
all-equilibria claim, not a correction to R08's existence theorem.

## Evidence and assurance limits

The rational checker enumerates Nature states, complete message paths and all
information-set deviations. Polynomial trembles give exact Bayesian limits.
Pure enumeration includes every off-path sender plan and every receiver tie
best reply. A separate real-algebraic encoding allows arbitrary probabilities at
all sender and receiver information sets. It uses consistent-belief weights but
inserts no cascade formula. Only the comparison function uses R08's formula.

The retained run checks 3,324 complete pure profiles, 139 arbitrary-mixed existence
queries, 142 constructed assessments and 312 information-set beliefs. It includes
two/three senders, five selected four-sender games, all orders at four shared-family
values, exact ties and fines just below/at/above B. Normal and optimized Python
give identical mathematical receipts. About 16 seconds is a fixture timing, not
a scalability result. No probability grid or tolerance decides existence.

Z3 mixed-query answers retain backend trust; the general written proof does not
depend on them. No external proof kernel or Lean checker verifies the full game.
The historical R08 4,802-check receipt remains intact and its unavailable original
executable is not falsely described as replayed. These are new independent checks.

Keep the main research question unchanged. The next confidence step is formalizing
the unique-belief lemma and continuation bridge, followed by the exact target-
existence statement. Formalizing suffix algebra alone would not establish the
strategic bridge. No growing-dimension complexity work was started in this gate.
