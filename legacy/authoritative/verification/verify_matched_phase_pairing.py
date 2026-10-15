#!/usr/bin/env python3
"""Index-orientation red team for the analytic two-row q/phase pairing."""
from itertools import combinations


def check(a, ell, u, v, root_rank):
    assert all(ui >= vi for ui, vi in zip(u, v))
    root_position = u[root_rank]

    def profile(rank, position):
        t = (root_rank - rank) % (2 * ell)
        gap = (root_position - position) % (2 * a)
        baseline = (a * t + ell - 1) // ell
        return t, gap, gap - baseline

    for i in range(ell):
        tu, gu, qu = profile(i, u[i])
        tv, gv, qv = profile(ell + i, a + v[i])
        d = u[i] - v[i]
        assert (tv - tu) % (2 * ell) == ell
        assert qv - qu == d, (a, ell, u, v, root_rank, i, qu, qv, d)


cases = 0
for a, ell in ((8, 4), (9, 4), (10, 4), (12, 5)):
    words = list(combinations(range(a), ell))
    for v in words:
        for u in words:
            if not all(ui >= vi for ui, vi in zip(u, v)):
                continue
            for k in range(ell):
                check(a, ell, u, v, k)
                cases += 1

N_MIN = 20390252058
assert 3 * N_MIN - 4 == 61170756170
assert 3 * N_MIN - 4 < 137528045312
print("RL343_MATCHED_PHASE_PAIRING_INDEX_GREEN", cases)
print("minimum_strict_rank_q0_exclusions", 3 * N_MIN - 4)
