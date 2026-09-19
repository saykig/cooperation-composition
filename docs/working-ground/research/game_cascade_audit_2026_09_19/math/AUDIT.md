# Independent audit of the sequential game

19 September 2026. Complete written derivation from primitives; not a Lean proof.
The suffix-product formula is the conclusion to be tested, not an assumption.

## 1. Exact game and equilibrium requirement

Nature draws x∈{0,1}^n with probability ∏_i p_i^{x_i}(1−p_i)^{1−x_i}.
Assume n≥2, independent coordinates, 0<p_i<τ=A/(A+B)<1, A,B>0,
k_i,η_i>0 and fine e≥0. The executable also treats n=1 as an explicitly labeled
boundary extension. All primitives and the actual vector p are common knowledge
among the players. Uncertainty about p belongs to the institution/analyst only.

A fixed publicly known permutation π gives the order. At position j, sender i=π_j
observes its own x_i and the ENTIRE public earlier transcript h∈{S,R}^{j−1}.
It has no other private signal and acts once. Type zero has only S. Type one can
choose S or authenticated R, paying k_i only for R. The receiver observes the
whole transcript after all n opportunities and chooses C or D. Its payoff is 0
under C and B−e under D if every x_i=1, otherwise −A−e. Sender i's payoff is
η_i 1_{D}−k_i 1_{R_i}. The fine is paid by the receiver; it is not deducted from
the sender reward. There is no later recall, negative certificate, receiver
intermediate action, shared random device, coalition or unobserved extra signal.

Write q_j(h)∈[0,1] for type-one disclosure probability and ρ(h)∈[0,1] for the
receiver's probability of D. Type-zero silence is compulsory, not an arbitrarily
chosen zero-probability action. Behavioral strategies are sufficient here: every
player acts at most once, remembers its type/history, and has perfect recall.

An assessment is a behavioral profile and beliefs over Nature states at every
information set. It is a **sequential equilibrium** if every action used is a best
reply at that information set and beliefs are limits of Bayes beliefs of completely
mixed feasible behavior profiles converging to the profile. The perturbing profiles
need NOT themselves be equilibria. Receiver actions are perturbed as well; that
does not affect beliefs at earlier nodes or at its own decision.

The target means S^n followed by C with probability one under the equilibrium
and full-support prior. Thus q_j(S^{j−1})=0 for every j and ρ(S^n)=0. It does
**not** require silence at every off-path information set. R08's own continuation
argument already uses that interpretation. Favorable ties mean existence of a
best-reply selection supporting the target, not a rule forcing every equilibrium
to choose silence.

## 2. Beliefs, including all zero-probability histories

For a completely mixed feasible profile, the likelihood of a fixed prefix h is

    Pr(h|x)=∏_{j≤|h|} L_j(x_{π_j};h_{<j}),

where at an R entry, L_j(1)=q_j(h_{<j}), L_j(0)=0; at S,
L_j(1)=1−q_j(h_{<j}), L_j(0)=1. Once h is fixed, each factor depends on only one
private bit. Later observed actions may depend on h, but h is already conditioned
on; they do not restore a dependence on an earlier hidden bit.

Multiplication by the independent prior therefore gives independent posterior
coordinates. A reported bit is certainly one. A silent past bit has posterior

    b_i(h)=p_i(1−q_j(h_{<j}))/(1−p_i q_j(h_{<j})).          (1)

An unvisited bit retains prior p_i. At sender i's information set additionally
condition on its observed x_i; the other factors are unchanged. Formula (1)
is derived from message likelihoods, not from continuation incentives.

Every denominator is ≥1−p_i>0, so this posterior formula extends continuously to
every behavioral profile, including q_j=0 at reported histories. Those zero
report-probability factors cancel from Bayes' rule before taking limits.
Consequently **every profile has exactly one consistent belief system** in this
game. Different relative tremble speeds give the same limiting beliefs.

Existence is explicit: replace each positive-type q by ε+(1−2ε)q for 0<ε<1/2,
and each receiver ρ similarly. Every feasible information set then has positive
probability because Nature has full support and type zero never reports. Bayes
beliefs converge to (1). More general powers ε^{a(h)} yield the same limit.
Uniqueness follows because (1) holds along ANY completely mixed convergent
sequence and its denominators stay bounded away from zero.

This is the missing detailed justification behind R08's receiver lemma. It would
not follow merely from “hard evidence” if bits were correlated or a sender had
additional private information. No such extension is used here.

## 3. Receiver best replies

From (1), 0≤b_i(h)≤p_i. At any incomplete TERMINAL transcript at least one sender
was silent, so the posterior probability Q(h) that all bits are one satisfies
Q(h)≤p_i<τ for such a sender. The receiver's D-minus-C payoff is

    (A+B)Q(h)−A−e < 0.

Thus C is strictly optimal there in every consistent assessment at every e≥0.
At the complete transcript R^n, Q=1. D is uniquely optimal for e<B; C and D are
both optimal at e=B; C is uniquely optimal for e>B. This argument covers off-path
transcripts too and uses no sender incentive formula.

## 4. Derive continuation incentives from the tree

First suppose 0≤e<B. If any earlier sender has already used S, no future action
can produce the complete transcript. The receiver will choose C at every leaf,
so R costs k_i and gives no benefit. Every positive type strictly chooses S at
each such information set.

