# Completion audit — general sharpness gate

19 September 2026. Author audit against the explicit active goal. Written proofs
are not proof-assistant checks. The initial state was main `807791b`; the first
published milestone is `5518615` after preserving independently published CI work.

| Explicit requirement | Authoritative evidence inspected | Outcome |
|---|---|---|
| Revalidate the recorded search and common first sender | R10 original source/receipt; R11 producer reads its exact missing-prefix list | Exactly 20, all start with zero-based sender 0 |
| Optimize each minimum log margin over the admissible affine slice | resolve_prefixes.py; numerical points, statuses and residuals in prefix-results.json | All 20 optimized individually; original q, fixed p0, budget and τ preserved |
| Certify rational witnesses exactly | exact.py; every rational point and strict product margin; verify_results.py replay | All 20 pass affine, probability and strict cascade checks |
| Prove obstruction if a prefix cannot be defeated | All 20 have strict witnesses | No unresolved individual case remains; no search failure used as proof |
| Separate numerical optimization from mathematical bounds | DIMENSION_FOUR.md tangent/support/series argument and saved certificates | True supremum enclosed rationally for every prefix; widest gap 4.6197·10^-8 |
| Extract arbitrary-d construction rather than more isolated dimensions | GENERAL_CONSTRUCTION.md full theorem and formulas | Written proof for every d≥0; finite rational H-polytope or explicit finite hull |
| Investigate structured perturbations around AM-GM equality | Record-block deficit construction, mixture with ones, rational ε | Exact quantitative margin εγ/2; no unbounded remainder assumption |
| Prove ACTUAL dimension | Independent dimension-spanning points and matching affine constraints | Dimension exactly d; finite exact rank controls supplement the proof |
| Successful (d+1)-prefix throughout hull | Weighted-AM-GM bound on entire containing affine slice | Written universal proof, favorable ties retained |
| Defeat every shorter candidate prefix | Two-case construction for every length-d prefix, then extension argument | Written all-prefix proof; separate models allowed and retained in logic |
| Parameters may depend on d; keep strategic model fixed | Explicit q_d, τ_d, r_i, A,B,η_i; stable R08 assumptions | Only admissible numerical parameters vary; target/messages/timing/equilibrium unchanged |
| Separate varying payoffs from fixed τ=2/3 | FIXED_THRESHOLD.md quantified statements | General theorem permits τ_d→1; arbitrary-family fixed-τ question remains OPEN |
| Treat construction obstruction only as such | Fixed-q inequality (G), fixed-threshold inequality (H), inherited R08 control | Original ansatz limitations proved; no universal improved bound claimed |
| Keep main question and settled routes unchanged | BRIEF, CURRENT_STATE, manuscript, decision ledger | No reopening of segment hardness, vertex success, unrestricted pairs or adaptation |
| Next algorithmic question is beyond segments; sharpness is not hardness | Manuscript and current-state next attack | Rational-polygon selection recommended; no complexity lower bound |
| Preserve old findings and receipts | Changed-file inspection against baseline | New phase only, plus living ledgers/index/CI; old phase files untouched |
| Separate proof/computation/formal/novelty statuses | VERIFICATION.md R11 row, source notes, experiment scope | Written proof + exact checks + numerical discovery; no Lean/external-kernel/novelty claim |

## Proof audit

The record list has at most m−1 blocks, including terminal m, so one block has
length at least two. The surplus identity W−C≥1 supplies uniform slack after
normalization. At a visited record R, exactly the deficits at labels ≤R have
been removed; a nonrecord label cannot make the remaining raw sum larger. The
artificial terminal record handles both prefixes containing m and prefixes that
never visit it. The nonzero-first case absorbs the entire weighted budget into
the first removed coordinate. Mixing preserves the affine constraint and strict
probability bounds. The explicit ε controls the quadratic Taylor term uniformly
for ALL exponents h≤m+1. Basis-point differences establish actual dimension.
The d=0 case and extension to empty/shorter prefixes are separately stated.

The parameter limitation proofs were checked separately: (G) uses the weighted
deficit budget; (H) uses the strict coordinate cap and the special cost r_{m−1}=q.
Neither hypothesis set is asserted for arbitrary constrained families. R08's
nonuniform τ=2/3 example remains a direct control against overgeneralization.

## Executed evidence

- 20 saved rational witnesses and 20 rigorous margin brackets replayed without
  SciPy/NumPy; four corrupted records rejected.
- 23,115 exhaustive prefix cases for m=2,...,7; 75 larger-m controls through m=100.
- Exact dimension controls through d=9, seven rational log-identity controls,
  99 fixed-threshold arithmetic checks and three preserved R08 singleton controls.
- Source hashes checked for the optimizer/certifier, construction code and original
  input receipt. Numerical discovery and exact replay remain distinct.
- Scoped CI steps added for these programs. This audit does not claim that the
  remote workflow or the unformalized R11 theorem has been Lean checked.

**Completion:** the three gate deliverables are satisfied by individual certified
resolution, an arbitrary-d construction, and an explicit fixed-threshold boundary.
The unresolved arbitrary-family τ=2/3 problem and historical novelty are correctly
separated follow-on questions. They are not used to conceal a missing general
construction or missing shorter-prefix witness in the theorem actually stated.
