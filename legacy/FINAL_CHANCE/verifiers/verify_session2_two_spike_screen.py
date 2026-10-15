#!/usr/bin/env python3
"""FINAL_CHANCE Session 2 two-spike verifier/screen.

Screens every admissible area-2 two-spike profile h_p=h_q=1 with
1 <= p < q <= 1000 for the first-survivor g=1 counts
A=217976794617, L=137528045312.

A rise into the first spike requires c_{p-1}=2.  For a nonadjacent second
spike, c_{q-1}=2 is also required; for q=p+1 there is no second rise and no
condition on c_p.  This gives 170651 admissible pairs in the stated window.

For every pair this script evaluates an outward interval for

    Q_{p,q}/D = [S - (rho_p+rho_q)/2] / [3(exp(Delta)-1)],

where
    D     = 2^A - 3^L,
    Delta = A ln 2 - L ln 3,
    b_j   = floor(A j/L),
    rho_j = 2^b_j / 3^j,
    S     = sum_{j=0}^{L-1} rho_j.

S and exp(Delta)-1 use the same rigorous interval machinery as the Session 1
verifier.  Only the Python standard library is required.  This file expects
verify_session1_interval.py in the same directory.
"""

from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING

from verify_session1_interval import (
    A, L, PREC, CTX_D, CTX_U, Interval, rop,
    iadd, isub, imul, idiv,
    rat_interval, fraction_interval,
    floor_sum_F, ln_integer_bounds, expm1_bounds,
)

LIMIT = 1000


def b(j):
    return (A * j) // L


def c(j):
    return b(j + 1) - b(j)


def nearest_integer_distance_interval(x):
    """Return rigorous (d_lo,d_hi,nearest_int) for distance to nearest integer."""
    flo = int(x.lo.to_integral_value(rounding=ROUND_FLOOR))
    cei = int(x.hi.to_integral_value(rounding=ROUND_CEILING))

    candidates = {flo, flo + 1, cei - 1, cei}
    best = None
    for n in candidates:
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


def pair_admissible(p, q):
    assert 1 <= p < q <= LIMIT
    if c(p - 1) != 2:
        return False
    return q == p + 1 or c(q - 1) == 2


def main():
    l2_lo, l2_hi = ln_integer_bounds(2, 300)
    l3_lo, l3_hi = ln_integer_bounds(3, 400)
    delta_lo = A * l2_lo - L * l3_hi
    delta_hi = A * l2_hi - L * l3_lo
    assert 0 < delta_lo < delta_hi
    e_lo, e_hi = expm1_bounds(delta_lo, delta_hi, 20)
    E = Interval(fraction_interval(e_lo).lo, fraction_interval(e_hi).hi)

    S = floor_sum_F(L, A, rat_interval(1, 3), Interval(2))
    denom = imul(Interval(3), E)
    base = idiv(S, denom)
    half_over_denom = idiv(Interval(1), imul(Interval(6), E))

    rise_admissible = [p for p in range(1, LIMIT + 1) if c(p - 1) == 2]
    assert len(rise_admissible) == 584

    pairs = [
        (p, q)
        for p in range(1, LIMIT)
        for q in range(p + 1, LIMIT + 1)
        if pair_admissible(p, q)
    ]
    assert len(pairs) == 170_651
    adjacent_extra = sum(1 for p, q in pairs if q == p + 1 and c(q - 1) != 2)
    assert adjacent_extra == 415

    needed_positions = sorted({j for pair in pairs for j in pair})
    rho = {j: rat_interval(2 ** b(j), 3 ** j) for j in needed_positions}

    records = []
    possible_owners = []

    for p, q in pairs:
        qint = isub(base, imul(half_over_denom, iadd(rho[p], rho[q])))
        dlo, dhi, nearest = nearest_integer_distance_interval(qint)
        if dlo == 0:
            possible_owners.append((p, q, qint, nearest))
        records.append((dlo, dhi, p, q, qint, nearest))

    assert len(records) == 170_651
    assert not possible_owners

    by_upper = sorted(records, key=lambda z: (z[1], z[0], z[2], z[3]))
    best = by_upper[0]
    second = by_upper[1]
    best_lo, best_hi, p, q, qint, nearest = best
    second_lo, second_hi, p2, q2, qint2, nearest2 = second

    assert (p, q) == (498, 972)
    assert (p2, q2) == (431, 549)

    min_other_lower = min(r[0] for r in records if (r[2], r[3]) != (p, q))
    assert best_hi < min_other_lower

    c497 = c(497)
    c498 = c(498)
    c971 = c(971)
    c972 = c(972)
    a497 = c497 - 1
    a498 = c498 + 1
    a971 = c971 - 1
    a972 = c972 + 1
    assert min(a497, a498, a971, a972) >= 1

    width_hi = rop(CTX_U, lambda: qint.hi - qint.lo)
    sep_lo = rop(CTX_D, lambda: min_other_lower - best_hi)

    print("FINAL_CHANCE Session 2 two-spike screen: PASS")
    print("A =", A)
    print("L =", L)
    print("screen phases = 1..", LIMIT)
    print("rise-admissible spike positions =", len(rise_admissible))
    print("additional admissible adjacent pairs =", adjacent_extra)
    print("screened admissible pairs =", len(records))
    print("formula = (S-(rho_p+rho_q)/2)/(3*(exp(Delta)-1))")
    print("Delta = A*ln(2)-L*ln(3)")
    print("rho_j = 2^floor(A*j/L)/3^j")
    print("S = sum_{j=0}^{L-1} rho_j")
    print("precision_digits =", PREC)
    print("possible owned pair in screen = False")
    print("closest pair =", (p, q))
    print("b_p,b_q =", (b(p), b(q)))
    print("modified exponents a_497,a_498,a_971,a_972 =",
          (a497, a498, a971, a972))
    print("Q_pq/D lower =", qint.lo)
    print("Q_pq/D upper =", qint.hi)
    print("interval width <=", width_hi)
    print("nearest integer =", nearest)
    print("closest miss distance lower =", best_lo)
    print("closest miss distance upper =", best_hi)
    print("second closest pair =", (p2, q2))
    print("second miss distance lower =", second_lo)
    print("second miss distance upper =", second_hi)
    print("minimum lower bound over all OTHER pairs =", min_other_lower)
    print("winner separated from whole field by >=", sep_lo)


if __name__ == "__main__":
    main()
