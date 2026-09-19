# T8: a sharper exact algorithm for one-parameter polytopes

Let P={a+t(b−a):0≤t≤1}, with positive rational endpoints below τ and positive
rational r_i. The sender count n is part of the input. For a supplied order define

    g_j(t)=product_{l>j}(a_{π_l}+t(b_{π_l}−a_{π_l}))−r_{π_j}.

These are rational univariate polynomials of degree at most n−j. The total degree
is at most n(n−1)/2. Their expanded coefficient bit lengths are polynomial in the
input size: multiply n linear rational factors using polynomial arithmetic.

**Theorem.** Whether a supplied order is robustly zero-fine on this segment can
be decided in polynomial bit time by exact univariate sign determination.
Consequently existence of a robust zero-fine order on a rational segment is in NP.

Proof. Reject cascade feasibility immediately if a g_j is identically zero or a
constant nonpositive polynomial. Otherwise isolate the real roots of the nonconstant
polynomials in [0,1], using standard exact polynomial-time rational-polynomial
root/sign algorithms, and merge their ordered root decomposition. Between successive
roots every sign is constant. Test one rational sample per open cell. A cascade
exists iff all g_j are positive in one of those cells. At a root some nonconstant
g_j is zero and strictness fails; at a strictly feasible endpoint continuity gives
a feasible neighboring open cell. Constant-only instances are checked directly.
For a concrete implementation, take the square-free part of the product of all
nonconstant g_j after clearing denominators. Polynomial gcd and square-free
preprocessing handle repeated/shared roots; its degree and coefficient bit length
remain polynomial. There are O(n²) roots/cells counting total degree. Standard univariate root isolation
and sign comparison are polynomial in degree and coefficient bit length. Guessing
an order takes polynomial space in the certificate and verifying it as above is
polynomial time, proving NP membership. ∎

This is not an NP-hardness or NP-completeness result, and not a polynomial-time
algorithm for finding an order. The new executable handles the n=3 quadratic
special case with rational arithmetic; it does NOT implement the general algebraic
root-isolation algorithm. The latter is a proved reduction to existing algorithms.

For arbitrary rational H-polytopes the fixed-order convex formulation remains
available, but exact boundary and bit-complexity questions are not settled by
numerical convex optimization. General real certificates in T2 are not automatically
NP certificates. These distinctions prevent an unsupported complexity conclusion.

## Quantifier control: modelwise choice is still different

For two senders let r=(2/5,3/10) and P be the segment p1+p2=7/10 with p1∈[1/10,3/5].
Every p admits a zero-fine order: either p2≤2/5 or p1≤3/10. However order (1,2)
fails at (1/10,3/5), while order (2,1) fails at (3/5,1/10). No common order works.
This is a diagnostic of the already-known quantifier boundary, not a new principle.

The minimax exchange in T1 is between a fixed order's constraint weights and p;
it never exchanges institutionally choosing the order with nature choosing p.
Stable score dominance in T5 is an extra condition that legitimately collapses
that distinction in a special class.
