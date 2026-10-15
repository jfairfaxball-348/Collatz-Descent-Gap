#!/usr/bin/env python3
"""Heavy reproducibility verifier for RL338 physical q=35 certificates.

Usage:
  python3 -I verify_rl338_q35_exhaustive.py --layers
  python3 -I verify_rl338_q35_exhaustive.py --successors 22 28
  python3 -I verify_rl338_q35_exhaustive.py --successors 29 29

The split successor commands reproduce the gap-free closeout verification while
keeping each run bounded. Startup should use verify_rl338_q35_fast.py instead.
"""
import argparse
from fractions import Fraction
from functools import lru_cache
from collections import Counter, defaultdict
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LOW=1<<71; UP=(1<<76)+(1<<36); HC=20_390_252_058

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms): total+=term/(2*j+1); term*=x2
    lo=2*total; return lo,lo+2*term/(2*terms+1)/(1-x2)
_,l2hi=log_interval_atanh(Fraction(1,3)); l3lo,_=log_interval_atanh(Fraction(1,2))
delta_up=A*l2hi-ELL*l3lo
@lru_cache(None)
def factors(length):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(length+1))}); out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in {a,min(a+1,b-1)}:
            prev=(r+ELL-1)//ELL; gaps=[]
            for j in range(1,length+1):
                cur=(r+D*j+ELL-1)//ELL; gaps.append(1+cur-prev); prev=cur
            out.add(tuple(gaps))
    assert len(out)==length+1
    return tuple(out)
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
    rec([]); return tuple(out)
def residue(gaps):
    c=0
    for j,g in enumerate(gaps): c=(1<<g)*c+3**j
    m=3**len(gaps); return c*pow(1<<sum(gaps),-1,m)%m,m
def reconstruct(x,gaps):
    st=[x]
    for g in gaps:
        y=(1<<g)*x-1
        if y%3:return None
        x=y//3
        if not(x&1):return None
        st.append(x)
    return tuple(st)
def candidates(gaps):
    r,m=residue(gaps); x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x&1:
            st=reconstruct(x,gaps)
            if st is not None: yield x,st
        x+=m
def templates(pair,p):
    left,right=pair; L=left+right+p-1
    for base in factors(L):
        for q in profiles(p):
            ext=(0,)+q+(0,); g=list(base); ok=True
            for off in range(p+1):
                pos=left-1+off; g[pos]+=ext[off+1]-ext[off]
                if g[pos]<1: ok=False; break
            if ok: yield tuple(g),q
def positive_pairs(p):
    return [(l,r) for l in range(22,36) for r in range(22,36) if 2*l-8*p>0]
def exceptional_rows():
    rows=[]
    for p in (5,6):
        for left,right in positive_pairs(p):
            for g,q in templates((left,right),p):
                for x,st in candidates(g):
                    if delta_up*min(st)>=HC:
                        rows.append((p,left,right,x,st[left+p],q,st[left-1]))
    return rows

def run_layers():
    expected={5:(196,64120,299,161,68),6:(154,130386,10,8,4),7:(98,185360,0,0,0),8:(42,204590,0,0,0)}
    for p in range(5,9):
        t=c=o=0; rows=[]
        for left,right in positive_pairs(p):
            for g,q in templates((left,right),p):
                t+=1
                for x,st in candidates(g):
                    c+=1
                    if delta_up*min(st)>=HC:
                        o+=1; rows.append((left,right,x,st[left+p],q,st[left-1]))
        cores={(r[5],r[3],r[4]) for r in rows}
        got=(len(positive_pairs(p)),t,c,o,len(cores))
        print('layer',p,got,'sources',dict(sorted(Counter(r[0] for r in rows).items())))
        assert got==expected[p]
    print('RL338_LAYERS_GREEN')

def run_successors(lo,hi):
    rows=exceptional_rows(); by_left=defaultdict(set)
    for p,left,right,x,exit_state,q,boundary in rows: by_left[right].add(exit_state)
    assert sorted(by_left)==list(range(22,30))
    cont=[]; checks=0
    for left in range(lo,hi+1):
        exits=by_left[left]
        for p in range(1,9):
            for right in range(1,36):
                for g,q in templates((left,right),p):
                    checks += len(exits)
                    for x in exits:
                        st=reconstruct(x,g)
                        if st is not None and delta_up*min(st)>=HC:
                            cont.append((left,right,p,x,st[left+p],q,min(st)))
    def d(z):return max(0,2*z-43)
    def phi(z):return 35 if z>=22 else 0
    def rc(l,r,p):
        s=d(r)-d(l)-(2*r-43*p); w=35*(p-2*(r<=21))-s
        return w+phi(l)-phi(r)
    print('successors',lo,hi,'checks',checks,'count',len(cont),'sig',dict(sorted(Counter((c[2],c[0],c[1]) for c in cont).items())))
    print('charges',dict(sorted(Counter(rc(c[0],c[1],c[2]) for c in cont).items())))
    if lo==22 and hi==28:
        assert len(cont)==29
        assert sum(c[2]<=4 for c in cont)==24
        assert sum(c[2]>=5 for c in cont)==5
        assert max(rc(c[0],c[1],c[2]) for c in cont)==-30
        assert {(c[2],c[0],c[1]) for c in cont if c[2]>=5}=={(7,22,1)}
        assert {rc(c[0],c[1],c[2]) for c in cont if c[2]>=5}=={-88}
    if lo==29 and hi==29:
        assert not cont
    print('RL338_SUCCESSORS_GREEN',lo,hi)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--layers',action='store_true'); ap.add_argument('--successors',nargs=2,type=int)
    a=ap.parse_args()
    if a.layers: run_layers()
    if a.successors: run_successors(*a.successors)
    if not a.layers and not a.successors: ap.error('choose --layers or --successors LO HI')
if __name__=='__main__': main()
