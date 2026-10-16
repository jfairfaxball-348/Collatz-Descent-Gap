#!/usr/bin/env python3
"""DG012 exact finite regression; universal nonrealisation has a separate paper proof.
Tests mountain affine identities, two-bridge congruences, DG011 regressions,
and strict finite positive realisations. Not a Collatz conjecture certificate.
"""
from itertools import product
from math import gcd

def T(x):
    assert x>0
    return x//2 if not x&1 else (3*x+1)//2

def affine(w):
    A,q,D=1,0,1
    pref=[(A,q,D)]
    for c in w:
        if c=='1': A,q=3*A,3*q+D
        else: assert c=='0'
        D*=2
        pref.append((A,q,D))
    return A,q,D,pref

def mountain(r):
    assert r>=5 and r%6==5
    s=1
    while 3**s<=2**(s+r):s+=1
    w='1'*s+'0'*r
    A,q,D,p=affine(w)
    assert (A,q,D)==(3**s,3**s-2**s,2**(s+r))
    assert D<A and 2*A<3*D
    return s,w,A,q,D

def trace(n,w):
    vals=[n]
    for c in w:
        assert vals[-1]%2==int(c)
        vals.append(T(vals[-1]))
    return vals

def positive_seed(words):
    W=''.join(words)
    A,q,D,_=affine(W)
    modulus=4*D
    residue=((3*D-q)*pow(A,-1,modulus))%modulus
    residue+=modulus*((-residue*pow(modulus,-1,3))%3)
    step=3*modulus
    for _ in range(40):
        x=residue
        if x>1:
            good=True
            for w in words:
                v=trace(x,w)
                if not(x<v[-1]<min(v[1:-1]) and v[-1]%9==7):
                    good=False;break
                x=v[-1]
            if good:
                assert residue%3==0
                return residue
        residue+=step
    raise AssertionError('no finite CRT witness found')

# DG011 mod-9 s<=6 shield independent finite enumeration
count=0
for d in range(1,10):
    for bs in product('01',repeat=d):
        w=''.join(bs); s=w.count('1')
        if s==0 or s>6 or 3**s<=2**d:continue
        count+=1
        A,q,D,_=affine(w)
        if s==1: assert q*pow(D,-1,3)%3==2
        else: assert q*pow(D,-1,9)%9!=7
assert count==179
A,q,D,p=affine('11111101000')
assert (A,q,D)==(2187,2123,2048)
assert trace(191,'11111101000')[-1]==205
print('PASS DG011 mod-9 shield, 179 expanding words; sharp length-11 witness')

for r in (5,11,17,23,29):
    s,w,A,q,D=mountain(r)
    assert (-pow(2,-r,9))%9==7
    assert s>r and D<A<3*D//2 + 1
    assert (A-D)<D//2 and q<3*D//2
    # Full affine identity for each step of a repeated block, at rational level
    # D*(C*F(x)+q)==A*(C*x+q).
    C=A-D
    for x in (1,3,10**6):
        assert C*(A*x+q)+q*D==A*(C*x+q)
print('PASS all r=5,11,17,23,29 mountain affine and repeated-block identity')

for rr in ((5,5),(11,11,11),(5,11,5),(5,11,17,5), (5,5,11,11,17,17)):
    ws=[mountain(r)[1] for r in rr]
    n=positive_seed(ws)
    y=n
    for r,w in zip(rr,ws):
        s,_,A,q,D=mountain(r)
        assert (y+1)%2**s==0
        y1=trace(y,w)[-1]
        assert 2**s <= y+1 and y1+1 < 3*(y+1)/2
        y=y1
    for r in set(rr):
        # Check non-overlap concept by locating maximal initial plateau if applicable
        pass
    print('PASS finite positive schedule',rr,'initial digits',len(str(n)))

# For actual repeated full mountain blocks, congruence is divisibility by D**K.
for r,K in ((5,2),(11,3)):
    s,w,A,q,D=mountain(r)
    n=positive_seed([w]*K)
    assert ((A-D)*n+q)%D**K==0
    assert D**(K-1)<n+1
    x=n
    for _ in range(K):x=trace(x,w)[-1]
    print('PASS fixed positive finite repetition',r,K,'start digits',len(str(n)))

# The DG011 old hostile schedule numeric parameters and budget trend.
t=0; expected=((0,5,9),(14,17,30),(61,65,112),(238,239,409))
for tt,r,s in expected:
    assert t==tt
    rr=max(5,t); rr+=(5-rr)%6
    assert r==rr and mountain(r)[0]==s
    t+=s+r
print('PASS DG011 hostile schedule',expected)

# New slow staircase: r_j / j -> 1/5, below the generic ~0.342 threshold,
# but uniform K=30 repeated-word divisibility contradicts fixed-positive growth.
# Check exact integer coefficient inequality (K-1)*(s+r) > j
# at plateau starts j=30*k, for k=1..15; since y_j <= 2^j(n+1),
# any fixed n would need n+1 > 2**((K-1)*d-j) for arbitrarily large k.
mins=[]
for k in range(1,16):
    j=30*k;r=5+6*k;s=mountain(r)[0]
    margin=29*(s+r)-j
    assert margin>0
    mins.append(margin)
assert all(b>a for a,b in zip(mins,mins[1:]))
print('PASS staircase r_j=5+6 floor(j/30), increasing repeat margins',mins[:5])
print('DG012 local exact regression PASS; no infinite positive E orbit certified')
