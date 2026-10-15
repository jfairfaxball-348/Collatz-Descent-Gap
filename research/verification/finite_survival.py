#!/usr/bin/env python3
"""Exact finite-horizon checks, NOT a Collatz proof or novelty certificate."""

def step(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2

def affine_prefixes(n, k):
    x, s, q = n, 0, 0
    bits, pairs = [], []
    for j in range(k):
        e = x & 1
        bits.append(e)
        if e:
            s, q = s + 1, 3*q + (1 << j)
        x = step(x)
        assert (1 << (j+1))*x == 3**s*n + q
        pairs.append((s, q))
    return tuple(bits), pairs

def check(K=8):
    for k in range(1, K+1):
        # Each parity word occurs exactly once amongst the 2^k residues.
        signatures = {}
        for representative in range(1, 2**k+1):
            word, prefixes = affine_prefixes(representative, k)
            assert word not in signatures
            upper = None
            for j, (s, q) in enumerate(prefixes, 1):
                deficit = 2**j - 3**s
                if deficit > 0:
                    bound = q // deficit
                    upper = bound if upper is None else min(upper, bound)
            signatures[word] = (representative % (2**k), upper)
        assert len(signatures) == 2**k

        # Compare the derived cylinder criterion with raw iteration.
        for n in range(2, 4*(2**k)+1):
            word, _ = affine_prefixes(n, k)
            residue, upper = signatures[word]
            predicted = n % (2**k) == residue and (upper is None or n <= upper)
            x = n
            actual = True
            for j in range(k):
                x = step(x)
                actual = actual and x >= n
            assert predicted == actual, (k, n, word, upper)

        # An unbounded family survives each prescribed finite horizon.
        for t in range(1, 6):
            n = (1 << k)*t - 1
            x = n
            for j in range(1, k+1):
                x = step(x)
                assert x == (3**j)*(1 << (k-j))*t - 1
                assert x > n

    print("Passed: exact finite-horizon parity, residue, truncation and long-prefix checks through K=%d." % K)
    print("This does not establish an infinite-horizon result.")

if __name__ == "__main__":
    check()
