# Fixed-dimensional uncertainty permits exact disclosure-order selection

19 September 2026. Developing note; first milestone.

The number of senders can grow while the uncertain model family occupies a fixed
number of dimensions. In that setting, exact order selection is polynomial-time
under an explicit rational polytope encoding. This follows by combining R10's
short-prefix theorem with established fixed-variable real-algebraic algorithms;
it is not a newly invented algebraic method.

The [complete theorem](../math/THEOREM.md) specifies the input, strict inequalities,
affine reduction and bit complexity. The polygon executable implements that
decision setting with established backends and returns auditable outputs. Its
success checks retain exact-solver trust, while rejection witnesses are checked
with rational arithmetic alone. A full research synthesis follows the final
independent replay audit; the strategic R08 bridge remains unformalized.
