#!/usr/bin/env python3
"""FINAL_CHANCE Session 5 verifier: exact ownership boundary-collar reduction.

Scope: the fixed first-survivor g=1 branch
  A=217976794617, L=137528045312,
with inherited physical least-state window 2^71 < m < 2^75.

This verifier does NOT enumerate defect area or height. It uses only:
  * the exact accelerated Collatz recurrence;
  * nonnegative defect h_j=b_j-S_j and least-root y_j>=m;
  * the state window;
  * the first-positive / last-positive defect boundary conditions.

It proves that if p is the first positive defect phase and q the last, then
  p + (L-q) <= 37.
"""

A = 217_976_794_617
L = 137_528_045_312
LOW = 1 << 71
HIGH = 1 << 75
FORWARD_CHECK = 200


def b(j: int) -> int:
    return (A * j) // L


def c(j: int) -> int:
    return b(j + 1) - b(j)


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def forward_failure(m: int, steps: int = FORWARD_CHECK):
    """Return first failure of inherited physical conditions, or None."""
    if m <= 0 or m % 2 == 0:
        return (0, "not_positive_odd")
    y = m
    S = 0
    for j in range(steps):
        z = 3 * y + 1
        a = v2(z)
        assert a >= 1
        S += a
        y = z >> a
        h = b(j + 1) - S
        if h < 0:
            return (j + 1, "negative_defect")
        if y < m:
            return (j + 1, "below_least_state")
    return None


