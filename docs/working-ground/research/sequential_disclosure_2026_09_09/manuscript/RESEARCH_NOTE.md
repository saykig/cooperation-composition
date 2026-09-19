# Cooperation, disclosure timing, and compatible uncertainty

Research investigation, **9 September 2026**.

**Status:** analytical derivations and exact rational computational checks. No
claim of historical novelty, independent human review, formal verification, or
empirical validity.

## Executive finding

The proposed contribution needs narrowing. Minimum payments that make a fixed
signaling scheme obedient are already explicitly characterized in the
persuasion-with-payments literature. Local product restrictions, multi-sender
signaling and sequential disclosure are also established subjects.

Two tempting routes fail in their proposed form:

1. Enlarging a family of information structures that must **all** be tolerated
   cannot lower the minimum robust sanction. Enlarging the institution's
   **choice** of an information structure is a different optimization problem.
2. Independent-sendership restrictions at histories where two senders disclose
   do not, on their own, create an incompatibility in a simultaneous all-silent
   equilibrium: those histories cannot be reached by one sender's unilateral
   deviation.

A more useful direction is sequential hard evidence. In a declared
complementary-evidence game, this phase derives an exact enforcement formula for
any number of senders and any disclosure order. It then constructs a three-sender
example where preserving one shared restriction on uncertain local probabilities
makes zero enforcement sufficient, whereas replacing that restriction by the
same separate local probability ranges raises the robust minimum to one. The
difference survives optimization over every sequential disclosure order.

This is a bounded research result and a clearer candidate research question, not
an established publication gap.

## 1. Literature boundary

The closest literature materially narrows the claim:

- Dughmi et al. already characterize minimum payments supporting a fixed
  information scheme.
- Costly disobedience is already a direct correlated-equilibrium object.
- Multi-sender persuasion already studies correlation, local information and
  decentralized signaling.
- Sequential persuasion and costly multi-sender disclosure already study timing.
- Hard-evidence communication already supplies consistency constructions.

The candidate contribution is therefore **not** that decentralized senders impose
implementability restrictions, nor that sequential communication matters. The
remaining target is an exact robust-enforcement statement when the analyst knows
only a jointly constrained family of local information conditions and one protocol
must work throughout that family.

See [sources/NOTES.md](../sources/NOTES.md).

## 2. Universal robustness is not institutional choice

For a fixed arrangement and an information family \(\mathcal I\), define

\[
E_{\forall}(\mathcal I)
=
\inf\{e\ge0:\text{the arrangement is sustainable for every }q\in\mathcal I\}.
\]

**Proposition 1.** If \(\mathcal I\subseteq\mathcal J\), then

\[
E_{\forall}(\mathcal I)\le E_{\forall}(\mathcal J).
\]

Every fine that works for every model in \(\mathcal J\) works for every model
in its subset. An existential design problem, in which the institution may choose
a structure from a larger menu, is a different problem and can move in the
opposite direction.

## 3. Convex mixtures and fixed obedience

For state \(\omega\), observed message \(m\), information kernel
\(q(m\mid\omega)\), deviation \(d\), and pre-fine deviation gain
\(g_d(\omega,m)\), the obedience condition after \(m\) can be written

\[
\sum_\omega p(\omega)q(m\mid\omega)
[g_d(\omega,m)-e]\le0.
\]

This avoids dividing by a posterior when the message has probability zero.

**Proposition 2.** For fixed target behavior and fixed deviation inequalities,
obedience for every \(q\in\mathcal I\) is equivalent to obedience for every
kernel in the convex hull of \(\mathcal I\); in finite dimensions the closed
convex hull gives the same result.

The reason is linearity in \(q\). This does **not** convexify equilibrium
constraints, authorize state-dependent hidden correlation, or turn an
existential design problem into a universal robustness problem.

## 4. Why the simultaneous all-silent obstruction fails

Consider finite states, finitely many senders, one receiver, deterministic sender
types, finite physically available messages including silence, simultaneous
messages, and a target in which all senders stay silent.

