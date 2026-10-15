from math import gcd

WORD = '1101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011010'
W = [int(c) for c in WORD]
A = len(W)
L = sum(W)
D = (1 << A) - 3**L

assert A == 184
assert L == 116
assert D > 1 and gcd(D, 6) == 1

# Primitive word check.
for p in range(1, A):
    if A % p == 0:
        assert W != W[:p] * (A // p)

# RL-L54 bit-level consequences:
# every proper suffix ending at the least-state rotation is subcritical,
# while the externally forced first 183 proper prefixes are supercritical.
P = [0]
s = 0
for b in W:
    s += b
    P.append(s)

for m in range(1, 184):
    assert 3**P[m] > 2**m

for m in range(1, A):
    E = L - P[A-m]
    assert 2**m > 3**E

# Root endpoint grammar in the hard s=2 branch: 1^s 0^t 1... with t=1.
assert W[:4] == [1, 1, 0, 1]
s_root = 2
t_exit = 1

# Final-return local block with n_close=t_close=1: ...10 | root.
assert W[-2:] == [1, 0]
n_close = 1
t_close = 1

# Freeze an explicit R# satisfying the endpoint valuation congruences and the
# inherited external floor. This is NOT claimed to realize the whole word.
R_floor = 1 << 71
R = R_floor + ((91 - R_floor) % 144)  # R == 91 mod 144
assert R >= R_floor
assert R % 16 == 11                   # v2(R+1)=2 and q == 3 mod 4
assert R % 9 == 1                     # exact v3(2R+1)=1 for t_close=1

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

assert vp(R + 1, 2) == s_root
q_root = (R + 1) >> s_root
assert vp(3**s_root * q_root - 1, 2) == t_exit
assert vp((1 << t_close) * R + 1, 3) == n_close
q_close = ((1 << t_close) * R + 1) // (3**n_close)
u_close = (1 << n_close) * q_close - 1
assert u_close > R
assert 2**(n_close + t_close) > 3**n_close

# Exact cyclic adjacent-swap (01<->10) distance via minimum l1 circulation.
def rot(w, m):
    return w[m:] + w[:m]

def cyclic_adjacent_swap_distance(a, b):
    assert len(a) == len(b) and sum(a) == sum(b)
    cumulative = []
    z = 0
    for x, y in zip(a, b):
        z += x - y
        cumulative.append(z)
    assert cumulative[-1] == 0
    vals = sorted(-z for z in cumulative)
    med = vals[len(vals)//2]
    return sum(abs(med + z) for z in cumulative)

# Canonical distinguished phase starts under the local interpretation:
# root, first post-neutral odd phase after 110, final odd anchor before 10.
distinguished = [0, 3, 182]
pair_distances = {}
for i, a in enumerate(distinguished):
    for b in distinguished[i+1:]:
        dd = cyclic_adjacent_swap_distance(rot(W, a), rot(W, b))
        pair_distances[(a, b)] = dd
        assert dd >= 4

# A conservative endpoint-neighbourhood audit is also far from radius 3.
neighbourhood = [0, 1, 2, 3, 181, 182, 183]
min_neighbourhood = min(
    cyclic_adjacent_swap_distance(rot(W, a), rot(W, b))
    for i, a in enumerate(neighbourhood)
    for b in neighbourhood[i+1:]
)
assert min_neighbourhood >= 4

# Stronger audit: among *all* cyclic rotations the minimum distance is exactly 4.
# Thus this local-grammar countermodel sits immediately outside the closed
# radius-3 obstruction, not merely outside it at the distinguished endpoints.
all_rotation_distances = []
for a in range(A):
    wa = rot(W, a)
    for b in range(a + 1, A):
        dd = cyclic_adjacent_swap_distance(wa, rot(W, b))
        all_rotation_distances.append((dd, a, b))
min_all, min_a, min_b = min(all_rotation_distances)
assert min_all == 4

# Standard Collatz word polynomial. The countermodel is deliberately NOT an RL object.
def Qword(w):
    pos = [i+1 for i,b in enumerate(w) if b]
    LL = len(pos)
    return sum((1 << (p-1)) * 3**(LL-k-1) for k,p in enumerate(pos))

Q = Qword(W)
assert Q % D != 0

print('RL20 bounded-bridge countermodel verifier: PASS')
print('A,L,D =', A, L, D)
print('primitive = True')
print('explicit endpoint-compatible R# =', R)
print('distinguished pair distances =', pair_distances)
print('endpoint-neighbourhood minimum distance =', min_neighbourhood)
print('all-rotation minimum distance =', min_all, 'at shifts', (min_a, min_b))
print('Q mod D =', Q % D)
print('D divides Q =', Q % D == 0)
