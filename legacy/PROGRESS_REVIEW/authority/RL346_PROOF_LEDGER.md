# RL346 proof ledger — cyclic signature contraction and deterministic inverse-carry decoder

Date: 2026-09-17
Status: CLOSED/FROZEN
Incoming BASE_HEAD: `11492738847ba59d0f32dcbb78eda40f2c0ad7bf`
Successor: RL347

## Scope

All results remain only in the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent branch with
`(a,ell)=(217976794617,137528045312)`, the genuine full two-row physical cycle, exact inherited
ownership/pruning, and the external conditional least-state floor `m>=2^71`.

R1 remains OPEN. Gate A, Gate B, later roadmap stages, `g=1`, and the global theorem remain open.
RL346 worked only on the long-return Phase-4 obstruction `O_75`.

## RL346.1 — exact 72-step terminal profile cone

Use the inherited RL344 endpoint-forward record notation

`B_r = a r - ell G_r`,

with exact endpoint phase tag `c`, and for a complete q=0 return

`q_(L-r) = 1 + floor((B_r-c)/ell)`

at every proper prefix `1<=r<L`.

For `r=72`, exact Euclidean division gives

`72 a = 114 ell + 16132046856`.

Hence

`q_(L-72) = 115-G_72` if `c<=16132046856`,
`q_(L-72) = 114-G_72` if `c>16132046856`.

For every Phase-4 return `L>=75`, depth 72 is proper, so `q_(L-72)>=1` and therefore
`G_72<=114`.

The inherited terminal-60 theorem excludes the all-one final-60 case, so a surviving 72-gap suffix
has `G_72>=73`. RL345 already eliminates every exact q=0-band endpoint in the low-modulus
`G_72=73,74,75` classes. Therefore every surviving long return satisfies

`76 <= G_72 <= 114`,

and equivalently

`1 <= q_(L-72) <= 39`.

In the branch `c>16132046856` the sharper upper bound is 38.

Classification: exact analytic all-length terminal-cone theorem, conditional only on the inherited
branch/band/floor and the promoted RL343/RL344/RL345 results.

## RL346.2 — bounded cyclic incoming signatures for every q=0 vertex

Every q=0 vertex of the closed q=0 return walk is the endpoint of the preceding complete return.
Thus the source state of one return may be described by bounded data from its predecessor rather
than by an arbitrarily tall prefix of the current return.

If the preceding return has length at least 75, retain only its final 72-gap word. By RL346.1 its
total gap lies in `76..114`. RL345.2 then gives at most one q=0-band endpoint for every fixed such
word, because the modulus `2^H` is at least `2^76`, larger than the whole q=0 band width.

If the preceding return has length `L<=74`, the exact closing inequality
`-ell < aL-ell H < ell` gives

`H in {floor(aL/ell), ceil(aL/ell)}`.

Hence `H<=ceil(74a/ell)=118`. For `48<=L<=74`, `H>=floor(48a/ell)=76`, so a fixed complete word again
has at most one q=0-band endpoint by the same modulus-width argument. The remaining `L<=47` class
is finite in both word length and endpoint lifts inside the bounded q=0 state interval.

Therefore every q=0 vertex has a bounded incoming signature independent of the length of the next
return:

- long predecessor: final 72 gaps with total gap `76..114`, plus exact decorated boundary data;
- short predecessor: complete word of length at most 74 and total gap at most 118, plus exact
decoration and a finite endpoint-lift index only where needed.

Classification: exact structural finite-signature reduction. It is not an enumeration certificate
and does not by itself close Phase 4.

## RL346.3 — decorated phase tags leave at most two return lengths

For a complete return the inherited endpoint/source phase tags satisfy

`B_L = c_end - c_source = aL-ell H`.

Therefore

`aL == c_end-c_source (mod ell)`.

Since `gcd(a,ell)=1`, the decorated tags determine one residue class for `L mod ell`. A complete
q=0-to-q=0 return lies within one traversal of the genuine two-row closed walk, so
`1<=L<=2ell`. Hence there are at most two possible lengths. For each surviving length,

`H = (aL-c_end+c_source)/ell`

is forced exactly.

Exact row identity, row contact and wrap orientation remain mandatory accept/reject tests; RL346
does not claim that decoration automatically accepts one of the two length representatives.

Classification: exact analytic length contraction.

## RL346.4 — deterministic inverse-carry word decoder

For any inherited inverse odd-gap word `g_1,...,g_L`, write `G_j=sum_(i<=j) g_i` and define

`C_0=0`,
`C_j=2^(g_j) C_(j-1)+3^(j-1)`.

Then the inverse recurrence gives

`3^j x_j = 2^(G_j) x_0 - C_j`.

For every `j>=1`, `C_j` is odd. Therefore for `j>=2`,

`v2(C_j-3^(j-1)) = g_j`,

and

`C_(j-1) = (C_j-3^(j-1))/2^(g_j)`.

Consequently, once the two physical endpoints, `L` and total gap `H` are fixed in the exact
inherited orientation, `C_L` is fixed and the gaps `g_L,...,g_2` are recovered uniquely backwards;
`g_1` is then forced by `sum g_i=H`. Invalid parity/divisibility or `g_1<1` rejects the candidate.

Thus fixed physical endpoints plus fixed `(L,H)` admit at most one complete inverse gap word.

Classification: exact analytic decoder/uniqueness theorem.

## RL346.5 — cyclic bounded-signature formulation of Phase 4

Combining RL346.2–RL346.4, a long Phase-4 return can be represented without an unbounded source
prefix catalogue:

1. a bounded incoming signature for the predecessor determines/candidates the source q=0 state;
2. a bounded incoming signature for the current return determines/candidates the endpoint q=0 state;
3. exact source/end phase tags leave at most two return lengths, with exact `H` for each;
4. the inverse-carry decoder leaves at most one complete middle word per surviving `(P,E,L,H)`.

The remaining Phase-4 obligations become accept/reject tests on this deterministic reconstruction:
predecessor and successor mixed-adic CRT, oddness, exact q-profile/record conditions, row contact,
wrap orientation, physical ownership/pruning, phase-potential sign, and deterministic least-state
descent.

This is a structural contraction of the arbitrary-middle problem. It is stronger as an organizing
interface than simply increasing suffix depth, but it does not yet prove `O_75=empty`.

## What is NOT proved

Phase 4 remains OPEN. RL346 does not provide an all-length skip/ranking theorem that certifies the
decoded middle without replaying up to `2ell` odd events, nor does it complete every inherited CRT,
ownership, row/wrap and descent test on the bounded cyclic-signature window.

RL344 Phase 5 remains scratch-only and was not resumed. Phase 6 remains conditional.

The attempted `G_72=76` scratch enumeration is explicitly NOT promoted; see the RL346 correction
ledger. No `G_72=77,78,...` ladder is authorized as the main successor route.

## Open obligation

R1 remains OPEN. RL347 should prove a genuine all-length skip/pumping/ranking theorem for the
deterministic decoder on the bounded cyclic-signature window, or freeze the first exact physical
signature on which such a theorem fails. It must not restart threshold enumeration.

The success criterion remains `O_75=empty`; only then may Phase 5 be resumed and R1 closure pursued
through the inherited RL343 closed-walk bridge.
