#!/usr/bin/env python3
# Independent arithmetic replay of RL347 boundary constants.
from fractions import Fraction

a=217_976_794_617
e=137_528_045_312

# Extended Euclid, independent of pow(...,-1,...).
def egcd(x,y):
    if y==0:
        return (x,1,0)
    g,s,t=egcd(y,x%y)
    return (g,t,s-(x//y)*t)

g,x,_=egcd(a,e)
assert g==1
ainv=x%e
assert ainv==65_470_613_321

# Rational lower bound for ln 2 from first six positive atanh(1/3) terms.
lo=Fraction(0)
z=Fraction(1,3)
for r in range(6):
    lo += 2*z/(2*r+1)
    z *= Fraction(1,9)
assert lo == Fraction(15_757_912,22_733_865)

n=20_390_252_058
sup=Fraction(e,1)/(2*lo)-Fraction(1,2)
b=6*(n-1)-1-sup
q=b.numerator//b.denominator
assert q==23_135_982_578
assert b-q>0
rmin=q+1
assert rmin==23_135_982_579
assert 2*e-rmin==251_920_108_045

band_hi=(1<<76)+(1<<36)
sep=Fraction(band_hi,1<<40)
assert sep < (1<<36)+1
# Any positive even D < sep:
# D=2k, k integer, and sep/2 < 2^35+1, hence D<=2^36.
assert sep/2 < (1<<35)+1

print("RL347_RED_TEAM_GREEN")
print("ln2_lower",lo)
print("R_integer_min",rmin)
print("L_integer_max",2*e-rmin)
