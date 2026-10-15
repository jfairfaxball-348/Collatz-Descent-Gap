# RL342 exact CRT recurrence-family certificate

Date: 2026-09-16
Status: PROMOTED EXACT FINITE CERTIFICATE under the inherited ordered `g=2`, `Z0>0`, `K<0` assumptions and the external least-state-floor qualification `m>=2^71`.

## Certified chain

The chain of singleton interfaces is

`(15,1) -> (1,16) -> (16,1)`.

The exact gap words are

- `PRE=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,2,1)`;
- `MID=(3,1,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1)`;
- `SUC=(1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,3,1)`.

The compatible middle source is exactly

`P(k)=23912137200748175205995 + (2^26*3^19) k`

for

`0<=k<238329`.

The numerical step is `77998046721343488`.

For `k=0`:

- predecessor source: `30676695662567844669575`;
- middle source: `23912137200748175205995`;
- middle run-exit: `42510466134663422588435`;
- successor run-exit: `44181903199359184830227`.

For the middle word the run-exit after the first two gaps is exactly

`E(P)=(16P-5)/9`.

The final allowed `k=238328` has `E(P)<2^76+2^36`; the next progression member has `E(P)>=2^76+2^36`. Thus the family range is sharp for the inherited q=0 source band.

## Phase-potential classification

Let `delta=a ln2-ell ln3`. The inherited `K<0` branch gives `delta>0`; the verifier proves this with exact rational atanh intervals.

For the middle return, the phase-adjusted ratio is

`V_out/V_in = exp(2 delta/ell) * (1-5/(16P))`.

Using `ln(1-x)>=-x/(1-x)` and the exact lower bound for `delta`, the verifier proves the logarithm of this ratio is positive already at the least family member `P(0)`. Hence every member is phase-potential nondecreasing.

## Escape

Every one of the 238,329 family sources is iterated under

`F(x)=(3x+1)/2^{v_2(3x+1)}`.

Every source reaches a state `<2^71`. Maximum escape depth is exactly 188 odd steps, first attained at `k=104356`.

Therefore no member of this entire phase-nondecreasing CRT family can lie on the hypothetical cycle with least odd state at least `2^71`.

## Scope boundary

This certificate concerns exactly the displayed CRT family. It does **not** complete the full `sigma=26` recurrence layer, prove `sigma<=26`, or establish the all-length phase-nondecreasing-carrier theorem required to close R1.

Portable replay: `verification/verify_rl342_fast.py`.
Independent replay: `verification/red_team_rl342.py`.
