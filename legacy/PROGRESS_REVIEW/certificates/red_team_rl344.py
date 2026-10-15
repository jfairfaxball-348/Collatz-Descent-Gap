#!/usr/bin/env python3
"""Independent RL344 red-team checks for the promoted Phase-4 singleton-interface constants."""
A = 217_976_794_617
ELL = 137_528_045_312
UP = (1 << 76) + (1 << 36)

# Avoid Fraction and re-derive the width inequality by integer cross multiplication.
q = 1 << 40
# 1 - 1/(1+2^-40)^2 = ((q+1)^2-q^2)/(q+1)^2 = (2q+1)/(q+1)^2.
num = UP * (2*q + 1)
den = (q + 1) ** 2
assert num < (1 << 37) * den
# Exact gap to 2^37.
assert (1 << 37) * den - num == (1 << 36) * (q + 1)

# Independently locate the first power of 3 exceeding 2^37.
p = 1
n = 0
while p <= (1 << 37):
    p *= 3
    n += 1
assert n == 24
assert p == 3**24
assert p // 3 == 3**23

# Independent Beatty-margin calibration for the known reversed (1,3) carrier.
G1 = 1
G2 = 4
assert A - ELL*G1 == 80_448_749_305
assert 2*A - ELL*G2 == -114_158_592_014

print("RL344_RED_TEAM_GREEN")
print("minimal_source_prefix_depth", n)
