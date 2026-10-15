#!/usr/bin/env python3
"""DG006: bounded, exact arithmetic regression only. E=empty remains OPEN.

All examples are finite Collatz paths, not known exceptional orbits.
The universal statements in DG006.md are paper proofs, not certified here.
"""
from itertools import product


def T(n):
    assert n >= 1
    return n // 2 if n % 2 == 0 else (3*n + 1)//2


def affine(word):
    A, q, D = 1, 0, 1
    for bit in word:
        if bit == '1':
            A, q = 3*A, 3*q + D
        D *= 2
    return A, q, D


def trace(n, steps):
    out = [n]
    for _ in range(steps):
        out.append(T(out[-1]))
    return out


def local_bridge(vals):
    """Only a local prefix, NOT membership in E or a true infinite suffix record."""
    a, b = vals[0], vals[-1]
    return (a >= 3 and a % 4 == b % 4 == 3 and a < b
            and min(vals[1:-1]) > b and vals[-2] == 2*b)


def v3(n):
    r = 0
    while n % 3 == 0:
        r += 1
        n //= 3
    return r


# The parity-bridge word table is a finite exact algebra identity, not the proof
# that there are no longer paths in an infinite E-orbit.
expected = {
    3: {'110': (9, 5, 8)},
    4: {'1100': (9, 5, 16), '1110': (27, 19, 16)},
    5: {'11000': (9, 5, 32), '11010': (27, 23, 32),
        '11100': (27, 19, 32), '11110': (81, 65, 32)},
}
for d, words in expected.items():
    assert {''.join(('11', *mid, '0')) for mid in product('01', repeat=d-3)} == set(words)
    assert {w: affine(w) for w in words} == words

# Bounded seeds independently verify all possible first short bridges.
short_tested = 0
short_good = {3: 0, 4: 0, 5: 0}
for a in range(3, 40000, 4):
    for d in (3, 4, 5):
        vals = trace(a, d)
        if local_bridge(vals):
            short_good[d] += 1
            assert d == 3
            assert a % 32 == 27
            assert vals[-1] % 3 == 1
            assert vals[-1] == (9*a+5)//8
        short_tested += 1
assert short_good[3] > 0 and short_good[4] == short_good[5] == 0

# Complete finite bridge cylinders for d=3, d=6, and a deeper inverse-chain example.
ex = [(27 + 32*h, 3, 31 + 36*h) for h in (0,1,5,100)]
ex += [(71 + 256*h, 6, 91 + 324*h) for h in (0,1,5,100)]
ex += [(207 + 256*h, 6, 263 + 324*h) for h in (0,1,5,100)]
ex += [(2815 + 65536*h, 14, 3383 + 78732*h) for h in (0,1,5,100)]
# 3^9 * (2^(14+2)/2^14) = 4 * 19683 = 78732.
for a, d, b in ex:
    vals = trace(a, d)
    assert vals[-1] == b and local_bridge(vals), (a,d,b,vals)
    last_odd = max(i for i in range(d) if vals[i] % 2)
    tail = d - last_odd - 1
    assert tail >= 1
    assert b % 3 == (2 if tail % 2 == 0 else 1)
    if b % 3 == 2:
        assert (2*b-1)//3 < a

# Arbitrarily many (parameter-r) valid finite 110 bridges, each record 1 mod 3.
finite_blocks = 0
for r in range(1,9):
    n = 12 * 8**r - 5
    vals = trace(n, 3*r)
    for j in range(r):
        a = 12 * 9**j * 8**(r-j) - 5
        b = 12 * 9**(j+1) * 8**(r-j-1) - 5
        assert vals[3*j] == a and vals[3*j+3] == b
        assert a % 4 == b % 4 == 3 and a % 3 == b % 3 == 1
        assert local_bridge(vals[3*j:3*j+4])
        assert ''.join(str(x%2) for x in vals[3*j:3*j+3]) == '110'
        finite_blocks += 1
    # At the final seed-independent continuation there can be a descent;
    # do not interpret these finite records as true infinite tail minima.

# 3-adic safe inverse chains: verify the actual odd T edges and strict descent.
chain_checks = 0
for b in range(5, 100000, 2):
    if b%3 != 2: continue
    r = v3(b+1)
    assert r >= 1
    nodes = [b]
    for i in range(1, r+1):
        z = (2**i * (b+1))//3**i - 1
        assert z >= 3 and z%2 == 1 and z < nodes[-1]
        assert T(z) == nodes[-1]
        nodes.append(z)
        chain_checks += 1

assert v3(3383+1) == 2
assert (2*3383-1)//3 == 2255
assert (2*2255-1)//3 == 1503
print('Short bridge seed-length pairs:', short_tested)
print('Admissible short finite bridges d=3,4,5:', short_good)
print('Explicit local bridge cylinders:', len(ex))
print('All-1-mod-3 consecutive finite 110 blocks:', finite_blocks)
print('Safe inverse T-edges checked:', chain_checks)
print('PASS — exact bounded regression; no universal E elimination or formal proof')
