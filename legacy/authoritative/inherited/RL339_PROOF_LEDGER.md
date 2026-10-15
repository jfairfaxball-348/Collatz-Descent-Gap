# RL339 proof ledger — singleton escape and 42-slack phase bound

Date: 2026-09-16. Status: CLOSED AND FROZEN. Incoming BASE_HEAD `1d21ed6023b9e129cfdf4f8450a8b956a58c6eab`. Successor RL340 is prepared, not started.

## Scope and dependencies

Every result here concerns only the ordered genuine `g=2`, `Z0>0`, `K<0` parent at `(a,ell)=(217976794617,137528045312)`, under the **external** least-state-floor assumption `m>=2^71`. The inherited q=0 source band is `[2^71,2^76+2^36)`. RL336 supplies `z<=35`, physical/mechanical reconstruction, and the band. RL337 supplies affine/suffix context. RL338 supplies the q=35 theorem `35(K-2H)-S<=43` and prior cap `n<=32546271999`. No R1 or global closure is claimed.

## RL339.1 Exact singleton escape certificate

The `RL339_EXACT_CERTIFICATE.md` enumerates every ordered adjacent zero pair with `1<=z,z'<=35` and `43<=z+z'<=70`, every admissible singleton mechanical template, and every odd residue lift of its reconstructed q=0 source in the inherited band. There is no high-carry ownership filter. All 119,764 candidate rows escape below `2^71` by deterministic forward odd Collatz iteration within 186 steps. Hence every live p=1 complete return has `z+z'<=42`. Classification: **exact finite certificate**, conditional on inherited band and external floor.

A separate exact scan covers every p=5..8 high-to-high pair with q=35 reduced charge `2z-8p>=0`; all 321 candidate rows escape in at most 39 steps. This excludes those nonnegative physical layers on the assumed cycle, including RL338's positive exceptions. Classification: **exact finite certificate** under the same scope. It is not needed for the new carry cap.

## RL339.2 Density theorem

Let `q_0,...,q_T` be the inherited genuine linear mechanical excess word, `q_0=0`, `T=ell-rho`; let `Z` count zeros and `K` positive positions, so `Z+K=T+1`. Each complete positive run of length `p` between zero runs `z,z'` satisfies `z+z'<=42p`: for p=1 by RL339.1; for p>=2 by `z,z'<=35` and `70<=42p`. The initial and final zero run each have length at most 35; a terminal positive tail only adds nonnegative slack. Summing yields `2Z<=42K+70`, so

`K>=Kbase(rho):=max(0,ceil((ell-rho+1-35)/22))`.

Classification: **analytic theorem** consuming RL339.1 and RL336.

## RL339.3 Zero-slack phase-pair theorem

For each complete return edge define `sigma=42p-z-z'>=0`; for a terminal positive tail define `sigma=42p-z` using a dummy zero target. Let `S42=sum sigma`. Every defect edge with `sigma>0` has `p<=sigma`: p=1 is integral; p>=2 follows `42p-70>=p`; the terminal tail satisfies `42p-z>=p`. Let `K0` count positive ranks on zero-slack edges and `B` count maximal zero-slack blocks. Thus `K0>=K-S42` and `B<=S42+1`.

A zero-slack edge necessarily has p=1 and `z+z'=42`: for p>=2, `42p>70`. Within each block the zero labels alternate `z,42-z,z,...`; the fixed case is `21,21,...`. A group of four consecutive zero-slack edges has a disjoint pair of low target anchors separated by exactly 44 physical ranks: choose its two low targets in the alternating case, or its first and third low targets in the 21 fixed case. If P counts these pairs, `4P>=K0-3B>=K-4S42-3`.

The step-44 phase is `alpha=(44a mod ell)/ell=101543836620/137528045312>1/2`. For any starting phase, the two inherited support weights sum to at least `1+2^(1-alpha)`. A rational atanh lower bound for `ln 2` and degree-six lower exponential polynomial prove `2^(1-alpha)-1>c=198849/1000000`. Every support rank has weight at least 1, and the P disjoint pairs add at least c. Therefore

`W_struct>=K+c*max(0,(K-4S42-3)/4)`.

Classification: **analytic all-length theorem** conditional on RL339.1 and inherited weighted-support framework. The finite edge cases, anchor grouping, and rational phase inequality are checked independently by the portable verifier and red team.

## RL339.4 Conditional carry cap

For fixed rho set `K=Kbase+h`, `h>=0`, and `s=44Kbase-2(ell-rho+1)+70` (for positive Kbase, `0<=s<=43`). The endpoint count gives `S42<=44h+s`. Intersect RL339.3 with the inherited arbitrary-support quartic residue envelope `W(Kbase)+h`. At rho=60, `Kbase=6251274783`, `s=16`, and the exact integer minimax is h=24,281,914. The inherited telescope RHS is in `(32537248343,32537248344)`.

For rho>=60 this RHS strictly decreases. If Kbase stays constant as rho increases, s increases by 2 and optimized gain drops by at most 2c; the newly omitted ideal term removes more than `1/(6 Lambda)`, exceeding the restored `2c/(12 Lambda)`. If Kbase drops one, s drops 42; at fixed h the structural positive-part argument rises by 167 and the residue weight step is at least 1, so optimized gain cannot fall. The newly omitted ideal term still exceeds `1/(6 Lambda)` while the restored residue step is less than `(22/21)/(12 Lambda)`, since `Kbase<ell/22` and the quartic step is less than 22/21. Here `Lambda=1+2^-40`. The inherited rho<=59 companion is below 17,179,869,185. The certified conditional cap is

`n<=32537248343`,

9,023,656 below RL338's cap. Classification: **exact rational conditional-branch consumer**. `verification/verify_rl339_fast.py` and `verification/red_team_rl339.py` check its endpoint and inequalities. The derivation of the inherited telescope and quartic envelope remains in the copied RL327/RL336/RL338 provenance and frozen sessions.

## Status and route barrier

R1 remains OPEN; the cap is still 12,146,996,285 above the fixed high-carry ownership threshold 20,390,252,058. At rho=60 even a hypothetical q=36 with the old boundary 43 would lower the direct consumer RHS only to 32,546,270,036.602..., so q=36 alone does not close R1. This is a **route barrier**, not a no-cycle theorem. The next attack must use exact physical identity across remaining negative-charge returns or find an absolute obstruction beyond the same linear telescope. Gate A, Gate B, `g=1`, R2 and later stages remain OPEN.
