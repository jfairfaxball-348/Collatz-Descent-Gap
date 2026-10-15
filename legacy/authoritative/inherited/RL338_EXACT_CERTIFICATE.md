# RL338 exact q=35 physical certificate

Date: 2026-09-16
Status: FROZEN EXACT FINITE CERTIFICATE under the inherited ordered `g=2`, `Z0>0`, `K<0` branch assumptions and external least-state-floor qualification.

## Definitions and inherited reconstruction

Use the inherited state band `2^71 <= P < 2^76+2^36`, high-carry ownership threshold `n>=20390252058`, exact mechanical factors, admissible positive profiles, residue reconstruction, parity checks, and affine owned-state test from RL336/RL337.

For the q=35 step potential `Phi(z)=0` for `z<=21` and `Phi(z)=35` for `z>=22`, every high-to-high return of positive-run length `p` has reduced charge

`R(z,p)=2z-8p`.

Thus only p=5,6,7,8 can be positive when `z<=35`; p>=9 is automatically nonpositive.

## Complete positive-region enumeration

The complete q=35-positive high-to-high regions were reconstructed exactly:

| p | source z range | ordered pair labels | admissible templates | state-band candidates | owned rows | boundary cores |
|---|---|---:|---:|---:|---:|---:|
| 5 | 22..35 | 196 | 64,120 | 299 | 161 | 68 |
| 6 | 25..35 | 154 | 130,386 | 10 | 8 | 4 |
| 7 | 29..35 | 98 | 185,360 | 0 | 0 | 0 |
| 8 | 33..35 | 42 | 204,590 | 0 | 0 | 0 |

For p=5, every owned row has source label z in `{22,23,24}`. For p=6, every owned row has source label z=25. Hence the only physically surviving positive reduced charges are `+4,+6,+8` for p=5 and `+2` for p=6.

A **boundary core** is the triple `(B,E,q)`, where `B` is the exact physical state at sequence index `left-1` immediately before the deformed positive-run interface, `E` is the exact run-exit state at index `left+p`, and `q` is the positive profile. Under this definition the 161 p=5 labeled rows collapse to 68 boundary cores and the 8 p=6 rows collapse to 4. If the full left-context source state is retained instead, the p=5 rows give 83 triples; this distinction is terminological only and is recorded to prevent ambiguity.

The right-context labels of exceptional rows satisfy:

- p=5: `22 <= right <= 29`;
- p=6: `22 <= right <= 24`.

There are 125 distinct `(right-context, exact exit-state)` successor interfaces, distributed as

`22:68, 23:32, 24:12, 25:5, 26:2, 27:2, 28:2, 29:2`.

## Gap-free successor reconstruction

For every one of those 125 exact interfaces, every successor right label `1..35` was checked for successor positive-run lengths p=1..8.

For p=1..4 there are exactly 24 owned exact shared-state continuations. Their `(p,left,right)` multiplicities are:

`(1,22,1):3, (1,22,2):2, (1,22,3):1, (2,22,1):4, (2,22,2):2, (2,22,3):1, (3,22,1):1, (4,22,1):1, (1,23,1):4, (1,23,2):1, (1,24,1):1, (1,24,2):1, (1,24,3):1, (1,27,1):1`.

Every one has reduced q=35 charge at most `-30`. The exact charge multiplicities are

`-64:1, -56:1, -48:4, -46:2, -44:1, -40:3, -38:6, -36:3, -34:1, -32:1, -30:1`.

For p=5..8 there are exactly five owned exact shared-state continuations. All five have signature

`p=7, left=22, right=1`

and reduced q=35 charge `-88`. No p=5, p=6, or p=8 owned successor exists from an exceptional exit, and context 29 has no p=1..8 owned successor at all.

If the immediate successor instead has p>=9, the exceptional right-context bound gives the uniform analytic estimate

`R_successor <= 2*29 - 8*9 = -14`

for a high target; low targets are more negative.

Therefore every exceptional edge has charge at most `+8` and its immediate successor has charge at most `-14` (or at most `-30` / `-88` in the exactly reconstructed shorter cases). Every exceptional-successor pair has net charge at most `-6`.

## All-length consequence

All nonexceptional surviving returns have reduced charge <=0. Exceptional edges cannot be consecutive and each nonterminal exceptional edge is paired with its immediate successor. Hence the total reduced path charge is at most `+8`, from a possible terminal unmatched exceptional edge.

Untelescoping the step potential of range 35 yields

`35(K-2H)-S <= 43`,

or equivalently

`2H >= K - S/35 - 43/35`.

Classification: exact finite physical certificate plus analytic all-length amortization. It is conditional only through the inherited branch/state-floor assumptions used by the physical ownership certificates.
