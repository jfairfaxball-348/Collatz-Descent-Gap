#!/usr/bin/env python3
"""Exact constant checks for the analytic two-row canonical-walk bridge."""
from fractions import Fraction
from math import gcd

A = 217976794617
ELL = 137528045312
N = 2 * ELL
LAMBDA_UP = Fraction((1 << 40) + 1, 1 << 40)
LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
M_MAX = (1 << 75) - 1

assert gcd(A, ELL) == 1
assert N < 1 << 39
# log(lambda) < 2^-40, and exp(x) <= 1/(1-x) for 0<=x<1.
x = Fraction(N, 1 << 40)
assert x < Fraction(1, 2)
assert Fraction(1, 1) / (1 - x) < 2
# Thus lambda^N < 2, and lambda^ELL < 2 as well.
assert 2 * LAMBDA_UP * M_MAX < UP
assert UP - LOW < 1 << 76
# The full-cycle q=0 band is the inherited band, so the terminal-60
# endpoint range and the 75-gap uniqueness bound remain unchanged.
STEP = 1 << 60
assert (LOW + STEP) // STEP == 2049
assert UP // STEP == 65536

print("RL343_FULL_CYCLE_BRIDGE_CONSTANTS_GREEN")
print("full_odd_steps", N)
print("lambda_to_full_odd_steps_upper", 1 / (1 - x))
print("global_q0_band", LOW, UP)
