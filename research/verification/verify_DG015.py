#!/usr/bin/env python3
"""DG015 exact finite checks. Infinite nonrealisation rests on paper proof."""
import sys
sys.set_int_max_str_digits(1000000)
MORPH = {'0':'012','1':'02','2':'1'}
R = {'0':5,'1':11,'2':17}

def thue(n):
    s='0'
    while len(s)<n:
        s=''.join(MORPH[c] for c in s)
    return s[:n]

def mountain(r):
    assert r>=5 and r%6==5
    s=1
    while 3**s <= 2**(s+r): s+=1
    assert s+r>=14 and 2*3**s<3*2**(s+r)
    return '1'*s+'0'*r

def schedule(n, spikes=False):
    u=thue(n)
    rr=[R[c] for c in u]
    if spikes:
        h=0
        while 2**(h+8)<n:
            rr[2**(h+8)]=23+6*h
            h+=1
    return rr

def seed_for(word):
    A,q,D=1,0,1
    for w in word:
        if w=='1':
            A,q=3*A,3*q+D
        D*=2
    n=(-q*pow(A,-1,D))%D
    n+=D*((-n*pow(D,-1,3))%3)
    if n<=1: n+=3*D
    assert n%3==0
    return n

def T(x):
    return x//2 if x%2==0 else (3*x+1)//2

def exact_finite(rs, p,q,h):
    words=[mountain(r) for r in rs]
    n=seed_for(''.join(words))
    x=n; endpoints=[x]
    for w in words:
        prev=x
        for j,b in enumerate(w):
            assert x%2==int(b)
            x=T(x)
            if j+1<len(w): assert x>prev
        assert x>prev
        endpoints.append(x)
    assert all(endpoints[i+1]>endpoints[i] for i in range(len(rs)))
    assert rs[p:p+h]==rs[q:q+h]
    L=sum(len(z) for z in words[p:p+h]); assert L>=14*h
    delta=endpoints[q]-endpoints[p]
    assert delta>0 and delta%(2**L)==0
    assert delta<endpoints[q]+1<2**q*(n+1)
    assert n+1>2**(L-q)
    return len(str(n)),L,L-q

for k in (1,2,3,5):
    H=3*2**(k-1)
    q=2*H
    rs=schedule(q+H)
    assert rs[:H]==rs[q:q+H]
    if k in (1,2,5):
        digits,L,margin=exact_finite(rs,0,q,H)
        print('PASS bounded Thue',k,'H',H,'q',q,'L',L,'L-q',margin,'finite_seed_digits',digits)
    else:
        print('PASS bounded Thue factor',k,'H',H)

for k in (5,6,7):
    unit=2**(k-1)
    H=3*unit; p=20*unit; q=24*unit
    left=16*unit; right=32*unit
    assert left<p<p+H<q<q+H<right
    rs=schedule(q+H,spikes=True)
    raw=schedule(q+H)
    assert rs[p:p+H]==rs[q:q+H]==raw[p:p+H]
    assert all(rs[j]==raw[j] for j in range(p,q+H))
    assert rs[left] != raw[left] and (right>=len(rs) or rs[right]!=raw[right])
    if k==5:
        digits,L,margin=exact_finite(rs,p,q,H)
        print('PASS spiked finite witness',k,'H',H,'p',p,'q',q,'L',L,'L-q',margin,'finite_seed_digits',digits)
    else:
        print('PASS spike gap scaled factors',k,'H',H,'p',p,'q',q)

print('DG015 finite checks PASS; infinite claims established separately by proofs. E empty remains OPEN.')
