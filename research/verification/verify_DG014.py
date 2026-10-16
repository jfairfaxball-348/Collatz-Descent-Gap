#!/usr/bin/env python3
"""DG014 finite exact checker; not a fixed infinite positive Collatz orbit proof."""
from fractions import Fraction
import sys
sys.set_int_max_str_digits(1000000)

H = {'0': '012', '1': '02', '2': '1'}

def thue_prefix(length):
    s = '0'
    while len(s) < length:
        s = ''.join(H[t] for t in s)
    return s[:length]

def r_schedule(length):
    s = thue_prefix(length)
    lookup = {'0':5, '1':11, '2':17}
    r = [lookup[c] for c in s]
    for k in range(100):
        j = 2 ** (k+8)
        if j >= length: break
        r[j] = 23+6*k
    return r

def assert_squarefree(word):
    n = len(word)
    for d in range(1,n//2+1):
        for j in range(n-2*d+1):
            assert word[j:j+d] != word[j+d:j+2*d], (j,d)

def affine(word):
    A,q,D = 1,0,1
    for bit in word:
        if bit == '1': A,q = 3*A,3*q+D
        else: assert bit == '0'
        D *= 2
    return A,q,D

def mountain(r):
    assert r>=5 and r%6==5
    s=1
    while 3**s <= 2**(s+r): s+=1
    assert 3**s > 2**(s+r) and 2*3**s < 3*2**(s+r)
    return '1'*s+'0'*r

def T(x):
    return x//2 if x%2==0 else (3*x+1)//2

def finite_seed(rs):
    words = [mountain(r) for r in rs]
    A,q,D = affine(''.join(words))
    modulus = 4*D
    n = ((3*D-q)*pow(A,-1,modulus))%modulus
    n += modulus*((-n*pow(modulus,-1,3))%3)
    for _ in range(30):
        if n>1:
            x=n
            good=True
            for w in words:
                v=[x]
                for bit in w:
                    if v[-1]%2 != int(bit):
                        good=False
                        break
                    v.append(T(v[-1]))
                if not good or not(x<v[-1]<min(v[1:-1])) or v[-1]%9 != 7:
                    good=False
                    break
                x=v[-1]
            if good:
                assert n%3==0
                return n,x,len(''.join(words))
        n += 3*modulus
    raise AssertionError('no finite witness found')

for N in (36,258,530):
    r=r_schedule(N)
    assert all(v>=5 and v%6==5 for v in r)
    assert_squarefree(r)
    n,b,d=finite_seed(r)
    assert b>n>0
    print('PASS squarefree finite strict witness',N,'bits',d,
          'seed_digits',len(str(n)),
          'spikes',[(j,r[j]) for j in (256,512) if j<N])

for r in range(5,9000,6):
    w=mountain(r)
    s=len(w)-r
    A,D=3**s,2**(s+r)
    if 1000*(3*D-2*A)<2*D:
        assert Fraction(3,2)-Fraction(A,D)<Fraction(1,1000)
        print('PASS near-sharp multiplier r',r,'s',s,'lambda',float(Fraction(A,D)))
        break
else:
    raise AssertionError('no sharp witness in test range')

for c in (5,23,41,59):
    z=(2*c-1)//3
    assert c%9==5 and c%2==1 and 0<z<c and z%3==0 and T(z)==c
    print('PASS formal conditional precursor',c,z)
print('DG014 finite exact regression PASS; conjecture OPEN')
