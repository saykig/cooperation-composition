"""Exact within-game dimension sharpness: witness search then rational certificates.
A failed finite search is reported as inconclusive, never as a feasibility decision.
"""
from fractions import Fraction as F
from itertools import permutations, combinations
from math import prod
from pathlib import Path
import hashlib
import json
import random
import time
from selector import require, constraints, decide, verify_sign

HERE = Path(__file__).resolve().parent


def rank(rows):
    a = [list(row) for row in rows]
    pivot = 0
    if not a:
        return 0
    for j in range(len(a[0])):
        k = next((k for k in range(pivot,len(a)) if a[k][j]),None)
        if k is None:
            continue
        a[pivot],a[k] = a[k],a[pivot]
        c = a[pivot][j]
        a[pivot] = [x/c for x in a[pivot]]
        for k in range(len(a)):
            if k != pivot:
                c = a[k][j]
                a[k] = [x-c*y for x,y in zip(a[k],a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def gains(p,r,prefix):
    remaining = set(range(len(p)))
    values = []
    for i in prefix:
        remaining.remove(i)
        values.append(prod(p[k] for k in remaining)-r[i])
    return values


def certify(m, vertices, r, tau):
    """P is EXACT convex hull of these rational points; no gridded continuum claim."""
    n=m+1; q=F(4,5); weight_sum=F(m*(m+1),2)
    require(all(len(v)==n and all(0<x<tau for x in v) for v in vertices))
    require(all(v[0]==vertices[0][0] for v in vertices))
    require(all(sum(i*v[i] for i in range(1,n))==q*weight_sum for v in vertices))
    require(r[:m]==[q**(m-i) for i in range(m)] and r[-1]>0)
    dim = rank([[x-y for x,y in zip(v,vertices[0])] for v in vertices[1:]])
    require(dim==m-1)
    rejected=[]
    for prefix in permutations(range(n),m-1):
        k=next((k for k,v in enumerate(vertices) if all(x>0 for x in gains(v,r,prefix))),None)
        require(k is not None,'missing strict prefix witness')
        rejected.append({'prefix':list(prefix),'vertex':k,
                         'positive_margins':list(map(str,gains(vertices[k],r,prefix)))})
    # For every point of the hull, weighted AM-GM gives product p_i^i <= q^sum(i).
    # Multiplying the first m canonical strict cascade inequalities contradicts it.
    return {'dimension':dim,'n':n,'q':str(q),'tau':str(tau),'r':list(map(str,r)),
            'vertices':[list(map(str,v)) for v in vertices],
            'successful_prefix':list(range(m)), 'full_order':list(range(n)),
            'universal_certificate':{'weights':list(range(1,n)),
                  'weighted_sum':str(q*weight_sum),'threshold_product':str(prod(r[:m])),
                  'bound':str(q**int(weight_sum)), 'method':'weighted AM-GM on affine hull'},
            'rejected_shorter_prefixes':rejected}


def triangle_search():
    # Finite rational search finds candidate witnesses only. certify() supplies
    # the continuum upper certificate and exact lower witnesses afterward.
    r=[F(64,125),F(16,25),F(4,5),F(1,100)]
    pairs=list(permutations(range(4),2)); reps={}; admissible=0
    for u in range(1,100):
        for v in range(1,100):
            p=(F(99,100),F(u,100),F(v,100),(F(24,5)-F(u,100)-2*F(v,100))/3)
            if not 0<p[3]<F(999,1000):
                continue
            admissible+=1
            mask=sum(1<<k for k,prefix in enumerate(pairs) if all(x>0 for x in gains(p,r,prefix)))
            if mask:
                reps.setdefault(mask,p)
    full=(1<<len(pairs))-1
    for size in range(1,4):
        for combo in combinations(reps,size):
            mask=0
            for c in combo:
                mask |= c
            if mask==full:
                return certify(3,[reps[c] for c in combo],r,F(999,1000)), {
                    'tested_grid_points':99**2,'admissible_points':admissible,
                    'distinct_nonempty_coverage_patterns':len(reps),
                    'cover_size':size,'minimal_cover_scope':'this finite searched catalogue only'}
    raise ValueError('triangle not recovered')


def higher_search():
    rng=random.Random(19092028); results=[]
    for m in (4,5):
        n=m+1; missing=set(permutations(range(n),m-1));found={}
        r=[F(4,5)**(m-i) for i in range(m)]+[F(1,1000)]
        valid=0
        for trial in range(30000):
            p=[F(999,1000)]+[F(rng.randrange(1,1000),1000) for _ in range(m-1)]
            p.append((F(4,5)*m*(m+1)/2-sum(i*p[i] for i in range(1,m)))/m)
            if not 0<p[-1]<F(9999,10000):
                continue
            valid+=1
            vals={mask:prod(p[i] for i in range(n) if mask>>i&1) for mask in range(1<<n)}
            for pref in list(missing):
                mask=(1<<n)-1
                for i in pref:
                    mask &= ~(1<<i)
                    if vals[mask]<=r[i]:
                        break
                else:
                    found[pref]=p
                    missing.remove(pref)
            if not missing:
                break
        record={'m':m,'trials':trial+1,'admissible_samples':valid,
                'missing_prefixes':[list(x) for x in sorted(missing)],
                'status':'certified' if not missing else 'inconclusive bounded search'}
        if not missing:
            vertices=sorted(set(tuple(p) for p in found.values()))
            record['certificate']=certify(m,vertices,r,F(9999,10000))
        else:
            record['interpretation']='No nonexistence or stronger reduction inferred.'
        results.append(record)
    return results


def main():
    start=time.perf_counter()
    d={'a':['13/20','3/5','1/5'],'b':['13/20','3/80','13/20'],
       'r':['7/50','2/5','1/10']}
    single=[]
    for i in range(3):
        c=decide(constraints(d,[i]));require(verify_sign(constraints(d,[i]),c))
        single.append({'prefix':[i],'certificate':c})
    pair=decide(constraints(d,[0,1]));require(not verify_sign(constraints(d,[0,1]),pair))
    tri,search=triangle_search()
    report={'status':'passed','segment_sharpness':{'input':d,'rejected_singletons':single,
                    'successful_pair':[0,1],'certificate':pair},
            'dimension_two':tri,'triangle_search':search,'higher_dimensions':higher_search(),
            'elapsed_seconds':time.perf_counter()-start,
            'source_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in ['selector.py','sharpness.py']},
            'scope':'Handwritten AM-GM proof plus exact rational certificate checks; no formal verification.'}
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
