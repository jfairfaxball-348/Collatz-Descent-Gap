# RL346 exact analytic certificate

Date: 2026-09-17
Status: CLOSED/FROZEN SUPPORT FOR RL346_PROOF_LEDGER.md

This certificate contains only exact arithmetic/algebra used by the promoted RL346 results. It adds
no finite enumeration claim.

## Constants

`a = 217976794617`
`ell = 137528045312`
`gcd(a,ell)=1`
`2ell = 275056090624`

Exact division at the 72-step endpoint interface:

`72a = 15694329212424 = 114ell + 16132046856`.

Therefore, with inherited endpoint tag `1<=c<=ell`,

`q_(L-72)=1+floor(((114-G_72)ell + 16132046856-c)/ell)`

which is exactly

`115-G_72` for `c<=16132046856`,
`114-G_72` for `c>16132046856`.

For `L>=75`, this is a proper-prefix q-value and is at least 1. Hence `G_72<=114`. Combining the
inherited terminal-60 obstruction and RL345 elimination of totals 73, 74 and 75 gives the promoted
surviving cone `76<=G_72<=114`, hence `1<=q_(L-72)<=39`.

## Short-predecessor arithmetic

`floor(48a/ell)=76`, with remainder `10754697904`.

`ceil(74a/ell)=118`; equivalently
`74a = 117ell + 39501500154`.

Thus every complete return of length at most 74 has total gap at most 118, while every one of
length 48 through 74 has total gap at least 76 under the exact closing condition
`-ell < aL-ell H < ell`.

The inherited q=0 band is

`[2^71, 2^76+2^36)`.

Its width is

`73196680484548220289024`,

strictly less than

`2^76 = 75557863725914323419136`.

Hence a fixed exact residue modulo `2^H` with `H>=76` has at most one lift in the band.

## Length congruence

For exact decorated endpoint/source phase tags,

`aL-ell H = c_end-c_source`.

Reducing modulo `ell` gives

`aL == c_end-c_source (mod ell)`.

Because `gcd(a,ell)=1`, this fixes exactly one residue class of `L mod ell`. Intersecting with
`1<=L<=2ell` leaves at most two integer representatives.

## Inverse-carry decoder

Let

`C_0=0`,
`C_j=2^(g_j)C_(j-1)+3^(j-1)`.

Then `C_1=1`, and if `C_(j-1)` is odd, `2^(g_j)C_(j-1)` is even while `3^(j-1)` is odd, so `C_j`
is odd. Thus every `C_j`, `j>=1`, is odd.

For `j>=2`,

`C_j-3^(j-1)=2^(g_j)C_(j-1)`

with odd cofactor, so

`g_j=v2(C_j-3^(j-1))`.

This recovers `C_(j-1)` exactly and recursively. Once `C_L` and the total gap `H` are fixed, all
`g_L,...,g_2` are forced and

`g_1=H-sum_(j=2)^L g_j`.

Any failed divisibility/parity/positivity condition rejects the candidate; there can be at most one
valid complete inverse word.

## Verification boundary

No RL346 numerical search is promoted. The only finite computation inherited as load-bearing is
RL345's already-authoritative exceptional `G_72=73,74,75` certificate and its independent red team.
