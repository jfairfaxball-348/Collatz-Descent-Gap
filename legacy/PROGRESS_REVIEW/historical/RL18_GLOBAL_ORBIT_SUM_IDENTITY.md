# RL18 global orbit-sum identity — an unbounded-radius invariant

## Purpose

The radius-3 programme by itself cannot close RL unless an RL object is forced to encounter radius 3.  This note extracts the local arithmetic into an identity valid for **arbitrary rotation distance and arbitrary prefix-flow support**.

It is the main strategic result of RL18 beyond repairing the radius-3 ledger.

## Setup

Let `d=(d_0,...,d_(A-1))` be a binary word of length `A` and weight `L`.  Put

`D=2^A-3^L>1`.

Let

`P_i=sum_{j<i} d_j`,

and define, modulo `D`,

`q_i=2^i 3^(-P_i)`.

Set

`Z=sum_{i=0}^{A-1} q_i`.

For the standard Collatz word polynomial `Q(d)`, direct telescoping gives

**`Q(d) = (3^L/4) Z (mod D)`.**

Since 3 and 4 are units modulo `D`,

**`D|Q(d)` iff `Z=0 (mod D)`.**

This recasts divisibility as a zero-sum problem for the prefix weights `q_i`.

## Rotation recurrence

Rotate left by `m`, and let

`p=P_m`.

Define the rotation multiplier

`rho=2^m 3^(-p) (mod D)`.

Let

`G_i=P_i(rot_m d)-P_i(d)`

be the prefix-flow difference.  Then, including the wraparound case,

**`q_(i+m mod A) = rho * 3^(-G_i) * q_i (mod D)`.**

No radius bound has been used.

## Decomposition into shift orbits

Let

`g=gcd(A,m)`, `h=A/g`.

The map `i -> i+m (mod A)` has `g` orbits of length `h`.  On an orbit starting at `i_0`, write

`i_k=i_0+km (mod A)`,

`S_k=sum_{j=0}^{k-1} G_(i_j)`.

Iterating the recurrence gives

`q_(i_k)=q_(i_0) rho^k 3^(-S_k)`.

Therefore that orbit contributes

**`Z_O = q_(i_0) * sum_{k=0}^{h-1} rho^k 3^(-S_k) (mod D)`.**

Summing the `g` orbit polynomials gives `Z` exactly.

After multiplying by a sufficiently large power of 3, each orbit contribution is an integer-coefficient Laurent/polynomial expression in `rho`, with exponent/coefficients determined entirely by the prefix-flow path `G`.

## Why radius 3 appears sparse

For a same-direction three-transposition flow, `G` has three isolated `-1` events and is otherwise 0.  The orbit polynomial telescopes into the familiar sparse trinomials.  The RL12 and cubic three-orbit P2 forms, and the one-orbit cubic sparse form, are therefore **specializations of this unbounded-radius identity**.

This matters strategically: instead of trying to prove that RL must have a short transposition edge, one may try to prove that the RL return path forces its general orbit polynomial to have a sign, norm, order, or resultant obstruction.

## Exact theorem status

The identities above are elementary algebraic consequences of the definitions.  `verify_rl18_global_orbit_identity.py` exhaustively checks them on a small domain:

- 1,623 word-level `Q <-> Z` checks;
- 121,854 pointwise shift-recurrence checks;
- 22,690 complete orbit-polynomial reconstructions.

The computation is a sanity check, not the proof.

## Missing bridge theorem

What is **not** yet proved is any statement of the form:

> the least-root/final-return grammar of a hypothetical primitive RL object forces the orbit polynomial above to be nonzero modulo `D`.

The next session should reconstruct the strongest actually-proved RL return/ownership constraints and substitute them into this identity.  It should try to derive a radius-independent obstruction before investing in larger finite radius scans.
