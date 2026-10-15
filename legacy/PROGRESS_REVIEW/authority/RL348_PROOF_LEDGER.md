# RL348 proof ledger — terminal law, half-cycle synchronization, and strict-late over-half localization

Date: 2026-09-18
Status: CLOSED/FROZEN
Incoming BASE_HEAD: `0eceb96a938c0ec0464f47624d0a24199b854d56`
Successor: RL349

## Scope

All promoted statements remain only in the inherited ordered genuine `g=2`, `Z0>0`, `K<0`
parent with

`(a,ell)=(217976794617,137528045312)`,

the genuine full two-row physical cycle, exact inherited ownership/pruning, the live inherited
high-carry subbranch where required, and the external conditional least-state floor `m>=2^71`.

R1 remains OPEN. Phase 4 remains OPEN. Phase 5 was not resumed.

RL348 was explicitly restricted to closing Phase 4. It did not prove `O_75=empty`; therefore no
Phase-5 mathematics was performed.

## RL348.1 — universal terminal gap/tag law for every Phase-4 return

Use the inherited RL344 endpoint-forward notation

`B_r=a r-ell G_r`

and exact phase tag `c in {1,...,ell}`. For every complete return and every proper
`1<=r<L`,

`q_(L-r)=1+floor((B_r-c)/ell)`

and completeness implies `B_r>=c`.

For every Phase-4 return `L>=75`, `r=1` is proper. Let its first endpoint-forward accelerated
gap be `g_1=G_1>=1`. Then

`B_1=a-ell g_1`.

If `g_1>=2`, then

`B_1<=a-2ell=-57079296007<1<=c`,

contradicting completeness. Hence exactly

`g_1=1`.

Now `B_1=a-ell=80448749305`. Therefore

`1<=c<=80448749305`

and, since `0<=B_1-c<ell`,

`q_(L-1)=1`.

For an odd physical endpoint `E`, `g_1=v2(3E+1)=1`, so

`E == 3 (mod 4)`.

Thus every Phase-4 complete return terminates at a q=0 endpoint whose immediate forward odd step
has exact gap one, whose adjacent profile height is exactly one, and whose phase tag lies in the
strict interval above.

Classification: exact analytic all-length Phase-4 theorem.

## RL348.2 — half-cycle parity synchronization window

Retain the promoted RL347 half-cycle result. Any phase-potential-nondecreasing `L=ell` return is a
matched contact pair of distinct odd physical states `S,E` with

`D=E-S`,
`D` positive even,
`2<=D<=2^36`.

Consider their ordinary shortcut trajectories phase-by-phase. As long as the two current states have
the same parity bit, their difference changes by

- `D -> D/2` on an even/even phase;
- `D -> 3D/2` on an odd/odd phase.

In either case the 2-adic valuation drops by exactly one. Since a positive integer
`D<=2^36` has `v2(D)<=36`, the two physical parity words must disagree within at most 36 ordinary
binary phases from the contact.

This is only a bounded-interface theorem. It does not eliminate the half-cycle class.

Classification: exact analytic physical synchronization contraction.

## RL348.3 — over-half q=0 support is entirely strict late-row

Let a complete Phase-4 return have `L>ell` and set

`R=2ell-L<ell`.

RL347 proves that every q=0 vertex lies on the complementary arc of length `R`.

Suppose an early-row q=0 vertex existed at matched rank `i`. The inherited paired-row identity

`q_v(i)=q_u(i)+d_i`, `d_i>=0`

would force `d_i=0` and a matched late-row q=0 vertex exactly `ell` odd ranks away. Both q=0
vertices would have to lie on the complement, impossible because its length is strictly below
`ell`.

Hence no early-row q=0 vertex exists. A late-row q=0 contact would have such an early-row q=0 mate,
so no late-row q=0 contact exists either. Therefore every q=0 vertex of an over-half complete return
is a strict late-row q=0 vertex.

Because the complementary arc has late-row endpoints and length `<ell`, it cannot leave the late row
and return to it: doing so would require traversing the entire other row. Thus the complement is one
strict-late interval. Since the global least state is q=0, its matched rank `k` lies on this interval.

Classification: exact analytic two-row geometry theorem.

## RL348.4 — crossing split sharpens the universal over-half bound

Write the strict-late complement as a matched-rank interval `[s,e]` containing the least-root rank
`k`, so

`s<=k<=e`,
`R=e-s`.

Let `j<k` be the inherited unique H-carry crossing rank and let

`T=k-j`.

### Case A: `s<=j`

Then the complement contains the whole crossing-to-root interval, so

`R>=T`.

RL325 gives at least `3n-4` strict matched ranks in that interval. Therefore

`R>=T>=3n-4`.

At the inherited high-carry floor `n>=20390252058`,

`R>=61170756170`.

### Case B: `j<s<=k`

Put

`t=k-s`.

Use the inherited RL326 canonical crossing-to-root profile

`q_r`, `1<=r<=T`,

where rank `k-r` is the corresponding late-row physical state. If `r>t`, then `k-r<s`, hence that
state lies outside the complementary interval. Since every q=0 state lies on the complement,

`q_r>0` for every `r>t`.

RL326 gives

`n-1 < (1/3) sum_(r=1)^T c_r 2^(-q_r)`

with `0<c_r<1`. Therefore

`n-1
 < (1/6)[sum_(r=1)^T c_r + sum_(r=1)^t c_r]
 < (S+t)/6`,

where

`S=sum_(r=1)^(ell-1)c_r < ell/(2 log 2)-1/2`.

Using the inherited exact lower enclosure

`log 2 > 15757912/22733865`

and `n>=20390252058` gives exactly

`t > 91143694380395855/3939478
   = 23135982579.518...`.

Hence integrally

`t>=23135982580`.

Since `R>=t`, this case also has

`R>=23135982580`.

Combining the two cases yields the new universal over-half consequence

`R>=23135982580`,
`L=2ell-R<=251920108044`.

This improves the promoted RL347 integer bound by one event, but the main gain is geometric:
all q=0 support is a single strict-late interval containing `k`, with an exact crossing split.

Classification: exact analytic high-carry theorem plus exact rational constant certificate.

## What RL348 does NOT prove

RL348 does not prove `O_75=empty`. Phase 4 remains OPEN.

The residual classes remain:

- `75<=L<ell`;
- `L=ell`, now a bounded matched contact pair with a forced parity mismatch within 36 binary phases;
- `ell<L<=251920108044`, with every q=0 state on one strict-late complement interval containing `k`.

The bounded incoming signatures, mixed 2/3-adic predecessor/successor tests, exact row/wrap
decoration, ownership/pruning, phase-potential sign, and least-state descent have not yet been
consumed in one gap-free closure argument across all three classes.

Phase 5 remains untouched.

## Successor discipline

By direct user instruction, RL349 is an aggressive one-session Phase-4 closure attempt.

Its sole mathematical success condition is

`O_75=empty`.

RL349 must not plan another sequence of incremental contraction sessions. It must attack the three
remaining classes as closure obligations and continue through them in the same research session,
subject to the binding connector resumability protocol. User-facing checkpoints inside that session
should occur only for elimination of an entire residual class, a theorem that merges classes, a
decisive correction, or a proved architecture barrier—not for another small numerical tightening.

If `O_75=empty` is proved, stop mathematics immediately and close RL349. Do not begin Phase 5 in
the same session.

`PARENT_DIFFICULTY_DELTA = EASIER`.
