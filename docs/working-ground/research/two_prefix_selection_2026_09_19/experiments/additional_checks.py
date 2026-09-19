"""Additive checks after the frozen first R10 receipt; does not overwrite it."""
import copy
from fractions import Fraction as F
from itertools import permutations
import hashlib
import json
from pathlib import Path
import random
import time
from selector import require, select, verify, decide, verify_sign, constraints

HERE=Path(__file__).resolve().parent

def main():
    start=time.perf_counter();checks=0
    def check(ok):
        nonlocal checks
        require(ok);checks+=1
    # A shared irrational root, a double irrational root and opposite signs.
    for gs,expected in [([(-F(1,2),0,1),(F(1,2),0,-1)],False),
                        ([(F(1,4),0,-1,0,1)],True),
                        ([(F(1,4),0,-1,0,1),(-F(1,4),0,1,0,-1)],False)]:
        cert=decide(gs);check(verify_sign(gs,cert)==expected)
    rng=random.Random(19092029)
    for n in range(2,5):
        for _ in range(10):
            data={'a':[str(F(rng.randrange(1,13),20)) for _ in range(n)],
                  'b':[str(F(rng.randrange(1,13),20)) for _ in range(n)],
                  'r':[str(F(rng.randrange(1,31),100)) for _ in range(n)]}
            answer=select(data);check(verify(data,answer))
            rev=dict(data,a=data['b'],b=data['a'])
            reverse_answer=select(rev)
            check(verify(rev,reverse_answer) and answer['status']==reverse_answer['status'])
            order=list(range(n));rng.shuffle(order)
            relabel={key:[data[key][i] for i in order] for key in ('a','b','r')}
            renamed=select(relabel)
            check(verify(relabel,renamed) and answer['status']==renamed['status'])
    eps=F(1,10**60+7)
    big={'a':[str(F(1,3)+eps),str(F(1,2)-eps),str(F(1,5)+eps)],
         'b':[str(F(1,2)+eps),str(F(1,4)-eps),str(F(3,5)-eps)],
         'r':['7/50','2/5','1/10']}
    answer=select(big);check(verify(big,answer))
    good=[]
    for order in permutations(range(3)):
        cert=decide(constraints(big,order))
        if not verify_sign(constraints(big,order),cert):good.append(order)
        check(True)
    check(bool(good)==(answer['status']=='success'))
    # Invalid instance input must fail before producing a certificate.
    for bad in [dict(big,r=['0','1/5','1/10']),dict(big,a=['0','1/2','1/5']),
                dict(big,b=['2/3','1/4','3/5']),dict(big,b=['1/2'])]:
        try:select(bad)
        except ValueError:check(True)
        else:raise ValueError('invalid instance accepted')
    print(json.dumps({'status':'passed','checks':checks,'large_endpoint_input':big,
                      'result':answer,'elapsed_seconds':time.perf_counter()-start,
                      'source_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                       for name in ['selector.py','additional_checks.py']}},indent=2))
if __name__=='__main__':main()
