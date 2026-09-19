"""Exact independent finite checks for R09; Python standard library only."""
from fractions import Fraction as F
from itertools import permutations, product, combinations
from pathlib import Path
import hashlib,json,random
from explore import cascade,segment_bad,prod

COUNTS={}
def check(name,condition):
    if not condition:raise AssertionError(name)
    COUNTS[name]=COUNTS.get(name,0)+1

def fixed_tree(o):
    if not o:return None
    child=fixed_tree(o[1:])
    return (o[0],child,child)

def trees(labels):
    if not labels:return [None]
    out=[]
    for i in labels:
        children=trees(tuple(j for j in labels if j!=i))
        out.extend((i,a,b) for a in children for b in children)
    return out

def positive_path(tree):
    return () if tree is None else (tree[0],)+positive_path(tree[2])

def backward(tree,p,r,reports=()):
    # Direct continuation-game recursion. Receiver chooses D iff every certificate
    # is present; ties in sender incentives favor silence. No suffix formula used.
    if tree is None:return F(all(reports))
    i,left,right=tree
    silent=backward(left,p,r,reports+(False,))
    disclosed=backward(right,p,r,reports+(True,))
    positive=disclosed if disclosed-r[i]>silent else silent
    return (1-p[i])*silent+p[i]*positive

def certificate(vertices,z,r,o,lam):
    n=len(r)
    if len(z)!=n or len(lam)!=n or sum(lam)!=1 or min(lam)<0:return False
    w=[F(0)]*n
    for j,i in enumerate(o):w[i]=sum(lam[:j])
    g=[w[i]/z[i] for i in range(n)]
    # Membership separately certified by supplied convex combination in fixtures.
    if any(sum(g[i]*(v[i]-z[i]) for i in range(n))>0 for v in vertices):return False
    from math import gcd
    den=1
    for x in list(w)+list(lam):den=den*x.denominator//gcd(den,x.denominator)
    return prod(z[i]**int(den*w[i]) for i in range(n))<=prod(r[o[j]]**int(den*lam[j]) for j in range(n))

def main():
    orders=list(permutations(range(3)));grid=[F(1,5),F(2,5),F(3,5)]
    for p in product(grid,repeat=3):
        for r in product([F(1,10),F(1,5),F(2,5)],repeat=3):
            for o in orders:
                check('backward_game_vs_suffix', (backward(fixed_tree(o),p,r)>0)==cascade(p,r,o))
                check('singleton_segment_vs_suffix',segment_bad(p,p,r,o)==cascade(p,r,o))
    a=(F(1,2),F(1,5),F(3,5));b=(F(1,2),F(3,5),F(1,5));r=(F(3,20),F(1,10),F(1,10))
    mid=tuple((x+y)/2 for x,y in zip(a,b))
    check('vertices_mislead',not cascade(a,r,(0,1,2)) and not cascade(b,r,(0,1,2)))
    for o in orders:check('midpoint_all_orders_bad',cascade(mid,r,o) and segment_bad(a,b,r,o))
    a2=(F(3,5),F(1,2),F(1,10));b2=(F(3,10),F(1,10),F(3,10));r2=(F(11,50),F(13,50),F(7,25))
    check('greedy_failure',segment_bad(a2,b2,r2,(2,1,0)) and not segment_bad(a2,b2,r2,(0,1,2)))
    p3=(F(1,10),F(3,5),F(1,2));r3=(F(4,25),F(1,2),F(8,25))
    good=[o for o in orders if not cascade(p3,r3,o)]
    check('five_successful_words',len(good)==5 and (0,2,1) not in good)
    prefixes={frozenset(o[:j]) for o in good for j in range(4)}
    check('all_prefix_sets_present',len(prefixes)==8)
    r8=(F(7,50),F(2,5),F(1,10))
    vertices=[(F(13,20),F(3,5),F(1,5)),(F(13,20),F(3,80),F(13,20))]
    z=(F(13,20),F(7,20),F(2,5));lam=(F(7,10),F(3,10),F(0))
    check('certificate_membership',z==tuple(F(5,9)*a+F(4,9)*b for a,b in zip(*vertices)))
    check('rational_polytope_certificate',certificate(vertices,z,r8,(0,1,2),lam))
    check('wrong_certificate_rejected',not certificate(vertices,z,r8,(0,1,2),(F(1),F(0),F(0))))
    v4=[tuple(F(1,4)+F(x,4) for x in bits) for bits in product([0,1],repeat=4) if sum(bits)<=2]
    for pair in combinations(range(4),2):
        check('identical_pairwise_projections',{tuple(v[i] for i in pair) for v in v4}==set(product([F(1,4),F(1,2)],repeat=2)))
    check('projection_product_bound',F(125,1728)<F(1,10)<F(1,8))
    for o in permutations(range(4)):check('box_all_orders_bad',cascade((F(1,2),)*4,(F(1,10),)*4,o))
    rng=random.Random(19092026)
    for n,cases in [(3,60),(4,8)]:
        ts=trees(tuple(range(n)))
        for _ in range(cases):
            p=tuple(rng.choice(grid) for _ in range(n));r=tuple(F(rng.randrange(1,50),100) for _ in range(n))
            for tree in ts:
                check('adaptive_game_vs_positive_path',(backward(tree,p,r)>0)==cascade(p,r,positive_path(tree)))
    for n in range(2,7):
        for _ in range(200):
            p=tuple(rng.choice(grid) for _ in range(n));r=tuple(F(rng.randrange(1,70),100) for _ in range(n))
            o=list(range(n));rng.shuffle(o);j=rng.randrange(n-1);i,k=o[j:j+2]
            if r[i]*p[i]>=r[k]*p[k]:
                swapped=o[:];swapped[j:j+2]=[k,i]
                check('uniform_swap_pointwise',not cascade(p,r,o) or cascade(p,r,swapped))
            sorted_o=tuple(sorted(range(n),key=lambda i:-r[i]*p[i]))
            check('known_model_sorted_score',cascade(p,r,sorted_o)==all(r[i]<prod(p[j] for j in range(n) if j!=i) for i in range(n)))
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('explore.py')]}
    print(json.dumps({'status':'passed','arithmetic':'fractions.Fraction','seed':19092026,'counts':COUNTS,'total':sum(COUNTS.values()),'source_sha256':hashes,'witnesses':{'vertex_counterexample':{'a':a,'b':b,'r':(F(3,20),F(1,10),F(1,10))},'switching_blocker_certificate':{'z':z,'lambda':lam,'vertices':vertices},'successful_words':good}},default=str,indent=2))
if __name__=='__main__':main()
