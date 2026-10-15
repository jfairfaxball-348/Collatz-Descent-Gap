#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
ELL=137_528_045_312
N0=20_390_252_058

# Independently reconstruct the six-term positive atanh(1/3) lower bound for ln 2.
lo=Fraction(0)
z=Fraction(1,3)
for r in range(6):
    lo += 2*z/(2*r+1)
    z *= Fraction(1,9)
assert lo == Fraction(15_757_912,22_733_865)

# Independent terminal check over the only relevant threshold cases.
# B1=A-ELL*g. Completeness requires B1>=c>=1.
assert A-ELL == 80_448_749_305
assert A-2*ELL == -57_079_296_007
assert A-ELL >= 1
assert A-2*ELL < 1

# Endpoint mod 4: test odd residues directly.
vals={}
for e in (1,3):
    x=3*e+1
    v=0
    while x%2==0:
        v+=1
        x//=2
    vals[e]=v
assert vals[3]==1 and vals[1]>=2

# Independent post-crossing bound.
sup=Fraction(ELL,1)/(2*lo)-Fraction(1,2)
b=6*(N0-1)-sup
q=b.numerator//b.denominator
assert q==23_135_982_579
assert b-q>0
assert q+1==23_135_982_580
assert 2*ELL-(q+1)==251_920_108_044

# Independent parity synchronization sanity:
# each equal-parity ordinary shortcut phase lowers v2 of a nonzero difference by exactly one.
def v2(n):
    r=0
    while n%2==0:
        n//=2; r+=1
    return r
for d in (2,6,10,12,1<<36):
    vd=v2(d)
    assert v2(d//2)==vd-1
    assert v2(3*d//2)==vd-1
    assert vd<=36

print("RL348_RED_TEAM_GREEN")
print("ln2_lower",lo)
print("post_crossing_R_min",q+1)
print("L_max",2*ELL-(q+1))
