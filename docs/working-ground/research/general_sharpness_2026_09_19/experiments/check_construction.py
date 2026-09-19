"""Exact finite falsification checks for the general construction; not its proof."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from math import prod
import hashlib,json,random,time
from exact import require,rank
from construction import parameters,dimension_points,check_witness

HERE=Path(__file__).resolve().parent


def main():
    start=time.perf_counter();counts={};examples=[]
    for m in range(2,8):
        count=0
        for prefix in permutations(range(m+1),m-1):
            p,x,method,bounds=check_witness(m,prefix);count+=1
            if prefix==tuple(range(m-1)):
                examples.append({'m':m,'prefix':list(prefix),'p':list(map(str,p)),
                                 'deficits':list(map(str,x)),'method':method,
                                 'linear_slacks':list(map(str,bounds))})
        counts[str(m)]=count
    rng=random.Random(19092030);large=[]
    for m in [8,10,20,50,100]:
        prefixes=[tuple(range(m-1)),tuple(range(m-2,-1,-1)),tuple([0]+list(range(m,m-(m-2),-1)))]
        prefixes += [tuple(rng.sample(range(m+1),m-1)) for _ in range(12)]
        for prefix in prefixes:check_witness(m,prefix)
        large.append({'m':m,'prefixes_checked':len(prefixes)})
    dimensions=[]
    for m in range(2,11):
        par=parameters(m);points=dimension_points(m)
        require(rank([[x-y for x,y in zip(v,points[0])] for v in points[1:]])==m-1)
        for p in points:
            require(all(0<v<par['tau'] for v in p))
            require(sum(i*p[i] for i in range(1,m+1))==par['q']*par['C'])
        require(prod(par['r'][:m])==par['q']**int(par['C']))
        # The q=4/5 failure condition is checked exactly for a range; the all-m
        # claim is the monotone polynomial argument in FIXED_THRESHOLD.md.
        dimensions.append(m-1)
    fixed=[]
    for m in range(11,101):
        C=F(m*(m+1),2)
        require(C/5>=F(m-1)+F(m,4))
        fixed.append(m)
    report={'status':'passed','exhaustive_prefix_counts':counts,
            'total_exhaustive_prefixes':sum(counts.values()),'large_dimension_checks':large,
            'affine_dimensions_checked':dimensions,'fixed_q_obstruction_integer_checks':fixed,
            'canonical_witness_examples':examples,'elapsed_seconds':time.perf_counter()-start,
            'source_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in ['exact.py','construction.py','check_construction.py']},
            'scope':'Finite exact tests of explicit formulas; arbitrary-d conclusions depend on the handwritten proof.'}
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
