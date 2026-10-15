#!/usr/bin/env python3
LOW=2**71; UP=2**76+2**36
START=23912137200748175205995
MOD=77998046721343488
N=238329
PRE=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,2,1)
MID=(3,1,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1)
SUC=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,3,1)

def fwd(x,word):
    out=[x]
    for g in word:
        q=(2**g*x-1)
        if q%3: return None
        x=q//3
        if x%2==0: return None
        out.append(x)
    return out

def rev(final,word):
    x=final
    for g in word[::-1]:
        q=3*x+1
        if q%(2**g): return None
        x=q//(2**g)
        if x%2==0: return None
    return x

def T(x):
    y=3*x+1
    while y%2==0: y//=2
    return y

assert MOD==2**26*3**19
maxd=0; arg=None
for k in range(N):
    p=START+MOD*k
    # Exact three-row shared-state reconstruction.
    pre=rev(p,PRE); assert pre is not None and LOW<=pre<UP
    a=fwd(pre,PRE); assert a is not None and a[-1]==p
    b=fwd(p,MID); assert b is not None
    e=b[2]; assert LOW<=e<UP
    c=fwd(e,SUC); assert c is not None
    # Least-state contradiction for this carrier source.
    x=p; d=0
    while x>=LOW:
        x=T(x); d+=1
        assert d<1000
    if d>maxd: maxd=d; arg=k
assert maxd==188 and arg==104356
# COUNT is sharp because the next middle run-exit leaves the q=0 band.
last=START+MOD*(N-1); nxt=last+MOD
assert (16*last-5)//9 < UP <= (16*nxt-5)//9
print('RL342_RED_TEAM_GREEN')
print('all_chain_members',N,'all_descend',True,'max_escape',maxd,'argmax_k',arg)
