#!/usr/bin/env python3
"""DG011 exact arithmetic regressions. NOT a Collatz proof or an E-orbit certificate."""
from itertools import product

def T(n):
    assert n > 0
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def aff(w):
    A, q, D = 1, 0, 1
    pref = [(A, q, D)]
    for bit in w:
        if bit == '1':
            A, q = 3 * A, 3 * q + D
        else:
            assert bit == '0'
        D *= 2
        pref.append((A, q, D))
    return A, q, D, pref

def orbit_word(z, w):
    tr = [z]
    for bit in w:
        assert tr[-1] % 2 == int(bit)
        tr.append(T(tr[-1]))
    return tr

# All expanding words with s<=6 have d<=9; exhaust all of them,
# with no strict-prefix-safe assumption.
expanding = 0
for d in range(1, 10):
    for bits in product('01', repeat=d):
        w = ''.join(bits)
        s = w.count('1')
        if s > 6 or not s or 3**s <= 2**d:
            continue
        expanding += 1
        A, q, D, _ = aff(w)
        assert A == 3**s and D == 2**d
        if s == 1:
            assert q * pow(D, -1, 3) % 3 == 2
        else:
            assert q * pow(D, -1, 9) % 9 != 7, w
print('PASS: mod-9 shield; all', expanding, 'expanding words with <=6 odd steps')

# Sharp s=7 example; 205 not asserted exceptional.
w = '11111101000'
A, q, D, pref = aff(w)
assert (A, q, D) == (2187, 2123, 2048)
tr = orbit_word(191, w)
assert tr[-1] == 205 and min(tr) == 191
assert all(Ai >= Di for Ai, _, Di in pref)
print('PASS: sharp s=7 witness 191 -> 205 in 11 steps')

def mountain(r):
    assert r >= 5 and r % 6 == 5
    s = 1
    while 3**s <= 2**(s+r):
        s += 1
    w = '1'*s + '0'*r
    A, q, D, pref = aff(w)
    assert (A, q, D) == (3**s, 3**s-2**s, 2**(s+r))
    assert 1 < A/D < 1.5
    assert all(Ai * D > A * Di for Ai, _, Di in pref[1:-1])
    return s, w

# Primitive-root interpolation modulo 3^k: every 7-mod-9 target
# is the endpoint residue of some mountain word.
for k in range(2, 6):
    modulus = 3**k
    targets = set()
    for j in range(3**(k-2)):
        r = 5 + 6*j
        s, w = mountain(r)
        assert s >= k
        target = (-pow(2, -r, modulus)) % modulus
        assert target % 9 == 7
        targets.add(target)
    assert targets == set(range(7, modulus, 9))
    print('PASS: complete mountain target interpolation mod 3^', k, sep='')

# Finite, not infinite, noninitial mountain bridge compatibility.
def mixed_seed(words):
    W = ''.join(words)
    A, q, D, _ = aff(W)
    M = 4*D
    residue = ((3*D - q)*pow(A, -1, M)) % M
    n = residue + M*((-residue*pow(M, -1, 3)) % 3)
    if n <= 1:
        n += 3*M
    for _ in range(30):
        x, records = n, []
        ok = True
        for w in words:
            path = orbit_word(x, w)
            y = path[-1]
            if not (x < y < min(path[1:-1]) and y % 9 == 7):
                ok = False
                break
            records.append(y)
            x = y
        if ok:
            assert n % 3 == 0
            assert all(y % 3 != 0 for y in records)
            return n, records
        n += 3*M
    raise AssertionError('failed finite CRT progression')

for rr in ((5, 11, 5), (11, 5, 11)):
    ws = [mountain(r)[1] for r in rr]
    n, records = mixed_seed(ws)
    assert len(records) == len(rr)
    print('PASS: mixed finite noninitial schedule', rr, 'initial digits', len(str(n)))

# A single positive starting n cannot realise the following infinite
# mountain schedule: at global start time t_j choose r_j>=t_j, r_j=5(mod6).
# The initial all-odd run forces 2^s <= (3/2)^t*(n+1).
t = 0
for j in range(4):
    r = max(5, t)
    r += (5-r) % 6
    s, w = mountain(r)
    assert s > r >= t
    print('PASS: hostile infinite-schedule prefix', j, 't', t, 'r', r, 's', s)
    t += len(w)
print('DG011 PASS: finite and algebraic checks only; E=empty remains OPEN')
