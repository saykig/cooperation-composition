"""Source-relative rational sandwich check, independent of encoder geometry.

Input: explicit source and decoded points. This module imports no codec code.
It constructs full downward polygons rather than the encoder's NE record chain.
"""
from fractions import Fraction as F

def det(o,a,b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])

def downward_polygon(points):
    cloud = {(F(0),F(0))}
    for x,y in points:
        cloud.update(((x,y),(x,F(0)),(F(0),y)))
    cloud = sorted(cloud)
    def half(seq):
        out = []
        for p in seq:
            while len(out)>=2 and det(out[-2],out[-1],p)<=0:
                out.pop()
            out.append(p)
        return out
    return half(cloud)[:-1]+half(reversed(cloud))[:-1]

def contained(points,polygon):
    return all(all(det(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]))
               for p in points)

def verify(source,decoded,epsilon,ell=F(1,8),u=F(3,4)):
    if not source or not decoded or not 0<epsilon<ell/2:
        return False
    if any(len(p)!=2 or not all(ell<=x<=u for x in p) for p in source):
        return False
    if any(len(p)!=2 or not all(0<x<=u for x in p) for p in decoded):
        return False
    factor = 1+epsilon/(ell-epsilon)
    lower = downward_polygon(source)
    upper = downward_polygon([tuple(factor*x for x in p) for p in decoded])
    return contained(decoded,lower) and contained(source,upper)
