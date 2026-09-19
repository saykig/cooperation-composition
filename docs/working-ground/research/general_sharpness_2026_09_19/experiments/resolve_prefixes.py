"""Optimize the 20 historical unresolved prefixes; certify witnesses and bounds."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time,platform
import numpy as np
import scipy
from scipy.optimize import minimize,linprog
from exact import require,ratios,margin_certificate

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'two_prefix_selection_2026_09_19/experiments/sharpness-results.json'


def solve(prefix):
    m=5;q=F(4,5);tau=F(9999,10000);budget=F(12);p0=F(999,1000)
    r=[q**(m-i) for i in range(m)]+[F(1,1000)]
    remaining=set(range(m+1));rows=[];constant=[]
    for i in prefix:
        remaining.remove(i)
        rows.append([int(j in remaining) for j in range(1,m+1)])
        constant.append((np.log(float(p0)) if 0 in remaining else 0)-np.log(float(r[i])))
    M=np.array(rows,dtype=float);constant=np.array(constant)
    weights=np.arange(1,m+1,dtype=float)
    def f(x):return M@np.log(x[:m])+constant
    def c(x):return f(x)-x[-1]
    def cj(x):return np.column_stack((M/x[:m],-np.ones(len(prefix))))
    result=minimize(lambda x:-x[-1],np.array([.8]*m+[-.1]),jac=lambda x:np.array([0.]*m+[-1.]),
                    method='SLSQP',bounds=[(1e-10,float(tau))]*m+[(None,None)],
                    constraints=[{'type':'eq','fun':lambda x:weights@x[:m]-12,
                                  'jac':lambda x:np.r_[weights,0.]},
                                 {'type':'ineq','fun':c,'jac':cj}],
                    options={'ftol':1e-12,'maxiter':2000})
    require(result.success,'optimizer failed: '+str(result.message))
    # Blend off the closed upper boundary, rationalize four coordinates, and
    # solve the affine equation EXACTLY for the fifth coordinate.
    lamix=1e-7
    x=(1-lamix)*result.x[:m]+lamix*.8
    p=[p0]+[F(round(float(y)*10**10),10**10) for y in x[:m-1]]
    p.append((budget-sum(j*p[j] for j in range(1,m)))/m)
    require(all(0<y<tau for y in p) and sum(j*p[j] for j in range(1,m+1))==budget)
    require(all(x>1 for x in ratios(p,r,prefix)),'candidate lacks exact positive margin')
    # Optimize tangent mixture to locate a tight global upper certificate.
    z=np.array([float(y) for y in p[1:]])
    J=M/z
    fz=M@np.log(z)+constant
    k=len(prefix)
    objective=np.r_[fz-J@z,12.,np.full(m,float(tau))]
    A=np.column_stack((J.T,-weights,-np.eye(m)))
    dual=linprog(objective,A_ub=A,b_ub=np.zeros(m),A_eq=np.array([[1.]*k+[0.]*(m+1)]),
                 b_eq=[1.],bounds=[(0,None)]*k+[(None,None)]+[(0,None)]*m,method='highs')
    require(dual.success,'dual optimizer failed')
    lam=[F(max(0.,float(v))).limit_denominator(10**8) for v in dual.x[:k]]
    total=sum(lam);lam=[v/total for v in lam]
    certificate=margin_certificate(p,r,prefix,lam,tau,budget)
    require(F(certificate['log_margin_lower'])>0)
    return {'prefix':list(prefix),'optimizer':{'success':bool(result.success),
                'message':str(result.message),'iterations':int(result.nit),
                'numerical_margin':float(result.x[-1]),'point':list(map(float,result.x[:m])),
                'affine_residual':float(weights@result.x[:m]-12),
                'minimum_constraint_residual':float(min(c(result.x)))},
            'rational_witness':list(map(str,p)),'certificate':certificate}


def main():
    start=time.perf_counter();old=json.loads(SOURCE.read_text())
    pending=old['higher_dimensions'][1]['missing_prefixes']
    require(len(pending)==20 and all(x[0]==0 for x in pending))
    results=[solve(p) for p in pending]
    print(json.dumps({'status':'all 20 certified defeated','indexing':'zero-based',
        'input':{'m':5,'q':'4/5','p0':'999/1000','tau':'9999/10000','weighted_sum':'12'},
        'results':results,'elapsed_seconds':time.perf_counter()-start,
        'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
        'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'exact.py',SOURCE]},
        'scope':'Numerical maximizers locate candidates; rational products and tangent/series bounds certify strict feasibility and supremum brackets.'},indent=2))

if __name__=='__main__':main()
