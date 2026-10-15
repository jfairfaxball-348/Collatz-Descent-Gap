#!/usr/bin/env python3
"""Exact fixed-depth suffix boundary and symbolic grammar count for RL343."""

A, ELL = 217976794617, 137528045312
D = A - ELL
LOW, UP = 1 << 71, (1 << 76) + (1 << 36)
DEPTH, EXCLUDED_UNIT_TAIL = 75, 60


def factors(length):
    cuts = sorted({0, ELL, *((-D * j) % ELL for j in range(length + 1))})
    result = set()
    for left, right in zip(cuts, cuts[1:]):
        for phase in {left, min(left + 1, right - 1)}:
            previous = (phase + ELL - 1) // ELL
            word = []
            for j in range(1, length + 1):
                current = (phase + D * j + ELL - 1) // ELL
                word.append(1 + current - previous)
                previous = current
            result.add(tuple(word))
    assert len(result) == length + 1
    return sorted(result)


def count_backward(h, require_terminal_ones=0):
    """Count q_0..q_(s-1)>0, q_s=0, q_(s-1)=1, g_j>=1."""
    if h[-1] != 2:
        return 0
    dp = {1: 1}
    s = len(h)
    for i in range(s - 1, 0, -1):
        next_dp = {}
        for q_i, multiplicity in dp.items():
            if require_terminal_ones and i >= s - require_terminal_ones + 1:
                choices = (q_i + h[i - 1] - 1,)
            else:
                choices = range(1, q_i + h[i - 1])
            for q_prev in choices:
                next_dp[q_prev] = next_dp.get(q_prev, 0) + multiplicity
        dp = next_dp
    return sum(dp.values())


def count_forward(h):
    """Independent direction: sum over every possible positive q_0."""
    n = len(h)
    if h[-1] != 2:
        return 0
    dp = [0] + [1] * n
    for i in range(1, n):
        prefix = [0] * len(dp)
        for q in range(1, len(dp)):
            prefix[q] = prefix[q - 1] + dp[q]
        next_dp = [0] * (n - i + 1)
        for q_i in range(1, n - i + 1):
            next_dp[q_i] = prefix[min(len(dp) - 1, q_i + h[i - 1] - 1)]
        dp = next_dp
    return dp[1]


def carry(gaps):
    value = 0
    for j, gap in enumerate(gaps):
        value = (1 << gap) * value + 3**j
    return value


def endpoint_residue(gaps):
    length, total_gap = len(gaps), sum(gaps)
    modulus = 1 << total_gap
    return (-carry(gaps) * pow(3**length, -1, modulus)) % modulus, modulus


assert UP - LOW < 1 << 76
mechanical = factors(DEPTH)
all_count = sum(count_backward(h) for h in mechanical)
assert all_count == sum(count_forward(h) for h in mechanical)
terminal_ones_count = sum(
    count_backward(h, EXCLUDED_UNIT_TAIL) for h in mechanical
)
surviving_count = all_count - terminal_ones_count
assert (all_count, terminal_ones_count, surviving_count) == (
    456795521589204615537376070040576,
    1251242493049578,
    456795521589204614286133576990998,
)
# A surviving 75-gap word has an extra gap beyond all ones, so H>=76.
assert DEPTH + 1 == 76
# Check the residue formula on an inherited exact two-gap return.
example = (3, 1)
e = 42510466134663422588435
residue, modulus = endpoint_residue(example)
assert e % modulus == residue
print("RL343_SUFFIX75_BOUNDARY_GREEN")
print("mechanical_factors", len(mechanical))
print("locally_admissible_profiles", all_count)
print("excluded_terminal60_profiles", terminal_ones_count)
print("remaining_symbolic_profiles", surviving_count)
print("endpoint_multiplicity_per_remaining_suffix", "at most one")
