"""Audit R08 against independent extensive-game calculations and mixed feasibility."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import time
import z3
from game import Game, require, encode_profile
from mixed import solve


def historical_prediction(g,e):
    """R08 formula is used ONLY on the comparison side, never to solve the game."""
    return e>=g.B or any(g.k[i]>=g.eta[i]*math.prod(g.p[t] for t in g.order[j+1:])
                        for j,i in enumerate(g.order))


def primitive_input(g):
    return {'p':list(map(str,g.p)), 'k':list(map(str,g.k)),
            'eta':list(map(str,g.eta)), 'A':str(g.A),'B':str(g.B),'order':list(g.order)}


def fixture_games():
    # Every position gets an exact tie, both sides, and heterogeneous primitives.
    out=[]
    for n in (2,3):
        for costs in product((F(1,8),F(1,4),F(1)),repeat=n):
            # n=3 uses a bounded covering slice instead of repeating 27 similar games.
            if n==3 and costs not in [(F(1,8),)*3,(F(1,4),)*3,
                                     (F(1,8),F(1,2),F(1)),
                                     (F(1,8),F(1,8),F(1)),
                                     (F(1,4),F(1,8),F(1,8)),
                                     (F(1,8),F(1),F(1,8))]:continue
            out.append(('grid_'+str(n)+'_'+str(len(out)),Game([F(1,2)]*n,costs)))
    out += [
        ('middle_exact_tie',Game(['1/2']*3,['1/8','1/2','1/4'])),
        ('heterogeneous',Game(['1/5','2/5','3/5'],['3/25','1/5','4/5'],['2','3/2','4/5'],A=3,B=F(3,2))),
        ('tiny_cost',Game(['1/10','1/3','3/5'],['1/1000000000000000000000000']*3)),
        ('near_prior_boundary',Game([str(F(2,3)-F(1,10**20)),'1/100000000000000000000'],['1/10','1/2'])),
        ('one_sender_tie',Game(['1/2'],['1'])),
        ('one_sender_strict',Game(['1/2'],['1/2'])),
    ]
    return out


def run(output=None):
    start=time.monotonic();rows=[];pure_profiles=0;mixed_queries=0;assessments=0
    for name,g in fixture_games():
        for e in [F(0),g.B/2,g.B-F(1,10**20),g.B,g.B+F(1,7)]:
            q,rho,a=g.backward_candidate(e);assessments+=1
            pred=historical_prediction(g,e)
            require(a['target']==pred,name+' backward target mismatch')
            row={'name':name,'game':primitive_input(g),'fine':str(e),'target':a['target']}
            # Full sender-plan enumeration, and all receiver tie best replies.
            # Distinct sub-B fines are covered by mixed/tree checks; pure search
            # needs only 0 and B to cover both receiver regimes.
            if e in (0,g.B):
                equilibria,count=g.pure_equilibria(e);pure_profiles+=count
                target_count=sum(x[2]['target'] for x in equilibria)
                require((target_count>0)==pred,name+' exhaustive pure mismatch')
                row.update(pure_profiles=count,pure_equilibria=len(equilibria),target_pure_equilibria=target_count)
            # Arbitrary real mixing at EVERY sender/receiver information set.
            answer=solve(g,e);mixed_queries+=1
            require(answer['exists']==pred,name+' mixed-equilibrium mismatch')
            row['mixed_exists']=answer['exists']
            rows.append(row)
        print(name,'passed',flush=True)

    # Three-sender shared-family benchmark: retain its changing blocker and all
    # orders; this is a finite game audit, not a new continuum/polytope proof.
    order_rows=[]
    for s in [F(1,5),F(7,25),F(2,5),F(13,20)]:
        for order in permutations(range(3)):
            g=Game([F(13,20),F(17,20)-F(5,4)*s,s],[F(7,50),F(2,5),F(1,10)],order=order)
            q,rho,a=g.backward_candidate(0);assessments+=1
            answer=solve(g,F(0));mixed_queries+=1
            require(a['target']==answer['exists']==historical_prediction(g,0),'Shared-family/order mismatch')
            order_rows.append({'s':str(s),'order':list(order),'target':a['target']})

    four_rows=[]
    for name,p,k,order in [
        ('strict',['1/2']*4,['1/16']*4,[0,1,2,3]),
        ('root_tie',['1/2']*4,['1/8','1/16','1/16','1/16'],[0,1,2,3]),
        ('middle_tie',['1/2']*4,['1/16','1/4','1/16','1/16'],[0,1,2,3]),
        ('last_tie',['1/2']*4,['1/16','1/16','1/16','1'],[0,1,2,3]),
        ('permuted',['1/5','2/5','1/2','3/5'],['1/20','1/10','1/5','1/2'],[3,1,0,2]),
    ]:
        g=Game(p,k,order=order)
        for e in [F(0),F(999,1000),g.B]:
            q,rho,a=g.backward_candidate(e);assessments+=1
            answer=solve(g,e);mixed_queries+=1
            require(a['target']==answer['exists']==historical_prediction(g,e),'Four-sender mismatch')
            four_rows.append({'name':name,'game':primitive_input(g),'fine':str(e),'target':a['target']})

    # Explicit nonpure sequential equilibria: same tie permits silence or report.
    g=Game(['1/2']*2,['1/4','1']);tie_examples=[]
    for root in [F(0),F(1,3),F(1)]:
        q={():root,(0,):F(0),(1,):F(1,2)}
        rho={h:F(all(h)) for h in g.terminals}
        a=g.assessment(q,rho,F(0));assessments+=1
        require(a['equilibrium'] and a['target']==(root==0),'Mixed tie witness invalid')
        tie_examples.append({'q':encode_profile(q),'rho':encode_profile(rho),'target':a['target'],
                             'sender_gains':[(list(h),str(v)) for h,v in a['sender_gains']]})

    # Attempt invalid off-path threats and mechanically altered receiver tie rule.
    g=Game(['1/2']*2,['1/4']*2)
    q={h:F(0) for h in g.nodes};rho={h:F(all(h)) for h in g.terminals}
    require(not g.assessment(q,rho,0)['equilibrium'],'Noncredible off-path silence accepted')
    q,rho,a=g.backward_candidate(g.B)
    bad=dict(rho);bad[(1,1)]=F(1)
    require(not g.assessment(q,bad,g.B)['equilibrium'],'Changed complete-history tie failed to affect incentives')

    # Beliefs from polynomial leading terms, at BOTH types and all histories.
    # Compare two nonuniform tremble-rate sequences and the independently derived
    # factorization, on non-equilibrium strategies as well as equilibria.
    belief_checks=0;receiver_bounds=0
    for n in (2,3,4):
        g=Game([F(i+1,2*n+1) for i in range(n)],[F(1,4)]*n)
        for shift in range(4):
            q={h:[F(0),F(1,3),F(2,3),F(1)][(i+shift)%4] for i,h in enumerate(g.nodes)}
            powers={h:1+(i%3) for i,h in enumerate(g.nodes)}
            for h in g.nodes+g.terminals:
                for own in ([0,1] if len(h)<n else [None]):
                    mu=g.belief(q,h,own);mu2=g.belief(q,h,own,powers)
                    require(mu==mu2 and sum(mu.values())==1 and all(v>=0 for v in mu.values()),'Tremble limit inconsistent')
                    marg=list(g.p)
                    for j,report in enumerate(h):
                        i=g.order[j];a=q[h[:j]]
                        marg[i]=F(1) if report else g.p[i]*(1-a)/(1-g.p[i]*a)
                    if own is not None:marg[g.order[len(h)]]=F(own)
                    for x,w in mu.items():
                        expected=math.prod(p if bit else 1-p for p,bit in zip(marg,x))
                        require(w==expected,'Factorized belief disagrees with state/tremble enumeration')
                    if len(h)==n and not all(h):
                        require(g.receiver_gain(mu,0)<0,'Incomplete receiver strictness failed');receiver_bounds+=1
                    belief_checks+=1

    invalid=0
    for p,k in [(['0','1/2'],['1/4']*2),(['2/3','1/2'],['1/4']*2),
                (['1','1/2'],['1/4']*2),(['1/2']*2,['0','1/4'])]:
        try:Game(p,k)
        except ValueError:invalid+=1
        else:raise ValueError('Outside-domain case silently treated as R08')
    report={'evidence':'written derivation plus finite exact state/path/tremble checks and solver-trusted mixed feasibility',
            'python':platform.python_version(),'z3':z3.get_version_string(),
            'primitive_cases':rows,'shared_order_cases':order_rows,'four_sender_cases':four_rows,
            'pure_complete_profiles':pure_profiles,'mixed_equilibrium_queries':mixed_queries,
            'constructed_assessments':assessments,'belief_information_sets':belief_checks,
            'incomplete_receiver_checks':receiver_bounds,'invalid_domain_rejections':invalid,
            'mixed_tie_examples':tie_examples,'negative_controls':2,
            'seconds':round(time.monotonic()-start,6),
            'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(__file__).parent.glob('*.py'))}}
    if output:output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('primitive_cases','shared_order_cases','four_sender_cases')},indent=2))
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);run(p.parse_args().output)
