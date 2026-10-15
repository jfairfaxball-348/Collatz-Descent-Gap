#!/usr/bin/env python3
"""FINAL_CHANCE Session 3 verifier: global exclusion of defect area exactly 2.

Scope:
  A=217976794617, L=137528045312, g=1 first-survivor branch.

This verifier supports the Session 3 analytic proof in two pieces.

1. Non-adjacent two-spike profiles.
   Both spike residues lie below M=A-L.  The full ownership polynomial
   collapses after multiplication by T-1 to a five-term polynomial E(T).
   A resultant + discrete Parseval bound gives

       0 < |Res(2T^L-1,E)| < 2^(A-41) < D,

   contradicting the necessary divisibility D | Res.

   The symbolic inequalities are explained in the ledger.  This script checks
   every finite arithmetic/log inequality used by that bound.

2. Adjacent two-spike profiles.
   Two complementary integer lifts exclude every adjacent pair except 52
   indices p in [T-26,T+25].  For those 52, the script rigorously encloses
   N_3/D, where D | N_3 is necessary for ownership, and verifies that no
   enclosure meets an integer.

Only the Python standard library is required.  It imports the repaired
Session 1 interval primitives from the same directory.
"""

from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from math import gcd

from verify_session1_interval import (
    A, L, PREC, CTX_D, CTX_U, Interval, rop,
    iadd, isub, imul, idiv,
    rat_interval, fraction_interval,
    ln_integer_bounds, expm1_bounds,
)

M = A - L

# Bezout/convergent data.
P = 65_470_613_321
U = 103_768_467_013
T = L - P
S = A - U

RESULTANT_POWER_CUTOFF = 1828


def b(j):
    return (A * j) // L


def c(j):
    return b(j + 1) - b(j)


def nearest_integer_distance_interval(x):
    """Rigorous interval for distance from x to its nearest integer."""
    flo = int(x.lo.to_integral_value(rounding=ROUND_FLOOR))
    cei = int(x.hi.to_integral_value(rounding=ROUND_CEILING))
    best = None
    for n in {flo, flo + 1, cei - 1, cei}:
        nd = Decimal(n)
        if x.lo <= nd <= x.hi:
            dlo = Decimal(0)
            dhi = max(
                rop(CTX_U, lambda nd=nd: nd - x.lo),
                rop(CTX_U, lambda nd=nd: x.hi - nd),
            )
        elif nd < x.lo:
            dlo = rop(CTX_D, lambda nd=nd: x.lo - nd)
            dhi = rop(CTX_U, lambda nd=nd: x.hi - nd)
        else:
            dlo = rop(CTX_D, lambda nd=nd: nd - x.hi)
            dhi = rop(CTX_U, lambda nd=nd: nd - x.lo)
        item = (dlo, dhi, n)
        if best is None or item[1] < best[1]:
            best = item
    return best


