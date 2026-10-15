#!/usr/bin/env python3
"""DG009 exact certificates: conditional first-record inverse obstructions,
low-depth safe inverse uniqueness and finite 2-adic-cylinder stress tests.
No result here establishes an infinite positive Collatz exception.
"""
from itertools import product

U, V = '111011010', '111101010'


def T(x):
    assert x > 0
    return x//2 if x%2 == 0 else (3*x+1)//2


def prefixes(w):
    out = [(1, 0, 1)]
    A, q, D = 1, 0, 1
    for bit in w:
        if bit == '1':
            A, q = 3*A, 3*q+D
        else:
            assert bit == '0'
        D *= 2
        out.append((A, q, D))
    return out


def trace(x, w):
    seq = [x]
    for _ in w:
        seq.append(T(seq[-1]))
    assert ''.join(str(v % 2) for v in seq[:-1]) == w
    return seq


assert prefixes(U)[-1] == (729, 881, 512)
assert prefixes(V)[-1] == (729, 809, 512)
base = {U:(1959,2791),V:(1327,1891)}
for w,(a0,b0) in base.items():
    p = prefixes(w)
    assert all(A >= D for A,q,D in p)
    assert all(A*512 > 729*D for A,q,D in p[1:-1])
    for h in (0,1,2,9,40):
        a,b = a0+2048*h,b0+2916*h
        vs = trace(a,w)
        assert vs[-1] == b and a < b < min(vs[1:-1]) and a%4==b%4==3
        assert b%81 == (37 if w==U else 28)
print('PASS: u/v affine bridges and uniform strict local inequalities')

# Entire endpoint progressions, not a finite sample: any strictly
# prefix-safe inverse with at most six odd bits has length <=9,
# because 3**6 < 2**10. Mod 3**s integrality does not vary with h
# as 3**s divides 2916=4*3**6.
for orig,(_,b0) in base.items():
    hits = []
    tested = 0
    for d in range(1,10):
        for tup in product('01',repeat=d):
            w = ''.join(tup)
            p = prefixes(w)
            A,q,D = p[-1]
            if w.count('1')>6 or A<=D or not all(x>=z for x,y,z in p):
                continue
            tested += 1
            if (D*b0-q)%A == 0:
                hits.append(w)
    assert hits == [orig], (orig,hits)
    print('PASS: safe inverses with <=6 odd steps for',orig,':',hits,
          '(strict-safe candidates checked:',tested,')')

# h=h0+mod*k, k>=0.  Every new root is positive, prefix-safe,
# integral, of the correct parity cylinder, and strictly below a.
# Final two rows include least-record sources a divisible by 3.
rows = [
 (U, '1111011010', 1,3,2671,1336),
 (V, '1111101010', 2,3,3615,1808),
 (U, '110111011010', 5,9,10843,1356),
 (V, '110111101010', 0,9,1179,148),
 (U, '111101111001010', 9,81,16111,4280),
 (V, '111101111100010', 40,81,65775,17472),
]
for orig,w,h0,mod,root0,gap0 in rows:
    a0,b0 = base[orig]
    A,q,D = prefixes(w)[-1]
    assert A>D and all(Ai>=Di for Ai,qi,Di in prefixes(w))
    assert (D*(b0+2916*h0)-q)%A == 0
    assert (D*2916*mod)%A == 0
    dz = D*2916*mod//A
    assert dz % (2**len(w)) == 0
    assert dz < 2048*mod
    for k in (0,1,4):
        h=h0+mod*k
        a,b=a0+2048*h,b0+2916*h
        z=root0+dz*k
        assert z == (D*b-q)//A and 3<=z<a<b
        assert a-z == gap0+(2048*mod-dz)*k
        seq=trace(z,w)
        assert seq[-1] == b and min(seq) == z
    print('PASS alternative safe root',orig,w,
          'h=',h0,'+',mod,'k; z=',root0,'+',dz,'k')

# Genuine finite mixed positive bridge schedules with initial seed 0 mod3.
for words in product((U,V),repeat=3):
    W=''.join(words)
    A,q,D=prefixes(W)[-1]
    N=4*D
    r=((3*D-q)*pow(A,-1,N))%N
    h=(-r*pow(N,-1,3))%3
    seed=r+N*h
    if seed<3: seed+=3*N
    valid=False
    for k in range(30):
        a=seed+3*N*k
        x=a
        for w in words:
            vs=trace(x,w)
            if not (x<vs[-1]<min(vs[1:-1]) and vs[-1]%4==3):
                break
            x=vs[-1]
        else:
            valid=True
            break
    assert valid and a%3==0
print('PASS: eight finite 3-block schedules with starts 0 mod3')

# A positive orbit realising U^t at any block start x necessarily has
# 512^t | (217*x+881). Arithmetic check of four genuine finite prefixes.
assert 512**2 > 3**9
for t in range(1,5):
    W=U*t
    A,q,D=prefixes(W)[-1]
    m=4*D
    r=((3*D-q)*pow(A,-1,m))%m
    if r<3: r+=m
    trace(r,W)
    assert (217*r+881)%(512**t)==0
print('PASS: repeated-u divisibility identity t=1..4')
print('DG009 PASS: finite/algebraic certificates only, not E=empty.')
