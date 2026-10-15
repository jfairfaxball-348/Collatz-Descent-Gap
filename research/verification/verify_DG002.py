#!/usr/bin/env python3
"""Independent exact finite checks for DG002. No universal-Collatz verification."""
from itertools import product


def step(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def data(word):
    s, q = 0, 0
    for j, bit in enumerate(word):
        if bit:
            q = 3 * q + (1 << j)
            s += 1
    return 3**s, 1 << len(word), q


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def prefix(n, k):
    bits = []
    for _ in range(k):
        bits.append(n % 2)
        n = step(n)
    return tuple(bits)


def check_periodic_blocks():
    checked = 0
    for m in range(1, 7):
        for word in product((0, 1), repeat=m):
            a, d, q = data(word)
            assert (d-a) % 2 == 1
            for t in range(1, 5):
                mod = d**t
                # Q=(D-A)n-q divisible by D^t for t exact repetitions.
                r = (q * pow(d-a, -1, mod)) % mod
                n = r if r else mod
                for sample in (n, n + mod):
                    assert prefix(sample, m*t) == word*t, (word, t, sample)
                    assert ((d-a)*sample-q) % mod == 0
                    diff = (d-a)*sample-q
                    if diff:
                        assert t <= v2(diff)//m
                    if a > d:
                        assert (a-d)*sample+q >= mod
                checked += 1
            # A positive integral fixed point is an actual periodic orbit.
            if a < d and q % (d-a) == 0 and q > 0:
                c = q // (d-a)
                assert prefix(c, m) == word
                x = c
                for _ in range(m):
                    x = step(x)
                assert x == c
    return checked


def check_mixed_survivors():
    for t in range(1, 13):
        n = 8**t - 5
        x = n
        for j in range(3*t):
            assert x >= n, (t, j, x)
            assert x % 2 == (1, 1, 0)[j % 3]
            x = step(x)
        assert x == 9**t - 5
        assert x > n
        assert v2(n + 5) == 3*t
        assert n == (-5) % (8**t)
        assert prefix(n, 3*t+1)[-1] == 0  # next bit is not 1


def check_shifted_block_growth():
    checked = 0
    for n in range(1, 301):
        x = n
        for J in range(0, 41):
            assert (1 << J) * (x + 1) <= 3**J * (n + 1)
            y, t = x, 0
            while t < 12 and prefix(y, 3) == (1, 1, 0):
                for _ in range(3):
                    y = step(y)
                t += 1
                assert 8**t <= x + 5
                assert (1 << J)*8**t <= 3**J*(n+1) + 4*(1 << J)
                checked += 1
            x = step(x)
    return checked


def check_nonperiodic_2adic_path():
    word = []
    J = 0
    for _ in range(4):
        t = J+1
        word.extend((1,1,0) * t)
        word.append(1)
        J = len(word)
        # Every prefix has strictly expanding homogeneous multiplier.
        s = 0
        for k, bit in enumerate(word, 1):
            s += bit
            assert 3**s > 2**k
        # The unique residue for the full word gives a positive finite survivor.
        a, d, q = data(word)
        r = (-q*pow(a, -1, d)) % d
        representative = r if r else d
        x = representative
        for bit in word:
            assert x >= representative
            assert (x & 1) == bit
            x = step(x)
        assert x >= representative
    return len(word)


def check_odd_density():
    count = 0
    for n in range(2, 2001):
        x, odds = n, 0
        for j in range(1, 33):
            odds += x & 1
            x = step(x)
            if x >= n:
                assert (2**j)*n**odds <= (3*n+1)**odds, (n,j,odds)
                assert 2*odds > j, (n,j,odds)
                count += 1
            else:
                break
    return count


if __name__ == '__main__':
    print('Block congruence word-depth cases:', check_periodic_blocks())
    check_mixed_survivors()
    print('Mixed (110)^t survivors through t=12: PASS')
    print('Shifted (110)-block inequalities checked:', check_shifted_block_growth())
    print('Explicit nonperiodic 2-adic word validated for bits:', check_nonperiodic_2adic_path())
    print('Surviving orbit-prefix odd density checks:', check_odd_density())
    print('Finite exact checks passed; no assertion about E=empty.')
