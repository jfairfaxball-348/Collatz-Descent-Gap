from fractions import Fraction
from itertools import product
from math import log

# Exact finite red-team of the algebra behind R19P.1 on small cyclic words.
# The distinct-state packing theorem itself is analytic and conditional on a
# primitive positive integer cycle; this script does not substitute a scan for it.

def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))

def rot(w,m):
    m%=len(w)
    return w[m:]+w[:m]

checks=0
integer_cycle_checks=0
for A in range(2,11):
    for bits in product((0,1), repeat=A):
        w=list(bits); L=sum(w)
        if not (0<L<A):
            continue
        D=2**A-3**L
        if D<=0:
            continue
        Q=Qword(w)
        R=Fraction(Q,D)
        if R<=0:
            continue
        xs=[Fraction(Qword(rot(w,i)),D) for i in range(A)]
        lam=Fraction(2**A,3**L)
        prodv=Fraction(1)
        for i,b in enumerate(w):
            if b:
                prodv *= 1 + Fraction(1,3*xs[i])
        assert prodv == lam
        checks += 1

        if all(x.denominator==1 and x>0 for x in xs):
            # For an actual integer cycle, check the exact step recurrence too.
            for i,b in enumerate(w):
                x=xs[i]; y=xs[(i+1)%A]
                if b:
                    assert y == (3*x+1)/2
                else:
                    assert y == x/2
            integer_cycle_checks += 1

# Explicit primitive 1-2 shortcut cycle sanity check.
w=[1,0]
D=2**2-3
R=Fraction(Qword(w),D)
xs=[Fraction(Qword(rot(w,i)),D) for i in range(2)]
assert R==1 and xs==[1,2]
assert Fraction(4,3) == 1+Fraction(1,3*xs[0])

print('RL19 global odd-step product verifier: PASS')
print('exact product word checks:', checks)
print('positive integer-cycle word checks:', integer_cycle_checks)
