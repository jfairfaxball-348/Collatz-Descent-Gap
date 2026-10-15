#!/usr/bin/env python3
"""FINAL_CHANCE Session 1 verifier.

Reproduces a rigorous high-precision interval for Q_h/D at
A=217976794617, L=137528045312 and defect profile h_2=h_4=1.

The script never materializes 2^A, 3^L, D, or Q_h.  It uses:
  * exact Fraction bounds for ln(2), ln(3) from the atanh series;
  * an exact Fraction Taylor/remainder bound for exp(Delta)-1;
  * outward-rounded Decimal interval arithmetic for the Beatty sum
        S = sum_{j=0}^{L-1} 2^floor(Aj/L) / 3^j;
  * Euclidean reciprocity for the bivariate floor-sum generating function.

Decimal powers are formed only by repeated directed multiplication; this
avoids Decimal.__pow__, whose implementation is not guaranteed to be
correctly rounded in every case.

Only the Python standard library is required.
"""

from decimal import (
    Decimal, Context, localcontext,
    ROUND_FLOOR, ROUND_CEILING,
    MAX_EMAX, MIN_EMIN,
)
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
PREC = 140

CTX_D = Context(prec=PREC, rounding=ROUND_FLOOR,
                Emin=MIN_EMIN, Emax=MAX_EMAX, traps=[])
CTX_U = Context(prec=PREC, rounding=ROUND_CEILING,
                Emin=MIN_EMIN, Emax=MAX_EMAX, traps=[])


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        if hi is None:
            hi = lo
        self.lo = lo if isinstance(lo, Decimal) else Decimal(lo)
        self.hi = hi if isinstance(hi, Decimal) else Decimal(hi)
        assert self.lo <= self.hi


def rop(ctx, fn):
    with localcontext(ctx):
        return fn()


def iadd(a, b):
    return Interval(
        rop(CTX_D, lambda: a.lo + b.lo),
        rop(CTX_U, lambda: a.hi + b.hi),
    )


def isub(a, b):
    return Interval(
        rop(CTX_D, lambda: a.lo - b.hi),
        rop(CTX_U, lambda: a.hi - b.lo),
    )


def imul(a, b):
    lows = []
    highs = []
    for x in (a.lo, a.hi):
        for y in (b.lo, b.hi):
            lows.append(rop(CTX_D, lambda x=x, y=y: x * y))
            highs.append(rop(CTX_U, lambda x=x, y=y: x * y))
    return Interval(min(lows), max(highs))


def idiv(a, b):
    assert not (b.lo <= 0 <= b.hi)
    lows = []
    highs = []
    for x in (a.lo, a.hi):
        for y in (b.lo, b.hi):
            lows.append(rop(CTX_D, lambda x=x, y=y: x / y))
            highs.append(rop(CTX_U, lambda x=x, y=y: x / y))
    return Interval(min(lows), max(highs))


def ipow(a, n):
    """Rigorous nonnegative integer power via directed multiplication."""
    assert n >= 0 and a.lo >= 0
    result = Interval(1)
    base = a
    while n:
        if n & 1:
            result = imul(result, base)
        n >>= 1
        if n:
            base = imul(base, base)
    return result


ONE = Interval(1)


def rat_interval(p, q=1):
    return Interval(
        rop(CTX_D, lambda: Decimal(p) / Decimal(q)),
        rop(CTX_U, lambda: Decimal(p) / Decimal(q)),
    )


def fraction_interval(fr):
    return rat_interval(fr.numerator, fr.denominator)


def geom(z, n):
    """Interval for 1+z+...+z^(n-1)."""
    if n == 0:
        return Interval(0)
    if z.lo == z.hi == 1:
        return Interval(n)
    return idiv(isub(ONE, ipow(z, n)), isub(ONE, z))


