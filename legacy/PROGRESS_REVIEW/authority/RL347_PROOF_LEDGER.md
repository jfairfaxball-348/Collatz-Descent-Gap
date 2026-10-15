# RL347 proof ledger — decorated rank decoder, over-half contraction, and matched H-carry quotient

Date: 2026-09-17
Status: CLOSED/FROZEN
Incoming BASE_HEAD: `32354aa440ae1d54a32359c6d0a77aa2f1bdea1e`
Successor: RL348

## Scope

All statements remain only in the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent with

`(a,ell)=(217976794617,137528045312)`,

the genuine full two-row physical cycle, exact inherited ownership/pruning, the live inherited
high-carry subbranch where `n>=20390252058`, and the external conditional least-state floor
`m>=2^71`.

R1 remains OPEN. Phase 4 remains OPEN. Phase 5 was not resumed.

## RL347.1 — exact decorated physical-rank decoder

For the full physical bridge let

`H_t=ceil(a t/ell)` and `u_t=ell H_t-a t`.

At a q=0 physical rank define the phase tag by

`c_t=ell-u_t` in `{1,...,ell}`, with the endpoint convention `u_t=0 => c_t=ell`.

Then

`c_t == a t (mod ell)`.

Since `gcd(a,ell)=1` and

`a^(-1) mod ell = 65470613321`,

the phase tag determines the matched rank modulo `ell`. Exact row identity then determines the
absolute rank modulo the full `2ell` two-row traversal.

Consequently, once exact source/end physical states and their row-phase decorations are fixed,
the directed return length in `1..2ell` is unique. This sharpens RL346's "at most two lengths"
statement: its two representatives arose only because the row identity/wrap acceptance test had not
yet been consumed.

For that unique `L`, the total gap remains forced by

`H=(aL-c_end+c_source)/ell`.

Classification: exact analytic theorem.

## RL347.2 — geometry of complete returns longer than one row

Let a complete q=0-to-q=0 return have `L>ell`.

The paired-row identity is

`q_v(i)=q_u(i)+d_i`, where `d_i=u_i-v_i>=0`.

Thus every early-row q=0 vertex is a contact (`d_i=0`) and has a matched late-row q=0 vertex exactly
`ell` odd ranks away. Conversely, a late-row q=0 contact has that early-row q=0 mate.

If an endpoint of a complete return of length `L>ell` were early-row, or were a late-row contact,
its matched q=0 mate at distance `ell` would lie strictly inside the return, contradicting
completeness. Hence every endpoint of a complete return with `L>ell` is a strict late-row q=0
vertex (`d_i>0`).

Writing

`R=2ell-L < ell`

for the complementary short arc, every q=0 vertex of the full closed walk lies on that complement.

Classification: exact analytic two-row geometry theorem.

## RL347.3 — exact high-carry exclusion of the extreme over-half tail

Use the inherited RL326/RL327 telescope on the genuine least-root interval:

`n-1 < (1/3) sum c_t 2^(-q_t)`,

with every ideal coefficient `0<c_t<1`.

For a complete `L>ell` return, all q=0 positions lie on its complementary arc of length `R`, so
there are at most `R+1` zero-profile positions in any linear subinterval. Every positive q-position
has `2^(-q_t)<=1/2`. Therefore

`n-1 < (S+R+1)/6`,

where

`S=sum_(t=1)^(ell-1) c_t < ell/(2 log 2)-1/2`.

Use the exact rational lower enclosure

`log 2 > 15757912/22733865`.

At the inherited high-carry floor `n>=20390252058`, exact rational arithmetic gives

`R > 91143694376456377/3939478 = 23135982578.518...`.

Hence integrally

`R >= 23135982579`

and therefore

`L <= 251920108045`.

Thus no complete over-half return can occupy the final 23,135,982,578 odd-event lengths nearest
the full `2ell` traversal.

Classification: exact analytic inequality plus exact rational constant certificate in the inherited
high-carry scope.

## RL347.4 — matched H-carry potential quotient and contact/strict monotonicity

At matched rank `i` define

`h_i = V_v(i)/V_u(i) = Q_i/(2^(d_i) P_i)`

and the normalized H-carry defect

`e_i=Delta_i/2^(d_i)`, `Delta_i=2^(d_i)P_i-Q_i`.

Then exactly

`h_i = 1-e_i/P_i`.

After the unique RL324 crossing one has `e_i>0`. The genuine owned-prefix identity

`A_i = D0 P_i - X e_i > 0`

with `X=2^a`, `Y=3^ell`, `D0=X-Y`, `lambda=X/Y` yields

`0 < e_i/P_i < D0/X = 1-1/lambda`.

Therefore every matched rank after the crossing satisfies the exact corridor

`1/lambda < h_i < 1`.

For consecutive matched ranks, ordinary Collatz evolution gives

`h_(i+1) = (3 h_i P_i + 2^(-d_i))/(3P_i+1)`

and hence

`h_(i+1)-h_i = (2^(-d_i)-h_i)/(3P_i+1)`.

Inside the post-crossing corridor:
- if `d_i>0`, then `2^(-d_i)<=1/2<h_i`, so `h_(i+1)<h_i`;
- if `d_i=0`, then `1>h_i`, so `h_(i+1)>h_i`.

Thus strict matched ranks decrease the half-cycle quotient and contacts are exactly the local
mechanism that can increase it.

Classification: exact analytic genuine-physical quotient theorem.

## RL347.5 — half-cycle residual collapses to a narrow physical contact pair

Let a Phase-4 complete return have exactly `L=ell`.

Exact decorated rank equality forces its endpoints to be a matched contact (`d_i=0`), with equal
phase tag; hence the closing identity forces `H=a`.

For any phase-potential nondecreasing such return, the contact endpoints have the same q=0 phase
factor, so if the physical source and endpoint are `S,E`, then `E>S`.

The ordinary affine return equation is

`3^ell E = 2^a S - C`, `C>0`,

so

`E < lambda S`.

Both endpoints lie in the global q=0 band

`S,E < 2^76+2^36`

and `lambda-1<2^-40`. Therefore

`0<E-S<2^-40(2^76+2^36)=2^36+1/16`.

The endpoints are distinct odd integers, so their difference is a positive even integer. Hence

`2 <= E-S <= 2^36`, with `E-S` even.

Thus the exact `L=ell` Phase-4 residual is a decorated contact-to-contact pair with physical
separation at most `2^36`, rather than an unrestricted `ell`-event decoder replay.

Classification: exact analytic contraction.

## What RL347 does not prove

RL347 does not prove `O_75=empty`; Phase 4 remains OPEN.

In particular:
- the residual classes `75<=L<ell`, `L=ell`, and `ell<L<=251920108045` are not all eliminated;
- the bounded incoming signatures have not yet been intersected with the new H-carry/contact
  contractions in a complete all-class CRT/ownership proof;
- no new least-state escape certificate covers the residual classes;
- Phase 5 remains scratch-only and untouched.

## Successor discipline

Per direct user instruction, RL348 has exactly one mathematical goal: CLOSE PHASE 4 by proving
`O_75=empty`.

RL348 must not work on Phase 5, R1 post-Phase-4 consequences, Gate A, Gate B, or later roadmap stages.
If Phase 4 closes, RL348 must stop research and enter closeout; Phase 5 belongs to a later numbered
session.

`PARENT_DIFFICULTY_DELTA = EASIER`.
