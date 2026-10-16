#!/usr/bin/env python3
"""DG017 exact finite arithmetic checks; not an infinite Collatz proof."""
from collections import defaultdict
from fractions import Fraction

def T(x):
    return x//2 if x%2==0 else (3*x+1)//2

def trace(n, steps):
    xs=[n]
    for _ in range(steps):
        xs.append(T(xs[-1]))
    return xs

def first_descent(n, xs):
    return next((i for i,x in enumerate(xs) if x<n),len(xs))

def uniform_weights(n, xs):
    B=Fraction(n+2,2*(n+1))
    W=Fraction(1)
    out=[W]
    for x in xs[:-1]:
        W*=Fraction(3,2) if x%2 else B
        out.append(W)
    return out

def check(n, maxsteps=90, hmax=15):
    xs=trace(n,maxsteps+hmax)
    stop=min(first_descent(n,xs)-1,maxsteps)
    W=uniform_weights(n,xs)
    for t in range(stop+1):
        assert xs[t]>=n
        assert Fraction(xs[t]+1,n+1)<=W[t],(n,t)
        assert W[t]>=1,(n,t)
    pars=''.join(str(x%2) for x in xs)
    checks=0
    strict=0
    wrong_q=None
    for h in range(1,hmax+1):
        seen=defaultdict(list)
        for q in range(stop+1):
            factor=pars[q:q+h]
            for p in seen[factor]:
                if xs[p]==xs[q]:
                    continue
                assert (xs[q]-xs[p])%(1<<h)==0,(n,p,q,h)
                assert (n+1)*max(W[p],W[q])>=n+1+(1<<h),(n,p,q,h)
                assert (n+1)*Fraction(3,2)**q>=n+1+(1<<h),(n,p,q,h)
                if max(W[p],W[q])<Fraction(3,2)**q:
                    strict+=1
                if wrong_q is None and (n+1)*W[q]<n+1+(1<<h):
                    wrong_q=(n,p,q,h,xs[p],xs[q])
                checks+=1
            seen[factor].append(q)
    return stop,checks,strict,wrong_q

def main():
    N=1500
    result=[check(n) for n in range(2,N+1)]
    print('PASS positive finite-prefix cases n=2..%d:'%N,
          sum(x[1] for x in result),'collision tests;',
          sum(x[2] for x in result),'strict weighted improvements')
    counter=next((x[3] for x in result if x[3]),None)
    print('Counterexample to using W_q without max(W_p,W_q):',counter)
    assert counter==(3,2,3,1,8,4)
    for k in [15,25,40,60]:
        n=(1<<k)-1
        stop,checks,strict,wrong=check(n,maxsteps=k,hmax=10)
        assert stop==k and checks>0
        print('Mersenne shadow: exponent',k,'seed bits',n.bit_length(),
              'finite steps',stop,'collisions',checks)
    xs=trace(15,7)
    assert xs==[15,23,35,53,80,40,20,10]
    print('PASS 15->20 finite-floor countermodel')

    def champer(k):
        return ''.join(''.join(str(i//3**j%3) for j in range(w-1,-1,-1))
              for w in range(1,k+1) for i in range(3**w))
    word=champer(5)
    for h in range(1,6):
        assert len({word[j:j+h] for j in range(len(word)-h+1)})==3**h
    print('PASS ternary high-complexity finite factor family h=1..5')

    def mountain(r):
        s=1
        while 3**s<=2**(s+r):
            s+=1
        return '1'*s+'0'*r

    def cylinder_seed(binary_word):
        a,b,D=1,0,1
        for digit in binary_word:
            if digit=='1':
                a,b=3*a,3*b+D
            D*=2
        first=(-b*pow(a,-1,D))%D
        for k in range(100,103):
            n=first+k*D
            if n%3==0:
                return n
        raise AssertionError('CRT failure')

    for count in [5,12,30]:
        rs=[(5,11,17)[int(c)] for c in word[:count]]
        blocks=[mountain(r) for r in rs]
        n=cylinder_seed(''.join(blocks))
        a=n
        for block in blocks:
            x=a
            for j,digit in enumerate(block):
                assert x%2==int(digit)
                x=T(x)
                if j<len(block)-1:
                    assert x>a
            assert x>a and x%9==7
            a=x
        print('PASS Champernowne finite strict mountains:',count,
              'blocks; initial seed bits',n.bit_length())
    print('All DG017 exact finite checks PASS; no proof of E empty.')

if __name__=='__main__':
    main()
