# RL345 proof ledger — 23/72 singleton-interface contraction

Date: 2026-09-17
Status: CLOSED/FROZEN
Incoming BASE_HEAD: `f10996208efb8cc437f0b364384054f3a55a3fb8`
Successor: RL346

## Scope

All results remain only in the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent branch with
`(a,ell)=(217976794617,137528045312)`, the genuine full two-row physical cycle, exact inherited
ownership/pruning, and the external conditional least-state floor `m>=2^71`.

R1 remains OPEN. No result here closes Gate A, Gate B, a later roadmap stage, or the global theorem.

RL344 Phases 1–3 remain accepted as closed methodological stages. RL345 worked only on Phase 4.
The frozen RL344 Phase-5 calculations remain scratch-only and were not resumed.

## RL345.1 — exact 23-gap source uniqueness

RL344 proved for every phase-potential nondecreasing complete return

`0 < P - 3^L E/2^H < 2^37`.

For any fixed first 23 inverse gaps, exact physical-prefix reconstruction fixes the odd source
`P` modulo `3^23`. Since every physical source is odd, the same prefix fixes `P` modulo
`2*3^23` by coprimality. Exactly

`2*3^22 < 2^37 < 2*3^23`.

Therefore, once `E,L,H` and the exact decorated source/end boundary data are fixed, a fixed
23-gap source prefix admits at most one phase-nondecreasing physical source. Depth 22 does not
give this uniform conclusion from the width bound.

Classification: exact analytic strengthening of the promoted RL344 source-localization theorem.

## RL345.2 — exact 72-gap endpoint uniqueness after finite exceptional escape

For a fixed final 72-gap word `v=(g_1,...,g_72)` of total gap `H`, let `C(v)` be its exact affine
carry. Then

`3^72 E + C(v) = 2^H Y`,

so `E` lies in one exact residue class modulo `2^H`.

The inherited RL343 terminal-60 theorem excludes any surviving suffix whose final 60 gaps are all
one. Hence a surviving 72-gap word has at least one excess gap unit in its final 60 positions and
therefore `H>=73`.

If `H>=76`, then the residue modulus is at least `2^76`, strictly larger than the entire inherited
q=0 band width

`(2^76+2^36)-2^71 < 2^76`.

Thus every fixed such 72-gap word has at most one band endpoint.

Only `H=73,74,75` require an exceptional finite check. Equivalently the all-one 72-word receives
respectively 1, 2, or 3 excess gap units, with at least one excess unit among the final 60
positions. The exact word counts are

- excess 1: 60 words;
- excess 2: 2,550 words;
- excess 3: 64,460 words;

for 67,070 exceptional words in total.

Enumerating every exact endpoint-residue lift in the inherited q=0 band gives

- excess 1: 460 endpoints;
- excess 2: 9,888 endpoints;
- excess 3: 125,008 endpoints;

for 135,356 exact band endpoints. Every endpoint reaches an odd state below `2^71` under
deterministic accelerated Collatz iteration. The maximum escape depth is exactly 446 odd steps,
uniquely for

`E = 32854878509085218570239`

with excess positions `(4,11,38)` in 1-based suffix coordinates.

The canonical ordered record is

`excess:comma-separated-1-based-excess-positions:endpoint:escape-depth`

and has SHA-256

`2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d`.

`verification/verify_rl345_fast.py` and `verification/red_team_rl345.py` independently reconstruct
the complete exceptional class and require these exact counts, maximum and digest.

Consequently every surviving fixed final 72-gap word has at most one viable q=0 band endpoint:
the low-modulus cases have none, while all `H>=76` cases have at most one by band width.

Classification: exact finite escape certificate plus analytic modulus argument, conditional on the
inherited band and the external floor.

## RL345.3 — contracted Phase-4 interface

Combining RL345.1 and RL345.2, the working Phase-4 boundary can be reduced from RL344's
24-source/75-endpoint depths to a 23-source/72-endpoint singleton interface.

Precisely: after fixing the final 72-gap suffix, first 23 inverse gaps, exact return length `L`,
total gap `H`, and the exact decorated source/end row-phase/boundary tags, there is at most one
phase-nondecreasing physical middle lift compatible with the band. The predecessor/successor
mixed-adic CRT and ownership conditions are therefore accept/reject tests on that singleton.

This remains full-two-row and wrap-safe only with the inherited exact decorated tags and row-contact
rules. No late-row-only simplification is made.

Classification: exact analytic consequence of RL345.1–RL345.2 and inherited RL342/RL343/RL344
interfaces.

## What is NOT proved

Phase 4 is NOT closed. RL345 did not complete the finite/compressed boundary-signature
intersection with predecessor CRT, successor CRT, physical ownership/pruning, row-contact/wrap
orientation, and least-state descent for every singleton 23/72 interface.

An overlap observation for return lengths `75<=L<=94` and a possible depth-71 endpoint extension
were considered only after the 23/72 theorem emerged. CLOSEOUT_LOCK was entered before either was
completed. Neither is promoted and neither is required by the frozen theorem.

Phase 5 remains scratch-only from RL344 and was not reopened. Phase 6 remains conditional.

## Open obligation

R1 remains OPEN. RL346 should finish Phase 4 from the verified 23/72 interface, not restart suffix
depth shaving, sigma-threshold enumeration, coefficient ladders, q-upgrades, or the old linear
consumer. If Phase 4 closes, proceed to the short-return Phase 5 in sequence. Phase 6 is used only
if a genuine arbitrary-middle residual remains.

The success criterion remains `O_75=empty` under the inherited parent assumptions.
