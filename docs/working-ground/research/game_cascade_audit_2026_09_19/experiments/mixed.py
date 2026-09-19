"""Exact mixed-equilibrium existence from state/path payoffs, NOT cascade tests.

Uses unique consistent-belief unnormalized weights proved in math/AUDIT.md.
All receiver decisions and positive-type sender decisions remain variables.
"""
import z3
from game import Game


def solve(game,e,timeout=30000):
    real=lambda x:z3.RealVal(str(x))
    q={h:z3.Real('q_'+(''.join(map(str,h)) or 'root')) for h in game.nodes}
    rho={h:z3.Real('D_'+''.join(map(str,h))) for h in game.terminals}
    solver=z3.SolverFor('QF_NRA');solver.set(timeout=timeout)
    for v in list(q.values())+list(rho.values()):solver.add(v>=0,v<=1)
    for j in range(game.n):solver.add(q[(0,)*j]==0)
    solver.add(rho[(0,)*game.n]==0)

    def weight(x,h,own=None):
        if own is not None and x[game.order[len(h)]]!=own:return real(0)
        # The own-type prior cancels on normalization. Keep it to match the
        # state-enumerating checker; every own type has strictly positive mass.
        value=real(game.prior[x])
        for j,report in enumerate(h):
            bit=x[game.order[j]]
            if report:
                if not bit:return real(0)
                # common q[h[:j]] factors cancel BEFORE limits, including q=0
            elif bit:value*=1-q[h[:j]]
        return value

    def prob_d(x,h):
        if len(h)==game.n:return rho[h]
        if not x[game.order[len(h)]]:return prob_d(x,h+(0,))
        return (1-q[h])*prob_d(x,h+(0,))+q[h]*prob_d(x,h+(1,))

    def best_reply(v,gain):
        gain=z3.simplify(gain)
        solver.add(z3.Implies(v>0,gain>=0),z3.Implies(v<1,gain<=0))

    for h in game.terminals:
        gain=sum(weight(x,h)*real((game.B if all(x) else -game.A)-e) for x in game.states)
        best_reply(rho[h],gain)
    for h in game.nodes:
        i=game.order[len(h)]
        gain=sum(weight(x,h,1)*(real(game.eta[i])*(prob_d(x,h+(1,))-prob_d(x,h+(0,)))-real(game.k[i]))
                 for x in game.states)
        best_reply(q[h],gain)
    answer=solver.check()
    if answer==z3.unknown:raise RuntimeError('Mixed game check incomplete: '+solver.reason_unknown())
    if answer==z3.unsat:return {'exists':False,'model':None}
    model=solver.model()
    values={str(v):str(model.eval(v,model_completion=True)) for v in list(q.values())+list(rho.values())}
    return {'exists':True,'model':values}
