# RL345 exact certificate — 72-gap exceptional endpoint escape

Date: 2026-09-17
Status: PROMOTED EXACT FINITE CERTIFICATE WITH INDEPENDENT RED TEAM

Scope: inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent, full q=0 band
`[2^71,2^76+2^36)`, and external conditional least-state floor `m>=2^71`.

For a fixed final 72-gap word, endpoint ambiguity can occur only when its total gap is below 76.
The inherited terminal-60 exclusion forces at least one excess gap unit in the final 60 positions,
so the exceptional total gaps are exactly 73, 74, 75.

Complete exceptional scopes:

| excess above 72 | suffix words | exact q=0-band endpoints |
|---:|---:|---:|
| 1 | 60 | 460 |
| 2 | 2,550 | 9,888 |
| 3 | 64,460 | 125,008 |
| total | 67,070 | 135,356 |

Every one of the 135,356 endpoints descends below `2^71` under deterministic accelerated odd
Collatz iteration.

Maximum escape depth: 446 odd steps.

Unique maximizer:
- endpoint: `32854878509085218570239`
- 1-based excess positions in the 72-gap suffix: `(4,11,38)`.

Canonical record format, in increasing excess and lexicographic excess-position order and then
increasing endpoint lift:

`excess:comma-separated-1-based-excess-positions:endpoint:escape-depth`

SHA-256:

`2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d`

Verification:
- `verification/verify_rl345_fast.py` uses sparse multiset enumeration, affine carry recurrence,
  exact endpoint residues, and low-bit accelerated iteration.
- `verification/red_team_rl345.py` independently uses explicit nested sparse generators, the closed
  carry sum, direct divisibility checks, and a separate trailing-two valuation loop.

Both reconstruct the whole claimed range; there is no sampling and no uncovered exceptional word
or endpoint.
