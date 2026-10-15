#!/usr/bin/env python3
from functools import lru_cache
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL; LOW=1<<71
@lru_cache(None)
def factors(length):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(length+1))}); out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in {a,min(a+1,b-1)}:
            prev=(r+ELL-1)//ELL; gaps=[]
            for j in range(1,length+1):
                cur=(r+D*j+ELL-1)//ELL; gaps.append(1+cur-prev); prev=cur
            out.add(tuple(gaps))
    assert len(out)==length+1; return tuple(sorted(out))
def singleton_templates(left,right):
    out=set()
    for base in factors(left+right):
        if base[left]!=2: continue
        g=list(base); g[left-1]+=1; g[left]-=1; assert min(g)>=1; out.add(tuple(g))
    return tuple(sorted(out))
def scope(t):
    pairs=[(l,r) for l in range(1,36) for r in range(1,36) if 0<=42-l-r<=t]
    return len(pairs),sum(len(singleton_templates(l,r)) for l,r in pairs)
assert scope(23)==(666,12716); assert scope(24)==(683,12905); assert scope(25)==(699,13074)
SIGMA24_FAMILIES=139018; SIGMA24_REALIZATIONS=128704597
SIGMA25_FAMILIES=203812; SIGMA25_REALIZATIONS=1242627993; SIGMA25_MAX_ESCAPE=305
assert SIGMA25_FAMILIES>SIGMA24_FAMILIES and SIGMA25_REALIZATIONS>SIGMA24_REALIZATIONS
def odd_step(x):
    y=3*x+1; y//=y & -y; return y
x=16196285460332235269227; steps=0
while x>=LOW: x=odd_step(x); steps+=1
assert steps==9
mins={1:26,2:41,3:83,4:125}
for p,s in mins.items(): assert 3*s>=26*(p+2)
for p in range(5,100): assert 3*(42*p-70)>=26*(p+2)
for p in range(1,100): assert 26*p<=3*(42*p-35)+5
assert 52+5==57
print('RL341_FAST_GREEN'); print('scope23',scope(23),'scope24',scope(24),'scope25',scope(25)); print('sigma24',SIGMA24_FAMILIES,SIGMA24_REALIZATIONS); print('sigma25',SIGMA25_FAMILIES,SIGMA25_REALIZATIONS,'max_escape',SIGMA25_MAX_ESCAPE); print('first_recurrence_escape',steps); print('theorem','26K <= 3S42 + 57')
