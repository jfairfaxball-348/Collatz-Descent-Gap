# RL20 — frozen countermodel to the local-grammar-only radius-3 bridge

Date: 2026-08-20

## Status

**EXACT FINITE CERTIFICATE** for the precise bit-level implication stated below.

It is **not** a counterexample to RL and **not** a Collatz cycle: its standard word polynomial does not satisfy `D|Q`.

## 1. The implication being falsified

The RL17--RL19 roadmap asked whether the currently extracted least-root/final-return bit grammar alone could force one of the canonical endpoint rotations into cyclic adjacent-transposition radius at most 3.

The relevant local package is:

1. RL-L54: every proper suffix ending at the least-state rotation is subcritical, `2^m>3^E_m`;
2. the inherited external-floor consequence of RL-L54: every proper root prefix of length `m<=183` is supercritical, `3^P_m>2^m`;
3. the hard root branch `s=2` from RL-L27, so the full-parity beginning is `1101...` (`t_exit=1`);
4. an endpoint-compatible final return with `n_close=t_close=1`, giving the ending block `...10 | root` and satisfying the RL-L36 odd/high/exact-valuation conditions for a suitable root residue;
5. primitivity of the binary word.

The hoped-for bridge was that these consequences would force the root rotation, first post-neutral rotation, or final-anchor rotation to be within radius 3.

That implication is false.

## 2. Exact length-184 word

Let `alpha=log_3 2`.  Define prefix counts by

`P_0=0`,

`P_m=ceil(alpha m)` for `1<=m<=183`,

`P_184=116`,

and put `d_m=P_(m+1)-P_m`.

The resulting word is

`1101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011011010110110110101101101011011011010110110101101101101011011010110110101101101101011010`.

It has

`A=184`, `L=116`, `D=2^184-3^116>1`,

and is primitive.

## 3. Why the RL-L54 envelopes hold

For every `1<=m<=183`, construction gives

`P_m=ceil(alpha m)>alpha m`,

hence

`3^P_m>2^m`.

For a proper suffix of length `k`, its number of ones is

`E_k=116-P_(184-k)`.

Since `116<184 alpha` and `P_(184-k)>alpha(184-k)`,

`E_k < 116-alpha(184-k) < alpha k`.

Therefore

`2^k>3^E_k`

for every proper suffix.

So the word sits exactly at the first `m=184,p=116` rescue threshold identified in RL-L54 while satisfying all earlier prefix and all proper suffix slope inequalities.

## 4. Endpoint grammar

The word begins

`1101...`,

so it realizes the bit pattern associated with the hard `s=2,t_exit=1` root departure.

It ends

`...10`,

so the final odd anchor can be assigned `n_close=t_close=1`.

To show that these endpoint valuations are mutually residue-compatible with the inherited root constraints and external floor, the verifier freezes

`R# = 2361183241434822606907`,

which satisfies

`R# >= 2^71`,

`R# = 11 (mod 16)`,

`R# = 1 (mod 9)`.

Thus

`v2(R#+1)=2`,

`v2(3^2 ((R#+1)/4)-1)=1`,

`v3(2R#+1)=1`,

and the `n_close=t_close=1` final anchor is strictly above `R#` and satisfies `2^(n+t)>3^n`.

This `R#` is only an endpoint-residue witness.  It is **not** claimed that iterating the whole 184-bit word from this integer gives a cycle.

## 5. Exact rotation distances

Using zero-based left shifts, take the natural endpoint rotations

- `0`: least-state/root rotation;
- `3`: first post-neutral odd phase after the initial `110` block;
- `182`: final odd anchor beginning the terminal `10` block.

The exact cyclic adjacent-transposition distances are

`dist(0,3)=20`,

`dist(0,182)=48`,

`dist(3,182)=28`.

All are far above 3.

The verifier also checks the conservative endpoint neighborhood

`{0,1,2,3,181,182,183}`

and finds minimum pairwise distance `20`.

A stronger all-rotation audit checks all `184 choose 2 = 16,836` pairs of cyclic rotations and finds

`min_(a<b) dist(rot_a(w),rot_b(w)) = 4`,

with one minimizing pair at shifts `(0,19)`. Thus the local-grammar countermodel is globally radius-4 packed: **no pair of its rotations lies within the closed radius-3 regime**.

The distance calculation is exact.  For two equal-weight binary words `a,b`, let `S_i` be the cumulative difference through position `i`.  Cyclic edge flows have the form `f_i=c+S_i`; hence the minimum number of adjacent `01<->10` moves is

`min_(c in Z) sum_i |c+S_i|`,

attained at an integer median.  The verifier evaluates this formula.

## 6. It is not an RL object

For the standard Collatz parity-word polynomial `Q`, the verifier obtains

`Q mod D = 322171738410077807581692882247758374512983113782519312 != 0`.

Therefore `D` does not divide `Q`.

This is exactly why the certificate retires only the **local-grammar-only bounded-radius bridge**.  A stronger bridge that uses global `D|Q`, exact state ownership, the weighted-difference identity, or another genuinely global condition is not touched by this countermodel.

## 7. Strategic consequence

The route

> RL-L27 + RL-L36 + RL-L54 bit-level endpoint/slope consequences alone => a distinguished radius-3 pair

is formally false and should be removed from the roadmap. In fact the stronger conclusion `=> some radius-3 pair anywhere in the rotation orbit` also fails for this certificate, because its all-rotation minimum is exactly 4.

Radius 3 remains a valid closed local theorem, but any route from radius 3 to RL must add a global arithmetic/ownership hypothesis strong enough to reject this 184-bit model.

Verifier: `verify_rl20_bounded_bridge_countermodel.py`.