A unilateral sender deviation reaches a history in which that sender sends one
non-silent message while all other senders remain silent. Therefore the target's
sender incentive constraints are determined by **solo-message** histories.
Restrictions on beliefs after two or more simultaneous disclosures are real
probability restrictions, but they do not by themselves add unilateral deviation
constraints at this target.

This rejects the proposed use of a two-sender rank-one joint-message restriction
as the main enforcement obstruction in the simultaneous all-silent model. It does
not reject those restrictions in games where joint messages occur on path, where
communication is sequential, or where coalitions deviate.

## 5. Sequential complementary evidence

### Model

There are \(n\ge2\) independent binary facts \(X_i\), with

\[
P(X_i=1)=p_i\in(0,1).
\]

Sender \(i\) sees only \(X_i\). If \(X_i=1\), the sender may disclose an
authenticated positive certificate at cost \(k_i>0\) or remain silent. If
\(X_i=0\), only silence is available. Sender \(i\) gains \(\eta_i>0\) if
the receiver chooses action \(D\), and zero under target action \(C\), minus
its own disclosure cost.

The receiver obtains \(B>0\) from \(D\) if all facts are positive and
\(-A<0\) otherwise; \(C\) yields zero. A credible fine \(e\ge0\) is charged
when \(D\) is chosen.

Assume

\[
p_i<\frac{A}{A+B}\qquad\text{for every }i.
\]

A sequential protocol \(\pi\) orders the senders. Each sender observes earlier
messages before acting once. We ask for existence of a sequential equilibrium
with complete silence and receiver action \(C\), using favorable tie selection.

### Receiver lemma

After any incomplete positive-certificate history, \(C\) is strictly optimal
at every nonnegative fine. A missing fact has posterior probability at most its
prior, so the probability that all facts are positive remains below the threshold
\(A/(A+B)\). At a complete certificate history, the receiver knows every fact
is positive and chooses \(D\) when \(e<B\), may choose \(C\) at \(e=B\),
and chooses \(C\) for \(e>B\).

### Theorem: exact fine for any order

For sender \(\pi_j\), define the suffix probability

\[
P_j(\pi)=\prod_{\ell>j}p_{\pi_\ell},
\]

with empty product one. Then

\[
E_\pi=
\begin{cases}
B,
& k_{\pi_j}<\eta_{\pi_j}P_j(\pi)
  \text{ for every position }j,\\
0,
& \text{otherwise.}
\end{cases}
\]

**Idea of proof.** Work backward. If every relevant inequality is strict, the
last positive sender strictly prefers to complete the evidence, the preceding
positive sender strictly prefers to continue given the chance later facts are
positive, and so on. The first positive sender then has a profitable initiating
deviation. Strictness also rules out a mixed-strategy rescue.

If at least one inequality fails weakly, choose silence at the first relevant
tie/failure when working backward. That sender blocks completion. Earlier
disclosures then cannot induce \(D\) and only incur positive costs. A zero-fine
silent equilibrium exists.

At fine \(B\), select \(C\) even after complete evidence. Disclosure then has
cost and no benefit, so \(B\) is sufficient whenever zero is not.

### Known-prior order choice

Some sequential order supports zero fine exactly when

\[
\exists i:\quad
\frac{k_i}{\eta_i}\ge\prod_{j\ne i}p_j.
\]

Put such a sender first. Conversely, any sender that blocks later in an order
faces a product over only a subset of the remaining probabilities, which is at
least the product over all other senders.

### Two-sender diagnostic

Let

\[
p_1=p_2=\tfrac12,quad A=2,quad B=1,quad
\eta_1=\eta_2=1,quad k_1=k_2=\tfrac14.
\]

With simultaneous reports, one unilateral certificate leaves one fact unknown,
so the receiver keeps \(C\); reporting only wastes \(1/4\). Fine zero sustains
silence.

With sequential reports, the second positive sender gains \(3/4\) by completing
the evidence. Anticipating this, the first positive sender gains \(1/4\) from
initiating. The minimum fine becomes one.

The information, payoffs, costs and prior are unchanged; only the communication
protocol changes.