def floor_sum_F(m, n, x, y):
    """Outward interval for sum_{j=0}^{m-1} x^j y^floor(nj/m).

    Euclidean reductions:
      n = q m + r  => F(m,n;x,y)=F(m,r;x*y^q,y).

    For 0<n<m and m=q n+r, r>0:
      a = y^(n-1) x^m,
      F = [1-a + (y-1)a(F(n,r;1/(y x^q),1/x)-1)]/(1-x).

    If r=0 the sum splits into two finite geometric sums.
    """
    assert m >= 1 and n >= 0
    if n == 0:
        return geom(x, m)
    if n >= m:
        q, r = divmod(n, m)
        return floor_sum_F(m, r, imul(x, ipow(y, q)), y)

    q, r = divmod(m, n)
    if r == 0:
        first = geom(x, q)
        second = geom(imul(y, ipow(x, q)), n)
        return imul(first, second)

    a = imul(ipow(y, n - 1), ipow(x, m))
    xp = idiv(ONE, imul(y, ipow(x, q)))
    yp = idiv(ONE, x)
    rec = floor_sum_F(n, r, xp, yp)
    num = iadd(
        isub(ONE, a),
        imul(imul(isub(y, ONE), a), isub(rec, ONE)),
    )
    return idiv(num, isub(ONE, x))


def ln_integer_bounds(n, terms):
    """Exact Fraction bounds for ln(n) using 2*atanh((n-1)/(n+1))."""
    z = Fraction(n - 1, n + 1)
    z2 = z * z
    zp = z
    s = Fraction(0)
    for k in range(terms):
        s += Fraction(2, 2 * k + 1) * zp
        zp *= z2
    tail = Fraction(2, 1) * zp / Fraction(2 * terms + 1, 1) / (1 - z2)
    return s, s + tail


def expm1_bounds(lo, hi, terms=20):
    """Exact Fraction bounds for exp(x)-1 on 0<=lo<=x<=hi<1."""
    assert 0 <= lo <= hi < 1

    lower = Fraction(0)
    p = Fraction(1)
    fact = 1
    for k in range(1, terms + 1):
        p *= lo
        fact *= k
        lower += p / fact

    upper_partial = Fraction(0)
    p = Fraction(1)
    fact = 1
    for k in range(1, terms + 1):
        p *= hi
        fact *= k
        upper_partial += p / fact

    tail = (p * hi) / (fact * (terms + 1)) / (1 - hi)
    return lower, upper_partial + tail


def main():
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

    S = floor_sum_F(L, A, rat_interval(1, 3), Interval(2))

    numerator = isub(S, rat_interval(68, 81))
    denominator = imul(Interval(3), expm1_delta)
    quotient = idiv(numerator, denominator)

    floor_lo = int(quotient.lo.to_integral_value(rounding=ROUND_FLOOR))
    floor_hi = int(quotient.hi.to_integral_value(rounding=ROUND_FLOOR))
    assert floor_lo == floor_hi
    next_integer = Decimal(floor_lo + 1)
    floor_decimal = Decimal(floor_lo)
    assert quotient.lo > floor_decimal
    assert quotient.hi < next_integer

    width_hi = rop(CTX_U, lambda: quotient.hi - quotient.lo)
    dist_above = rop(CTX_D, lambda: quotient.lo - floor_decimal)
    dist_below = rop(CTX_D, lambda: next_integer - quotient.hi)

    print("FINAL_CHANCE Session 1 interval verifier: PASS")
    print("A =", A)
    print("L =", L)
    print("profile = h_2=h_4=1, all other h_j=0")
    print("method = exact rational log/expm1 bounds + directed-multiplication Decimal intervals")
    print("precision_digits =", PREC)
    print("Q_h/D lower =", quotient.lo)
    print("Q_h/D upper =", quotient.hi)
    print("interval width <=", width_hi)
    print("common integer part =", floor_lo)
    print("distance above floor >=", dist_above)
    print("distance below next integer >=", dist_below)
    print("D divides Q_h = False")


if __name__ == "__main__":
    main()
