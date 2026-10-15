#!/usr/bin/env python3
"""DG005 bounded exact regression, NOT a certification of E=empty.

Proved formulas are in research/sessions/DG005.md. Finite traces do not
certify actual exceptional points: no nontrivial exception is known.
"""

def T(x):
    return x // 2 if x % 2 == 0 else (3*x + 1) // 2


def finite_distinct_trace(n, horizon=150):
    out = []
    seen = set()
    while n not in seen and len(out) < horizon:
        seen.add(n)
        out.append(n)
        n = T(n)
    return out


def suffix_records(x):
    records = []
    least = None
    for i in range(len(x)-1, -1, -1):
        if least is None or x[i] < least:
            least = x[i]
            records.append((i,x[i]))
    return records[::-1]


# 3-adic observation: an orbit from an odd seed has no multiple of 3 at positive time.
checked_3 = 0
for n in range(3,5002,2):
    x = n
    for _ in range(90):
        x = T(x)
        assert x % 3 != 0, (n,x)
        checked_3 += 1

# Pairwise successive truncated-tail minima (no assumption of exceptional status).
# Fixed length 40 produces many nontrivial record transitions.
record_pairs = 0
long_gap_2mod3 = 0
immediate_pairs = 0
for n in range(3,50002,2):
    trace = [n]
    for _ in range(39):
        trace.append(T(trace[-1]))
    records = suffix_records(trace)
    for (i,a),(j,b) in zip(records,records[1:]):
        d = j-i
        assert a < b <= T(a)
        assert d != 2
        assert b % 3 != 0
        if d == 1:
            immediate_pairs += 1
            assert b == T(a) and b % 3 == 2
        else:
            assert d >= 3 and trace[j-1] == 2*b
            if b % 3 == 2 and b >= 5:
                z,rem = divmod(2*b-1,3)
                assert rem == 0 and 2 <= z < b and T(z) == b
                # No off-orbit inference is made for traces with repeats.
                if len(set(trace)) == len(trace):
                    assert z not in trace
                long_gap_2mod3 += 1
        record_pairs += 1

# Model of abstract record minima avoiding 3mod8, multiples of three,
# and the recorded least-E arithmetic exclusions. NOT an actual orbit.
f = [(10 * 5**j)//4**j for j in range(100)]
b = [648*x + 55 for x in f]
assert all(b[i] < b[i+1] and 2*(b[i+1]+1) <= 3*(b[i]+1) for i in range(99))
assert all(v%648==55 and v%8==7 and v%3==1 for v in b)
assert all(v%6!=5 and v%18!=13 and v%162!=91 and
           v%1458 not in (433,1333) for v in b)

# Whole-E-disjoint parameter progressions with exact first descent for h=0.
family = []
for k in range(2,8):
    r = 3**(k-1)
    assert (2**r + 1) % 3**k == 0
    t = (2**r + 1) // 3**k
    n = (2**k)*t-1
    assert n >= 3 and n < 2**r
    x=n
    first = None
    for j in range(1,k+r+1):
        x=T(x)
        if j <= k:
            assert x == 3**j * 2**(k-j) * t - 1
        if first is None and x < n:
            first=j
    assert x==1
    predicted=k+r-(n.bit_length()-1)
    assert first==predicted and first>k
    family.append((k, r, first, n.bit_length()))
    for h in (0, 1, 2, 7, 100):
        seed = n + (1 << (k+r))*h
        y=seed
        for j in range(1,k+r+1):
            if j<=k: assert y%2==1
            if k<j<=k+r: assert y%2==0
            y=T(y)
            if j<=k: assert y>seed
        assert y==1+3**k*h and y<seed

# Boundary check: at n=1 parity 10 has contraction without strict descent.
# It does not yield any positive n>=2 exceptional integer.
x=1; word=[]; odds=0
for _ in range(2):
    bit=x%2; word.append(str(bit)); odds+=bit; x=T(x)
assert ''.join(word)=='10' and 3**odds < 2**2 and x==1

print('Odd-origin future 3-adic iterate checks:',checked_3)
print('Finite horizon-40 tail-record transitions:',record_pairs)
print('  immediate:',immediate_pairs,'long gap with 2 mod 3 target:',long_gap_2mod3)
print('Sparse adversarial 55 mod 648 sequence checked:',len(b))
print('Certified variable-depth descending family (k,r,sigma,seed_bits):',family)
print('Complete residue-family examples checked:', 5*len(family))
print('PASS: bounded exact arithmetic only; E=empty remains open')
