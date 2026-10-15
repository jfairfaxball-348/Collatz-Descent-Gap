# RL341 exact physical recurrence/descent certificate

Date: 2026-09-16
Status: PROMOTED EXACT FINITE CERTIFICATE under inherited ordered `g=2`, `Z0>0`, `K<0` assumptions and the external least-state-floor qualification `m>=2^71`.

## Domain

Use `a=217976794617`, `ell=137528045312`, `D=a-ell`, zero labels `1<=z,z'<=35`, q=0 source band `2^71 <= P < 2^76+2^36`, and RL339 defect `sigma=42p-z-z'` for complete returns.

For a singleton pair `(left,right)`, enumerate every rational-mechanical factor of length `left+right`, retain factors whose positive insertion site has base gap 2, and deform `g[left-1] += 1`, `g[left] -= 1`.

The source congruence is solved exactly modulo `3^L`; odd parity and the q=0 source band are imposed exactly. The run-exit after `left+1` gaps is an affine function of the source. Consecutive-return compatibility is therefore an exact intersection of arithmetic progressions of physical states.

## Calibration

The overlap solver reproduces inherited total-44 physical-link count 14; total-42 physical layer 244,174 physical rows; exactly one total-42 shared-state transition `(9,33)->(33,9)` with shared state `10625929812242865646699`; and no reverse transition.

## First recurrence carrier

No exact row is both predecessor-capable and successor-capable through `sigma<=14`.

At `sigma<=15`, the first such chain is `(5,22) -> (22,13) -> (13,14)` with middle state `16196285460332235269227`. Deterministic accelerated odd Collatz iteration reaches below `2^71` after 9 odd steps.

## Complete certified threshold through sigma<=25

| threshold | interfaces | templates |
|---:|---:|---:|
| 23 | 666 | 12,716 |
| 24 | 683 | 12,905 |
| 25 | 699 | 13,074 |

Dense new layers are represented losslessly by progression families rather than enumerated pointwise:

| new layer | progression families | represented recurrence realizations | non-descending families | max certified escape |
|---:|---:|---:|---:|---:|
| `sigma=24` | 139,018 | 128,704,597 | 0 | <=305 |
| `sigma=25` | 203,812 | 1,242,627,993 | 0 | <=305 |

For each progression family, exact 2-adic partitioning of the accelerated odd Collatz map proves that every band member reaches a state `<2^71`. No sampling or probabilistic step is used.

RL335 eliminates the only possible live p=2 contamination of this defect range; p>=3 cannot contribute a live `sigma<=25` return. Therefore the certificate proves: on the hypothesized cycle, no three consecutive complete returns all have `sigma<=25`.

## Unpromoted next layer

At `sigma=26`, family generation produced 199,350 exact progression families representing approximately 7.54 billion recurrence realizations. The full escape partition was not completed. This layer is frozen **UNPROMOTED**.

## Portable verification

`verification/verify_rl341_fast.py` recomputes the gap-free threshold interface/template scope and the analytic corollary boundary cases. `verification/red_team_rl341.py` independently attacks the sharp separator and terminal endpoint inequalities and checks the first recurrence carrier's escape.

The very large sigma=24/25 family expansion is not replayed pointwise by the fast suite; its exact symbolic certificate summary is the promoted finite object.
