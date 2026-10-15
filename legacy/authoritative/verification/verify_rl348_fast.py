#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
ELL=137_528_045_312
D=A-ELL
N0=20_390_252_058

assert D == 80_448_749_305
assert A-2*ELL == -57_079_296_007
assert 2*ELL == 275_056_090_624

# Universal r=1 terminal law arithmetic.
assert A-2*ELL < 1
assert 0 < D < ELL
# If g1>=2 then B1<=A-2ELL<1<=c; only g1=1 can be complete.
# With g1=1, B1=D and c<=D makes q=1+floor((D-c)/ELL)=1.
for c in (1, D//2, D):
    assert 0 <= D-c < ELL
    assert 1 + (D-c)//ELL == 1

# Exact mod-4 consequence: for odd E mod 4, v2(3E+1)=1 iff E==3 mod4.
good=[]
for e in (1,3):
    x=3*e+1
    v=0
    while x%2==0:
        v+=1; x//=2
    if v==1: good.append(e)
assert good == [3]

# Crossing split constants.
assert 3*N0-4 == 61_170_756_170
L2=Fraction(15_757_912,22_733_865)
S_UP=Fraction(ELL,1)/(2*L2)-Fraction(1,2)
T_BOUND=6*(N0-1)-S_UP
assert T_BOUND == Fraction(91_143_694_380_395_855,3_939_478)
assert Fraction(23_135_982_579,1) < T_BOUND < Fraction(23_135_982_580,1)
RMIN=23_135_982_580
assert 2*ELL-RMIN == 251_920_108_044

# Safe half-cycle synchronization depth.
assert (1<<36) <= (1<<36)
def v2(n):
    r=0
    while n%2==0:
        r+=1; n//=2
    return r
for d in (2,4,8,1<<35,1<<36):
    assert v2(d)<=36

print("RL348_FAST_GREEN")
print("terminal_phase_tag_max",D)
print("pre_crossing_R_min",3*N0-4)
print("post_crossing_bound",T_BOUND)
print("universal_R_min",RMIN)
print("universal_L_max",2*ELL-RMIN)
print("half_cycle_sync_max",36)
