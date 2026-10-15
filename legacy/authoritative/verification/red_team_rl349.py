#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
ELL=137_528_045_312
N0=20_390_252_058

# Reconstruct independently the inherited six-term positive atanh(1/3)
# lower bound for ln 2.
lo=Fraction(0)
z=Fraction(1,3)
for r in range(6):
    lo += 2*z/(2*r+1)
    z *= Fraction(1,9)
assert lo == Fraction(15_757_912,22_733_865)

# Recompute the only new retained arithmetic diagnostic directly.
b=Fraction(ELL,1)/(12*lo)
assert b.numerator == 32_568_166_831_634_280
assert b.denominator == 1_969_739
assert b < N0-1
margin=Fraction(N0-1,1)-b
assert margin == Fraction(7_595_307_864_868_843,1_969_739)
assert margin > 0

# Sanity-check inherited constants used by the successor handover.
assert A-ELL == 80_448_749_305
assert 2*ELL == 275_056_090_624
assert 2*ELL-251_920_108_044 == 23_135_982_580

print("RL349_RED_TEAM_GREEN")
print("ln2_lower",lo)
print("diagnostic_margin",margin)
