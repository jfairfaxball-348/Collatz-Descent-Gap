from fractions import Fraction
from itertools import product
from math import gcd

# Finite exact-algebra red-team for RL19 global weighted population identities.
# The least-state integer packing theorem is analytic; this script checks its
# underlying word identities and suffix domination on small words.


def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))


def rot(w,m):
    m%=len(w)
    return w[m:]+w[:m]


def pref(w):
    P=[0]; s=0
    for b in w:
        s+=b; P.append(s)
    return P

word_checks=0
rotation_checks=0
suffix_checks=0
population_checks=0

for A in range(3,11):
    for bits in product((0,1),repeat=A):
        w=list(bits); L=sum(w)
        if not (0<L<A): continue
        D=2**A-3**L
        if D<=0: continue
        Q=Qword(w)
        R=Fraction(Q,D)
        P=pref(w)
        lam=Fraction(2**A,3**L)
        q=[Fraction(2**i,3**P[i]) for i in range(A)]
        Z=sum(q,Fraction(0))
        assert Z==(lam-1)*(4*R+1)
        word_checks+=1

        O=sum((q[i] for i,b in enumerate(w) if b),Fraction(0))
        E=sum((q[i] for i,b in enumerate(w) if not b),Fraction(0))
        assert E-O/Fraction(3)==lam-1
        assert O==3*R*(lam-1)
        assert E==(R+1)*(lam-1)
        population_checks+=1

        # Every rotation gives the exact arbitrary-radius weighted difference.
        for m in range(1,A):
            wr=rot(w,m); Pr=pref(wr); Rm=Fraction(Qword(wr),D)
            G=[Pr[i]-P[i] for i in range(A)]
            lhs=sum((q[i]*(Fraction(1,3)**G[i]-1) for i in range(A)),Fraction(0))
            rhs=4*(lam-1)*(Rm-R)
            assert lhs==rhs
            rotation_checks+=1

        # Check suffix domination directly against rotated phase numerators.
        # No integrality/minimality is needed for this underlying inequality.
        for i in range(A):
            xi=Fraction(Qword(rot(w,i)),D)
            assert xi>0
            assert q[i] <= lam*R/xi
            suffix_checks+=1

print('RL19 global weighted-population verifier: PASS')
print('exact positive-lift word checks:',word_checks)
print('weighted arbitrary-radius rotation checks:',rotation_checks)
print('odd/even weighted-population checks:',population_checks)
print('suffix-domination point checks:',suffix_checks)
