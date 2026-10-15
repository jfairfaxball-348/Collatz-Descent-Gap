#!/usr/bin/env python3
"""DG010: exact finite checks, NOT a proof of existence/absence of an infinite exceptional Collatz orbit."""
U,V='111011010','111101010'
BASE={U:(1959,2791),V:(1327,1891)}

def T(n):
    assert n>0
    return n//2 if n%2==0 else (3*n+1)//2

def prefix(w):
    A,q,D=1,0,1
    result=[(A,q,D)]
    for bit in w:
        if bit=='1':
            A,q=3*A,3*q+D
        else:
            assert bit=='0'
        D*=2
        result.append((A,q,D))
    return result

def trace(z,w):
    a=[z]
    for bit in w:
        assert a[-1]%2==int(bit),(w,z,a)
        a.append(T(a[-1]))
    return a

def safe_words(max_depth):
    frontier=[('',1,0,1,0)]
    for d in range(1,max_depth+1):
        new=[]
        for w,A,q,D,s in frontier:
            for bit in '01':
                AA,qq,ss=(3*A,3*q+D,s+1) if bit=='1' else (A,q,s)
                DD=2*D
                if AA<DD:
                    continue
                ww=w+bit
                new.append((ww,AA,qq,DD,ss))
                if AA>DD:
                    yield ww,AA,qq,DD,ss
        frontier=new

def alternatives(orig):
    a0,b0=BASE[orig]
    result=[]
    for w,A,q,D,s in safe_words(18):
        if w==orig or not(7<=s<=12) or A*512<=D*729:
            continue
        if (D*b0-q)%729:
            continue
        M=3**(s-6)
        h0=(((q-D*b0)//729)*pow(4*D,-1,M))%M
        a,b=a0+2048*h0,b0+2916*h0
        num=D*b-q
        assert num%A==0
        z=num//A
        if z<3 or z>=a:
            continue
        dz=D*2916*M//A
        assert D*2916*M%A==0
        if dz<=0 or dz>=2048*M:
            continue
        assert dz%D==0
        for k in (0,1):
            ak,bk=a+2048*M*k,b+2916*M*k
            zk=z+dz*k
            assert 3<=zk<ak<bk
            t=trace(zk,w)
            assert t[-1]==bk and min(t)==zk
            main=trace(ak,orig)
            assert main[-1]==bk and ak<bk<min(main[1:-1])
        result.append((w,h0,M,z,dz,a-z,s))
    return result

for orig in (U,V):
    fam=alternatives(orig)
    covered={h for w,h0,M,*_ in fam for h in range(h0,729,M)}
    source_class=0 if orig==U else 1
    hits={h for h in covered if h%3==source_class}
    old_class=9 if orig==U else 40
    new=sorted(h for h in hits if h%81!=old_class)
    expected=[138,207,276,468] if orig==U else [175,574,643,712]
    assert len(fam)==93 and len(hits)==13
    assert new==expected and len(hits-set(new))==9
    print('PASS',orig,'restricted inverse families',len(fam),
          '3-divisible source h classes 13/243; new',new)

for orig,h0,w,z0,gap0,qq in [
    (U,138,'111111010011011010',199871,84712,842545),
    (V,175,'111011101111100010',252647,107080,823177),
]:
    a0,b0=BASE[orig]
    p=prefix(w)
    A,q,D=p[-1]
    assert (len(w),w.count('1'),A,q,D)==(18,12,531441,qq,262144)
    assert w[-9:]!=orig and all(Ai>=Di for Ai,qi,Di in p)
    assert D*(b0+2916*h0)==A*z0+q
    assert a0+2048*h0-z0==gap0
    dz=D*2916*729//A
    assert dz==1048576 and dz%D==0
    for k in (0,1,5):
        a=a0+2048*(h0+729*k)
        b=b0+2916*(h0+729*k)
        z=z0+dz*k
        t=trace(z,w)
        assert a%3==0 and 3<=z<a<b
        assert a-z==gap0+444416*k
        assert t[-1]==b and min(t)==z
print('PASS divergent full modulo-729 certificates')

samples=[
    ('110',27,31),('111010',327,415),
    ('111111000',63,91),('11111011000',927,991),
    ('11101111101000',1383,1663),
    ('11111011010011010',2463,3331),
]
for w,a0,b0 in samples:
    p=prefix(w)
    A,q,D=p[-1]
    assert a0%3==0 and a0%4==b0%4==3 and b0%3==1
    assert (A*a0+q)==D*b0
    assert A>D and all((D//Di)*Ai>A for Ai,qi,Di in p[1:-1])
    for k in (0,1,3):
        a=a0+12*D*k
        b=b0+12*A*k
        t=trace(a,w)
        assert t[-1]==b and a<b<min(t[1:-1])
        assert a%3==0 and b%3==1
print('PASS gap 3,6,9,11,14,17 full affine families')

def mountain(r):
    assert r>=5 and r%6==5
    s=1
    while 3**s<=2**(s+r):
        s+=1
    w='1'*s+'0'*r
    p=prefix(w)
    A,q,D=p[-1]
    assert 2*D<2*A<3*D
    assert all((D//Di)*Ai>A for Ai,qi,Di in p[1:-1])
    assert (-pow(2,-r,9))%9==7
    return w

def joint_cylinder(words):
    W=''.join(words)
    A,q,D=prefix(W)[-1]
    M=4*D
    residue=((3*D-q)*pow(A,-1,M))%M
    h=(-residue*pow(M,-1,3))%3
    n=residue+M*h
    if n<=1:
        n+=3*M
    for trial in range(30):
        x=n
        good=True
        endpoints=[]
        for w in words:
            path=trace(x,w)
            b=path[-1]
            if not(x<b<min(path[1:-1]) and x%4==b%4==3 and b%9==7):
                good=False
                break
            endpoints.append(b)
            x=b
        if good:
            assert n%3==0
            return n,endpoints
        n+=3*M
    raise AssertionError('no large finite positive bridge seed')

for r in (5,11,17,23,29):
    w=mountain(r)
    n,bs=joint_cylinder([w])
    assert bs[0]%9==7
    print('PASS mountain gap',len(w))
for rr in ((5,11,5),(23,5,17),(17,11,23,5)):
    words=[mountain(r) for r in rr]
    n,bs=joint_cylinder(words)
    assert len(bs)==len(words) and all(b%9==7 for b in bs)
    print('PASS mixed gaps',[len(w) for w in words],'seed 0 mod3')
print('DG010 PASS: only finite/algebraic certificates, NOT E=empty')
