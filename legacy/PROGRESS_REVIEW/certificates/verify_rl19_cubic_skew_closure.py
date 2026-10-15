from math import gcd

# Finite red-team verifier for the analytic RL19 cubic-skew closure.
# It does not replace the infinite proof in RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md.


def rot(w,m):
    m%=len(w)
    return w[m:]+w[:m]


def primitive(w):
    return all(w != rot(w,m) for m in range(1,len(w)))


def prefix_diff(source,target):
    A=len(source); out=[0]; s=0
    for i in range(A-1):
        s += target[i]-source[i]
        out.append(s)
    return out


def solve_rotation_from_flow(A,m,F):
    delta=[0]*A
    prev=0
    for i in range(A-1):
        delta[i]=F[i]-prev; prev=F[i]
    delta[A-1]=-prev
    H=gcd(A,m)
    partial=[{}]
    for r0 in range(H):
        vals={r0:0}; r=r0
        while True:
            nr=(r+m)%A; nv=vals[r]+delta[r]
            if nr in vals:
                if nv!=vals[nr]: return []
                break
            vals[nr]=nv; r=nr
        lo=min(vals.values()); hi=max(vals.values())
        if hi-lo>1: return []
        opts=[]
        for c in range(-lo,2-hi):
            z={q:v+c for q,v in vals.items()}
            if all(v in (0,1) for v in z.values()): opts.append(z)
        if not opts: return []
        partial=[{**base,**o} for base in partial for o in opts]
    return [[z[i] for i in range(A)] for z in partial]


def cyclic_gaps(A,T):
    q=sorted(T)
    return (q[1]-q[0],q[2]-q[1],A-q[2]+q[0])


def flow_binary_realizable(A,gaps,r):
    u,v,w=gaps
    T={0,u,u+v}
    inc=[(1 if t in T else 0)-(1 if (t+r)%A in T else 0) for t in range(A)]
    for x0 in (0,1):
        cur=x0; ok=True
        for t,z in enumerate(inc):
            nxt=cur+z
            if t==A-1:
                if nxt!=x0: ok=False
            else:
                if nxt not in (0,1): ok=False; break
                cur=nxt
        if ok: return True
    return False


def norm_eis(a,b):
    return a*a-a*b+b*b

# A. Exact weak-interlacing criterion, including coincidences.
interlace_checks=0
for A in range(6,31):
    for u in range(1,A-1):
        for v in range(1,A-u):
            w=A-u-v
            for r in range(1,A):
                got=flow_binary_realizable(A,(u,v,w),r)
                pred=(r<=min(u,v,w) or A-r<=min(u,v,w)
                      or max(u,v,w)<=min(r,A-r))
                assert got==pred,(A,u,v,w,r,got,pred)
                interlace_checks+=1

# B. Arithmetic inverse-step identity and k-sector geometry on all admissible
# parameter quadruples in a broad finite range.
parameter_checks=0
gap_geometry_checks=0
lift_checks=0
for a in range(2,41):
    A=3*a
    for ell in range(1,a):
        if gcd(a,ell)!=1 or 3**ell>=2**a:
            continue
        X=2**a; Y=3**ell; C=X*X+X*Y+Y*Y
        for m in range(1,A):
            if gcd(m,A)!=1 or (m*ell+1)%a:
                continue
            p=(m*ell+1)//a
            k=next(k for k in (1,2,3) if (k*m-p)%3==0)
            r=k*a-ell
            assert 1<=r<A and (m*r-1)%A==0
            # full-D rational exponent identity represented by exponent pairs
            h=(k*m-p)//3
            assert m*r==1+A*h
            assert 3*ell*h-p*r==-k
            parameter_checks+=1

            # Lift coordinates for every 0<n<a.
            for n in range(1,a):
                hh=(n*m)//a
                J=n*m-a*hh
                I=n*p-ell*hh
                assert a*I-ell*J==n
                assert 1<=J<=a-1 and 1<=I<=ell
                assert 3**(ell-I) < 2**(a-J)
                omega=X*pow(Y,-1,C)%C
                rho=pow(2,m,C)*pow(pow(3,p,C),-1,C)%C
                lhs=pow(rho,n,C)
                rhs=(pow(omega,hh+1,C)*3**(ell-I)*pow(pow(2,a-J,C),-1,C))%C
                assert lhs==rhs
                lift_checks+=1

            # The universal interlacing loop above proves the finite geometry
            # check independently of parameters. Here only check the algebraic
            # specialization of its three alternatives.
            if k==1:
                assert r==a-ell and A-r==2*a+ell
            elif k==2:
                assert min(r,A-r)==a+min(ell,a-ell)<2*a
            else:
                assert A-r==ell
            gap_geometry_checks+=1

