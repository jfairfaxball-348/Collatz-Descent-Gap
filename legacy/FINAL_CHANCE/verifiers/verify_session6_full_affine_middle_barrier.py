#!/usr/bin/env python3
"""FINAL_CHANCE Session 6: full-affine middle-bridge countermodel.

The profile
    h_j = 1 for 2 <= j <= L-1, and 0 at j=0,1,L
is a legal nonnegative first-survivor defect excursion with boundary collar
p+(L-q)=3.  Its unique positive rational ordinary +1 affine return has least
root Q_h/D strictly inside [2^71,2^75), but Q_h/D is not an integer.

Thus full-period affine middle closure, least-root order, state-window size,
the exact (A,L) counts, and a very tight boundary collar can all hold without
ordinary physical ownership.

No giant integer D or Q_h is materialized.
"""

from decimal import Decimal, ROUND_FLOOR
from verify_session1_interval import (
    A, L, Interval, rat_interval, fraction_interval, floor_sum_F,
    ln_integer_bounds, expm1_bounds, iadd, imul, idiv, rop, CTX_D, CTX_U,
)

LOW = 1 << 71
HIGH = 1 << 75

def b(j):
    return (A * j) // L

def c(j):
    return b(j + 1) - b(j)

# Exact grammar / collar checks.
assert c(0) == 1
assert c(1) == 2
assert c(L - 1) == 2

# h_0=h_1=h_L=0 and h_j=1 on 2..L-1.
# a_0=c_0=1; a_1=c_1-1=1; interior a_j=c_j; final a_(L-1)=c_(L-1)+1=3.
assert c(0) >= 1
assert c(1) - 1 >= 1
assert c(L - 1) + 1 >= 1

p = 2
q = L - 1
assert p + (L - q) == 3
area = L - 2
assert area >= 3

# Telescoping a_j=c_j+h_j-h_(j+1) gives the exact total exponent A.
assert b(L) == A

# Rigorous denominator 3*(exp(Delta)-1).
l2_lo, l2_hi = ln_integer_bounds(2, 300)
l3_lo, l3_hi = ln_integer_bounds(3, 400)
delta_lo = A * l2_lo - L * l3_hi
delta_hi = A * l2_hi - L * l3_lo
assert 0 < delta_lo < delta_hi
e_lo, e_hi = expm1_bounds(delta_lo, delta_hi, 20)
expm1_delta = Interval(
    fraction_interval(e_lo).lo,
    fraction_interval(e_hi).hi,
)
denominator = imul(Interval(3), expm1_delta)

# S = sum rho_j, rho_j = 2^floor(Aj/L)/3^j.
S = floor_sum_F(L, A, rat_interval(1, 3), Interval(2))

# For h_j=1 exactly on 2..L-1,
# sum rho_j 2^-h_j = S/2 + (rho_0+rho_1)/2 = S/2 + 5/6,
# because rho_0=1 and rho_1=2/3.
numerator = iadd(imul(S, rat_interval(1, 2)), rat_interval(5, 6))
quotient = idiv(numerator, denominator)

assert quotient.lo > Decimal(LOW)
assert quotient.hi < Decimal(HIGH)

floor_lo = int(quotient.lo.to_integral_value(rounding=ROUND_FLOOR))
floor_hi = int(quotient.hi.to_integral_value(rounding=ROUND_FLOOR))
assert floor_lo == floor_hi
assert quotient.lo > Decimal(floor_lo)
assert quotient.hi < Decimal(floor_lo + 1)

width = rop(CTX_U, lambda: quotient.hi - quotient.lo)
dist_above = rop(CTX_D, lambda: quotient.lo - Decimal(floor_lo))
dist_below = rop(CTX_D, lambda: Decimal(floor_lo + 1) - quotient.hi)

print("FINAL_CHANCE Session 6 full-affine middle-bridge verifier: PASS")
print("A,L =", (A, L))
print("profile = h_j=1 for 2<=j<=L-1, zero otherwise")
print("defect area =", area)
print("first defect p =", p)
print("last defect q =", q)
print("boundary collar p+(L-q) =", p + (L-q))
print("exponent endpoints = a_0=1, a_1=1, a_(L-1)=3")
print("total exponent = A (telescoping) = True")
print("Q_h/D lower =", quotient.lo)
print("Q_h/D upper =", quotient.hi)
print("interval width <=", width)
print("Q_h/D in [2^71,2^75) =", True)
print("common integer part =", floor_lo)
print("distance above floor >=", dist_above)
print("distance below next integer >=", dist_below)
print("ordinary ownership D|Q_h =", False)
print("scope=positive rational full-affine +1 return; not an integer Collatz cycle")
