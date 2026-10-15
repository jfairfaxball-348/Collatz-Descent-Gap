#!/usr/bin/env python3
"""Portable RL337 checks: affine sign, suffix grammar, and targeted p=5 identity."""
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
ELL=137_528_045_312
D=A-ELL
LOW=1<<71
UP=(1<<76)+(1<<36)
HC=20_390_252_058

def carry(gaps):
    c=0; p3=1
    for g in gaps:
        c=(1<<g)*c+p3
        p3*=3
    return c

def closed_carry(gaps):
    return sum((3**k)*(1<<sum(gaps[k+1:])) for k in range(len(gaps)))

def deform(base,q):
    ext=(0,)+tuple(q)+(0,)
    return tuple(base[j]+ext[j+1]-ext[j] for j in range(len(base)))

def drop_formula(base,q):
    L=len(base); out=Fraction(0)
    for k in range(1,L):
        Q=q[k-1]
        out += (3**(k-1))*(1<<sum(base[k:]))*Fraction((1<<Q)-1,1<<Q)
    return out

examples=[
    ((2,2),(1,)),
    ((1,2,2),(2,1)),
    ((1,1,2,2),(1,2,1)),
    ((2,2,1,2,1,2),(2,1,2,1,1)),
]
for base,q in examples:
    g=deform(base,q)
    assert min(g)>=1 and sum(g)==sum(base)
    assert carry(base)==closed_carry(base) and carry(g)==closed_carry(g)
    drop=carry(base)-carry(g)
    assert drop==drop_formula(base,q) and drop>0
    H=sum(base); terminal=123456789
    src_base=Fraction((3**len(base))*terminal+carry(base),1<<H)
    src_g=Fraction((3**len(g))*terminal+carry(g),1<<H)
    assert src_g==src_base-Fraction(drop,1<<H)
    assert src_g<src_base

for u in [(2,2),(1,2,1),(2,1,2)]:
    for v in [(1,1),(2,1),(1,2,2)]:
        assert carry(u+v)==(1<<sum(v))*carry(u)+(3**len(u))*carry(v)

@lru_cache(None)
def profiles(p):
    out=[]
    def rec(pref):
        i=len(pref)
        if i==p-1:
            q=tuple(pref+[1])
            if all(q[j]<=q[j+1]+1 for j in range(p-1)): out.append(q)
            return
        for v in range(1,p-i+1): rec(pref+[v])
    rec([])
    return tuple(out)

for p in range(1,9):
    for q in profiles(p):
        assert q[-1]==1
        assert all(q[i]<=p-i for i in range(p))

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms):
        total += term/(2*j+1); term*=x2
    lo=2*total
    return lo,lo+2*term/(2*terms+1)/(1-x2)

l2lo,l2hi=log_interval_atanh(Fraction(1,3))
l3lo,l3hi=log_interval_atanh(Fraction(1,2))
delta_up=A*l2hi-ELL*l3lo

@lru_cache(None)
def factors(length):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(length+1))})
    out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in {a,min(a+1,b-1)}:
            prev=(r+ELL-1)//ELL; gaps=[]
            for j in range(1,length+1):
                cur=(r+D*j+ELL-1)//ELL
                gaps.append(1+cur-prev); prev=cur
            out.add(tuple(gaps))
    assert len(out)==length+1
    return tuple(out)

def residue(gaps):
    c=0
    for j,g in enumerate(gaps): c=(1<<g)*c+3**j
    m=3**len(gaps)
    return c*pow(1<<sum(gaps),-1,m)%m,m

def reconstruct(x,gaps):
    st=[x]
    for g in gaps:
        y=(1<<g)*x-1
        if y%3:return None
        x=y//3
        if not(x&1):return None
        st.append(x)
    return tuple(st)

def realizations(gaps):
    r,m=residue(gaps)
    x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x&1:
            st=reconstruct(x,gaps)
            if st: yield x,st
        x+=m

def templates_with_profile(pair,p):
    left,right=pair; out=[]
    for base in factors(left+right+p-1):
        for q in profiles(p):
            ext=(0,)+q+(0,); g=list(base); ok=True
            for off in range(p+1):
                pos=left-1+off
                g[pos]+=ext[off+1]-ext[off]
                if g[pos]<1:
                    ok=False; break
            if ok: out.append((tuple(g),q))
    return out

def physical_rows(pair,p=5):
    left,right=pair; rows=[]
    for g,q in templates_with_profile(pair,p):
        for x,st in realizations(g):
            if delta_up*min(st)>=HC:
                rows.append((x,st[left+p],q,min(st)))
    return rows

wanted=[(24,27),(24,28),(24,29)]
expected=(30437321051399780895133,31208280367336569715567,(2,1,2,1,1))
for pair in wanted:
    rows=physical_rows(pair)
    assert len(rows)==1 and rows[0][:3]==expected
for pair in [(27,24),(28,24),(29,24)]:
    assert physical_rows(pair)==[]

print('RL337_AFFINE_PROFILE_GREEN')
print('fixed_terminal_sign','positive_profile_source_is_smaller')
print('suffix_height_bound_green','p<=8_exhaustive')
print('p5_shared_identity',expected[0],expected[1],expected[2],wanted)
print('p5_reverse_rows',0)
