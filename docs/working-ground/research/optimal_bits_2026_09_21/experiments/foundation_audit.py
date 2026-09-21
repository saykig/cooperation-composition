"""Independent exact probes; no third-party dependencies; assertions survive -O."""
from fractions import Fraction as F
from itertools import combinations
import json

counts = {}

def check(value, category):
    if not value:
        raise ValueError(category)
    counts[category] = counts.get(category, 0) + 1

def ratio_margin(point, ratios):
    suffix = F(1)
    margins = []
    for p, r in zip(reversed(point), reversed(ratios)):
        margins.append(suffix/r)
        suffix *= p
    return min(margins)  # exp(m), so comparison with 1 is exact

def main():
    m = 8
    h = F(3, 20*(m+1))
    vertices = [(F(1,4)+h*j, F(3,5)-(F(1,4)+h*j)**2)
                for j in range(m+2)]
    for k, v in enumerate(vertices):
        n = (2*v[0], F(1))
        total = n[0]*v[0]+v[1]
        check(total <= F(19,25), 'packing_normalizer')
        for j, z in enumerate(vertices):
            gap = sum(a*(b-c) for a,b,c in zip(n,v,z))
            check(gap == (v[0]-z[0])**2, 'tangent_identity')
            if j != k:
                check(gap/total >= F(9,304*(m+1)**2), 'tangent_gap')
    for mask, other in combinations(range(1 << m), 2):
        k = ((mask ^ other) & -(mask ^ other)).bit_length()
        with_k, without_k = (mask,other) if mask & (1 << (k-1)) else (other,mask)
        check(bool(with_k & (1 << (k-1))) and not without_k & (1 << (k-1)),
              'arbitrary_packing_pair')
    rho = F(1,2)
    a,b,g = (F(9,16),F(1,4)),(F(1,9),F(9,16)),(F(1,4),F(3,8))
    ratios = (F(9,100),F(1,3),F(1,10))
    check(all(g[i]**2 == a[i]*b[i] for i in range(2)), 'geometric_mean')
    check(ratio_margin((rho,)+a,ratios)<1, 'nonconvex_a')
    check(ratio_margin((rho,)+b,ratios)<1, 'nonconvex_b')
    check(ratio_margin((rho,)+g,ratios)>1, 'nonconvex_g')
    r = (F(1,4),F(1,4))
    check(ratio_margin((rho,F(1,4)),r)==1, 'favorable_tie')
    check(ratio_margin((rho,F(1,2)),r)==2, 'beta_equals_gamma')
    # Exp of directed discrepancy for singleton products equals product of
    # max(1,p_i/q_i), directly maximizing each weight on [0,1].
    forward = max(1,F(1,2)/F(1,4))*max(1,F(1,4)/F(1,2))
    backward = max(1,F(1,4)/F(1,2))*max(1,F(1,2)/F(1,4))
    check(max(forward,backward)==2 and 2*2==4, 'symmetric_nonadditivity')
    print(json.dumps({'arithmetic':'fractions.Fraction','counts':counts,
                      'total':sum(counts.values()),'status':'pass'},sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
