#!/usr/bin/env python3
"""Independent replay of the complete 60-unit-suffix endpoint escape range."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
record = json.loads((root / "terminal_ones_escape.json").read_text())
low = 2**71
upper = 2**76 + 2**36
step = 2**60
k_start = (low + step) // step
k_end = upper // step
assert (k_start, k_end) == (2049, 65536)
assert record["k_lo"] == k_start and record["k_hi"] == k_end
assert record["count"] == k_end - k_start + 1

checksum = hashlib.sha256()
maximum = (0, None)
for k in range(k_start, k_end + 1):
    state = step * k - 1
    assert low <= state < upper and state % 2 == 1
    count = 0
    while state >= low:
        state = 3 * state + 1
        while state % 2 == 0:
            state //= 2
        count += 1
        assert count <= 10000, ("unresolved", k)
    checksum.update(f"{k}:{count}\n".encode())
    if count > maximum[0]:
        maximum = (count, k)

assert record["unresolved_k"] == []
assert record["depths_sha256"] == checksum.hexdigest()
assert (record["max_escape_depth"], record["first_max_k"]) == maximum
print("RL343_TERMINAL_ONES_60_RED_TEAM_GREEN", maximum, checksum.hexdigest())
