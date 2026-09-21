# From the disclosure game to its continuation formula

R14. Started September 19; written September 20, 2026.
Formal status: all six modules passed a fresh Lean 4.33.1 build. The
[source-bound audit](../results/lean_full_bridge_2026_09_20.json) covers 119 named
declarations and permits only `propext`, `Classical.choice`, and `Quot.sound`.
No admitted proofs or custom axioms occur in their dependency closures.

## Result and why it matters

The relevant confidence question is whether the product conditions used in
R08–R12 follow from the declared game. Checking those products algebraically would
not answer it. This phase instead formalizes independent Nature draws, feasible
messages, history-dependent strategies, and Bayesian conditioning, then computes
expected payoffs over Nature states and terminal message paths.

The main research question remains unchanged. This is a formal specialization of
standard probability and equilibrium-consistency machinery, not a claim of a new
general equilibrium theorem. Growing-dimension complexity was not investigated.

## Precise bridge statement

There are n senders in a fixed public order. Index by protocol position. Nature
independently draws X_i∈{0,1} with probabilities 0<p_i<1. Sender i acts once,
observes its own bit and the full earlier public transcript, and can authenticate
a report only if X_i=1. A positive type's report probability q_i(h) lies in [0,1].
A zero type must remain silent. The receiver acts only after all senders.

**Belief theorem.** Every feasible behavioral profile has one and only one belief
system obtainable as the limit of Bayesian conditioning along completely mixed
feasible profiles converging to it. At a fixed history, coordinates remain
independent. A reported coordinate equals one, an unvisited coordinate retains
prior p_i, a privately observed coordinate equals its observed value, and a silent
coordinate has probability

    p_i(1−q_i(h_before_i)) / (1−p_i q_i(h_before_i)).

This includes all zero-reach histories. Existence uses a single global strategy
sequence, including receiver perturbations. Uniqueness covers arbitrary relative
rates of convergence, without requiring the perturbations to be equilibria.

For the strategic part assume A,B>0, e≥0, and every p_i<τ=A/(A+B). The receiver's
payoff from C is zero. Its payoff from D is B−e if every bit is one and −A−e
otherwise. A sender's payoff is η_i times the eventual probability of D, minus
k_i if it reports. The intended game has η_i,k_i>0; the payoff identity itself
holds for arbitrary real η_i,k_i.

**Receiver theorem.** At every incomplete terminal transcript, C is uniquely
optimal. At the complete report transcript, D is uniquely optimal if e<B;
every mixture is optimal at e=B; C is uniquely optimal if e>B. These statements
compare expected payoffs against every feasible mixed deviation.

**Continuation theorem.** Suppose 0≤e<B and the receiver acts optimally at each
terminal transcript. For a current positive sender j, at an all-report preceding
history, the report-minus-silence payoff equals

    η_j ∏_{i>j} [p_i q_i(R^{i−1})] − k_j.

After any past silence it equals −k_j. No future sender rationality or pure-play
assumption is required. Positive gain forces reporting, negative gain forces
silence, and zero gain permits any feasible mixture when optimizing this sender's
mixed action. Thus disclosure probabilities must remain in the formula until a
separate backward argument justifies removing them.

## Proof from primitives

1. Define each state's prior mass as a product of Bernoulli masses. Finite
   distributivity proves that masses sum to one. They are nonnegative.
2. For a fixed observed prefix, multiply each visited sender's conditional action
   probability at its full earlier prefix. Multiply by the prior and normalize.
   The likelihood factors by private bit because the transcript has been fixed.
   Conditioning on the current sender's private bit inserts its indicator.
3. Normalize coordinate by coordinate. A silent coordinate's denominator is
   1−pq≥1−p>0. Report factors are cancelled while strategies are fully mixed.
   Continuity gives every limiting posterior. Perturb all behavioral probabilities
   by (q+ε)/(1+2ε), ε=1/(m+1), to obtain existence. Uniqueness of real limits gives
   uniqueness for every other completely mixed convergent sequence.
4. Start the receiver calculation with the finite expectation of its primitive
   payoff. It equals (A+B)Q−A−e, where Q is the all-positive state mass. At an
   incomplete transcript Q≤p_i<τ for a silent coordinate. At complete disclosure
   Q=1. This proves the receiver rule, including off-path histories and the tie.
5. For each Nature state, sum over every terminal transcript extending the past
   and the forced current action. Each future path has its chain-rule product of
   actual action probabilities. Integrate this path expectation against the
   sender's previously derived conditional state distribution.