Only the chain of histories R^{j−1} remains. Put a_j=q_j(R^{j−1}). At such a
history, all earlier bits are known to be one, and all unvisited bits still have
their independent priors. If the current positive type chooses S, the eventual
receiver action is C with certainty. If it chooses R, the probability of D is
obtained by enumerating future types and message paths: only the path on which
every future type is one AND every future sender reports can end in D. Hence

    U_j(R)−U_j(S)=η_{π_j} ∏_{ℓ>j}(p_{π_ℓ}a_ℓ)−k_{π_j}.    (2)

This is where products first arise in the derivation. Type probabilities and
continuation disclosure probabilities both appear. It would be invalid to assume
a_ℓ=1 before proving the relevant continuation incentives.

Sequential rationality requires a_j=1 for a positive difference, a_j=0 for a
negative difference, and permits any a_j∈[0,1] for equality. Together with the
unique beliefs, receiver rule and strict silence after a past silence, these
conditions characterize ALL sequential equilibria below B. Each player acts
only once, so checking the two actions at its information set already checks
every available continuation strategy for that player; no unproved one-shot
deviation principle is needed.

## 5. Both directions of the all-silent characterization

Define T_j=∏_{ℓ>j}p_{π_ℓ}, with T_n=1, only now, after deriving (2).

**Necessity / no mixed rescue.** Suppose k_{π_j}<η_{π_j}T_j at every position.
At j=n, (2) is η_{π_n}−k_{π_n}>0, forcing a_n=1 in every sequential equilibrium.
Induct backwards. Once every later a_ℓ=1, the current difference equals
η_{π_j}T_j−k_{π_j}>0, forcing a_j=1. In particular a_1=1. The first sender has
positive type with positive probability, so the target is impossible. This
excludes all mixed strategies, not only enumerated pure plans.

**Sufficiency / consistent target construction.** Suppose at least one weak
failure k_{π_j}≥η_{π_j}T_j exists. Choose its largest position b. Set a_j=1 for
j>b and a_j=0 for j≤b. At b, (2) is nonpositive; choosing silence is optimal,
including equality. At j<b a_b=0 makes completion impossible, so disclosure
strictly loses k_{π_j}>0. At j>b all later tests are strict by definition of b,
so disclosure is optimal. At all histories containing a past S choose S. Let
the receiver choose D only at R^n and C otherwise. These strategies are optimal
at EVERY information set, and Section 2 supplies their unique consistent beliefs
via an explicit fully mixed sequence. They form a sequential equilibrium with
the target, not just an on-path Nash equilibrium or an unconstrained PBE. ∎

**Audited theorem.** For every fixed order and every 0≤e<B, a target sequential
equilibrium exists iff some position has k_{π_j}≥η_{π_j}T_j. Thus the target
existence answer is identical at every sub-B fine. The theorem is existential:
when it succeeds, OTHER sequential equilibria may disclose, especially at ties.

## 6. Enforcement at and above B

At e=B choose C at every receiver information set, including R^n. Every sender
strictly prefers S at every information set since k_i>0. Section 2 again supplies
consistent beliefs. For e>B the same profile works with the receiver strictly
preferring C everywhere. Therefore the feasible-fine set is exactly

    [0,∞) if some k_{π_j}≥η_{π_j}T_j,
    [B,∞) otherwise.

The minimum is attained and equals 0 or B. This is not merely a numerical
frontier or an infimum approached as e↑B. It uses receiver favorable tie selection
at B and sender favorable ties at weak blockers. Under a different refinement or
mandatory tie rule, this conclusion must be rederived rather than transferred.

## 7. A sharp warning about the equilibrium quantifier

Take n=2, p₁=p₂=1/2, A=2, B=1, η₁=η₂=1, k₁=1/4, k₂=1, order (1,2), e=0.
At history R the second positive sender is indifferent. Set its disclosure
probability a₂=1/2. Equation (2), independently reproduced by full state/path
enumeration, gives first-sender gain (1/2)(1/2)−1/4=0. Thus a₁=0 and a₁=1
both fit sequential equilibria, with silence after any past silence. The first
is a silent-target equilibrium; the second has disclosure with positive probability.

This is an exact counterexample to the stronger, false statement “a weak blocker
makes every sequential equilibrium silent.” It is NOT a counterexample to R08's
existence theorem. The audit preserves that theorem and supplies the missing
belief/continuation proof. A mixed continuation at a tie is legitimate and cannot
be dismissed by a pure-profile search.

## 8. Consequences and residual assurance limits

R09–R12's algebraic product sets, Helly reduction, sharpness examples and exact
selectors remain unchanged. Their strategic interpretation as minimum receiver
enforcement now has an explicit independent derivation under precisely R08's
assumptions. Robustness still means one order/fine for all p, with a possibly
different sequential equilibrium for each known actual p. No common strategy
profile across all models is required or proved.

The proof is complete as written, but informal: no claim of independent human
review or full Lean verification. The checker uses state/path enumeration,
polynomial tremble limits and arbitrary mixed equilibrium constraints; finite
tests cannot prove the arbitrary-n theorem. The novel scope is an audit, not a
new solution concept or a claim of publication novelty. Private correlations,
zero costs, p_i≥τ, additional private observations, coalition deviations and
changed equilibrium selection remain outside the theorem.
