# Formal model and statement map

R14, started September 19; updated September 20, 2026.
The complete source set passed a fresh build and all 119 named declarations
passed the standard-axiom audit. Exact identities are in the receipts and ledger.

## Game represented

Positions are `Fin n`. An arbitrary fixed public order is represented by assigning
its sender's prior and payoff parameters to each position; the model does not
optimize or endogenize the order. Nature draws the full Boolean state with mass
`nature p x = ∏ i, bern (p i) (x i)`. Its nonnegativity and normalization are proved.
The prior is independent, with every coordinate strictly between zero and one.

`Hist n` is a Boolean message list of length at most n. `Info n` has length less
than n: its length identifies the current sender. `Strategy n` assigns a positive
type's report probability to every such full public history. A zero type has only
silence. Feasibility is the closed interval [0,1]; full mixing is (0,1) for each
positive-type decision. No extraneous private signals or correlated types appear.

A receiver strategy assigns its D probability to each complete transcript.
Its choice occurs after all messages and so cannot affect any conditioning
likelihood. `receiver_perturbation` provides fully mixed receiver approximations
indexed by the same natural numbers as the sender perturbations.

## Bayesian conditioning: Beliefs and Transcripts

`prefixLikelihood` multiplies the primitive conditional action probabilities,
using the observed preceding prefix at each visited sender. `transcriptBayes`
normalizes the independent state mass times this likelihood. `senderBayes`
additionally conditions on the current sender's own observed Boolean bit.

`bayes_factorization` is an equality with this normalized joint distribution,
under a full-support prior and fully mixed behavior. `posterior` is initially a
candidate formula, not an assumed Bayesian or equilibrium belief. The equality
proves its interpretation. For a coordinate it is:

- its prior if unvisited;
- one after an authenticated report;
- p(1−q)/(1−pq) after silence;
- its observed value when privately known.

`silent_den_pos` proves the denominator remains positive even at boundary
strategies. `posterior_tendsto` and `bayes_tendsto` therefore cover arbitrary
convergent sequences of fully mixed behavior, without restrictions on relative
tremble speeds. A transcript may have probability zero at the limiting strategy.
The theorem concerns the limit of Bayes conditioning, not division by that zero
probability at the endpoint.

`global_consistency_exists` uses one sequence of whole history-dependent sender
strategies for all public and private histories simultaneously. The perturbation
is q ↦ (q+ε)/(1+2ε), ε=1/(m+1). `global_consistency_unique` proves that any limiting
belief arrays from any such sequence equal the displayed formulas. Normalization
and nonnegativity are separate theorems. Receiver behavior can be perturbed at the
same indices, so full feasible-profile consistency does not require equilibrium
play by the perturbations.

## Receiver and continuation

`receiverGain` starts with the finite expectation of the primitive D payoff:
B−e in the all-positive state, −A−e otherwise. The C payoff is zero. Its expression
(A+B)Q−A−e is a theorem, not the definition of the expected payoff.

For A,B>0, e≥0, and every p_i<A/(A+B), an incomplete transcript has a silent
coordinate. Its posterior is at most p_i, and the all-positive state probability
is at most that coordinate. Complete transcripts reveal the all-positive state.
Best replies must be established by comparison with every feasible mixed action.

`terminal_bestReply_below` derives the unique receiver strategy from comparisons
with all feasible mixed deviations. The boundary and above-B complete-history
best replies are also proved.

The continuation calculation sums over all terminal transcripts, multiplying each
future sender's primitive action probability at its own full preceding history.
It then integrates over the current sender's conditional distribution of Nature.
The current forced action is evaluated only for the positive private type in
`senderPayoff`; zero-type states have conditional mass zero. The helper kernel
is defined on all Boolean states, but this extension does not give the zero type
a new feasible action.
Only applying the receiver's derived below-B rule eliminates all but the complete
report path. A separate finite distributivity calculation integrates the future
bits and earns the factors p_i q_i. The gain is not defined as a suffix product.

`continuation_bridge` combines the derived receiver rule with this actual payoff
calculation. It assumes receiver optimality, not a suffix condition. The
`sender_bestReply_gain` and sign/tie lemmas handle all mixed sender deviations.

`Kernel.lean` defines a recursive binary behavioral tree separately. It proves
its normalization, unrolls it to a product, and identifies that product with the
`continuationWeight` used in the payoff calculation. The actual continuation
kernel therefore has nonnegative weights summing to one. `Bridge.lean` also
combines sender and receiver perturbations into one full-profile existence theorem,
proves positivity of actual public/private conditioning masses, and checks three
small assumption/interpretation examples.

## Explicit boundary of this goal

The desired bridge does not itself constitute a formalization of the full R08
existence theorem. Still to be formalized after this bridge: a complete assessment
and sequential-equilibrium predicate; the backward-induction no-mixed-rescue
argument; the largest-blocker strategy construction and its rationality at every
information set; the on-path target equivalence; and the attained minimum-fine
classification 0 or B. R13 contains written proofs of these statements.

No robustness-over-uncertainty theorem, Helly reduction, order selector,
adaptive-policy theorem, growing-dimension complexity result, correlated-prior
extension, refinement beyond consistency/sequential rationality, or publication
novelty claim is established by these Lean files.