6. Apply the receiver rule proved in step 4. Only the complete report transcript
   contributes to D. If the current action or any past message is silence, none
   contributes. Otherwise finite distributivity integrates each future bit:
   a positive future type reports with its actual probability q_i, producing
   p_i q_i. Earlier/known coordinates contribute normalized mass one. Subtract
   the report cost. This earns the continuation formula from the original sums.

The proof uses Mathlib's existing finite-sum/product and continuity theorems.
The [source notes](../sources/NOTES.md) identify those borrowed tools and the
sequential-equilibrium definition used in R13.

## Assumption tests and rejected shortcuts

**Dropping the strict prior bound is false.** With two senders, p₁=p₂=1/2,
A=B=1, e=0 and silent behavior q=0, consider the limiting belief at transcript
(S,R). Its all-positive probability is 1/2, so the receiver is indifferent.
Incomplete evidence therefore does not strictly force C at the threshold. The
Lean counterexample uses the same posterior derived by off-path limits.

**Evaluating Bayes division at a zero-reach endpoint is invalid.** A report with
q=0 has zero joint mass and zero conditioning mass. Lean's totalized real division
returns zero for 0/0, whereas its consistent posterior on the reported bit is one.
The zero-denominator expression is not ordinary conditional probability. The
formal theorem cancels at positive-reach approximations before taking the limit.

**Replacing future mixed disclosure by certainty is invalid.** The two-sender
mixed-tie example with future prior 1/2, future reporting probability 1/2,
η₁=1 and k₁=1/4 gives zero first-sender gain. Replacing the future report probability
by one would instead give 1/4. `mixed_tie_gain` evaluates the full state/path payoff
through the proved bridge; R13 separately checks the equilibrium example from
primitive finite enumeration.

These are assumption/interpretation checks, not new counterexamples to R08's
stated theorem. No mathematical conjecture had to be weakened during this phase.

## Computational fidelity evidence

A new exact-rational checker compares the formal definitions with R13's separate
recursive game evaluator. Across 28 designed profiles at n=1,2,3,4, including
reversed orders, pure boundary strategies, history-dependent mixtures and unequal
tremble exponents, it checks:

- 844 posterior distributions against polynomial-tremble limits;
- 4,944 normalized nonnegative continuation kernels;
- 9,888 path expectations against recursive tree evaluation, including arbitrary
  mixed receiver strategies rather than only the optimal complete-report rule;
- 408 primitive sender gains and 204 comparisons with the derived cascade gain.

These are finite computations, not an exhaustive behavioral-profile search and
not the proof for arbitrary n. The Lean proofs provide the latter. Normal and
optimized Python produce identical receipts; the retained
[model-fidelity receipt](../results/model_fidelity_2026_09_20.json) records their
agreement and source identities.

## Exact formal coverage and remaining gaps

The formal sources define the finite game directly; they do not invoke an assumed
posterior law or assume the continuation gain. Receiver optimality is the only
strategic premise of `continuation_bridge`. The observations-to-game adapters and
full-profile perturbation ensure the generic probability lemmas apply to the
actual private/public information sets.

The formal model defines path likelihoods as chain-rule products of feasible
behavioral action probabilities. It proves local action normalization, prior and
posterior normalization, positive completely mixed conditioning masses, and
nonnegative continuation weights. `continuation_weight_tree` additionally identifies those weights with probabilities
generated recursively by the full behavioral tree, and `continuation_weight_sum`
proves their sum is one. No equivalence to an external extensive-game library is
claimed. This bridge should not be mistaken for a proof of every aspect of
sequential equilibrium.

Still **unformalized**:

- a complete assessment and sequential-equilibrium predicate combining consistency
  and every player's sequential rationality;
- backward induction forcing all-report behavior when every strict suffix test
  succeeds, including the exclusion of mixed rescue;
- the largest-blocker strategy construction and its rationality at every node;
- equivalence between the on-path silent target and that assessment;
- both directions of the target-existence theorem and the attained 0-or-B minimum;
- robust families, the R10 Helly/order-selection theorems and adaptive policies.

R13 gives written proofs of the first game's existence arguments. This phase
closes the belief/receiver/continuation bridge only. Proof compilation verifies
the stated formal propositions; independent model review and external kernel
replay remain separate assurance steps. There is no Palomar claim.

## Next attack

The recommended next formal attack is R13's assessment predicate and backward
largest-blocker construction, using this bridge to close both directions of
target existence. Growing-dimension complexity remains the separately agreed
mathematical-discovery frontier for a subsequent goal. No further numerical
frontier is needed before either attack.