# C. Eisenstein size lemma, tested exhaustively for representative coefficient
# ranges. Coefficients are positive and M1,M2<M0.
size_checks=0
for M0 in range(2,24):
    for M1 in range(1,M0):
        for M2 in range(1,M0):
            for e1 in range(3):
                for e2 in range(3):
                    # Z=M0 + M1*zeta^e1 + M2*zeta^e2, reduce to A+B*zeta.
                    A=M0; B=0
                    for M,e in ((M1,e1),(M2,e2)):
                        if e==0: A+=M
                        elif e==1: B+=M
                        else: A-=M; B-=M
                    N=norm_eis(A,B)
                    assert N>0
                    if not (e1==0 and e2==0):
                        assert N < (2*M0)**2
                    size_checks+=1

# D. Direct RL10-convention structural cross-check for the cubic one-orbit
# branch. Normalize the first used flow edge at 0 as in RL10/RL17.
structural_checks=0
equal_gap_structural=0
for A in range(6,25,3):
    a=A//3
    for m in range(1,A):
        if gcd(A,m)!=1: continue
        r=pow(m,-1,A)
        for j in range(1,A-1):
            for kk in range(j+1,A-1):
                F=[0]*(A-1); F[0]=F[j]=F[kk]=-1
                for d in solve_rotation_from_flow(A,m,F):
                    L=sum(d)
                    if gcd(A,L)!=3: continue
                    ell=L//3
                    D=2**A-3**L
                    if D<=1: continue
                    p=sum(d[:m])
                    if a*p-m*ell!=1: continue
                    target=rot(d,m)
                    G=prefix_diff(d,target)
                    T=[]
                    for t in range(A):
                        i=(t*m)%A
                        if G[i]:
                            assert G[i]==-1
                            T.append(t)
                    assert len(T)==3
                    gaps=cyclic_gaps(A,T)
                    assert flow_binary_realizable(A,gaps,r)
                    pred=(r<=min(gaps) or A-r<=min(gaps)
                          or max(gaps)<=min(r,A-r))
                    assert pred
                    kval=next(k for k in (1,2,3) if (k*m-p)%3==0)
                    assert r==kval*a-ell
                    if kval==1: assert min(gaps)>=a-ell
                    elif kval==2: assert max(gaps)<=a+min(ell,a-ell)
                    else: assert min(gaps)>=ell
                    if gaps==(a,a,a):
                        # Equal gaps make g_t periodic with period a; verify the
                        # inherited word is actually nonprimitive.
                        assert not primitive(d)
                        equal_gap_structural+=1
                    structural_checks+=1


