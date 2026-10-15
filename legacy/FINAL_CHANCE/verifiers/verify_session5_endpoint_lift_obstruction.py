#!/usr/bin/env python3
"""FINAL_CHANCE Session 5 verifier: endpoint-lift bridge obstruction.

Exact arithmetic checks for the two global endpoint lifts and for the
connected height-one state-window countermodel used to kill the proposed
uniform endpoint-size bridge.  No giant 2^A or 3^L integer is materialized.
"""
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
M = A - L
P = 65_470_613_321
U = 103_768_467_013
T = L - P
S = A - U


def b(j):
    return (A*j)//L


def c(j):
    return b(j+1)-b(j)


def ln_integer_bounds(n, terms):
    z = Fraction(n - 1, n + 1)
    z2 = z*z
    zp = z
    total = Fraction(0)
    for k in range(terms):
        total += Fraction(2, 2*k+1)*zp
        zp *= z2
    tail = Fraction(2)*zp/Fraction(2*terms+1)/(1-z2)
    return total, total + tail


def expm1_bounds(lo, hi, terms=20):
    assert 0 <= lo <= hi < 1
    lower = Fraction(0)
    p = Fraction(1)
    fact = 1
    for k in range(1, terms+1):
        p *= lo
        fact *= k
        lower += p/fact
    upper = Fraction(0)
    p = Fraction(1)
    fact = 1
    for k in range(1, terms+1):
        p *= hi
        fact *= k
        upper += p/fact
    tail = (p*hi)/(fact*(terms+1))/(1-hi)
    return lower, upper + tail


l2_lo, l2_hi = ln_integer_bounds(2, 300)
l3_lo, l3_hi = ln_integer_bounds(3, 400)
delta_lo = A*l2_lo - L*l3_hi
delta_hi = A*l2_hi - L*l3_lo
assert 0 < delta_lo < delta_hi
em1_lo, em1_hi = expm1_bounds(delta_lo, delta_hi, 20)

assert A*P-U*L == 1
assert A*T-S*L == -1
assert (M,P,U,T,S) == (
    80_448_749_305,
    65_470_613_321,
    103_768_467_013,
    72_057_431_991,
    114_208_327_604,
)

# Global floor-lock integrity condition highlighted by the Session 3 audit.
assert delta_hi * L < l2_lo

# Near-unity errors for the two Bezout representations.
# 2^U/3^P = exp(-x3), 3^T/2^S = exp(-x2).
x3_lo = P*l3_lo - U*l2_hi
x3_hi = P*l3_hi - U*l2_lo
x2_lo = S*l2_lo - T*l3_hi
x2_hi = S*l2_hi - T*l3_lo
assert 0 < x3_lo < x3_hi
assert 0 < x2_lo < x2_hi

# Session-3 denominator lower bounds retained exactly.
assert delta_lo > Fraction(1, (1 << 41) - 1)
assert delta_lo > Fraction(1, 3**26)

# Universal endpoint-lift positivity margins.
# For q<=T-26, q+1<=T-25 and 1-exp(-x3)<x3.
assert 2*x3_hi*(T-25) < 1
# For p>=T+26, L-p<=P-26 and 1-exp(-x2)<x2.
assert 2*x2_hi*(P-26) < 1

# Exact high-end exponent cutoff.
assert b(T) == S-1
assert b(T+26) == S+41

# Therefore any owned nonzero excursion must satisfy
#   p <= T+25 and q >= T-25.
low_last_defect_excluded_through = T-26
high_first_defect_excluded_from = T+26
assert low_last_defect_excluded_through == 72_057_431_965
assert high_first_defect_excluded_from == 72_057_432_017

# Countermodel: one connected height-one run h_j=1 for 2<=j<=T.
# It is legal because the only rise is at j=1 and c_1=2; plateau and drop
# satisfy a_j=c_j+h_j-h_(j+1)>=1.
assert c(1) == 2
p = 2
q = T
run_count = T-1
assert b(p) == 3

# Its real quotient Q_h/D lies strictly inside the inherited state window.
# Put rho_j=2^b_j/3^j.  The global floor lock gives 1/2<rho_j<1.
# Outside the run the weight is 1; inside it is 1/2.
# outside count = L-(T-1)=P+1.
num_lower = Fraction(P+1, 2) + Fraction(T-1, 4)
num_upper = Fraction(P+1, 1) + Fraction(T-1, 2)
# Actual denominator is 3*(exp(Delta)-1), with
# 3*delta_lo < denominator < 3*em1_hi.
assert num_lower > (1 << 71) * 3 * em1_hi
assert num_upper < (1 << 75) * 3 * delta_lo

# Yet both endpoint lifts are far too large for the hoped-for small-lift
# bridge.  For the last-defect 3-lift, q=T and P+q=L.
# K3/3^L > 1-2*x3*(T-1) > 1/4, while D/3^L=exp(Delta)-1<1/1000.
assert 1 - 2*x3_hi*run_count > Fraction(1,4)
assert em1_hi < Fraction(1,1000)

# For the first-defect 2-lift, all T-1 defect terms obey the same theta<1
# bound.  Thus K2/2^(S+A-b_p) > 1-2*x2*(T-1) > 1/8.
# With b_p=3 this is >2^(S+A-6)>2^A>D.
assert 1 - 2*x2_hi*run_count > Fraction(1,8)
assert S > 6

print("FINAL_CHANCE Session 5 endpoint-lift obstruction verifier: PASS")
print("A,L,M =", (A,L,M))
print("P,U,T,S =", (P,U,T,S))
print("global floor lock delta_hi*L < ln2_lo = True")
print("owned last defect q <=", low_last_defect_excluded_through, "= impossible")
print("owned first defect p >=", high_first_defect_excluded_from, "= impossible")
print("owner endpoint span forced: p <=", T+25, "and q >=", T-25)
print("countermodel = connected height-one run 2..T")
print("countermodel run length =", run_count)
print("countermodel real quotient in [2^71,2^75) = True")
print("countermodel K3 > D = True")
print("countermodel K2 > D = True")
print("scope=structural endpoint-size countermodel; full ownership not asserted")
