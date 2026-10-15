# RL343 analytic candidate — paired q and phase potential across ordered rows

Status: LOCAL, NOT PROMOTED. Scope: the same full genuine `g=2` two-row physical cycle as `full_cycle_canonical_bridge.md`, with late row `u`, early row `v`, both of binary length `a` and odd weight `ell`, rankwise ordered one positions `u_i>=v_i`, and global least state at rank `k` in `u`.

Let `d_i=u_i-v_i>=0`. Let `P_i` be the physical odd state at the `i`-th one of `u`, `Q_i` the physical odd state at the matched one of `v`. The inherited RL325 matched defect is `Delta_i=2^d_i P_i-Q_i`.

## Exact profile pairing

Root the full two-row binary cycle at `u_k` and use the backward mechanical excess `q_t=G_t-ceil(a t/ell)` from the preceding bridge. Let `q_u(i)` and `q_v(i)` be its values at the matched rank-`i` odd states in the two rows.

If `i<=k`, the backward visit to `v_i` is `ell` odd ranks after the visit to `u_i`, and its cumulative halving distance is larger by `a+d_i`. The mechanical baseline rises by exactly `a`, so `q_v(i)=q_u(i)+d_i`.

If `i>k`, the backward visit to `u_i` is `ell` odd ranks after the visit to `v_i`, with cumulative halving distance larger by `a-d_i`. The same identity follows. Thus, at **every matched rank**, exactly

`q_v(i)=q_u(i)+d_i`.

Consequently an early-row q=0 state requires both `d_i=0` and `q_u(i)=0`. Every strict matched rank `d_i>0` is excluded from early-row q=0 ownership. In the inherited live high-carry interval, RL325.1 proves at least `3n-4>=61170756170` strict matched ranks, so at least that many matched early-row ranks cannot be q=0. This is a rank exclusion, not a count of distinct physical return carriers.

## Exact phase-potential pairing

The mechanical ceiling remainder has period `ell`, so matched ranks separated by `ell` odd events have equal remainder `u`. Since their q values differ by `d_i`, their phase-adjusted exponents differ by `ell*d_i`. Hence

`V_u(i)-V_v(i) = 2^(-(u+ell*q_u(i))/ell-d_i) * Delta_i`.

The positive factor makes the potential-order sign exactly the inherited matched-defect sign. RL324 proves `Delta_i<0` through the crossing rank `j` and `Delta_i>0` from `j+1` onward. Thus the paired potential order flips at that same rank. This is an interpretation of the existing physical H-carry crossing, not a second independent sign theorem or R1 closure.

## Consequence and boundary

The full closed q=0 return walk has early-row vertices only at row-contact ranks. Its other early-row ranks lie inside positive-excess excursions. This compresses the location of possible early-row return endpoints, while leaving the exact long excursions, contact endpoints, nondecreasing carrier class, and descent obligation open. Do not infer that all remaining nondecreasing carriers lie in the late row.

The index orientation was checked for all ordered pairs of small binary row words in `verify_matched_phase_pairing.py` (`RL343_MATCHED_PHASE_PAIRING_INDEX_GREEN`); the general equalities above are analytic.
