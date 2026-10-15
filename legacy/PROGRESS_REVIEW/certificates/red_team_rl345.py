#!/usr/bin/env python3
"""Independent RL345 red team for the 72-gap exceptional endpoint certificate."""
from hashlib import sha256

LOW = 1 << 71
UP = (1 << 76) + (1 << 36)
N = 72

assert 2 * 3**22 < 2**37 < 2 * 3**23

def sparse_words(e):
    if e == 1:
        for i in range(N): yield (i,)
    elif e == 2:
        for i in range(N):
            for j in range(i, N): yield (i,j)
    elif e == 3:
        for i in range(N):
            for j in range(i, N):
                for k in range(j, N): yield (i,j,k)

def direct_carry(gaps):
    suffix = 0
    c = 0
    for j in range(len(gaps)-1, -1, -1):
        c += 3**j * (1 << suffix)
        suffix += gaps[j]
    return c

def step(x):
    y = 3*x + 1
    while y % 2 == 0:
        y //= 2
    return y

def depth_to_floor(x):
    d = 0
    while x >= LOW:
        x = step(x)
        d += 1
        assert d <= 446
    return d

wc = {}; ec = {}; h = sha256(); mx = (-1,None,None); mx_count = 0
for e in (1,2,3):
    words = endpoints = 0
    for ps in sparse_words(e):
        if not any(p >= 12 for p in ps):
            continue
        gaps = [1]*N
        for p in ps: gaps[p] += 1
        words += 1
        H = N + e
        mod = 1 << H
        C = direct_carry(gaps)
        r = (-C * pow(3**N, -1, mod)) % mod
        q0 = (LOW - r + mod - 1)//mod
        q1 = (UP - 1 - r)//mod
        for q in range(q0, q1+1):
            E = r + q*mod
            assert LOW <= E < UP
            assert ((3**N)*E + C) % mod == 0
            d = depth_to_floor(E)
            endpoints += 1
            h.update(f"{e}:{','.join(str(p+1) for p in ps)}:{E}:{d}\n".encode())
            if d > mx[0]:
                mx = (d,ps,E); mx_count = 1
            elif d == mx[0]: mx_count += 1
    wc[e]=words; ec[e]=endpoints

assert wc == {1:60,2:2550,3:64460}
assert ec == {1:460,2:9888,3:125008}
assert mx == (446,(3,10,37),32854878509085218570239)
assert mx_count == 1
assert h.hexdigest() == "2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d"

print("RL345_RED_TEAM_GREEN")
print("word_counts", wc)
print("endpoint_counts", ec)
print("unique_max", mx)
print("digest", h.hexdigest())
