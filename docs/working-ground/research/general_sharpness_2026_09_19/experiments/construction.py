"""Explicit arbitrary-dimension rational sharpness construction (m=d+1>=2)."""
from fractions import Fraction as F
from exact import require,ratios


def parameters(m):
    require(type(m) is int and m>=2)
    C=F(m*(m+1),2)
    kappa=1/(8*m*(C+1))
    gamma=1/(2*(C+1))
    epsilon=gamma/(m*(m+1))
    q=1-epsilon
    return {'m':m,'C':C,'kappa':kappa,'gamma':gamma,'epsilon':epsilon,
            'q':q,'tau':1-epsilon*kappa/2,
            'r':[q**(m-i) for i in range(m)]+[q**(m+1)]}


def from_deficits(par,x):
    return [1-par['epsilon']*par['kappa']]+[1-par['epsilon']*v for v in x]


def witness(m,prefix):
    par=parameters(m);C=par['C'];kappa=par['kappa']
    require(len(prefix)==m-1 and len(set(prefix))==m-1 and all(0<=i<=m for i in prefix))
    base=[F(0)]*m
    if prefix[0]!=0:
        base[prefix[0]-1]=C/prefix[0]
        method={'case':'nonzero_first','absorbing_sender':prefix[0]}
    else:
        records=[];last=0
        for i in prefix[1:]:
            if i>last:records.append(i);last=i
        if last<m:records.append(m)
        last=0;raw=[F(0)]*m
        for j in records:
            raw[j-1]=F(j-last);last=j
        W=sum((i+1)*v for i,v in enumerate(raw))
        require(W>=C+1)
        base=[C*v/W for v in raw]
        method={'case':'zero_first','records':records,'weighted_record_sum':str(W)}
    x=[(1-kappa)*v+kappa for v in base]
    p=from_deficits(par,x)
    return p,x,method


def dimension_points(m):
    par=parameters(m);x=[F(1)]*m
    out=[from_deficits(par,x)]
    for i in range(1,m):
        y=x.copy();y[i-1]+=F(1,4);y[m-1]-=F(i,4*m)
        out.append(from_deficits(par,y))
    return out


def check_witness(m,prefix):
    par=parameters(m);p,x,method=witness(m,prefix)
    require(all(0<v<par['tau'] for v in p),'probability bounds')
    require(sum((i+1)*v for i,v in enumerate(x))==par['C'],'affine deficit constraint')
    require(sum(i*p[i] for i in range(1,m+1))==par['q']*par['C'],'probability slice')
    require(all(par['kappa']<=v<=par['C'] for v in x),'deficit bounds')
    remaining=set(range(m+1));bounds=[]
    for i in prefix:
        remaining.remove(i)
        S=sum(par['kappa'] if j==0 else x[j-1] for j in remaining)
        h=m-i if i<m else m+1
        require(S<=h-par['gamma'],'linear strict slack')
        bounds.append(h-S)
    rs=ratios(p,par['r'],prefix)
    require(all(v>1 for v in rs),'exact cascade inequality')
    # The uniform analytic lower bound on product minus threshold.
    require(all((v-1)*par['r'][i]>=par['epsilon']*par['gamma']/2
                for v,i in zip(rs,prefix)),'quantitative product slack')
    return p,x,method,bounds
