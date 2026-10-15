#!/usr/bin/env python3
"""Exact RL342 CRT boundary diagnostic (not an authoritative certificate)."""
from fractions import Fraction as F

A, ELL = 217976794617, 137528045312
LOW, UP = 1 << 71, (1 << 76) + (1 << 36)
P0, PS = 23912137200748175205995, 77998046721343488
X0, XS = 30676695662567844669575, 100063090197999414
E0, ES = 42510466134663422588435, 138663194171277312
PRE = (1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1)
MID = (3, 1, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1)
SUC = (1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 3, 1)


def bounds(base, step):
    return -((base - LOW) // step), (UP - 1 - base) // step


def states(source, gaps):
    result = [source]
    for gap in gaps:
        numerator = (1 << gap) * result[-1] - 1
        assert numerator % 3 == 0
        state = numerator // 3
        assert state > 0 and state % 2 == 1
        result.append(state)
    return result


def log_interval(x, terms=100):
    x2, term, total = x * x, x, F(0)
    for j in range(terms):
        total += term / (2 * j + 1)
        term *= x2
    lo = 2 * total
    return lo, lo + 2 * term / ((2 * terms + 1) * (1 - x2))


assert PS == (1 << 26) * 3**19
assert XS == 3**len(PRE) * PS // (1 << sum(PRE))
assert ES == 16 * PS // 9
lo = max(bounds(base, step)[0] for base, step in ((P0, PS), (X0, XS), (E0, ES)))
hi = min(bounds(base, step)[1] for base, step in ((P0, PS), (X0, XS), (E0, ES)))
assert (lo, hi) == (-276301, 238328)
assert PS % (2 * 3**len(MID)) == 0
assert XS % (2 * 3**len(PRE)) == 0
assert ES % (2 * 3**len(SUC)) == 0

for k in (lo, -1, 0, hi):
    p, x, e = P0 + PS * k, X0 + XS * k, E0 + ES * k
    assert LOW <= p < UP and LOW <= x < UP and LOW <= e < UP
    assert states(x, PRE)[-1] == p
    assert states(p, MID)[2] == e
    states(e, SUC)

l2lo, l2hi = log_interval(F(1, 3))
l3lo, l3hi = log_interval(F(1, 2))
delta_lo, delta_hi = A * l2lo - ELL * l3hi, A * l2hi - ELL * l3lo
assert delta_lo > 0
x0, xm1 = F(5, 16 * P0), F(5, 16 * (P0 - PS))
assert 2 * delta_lo / ELL > x0 / (1 - x0)
assert 2 * delta_hi / ELL < xm1
print('RL343_PHASE_BOUNDARY_GREEN')
print('band-compatible progression', lo, hi, 'count', hi - lo + 1)
print('phase-nondecreasing progression', 0, hi, 'count', hi + 1)
print('phase-decreasing progression', lo, -1, 'count', -lo)