def interval_progression(base: int, modulus: int):
    """Integers m in [LOW,HIGH) with m == base mod modulus."""
    base %= modulus
    k0 = max(0, (LOW - base + modulus - 1) // modulus)
    k1 = (HIGH - 1 - base) // modulus
    if k1 < k0:
        return range(0)
    return range(k0, k1 + 1)


def mechanical_prefix_candidates(n: int):
    """Candidates having h_0=...=h_n=0, checked for exact valuations."""
    S = b(n)
    mod = 1 << S
    C = sum(3 ** (n - 1 - k) * (1 << b(k)) for k in range(n))
    r = (-C * pow(3 ** n, -1, mod)) % mod
    out = []
    for kk in interval_progression(r, mod):
        m = r + kk * mod
        y = m
        ok = m > 0 and (m & 1)
        for j in range(n):
            if not ok:
                break
            z = 3 * y + 1
            a = v2(z)
            if a != c(j):
                ok = False
                break
            y = z >> a
            if y < m:
                ok = False
                break
        if ok:
            out.append(m)
    return out


def mechanical_suffix_residue(n: int):
    """m residue mod 3^n if the final n defect heights are all zero."""
    q = L - n
    exps = [c(j) for j in range(q, L)]
    ps = [0]
    for a in exps:
        ps.append(ps[-1] + a)
    T = ps[-1]
    C = sum(3 ** (n - 1 - k) * (1 << ps[k]) for k in range(n))
    mod = 3 ** n
    return (C * pow(1 << T, -1, mod)) % mod, mod


def first_defect_cylinder(p: int):
    """Exact 2-adic cylinder when p is the first positive defect phase.

    Then h_0=...=h_(p-1)=0, h_p=1, so c_(p-1)=2 and the
    p-th accelerated exponent is 1. Exact oddness of y_p selects one lift
    modulo 2^b_p.
    """
    assert p >= 1 and c(p - 1) == 2
    exps = [c(j) for j in range(p - 1)] + [1]
    ps = [0]
    for a in exps:
        ps.append(ps[-1] + a)
    S = ps[-1]
    assert S == b(p) - 1
    C = sum(3 ** (p - 1 - k) * (1 << ps[k]) for k in range(p))
    mod = 1 << S
    r = (-C * pow(3 ** p, -1, mod)) % mod
    exact_mod = 2 * mod
    lifts = []
    for rr in (r, r + mod):
        num = 3 ** p * rr + C
        assert num % mod == 0
        if (num // mod) & 1:
            lifts.append(rr % exact_mod)
    assert len(lifts) == 1
    assert exact_mod == 1 << b(p)
    return lifts[0], exact_mod


def last_defect_cylinder(n: int, parity: int, representative_height=None):
    """Exact 3-adic cylinder when q=L-n is the last positive defect.

    The height h_q can be arbitrarily large. Its suffix residue depends only
    on parity(h_q). parity=1 means odd, parity=0 means even.
    """
    assert 1 <= n <= 48 and parity in (0, 1)
    q = L - n
    h = representative_height
    if h is None:
        h = 1 if parity else 2
    assert h >= 1 and h % 2 == parity
    exps = [c(q) + h] + [c(j) for j in range(q + 1, L)]
    ps = [0]
    for a in exps:
        ps.append(ps[-1] + a)
    T = ps[-1]
    C = sum(3 ** (n - 1 - k) * (1 << ps[k]) for k in range(n))
    mod = 3 ** n
    return (C * pow(1 << T, -1, mod)) % mod, mod


def crt(r1: int, m1: int, r2: int, m2: int):
    assert __import__("math").gcd(m1, m2) == 1
    k = ((r2 - r1) * pow(m1, -1, m2)) % m2
    x = r1 + m1 * k
    return x, m1 * m2


def main():
    assert b(47) == 74
    assert b(48) == 76

    # If no positive defect occurs through phase 47, there is exactly one
    # state in the inherited state window with the exact mechanical prefix.
    # Its next actual accelerated step overshoots the nonnegative-defect wall.
    mech47 = mechanical_prefix_candidates(47)
    assert mech47 == [23_587_405_242_550_913_489_915]
    assert forward_failure(mech47[0], 48) == (48, "negative_defect")

    first_positions = [p for p in range(1, 48) if c(p - 1) == 2]
    assert len(first_positions) == 27
    assert first_positions == [
        2, 4, 6, 7, 9, 11, 12, 14, 16, 18, 19, 21, 23, 24,
        26, 28, 30, 31, 33, 35, 36, 38, 40, 42, 43, 45, 47,
    ]

    # If the last defect were earlier than L-48, the final 48 heights would
    # all be zero. The resulting exact 3-adic residue has no representative
    # in the inherited least-state window. Hence n=L-q<=48.
    r48, mod48 = mechanical_suffix_residue(48)
    assert not list(interval_progression(r48, mod48))

    # Audit the key height-independence: the last-defect suffix cylinder
    # depends only on parity of the terminal defect height.
    for n in range(1, 49):
        assert last_defect_cylinder(n, 1, 1) == last_defect_cylinder(n, 1, 3)
        assert last_defect_cylinder(n, 0, 2) == last_defect_cylinder(n, 0, 4)

    # Attack every boundary signature with p+n >= 38.
    signature_count = 0
    candidate_count = 0
    distinct_candidates = set()
    failure_cache = {}
    max_failure_step = 0

    for p in first_positions:
        rp, mp = first_defect_cylinder(p)
        for n in range(1, 49):
            if p + n < 38:
                continue
            for parity in (0, 1):
                signature_count += 1
                rt, mt = last_defect_cylinder(n, parity)
                x, mod = crt(rp, mp, rt, mt)
                for kk in interval_progression(x, mod):
                    m = x + kk * mod
                    candidate_count += 1
                    distinct_candidates.add(m)
                    if m not in failure_cache:
                        failure_cache[m] = forward_failure(m)
                    failure = failure_cache[m]
                    assert failure is not None, (p, n, parity, m)
                    max_failure_step = max(max_failure_step, failure[0])

    assert signature_count == 1848
    assert candidate_count == 2_056_165
    assert len(distinct_candidates) == 1_370_780
    assert max_failure_step == 194

    residual_signatures = [
        (p, n, parity)
        for p in first_positions
        for n in range(1, 49)
        if p + n <= 37
        for parity in (0, 1)
    ]
    residual_first_positions = sorted({p for p, _, _ in residual_signatures})
    assert len(residual_signatures) == 744
    assert len(residual_first_positions) == 21
    assert residual_first_positions[-1] == 36

    print("FINAL_CHANCE Session 5 ownership boundary-collar verifier: PASS")
    print("A,L =", (A, L))
    print("least-state window = [2^71, 2^75)")
    print("mechanical-prefix-through-47 candidates =", len(mech47))
    print("mechanical-prefix candidate fails nonnegative defect at phase = 48")
    print("first-defect positions <=47 =", len(first_positions))
    print("mechanical final-48 suffix has state-window candidate = False")
    print("last-defect suffix depends only on terminal-height parity = True")
    print("boundary signatures attacked with p+(L-q)>=38 =", signature_count)
    print("state candidates checked across those signatures =", candidate_count)
    print("distinct state candidates checked =", len(distinct_candidates))
    print("latest rejection phase =", max_failure_step)
    print("surviving owner must satisfy p+(L-q) <= 37 = True")
    print("residual boundary signatures =", len(residual_signatures))
    print("residual first-defect positions =", len(residual_first_positions))
    print("scope=full-owner boundary reduction; no defect-area/height enumeration")


if __name__ == "__main__":
    main()