# E. End-to-end proof-route audit on small admissible parameters: classify every
# geometrically realizable skew triple into the interior or one of the two
# extreme sectors, and check the exact transformed congruences and size bounds.
route_counts={"gap_a_boundary":0,"interior":0,"k1_extreme":0,"k3_extreme":0,"equal":0}
for a in range(2,16):
    A=3*a
    for ell in range(1,a):
        if gcd(a,ell)!=1 or 3**ell>=2**a: continue
        X=2**a; Y=3**ell; C=X*X+X*Y+Y*Y
        for m in range(1,A):
            if gcd(m,A)!=1 or (m*ell+1)%a: continue
            ppar=(m*ell+1)//a
            ksec=next(k for k in (1,2,3) if (k*m-ppar)%3==0)
            r=ksec*a-ell
            rho=pow(2,m,C)*pow(pow(3,ppar,C),-1,C)%C
            omega=X*pow(Y,-1,C)%C
            assert 27*pow(rho,A,C)%C==1
            for u0 in range(1,A-1):
                for v0 in range(1,A-u0):
                    w0=A-u0-v0
                    if not flow_binary_realizable(A,(u0,v0,w0),r): continue
                    P0=(1+3*pow(rho,u0,C)+9*pow(rho,u0+v0,C))%C
                    if (u0,v0,w0)==(a,a,a):
                        route_counts["equal"]+=1
                        continue
                    rots=[(u0,v0,w0),(w0,u0,v0),(v0,w0,u0)]
                    if a in (u0,v0,w0):
                        cand=next(g for g in rots if g[2]==a)
                        u,v,w=cand
                        d=u-a
                        assert d!=0 and 0<abs(d)<a
                        Prot=(1+3*pow(rho,u,C)+9*pow(rho,u+v,C))%C
                        assert (P0==0)==(Prot==0)
                        # Centered boundary becomes a unit times (rho^d-1).
                        centered=(1+pow(omega,m,C)*pow(rho,d,C)+pow(omega,2*m,C))%C
                        assert centered==Prot
                        assert pow(rho,d,C)!=1
                        assert Prot!=0
                        route_counts["gap_a_boundary"]+=1
                        continue
                    if max(u0,v0,w0)<2*a:
                        cand=next((g for g in rots if a<g[0]<2*a and g[2]<a),None)
                        assert cand is not None
                        u,v,w=cand
                        Prot=(1+3*pow(rho,u,C)+9*pow(rho,u+v,C))%C
                        # Cyclic sparse zeros are equivalent; direct unit relation.
                        # We only need zero-equivalence here.
                        assert (P0==0)==(Prot==0)
                        d=u-a; t=a-w
                        data=[]
                        for n in (d,t):
                            hh=(n*m)//a; J=n*m-a*hh; I=n*ppar-ell*hh
                            data.append((hh,J,I,a-J))
                        S=max(data[0][3],data[1][3])
                        M0=2**S
                        coeffs=[M0]; phases=[0]
                        for idx,(hh,J,I,den) in enumerate(data):
                            coeffs.append(3**(ell-I)*2**(S-den))
                            phases.append(((m if idx==0 else 2*m)+hh+1)%3)
                        assert 0<coeffs[1]<M0 and 0<coeffs[2]<M0 and M0<=X//2
                        Zmod=sum(c*pow(omega,e,C) for c,e in zip(coeffs,phases))%C
                        centered=(1+pow(omega,m,C)*pow(rho,d,C)+pow(omega,2*m,C)*pow(rho,t,C))%C
                        assert centered==Prot
                        assert Zmod==(pow(2,S,C)*centered)%C
                        AA=0; BB=0
                        for c,e in zip(coeffs,phases):
                            if e==0: AA+=c
                            elif e==1: BB+=c
                            else: AA-=c; BB-=c
                        NZ=norm_eis(AA,BB)
                        assert NZ>0
                        if len(set(phases))==1:
                            Nint=sum(coeffs)
                            assert Nint<C
                        else:
                            assert NZ<X*X<C
                        assert P0!=0
                        route_counts["interior"]+=1
                    else:
                        cand=next(g for g in rots if g[2]>=2*a)
                        u,v,w=cand
                        Prot=(1+3*pow(rho,u,C)+9*pow(rho,u+v,C))%C
                        assert (P0==0)==(Prot==0)
                        if ksec==1:
                            rr=a-ell; x=u-rr; y=v-rr; n=x+y
                            assert x>=0 and y>=0 and n<=ell-rr
                            desc=(1+2*pow(rho,x,C)+4*pow(rho,n,C))%C
                            assert Prot==desc
                            if n>0: assert 3**n*7**rr < X*X < C
                            else: assert desc==7%C and C>7
                            assert Prot!=0
                            route_counts["k1_extreme"]+=1
                        elif ksec==3:
                            x=u-ell; y=v-ell; n=x+y
                            assert x>=0 and y>=0 and n<=a-2*ell
                            desc=(4+6*pow(rho,x,C)+9*pow(rho,n,C))%C
                            assert (4*Prot)%C==desc
                            if n>0:
                                assert 2*ell<a
                                assert 2**n*16**ell < X*X < C
                            else: assert desc==19%C and C>19
                            assert Prot!=0
                            route_counts["k3_extreme"]+=1
                        else:
                            raise AssertionError((a,ell,m,(u0,v0,w0),ksec))

print('RL19 cubic-skew analytic-closure verifier: PASS')
print('weak-interlacing gap checks:',interlace_checks)
print('admissible parameter checks:',parameter_checks)
print('k-sector geometrically realizable gap checks:',gap_geometry_checks)
print('Eisenstein lift checks:',lift_checks)
print('Eisenstein coefficient-size checks:',size_checks)
print('RL10-convention cubic structural checks:',structural_checks)
print('equal-gap structural nonprimitivity checks:',equal_gap_structural)
print('end-to-end proof-route classifications:',route_counts)
