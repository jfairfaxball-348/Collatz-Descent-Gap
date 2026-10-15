# RL343 analytic candidate: full two-row canonical q=0 walk

Status: LOCAL, NOT PROMOTED. Scope: the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent with two physical rows of length `a=217976794617`, weight `ell=137528045312`, global least odd state `m`, external floor `m>=2^71`, inherited `m<2^75`, and `lambda=2^a/3^ell<1+2^-40`.

## Exact global nonnegative excess

Root the full physical cycle of `N=2ell` odd steps and total gap `2a` at `m`. Traverse it backward by accelerated odd inverse steps. Let `P_t` be the physical state after `t` inverse steps, `G_t` the cumulative gap, and `C_t>0` the inverse affine carry, so

`2^G_t m = 3^t P_t + C_t` for `1<=t<=N`, with `P_t>=m` and `P_0=P_N=m`.

Put `H_t=ceil(a t/ell)` and `q_t=G_t-H_t`. The inherited lambda bound gives `lambda^N<2`: indeed `N<2^39`, so `N/2^40<1/2`, and `log(lambda)<2^-40`, `exp(x)<=1/(1-x)<2` for `x<1/2`.

For every `1<=t<=N`, set `r_t=ell H_t-a t`, so `0<=r_t<ell`. Then

`(2^(H_t-1)/3^t)^ell = lambda^t/2^(ell-r_t) < 1`, because `ell-r_t>=1` and `lambda^t<=lambda^N<2`. Hence `2^(H_t-1)<3^t<2^G_t`, and integer `G_t>=H_t`. Thus **`q_t>=0` throughout the full two-row cycle**, with `q_0=q_N=0`.

This extends the inherited linear `q_0..q_(ell-rho)` profile to a genuine nonnegative cyclic profile of length `2ell`; no wrap of a single balanced row is asserted. It uses the actual physical two-row cycle rooted at its least state.

## The inherited q=0 band holds globally

For `0<=s<=ell`, let `A_s=2^(ceil(a s/ell))/3^s`. For `1<=s<ell`, coprimality gives `r=a s mod ell` in `1..ell-1`, and

`(A_s/2)^ell = lambda^s/2^r < 1` because `lambda^ell<2<=2^r`. Also `A_0=1` and `A_ell=lambda<2`. Therefore `A_s<2` for every `s` in `0..ell`.

For `t=b ell+s`, `b=0` or `1`, `0<=s<=ell`, one has `2^(H_t)/3^t=lambda^b A_s<2lambda`. At any `q_t=0`, the positive carry yields

`m<=P_t<2^(H_t)m/3^t<2lambda m<2^76+2^36`.

Thus **every** q=0 physical state on the full two-row cycle lies in the inherited band `[2^71,2^76+2^36)`. No wider second-row band is needed. The local 60-unit-suffix escape certificate and 75-gap endpoint uniqueness apply to q=0 endpoints in either row; any other inherited certificate still retains its own ownership and verifier conditions.

## Closed decorated walk

Write `D=a-ell`, `h_t=H_t-H_(t-1)=1+ceil(Dt/ell)-ceil(D(t-1)/ell)`, and `g_t=G_t-G_(t-1)=h_t+q_t-q_(t-1)`. Let `u_t=ell ceil(Dt/ell)-Dt` and `U_t^phase=u_t+ell q_t`. Then `u_0=u_N=0` and `q_0=q_N=0`. The RL342 potential `V_t=P_t 2^(-U_t^phase/ell)` is single-valued on rank-decorated physical states and satisfies `V_0=V_N=m`.

Partition the full cyclic profile at q=0 vertices, or group consecutive zeros with their following positive run as complete returns. Exact physical states join by construction, and the product of their potential ratios is 1. Consequently **at least one exact physical q=0-to-q=0 return is phase-potential nondecreasing**. In the inherited live high-carry branch, RL325.1 gives `T=k-j>=3n-4`, which is over 61 billion at the inherited high-carry threshold; the certified `z<=35` on that original owned linear interval therefore excludes an all-zero profile. Hence positive-return edges exist. This proves the abstract closed-walk arrow sought in the RL343 target for the full physical two-row cycle, subject to the exact inherited scope.

## Remaining boundary

This result does not eliminate the forced nondecreasing return. Its predecessor/middle/successor CRT class still has to be shown empty or descending with all ownership qualifiers. The closed walk is global across both physical rows; any local certificate used against its edge must cover that edge's exact physical/ownership scope. R1 remains OPEN.

Constant checker: `verify_full_cycle_bridge.py` -> `RL343_FULL_CYCLE_BRIDGE_CONSTANTS_GREEN`. The analytic proof above, not the checker alone, carries the full-cycle implication.
