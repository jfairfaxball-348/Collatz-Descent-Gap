#!/usr/bin/env python3
"""DG007 exact finite/algebraic regression; never certifies an infinite E-orbit.

Reproduces bridge-cylinder inequality decisions at every candidate word in
the listed lengths, safe inverse residue sieve, and positive-integer finite
concatenation counterexamples. E-theorems require the DG007 paper proofs.
"""
from fractions import Fraction
from itertools import product


def T(n):
    assert n >= 1
    return n // 2 if n % 2 == 0 else (3*n + 1)//2


def prefixes(word):
    A, q, D = 1, 0, 1
    p = [(A, q, D)]
    for bit in word:
        assert bit in '01'
        if bit == '1':
            A, q = 3*A, 3*q + D
        D *= 2
        p.append((A, q, D))
    return p


def trace(n, length):
    v = [n]
    for _ in range(length):
        v.append(T(v[-1]))
    return v


def finite_bridge(v):
    return (len(v) >= 4 and v[0] >= 3 and v[0] % 4 == v[-1] % 4 == 3
            and v[0] < v[-1] and min(v[1:-1]) > v[-1]
            and v[-2] == 2*v[-1])


def viable_word(word):
    """Exact decision for all sources in its 4*2^d endpoint cylinder.

    Each strict bridge condition is alpha*h + beta > 0 for h>=0.
    Rationals here certify full finite-word algebra, not an orbit in E.
    """
    p = prefixes(word)
    A, q, D = p[-1]
    M = 4*D
    a0 = (3*D-q)*pow(A, -1, M) % M
    if a0 < 3:
        a0 += M
    lower, upper = 0, None
    for i, (Ai, qi, Di) in enumerate(p[:-1]):
        alpha = Fraction(Ai*M, Di) - Fraction(A*M, D)
        beta = Fraction(Ai*a0+qi, Di) - Fraction(A*a0+q, D)
        if i == 0:
            alpha, beta = -alpha, -beta
        if alpha > 0:
            bound = -beta / alpha
            lower = max(lower, bound.numerator // bound.denominator + 1)
        elif alpha < 0:
            bound = -beta / alpha
            upper = bound if upper is None else min(upper, bound)
        elif beta <= 0:
            return None
    if upper is not None and lower >= upper:
        return None
    a = a0 + M*lower
    v = trace(a, len(word))
    assert finite_bridge(v)
    assert ''.join(str(x%2) for x in v[:-1]) == word
    assert v[-1] == (A*a+q)//D
    # All feasible words in this specified range are feasible for all h>=0.
    assert all((Fraction(A, D)-1 if i == 0 else
                Fraction(Ai, Di)-Fraction(A, D)) > 0
               for i, (Ai, qi, Di) in enumerate(p[:-1]))
    return (a, v[-1], v[-1] % 3, M, A*M//D)


expected = {
    3: ['110'], 4: [], 5: [], 6: ['111010', '111100'],
    7: [], 8: [],
    9: ['111011010', '111011100', '111101010', '111101100',
        '111110010', '111110100', '111111000'],
    10: [], 11: None, 12: [],
}
all_bridge = {}
checked_words = 0
for d in range(3, 13):
    good = {}
    for bits in product('01', repeat=d-3):
        word = '11'+''.join(bits)+'0'
        tested = viable_word(word)
        if tested is not None:
            good[word] = tested
        checked_words += 1
    assert (list(good) == expected[d] if expected[d] is not None
            else len(good) == 30), (d, good)
    all_bridge[d] = good
assert all_bridge[3]['110'][:2] == (27, 31)
assert all_bridge[6]['111010'][:2] == (71, 91)
assert all_bridge[6]['111100'][:2] == (207, 263)
assert [(w, data[:3]) for w, data in all_bridge[9].items()] == [
    ('111011010', (1959,2791,1)), ('111011100', (487,695,2)),
    ('111101010', (1327,1891,1)), ('111101100', (1903,2711,2)),
    ('111110010', (223,319,1)), ('111110100', (799,1139,2)),
    ('111111000', (63,91,1)),
]

alphabet = [w for d in (3, 6, 9) for w, e in all_bridge[d].items()
            if e[2] == 1]
assert len(alphabet) == 6
concatenations = 0
for depth in (1, 2, 3):
    for ws in product(alphabet, repeat=depth):
        word = ''.join(ws)
        A,q,D = prefixes(word)[-1]
        M=4*D
        n = (3*D-q)*pow(A,-1,M) % M
        if n < 3:
            n += M
        for w in ws:
            v = trace(n, len(w))
            assert finite_bridge(v)
            assert ''.join(str(x%2) for x in v[:-1]) == w
            assert v[-1]%3 == 1
            n=v[-1]
        concatenations += 1
assert concatenations == 258

offspine_examples = 0
for h in (0,1,7,99):
    a=223+2048*h
    b=319+2916*h
    z=(8*b-5)//9
    y=(4*b-1)//3
    assert trace(a,9)[-1]==b and finite_bridge(trace(a,9))
    assert 3 <= z < b < y < 2*b
    assert trace(z,3)==[z,y,2*b,b]
    assert z not in trace(a,9)
    offspine_examples += 1


def safe_words(bound):
    out=[]
    for d in range(1,bound+1):
        for bits in product('01', repeat=d-1):
            w='1'+''.join(bits)
            p=prefixes(w)
            if not all(A>=D for A,q,D in p[1:]):
                continue
            A,q,D=p[-1]
            if not A>D:
                continue
            r=q*pow(D,-1,A) % A
            out.append((w,r,A,q,D))
    return out


W9=safe_words(9)
W11=safe_words(11)
assert len(W9)==89 and len(W11)==281
M=3**7

def sieve(words):
    covered=bytearray(M)
    for w,r,mod,q,D in words:
        for i in range(r,M,mod):
            covered[i]=1
    return covered

old=sieve(W9)
new=sieve(W11)
assert sum(old)==1005 and sum(new)==1013
new_residues=[i for i in range(M) if new[i] and not old[i]]
assert new_residues==[205,325,919,991,1000,1090,1171,2170]
new_witness={205:'11111101000', 325:'11110101010',
             919:'11011101010', 991:'11111011000',
             1000:'11101101010', 1090:'11011011010',
             1171:'11101011010', 2170:'11110111000'}
for residue,w in new_witness.items():
    A,q,D=prefixes(w)[-1]
    assert A==2187 and D==2048
    assert (q*pow(D,-1,A))%A==residue
    m=residue if residue%2 else residue+M
    z=(D*m-q)//A
    assert z>=3 and z%2==1 and z<m
    v=trace(z,len(w))
    assert v[-1]==m and min(v)==z
    assert ''.join(str(x%2) for x in v[:-1])==w
    assert not old[residue]

assert trace(763,6)==[763,1145,1718,859,1289,1934,967]
assert finite_bridge(trace(207,6)) and trace(207,6)[-1]==263
assert finite_bridge(trace(2815,14)) and trace(2815,14)[-1]==3383
assert T(1503)==2255 and T(2255)==3383
for t in range(1,9):
    n=8**t-5
    assert ''.join(str(x%2) for x in trace(n,3*t)[:-1])=='110'*t
    assert min(trace(n,3*t))==n
for k in range(2,8):
    r=3**(k-1)
    assert (2**r+1)%3**k==0
    N=2**k*((2**r+1)//3**k)-1
    for h in (0,1,2,7,100):
        n=N+2**(k+r)*h
        v=trace(n,k+r)
        assert all(x%2==1 for x in v[:k])
        assert all(x%2==0 for x in v[k:k+r])
        assert v[-1]==1+3**k*h<n

print('Finite bridge words decided symbolically d=3..12:',checked_words)
print('Feasible local bridges by gap:',{d:len(v) for d,v in all_bridge.items()})
print('All-1-mod-3 finite bridge alphabet:',alphabet)
print('Positive integer concatenations tested:',concatenations)
print('Gap-9 off-spine 110 examples:',offspine_examples)
print('Strict-prefix safe words length<=9,<=11:',len(W9),len(W11))
print('Odd least-exception residues banned /2187: old',sum(old),'new',sum(new))
print('Eight newly banned classes:',new_residues)
print('DG002/DG005/DG006 finite regressions: PASS')
print('PASS — exact bounded/finite-word regression; E=empty remains OPEN')
