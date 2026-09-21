"""Exact three-sender contextual decisions, including strict cascade ties.

Known sender first, two-coordinate uncertain family next. Tests the rational
outer/lower decision rule; does not implement arbitrary-order optimization.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement,product
import json
from codec import encode,decode
from verify import downward_polygon,verify

def cascades(vertices,r0,r1,r2):
    # Exists p in conv(V): x*y>r0, y>r1, 1>r2. The maximizer of
    # xy over y>=r1 lies on a Pareto edge. Enumerating all vertex pairs
    # includes every such edge, with no assumption on the vertex order.
    if r2>=1 or max(y for x,y in vertices)<=r1:
        return False
    best = F(0)
    for a,b in combinations_with_replacement(vertices,2):
        if a[1]<b[1]:
            a,b = b,a
        if a[1]<r1:
            continue
        dx,dy = b[0]-a[0],b[1]-a[1]
        hi = F(1) if b[1]>=r1 else (a[1]-r1)/(a[1]-b[1])
        choices = [F(0),hi]
        if dx*dy<0:
            critical = -(dx*a[1]+dy*a[0])/(2*dx*dy)
            if 0<critical<hi:
                choices.append(critical)
        for t in choices:
            best = max(best,(a[0]+t*dx)*(a[1]+t*dy))
    return best>r0

def main():
    sources = [
        [(F(1,4),F(1,2)),(F(1,2),F(1,4))],
        [(F(1,3),F(2,5))],
        [(F(1,8),F(3,4)),(F(1,2),F(2,3)),(F(3,4),F(1,8))],
        [(F(1,4)+F(j,80),F(3,5)-(F(1,4)+F(j,80))**2) for j in range(13)]
    ]
    results = {'zero':0,'full':0,'refine':0}
    for source in sources:
        b = 7
        payload,_ = encode(source,b)
        _,decoded = decode(payload)
        epsilon,ell = F(1,1 << b),F(1,8)
        if not verify(source,decoded,epsilon):
            raise ValueError('sandwich failed')
        lower = [p for p in downward_polygon(decoded) if all(x>0 for x in p)]
        scale = 1+epsilon/(ell-epsilon)
        upper = [tuple(scale*x for x in p) for p in lower]
        for r0,r1,r2 in product([F(j,64) for j in range(1,33)],
                                [F(j,16) for j in range(1,13)],
                                (F(1,2),F(1),F(3,2))):
            real = cascades(source,r0,r1,r2)
            low = cascades(lower,r0,r1,r2)
            high = cascades(upper,r0,r1,r2)
            if low and not real or real and not high:
                raise ValueError('unsound contextual bracket')
            answer = 'zero' if not high else 'full' if low else 'refine'
            results[answer] += 1
    # Tangency is favorable and strict inequalities must not be relaxed.
    segment = [(F(1,4),F(1,2)),(F(1,2),F(1,4))]
    if cascades(segment,F(9,64),F(1,8),F(1,2)):
        raise ValueError('product tangency incorrectly called strict cascade')
    if not cascades(segment,F(9,64)-F(1,10000),F(1,8),F(1,2)):
        raise ValueError('strict interior cascade missed')
    if cascades(segment,F(1,100),F(1,2),F(1,2)):
        raise ValueError('suffix tie incorrectly called strict cascade')
    print(json.dumps({'status':'pass','arithmetic':'fractions.Fraction',
                      'contextual_queries':sum(results.values()),'answers':results,
                      'exact_tie_controls':3,
                      'scope':'known first sender; two-coordinate convex source; fixed order'},
                     sort_keys=True,indent=2))

if __name__=='__main__':
    main()
