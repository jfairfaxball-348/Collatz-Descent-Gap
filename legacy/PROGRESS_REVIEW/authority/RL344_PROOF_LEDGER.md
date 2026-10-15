# RL344 proof ledger — methodological compression of O_75

Date: 2026-09-17
Status: CLOSED/FROZEN
Incoming BASE_HEAD: `6929776ecd7093b6673e235a9aa8ca25bd2dc67f`
Successor: RL345

## Scope

All work remains only in the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent branch with
`(a,ell)=(217976794617,137528045312)`, the genuine full two-row physical cycle, exact inherited ownership/pruning, and the external conditional least-state floor `m>=2^71`.

R1 remains OPEN. No result here closes Gate A, Gate B, later roadmap stages, or the global theorem.

## Phase 1 — CLOSED as a methodological stage

The return-profile description was converted from an enormous symbolic mechanical/profile grammar into an exact endpoint-forward record formulation.

For a q=0 endpoint `E`, let
`y_r=T^r(E)`,
`d_r=v2(3*y_(r-1)+1)`,
`G_r=sum_(i<=r) d_i`,
and `B_r=a*r-ell*G_r`.

For exact endpoint phase tag `c in {1,...,ell}`, the profile height `r` steps backward from the endpoint is

`q_(L-r)=1+floor((B_r-c)/ell)`.

Hence a complete q=0-to-q=0 return of exact length `L` exists at phase `c` iff

- `B_r>=c` for `1<=r<L`, and
- `c-ell<=B_L<c`.

Equivalently the admissible phase tags are exactly

`max(1,B_L+1) <= c <= min(ell,B_L+ell,min_(r<L) B_r)`.

Candidate return lengths are strict record lows of `B_r`. The source tag is `c_source=c-B_L`.

The phase-potential ratio is exactly

`V_endpoint/V_source = (E/P) * 2^(B_L/ell)`

for `P=T^L(E)`, so its sign is independent of which admissible phase lift is chosen.

Classification: exact analytic reduction. It subsumes the arbitrary mechanical/profile enumeration for a fixed physical endpoint trajectory.

## Phase 2 — CLOSED as a methodological stage

For a genuine last defect followed by a maximal terminal run of `t` unit physical gaps, write
`E=2^t k-1`. Exact parity at the preceding defect gives `v2(k)=1`, hence

`v2(E+1)=t+1`.

Writing `k=2j` with `j` odd,

`E=2^(t+1) j - 1`

and the preceding defect exponent satisfies

`d-1 = v2(3^(t+1) j - 1)`.

Thus the terminal tail is encoded exactly by the endpoint valuation, not by a free profile label. This is the endpoint-side affine/residue transducer boundary requested by the RL344 route.

Classification: exact analytic theorem.

## Phase 3 — CLOSED as a methodological stage, residual handed to Phase 4

The endpoint-only stage was exhausted rather than allowed to become an unbounded raw scan.

Inherited RL343 already excludes terminal runs of 60 or more unit gaps. RL344 scratch scans additionally explored exact endpoint cylinders for successively shorter terminal tails and found deterministic descent through the classes corresponding to `t=50`; however these extra scans did not receive a complete independent closeout red team and are therefore NOT PROMOTED.

The promoted outcome of Phase 3 is structural: endpoint cylinders are represented by the exact valuation law above, and unresolved endpoint-only classes must be passed to exact physical tightening rather than extended indefinitely by raw doubling scans.

Phase 3 is therefore closed in the prescribed workflow sense: the endpoint-only mechanism has been extracted, its limitation identified, and the residual passed forward. It is NOT claimed that Phase 3 alone eliminates every long return.

## Phase 4 — MAJOR ADVANCE, NOT CLOSED

For any phase-potential nondecreasing complete return of length `L`, source `P`, endpoint `E`, total gap `H`, and carry `C>0`,

`3^L E = 2^H P - C`.

The genuine full cycle has `L<=2ell`, both q=0 endpoints lie in
`[2^71,2^76+2^36)`, and the inherited bound is
`lambda=2^a/3^ell < 1+2^-40`.

Nondecrease gives

`lambda^(L/ell) * (1-C/(2^H P)) >= 1`.

Therefore, with `U=1+2^-40`,

`0 < P - 3^L E/2^H = C/2^H < P(1-U^-2)`

and the global q=0 upper band gives the exact uniform bound

`0 < P - 3^L E/2^H < 2^37`.

Moreover

`3^23 < 2^37 < 3^24`.

For any fixed first 24 inverse gaps, exact physical-prefix reconstruction fixes `P` modulo `3^24`. Hence once the exact endpoint `E`, length `L`, total gap `H`, decorated source/end row-phase tags, and first 24-gap source prefix are fixed, there is at most one phase-nondecreasing source `P`.

Combining this with RL343's fixed-75-suffix endpoint uniqueness, a fixed decorated two-ended interface

`(first 24 inverse gaps, last 75 inverse gaps, exact source/end decorated row-phase tags)`

has at most one physical middle-return lift. Predecessor/successor mixed-adic CRT constraints and row/contact ownership therefore become accept/reject tests on a singleton, not generators of a new middle-source progression.

This argument is full-two-row and wrap-safe because it uses the global RL343 q=0 band and exact decorated boundary tags. Early-row q=0 ownership still requires inherited row contact.

Classification: exact analytic Phase-4 singleton-interface theorem, independently checked by `verification/verify_rl344_fast.py` and `verification/red_team_rl344.py`.

Phase 4 remains OPEN because the finite boundary-signature set has not yet been fully intersected with predecessor/successor CRT, row/contact ownership, and deterministic least-state descent.

## Phase 5 — scratch only, performed early and frozen

Before the sequencing correction, RL344 explored short returns. Useful scratch was obtained:

- for a short return `L<ell`, total reverse gap is constrained to `floor(aL/ell)` or `ceil(aL/ell)`;
- exact Beatty-prefix inequalities give a small-state lattice-path quotient;
- lengths 48..74 inherit fixed-word endpoint uniqueness because their total gap is at least 76;
- additional exact counts and small-length word classifications were computed.

This work was performed out of the prescribed phase order and was not independently packaged/red-teamed for promotion. It is therefore frozen as NON-AUTHORITATIVE SCRATCH for RL345 to reuse only after Phase 4 closes.

## Open obligation

R1 remains OPEN. The next session must work methodically in sequence:

1. accept Phases 1–3 as closed methodological stages unless a contradiction is found;
2. finish Phase 4 completely;
3. only then promote/complete Phase 5 short returns;
4. use Phase 6 only if a genuine arbitrary-prefix residual remains after the record/singleton reductions;
5. close R1 only after every member of the exact owned phase-nondecreasing return obstruction `O_75` is impossible or descends below the conditional least state.

No defect-threshold ladder or raw symbolic-profile enumeration should be restarted.
