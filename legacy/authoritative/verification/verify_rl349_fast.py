#!/usr/bin/env python3
from fractions import Fraction

A=217_976_794_617
ELL=137_528_045_312
N0=20_390_252_058
L2=Fraction(15_757_912,22_733_865)

assert A-ELL == 80_448_749_305

# RL349 retains only this arithmetic diagnostic, not its unproved antecedent.
upper=Fraction(ELL,1)/(12*L2)
assert upper == Fraction(32_568_166_831_634_280,1_969_739)
assert upper < N0-1
assert Fraction(N0-1,1)-upper == Fraction(7_595_307_864_868_843,1_969_739)

# Inherited Phase-4 bounds remain unchanged.
assert 2*ELL-23_135_982_580 == 251_920_108_044
assert 3*N0-4 == 61_170_756_170

print("RL349_FAST_GREEN")
print("height_one_candidate_upper",upper)
print("high_carry_floor_minus_one",N0-1)
