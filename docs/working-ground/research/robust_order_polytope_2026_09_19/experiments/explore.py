from fractions import Fraction as F
from itertools import permutations, product
import json, random

def prod(xs):
    z=F(1)
    for x in xs:z*=x
    return z

def cascade(p,r,o):
    return all(r[i]<prod(p[k] for k in o[j+1:]) for j,i in enumerate(o))

def segment_bad(a,b,r,o):
    i,j,k=o
    if r[k]>=1:return False
    d=[b[z]-a[z] for z in range(3)]
    lo,hi=F(0),F(1)
    if d[k]==0:
        if a[k]<=r[j]:return False
    elif d[k]>0:lo=max(lo,(r[j]-a[k])/d[k])
    else:hi=min(hi,(r[j]-a[k])/d[k])
    if hi<=lo:return False
    c0=a[j]*a[k]-r[i];c1=a[j]*d[k]+a[k]*d[j];c2=d[j]*d[k]
    candidates=[lo,hi]
    if c2<0:
        t=-c1/(2*c2)
        if lo<=t<=hi:candidates.append(t)
    return max(c0+c1*t+c2*t*t for t in candidates)>0

def main():
    rng=random.Random(19092026);orders=list(permutations(range(3)))
    pgrid=[F(i,10) for i in range(1,7)]
    rgrid=[F(i,100) for i in range(2,61,2)]
    found={}
    for trial in range(100000):
        a=tuple(rng.choice(pgrid) for _ in range(3));b=tuple(rng.choice(pgrid) for _ in range(3))
        r=tuple(rng.choice(rgrid) for _ in range(3))
        good=[o for o in orders if not segment_bad(a,b,r,o)]
        greedy=tuple(sorted(range(3),key=lambda i:(-r[i],i)))
        if good and greedy not in good and 'largest_cost_first' not in found:
            found['largest_cost_first']={'a':a,'b':b,'r':r,'good':good,'greedy':greedy}
        if (0,1,2) in good and (2,1,0) in good and (0,2,1) not in good and 'antimatroid' not in found:
            found['antimatroid']={'a':a,'b':b,'r':r,'good':good}
        if len(found)==2:break
    print(json.dumps({'trials':trial+1,'found':found},default=str,indent=2))
if __name__=='__main__':main()
