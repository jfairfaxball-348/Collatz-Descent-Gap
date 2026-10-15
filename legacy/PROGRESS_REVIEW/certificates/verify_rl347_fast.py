#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

A=217_976_794_617
ELL=137_528_045_312
N0=20_390_252_058
INV=65_470_613_321

assert gcd(A,ELL)==1
assert (A*INV) % ELL == 1
assert 2*ELL == 275_056_090_624
assert 3*N0-4 == 61_170_756_170

L2=Fraction(15_757_912,22_733_865)
S_UP=Fraction(ELL,1)/(2*L2)-Fraction(1,2)
R_BOUND=6*(N0-1)-1-S_UP
assert R_BOUND == Fraction(91_143_694_376_456_377,3_939_478)
assert Fraction(23_135_982_578,1) < R_BOUND < Fraction(23_135_982_579,1)
RMIN=23_135_982_579
assert 2*ELL-RMIN == 251_920_108_045

UP=(1<<76)+(1<<36)
SEP=Fraction(UP,1<<40)
assert SEP == Fraction((1<<40)+1,16)
assert SEP == Fraction(1<<36,1)+Fraction(1,16)
# A positive even integer strictly below 2^36+1/16 is at most 2^36.
assert (1<<36) % 2 == 0
assert Fraction(1<<36,1) < SEP < Fraction((1<<36)+2,1)

print("RL347_FAST_GREEN")
print("inverse",INV)
print("R_bound",R_BOUND)
print("R_min",RMIN)
print("L_max",2*ELL-RMIN)
print("half_cycle_even_separation_max",1<<36)
