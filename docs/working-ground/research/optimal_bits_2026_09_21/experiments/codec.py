"""Uniform rational multiscale bit codec. Standard library only.

The source is a convex hull of rational points. The output is an actual byte
string; up to seven zero padding bits are charged. See math/PLANAR_RATE.md.
"""
from fractions import Fraction as F
from math import comb
from bisect import bisect_right

MAGIC = '10110110'

def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def frontier(vertices):
    # Drop dominated points by a right-to-left record scan, then take upper hull.
    points = sorted(set(tuple(map(F,p)) for p in vertices), reverse=True)
    records, best = [], F(-1)
    for p in points:
        if p[1] > best:
            records.append(p)
            best = p[1]
    chain = []
    for p in reversed(records):
        while len(chain)>1 and cross(chain[-2],chain[-1],p)>=0:
            chain.pop()
        chain.append(p)
    if not chain:
        raise ValueError('empty source')
    return chain

def parameterize(chain):
    lengths = [F(0)]
    for a,b in zip(chain,chain[1:]):
        lengths.append(lengths[-1]+b[0]-a[0]+a[1]-b[1])
    total = lengths[-1]
    def evaluate(t):
        if total == 0:
            return chain[0]
        s = t*total
        if s == total:
            return chain[-1]
        i = bisect_right(lengths,s)-1
        lam = (s-lengths[i])/(lengths[i+1]-lengths[i])
        return tuple((1-lam)*a+lam*b for a,b in zip(chain[i],chain[i+1]))
    return evaluate

def level_parameters(b,j):
    a = 1+abs(j-b//2)
    exponent = b+4+2*(a-1).bit_length()
    delta = F(1,1 << exponent)
    m = 1 << j
    s = (F(1,m)/delta).__floor__()
    number = comb(m+s,m)
    width = (number-1).bit_length()
    return delta,m,s,number,width

def rank_sequence(z, limit):
    if any(x<0 for x in z) or sum(z)>limit:
        raise ValueError('coefficient budget')
    partial, rank = 0,0
    for i,value in enumerate(z):
        partial += value
        rank += comb(partial+i,i+1)
    return rank

def unrank_sequence(rank,m,s):
    if not 0<=rank<comb(m+s,m):
        raise ValueError('unused rank')
    bars = [0]*m
    ceiling = m+s-1
    for k in range(m,0,-1):
        lo,hi = k-1,ceiling
        while lo<hi:
            mid = (lo+hi+1)//2
            if comb(mid,k)<=rank:
                lo = mid
            else:
                hi = mid-1
        bars[k-1] = lo
        rank -= comb(lo,k)
        ceiling = lo-1
    z, previous = [], -1
    for bar in bars:
        z.append(bar-previous-1)
        previous = bar
    if rank or sum(z)>s:
        raise ValueError('invalid composition')
    return z

def integer_bits(value,width):
    if not 0<=value<(1 << width):
        raise ValueError('field overflow')
    return format(value, f'0{width}b') if width else ''

def encode(vertices,b):
    if not isinstance(b,int) or b<1:
        raise ValueError('positive accuracy exponent required')
    vertices = [tuple(map(F,p)) for p in vertices]
    if any(len(p)!=2 or not all(0<x<1 for x in p) for p in vertices):
        raise ValueError('source outside open unit square')
    f = parameterize(frontier(vertices))
    header = bin(b)[2:]
    pieces = [MAGIC,'0'*(len(header)-1),header]
    for p in [f(F(0)),f(F(1))]:
        for x in p:
            pieces.append(integer_bits((x*(1 << (b+3))).__floor__(),b+3))
    stats = []
    for j in range(b+3):
        delta,m,s,number,width = level_parameters(b,j)
        z = []
        for k in range(m):
            left,right,mid = f(F(k,m)),f(F(k+1,m)),f(F(2*k+1,2*m))
            cx = mid[0]-(left[0]+right[0])/2
            cy = mid[1]-(left[1]+right[1])/2
            if cx<0 or cx!=cy:
                raise ValueError('source curvature invariant')
            z.append((cx/delta).__floor__())
        rank = rank_sequence(z,s)
        pieces.append(integer_bits(rank,width))
        stats.append({'level':j,'slots':m,'budget':s,'nonzero':sum(x>0 for x in z),
                      'bits':width})
    bits = ''.join(pieces)
    meaningful = len(bits)
    bits += '0'*(-len(bits)%8)
    payload = int(bits,2).to_bytes(len(bits)//8,'big')
    return payload,{'b':b,'meaningful_bits':meaningful,'stored_bits':len(bits),
                    'levels':stats}

class Reader:
    def __init__(self,payload):
        self.bits = ''.join(format(x,'08b') for x in payload)
        self.pos = 0
    def take(self,n):
        if self.pos+n>len(self.bits):
            raise ValueError('truncated stream')
        value = self.bits[self.pos:self.pos+n]
        self.pos += n
        return int(value,2) if n else 0

def decode(payload):
    r = Reader(payload)
    if r.take(8)!=int(MAGIC,2):
        raise ValueError('bad format')
    zeros = 0
    while r.take(1)==0:
        zeros += 1
    b = (1 << zeros)+r.take(zeros)
    endpoints = [tuple(F(r.take(b+3),1 << (b+3)) for _ in range(2)) for _ in range(2)]
    points = endpoints
    for j in range(b+3):
        delta,m,s,number,width = level_parameters(b,j)
        z = unrank_sequence(r.take(width),m,s)
        new = []
        for k in range(m):
            new.append(points[k])
            new.append(tuple((a+c)/2+delta*z[k] for a,c in zip(points[k],points[k+1])))
        new.append(points[-1])
        points = new
    padding = r.bits[r.pos:]
    if len(padding)>7 or any(x!='0' for x in padding):
        raise ValueError('noncanonical padding')
    return b,points
