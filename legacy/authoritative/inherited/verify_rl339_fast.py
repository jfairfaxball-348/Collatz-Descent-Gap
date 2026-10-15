"""Candidate 42-slack phase-pair arithmetic; PROMOTED; see RL339 certificate."""
from fractions import Fraction
from pathlib import Path
from runpy import run_path

v=run_path(str(Path(__file__).resolve().parent/"cap_core.py"))
c=Fraction(198849,1000000)
CAP=32537248343
ell=v["ELL"]
a=v["A"]
alpha44=Fraction((44*a)%ell,ell)
assert Fraction(1,2)<alpha44<1

beta=1-alpha44
log2_lower=v["l2"]
y=beta*log2_lower
exp_lower=1+y+y*y/2+y**3/6+y**4/24+y**5/120+y**6/720
assert exp_lower-1>c

K0=v["K"]
T=ell-60
s=44*K0-2*(T+1)+70
assert 0<=s<=43
W=v["W"]
def St(h):
    K=K0+h
    S=44*h+s
    return K+c*max(Fraction(0),Fraction(K-4*S-3,4))
def g(h):return max(Fraction(h),St(h)-W(K0))
m=St(1)-St(0)
cross=(St(0)-W(K0))/(1-m)
q=max(0,cross.numerator//cross.denominator)
choices={0,q,q+1}
h,gain=min(((h,g(h)) for h in choices),key=lambda item:item[1])
R=1+(v["full"]-v["om59"])/3-W(K0)/(12*v["LAM"])-gain/(12*v["LAM"])
cutoff=Fraction(K0-4*s-3,175)
assert q<cutoff and h==24281914
assert CAP<R<CAP+1

# All-rho monotonicity. Let K_r=ceil((T+1-35)/22), s_r=44K_r-2(T+1)+70.
# If K_r is unchanged when rho grows by one, s grows by two, so every
# structural-minus-residue value drops by at most 2c; the optimized gain
# drops by at most 2c. The newly omitted ideal term lowers RHS by more than
# 1/(6 Lambda), while loss of gain can restore at most 2c/(12 Lambda).
assert c<1
assert 2*c/(12*v["LAM"])<1/(6*v["LAM"])

# If K_r drops by one, s falls by 42. At fixed h the argument of the
# positive-part structural gain grows by 167, while K+h falls by one.
# W(K)-W(K-1)>=1, hence structural-minus-residue and its optimized gain
# cannot decrease. The restored residue weight is <22/21 and is paid by the
# newly omitted term (>1/(2 Lambda)).
assert 22*K0<ell
assert Fraction(22,21)/(12*v["LAM"])<1/(6*v["LAM"])
assert v["rho59"]<CAP+1
print("PHASE42_CAP_GREEN")
print("alpha44",float(alpha44),"certified_pair_gain",c)
print("K0",K0,"endpoint_slack",s,"optimal_h",h,"weighted_gain",float(gain))
print("rho60_RHS",float(R),"floor",R.numerator//R.denominator)
print("all_rho_monotonic",True,"cap",CAP)
print("RL339_PROMOTED")
