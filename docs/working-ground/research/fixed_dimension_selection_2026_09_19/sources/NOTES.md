# Sources and borrowed machinery

Inspected 19 September 2026. Primary author papers and official documentation.
No historical novelty claim follows from this bounded comparison.

1. **Saugata Basu, Algorithms in Real Algebraic Geometry: A Survey (2014)**,
   [author preprint](https://arxiv.org/pdf/1409.1534), §2.5.2, Theorem 2.27,
   especially the integer coefficient bit-size clause on printed p.16. This states
   effective block quantifier elimination from Basu–Pollack–Roy, *Algorithms in
   Real Algebraic Geometry*, Chapter 14. Fixing the number of quantified variables
   makes its operation count and intermediate integer lengths polynomial in the
   remaining explicit polynomial parameters. Our reduction controls those
   parameters before applying the theorem. We do not credit mere decidability
   or arithmetic-operation complexity alone with proving polynomial BIT time.

2. **Nikolaj Bjørner and Leonardo de Moura, Z3 Internals (author draft)**,
   [paper](https://z3prover.github.io/papers/z3internals.html), nonlinear real
   arithmetic/NLSAT discussion. Related original result: Dejan Jovanović and
   Leonardo de Moura, *Solving Non-linear Arithmetic*, IJCAR 2012,
   [DOI](https://doi.org/10.1007/978-3-642-31365-3_27). The executable calls the
   dedicated QF_NRA logic, not a solver for arbitrary nonlinear integer or
   mixed-theory formulas. Z3 is an established backend, not a formal proof kernel
   built by this phase. Version pinned at 4.15.3.0.

3. **Gereon Kremer, Andrew Reynolds, Clark Barrett and Cesare Tinelli (2022),
   Cooperating Techniques for Solving Nonlinear Real Arithmetic in the cvc5 SMT
   Solver**, [author paper](https://theory.stanford.edu/~barrett/pubs/KRB%2B22.pdf),
   §2.1–2.3. Cylindrical coverings and incremental linearization supply a separate
   established method. The proof-generation subsection explicitly distinguishes
   detailed lemmas from covering proof skeletons. Our observed CPC `TRUST` steps
   agree with that limitation; they must not be advertised as external kernel
   verification. We force the covering strategy in the independent checker.

4. **cvc5 1.3.1 official proof documentation**,
   [Proof Production](https://cvc5.github.io/docs/cvc5-1.3.1/proofs/proofs.html).
   Documents the API proof object and CPC export. We enable internal proof checking
   and retain the exported skeleton; no external Ethos/LFSC/CPC replay is claimed.
   [Official theory tutorial](https://cvc5.github.io/tutorials/beginners/theories.html)
   identifies QF_NRA and the exact real-algebraic decision setting. Version pinned
   at 1.3.1. Installed wheel lacks CoCoA support for Lazard evaluation, so experiments
   use its default regular covering projection/lifting, with that implementation
   inside the trusted backend. We did not silently claim a different configuration.

5. **Internal dependencies, not new literature:** R08's game-to-cascade theorem;
   R10's finite-Helly/move-to-front reduction and sharp triangle; R11's general
   sharpness construction and fixed-threshold obstruction. These records retain
   their original evidence status. The side investigation tightens two deductions
   inside R11's ansatz and makes no broader literature claim.

**Closest comparison.** The algorithmic machinery for a fixed-variable
semialgebraic decision is established. This gate contributes a specialization
and an auditable implementation, not a new real-algebraic complexity class or
general optimization theorem. Generic equilibrium-continuity results are not
needed for this finite strict-product decision. Growing dimension, a smaller
trusted checker, and strategic fidelity remain separate questions.
