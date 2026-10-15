#!/usr/bin/env python3
"""Exact finite escape scan for q=0 endpoints with a 60-unit inverse suffix."""
import hashlib

LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
K_LO = 2049
K_HI = 65536
STEP_CAP = 10000

assert (K_LO << 60) - 1 >= LOW
assert ((K_LO - 1) << 60) - 1 < LOW
assert (K_HI << 60) - 1 < UP
assert ((K_HI + 1) << 60) - 1 >= UP

digest = hashlib.sha256()
max_depth = -1
max_k = None
unresolved = []
for k in range(K_LO, K_HI + 1):
    x = (k << 60) - 1
    depth = 0
    while x >= LOW and depth < STEP_CAP:
        y = 3 * x + 1
        x = y // (y & -y)
        depth += 1
    if x >= LOW:
        unresolved.append(k)
    else:
        digest.update(f"{k}:{depth}\n".encode("ascii"))
        if depth > max_depth:
            max_depth, max_k = depth, k

assert not unresolved, unresolved
assert (max_depth, max_k) == (403, 58658)
assert digest.hexdigest() == "6b865b436278792435dc59fcf4f15975f9e4961f403af18a4cbd2ff12be616ad"
print("RL343_TERMINAL_ONES_60_GREEN")
