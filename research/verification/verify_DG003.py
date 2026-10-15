#!/usr/bin/env python3
"""DG003 exact finite checks. Only validates encoded prefix/certificate identities."""
from itertools import product


def step(n):
    return (n // 2) if n % 2 == 0 else (3 * n + 1) // 2


def affine(word):
    s = q = 0
    for j, bit in enumerate(word):
        if bit:
            q = 3 * q + (1 << j)
            s += 1
    return 3**s, 1 << len(word), q


def prefix(x, length):
    answer = []
    for _ in range(length):
        answer.append(x % 2)
        x = step(x)
    return tuple(answer)


def test_backward_certificates():
    certificates = [
        ('1', 5, 6),
        ('110', 13, 18),
        ('111010', 91, 162),
    ]
    inspected = 0
    for pattern, start, modulus in certificates:
        word = tuple(int(bit) for bit in pattern)
        a, d, q = affine(word)
        odds = 0
        for j, bit in enumerate(word, start=1):
            odds += bit
            assert 3**odds > 2**j
        assert a > d
        assert (d * start - q) % a == 0
        for k in range(400):
            n = start + k * modulus
            z, remainder = divmod(d*n - q, a)
            assert remainder == 0, (pattern, n)
            assert 2 <= z < n, (pattern, n, z)
            x = z
            for bit in word:
                assert x >= z and x % 2 == bit, (pattern, n, x)
                x = step(x)
                assert x >= z, (pattern, n, x)
            assert x == n, (pattern, n, x)
            inspected += 1
    residues = [n for n in range(1, 163, 2)
                if n % 6 == 5 or n % 18 == 13 or n % 162 == 91]
    assert len(residues) == 37
    assert not any(sum([n%6==5,n%18==13,n%162==91])>1 for n in residues)
    return inspected, len(residues)


def test_cross_depth_cylinder():
    checked = 0
    for J in range(0, 5):
        for u in product((0, 1), repeat=J):
            b, e, Q = affine(u)
            assert e == 2**J
            for m in range(1, 5):
                for w in product((0, 1), repeat=m):
                    a, d, q = affine(w)
                    for t in range(1, 4):
                        K = J + m*t
                        modulus = 2**K
                        coefficient = (d-a)*b
                        rhs = e*q - (d-a)*Q
                        assert coefficient & 1
                        root = (rhs*pow(coefficient, -1, modulus))%modulus
                        x = root if root else modulus
                        assert prefix(x, K) == u + w*t, (u, w, t, x)
                        assert ((d-a)*(b*x+Q)-e*q)%modulus == 0
                        assert prefix(x+modulus, K) == u+w*t
                        checked += 1
    return checked


def test_finite_survival_countermodels():
    for k in range(1, 25):
        n=(1<<k)-1
        x=n
        for _ in range(k):
            assert x>=n
            assert x%2==1
            x=step(x)
        assert x==3**k-1
    for t in range(1, 16):
        n=8**t-5
        x=n
        for j in range(3*t):
            assert x>=n and x%2==(1,1,0)[j%3]
            x=step(x)
        assert x==9**t-5
    return 24,15


if __name__=='__main__':
    n,classes=test_backward_certificates()
    print('Inverse ascending certificates checked:',n)
    print('Odd residues excluded for hypothetical least E modulo 162:',classes,'of 81')
    print('Cross-depth cylinder equivalences checked:',test_cross_depth_cylinder())
    print('Long finite survivor families checked:',test_finite_survival_countermodels())
    print('PASS: exact bounded checks only; no exception or full Collatz proof claimed.')
