# RL347 closeout verification

Date: 2026-09-17
Status: CLOSEOUT CHECKS GREEN FOR PROMOTED RL347 CONTENT

Incoming `main` remained

`32354aa440ae1d54a32359c6d0a77aa2f1bdea1e`

through research and candidate construction before the final concurrency check.

Connector closeout used committed flat Git-tree transport. No RL347 ZIP/bundle is required.

## Candidate checks

The RL347 fast verifier checks:
- `gcd(a,ell)=1`;
- `a^(-1) mod ell=65470613321`;
- `2ell=275056090624`;
- inherited high-carry floor consequence `3*20390252058-4=61170756170`;
- the exact rational over-half boundary
  `91143694376456377/3939478`;
- corrected integer consequences
  `R>=23135982579`, `L<=251920108045`;
- the half-cycle band/separation arithmetic giving even difference at most `2^36`.

Independent red team:
- recomputes the modular inverse by extended Euclid;
- reconstructs `15757912/22733865` directly from the first six positive
  `2*atanh(1/3)` series terms;
- independently recomputes the over-half floor/ceiling boundary;
- independently checks the half-cycle integer separation consequence.

Expected outputs:

`RL347_FAST_GREEN`
`RL347_RED_TEAM_GREEN`

The written analytic proofs, not the scripts alone, carry:
- decorated rank uniqueness;
- strict-late over-half endpoint geometry;
- matched H-carry quotient corridor and local contact/strict monotonicity;
- the half-cycle contact interpretation.

## Corrections checked

The closeout candidate explicitly excludes:
- the invalid scratch claim `L=ell` is impossible;
- the inverse-orientation-mistaken right-endpoint skip estimate;
- the transient one-unit-too-strong over-half bound.

No inherited theorem is demoted.

## Transport and catalogue

Transport: committed flat Git-tree authority.
Knowledge catalogues: stale/deferred and unchanged.