## 6. Shared uncertainty can change enforcement after optimizing the order

Now let each actual model still have independent private facts, but let the
analyst be uncertain about the local probabilities. Players know the actual
probability vector. The institution must choose one order and one fine that work
for every admissible vector.

Take three senders, \(A=2\), \(B=1\), \(\eta_i=1\), and

\[
(k_1,k_2,k_3)=
\left(\frac7{50},\frac25,\frac1{10}\right).
\]

Admit the compact family

\[
p_1=\frac{13}{20},\qquad
p_2=\frac{17}{20}-\frac54s,\qquad
p_3=s,
\qquad
\frac15\le s\le\frac{13}{20}.
\]

All probabilities are positive and below \(2/3=A/(A+B)\).

### True shared family

Use order \((1,2,3)\). Sender 3 reports after two positive certificates. Sender
2 would continue exactly when

\[
s>\frac25.
\]

Sender 1 could want to initiate, assuming later positive senders continue, only
when

\[
p_2p_3>\frac7{50}.
\]

But

\[
p_2p_3-\frac7{50}
=
-\frac54
\left(s-\frac7{25}\right)
\left(s-\frac25\right),
\]

which is positive only for

\[
\frac7{25}<s<\frac25.
\]

The condition making sender 1 willing and the condition making sender 2 willing
never hold together. Every admissible model therefore has a blocker, although
the identity of the blocker changes with the model. Fine zero works throughout.

### Separate local ranges

If the shared relation is discarded and only the coordinate ranges are retained,
the outer rectangle admits

\[
(p_1,p_2,p_3)=
\left(\frac{13}{20},\frac35,\frac{13}{20}\right).
\]

At this artificial combination,

\[
\frac7{50}<\frac{39}{100},\qquad
\frac25<\frac{169}{400},\qquad
\frac1{10}<\frac{39}{100}.
\]

The known-prior order criterion then says every sequential order permits a
profitable disclosure cascade. Hence the optimized robust values are exactly

\[
\boxed{
E_{\text{shared}}=0,
\qquad
E_{\text{{separate ranges}}}=1.
}
\]

The outer approximation is conservative rather than unsafe: it demands
unnecessary enforcement because it admits a combination the shared constraint
forbids.

The result also shows that robust deterrence need not come from one universally
blocking sender. Different admissible models can be blocked by different senders
under the same protocol.

## 7. Computational evidence

The phase records 4,802 exact rational checks:

- 960 sequential-fine comparisons;
- 1,824 all-order comparisons;
- 918 shared-family/outer-range checks;
- 900 exact tremble/posterior checks;
- 200 hidden-mixture fixed-obedience checks.

These corroborate the formulas but are not proofs of continuum claims or novelty.
No Lean or other formal verifier was run. See
[experiments/README.md](../experiments/README.md).

## 8. Limits and next target

The broad contribution is not yet novel. The benchmark assumes complementary
evidence, one receiver, independent private bits within each actual model,
positive disclosure costs, a fixed pure target, a uniform credible receiver fine,
players who know the actual model, analyst uncertainty only over local
probabilities, and favorable equilibrium selection.

If simultaneous communication is freely available as an institutional design
option, this benchmark permits zero enforcement, so the model does not yet contain
an information-quality requirement that makes communication unavoidable.

**Next bounded attack:** characterize robust sequential order choice when local
probabilities lie in a genuinely shared uncertainty class. Rectangular families
are solved by their upper corner. For a declared class such as a compact
polytope, seek either:

1. a necessary-and-sufficient condition with a checkable certificate for the
   existence of one order sustaining zero fine across the family; or
2. a complexity result showing why no simple local summary/order rule can do so.

Do not replace the shared uncertainty family by independent coordinate ranges.
Do not claim a novelty gap until the result is compared directly with sequential
hard-evidence and robust mechanism-design literatures.

**Assessment:** this phase earns a clearer negative result about simultaneous
pooling and a positive exact diagnostic for sequential protocol design under
compatible uncertainty. It does not establish a new general information theory
or a publication-ready novelty claim.
