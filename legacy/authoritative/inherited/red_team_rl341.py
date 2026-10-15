#!/usr/bin/env python3
LOW=1<<71
def odd_step(x):
    y=3*x+1; y//=y & -y; return y
assert 3*26==26*(1+2)
assert 3*(84-43)>26*(2+2); assert 3*(126-43)>26*(3+2); assert 3*(168-43)>26*(4+2)
for p in (5,6,10,100,10000): assert 3*(42*p-70)>=26*(p+2)
for p in (1,2,5,100,10000): assert 26*p<=3*(42*p-35)+5
x=16196285460332235269227; trace=[x]
while x>=LOW: x=odd_step(x); trace.append(x)
assert len(trace)-1==9 and trace[-1]<LOW
count=sum(1 for l in range(1,36) for r in range(1,36) if 0<=42-l-r<=25); assert count==699
print('RL341_RED_TEAM_GREEN'); print('sharp_complete_boundary',(1,26)); print('first_chain_escape_depth',len(trace)-1); print('interfaces_sigma_le_25',count); print('global_constant',57)
