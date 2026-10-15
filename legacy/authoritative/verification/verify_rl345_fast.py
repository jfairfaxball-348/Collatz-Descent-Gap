#!/usr/bin/env python3
"""RL345 fast verifier: 23-source / 72-endpoint Phase-4 contraction."""
from hashlib import sha256
from itertools import combinations_with_replacement

LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
DEPTH = 72

assert 2 * 3**22 < 1 << 37 < 2 * 3**23

def carry(gaps):
    c = 0
    for j, g in enumerate(gaps):
        c = (1 << g) * c + 3**j
    return c

def endpoint_residue(gaps):
    H = sum(gaps)
    modulus = 1 << H
    return (-carry(gaps) * pow(3**len(gaps), -1, modulus)) % modulus, modulus

def odd_step(x):
    y = 3*x + 1
    return y // (y & -y)

def escape_depth(x):
    d = 0
    while x >= LOW:
        x = odd_step(x)
        d += 1
        assert d <= 446
    return d

word_counts = {}
endpoint_counts = {}
digest = sha256()
max_depth = -1
max_records = []

for excess in (1, 2, 3):
    words = endpoints = 0
    for positions in combinations_with_replacement(range(DEPTH), excess):
        if max(positions) < DEPTH - 60:
            continue
        gaps = [1] * DEPTH
        for p in positions:
            gaps[p] += 1
        words += 1
        residue, modulus = endpoint_residue(gaps)
        E = residue + max(0, (LOW - residue + modulus - 1) // modulus) * modulus
        while E < UP:
            depth = escape_depth(E)
            endpoints += 1
            digest.update(f"{excess}:{','.join(str(p+1) for p in positions)}:{E}:{depth}\n".encode())
            if depth > max_depth:
                max_depth = depth
                max_records = [(positions, E)]
            elif depth == max_depth:
                max_records.append((positions, E))
            E += modulus
    word_counts[excess] = words
    endpoint_counts[excess] = endpoints

assert word_counts == {1: 60, 2: 2550, 3: 64460}
assert endpoint_counts == {1: 460, 2: 9888, 3: 125008}
assert sum(word_counts.values()) == 67070
assert sum(endpoint_counts.values()) == 135356
assert max_depth == 446
assert max_records == [((3, 10, 37), 32854878509085218570239)]
assert digest.hexdigest() == "2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d"

print("RL345_FAST_GREEN")
print("source_prefix_depth", 23)
print("suffix_depth", 72)
print("exceptional_words", sum(word_counts.values()))
print("exceptional_endpoints", sum(endpoint_counts.values()))
print("max_escape", max_depth)
print("digest", digest.hexdigest())
