from math import gcd
from itertools import product
from fractions import Fraction


def modpow_signed(a,e,n):
    return pow(a,e,n) if e>=0 else pow(pow(a,-1,n),-e,n)

params=0; triples=0; skew_positive=0; cofactor_zeros=[]
for a in range(2,31):
    for ell in range(1,a):
        if gcd(a,ell)!=1 or (1<<a)<=3**ell:
            continue
        X=1<<a; Y=3**ell; C=X*X+X*Y+Y*Y
        for m in range(1,3*a):
            if gcd(3*a,m)!=1: continue
            z=1+m*ell
            if z%a: continue
            p=z//a
            if not (0<=p<=m and 0<=3*ell-p<=3*a-m): continue
            params+=1
            rho=(pow(2,m,C)*pow(pow(3,p,C),-1,C))%C
            eps=(3*pow(rho,a,C))%C
            assert (eps*eps+eps+1)%C==0
            assert pow(eps,3,C)==1
            q=Fraction(2**m,3**p)
            pw=[1]*(3*a+1)
            for k in range(1,3*a+1): pw[k]=pw[k-1]*rho%C
            for u in range(1,3*a-1):
                for v in range(1,3*a-u):
                    w=3*a-u-v
                    triples+=1
                    d1=u-a; t=a-w
                    A=(modpow_signed(rho,d1,C)-1)%C
                    B=(modpow_signed(rho,t,C)-1)%C
                    P=(1+3*pw[u]+9*pw[u+v])%C
                    # Exact phase-centered identity.
                    assert P==(1+eps*modpow_signed(rho,d1,C)+(eps*eps)*modpow_signed(rho,t,C))%C
                    centered=(eps*A+(eps*eps)*B)%C
                    assert centered==P  # 1+eps+eps^2=0
                    N=(A*A-A*B+B*B)%C
                    assert N==((A+eps*B)*(A+(eps*eps)*B))%C
                    if P==0:
                        assert N==0
                        cofactor_zeros.append((a,ell,m,p,u,v,w))
                    if (u,v,w)!=(a,a,a):
                        Aq=q**d1-Fraction(1)
                        Bq=q**t-Fraction(1)
                        Nq=Aq*Aq-Aq*Bq+Bq*Bq
                        assert Nq>0
                        skew_positive+=1

# In this declared finite domain the only cofactor zeros are equal gaps, as expected.
assert all((u,v,w)==(a,a,a) for a,ell,m,p,u,v,w in cofactor_zeros)
print('RL18 cubic phase/norm reduction verifier: PASS')
print('parameter quadruples a<=30:', params)
print('gap triples checked:', triples)
print('skew rational norm positivity checks:', skew_positive)
print('cofactor zeros (all equal-gap):', len(cofactor_zeros))
