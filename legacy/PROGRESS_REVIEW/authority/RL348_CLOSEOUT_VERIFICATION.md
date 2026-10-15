# RL348 closeout verification

Date: 2026-09-18
Status: CLOSEOUT CHECKS GREEN FOR PROMOTED RL348 CONTENT

Incoming `main` remained

`0eceb96a938c0ec0464f47624d0a24199b854d56`

through research and candidate construction before the final concurrency check.

Connector closeout uses committed flat Git-tree authority via one squash commit to `main`.
No RL348 ZIP/bundle is required.

## Candidate checks

The RL348 fast verifier checks:
- all fixed constants;
- `a-2ell=-57079296007`;
- terminal threshold `d=a-ell=80448749305`;
- the high-carry strict-rank value `3*n0-4=61170756170`;
- the exact post-crossing rational boundary
  `91143694380395855/3939478`;
- integer consequences
  `R>=23135982580`, `L<=251920108044`;
- the safe half-cycle synchronization depth 36.

Independent red team:
- reconstructs `15757912/22733865` from the first six positive `2*atanh(1/3)` terms;
- independently evaluates the post-crossing rational floor;
- checks the terminal `r=1` inequality directly;
- checks the mod-4 endpoint consequence;
- checks the 2-adic synchronization bound.

Expected outputs:

`RL348_FAST_GREEN`
`RL348_RED_TEAM_GREEN`

The written proofs, not the scripts alone, carry:
- the all-length terminal law;
- absence of early-row q=0 vertices in over-half complements;
- strict-late complement localization;
- the crossing split and its use of the genuine RL326 linear telescope.

## Corrections checked

The candidate explicitly does not promote:
- the scratch `S,E<2m` / `D<=2^36-2` strengthening;
- the 35-phase synchronization value;
- the false implication contact -> q=0 contact;
- `3n-3`;
- `R>=23135982581`;
- unfinished source-side residual inequalities.

No inherited theorem is demoted.

## Transport and catalogue

Transport: committed flat Git-tree authority.
Knowledge catalogues: stale/deferred and unchanged.

Post-commit readback must confirm:
- `sessions/RL348/` exists with this frozen closeout;
- `authoritative/START_HERE.md` names exactly RL349 and the aggressive target;
- portable verifier and red team are present under `authoritative/verification/`.
