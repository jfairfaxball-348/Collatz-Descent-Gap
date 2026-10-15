# RL337 proof ledger — affine profile collapse, suffix compression, and physical-identity frontier

Date: 2026-09-16
Status: CLOSED AND FROZEN
Incoming authoritative HEAD: `a456ff4d27624d015e06f92456b08b6665946e0e`
Successor: RL338

## Scope retained

Work remains only in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at `(a,ell)=(217976794617,137528045312)`. The inherited least-state floor `m>=2^71` remains externally conditional. RL336 remains authoritative for `z<=35`, `n<=32546278588`, the q=32 all-length theorem, the exact p<=4 physical exclusions, and the p=5/p=6 high-pair prefix obstructions. Gate A, Gate B, R1, `g=1`, and the global positive non-trivial-cycle theorem remain OPEN.

## RL337.1 — exact affine profile-collapse identity

Let `h=(h_1,...,h_L)` be a positive mechanical gap word. Let `Q_0=Q_L=0`, `Q_k>=0`, and define the profile-deformed gaps

`g_k = h_k + Q_k - Q_(k-1)`

whenever every `g_k>=1`. Then

`sum g_k = sum h_k =: H`.

For any positive gap word `w`, define the exact affine carry

`C(w)=sum_(k=1)^L 3^(k-1) 2^(sum_(i=k+1)^L w_i)`.

Since the suffix exponent for the deformed word is

`sum_(i=k+1)^L g_i = sum_(i=k+1)^L h_i - Q_k`,

one has

`C(g)=sum_(k=1)^L 3^(k-1) 2^(sum_(i=k+1)^L h_i-Q_k)`

and therefore

`C(h)-C(g)=sum_(k=1)^L 3^(k-1) 2^(sum_(i=k+1)^L h_i) (1-2^(-Q_k)) >= 0`.

The inequality is strict for every nonzero internal profile.

The corresponding exact state identity is

`3^L x_L = 2^H x_0 - C(w)`.

Hence, if the same terminal state `x_L` is held fixed,

`x_0(g)=x_0(h) - (C(h)-C(g))/2^H`.

Thus a positive profile gives a strictly SMALLER source than its zero-profile mechanical reference at fixed terminal state. This sign is load-bearing and corrects an earlier scratch statement made during RL337.

For concatenation,

`C(uv)=2^(H_v) C(u)+3^|u| C(v)`.

Consequently profile carry-drops concatenate with positive weights:

`DeltaC(uv)=2^(H_v) DeltaC(u)+3^|u| DeltaC(v)`.

Classification: exact analytic theorem; independently checked by the RL337 portable verifier.

## RL337.2 — relation to the inherited weighted telescope

The factor `1-2^(-Q_k)` shows that the affine carry-drop is the exact nonlinear version of the `2^(-q_t)` suppression already present in the RL326/RL327 telescope machinery. It is therefore not a second independent global mechanism.

The identity remains useful because it preserves the full profile heights rather than only the binary event `q_t>0`. However it does not by itself yield a physical descent theorem: the zero-profile reference generally belongs to a different exact congruence class and need not be an integral physical state. Any closure argument must therefore consume integrality, residue ownership, or exact shared physical identity.

Classification: exact interpretation of RL337.1 against inherited RL326/RL327 machinery; no new R1 closure claimed.

## RL337.3 — all-length right-suffix profile compression

For every admissible positive run `q_1,...,q_p`, the inherited profile grammar has

`q_p=1`, `q_i>=1`, `q_i<=q_(i+1)+1`.

Backward induction gives

`q_i <= p-i+1`.

Hence for every fixed suffix length `s`, the last `s` positive heights lie in a finite set depending only on `s`, not on the total positive-run length `p`. Since RL336 also gives right zero-run length at most 35, every arbitrarily long positive return admits a finite right-aligned suffix interface of fixed depth.

This is genuinely all-length and is the preferred compression device for a successor physical-identity attack. It is not itself an ownership or acyclicity theorem.

Classification: exact analytic all-length grammar corollary; checked exhaustively for `p<=8` in the portable verifier.

## RL337.4 — exact p=5 shared-state diagnostic

At the inherited high-carry ownership threshold `n>=20390252058`, exact reconstruction finds one physical p=5 realization for each of the pairs

`(24,27)`, `(24,28)`, `(24,29)`.

They are not three independent witnesses. They use the same physical source

`30437321051399780895133`,

the same state immediately after the five-positive run

`31208280367336569715567`,

and the same positive profile

`(2,1,2,1,1)`.

The reverse pairs `(27,24)`, `(28,24)`, `(29,24)` have zero physical realization under the same exact reconstruction and ownership filter.

This shows concretely that anonymous pair-level fallback edges can manufacture apparent bidirectional/cyclic structure that disappears once exact physical identity is retained. It does NOT prove that the full p=5, p=6, or arbitrary-p fallback layer is acyclic.

Classification: exact finite diagnostic, verified by the portable checker; strategically important but not a closure theorem.

## RL337.5 — corrected/demoted routes

1. Earlier scratch commentary incorrectly said that lowering the affine carry makes the fixed-terminal reverse source larger. The exact state identity above proves the opposite. No result depending on the incorrect sign is promoted.
2. A proposed mechanical-reference least-state margin/descent barrier is therefore demoted. Its orientation was tied to the incorrect fixed-terminal sign and it is not part of frozen mathematics.
3. Ordinary ordering of canonical residues does not follow the carry ordering; residue displacement can wrap modulo powers of three.
4. A full-cycle divisibility-by-`2^a-3^ell` idea was not promoted because the live `q_t` sequence is a linear least-root interval of length `ell-rho`, not automatically a cyclic full-row profile.
5. Exploratory 3-adic profile-decoding calculations and denominator ideas remain scratch diagnostics only.
6. RL336's q=33 diagnostic remains unpromoted.

## Sharp successor target

The strongest live clue is now physical identity, not another run-length census. RL338 should seek a support-uniform theorem for arbitrary positive-run returns that retains exact source/run-exit identity through a fixed-depth right suffix, exact residue lifting, or an equivalent quotient. The decisive question is whether the anonymous p>=5 fallback cycles have any genuine shared-state cycle at all. A proof of acyclicity, forced owned descent, or an exact state obstruction would close the ordered parent branch.

Do not use a p=7,p=8,... catalogue as the main route. Finite p=5/p=6 reconstruction is permitted only as a diagnostic or as a finite base case for an all-length suffix/identity theorem.

## Final status

R1 Parent Bridge: OPEN.
Gate A: OPEN.
Gate B: OPEN.
`g=1`: separate.
Global positive non-trivial-cycle exclusion: OPEN.

`PARENT_DIFFICULTY_DELTA = EASIER`.
