#!/usr/bin/env python3
"""DG004: exact bounded sanity checks, NOT verification that E is empty."""
from collections import Counter

MAX_LENGTH = 9
count_by_length = Counter()
new = []

def walk(word='', odds=0, q=0):
    length = len(word)
    if length:
        count_by_length[length] += 1
        A, D = 3 ** odds, 1 << length
        residue = (q * pow(D, -1, A)) % A
        old = (residue % 3 == 2 or
               (odds >= 2 and residue % 9 == 4) or
               (odds >= 4 and residue % 81 == 10))
        if not old:
            new.append((word, odds, residue, q))
    if length == MAX_LENGTH:
        return
    for bit in (0, 1):
        new_odds = odds + bit
        if 3 ** new_odds > 2 ** (length + 1):
            walk(word + str(bit), new_odds,
                 3 * q + (1 << length) if bit else q)

walk()
assert [count_by_length[i] for i in range(1, 10)] == [1, 1, 2, 3, 4, 8, 13, 19, 38]
assert sorted(new) == sorted([
    ('111011010', 6, 604, 881),
    ('111101010', 6, 433, 809),
])

certs = [
    ('111011010', 881, 1333, 935),
    ('111101010', 809, 433, 303),
]
checked = 0
for word, q, y0, z0 in certs:
    for h in (0, 1, 2, 3, 10, 2000):
        y, z = y0 + 1458 * h, z0 + 1024 * h
        assert y % 2 == 1 and 2 <= z < y
        assert (729 * z + q) == 512 * y
        x = z
        for bit in word:
            assert x % 2 == int(bit)
            x = (3 * x + 1) // 2 if bit == '1' else x // 2
            assert x > z
            checked += 1
        assert x == y

def T(n):
    return n // 2 if n % 2 == 0 else (3*n+1) // 2

record_checks = 0
for n in range(2, 1502):
    for cutoff in (5, 12, 25, 40):
        x = n
        trace = []
        for _ in range(cutoff):
            trace.append(x)
            x = T(x)
        records = []
        minimum = float('inf')
        for i in range(len(trace) - 1, -1, -1):
            if trace[i] < minimum:
                minimum = trace[i]
                records.append((i, trace[i]))
        records.reverse()
        for (_, a), (_, b) in zip(records, records[1:]):
            assert a < b and b <= T(a)
            record_checks += 1

abstract = [4 * ((10 * 5**j) // 4**j) + 3 for j in range(50)]
assert all(abstract[j] < abstract[j+1]
           and 2*(abstract[j+1]+1) <= 3*(abstract[j]+1)
           for j in range(49))
print('Strictly expanding words by length 1..9:',
      [count_by_length[i] for i in range(1, 10)])
print('New shortest residue certificates:', sorted(new))
print('Certificate iterate comparisons checked:', checked)
print('Finite-trace suffix-record comparisons checked:', record_checks)
print('Sparse countermodel sample length:', len(abstract))
print('PASS: bounded exact checks only; Collatz descent gap remains open')
