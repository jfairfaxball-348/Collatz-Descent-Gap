#!/usr/bin/env python3
"""DG008: exact finite Collatz bridge and strict safe-inverse computations.

All enumerations are symbolic integer inequalities / finite residue certificates.
They DO NOT establish existence or absence of an infinite exceptional orbit.
"""
from itertools import product


def T(n):
    assert n > 0
    return n // 2 if n % 2 == 0 else (3*n+1)//2


def prefix(word):
    p = [(1, 0, 1)]
    A, q, D = 1, 0, 1
    for bit in word:
        if bit == '1':
            A, q = 3*A, 3*q+D
        else:
            assert bit == '0'
        D *= 2
        p.append((A, q, D))
    return p


def trace(n, d):
    v = [n]
    for _ in range(d):
        v.append(T(v[-1]))
    return v


def viable(word):
    """Exact existential affine-linear feasibility over a>=3 in its cylinder."""
    p = prefix(word)
    A, q, D = p[-1]
    M = 4*D
    a0 = ((3*D-q)*pow(A, -1, M)) % M
    if a0 < 3:
        a0 += M
    lo, hi = 0, None
    # i=0 requires b>a; all 1<=i<d require x_i>b.
    for i, (Ai, qi, Di) in enumerate(p[:-1]):
        c = (D//Di)*Ai-A
        alpha = c*M
        beta = c*a0+(D//Di)*qi-q
        if i == 0:
            alpha, beta = -alpha, -beta
        if alpha > 0:
            lo = max(lo, (-beta)//alpha+1)
        elif alpha < 0:
            limit = (beta-1)//(-alpha)
            hi = limit if hi is None else min(hi, limit)
        elif beta <= 0:
            return None
        if hi is not None and lo > hi:
            return None
    a = a0+M*lo
    v = trace(a, len(word))
    assert ''.join(str(x % 2) for x in v[:-1]) == word
    assert a % 4 == v[-1] % 4 == 3
    assert a < v[-1] and min(v[1:-1]) > v[-1]
    assert v[-2] == 2*v[-1]
    slopes_positive = (A > D and all((D//Di)*Ai > A
                     for Ai, qi, Di in p[1:-1]))
    return a, v[-1], slopes_positive


bridge = {}
for d in range(3, 19):
    found = {}
    for bits in product('01', repeat=d-3):
        word = '11'+''.join(bits)+'0'
        info = viable(word)
        if info is not None:
            found[word] = info
    bridge[d] = found
expected = {3:1, 4:0, 5:0, 6:2, 7:0, 8:0, 9:7,
            10:0, 11:30, 12:0, 13:0, 14:113, 15:0,
            16:0, 17:525, 18:0}
assert {d:len(v) for d,v in bridge.items()} == expected
assert all(info[2] for fam in bridge.values() for info in fam.values())
print('Finite bridge candidate words evaluated d=3..18:', sum(2**(d-3) for d in range(3, 19)))
print('Finite locally feasible words:', expected)

# Strict-prefix safe inverse words, using 3^s>=2^i at every prefix.
safe = []
frontier = [('', 1, 0, 1)]
for d in range(1, 18):
    next_frontier = []
    for w, A, q, D in frontier:
        for bit in '01':
            AA, qq = (3*A, 3*q+D) if bit == '1' else (A, q)
            DD = 2*D
            if AA < DD:
                continue
            ww = w+bit
            next_frontier.append((ww, AA, qq, DD))
            if AA > DD:
                r = qq*pow(DD, -1, AA) % AA
                safe.append((d, ww, AA, qq, DD, r, ww.count('1')))
    frontier = next_frontier

M = 3**11
marked = bytearray(M)
new_by_depth = {}
new_witness = {}
for d in range(1, 18):
    newly = []
    for dd, w, A, q, D, r, s in safe:
        if dd != d or s > 11:
            continue
        for residue in range(r, M, A):
            if not marked[residue]:
                marked[residue] = 1
                newly.append(residue)
                new_witness[residue] = (w, A, q, D, r)
    new_by_depth[d] = newly
    if d == 11:
        assert sum(marked) == 82053
    if d == 14:
        assert sum(marked) == 82305
    if d == 17:
        assert sum(marked) == 82429
assert len(new_by_depth[14]) == 252
assert len(new_by_depth[17]) == 124
assert not any(new_by_depth[d] for d in (12, 13, 15, 16))
assert len({new_witness[r][4] for r in new_by_depth[14]}) == 28
assert len({new_witness[r][4] for r in new_by_depth[17]}) == 124
for d in (14, 17):
    for residue in new_by_depth[d]:
        w, A, q, D, r = new_witness[residue]
        # Verify the least positive ODD representative in its true modulus A,
        # not merely the projection to the smaller counting modulus.
        y = r if r % 2 else r+A
        assert (D*y-q) % A == 0
        z = (D*y-q)//A
        assert z >= 3 and z % 2 == 1 and z < y
        v = trace(z, len(w))
        assert v[-1] == y and min(v) == z
        assert ''.join(str(x % 2) for x in v[:-1]) == w
        assert all(Ai >= Di for Ai, qi, Di in prefix(w)[1:])
print('Strict inverse words through d=17:', len(safe))
print('Banned odd minimum locations, restricted s<=11, modulus 3^11:',
      {11:82053, 14:82305, 17:82429})
print('New full classes: depth 14: 28 mod 3^9; depth 17: 124 mod 3^11')

# Six-step alternative inverse of targets 10 mod 81.
assert prefix('111010')[-1] == (81, 73, 64)
for k in (0, 1, 2, 10):
    b = 91+162*k
    z = (64*b-73)//81
    v = trace(z, 6)
    assert (64*b-73) % 81 == 0 and z < b
    assert v[-1] == b and min(v) == z
assert trace(63, 9)[-1] == 91
assert trace(71, 6)[-1] == 91
print('New off-spine finite model: 63 --9--> 91 and 71 --6--> 91')

# Strong finite adversary: any finite schedule using two gap-nine
# words has all targets 1 mod 9 but neither 4 mod 9 nor 10 mod 81.
alphabet = ['111011010', '111101010']
assert {bridge[9][w][1] % 81 for w in alphabet} == {28, 37}
for words in product(alphabet, repeat=3):
    W = ''.join(words)
    A, q, D = prefix(W)[-1]
    modulus = 4*D
    r = ((3*D-q)*pow(A, -1, modulus)) % modulus
    # CRT: choose source divisible by 3, then increase by 3*modulus.
    k = (-r*pow(modulus, -1, 3)) % 3
    a = r+k*modulus
    if a < 3:
        a += 3*modulus
    ok = False
    for t in range(50):
        cur = a+3*modulus*t
        if cur < 3:
            continue
        x = cur
        segments = []
        for w in words:
            v = trace(x, len(w))
            if ''.join(str(y % 2) for y in v[:-1]) != w:
                break
            segments.append(v)
            x = v[-1]
        if len(segments) == len(words) and all(
            v[0] < v[-1] and min(v[1:-1]) > v[-1]
            and v[-1] % 81 in (28, 37) for v in segments):
            ok = True
            break
    assert ok and cur % 3 == 0
print('Positive finite mixed 1 mod9 schedules with 3-divisible starts:',
      len(alphabet)**3)
print('PASS: exact finite algebra only; E=empty remains OPEN')
