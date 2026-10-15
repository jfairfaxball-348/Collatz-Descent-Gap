# RL338 proof ledger — exact physical-core amortization and q=35 contraction

Date: 2026-09-16
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `6b1f64050acbf3464ecf7a973bc648e5be520f18`
Successor: RL339

## Scope retained

Work remains only in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at `(a,ell)=(217976794617,137528045312)`. The inherited least-state floor `m>=2^71` remains externally conditional. RL336 remains authoritative for the physical band, `z<=35`, the inherited owned-state architecture, q=32, and the exact p<=4 / prefix certificates. RL337 remains authoritative for affine profile collapse and all-length right-suffix compression. R1, Gate A, Gate B, `g=1`, and the global positive non-trivial-cycle theorem remain OPEN.

## RL338.1 — q=35 physical-core finite certificate

For the step potential `Phi(z)=0` on `z<=21` and `Phi(z)=35` on `z>=22`, a high-to-high p-positive return has reduced charge `2z-8p`. Complete exact reconstruction of every positive region gives:

- p=5: 196 pair labels, 64,120 admissible templates, 299 state-band candidates, 161 owned rows, all source labels 22..24, collapsing to 68 exact boundary cores;
- p=6: 154 pair labels, 130,386 templates, 10 candidates, 8 owned rows, all source label 25, collapsing to 4 boundary cores;
- p=7: 98 pair labels, 185,360 templates, zero state-band candidates;
- p=8: 42 pair labels, 204,590 templates, zero state-band candidates.

The boundary-core convention is defined precisely in `RL338_EXACT_CERTIFICATE.md`. The finite ranges are complete and gap-free.

Classification: exact finite physical certificate under inherited branch/state-floor assumptions.

## RL338.2 — exact successor recovery

The exceptional p=5 rows have right context at most 29; exceptional p=6 rows have right context at most 24. Across the resulting 125 distinct `(right-context, exact exit-state)` interfaces, every successor right label 1..35 and successor p=1..8 was reconstructed exactly.

There are 24 owned p<=4 continuations; every one has reduced q=35 charge <=-30. There are exactly five p=5..8 continuations; all are p=7, `22->1`, with charge -88. If no p<=8 successor exists, p>=9 gives charge <=-14 by the context bound. Thus every exceptional edge of charge at most +8 is immediately followed by charge at most -14, and every exceptional-successor pair has net charge <=-6.

Classification: exact finite shared-state certificate plus analytic tail bound.

## RL338.3 — all-length q=35 theorem

All surviving nonexceptional edges have reduced charge <=0. Pair every nonterminal exceptional edge with its immediate successor. Only a terminal exceptional edge can remain unmatched, contributing at most +8. Since the step potential has range 35,

`35(K-2H)-S <= 43`,

hence

`2H >= K - S/35 - 43/35`.

This is support-uniform in positive-run length: p=5..8 are the only possible positive baselines, and p>=9 is discharged analytically. It replaces the anonymous fallback-cycle obstruction by an exact physical-state amortization theorem.

Classification: exact finite-state/physical certificate plus analytic all-length theorem.

## RL338.4 — phase consumer and carry cap

The q=35 theorem supplies

`W_struct >= K + C*(K/2 - (71/70)S - 113/70)`,

with inherited `C=25120009946627/10^14`.

Exact rational verification gives:

- finite rho 60..2894 maximum at rho=60, `K=6112357564`, endpoint slack 3, optimal `h=59311669`, RHS `32546271992.519188...`;
- uniform bridge through rho=21,999,999: `h=59303536`, endpoint RHS `32546271999.09747...`;
- inherited ordinary Q256 handoff at rho=22,000,000 remains below the bootstrap;
- rho<=59 companion bound remains below the bootstrap.

Therefore the self-consistent conditional carry cap is

`n <= 32546271999`.

This improves the incoming authoritative cap `32546278588` by 6,589.

Classification: exact rational conditional-branch consumer.

## Intermediate q=33/q=34 work

q=33 and q=34 were useful scratch stepping stones during RL338. They are not needed as separate load-bearing promoted theorems because RL338.3 directly proves the stronger q=35 statement from exact physical reconstruction and inherited dependencies. Their scratch conclusions are therefore subsumed, not independently promoted.

## Open obligation

R1 remains open. RL338 achieved its unique target—a support-uniform exact physical-state quotient/amortization theorem—but the q=35 anchor and new cap have not yet been converted into contradiction, owned descent, or another parent-level closure theorem.

The successor should attack the smallest direct R1 closure theorem using q=35 and `n<=32546271999`. q=36 is subordinate and should be pursued only if a direct closure calculation shows that one additional charge unit is genuinely the minimal missing ingredient.

`PARENT_DIFFICULTY_DELTA = EASIER`.
