# RL342 proof ledger — canonical CRT recurrence and phase-potential reduction

Date: 2026-09-16
Status: CLOSED AND FROZEN
Incoming mathematical authority: `3b2bc6c56a4dae65c3c7210321c8ccec5b1b47ad`
Successor: RL343

## Scope

All statements remain only in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at

`(a,ell)=(217976794617,137528045312)`,

with inherited `z<=35`, q=0 physical source band `[2^71,2^76+2^36)`, exact ownership/pruning, RL337 affine/right-suffix compression, RL339 defect notation, RL341 exact physical overlap machinery, and the **external conditional least-state floor** `m>=2^71`.

R1, Gate A, Gate B, later `g=2` branches, `g=1`, and the global theorem remain OPEN.

RL342 did not promote any `sigma<=26` theorem.

## RL342.1 — exact mixed 2/3-adic carrier interface

Fix exact predecessor, middle, and successor return templates. The middle physical source lies in an exact residue class modulo a power of three and hence, after band truncation, in an arithmetic progression.

If the predecessor has `t` odd steps, total gap exponent `H`, and affine carry `C`, then requiring its run-exit to equal a proposed middle source `P` gives

`2^H X = 3^t P + C`.

Thus predecessor compatibility is exactly a congruence on `P` modulo `2^H`; requiring the reconstructed predecessor source `X` to be odd adds at most one further factor of two.

The middle run-exit is an exact affine rational function of `P`. Requiring that exit to lie in the successor's exact source residue class gives an exact congruence on the middle progression parameter modulo a power of three. After cancelling any common power of three in the affine coefficient, the surviving condition is either empty or one residue class modulo a power of three.

Because the predecessor and successor moduli are powers of two and three, respectively, every fixed predecessor/middle/successor compatibility problem is therefore either empty or an exact Chinese-remainder arithmetic progression, truncated only by the inherited physical band and exact ownership conditions.

This is the canonical physical recurrence-carrier interface sought in RL342: giant overlap row sets are finite unions of explicit CRT progressions, not anonymous label edges.

Classification: **exact analytic interface theorem**. It is a structural reformulation of the exact affine/congruence machinery and does not by itself prove global acyclicity.

## RL342.2 — phase-adjusted physical potential identity

For a mechanical factor with phase parameter `r`, write

`h_j = 1 + ceil((r+D j)/ell) - ceil((r+D(j-1))/ell)`,

where `D=a-ell`, and define the ceiling remainder

`u_j = ell*ceil((r+D j)/ell) - (r+D j)`.

Then exactly

`h_j ell - a = u_j-u_(j-1)`.

For a profile deformation `g_j=h_j+Q_j-Q_(j-1)`, define

`U_j=u_j+ell Q_j`.

Then

`g_j ell-a = U_j-U_(j-1)`.

For a physical odd inverse step

`x_j=(2^(g_j)x_(j-1)-1)/3`,

let

`delta=a ln 2-ell ln 3 > 0`

under the inherited `K<0` branch, and define

`V_j=x_j 2^(-U_j/ell)`.

Direct substitution gives the exact ratio

`V_j/V_(j-1) = exp(delta/ell) * (1-1/(2^(g_j)x_(j-1)))`.

Across `t` steps with total gap exponent `H` and affine carry `C`,

`V_t/V_0 = exp(t delta/ell) * (1-C/(2^H x_0))`.

Therefore, on any closed walk of **canonical decorated physical states** for which this `V` is single-valued at vertices, at least one carrier is phase-potential nondecreasing. A strict-decrease theorem for every carrier is stronger than necessary: R1 closure only needs elimination of the phase-nondecreasing carriers once the parent recurrence is represented by such a closed canonical interface.

Classification: **exact analytic identity and necessary closed-walk criterion**. The remaining parent-level bridge is to make the canonical decorated-state representation fixed-depth/all-length and prove all its nondecreasing carriers impossible or descending.

## RL342.3 — exact first new sigma=26 CRT-family escape certificate

The concrete chain

`(15,1) -> (1,16) -> (16,1)`

uses exact gap words

- predecessor `(15,1)`: `(1,2,1,2,2,1,2,1,2,1,2,2,1,2,2,1)`;
- middle `(1,16)`: `(3,1,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1)`;
- successor `(16,1)`: `(1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,3,1)`.

Its exact compatible middle-source family is

`P(k)=23912137200748175205995 + 77998046721343488*k`,

with

`0 <= k < 238329`,

and

`77998046721343488 = 2^26 * 3^19`.

For `k=0`, the predecessor source is `30676695662567844669575`; the middle run-exit is `42510466134663422588435`; and the successor reconstructs exactly. The middle run-exit is `(16P-5)/9`. The upper bound `k<238329` is sharp because the next progression member has middle run-exit at or above the inherited q=0 upper band.

The complete family is phase-potential nondecreasing: a rational atanh enclosure proves `delta>0`, and the rigorous inequality `ln(1-x)>=-x/(1-x)` at `x=5/(16P(0))` proves

`2 delta/ell + ln(1-5/(16P(0))) > 0`.

Since the correction decreases as `P` increases, every member of the family is nondecreasing for the middle return.

Nevertheless every one of the 238,329 exact physical family members reaches a state `<2^71` under deterministic accelerated odd Collatz iteration. The maximum escape depth is exactly 188 odd steps, attained first at `k=104356`.

Hence this entire genuine phase-nondecreasing recurrence family is excluded from the hypothetical least-state cycle.

Classification: **exact gap-free CRT-family escape certificate** under the inherited branch/band and external floor. It is not a complete `sigma<=26` certificate.

## Strategic consequence

RL342 replaces the broad conjecture

`every recurrence carrier descends`

by the smaller sufficient target

`every canonical phase-potential nondecreasing recurrence carrier is impossible or descends`.

RL337 already makes every fixed-depth right profile suffix finite independently of positive-run length. RL343 must combine that suffix compression with the mixed-adic CRT carrier interface and the phase-nondecreasing inequality to make the reduction all-length. If every resulting canonical suffix/CRT class is empty or descends below the floor, the ordered parent cycle is impossible and R1 closes.

No defect-threshold ladder is required by this architecture.

## Verification

Portable verifier: `verification/verify_rl342_fast.py` -> `RL342_FAST_GREEN`.

Independent red team: `verification/red_team_rl342.py` -> `RL342_RED_TEAM_GREEN`.

Both independently replay the 238,329-member family. The red team reconstructs every predecessor/middle/successor shared-state join and independently iterates every family source below the floor; the fast verifier also checks the exact CRT modulus, sharp band endpoint, representative identities, exact rational positivity of `delta`, the phase-nondecreasing inequality, and maximum escape depth 188.

## Status

R1 Parent Bridge: **OPEN**.

The smallest blocker is now a fixed-depth all-length theorem eliminating every phase-potential nondecreasing canonical CRT carrier, not another finite defect threshold.

`PARENT_DIFFICULTY_DELTA = EASIER`.
