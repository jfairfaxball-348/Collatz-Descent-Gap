from math import gcd
from itertools import product


def Qword(w):
    pos=[i+1 for i,b in enumerate(w) if b]
    L=len(pos)
    return sum((1<<(p-1))*3**(L-k-1) for k,p in enumerate(pos))

def rot(w,m): return w[m:]+w[:m]

def prefix_counts(w):
    P=[0]; s=0
    for b in w:
        s+=b; P.append(s)
    return P

def modpow_signed(a,e,n):
    return pow(a,e,n) if e>=0 else pow(pow(a,-1,n),-e,n)

checks=0; orbit_checks=0; qsum_checks=0
for A in range(3,11):
    for bits in product([0,1], repeat=A):
        w=list(bits); L=sum(w)
        if not (0<L<A): continue
        D=(1<<A)-3**L
        if D<=1 or gcd(D,6)!=1: continue
        P=prefix_counts(w)
        q=[]
        for i in range(A):
            q.append((pow(2,i,D)*modpow_signed(3,-P[i],D))%D)
        Z=sum(q)%D
        assert Qword(w)%D == (pow(4,-1,D)*pow(3,L,D)*Z)%D
        assert (Qword(w)%D==0)==(Z==0)
        qsum_checks+=1
        for m in range(1,A):
            target=rot(w,m); Pt=prefix_counts(target); p=P[m]
            rho=(pow(2,m,D)*modpow_signed(3,-p,D))%D
            G=[Pt[i]-P[i] for i in range(A)]
            for i in range(A):
                j=(i+m)%A
                assert q[j] == (rho*modpow_signed(3,-G[i],D)*q[i])%D
                checks+=1
            g=gcd(A,m); h=A//g
            seen=set(); total=0
            for i0 in range(g):
                # Since m may not preserve literal residue i0 mod g only if labels align;
                # starts 0..g-1 give the g shift orbits.
                i=i0; S=0; orbit_sum=0
                for k in range(h):
                    assert i not in seen
                    seen.add(i)
                    term=(q[i0]*pow(rho,k,D)*modpow_signed(3,-S,D))%D
                    assert term==q[i]
                    orbit_sum=(orbit_sum+term)%D
                    S += G[i]
                    i=(i+m)%A
                assert i==i0
                total=(total+orbit_sum)%D
                orbit_checks+=1
            assert len(seen)==A and total==Z

print('RL18 global orbit-sum identity verifier: PASS')
print('Q<->Z word checks:', qsum_checks)
print('shift recurrence point checks:', checks)
print('orbit polynomial reconstructions:', orbit_checks)
