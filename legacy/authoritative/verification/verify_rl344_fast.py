#!/usr/bin/env python3
"""Portable RL344 fast checks for promoted analytic constants and boundary identities."""
from fractions import Fraction
from math import gcd

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
U = Fraction((1 << 40) + 1, 1 << 40)

assert D == 80_448_749_305
assert gcd(A, ELL) == 1
assert UP - LOW < 1 << 76

# Phase-4 absolute source localization:
# P - 3^L E / 2^H = C/2^H < P(1-U^-2) < UP(1-U^-2) < 2^37.
width = Fraction(UP) * (1 - 1 / (U * U))
assert width < 1 << 37
assert (1 << 37) - width == Fraction(1 << 36, (1 << 40) + 1)

# 24 is the first uniform 3-adic prefix depth exceeding the phase-width bound.
assert 3**23 < 1 << 37 < 3**24

# Calibration against the promoted RL342 two-step middle return, reversed as valuations (1,3).
gaps = (1, 3)
G = 0
B = []
for r, d in enumerate(gaps, 1):
    G += d
    B.append(A * r - ELL * G)
assert B == [80_448_749_305, -114_158_592_014]

# Terminal last-defect cylinder identity: E=2^(t+1)j-1 with j odd has exact v2(E+1)=t+1.
for t in range(60):
    for j in (1, 3, 5, 101):
        e = (j << (t + 1)) - 1
        z = e + 1
        v = 0
        while z % 2 == 0:
            z //= 2
            v += 1
        assert v == t + 1

# Short-return scratch is intentionally not promoted here.
print("RL344_FAST_GREEN")
print("phase4_width_upper", width)
print("source_prefix_depth", 24)
