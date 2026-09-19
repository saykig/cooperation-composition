"""Primitive extensive-game evaluator. No suffix-product characterization.

0=silence/C; 1=certificate/D. q[h] is positive-type sender behavior;
type zero has ONLY silence. Receiver behavior is rho[terminal history].
Beliefs are computed from exact polynomial trembles and full state enumeration.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import math


def require(test, message):
    if not test:
        raise ValueError(message)


def histories(n, terminal=False):
    return list(product((0,1), repeat=n)) if terminal else [h for j in range(n) for h in product((0,1),repeat=j)]


def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


class Game:
    def __init__(self,p,k,eta=None,A=2,B=1,order=None):
        self.p=tuple(map(F,p)); self.k=tuple(map(F,k));self.n=len(self.p)
        self.eta=tuple(map(F,eta or [1]*self.n));self.A=F(A);self.B=F(B)
        self.order=tuple(range(self.n)) if order is None else tuple(order)
        require(self.n>=1 and len(self.k)==len(self.eta)==self.n,'shape')
        require(sorted(self.order)==list(range(self.n)),'order')
        require(self.A>0 and self.B>0,'receiver payoffs')
        require(all(x>0 for x in self.k+self.eta),'strict costs/rewards')
        require(all(0<x<self.A/(self.A+self.B) for x in self.p),'strict prior domain')
        self.states=histories(self.n,True)
        self.prior={x:math.prod(p if bit else 1-p for p,bit in zip(self.p,x)) for x in self.states}
        self.nodes=histories(self.n);self.terminals=histories(self.n,True)

    def belief(self,q,h,own=None,powers=None):
        """Limit of Bayesian beliefs for q_eps=q+(1-2q)*eps**power.

        Enumerate every state and its actual trembled transcript probability.
        Leading coefficients compute the limit exactly, including zero-reach h.
        No cancellation formula for posteriors is used here.
        """
        mass={}
        for x in self.states:
            if own is not None and x[self.order[len(h)]]!=own:continue
            polynomial=[self.prior[x]]
            for j,report in enumerate(h):
                i=self.order[j];node=h[:j]
                if x[i]==0:
                    factor=[F(0) if report else F(1)]
                else:
                    power=1 if powers is None else powers[node]
                    factor=[q[node]]+[F(0)]*(power-1)+[1-2*q[node]]
                    if not report:
                        factor=[1-factor[0]]+[-a for a in factor[1:]]
                polynomial=pmul(polynomial,factor)
            mass[x]=polynomial
        degree=next(d for d in range(max(map(len,mass.values())))
                    if sum(v[d] if d<len(v) else 0 for v in mass.values())!=0)
        denominator=sum(v[degree] if degree<len(v) else 0 for v in mass.values())
        return {x:(v[degree] if degree<len(v) else F(0))/denominator for x,v in mass.items()}

    def d_probability(self,x,h,q,rho):
        """Enumerate actual future message paths, conditional on full state x."""
        if len(h)==self.n:return rho[h]
        i=self.order[len(h)]
        if x[i]==0:return self.d_probability(x,h+(0,),q,rho)
        a=q[h]
        return ((1-a)*self.d_probability(x,h+(0,),q,rho)
                +a*self.d_probability(x,h+(1,),q,rho))

    def receiver_gain(self,belief,e):
        return sum(w*((self.B if all(x) else -self.A)-e) for x,w in belief.items())

    def sender_gain(self,q,rho,h,belief=None):
        i=self.order[len(h)]
        belief=self.belief(q,h,own=1) if belief is None else belief
        report=sum(w*self.d_probability(x,h+(1,),q,rho) for x,w in belief.items())
        silent=sum(w*self.d_probability(x,h+(0,),q,rho) for x,w in belief.items())
        return self.eta[i]*(report-silent)-self.k[i]

    def assessment(self,q,rho,e):
        require(set(q)==set(self.nodes) and set(rho)==set(self.terminals),'complete behavior profile')
        require(all(0<=a<=1 for a in list(q.values())+list(rho.values())),'behavior probabilities')
        e=F(e); require(e>=0,'nonnegative fine')
        failures=[];sender=[];receiver=[]
        for h in self.terminals:
            mu=self.belief(q,h);gain=self.receiver_gain(mu,e);a=rho[h]
            receiver.append((h,gain))
            if (a>0 and gain<0) or (a<1 and gain>0):failures.append(('receiver',h,gain))
        for h in self.nodes:
            gain=self.sender_gain(q,rho,h);a=q[h];sender.append((h,gain))
            if (a>0 and gain<0) or (a<1 and gain>0):failures.append(('sender',h,gain))
        silent=all(q[(0,)*j]==0 for j in range(self.n)) and rho[(0,)*self.n]==0
        return {'equilibrium':not failures,'target':silent,'failures':failures,
                'sender_gains':sender,'receiver_gains':receiver}

    def pure_equilibria(self,e):
        """Exhaust ALL sender plans and all receiver best replies, including ties."""
        checked=0;equilibria=[]
        for actions in product((F(0),F(1)),repeat=len(self.nodes)):
            q=dict(zip(self.nodes,actions))
            choices=[]
            for h in self.terminals:
                gain=self.receiver_gain(self.belief(q,h),F(e))
                choices.append((F(1),) if gain>0 else (F(0),) if gain<0 else (F(0),F(1)))
            for replies in product(*choices):
                rho=dict(zip(self.terminals,replies));checked+=1
                audit=self.assessment(q,rho,e)
                if audit['equilibrium']:equilibria.append((q,rho,audit))
        return equilibria,checked

    def backward_candidate(self,e):
        """Primitive tree best replies with silence ties, followed by full audit.

        Receiver initialized by actual Bayes limits of an all-silent profile.
        In the declared domain its reply is invariant (proved separately).
        No suffix formula or product-of-future-probabilities shortcut is used.
        """
        q={h:F(0) for h in self.nodes}
        rho={h:F(self.receiver_gain(self.belief(q,h),F(e))>0) for h in self.terminals}
        for h in reversed(self.nodes):q[h]=F(self.sender_gain(q,rho,h)>0)
        audit=self.assessment(q,rho,e)
        require(audit['equilibrium'],'backward construction failed full game audit')
        return q,rho,audit


def encode_profile(q):
    return {''.join(map(str,h)):str(v) for h,v in q.items()}
