"""Hand-designed edge cases; no tolerance separates ties from strict feasibility."""
from fractions import Fraction as F


def instance(vertices, r, tau='2/3'):
    return {'vertices': [[str(x) for x in v] for v in vertices],
            'r': list(map(str, r)), 'tau': tau}


def cases():
    triangle = instance([
        ['99/100', '1/100', '9/10', '299/300'],
        ['99/100', '3/4', '49/50', '209/300'],
        ['99/100', '47/50', '63/100', '13/15']],
        ['64/125', '16/25', '4/5', '1/100'], '999/1000')
    segment = [['1/2', '1/5', '3/5'], ['1/2', '3/5', '1/5']]
    # A genuine polygon, not just a mislabeled segment. The same hidden interior
    # product maximum persists while p1 varies independently.
    rectangle = [[p, a, b] for p in ['49/100', '51/100']
                 for a, b in [('1/5', '3/5'), ('3/5', '1/5')]]
    changing = [['13/20', '3/5', '1/5'], ['13/20', '3/80', '13/20']]
    eps = F(1, 10**30)
    return {
        'triangle_three': (triangle, 'zero', 3),
        'vertex_miss_polygon': (instance(rectangle, ['3/20', '1/10', '1/10']), 'positive', None),
        'vertex_miss_segment': (instance(segment, ['3/20', '1/10', '1/10']), 'positive', None),
        'tangent_polygon': (instance(rectangle, ['4/25', '1/10', '1/10']), 'zero', 1),
        'narrow_segment': (instance(segment[::-1], [F(4,25)-eps**2, F(2,5), F(1,10)]), 'zero', 1),
        'changing_blocker': (instance(changing, ['7/50', '2/5', '1/10']), 'zero', 2),
        'distinct_witnesses': (instance([['1/10','3/5'], ['3/5','1/10']], ['2/5','3/10']), 'positive', None),
        'point_tie': (instance([['1/2','2/5','3/10']], ['3/25','1/100','1/100']), 'zero', 1),
        'point_strict': (instance([['1/2','2/5','3/10']], ['1/100']*3), 'positive', None),
        'one_sender_tie': (instance([['1/2']], ['1']), 'zero', 1),
        'one_sender_strict': (instance([['1/2']], ['1/2']), 'positive', None),
        'duplicate_collinear': (instance(segment+[segment[0], ['1/2','2/5','2/5']], ['4/25','1/10','1/10']), 'zero', 1),
        'endpoint_tie': (instance([['1/5','1/5'], ['1/5','3/5']], ['3/5','1/10']), 'zero', 1),
        'polygon_all_ties': (instance([['1/5','1/5','1/5'],['3/5','1/5','1/5'],['1/5','3/5','1/5']], ['1','1','1']), 'zero', 1),
    }
