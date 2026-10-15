# RL341 proof ledger — physical recurrence, owned descent, and low-defect compression

Date: 2026-09-16
Status: CLOSED AND FROZEN
Incoming BASE_HEAD: `21804be4e55b67a4d31d896055336541a8e79293`
Successor: RL342

## Scope

All claims remain only in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at

`(a,ell)=(217976794617,137528045312)`,

with inherited `z<=35`, q=0 source band `[2^71,2^76+2^36)`, exact ownership/pruning, and the **external conditional least-state floor** `m>=2^71`. R1, Gate A, Gate B, `g=1`, later roadmap stages, and the global positive non-trivial-cycle theorem remain OPEN.

RL335 exact p=2/p=3/p=4 escape pruning, RL337 affine/suffix compression, RL338 q=35 bookkeeping, RL339 42-slack definitions, and RL340 exact physical-identity frontier are inherited.

## RL341.1 — exact physical identity destroys anonymous recurrence

RL341 retained exact source/run-exit identity rather than anonymous `(z,z',p)` labels. The total-42 singleton layer, which anonymously contains many complementary two-cycles, was reconstructed physically. Across all 29 ordered total-42 pairs with labels in `7..35`, the layer contains 244,174 q=0 physical rows but exactly one shared-state transition:

`(9,33) -> (33,9)`

through shared state

`10625929812242865646699`.

There is no return edge. Hence the total-42 physical transition layer is a DAG. This realizes the physical-identity mechanism anticipated in RL337/RL340.

Classification: exact finite physical-state theorem under the inherited band and external floor.

## RL341.2 — symbolic overlap-congruence solver

To avoid materializing huge row sets, RL341 rewrote consecutive singleton-return compatibility as exact arithmetic-progressions of shared physical states. The construction retains full mechanical singleton templates, exact source congruence modulo powers of three, odd parity, source-band bounds, exact affine source-to-run-exit maps, and exact predecessor/middle/successor shared-state identity.

The solver was calibrated against inherited exact data: with the parity filter restored it reproduces RL331's 14 total-44 physical links and the unique total-42 physical link above.

Classification: exact finite symbolic representation of physical joins; no anonymous edge substitution.

## RL341.3 — first genuine recurrence and forced descent

Using RL339's complete-return defect `sigma = 42p-z-z'`, RL341 found that the exact singleton overlap quotient is chain-free through `sigma<=14`. Genuine two-join chaining first appears at `sigma<=15`, initially in one middle row:

`(5,22) -> (22,13) -> (13,14)`

with middle source `16196285460332235269227`.

That middle state reaches below `2^71` after exactly 9 odd Collatz steps, so it cannot lie on the hypothetical least-state cycle.

As the defect threshold is raised, more algebraic recurrence carriers appear, but exact forward continuation removes every carrier found through `sigma<=25`.

Classification: exact owned-descent phenomenon; finite symbolic certificate through defect 25.

## RL341.4 — complete low-defect certificate through sigma<=25

For singleton returns with `1<=z,z'<=35`, the complete threshold scopes are:

| threshold | ordered interfaces | distinct mechanical singleton templates |
|---:|---:|---:|
| `sigma<=23` | 666 | 12,716 |
| `sigma<=24` | 683 | 12,905 |
| `sigma<=25` | 699 | 13,074 |

The new dense layers were compressed into exact progression families:

- new `sigma=24` layer: 139,018 carrier families representing 128,704,597 recurrence realizations; every family is covered by an exact 2-adic forward partition proving descent below `2^71`;
- new `sigma=25` layer: 203,812 carrier families representing 1,242,627,993 recurrence realizations; every family descends below `2^71`;
- maximum certified escape depth in the new layers: 305 odd steps.

RL335 exact p=2 pruning is load-bearing: a p=2 return with `sigma<=25` requires adjacent-zero total at least 59 and lies inside the exact p=2 layer already proved to escape. Higher p cannot contribute a live low-defect return in this range. Therefore every **live** complete return with `sigma<=25` is a singleton.

Hence, on the hypothetical cycle: **no three consecutive complete returns can all satisfy `sigma<=25`.**

Classification: exact finite symbolic/escape certificate under inherited scope and external floor.

## RL341.5 — all-length physical-defect theorem

Call a complete return low if `sigma<=25` and high if `sigma>=26`. By RL341.4, each maximal low block has length at most two.

For a surviving high complete return of positive-run length `p`, one has `26(p+2) <= 3 sigma`.

The sharp case is `p=1, sigma=26`. For `p=2,3,4`, RL335 exact pruning forces adjacent-zero total at most 43, giving minimum surviving defects 41, 83, and 125 respectively. For `p>=5`, `z+z'<=70` gives `sigma>=42p-70`, which is stronger than required.

Assign the at-most-two low singleton returns preceding each high return to that high return. Apart from at most two initial low returns,

`K_complete <= 2 + sum_high (p+2)`,

so `26 K_complete <= 52 + 3 S_complete`.

For a terminal positive tail, `sigma_tail=42p-z` with `z<=35`, hence `26 p <= 3 sigma_tail + 5`.

Therefore the full linear q-word satisfies

`26 K <= 3 S42 + 57`,

or equivalently `S42 >= (26K-57)/3`.

This is support-uniform and all-length. It is not another phase-weight or q-upgrade theorem; its input is exact physical nonrecurrence/least-state descent.

Classification: analytic all-length theorem consuming RL341.4 and inherited RL335/RL339 facts.

## RL341.6 — supporting coefficient ladder, not load-bearing

Before the defect formulation emerged, RL341 replayed and surpassed RL340's unpromoted physical-potential candidate through a sequence of exact-interface eliminations (`c=5,7,9,13,14,15,16,17`). This work supplied important diagnostics: many projected positive cycles vanish under fixed-depth q=0 prefix congruence; several whole left-interface families have no physical lift; and the total-42 anonymous cycle obstruction disappears under exact shared-state identity.

The coefficient ladder is frozen as supporting scratch/provenance, not promoted as a separate load-bearing theorem because RL341.4–RL341.5 subsume the strategic advance more cleanly.

## RL341.7 — incomplete sigma=26 diagnostic

The `sigma=26` symbolic family generation was completed far enough to identify 199,350 progression families representing approximately 7.54 billion recurrence realizations. The exhaustive forward 2-adic escape partition was **not completed before closeout**. No `sigma<=26` theorem and no 9-to-1 defect-density theorem is promoted.

This is the immediate finite diagnostic fallback for RL342, not the preferred main route.

## Verification

Portable closeout fast verifier: `verification/verify_rl341_fast.py`

Independent red team: `verification/red_team_rl341.py`

Closeout results: `RL341_FAST_GREEN`; `RL341_RED_TEAM_GREEN`.

The fast suite recomputes the threshold interface/template scopes, verifies the first recurrence carrier's 9-step escape, and checks every analytic boundary used in `26K<=3S42+57`. The full sigma=24/25 progression partition is a large exact certificate produced during the live session; it is summarized in `RL341_EXACT_CERTIFICATE.md` rather than expanded into its >1.3 billion represented realizations by the portable fast checker.

## Status

R1 Parent Bridge: **OPEN**.

The blocker has changed materially: anonymous fallback cycles are no longer the sharp frontier. The live question is whether the observed recurrence-carrier descent can be made **uniform in defect/interface depth**, or whether a first genuine non-descending exact physical carrier exists.

`PARENT_DIFFICULTY_DELTA = EASIER`.
