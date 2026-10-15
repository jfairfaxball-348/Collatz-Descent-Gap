#!/usr/bin/env python3

from fractions import Fraction
A=217_976_794_617
ELL=137_528_045_312

def log_interval_atanh(x,terms=280):
    x2=x*x; term=x; total=Fraction(0)
    for j in range(terms):
        total += term/(2*j+1); term*=x2
    lo=2*total
    return lo,lo+2*term/(2*terms+1)/(1-x2)

LOW=1<<71
UP=(1<<76)+(1<<36)
P0=23912137200748175205995
STEP=77998046721343488
COUNT=238329
MID_EXIT0=42510466134663422588435
PRED_SOURCE0=30676695662567844669575
MAX_ESCAPE=188
GPRE=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,2,1)
GMID=(3,1,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1)
GSUCC=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,3,1)

def carry(gaps):
    c=0
    for j,g in enumerate(gaps):
        c=(1<<g)*c+3**j
    return c

def reconstruct(x,gaps):
    st=[x]
    for g in gaps:
        y=(1<<g)*x-1
        assert y%3==0
        x=y//3
        assert x&1
        st.append(x)
    return st

def source_for_exit(exit_state,gaps):
    num=(3**len(gaps))*exit_state+carry(gaps)
    den=1<<sum(gaps)
    assert num%den==0
    x=num//den
    assert x&1
    return x

def odd_step(x):
    y=3*x+1
    return y//(y & -y)

assert STEP==(1<<26)*(3**19)
# Exact positivity of delta=a ln2-ell ln3, and a rigorous lower bound
# showing the middle return is phase-potential nondecreasing already at P0.
l2lo,l2hi=log_interval_atanh(Fraction(1,3))
l3lo,l3hi=log_interval_atanh(Fraction(1,2))
delta_lo=A*l2lo-ELL*l3hi
assert delta_lo>0
x=Fraction(5,16*P0)
# ln(1-x) >= -x/(1-x), so this proves
# 2*delta/ell + ln(1-5/(16P0)) > 0 exactly.
assert 2*delta_lo/ELL - x/(1-x) > 0
assert 42-15-1==26 and 42-1-16==25 and 42-16-1==25
assert source_for_exit(P0,GPRE)==PRED_SOURCE0
pred=reconstruct(PRED_SOURCE0,GPRE); assert pred[-1]==P0
mid=reconstruct(P0,GMID); assert mid[2]==MID_EXIT0
succ=reconstruct(MID_EXIT0,GSUCC)
assert succ[17]==44181903199359184830227
last=P0+STEP*(COUNT-1)
nextp=P0+STEP*COUNT
assert LOW<=P0<UP and LOW<=last<UP
assert ((16*last-5)//9)<UP <= ((16*nextp-5)//9)
# Congruence-class compatibility is constant on STEP=2^26*3^19.
for P in (P0,last):
    x=source_for_exit(P,GPRE)
    assert LOW<=x<UP and reconstruct(x,GPRE)[-1]==P
    m=reconstruct(P,GMID); e=m[2]
    assert LOW<=e<UP
    reconstruct(e,GSUCC)
mx=0; arg=-1
for k in range(COUNT):
    x=P0+STEP*k
    steps=0
    while x>=LOW:
        x=odd_step(x); steps+=1
        assert steps<=MAX_ESCAPE
    if steps>mx: mx=steps; arg=k
assert mx==MAX_ESCAPE and arg==104356
print('RL342_FAST_GREEN')
print('family_count',COUNT,'step',STEP,'max_escape',mx,'argmax_k',arg)
print('chain','(15,1)->(1,16)->(16,1)')
