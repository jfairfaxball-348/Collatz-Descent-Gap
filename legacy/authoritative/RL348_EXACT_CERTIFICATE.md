# RL348 exact analytic certificate

Date: 2026-09-18
Status: CLOSED/FROZEN SUPPORT FOR RL348_PROOF_LEDGER.md

## Constants

`a=217976794617`
`ell=137528045312`
`d=a-ell=80448749305`
`2ell=275056090624`
`a-2ell=-57079296007`
`n0=20390252058`

## Universal terminal law

At `r=1`,

`B_1=a-ell g_1`.

For every positive integer gap `g_1>=2`,

`B_1<=a-2ell=-57079296007<1`.

A complete return requires `B_1>=c>=1`, so `g_1=1`. Hence

`B_1=d=80448749305`,
`1<=c<=d`,
`q_(L-1)=1`.

For odd endpoint `E`, `v2(3E+1)=1` is equivalent to `E==3 (mod 4)`.

## Half-cycle synchronization

RL347 gives positive even `D<=2^36`. If the two ordinary shortcut trajectories have equal parity
for one phase, their difference is multiplied by either `1/2` or `3/2`; hence its 2-adic valuation
drops by exactly one. Since `v2(D)<=36`, parity mismatch occurs within at most 36 phases.

## Over-half exact rational boundary

Use

`L2=15757912/22733865 < log 2`.

Put

`S_up=ell/(2 L2)-1/2`.

In the post-crossing complement case,

`t > 6(n0-1)-S_up`.

Exact arithmetic gives

`6(n0-1)-S_up
 = 91143694380395855/3939478
 = 23135982579.518...`.

Therefore

`t>=23135982580`.

The pre-crossing case has

`R>=3n0-4=61170756170`.

Thus universally

`R>=23135982580`

and

`L<=2ell-R=251920108044`.

No finite trajectory enumeration is promoted in RL348.