def main():
    # Exact arithmetic identities.
    assert gcd(A, L) == 1
    assert A * P - U * L == 1
    assert A * T - S * L == -1
    assert P + T == L
    assert U + S == A
    assert M == 80_448_749_305
    assert L % 2 == 0

    # Exact rational log enclosures.
    l2_lo, l2_hi = ln_integer_bounds(2, 300)
    l3_lo, l3_hi = ln_integer_bounds(3, 400)

    delta_lo = A * l2_lo - L * l3_hi
    delta_hi = A * l2_hi - L * l3_lo
    assert 0 < delta_lo < delta_hi

    # One lower bound powers all three size comparisons used in the proof.
    # If Delta > 1/(2^41-1), then
    #   1-exp(-Delta) > Delta/(1+Delta) > 2^-41,
    # hence D > 2^(A-41).
    assert delta_lo > Fraction(1, (1 << 41) - 1)
    assert delta_lo > Fraction(1, 3**26)

    # The two near-unity Bezout ratios lie strictly below 1 but above 1/2.
    # x3 = P ln3 - U ln2 > 0 gives 2^U/3^P = exp(-x3).
    x3_lo = P * l3_lo - U * l2_hi
    x3_hi = P * l3_hi - U * l2_lo
    assert 0 < x3_lo < x3_hi < l2_lo

    # x2 = S ln2 - T ln3 > 0 gives 3^T/2^S = exp(-x2).
    x2_lo = S * l2_lo - T * l3_hi
    x2_hi = S * l2_hi - T * l3_lo
    assert 0 < x2_lo < x2_hi < l2_lo

    # ---------- non-adjacent global resultant bound ----------
    #
    # For non-adjacent area-2 spikes, each rise requires c_(j-1)=2.
    # With r_j = A*j mod L this is equivalent to 1 <= r_j < M.
    #
    # Ownership gives E(rho)=0 mod D for
    #   E(T)=1+(T-1)(T^r+T^s),  1<=r,s<M.
    # B(T)=2T^L-1 is irreducible and deg E <= M < L, so Res(B,E) != 0.
    #
    # If alpha=2^(-1/L), discrete Parseval plus AM-GM gives
    #   |Res(B,E)| <= 2^m V_m^(L/2), m=deg E<=M.
    # The bound is increasing in m, and at M:
    #   V_M < 319/81.
    # Therefore
    #   |Res| < 2^A (319/324)^(L/2).
    #
    # The following exact integer checks show
    #   (319/324)^(L/2) < 2^-41,
    # hence |Res| < 2^(A-41) < D.
    assert L > 14
    assert 10**14 > 4 * 9**14       # implies 2^(2/L) < 10/9
    assert L // 2 >= RESULTANT_POWER_CUTOFF
    assert (
        319**RESULTANT_POWER_CUTOFF * 2**41
        < 324**RESULTANT_POWER_CUTOFF
    )

    # ---------- adjacent global reduction ----------
    #
    # First 3-denominator lift:
    #   N3 = 3^(P+q)
    #        +(2^U-3^P)(2^b_p 3^(q-p)+2^b_q).
    # Ownership => D | N3, while 0<N3<3^(P+q).
    # Thus q<=T-26 is impossible because 3^(L-26)<D.
    #
    # Complementary 2-denominator lift:
    #   N2 = 2^(S+A-b_p)
    #        +(3^T-2^S)(3^(L-p)+3^(L-q)2^(b_q-b_p)).
    # Ownership => D | N2, while 0<N2<2^(S+A-b_p).
    # p>=T+26 is impossible because b_(T+26)=S+41 and 2^(A-41)<D.
    assert b(T) == S - 1
    assert b(T + 26) == S + 41
    assert b(T + 25) == S + 39

    residual_p = list(range(T - 26, T + 26))
    assert len(residual_p) == 52

    # Rigorous interval for E_D = exp(Delta)-1.
    e_lo, e_hi = expm1_bounds(delta_lo, delta_hi, 20)
    E_D = Interval(fraction_interval(e_lo).lo, fraction_interval(e_hi).hi)

    # epsilon3 = 1 - 2^U/3^P = 1-exp(-x3)
    #          = expm1(x3)/(1+expm1(x3)).
    e3_lo, e3_hi = expm1_bounds(x3_lo, x3_hi, 20)
    e3 = Interval(fraction_interval(e3_lo).lo, fraction_interval(e3_hi).hi)
    epsilon3 = idiv(e3, iadd(Interval(1), e3))

    # rho_T = 2^(S-1)/3^T = exp(x2)/2.
    e2_lo, e2_hi = expm1_bounds(x2_lo, x2_hi, 20)
    e2 = Interval(fraction_interval(e2_lo).lo, fraction_interval(e2_hi).hi)
    rho_T = idiv(iadd(Interval(1), e2), Interval(2))

    # Build only the 53 rho_j values needed for the 52 residual adjacent pairs.
    # rho_(j+1)/rho_j = 2^c_j / 3 exactly.
    rho = {T: rho_T}
    for j in range(T - 1, T - 27, -1):
        rho[j] = imul(rho[j + 1], rat_interval(3, 2**c(j)))
    for j in range(T, T + 26):
        rho[j + 1] = imul(rho[j], rat_interval(2**c(j), 3))

    assert min(rho) == T - 26
    assert max(rho) == T + 26
    assert len(rho) == 53

    records = []
    integer_hits = []

    for p in residual_p:
        q = p + 1
        # N3/D = 3^(P+q-L) *
        #         [1-epsilon3(rho_p+rho_q)] / (exp(Delta)-1).
        factor = isub(
            Interval(1),
            imul(epsilon3, iadd(rho[p], rho[q])),
        )
        assert factor.lo > 0

        k = q - T   # because P+T=L
        scale = (
            rat_interval(3**k)
            if k >= 0
            else rat_interval(1, 3**(-k))
        )
        ratio = idiv(imul(scale, factor), E_D)
        dlo, dhi, nearest = nearest_integer_distance_interval(ratio)

        if dlo == 0:
            integer_hits.append((p, q, ratio, nearest))
        records.append((dlo, dhi, p, q, ratio, nearest))

    assert not integer_hits
    assert len(records) == 52

    best = min(records, key=lambda z: (z[1], z[0], z[2]))
    best_lo, best_hi, p, q, ratio, nearest = best

    assert p == T + 9
    assert q == T + 10

    min_other_lower = min(
        r[0] for r in records if (r[2], r[3]) != (p, q)
    )
    assert best_hi < min_other_lower

    width_hi = rop(CTX_U, lambda: ratio.hi - ratio.lo)
    separation_lo = rop(CTX_D, lambda: min_other_lower - best_hi)

    print("FINAL_CHANCE Session 3 global area-2 verifier: PASS")
    print("A,L,M =", (A, L, M))
    print("Bezout P,U =", (P, U))
    print("complement T,S =", (T, S))
    print("Delta lower > 1/(2^41-1) = True")
    print("non-adjacent resultant cutoff exponent =", RESULTANT_POWER_CUTOFF)
    print("(319/324)^1828 < 2^-41 = True")
    print("non-adjacent area-2 owner possible = False")
    print("adjacent low exclusion: q <=", T - 26)
    print("adjacent high exclusion: p >=", T + 26)
    print("residual adjacent pairs checked =", len(records))
    print("residual integer hit = False")
    print("closest residual pair =", (p, q))
    print("offsets from T =", (p - T, q - T))
    print("N3/D lower =", ratio.lo)
    print("N3/D upper =", ratio.hi)
    print("interval width <=", width_hi)
    print("nearest integer =", nearest)
    print("closest miss distance lower =", best_lo)
    print("closest miss distance upper =", best_hi)
    print("minimum lower bound over all OTHER residual pairs =", min_other_lower)
    print("winner separated from residual field by >=", separation_lo)
    print("GLOBAL defect-area-2 owner possible = False")


if __name__ == "__main__":
    main()
