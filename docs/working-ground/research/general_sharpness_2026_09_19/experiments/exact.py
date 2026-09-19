"""Rational certificate utilities; standard library, no numerical optimizer."""
from fractions import Fraction as F
from math import prod


def require(ok, message='certificate check failed'):
    if not ok: raise ValueError(message)


def log_bounds(x, terms=24):
    """Proved rational bounds: log(x)=k log(2)+2 atanh((y-1)/(y+1))."""
    x=F(x);require(x>0);k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def series(y):
        z=(y-1)/(y+1)
        s=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        err=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return s,s+err
    lo,hi=series(x);a,b=series(F(2))
    lo,hi=(lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)
    # Outward rounding preserves the bounds and keeps evidence compact.
    scale=10**14
    return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)


def ratios(p,r,prefix):
    remaining=set(range(len(p)));out=[]
    for i in prefix:
        remaining.remove(i)
        out.append(prod(p[j] for j in remaining)/r[i])
    return out


def rank(rows):
    a=[list(map(F,row)) for row in rows];jrow=0
    if not a:return 0
    for col in range(len(a[0])):
        k=next((k for k in range(jrow,len(a)) if a[k][col]),None)
        if k is None:continue
        a[k],a[jrow]=a[jrow],a[k];c=a[jrow][col]
        a[jrow]=[v/c for v in a[jrow]]
        for k in range(len(a)):
            if k!=jrow:
                c=a[k][col];a[k]=[v-c*w for v,w in zip(a[k],a[jrow])]
        jrow+=1
        if jrow==len(a):break
    return jrow


def margin_certificate(p,r,prefix,lam,tau,budget):
    """Upper bound by concave tangent + exact fractional-knapsack support."""
    m=len(p)-1
    require(len(lam)==len(prefix) and min(lam)>=0 and sum(lam)==1)
    rs=ratios(p,r,prefix)
    lower=min(log_bounds(x)[0] for x in rs)
    g=[F(0)]*m;remaining=set(range(m+1))
    for i,w in zip(prefix,lam):
        remaining.remove(i)
        for j in remaining:
            if j:g[j-1]+=w/p[j]
    # p0 is fixed and contributes zero derivative in the affine slice.
    rest=budget;v=[F(0)]*m
    for j in sorted(range(m),key=lambda j:(-g[j]/(j+1),j)):
        v[j]=min(tau,rest/(j+1));rest-=(j+1)*v[j]
    require(rest==0)
    correction=sum(g[j]*(v[j]-p[j+1]) for j in range(m))
    upper=sum(w*log_bounds(x)[1] for w,x in zip(lam,rs))+correction
    require(upper>=lower)
    # Again outward round to keep stored bounds small and easy to review.
    scale=10**12
    lo=F((lower*scale).__floor__(),scale);hi=F((upper*scale).__ceil__(),scale)
    return {'ratio_margins':[str(x-1) for x in rs],
            'log_margin_lower':str(lo),'supremum_upper':str(hi),
            'certified_gap':str(hi-lo),'weights':list(map(str,lam)),
            'support_vertex':list(map(str,v)),
            'gradient':list(map(str,g))}
