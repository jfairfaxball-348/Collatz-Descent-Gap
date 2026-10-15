#!/usr/bin/env python3
"""FINAL_CHANCE Session 5 verifier: ownership-quotient state-window barrier.

Uses the rigorously outward-rounded Session 1 primitives.  It proves that the
necessary real size information coming from a genuine owner,
    m = Q_h / D and 2^71 <= m < 2^75,
cannot by itself control either residue-order support or defect height.

No ownership/integrality is asserted for the countermodels below.
"""

from verify_session1_interval import (
    A, L, Interval, rat_interval, fraction_interval, floor_sum_F,
    ln_integer_bounds, expm1_bounds, iadd, isub, imul, idiv,
)

M = A - L
P = pow(A, -1, L)
T = L - P

def b(j):
    return (A * j) // L

def c(j):
    return b(j + 1) - b(j)

# Rigorous denominator factor:
# Q_h/D = [sum rho_j 2^-h_j] / [3(exp(Delta)-1)].
l2_lo, l2_hi = ln_integer_bounds(2, 300)
l3_lo, l3_hi = ln_integer_bounds(3, 400)
delta_lo = A * l2_lo - L * l3_hi
delta_hi = A * l2_hi - L * l3_lo
assert 0 < delta_lo < delta_hi
e_lo, e_hi = expm1_bounds(delta_lo, delta_hi, 20)
E = Interval(fraction_interval(e_lo).lo, fraction_interval(e_hi).hi)
den = imul(Interval(3), E)
C = idiv(Interval(1), den)

S = floor_sum_F(L, A, rat_interval(1, 3), Interval(2))
q0 = idiv(S, den)

# Every nonnegative defect decreases Q, so the upper state ceiling is
# automatically satisfied once the zero-defect quotient lies below 2^75.
assert q0.hi < 2**75

# Family A: Session-4 connected height-one run, maximal certified length.
# Each defective phase loses rho_j/2 < 1/2 in the normalized numerator.
N = P - 1
q_run = isub(q0, imul(C, rat_interval(N, 2)))
q_run_lower = q_run.lo
assert q_run_lower > 2**71
support = 2 * N + 1
assert support == 130_941_226_641

# Family B: very high legal ramp followed by a drop.
# h_j = floor(M*j/L) for 0<=j<=J, then zero.
# It is legal because h_(j+1)-h_j = c_j-1 in {0,1}.
# Every defective phase can lose less than 1 normalized unit, so even the
# crude bound q_h > q0 - C*J proves the state floor.
J = 1_000_000_000
H = (M * J) // L
assert H == 584_962_500
assert c(0) in (1, 2)
assert c(J - 1) in (1, 2)
q_ramp = isub(q0, imul(C, Interval(J)))
q_ramp_lower = q_ramp.lo
assert q_ramp_lower > 2**71

# The final drop from h_J=H to zero is always allowed by
# a_J = c_J + H >= 1.
assert c(J) + H >= 1

print("FINAL_CHANCE Session 5 ownership-quotient state-window verifier: PASS")
print("A,L,M =", (A, L, M))
print("inverse phase P =", P)
print("zero-defect quotient lower =", q0.lo)
print("zero-defect quotient upper =", q0.hi)
print("zero-defect quotient < 2^75 =", q0.hi < 2**75)
print("height-one maximal-run N =", N)
print("height-one collapsed support =", support)
print("height-one quotient lower bound =", q_run_lower)
print("height-one quotient lower bound > 2^71 =", q_run_lower > 2**71)
print("ramp cut J =", J)
print("ramp height H =", H)
print("ramp quotient lower bound =", q_ramp_lower)
print("ramp quotient lower bound > 2^71 =", q_ramp_lower > 2**71)
print("scope=necessary ownership quotient window only; integrality not asserted")
