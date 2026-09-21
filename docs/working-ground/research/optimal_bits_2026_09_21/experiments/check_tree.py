"""Exact max-sum budget replay against global label enumeration."""
from fractions import Fraction as F
from itertools import product
import json
import random

def solve_tree(neighbors,tables,alphabet):
    def visit(v,parent):
        children = [w for w in neighbors[v] if w!=parent]
        messages = {w:visit(w,v) for w in children}
        out = {}
        for parent_label in (alphabet if parent is not None else (None,)):
            values = []
            for labels,cost in tables[v].items():
                binding = dict(zip(neighbors[v],labels))
                if parent is not None and binding[parent]!=parent_label:
                    continue
                child_values = [messages[w][binding[w]] for w in children]
                if all(value is not None for value in child_values):
                    values.append(cost+sum(child_values,F(0)))
            out[parent_label] = max(values) if values else None
        return out
    return visit(0,None)[None]

def brute(edges,neighbors,tables,alphabet):
    values = []
    for labels in product(alphabet,repeat=len(edges)):
        binding = {}
        for (u,v),label in zip(edges,labels):
            binding[u,v] = binding[v,u] = label
        costs = []
        for v in range(len(neighbors)):
            key = tuple(binding[v,w] for w in neighbors[v])
            if key not in tables[v]:
                break
            costs.append(tables[v][key])
        else:
            values.append(sum(costs,F(0)))
    return (max(values) if values else None),len(values)

def main():
    rng = random.Random(20260921)
    total,empty,assignments = 0,0,0
    for n in range(1,8):
        for alphabet_size in (2,3):
            alphabet = tuple(range(alphabet_size))
            for trial in range(12):
                edges = [(v,rng.randrange(v)) for v in range(1,n)]
                neighbors = [[] for _ in range(n)]
                for u,v in edges:
                    neighbors[u].append(v)
                    neighbors[v].append(u)
                tables = []
                for adj in neighbors:
                    table = {}
                    for labels in product(alphabet,repeat=len(adj)):
                        if rng.randrange(4)!=0:
                            table[labels] = F(rng.randrange(17),32)
                    tables.append(table)
                expected,count = brute(edges,neighbors,tables,alphabet)
                actual = solve_tree(neighbors,tables,alphabet)
                if actual!=expected:
                    raise ValueError((n,alphabet_size,trial,actual,expected))
                total += 1
                empty += expected is None
                assignments += count
    print(json.dumps({'status':'pass','arithmetic':'fractions.Fraction',
                      'tree_instances':total,'globally_empty_instances':empty,
                      'compatible_assignments_enumerated':assignments,
                      'scope':'error-budget dynamic program; not order optimization'},
                     sort_keys=True,indent=2))

if __name__=='__main__':
    main()
