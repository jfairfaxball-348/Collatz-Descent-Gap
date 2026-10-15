# RL343 proof-state ledger

Date: 2026-09-17. Scope throughout: inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent with `(a,ell)=(217976794617,137528045312)`, external least-state floor `m>=2^71`, and every inherited ownership qualification. R1 remains OPEN.

## Promoted analytic result: full physical two-row bridge

The complete proof is frozen in `sessions/RL343/full_cycle_canonical_bridge.md` and carried here by this ledger. For the genuine `2ell`-odd-step cycle rooted at its least state, the backward excess `q_t=G_t-ceil(at/ell)` is nonnegative at **every** rank, including both physical rows, and agrees at the two ends. Every physical `q=0` state lies in the inherited band `[2^71,2^76+2^36)`. The phase-adjusted potential is single-valued on the resulting closed decorated walk. The inherited high-carry `T>=3n-4` and owned `z<=35` rule out an all-zero profile. Therefore at least one complete physical return is phase-potential nondecreasing. This is an analytic bridge, **not** a contradiction: its forced return remains to be eliminated. `verification/verify_full_cycle_bridge.py` checks constants only; the written inequalities prove the result.

## Promoted exact finite certificate: terminal 60 unit gaps

For an inverse gap word ending in 60 unit gaps, `E+1=(2/3)^60(Y+1)` forces `2^60 | E+1`. In the global `q=0` band the exact endpoints are `E=2^60 k-1`, `2049<=k<=65536` (63,488). Every endpoint reaches an odd state below `2^71` under deterministic accelerated Collatz iteration. Maximum depth is 403 odd steps, first at `k=58658`; the ordered `k:depth` SHA-256 is `6b865b436278792435dc59fcf4f15975f9e4961f403af18a4cbd2ff12be616ad`. `verification/terminal_ones_60.py` and independent `verification/red_team_terminal_ones_60.py` replay the entire range. Consequently no cycle return of any prefix length can end in 60 or more consecutive unit inverse gaps. The floor qualification remains external.

## Promoted analytic boundary and finite grammar count

For a final inverse suffix `v=(g_1,...,g_75)` of total gap `H`, the carry identity is `3^75 E+C(v)=2^H Y`. Thus `E ≡ -3^{-75}C(v) (mod 2^H)`. A surviving suffix cannot have its final 60 gaps all one, so `H>=76`. The inherited band width is less than `2^76`; hence **each fixed final 75-gap word has at most one band endpoint**, regardless of prefix. This is endpoint uniqueness, not physical ownership or elimination.

The exact local positive-profile grammar has 76 mechanical factors and 456,795,521,589,204,615,537,376,070,040,576 symbolic profiles. Of these, 1,251,242,493,049,578 have the eliminated terminal 60-one tail, leaving 456,795,521,589,204,614,286,133,576,990,998 symbolic profiles. `verification/suffix75_boundary.py` checks the count by backward and forward recurrences. These are symbolic local profiles, **not** owned carriers, distinct endpoints, or surviving cycles. Raw profile listing is a route barrier.

## Promoted analytic paired-row localization

For matched late/early row rank `i` and inherited displacement `d_i=u_i-v_i>=0`, the full physical excess satisfies `q_v(i)=q_u(i)+d_i`. Thus an early-row `q=0` vertex requires a row contact `d_i=0` and late-row `q_u(i)=0`. At least `3n-4>=61,170,756,170` strict ranks in the live high-carry interval exclude their matched early-row ranks. The exact phase-potential identity is `V_u(i)-V_v(i)=2^{-(u_phase+ell q_u(i))/ell-d_i} Delta_i`, where `Delta_i=2^{d_i}P_i-Q_i`; its sign is exactly the inherited RL324 H-carry sign. This is an interpretation of that sign law, not a new crossing theorem. Full derivation: `sessions/RL343/matched_phase_pairing.md`; `verification/verify_matched_phase_pairing.py` checks indexing only.

## Open parent obligation

The global parent contradiction has **not** been proved. The exact residual set `O_75` is defined in `RL344_R1_RESIDUAL_CRT_RETURN_TARGET.md`. It contains all owned, phase-potential nondecreasing complete returns in the full physical closed `q=0` walk that do not descend below the least state. Its short class has length below 75. Its long class has a final 75-gap suffix with at least one gap above one among its final 60 positions, `H>=76`, the unique possible endpoint residue in the inherited band, and the full predecessor/return/successor mixed-adic CRT and ownership conditions. Proving `O_75` empty would close R1. Neither emptiness nor nonemptiness is claimed; later branches R2–R7 remain open.
