"""Rational affine reduction and convex hulls in actual dimension at most two."""
from fractions import Fraction as F
from itertools import combinations


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (str, int, F)):
        raise ValueError('Use integer or rational-string input, never floats')
    return F(x)


def solve_columns(columns, target):
    """Unique coefficients, or None if inconsistent/dependent; exact elimination."""
    k = len(columns)
    if not k:
        return [] if not any(target) else None
    a = [[c[i] for c in columns] + [v] for i, v in enumerate(target)]
    row = 0
    for j in range(k):
        pivot = next((i for i in range(row, len(a)) if a[i][j]), None)
        if pivot is None:
            return None
        a[row], a[pivot] = a[pivot], a[row]
        t = a[row][j]
        a[row] = [x / t for x in a[row]]
        for i in range(len(a)):
            if i != row:
                t = a[i][j]
                a[i] = [x - t*y for x, y in zip(a[i], a[row])]
        row += 1
    if any(not any(v[:-1]) and v[-1] for v in a):
        return None
    return [a[i][-1] for i in range(k)]


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


class Domain:
    def __init__(self, data):
        self.r = list(map(rational, data['r']))
        self.n = len(self.r)
        self.tau = rational(data['tau'])
        self.v = [list(map(rational, v)) for v in data['vertices']]
        if (not self.n or not self.v or not 0 < self.tau < 1
                or any(r <= 0 for r in self.r)
                or any(len(v) != self.n for v in self.v)
                or any(not 0 < p < self.tau for v in self.v for p in v)):
            raise ValueError('Require n>=1, nonempty hull, r>0 and 0<p_i<tau<1')
        self.base = self.v[0]
        self.basis = []
        for v in self.v:
            t = [p-b for p, b in zip(v, self.base)]
            if solve_columns(self.basis, t) is None:
                self.basis.append(t)
        self.d = len(self.basis)
        if self.d > 2:
            raise ValueError('Executable supports actual affine dimension <=2')
        self.coords = [solve_columns(self.basis, [p-b for p, b in zip(v, self.base)])
                       for v in self.v]
        self.facets = []  # c + a*x + b*y >= 0
        if self.d == 1:
            lo = min(t[0] for t in self.coords)
            hi = max(t[0] for t in self.coords)
            self.facets = [[-lo, F(1)], [hi, F(-1)]]
        elif self.d == 2:
            points = sorted(set(map(tuple, self.coords)))
            lo, hi = [], []
            for chain, seq in ((lo, points), (hi, reversed(points))):
                for p in seq:
                    while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:
                        chain.pop()
                    chain.append(p)
            hull = lo[:-1] + hi[:-1]
            for a, b in zip(hull, hull[1:] + hull[:1]):
                dx, dy = b[0]-a[0], b[1]-a[1]
                self.facets.append([dy*a[0]-dx*a[1], -dy, dx])

    def point(self, t):
        return [b + sum(c[i]*x for c, x in zip(self.basis, t))
                for i, b in enumerate(self.base)]

    def contains(self, t, strict=False):
        if len(t) != self.d:
            return False
        values = [f[0]+sum(a*x for a, x in zip(f[1:], t)) for f in self.facets]
        return all(v > 0 if strict else v >= 0 for v in values)

    def weights(self, t):
        """Caratheodory search, used only to export solver-free witness membership."""
        for ids in combinations(range(len(self.v)), self.d+1):
            columns = [[F(1)] + self.coords[i] for i in ids]
            w = solve_columns(columns, [F(1)] + list(t))
            if w is not None and all(x >= 0 for x in w):
                return [{'vertex': i, 'weight': str(x)} for i, x in zip(ids, w)]
        raise ArithmeticError('No convex representation of computed witness')
