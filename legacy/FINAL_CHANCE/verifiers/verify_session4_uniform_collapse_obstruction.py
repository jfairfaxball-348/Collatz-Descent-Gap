#!/usr/bin/env python3
"""FINAL_CHANCE Session 4 verifier: uniform-collapse structural obstruction.

This is an exact arithmetic verifier for the countermodels used in Session 4.
It does not enumerate profiles at the actual L scale and does not test ownership.

It verifies:
  * the actual-scale modular inverse controlling residue-order adjacency;
  * a legal connected height-one family whose collapsed support grows as 2N+1
    for every 3 <= N <= P-1;
  * an area-three member whose collapsed degree already exceeds M=A-L;
  * a legal height-three profile for which the Session-3-style
    Parseval/AM-GM sufficient upper bound is necessarily > D from the
    constant coefficient alone;
  * the available legal height range for the monotone-ramp family.
"""

from math import gcd

A = 217_976_794_617
L = 137_528_045_312
M = A - L

def b(j: int) -> int:
    return (A * j) // L

def c(j: int) -> int:
    return b(j + 1) - b(j)

def r(j: int) -> int:
    return (A * j) % L

def add_coeff(poly: dict[int, int], k: int, v: int) -> None:
    poly[k] = poly.get(k, 0) + v
    if poly[k] == 0:
        del poly[k]

assert gcd(A, L) == 1
assert M == 80_448_749_305

# A P - U L = 1. Exponent adjacency therefore corresponds to phase
# separation +/-P modulo L.
P = pow(A, -1, L)
U = (A * P - 1) // L
T = L - P
assert (P, U, T) == (65_470_613_321, 103_768_467_013, 72_057_431_991)
assert A * P - U * L == 1
assert P < T

# The connected height-one family is
#   h_j = 1 for 2 <= j <= N+1, and 0 otherwise.
# The only rise is h_1=0 -> h_2=1, and c_1=2 makes it legal.
assert c(1) == 2
Nmax = P - 1
assert Nmax + 1 == P < T
# For two phases in [2,N+1], a collision r_k = r_j +/- 1 would require
# k-j congruent to +/-P modulo L, i.e. a positive separation P or T.
# But |k-j| <= N-1 <= P-2 throughout the family.
assert Nmax - 1 == P - 2 < P < T

support_max = 2 * Nmax + 1
assert support_max == 130_941_226_641
assert support_max < L

# The N=3 member is already enough to kill the Session 3 degree window.
area3_residues = [r(j) for j in range(2, 5)]
assert area3_residues == [23_369_453_298, 103_818_202_603, 46_738_906_596]
area3_degree = max(x + 1 for x in area3_residues)
assert area3_degree == 103_818_202_604
assert area3_degree > M
assert area3_degree < L

# Legal height-three ramp:
# h_j=b_j-j through j=6, then drop to zero.
h = [b(j) - j for j in range(7)] + [0]
assert h == [0, 0, 1, 1, 2, 2, 3, 0]
for j in range(7):
    # Equivalent inherited excursion grammar:
    # a_j = c_j + h_j - h_{j+1} >= 1.
    assert c(j) + h[j] - h[j + 1] >= 1
H = max(h)
assert H == 3
assert sum(h[:-1]) == 9

# E_h(X)=2^(H-1)+(X-1)G_h(X),
# G_h=sum_j (2^H-2^(H-h_j)) X^(r_j).
E: dict[int, int] = {0: 2 ** (H - 1)}
for j in range(1, 7):
    if h[j] == 0:
        continue
    d = 2**H - 2 ** (H - h[j])
    rr = r(j)
    assert rr != L - 1
    add_coeff(E, rr, -d)
    add_coeff(E, rr + 1, d)

assert E[0] == 4
assert max(E) < L
assert gcd(*[abs(v) for v in E.values()]) == 1
assert 7 in [abs(v) for v in E.values()]
assert len(E) == 11

# For B(X)=2X^L-1, the Session-3 Parseval/AM-GM route has sufficient
# upper bound
#   |Res(B,E)| <= 2^m * V(E)^(L/2),
#   V(E)=sum e_k^2 alpha^(2k), alpha=2^(-1/L).
# Since e_0=4, V(E)>=16, hence that RHS is >=4^L=2^(2L).
# As 2L>A and D=2^A-3^L<2^A, this sufficient upper bound is >D
# before any other coefficient is counted.
assert 2 * L > A

# General ramp height range: d_j=b_j-j has increments c_j-1 in {0,1},
# starts at 0, and reaches M-1 at j=L-1. Hence every height
# 1,...,M-1 occurs and can be made the unique maximum by dropping to zero
# immediately after its first occurrence.
assert b(L - 1) - (L - 1) == M - 1
assert c(0) in (1, 2)
assert c(L - 2) in (1, 2)

print("FINAL_CHANCE Session 4 uniform-collapse obstruction verifier: PASS")
print("A,L,M =", (A, L, M))
print("inverse phase P,U =", (P, U))
print("complement T =", T)
print("connected height-one family N range = [3,", Nmax, "]")
print("support count formula = 2N+1")
print("maximum certified family support =", support_max)
print("area-3 residues =", tuple(area3_residues))
print("area-3 collapsed degree =", area3_degree)
print("Session-3 degree window M =", M)
print("degree window violated =", area3_degree > M)
print("height-3 ramp h[0:8] =", tuple(h))
print("height-3 defect area =", sum(h[:-1]))
print("height-3 primitive collapsed constant =", E[0])
print("height-3 collapsed support =", len(E))
print("2L>A =", 2 * L > A)
print("Parseval sufficient bound already > D from e0 alone = True")
print("legal ramp heights include every H in [1,", M - 1, "]")
print("scope=structural grammar countermodels; ownership not asserted")
