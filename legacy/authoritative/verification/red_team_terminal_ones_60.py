#!/usr/bin/env python3
"""Independent full-range replay for terminal 60-unit inverse suffix."""
import hashlib
low = 2**71
upper = 2**76 + 2**36
step = 2**60
k_start = (low + step) // step
k_end = upper // step
assert (k_start, k_end) == (2049, 65536)

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

assert checksum.hexdigest() == "6b865b436278792435dc59fcf4f15975f9e4961f403af18a4cbd2ff12be616ad"
assert maximum == (403, 58658)
print("RL343_TERMINAL_ONES_60_RED_TEAM_GREEN", maximum, checksum.hexdigest())
