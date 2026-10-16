#!/usr/bin/env python3
"""DG016 finite exact checks; paper proofs are independent of these tests."""
from collections import defaultdict
from fractions import Fraction
from math import log2

def T(n):
    return n // 2 if n % 2 == 0 else (3*n+1) // 2

def orbit(n, steps):
    xs = [n]
    for _ in range(steps):
        xs.append(T(xs[-1]))
    return xs

def check_parity_collision(n, horizon=52, hmax=18):
    xs = orbit(n, horizon+hmax)
    pars = ''.join(str(x % 2) for x in xs)
    tested = 0
    for h in range(1,hmax+1):
        seen = defaultdict(list)
        for q in range(horizon+1):
            factor=pars[q:q+h]
            for p in seen[factor]:
                if xs[p]==xs[q]:
                    continue
                assert (xs[q]-xs[p]) % (1<<h) == 0, (n,p,q,h)
                assert (1 << (h+q)) < 3**q*(n+1), (n,p,q,h)
                tested+=1
            seen[factor].append(q)
    return tested

MORPH={'0':'012','1':'02','2':'1'}
R={'0':5,'1':11,'2':17}
def thue(h):
    s='0'
    while len(s)<h:
        s=''.join(MORPH[c] for c in s)
    return s[:h]

def mountain(r):
    assert r>=5 and r%6==5
    s=1
    while 3**s <= 2**(s+r):
        s+=1
    return '1'*s+'0'*r

def seed_for(word):
    a,b,D=1,0,1
    for c in word:
        if c=='1':
            a,b = 3*a,3*b+D
        D *= 2
    return (-b * pow(a,-1,D))%D + D

def mountain_collision(rs):
    words=[mountain(r) for r in rs]
    n=seed_for(''.join(words)); x=n; endpoints=[n]
    for word in words:
        a=x
        for j,b in enumerate(word):
            assert x%2==int(b)
            x=T(x)
            if j+1<len(word): assert x>a
        assert x>a
        endpoints.append(x)
    assert all(endpoints[j+1]+3 < Fraction(3,2)*(endpoints[j]+3) for j in range(len(rs)))
    count=0
    for h in range(1,len(rs)):
        for p in range(len(rs)-h+1):
            for q in range(p+1,len(rs)-h+1):
                if rs[p:p+h]!=rs[q:q+h]: continue
                L=sum(map(len,words[p:p+h]))
                delta=endpoints[q]-endpoints[p]
                assert delta>0 and delta%(1<<L)==0
                assert (1<<(L+q)) < 3**q*(n+3)
                count+=1
    return n.bit_length(),count

def champernowne_prefix(k):
    return ''.join(''.join(str((i//(3**j))%3) for j in range(w-1,-1,-1)) for w in range(1,k+1) for i in range(3**w))

total=sum(check_parity_collision(n) for n in range(2,112))
assert total>50000
print('PASS arbitrary finite orbits (n=2..111):',total,'distinct-state repeated-window inequalities')

params=[R[c] for c in thue(15)]
bits, pairs=mountain_collision(params)
assert pairs>0
print('PASS mountain finite positive seed: bit_length',bits,'separated-factor collisions',pairs)

word=champernowne_prefix(5)
for h in range(1,6):
    factors={word[i:i+h] for i in range(len(word)-h+1)}
    assert len(factors)==3**h
print('PASS full three-letter finite-factor complexity p(h)=3^h for h<=5')

xs=orbit(15,7)
assert xs==[15,23,35,53,80,40,20,10]
assert 20%3==2 and 20<T(15)
print('PASS finite-survival countermodel to applying least-E floor without infinite exception:',xs)

mu=log2(1.5)
print('slopes parity = %.9f; mountain (d_min=14) = %.9f' % (1/mu,14/mu))
print('DG016 finite checks PASS; no global Collatz claim.')
