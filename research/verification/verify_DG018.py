#!/usr/bin/env python3
"""DG018: exact finite tests of the universal mountain side-entrance identity.
These are finite tests, not certification of any E member or infinite orbit.
"""
from fractions import Fraction
from collections import Counter


def T(n):
    return n // 2 if n % 2 == 0 else (3*n+1)//2

def mountain(r):
    s=1
    while 3**s<=2**(s+r):
        s+=1
    return s, '1'*s+'0'*r

def cylinder_seed(word):
    A,Q,D=1,0,1
    for c in word:
        if c=='1':
            A,Q=3*A,3*Q+D
        D*=2
    residue=(-Q*pow(A,-1,D))%D
    return residue+100*D

def champer(k):
    return ''.join(''.join(str(i//(3**j)%3) for j in range(w-1,-1,-1))
                   for w in range(1,k+1) for i in range(3**w))

def check_mountain_sequence(rs):
    blocks=[mountain(r) for r in rs]
    n=cylinder_seed(''.join(w for _,w in blocks))
    t=0; a=n; side_roots=[]; meetings=[]; events=[]
    for r,(s,w) in zip(rs,blocks):
        d=s+r
        assert s>=4 and r>=2 and pow(3,s)>pow(2,d)
        original=[a]
        for digit in w:
            assert original[-1]%2==int(digit)
            original.append(T(original[-1]))
        b=original[-1]
        assert all(y>b for y in original[1:-1]), (r,s)
        assert b>a
        assert (3*a-1)%4==0
        z=(3*a-1)//4
        assert 2<=z<a<b
        altword='1'*(s-2)+'01'+'0'*(r-2)
        assert len(altword)==d-2
        alt=[z]
        for digit in altword:
            assert alt[-1]%2==int(digit)
            alt.append(T(alt[-1]))
        assert alt[-1]==b
        assert all(y>=z for y in alt)
        assert alt[s]==original[s+2]
        for p in range(s):
            assert alt[p]!=original[p+2]
        assert all(original[u]>a for u in range(1,d))
        meetings.append(t+s+2)
        side_roots.append(z)
        events.append((r,s,d,z,a,b))
        a=b; t+=d
    assert len(set(side_roots))==len(side_roots), 'distinct side roots'
    assert len(set(meetings))==len(meetings), 'distinct first meetings'
    assert all(events[j][4]<events[j+1][4] for j in range(len(events)-1))
    return n.bit_length(),events,meetings

for count in [5,12,30,60]:
    rs=[(5,11,17)[int(c)] for c in champer(4)[:count]]
    bits,events,meetings=check_mountain_sequence(rs)
    print('PASS Champernowne',count,'mountain bridges; seed bits',bits,
          'distinct strict-safe side roots',len(meetings),
          'first root/record/endpoint',events[0][3:])
for r in [5,11,17,23,29,35,59,83]:
    bits,events,meetings=check_mountain_sequence([r])
    print('PASS variable-length r =',r,'length',events[0][2], 'source bits',bits)

# A valid strict rising finite example with r=2, s=4, outside the large mountain family.
x=15; w='111100'; xs=[x]
for c in w:
    assert xs[-1]%2==int(c)
    xs.append(T(xs[-1]))
z=(3*x-1)//4
alt=[z]
for c in '1101':
    assert alt[-1]%2==int(c)
    alt.append(T(alt[-1]))
assert xs == [15,23,35,53,80,40,20]
assert alt == [11,17,26,13,20]
assert alt[-1]==xs[-1] and min(alt)==z
print('PASS small explicit safe sibling 15->20, 11->20')

# Nonmountain strict bridge is NOT covered by the construction.
x=27; xs=[x]
for c in '110':
    assert xs[-1]%2==int(c)
    xs.append(T(xs[-1]))
assert xs == [27,41,62,31]
print('PASS nonmountain 27->31 remains outside the theorem')

print('DG018 finite side-entrance checks PASS; does not prove E empty.')
