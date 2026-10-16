#!/usr/bin/env python3
"""DG013 finite exact verifier. Universal claims need the accompanying paper proof.

Checks paired superword affine divisibility, integer finite witnesses,
and the logarithmic plateau parameters. Does NOT prove Collatz.
"""
def T(x):
    assert x > 0
    return x // 2 if x % 2 == 0 else (3*x + 1) // 2

def affine(word):
    A, q, D = 1, 0, 1
    for b in word:
        if b == "1":
            A, q = 3*A, 3*q + D
        else:
            assert b == "0"
        D *= 2
    return A, q, D

def mountain(r):
    assert r >= 5 and r % 6 == 5
    s = 1
    while 3**s <= 2**(s+r):
        s += 1
    w = "1"*s + "0"*r
    A, q, D = affine(w)
    assert (A, q, D) == (3**s, 3**s-2**s, 2**(s+r))
    assert D < A and 2*A < 3*D
    return s, w

def pair(r, base=5):
    _, w0 = mountain(base)
    s, w1 = mountain(r)
    w = w0 + w1
    A, q, D = affine(w)
    assert D == 2**len(w)
    assert 0 < A-D+q < 5*D
    return w, A, q, D

def seed_for_finite(rs):
    words = [mountain(r)[1] for r in rs]
    A, q, D = affine("".join(words))
    mod = 4*D
    # Final endpoint is 3 mod 4; this selects one full parity cylinder.
    n = ((3*D-q)*pow(A, -1, mod)) % mod
    # Independently require a 3-divisible first source.
    n += mod*((-n*pow(mod, -1, 3)) % 3)
    delta = 3*mod
    for _ in range(100):
        if n > 1:
            x = n
            good = True
            for w in words:
                vals = [x]
                for b in w:
                    if vals[-1] % 2 != int(b):
                        good = False
                        break
                    vals.append(T(vals[-1]))
                if not good or not(x < vals[-1] < min(vals[1:-1])):
                    good = False
                    break
                if vals[-1] % 9 != 7:
                    good = False
                    break
                x = vals[-1]
            if good:
                assert n % 3 == 0
                return n
        n += delta
    raise AssertionError("no finite witness found")

for r in (5, 11, 17, 23, 29, 35, 41):
    s, _ = mountain(r)
    w, A, q, D = pair(r)
    assert len(w) == 14+s+r
    assert (A-D+q) < 5*D
    print("PASS pair", r, "s", s, "d", len(w))

for r, K in ((5, 2), (11, 2), (11, 3), (17, 2)):
    w, A, q, D = pair(r)
    n = seed_for_finite([5, r]*K)
    C = A-D
    assert (C*n+q) % (D**K) == 0
    assert D**(K-1) < 5*(n+1)
    x = n
    for _ in range(K):
        assert (A*x+q) % D == 0
        x = (A*x+q)//D
    assert x > n
    print("PASS finite repeated superword", r, K, "digits", len(str(n)))

for rs in (
    (5, 11, 5, 11, 5, 17),
    (5, 11, 5, 11, 5, 17, 5, 17),
    (5, 5, 5, 11, 5, 11),
    (5, 11, 5, 11, 5, 11, 5, 11)
):
    n = seed_for_finite(rs)
    print("PASS strict finite CRT shadow", rs, "digits", len(str(n)))

# R_j = 5+6 floor(log2(j+2)); for k>=1 its kth high plateau is
# j = 2^k - 2, ..., 2^(k+1) - 3, of K=2^k paired superwords.
margins = []
for k in range(1, 10):
    J, K, rho = 2**k-2, 2**k, 5+6*k
    for j in range(J, J+K):
        assert 5+6*((j+2).bit_length()-1) == rho
    margin = (K-1)*rho - 2*J
    assert margin > 0
    margins.append(margin)
    print("PASS logarithmic plateau", k, "rho", rho, "start", J,
          "copies", K, "required log2(5(n+1)) >", margin)
assert all(b>a for a, b in zip(margins, margins[1:]))
print("DG013 finite exact regression PASS; no infinite positive orbit certified")
