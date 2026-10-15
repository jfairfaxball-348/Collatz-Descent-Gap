#!/usr/bin/env python3
"""FINAL_CHANCE Session 5 verifier: two-sided transfer bridge countermodel.

Constructs an exact same-m countermodel to the hoped-for theorem that the
RL154-style exact 75-step prefix and suffix ownership transfers, together with
the physical m-window and the full nonnegative defect grammar, already force a
contradiction.

The construction is NOT a cycle and does NOT satisfy the unknown global
middle physical connection.  That missing connection is precisely the point.
"""

A = 217_976_794_617
L = 137_528_045_312
N = 75

def b(j):
    return (A * j) // L

def c(j):
    return b(j + 1) - b(j)

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

m = 2**75 - 1
assert 2**71 <= m < 2**75
assert m % 2 == 1
assert m % 3 != 0

# ---------- exact physical prefix from m ----------
y = m
S = 0
prefix_a = []
prefix_h = [0]
prefix_states = [m]
for j in range(N):
    z = 3 * y + 1
    a = v2(z)
    y = z >> a
    S += a
    h = b(j + 1) - S
    assert a >= 1
    assert h >= 0
    assert y > m
    prefix_a.append(a)
    prefix_h.append(h)
    prefix_states.append(y)

assert prefix_a == [1] * 74 + [2]
assert S == 76
assert b(75) == 118
assert prefix_h[-1] == 42
assert sum(prefix_h) == 1629
prefix_terminal = y

# ---------- exact physical suffix returning to the SAME m ----------
#
# Work backwards from y_L=m.  For each step choose the smallest exponent a
# of the required parity which:
#   1. makes (2^a y_(j+1)-1)/3 an integer,
#   2. keeps the induced defect h_j nonnegative, and
#   3. keeps the predecessor nonzero mod 3 so another backward step exists.
#
# This is a deterministic exact construction, not a search over the global
# phase space.
cut = L - N
y_next = m
h_next = 0
tail_h = {L: 0}
tail_a = {}
tail_pred = {}
for j in range(L - 1, cut - 1, -1):
    cj = c(j)
    assert y_next % 3 in (1, 2)
    parity = 0 if y_next % 3 == 1 else 1
    a = max(1, cj - h_next)
    if a % 2 != parity:
        a += 1
    while True:
        num = (2**a) * y_next - 1
        assert num % 3 == 0
        pred = num // 3
        if pred % 3 != 0:
            break
        a += 2

    h = a - cj + h_next
    assert h >= 0
    assert pred > m
    assert pred % 2 == 1
    assert pred % 3 != 0

    tail_a[j] = a
    tail_h[j] = h
    tail_pred[j] = pred
    y_next = pred
    h_next = h

assert h_next == 53
suffix_start = y_next
assert suffix_start > m

# Replay the suffix forward and verify that all a_j are exact valuations and
# that the endpoint is exactly the same m.
y = suffix_start
for j in range(cut, L):
    z = 3 * y + 1
    a = v2(z)
    assert a == tail_a[j]
    y = z >> a
    if j < L - 1:
        assert y > m
assert y == m

# ---------- glue a COMPLETE legal defect path between the two physical ends ----------
#
# Prefix ends at h_75=42.  Drop to zero immediately (downward jumps are
# unrestricted by positivity), remain at zero, then use a 90-step tight ramp
# ending exactly at the suffix boundary height 53.
assert c(75) + prefix_h[-1] >= 1  # exponent on the 42 -> 0 drop
j0 = cut - 90
assert j0 > 76

ramp_h = 0
for j in range(j0, cut):
    next_h = ramp_h + c(j) - 1
    assert next_h >= ramp_h
    assert next_h - ramp_h in (0, 1)
    # Tight ramp exponent a_j = c_j + h_j - h_(j+1) = 1.
    assert c(j) + ramp_h - next_h == 1
    ramp_h = next_h

assert ramp_h == 53
assert ramp_h == tail_h[cut]

# Long middle zero segment uses a_j=c_j in {1,2}; no enumeration is needed.
assert c(76) in (1, 2)
assert c(j0 - 1) in (1, 2)

# All suffix transitions satisfy the defect/exponent identity.
for j in range(cut, L):
    assert tail_a[j] == c(j) + tail_h[j] - tail_h[j + 1]
    assert tail_a[j] >= 1

# Prefix transitions satisfy the same identity.
for j in range(N):
    assert prefix_a[j] == c(j) + prefix_h[j] - prefix_h[j + 1]

# Since h_0=h_L=0, summing a_j=c_j+h_j-h_(j+1) over the complete glued
# path gives total exponent A exactly, without materializing L entries.
assert b(L) == A

print("FINAL_CHANCE Session 5 two-sided transfer countermodel verifier: PASS")
print("A,L =", (A, L))
print("m =", m)
print("m window =", (2**71, 2**75))
print("prefix exact exponents =", "1^74,2")
print("prefix total exponent S_75 =", S)
print("prefix terminal defect h_75 =", prefix_h[-1])
print("prefix defect area through 75 =", sum(prefix_h))
print("prefix terminal state =", prefix_terminal)
print("suffix cut =", cut)
print("suffix boundary defect h_(L-75) =", tail_h[cut])
print("suffix start state =", suffix_start)
print("suffix maximum exponent =", max(tail_a.values()))
print("suffix maximum defect =", max(tail_h.values()))
print("middle tight-ramp length =", 90)
print("middle tight-ramp terminal height =", ramp_h)
print("same m selected by exact physical prefix and suffix = True")
print("complete nonnegative positive-exponent defect grammar = True")
print("global middle physical connection = NOT ASSERTED")
print("scope=countermodel to two-sided-transfer bridge; not a cycle")
