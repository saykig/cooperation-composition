# Sources, dependence and novelty boundary

Inspected 19 September 2026. No claim of historical priority or independent review.

1. **Finite Helly theorem / Radon proof.** Eduard Helly, *Über Mengen konvexer
   Körper mit gemeinschaftlichen Punkten*, Jahresbericht der Deutschen
   Mathematiker-Vereinigung 32 (1923), 175–176, is the historical attribution;
   its original scan was not inspected. The [University of Toronto mathematical
   notes](https://www.comm.utoronto.ca/~frank/notes/caratheodory.pdf) give the theorem
   and affine-dependence/Radon argument; their four-page PDF was inspected. Our
   proof reproduces the finite convex-set argument, so strict cascade sets do not
   require a compact-set version. The application is to sets INSIDE parameter
   space, and the affine dimension of that space matters.

2. **Sagraloff and Mehlhorn, *Computing Real Roots of Real Polynomials*,
   arXiv:1308.4088v2.** [Author paper](https://arxiv.org/pdf/1308.4088v2), §1.1,
   especially Theorem 2 on square-free integer inputs. The abstract, algorithm
   scope and bit-complexity statement were inspected again. Polynomial degree and
   coefficient size control root isolation; rational inputs reduce to integer
   polynomials after denominator clearing. We borrow that machinery to prove
   polynomial-bit segment selection. The local executable implements elementary
   Sturm subdivision, NOT their ANewDsc algorithm. Its elapsed time is not evidence
   that it attains their complexity bound.

3. **Pébay, Rojas and Thompson, *Sturm's Theorem with Endpoints*,
   arXiv:2208.07904 (2022).** [Author paper](https://arxiv.org/pdf/2208.07904),
   Theorem 1.2 and the proof in §§1–2 inspected. The theorem counts distinct roots
   by a difference of sign variations, with attention to endpoint multiplicities.
   Our implementation takes the square-free part and strips roots at 0 and 1;
   every remaining bracket endpoint is a checked nonroot. Positive rescaling of
   sequence terms preserves the Sturm sign properties. This supports the exact
   certificate checker; no floating-point root estimates are used.

4. **Strategic and robust-optimization comparisons are inherited, not restarted.**
   See [R09's inspected-source audit](../../robust_order_polytope_2026_09_19/sources/NOTES.md)
   and [R08's literature correction](../../sequential_disclosure_2026_09_09/sources/NOTES.md).
   Sion explains the earlier weighted-log alternative. Helly now limits how many
   cascade inequalities an empty-intersection certificate needs; monotonicity of
   suffix products translates that geometric certificate into a protocol prefix.
   None of this establishes new minimax, Helly, root-isolation, hard-evidence or
   robust-optimization theory. Ordinary scheduling hardness cannot override the
   polynomial segment algorithm, and was never a valid imported lower bound.

**What may remain distinct:** the combination of the specific sequential-game
criterion, order-preserving move-to-front lemma, exact certificate-producing
selector, and sharp short-prefix examples. Priority for that combination remains
unresolved. A focused search in robust sequencing / certificate complexity would
be needed before claiming novelty. The central question is unchanged; this phase
settles its rational-segment order-selection subproblem.
