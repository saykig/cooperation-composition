"""Exact replay, binary round trips and hostile-source controls."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import random
from codec import encode,decode,rank_sequence,unrank_sequence,level_parameters
from verify import verify,downward_polygon,contained

counts = {}
def check(ok,tag):
    if not ok:
        raise ValueError(tag)
    counts[tag] = counts.get(tag,0)+1

def main():
    for m in range(1,6):
        for s in range(6):
            seen = set()
            for z in product(range(s+1),repeat=m):
                if sum(z)>s:
                    continue
                r = rank_sequence(z,s)
                check(unrank_sequence(r,m,s)==list(z),'combinatorial_roundtrip')
                seen.add(r)
            check(seen==set(range(comb(m+s,m))),'complete_rank_range')
    fixtures = {
        'singleton':[(F(1,3),F(2,5))],
        'horizontal':[(F(1,4),F(1,2)),(F(1,2),F(1,2))],
        'vertical':[(F(1,2),F(1,4)),(F(1,2),F(1,2))],
        'diagonal_segment':[(F(1,4),F(1,2)),(F(1,2),F(1,4))],
        'increasing_segment':[(F(1,4),F(1,4)),(F(1,2),F(1,2))],
        'corner':[(F(1,8),F(3,4)),(F(1,2),F(2,3)),(F(3,4),F(1,8))],
        'tiny_corner':[(F(1,8),F(3,4)),(F(3,4)-F(1,2**60),F(2,3)),
                       (F(3,4),F(1,8))],
        'parabola':[(F(1,4)+F(j,160),F(3,5)-(F(1,4)+F(j,160))**2)
                    for j in range(25)],
        'box':list(product((F(1,8),F(3,4)),repeat=2)),
    }
    rng = random.Random(162109)
    for i in range(12):
        fixtures['random_'+str(i)] = [(F(rng.randrange(8,49),64),F(rng.randrange(8,49),64))
                                      for _ in range(12)]
    rows = []
    for name,source in fixtures.items():
        for b in (5,6,7):
            blob,meta = encode(source,b)
            decoded_b,points = decode(blob)
            check(decoded_b==b,'accuracy_header')
            check(verify(source,points,F(1,1 << b)),'continuum_sandwich')
            check(len(points)==(1 << (b+3))+1,'expanded_length')
            # Exact order/permutation/duplicate invariance.
            other,_ = encode(list(reversed(source))+source[:1],b)
            check(other==blob,'canonical_source_order')
            for broken in (blob[:-1],bytes([blob[0]^1])+blob[1:],blob+b'\0'):
                try:
                    decode(broken)
                    rejected = False
                except ValueError:
                    rejected = True
                check(rejected,'malformed_stream_rejection')
            # A self-contained encoding is not a proof relative to another source.
            wrong = [(F(1,8),F(1,8))]
            check(not verify(wrong,points,F(1,1 << b)),'wrong_source_rejection')
            check(not verify(source,wrong,F(1,1 << b)),'false_upper_inclusion_rejection')
            bad = [(F(7,8),F(7,8))]+points
            check(not verify(source,bad,F(1,1 << b)),'illegal_vertex_rejection')
            # Use a valid-domain invented high point, testing geometric inclusion.
            if name!='box':
                check(not verify(source,[(F(3,4),F(3,4))],F(1,1 << b)),
                      'false_lower_inclusion_rejection')
            rows.append({'fixture':name,'b':b,'payload_bits':8*len(blob),
                         'expanded_points':len(points),
                         'source_coordinate_max_bits':max(max(x.numerator.bit_length(),
                         x.denominator.bit_length()) for p in source for x in p)})
            if name=='parabola' and b==7:
                Path(__file__).with_name('sample.bin').write_bytes(blob)
    # Count exact format sizes separately from experimental compression factors.
    rates = []
    for b in range(5,13):
        length = 8+(2*b.bit_length()-1)+4*(b+3)
        length += sum(level_parameters(b,j)[-1] for j in range(b+3))
        rates.append({'b':b,'meaningful_bits':length,'bits_times_sqrt_epsilon':
                      round(length*2**(-b/2),6)})
    paths = ['codec.py','verify.py','check_codec.py','foundation_audit.py','sample.bin']
    hashes = {p:hashlib.sha256(Path(__file__).with_name(p).read_bytes()).hexdigest() for p in paths}
    print(json.dumps({'status':'pass','arithmetic':'fractions.Fraction',
                      'counts':counts,'total':sum(counts.values()),'fixtures':rows,
                      'format_size_checks':rates,'sha256':hashes,
                      'scope':'finite exact checks; no Lean or independent human review'},
                     indent=2,sort_keys=True))

if __name__=='__main__':
    main()
