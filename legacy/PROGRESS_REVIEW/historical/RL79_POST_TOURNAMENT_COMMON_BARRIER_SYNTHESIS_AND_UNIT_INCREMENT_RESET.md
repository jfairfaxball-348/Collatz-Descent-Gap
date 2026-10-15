# RL79 — Post-tournament common-barrier synthesis and unit-increment reset

Date: 2026-08-24

## 0. Executive outcome

RL79 executed the requested post-tournament route reset against the frozen RL78 state and the inherited RL72/RL75 route maps.

The incoming RL78 outer sidecar, fresh internal manifest, and fast verifier suite pass. Under the verification-economy rule, the frozen RL78 ledger is accepted without recursively rerunning historical expensive certificates.

RL79 does **not** close Gate A, Gate B, RL/nontrivial-cycle exclusion, or the Collatz conjecture. It does produce a stronger common-barrier theorem that explains why a broad class of apparently different word/phase/invariant routes keep surviving fake models.

The central new result is:

> **Canonical generalized-increment cycle theorem.** Every primitive binary word `w` with `D=2^A-3^L>0` canonically determines a positive primitive integer cycle of a generalized shortcut map
>
> `T_s(n)=n/2` for even `n`, and `T_s(n)=(3n+s)/2` for odd `n`,
>
> where
>
> `s=D/gcd(D,Q(w))`.
>
> The parity word of that integer cycle is exactly `w`, every state is coprime to `s`, and genuine full-`D` Collatz ownership is exactly the exceptional case `s=1`.

Thus the RL20 fake is not an isolated pathology. It is one instance of a universal mechanism: essentially every primitive above-resonance word has a positive integer realization for *some* odd increment `s`. Any theorem that is unchanged when the odd-step increment `1` is replaced by a variable odd `s`, or that becomes homogeneous after normalizing states by `s`, cannot be the missing ownership bridge.

RL79 then seriously tests four theorem architectures:

1. nonlinear cross-rotation minors/products modulo `D`;
2. prime/order structure of the full denominator;
3. global integer-permutation / Vandermonde spacing;
4. global moment identities of all cycle states.

The first two collapse analytically. The most attractive scale-free 2-adic part of the Vandermonde route collapses to a pure cyclic-word longest-common-prefix identity. The moment hierarchy is exactly homogeneous in `(states,s)` and therefore denominator-blind after normalization. The surviving requirement is sharper than before:

# A successful next theorem must consume the absolute fact `s=1` in a non-homogeneous, non-asymptotically-erasable way.

This is a new **unit-increment / denominator-content barrier**. It is not merely the RL76–RL78 physical-scale barrier, although it explains why scale-normalized algebra repeatedly loses ownership information.

Because RL79 is mainly a route-elimination/common-barrier result, the requested RL80 pivot to the **infinite proved-blue dyadic funnel / certified basin** is strongly justified. Basin membership is genuinely special to the ordinary `s=1` Collatz map and is not preserved by the generalized `T_s` fake mechanism.

---

## 1. Frozen incoming state and route-map baseline

Retain the authoritative RL78 proof-state ledger:

- primitive/full-`D` radius-3 local obstruction: **closed**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

RL72's audit identified the missing ingredient as an ownership-sensitive global coupling rather than another local q-digit. RL75's tournament ranked, in order, owned-macro periodicity/packing, product/growth/CF + full phase, `D|Q`-sensitive bounded-radius Gate B, and two-scale Diophantine incompatibility. RL76–RL78 then seriously exercised the first three and exposed the common free-scale, coordinate-change, and ownership-defect barriers.

RL79 therefore does not resume the old ladder. It asks what information is *structurally absent* from those architectures.

---

## 2. Notation

Let `w=d_0...d_(A-1)` be a binary word of length `A` and weight `L`.

Use the standard word numerator

`Q(w)=sum_(d_i=1) 2^i 3^(number of later 1s)`

and

`D=2^A-3^L`.

For the left rotation `w_m=rot_m(w)`, write

`Q_m=Q(w_m)`.

For positive-cycle/RL geometry the relevant case is `D>0`.

RL78 proved the exact rotation transport

`2^m Q_m - 3^(P_m) Q_0 = D Q(prefix_m)`,

and therefore

`gcd(D,Q_m)=gcd(D,Q_0)`

for every rotation.

Put

`g=gcd(D,Q_0)`,

`s=D/g`.

RL78 called `s` the common reduced denominator / ownership-defect denominator. Full integer ownership is exactly `s=1`.

---

## 3. New theorem A — canonical generalized-increment cycle

### Theorem A

Let `w` be a binary word with `D>0`. Define `Q_m`, `g`, `s` as above and

`n_m=Q_m/g`.

Then for every `m` (cyclically),

`boxed: 2 n_(m+1) = n_m` if `d_m=0`,

and

`boxed: 2 n_(m+1) = 3 n_m + s` if `d_m=1`.             (3.1)

Moreover:

1. every `n_m` is a positive integer;
2. `n_m` is even iff `d_m=0`, and odd iff `d_m=1`;
3. `gcd(n_m,s)=1` for every `m`;
4. if `w` is primitive, the `n_m` are pairwise distinct and form a primitive positive integer cycle of

   `T_s(n)=n/2` for even `n`,

   `T_s(n)=(3n+s)/2` for odd `n`.

Classification: **new analytic theorem**.

### Proof

Apply RL78 rotation transport with `m=1`. The one-letter prefix has `Q(0)=0`, `Q(1)=1`, hence

`2Q_(m+1)-3^(d_m)Q_m=d_m D`.

Divide by `g` to obtain (3.1).

Because `D>0` and every rotated word numerator is positive, all `n_m>0`.

`D` and therefore `s` are odd. If `d_m=0`, (3.1) gives `n_m=2n_(m+1)`, so `n_m` is even. If `d_m=1`, `3n_m+s` is even, and odd `s` forces `n_m` odd.

RL78 gcd invariance gives `gcd(D,Q_m)=g`; dividing by `g` yields `gcd(s,n_m)=1`.

Finally, `T_s` is deterministic from integer parity. If a primitive word had `n_i=n_j` for `0<=i<j<A`, the forward integer orbit and its parity sequence would repeat with a smaller period, forcing `w` to be periodic. Hence a primitive word gives distinct states.

### Consequence A1 — every primitive above-resonance word has a positive integer generalized cycle

This is the main conceptual reset.

The existence of a positive primitive integer cycle with a prescribed primitive parity word is **not** restrictive once the odd increment is allowed to be `s` rather than fixed to `1`.

The genuine Collatz condition is precisely

`boxed: s=1`.                                            (3.2)

The RL20 radius-4 fake has `g=1`, hence `s=D`, and is therefore a perfectly legitimate primitive positive integer `T_D` cycle even though it is not an ordinary Collatz cycle.

---

## 4. New synthesis B — the unit-increment / homogeneity barrier

The generalized maps satisfy the exact odd-scaling covariance

`T_(c s)(c n)=c T_s(n)`

for every positive odd integer `c`.

Equivalently, if `x=n/s`, then every canonical `T_s` orbit satisfies the ordinary rational affine recurrence

`2x_(m+1)=x_m` for `d_m=0`,

`2x_(m+1)=3x_m+1` for `d_m=1`.

Thus

`x_m=n_m/s=Q_m/D`.

The ownership defect has been moved entirely into the denominator `s`.

### Barrier statement

Any proposed invariant that is homogeneous under simultaneous scaling

`(n_m,s) -> (c n_m,c s)`,

or which is expressed only in the normalized rational phases `x_m=n_m/s`, is **incapable of distinguishing `s=1` from `s>1`**.

It can still be a true identity or useful inequality, but it is not by itself an ownership theorem.

Classification: **analytic synthesis / common method barrier**.

This adds a fourth post-tournament barrier to the inherited three:

1. coboundary / unit transport;
2. free physical scale/context;
3. local-grammar fake compatibility;
4. **unit-increment homogeneity:** after canonical reduction, the argument never uses that the additive odd-step increment is exactly `1`.

A successful route must break this scaling symmetry by a genuinely non-homogeneous integer-lattice, basin-membership, exact-content, or other `s=1`-specific fact.

---

## 5. Candidate architecture 1 — nonlinear cross-rotation invariants

RL79 tested the RL79-target suggestion that quadratic/higher minors or products of rotation numerators might survive RL78's linear unit-transport barrier.

### New theorem C — polynomial rotation-algebra collapse modulo `D`

Work in `R=Z/DZ`. Since `D` is odd, `2` is a unit. RL78 transport gives

`Q_m == u_m Q_0 (mod D)`,

where

`u_m=3^(P_m) 2^(-m) in R^*`.                            (5.1)

Therefore for **every** polynomial

`F(X_0,...,X_(A-1)) in R[X_0,...,X_(A-1)]`,

`boxed: F(Q_0,...,Q_(A-1)) = F(u_0 T,...,u_(A-1)T)|_(T=Q_0) (mod D).`   (5.2)

In particular, if `F` is homogeneous of degree `r`,

`boxed: F(Q_0,...,Q_(A-1)) == Q_0^r F(u_0,...,u_(A-1)) (mod D).`       (5.3)

Classification: **new analytic method barrier**.

### Consequence

At modulus `D`, the entire cross-rotation numerator algebra is rank one: all rotation numerators lie on a single unit line generated by `Q_0`.

Hence a quadratic determinant/minor/product candidate has only two possibilities:

- its coefficient `F(u_0,...,u_(A-1))` vanishes, in which case it is an all-word transport identity and passes the RL20 fake automatically;
- or it does not vanish, in which case setting the expression to zero under genuine ownership is only a reformulation/consequence of `Q_0==0 (mod D)` and supplies no second independent ownership condition.

This does **not** rule out quotient-sensitive constructions modulo `D^2`, expressions after division by `D`, or invariants using additional non-rotation data. It does rule out the most natural nonlinear extension of RL78's normalized-rotation idea at the same modulus.

**Route classification:** **dead at modulus `D`**.

---

## 6. Candidate architecture 2 — prime/order structure of the denominator

The RL79 target proposed factoring `D` prime-by-prime and seeking incompatible multiplicative orders.

### New theorem D — owned full-word monodromy is the identity modulo `D`

The full affine word map is

`F_w(x)=(3^L x+Q_0)/2^A`.

Therefore

`boxed: 2^A(F_w(x)-x)=Q_0-Dx.`                           (6.1)

If `D|Q_0`, write `Q_0=DR`. Then

`boxed: F_w(x)-x = D(R-x)/2^A.`                          (6.2)

Consequently, for every divisor `M|D`,

`boxed: F_w(x)==x (mod M) for every integer x.`          (6.3)

In particular, at every prime power `p^e|D`, genuine ownership makes the full-word monodromy maximally degenerate: multiplier `1`, translation `0`.

Classification: **new analytic method barrier**.

### Consequence

A prime/order route based only on the multiplicative order or affine order of the **full return map** modulo factors of `D` cannot contradict ownership: ownership makes that return map the identity.

A viable denominator-prime route must instead use genuinely finer data, such as sparse prefix sums, a nontrivial additive zero-sum obstruction, or a coupling to ordering/positivity that is not already encoded by the full monodromy.

The reduced generalized map has the same issue. Its full map is

`F_(w,s)(n)=(3^L n+sQ_0)/2^A`,

and because `s|D`,

`F_(w,s)(n)==n (mod s)`

for every `n`. Thus prime/order analysis modulo the ownership-defect denominator `s` alone is also structurally degenerate.

**Route classification:** **pure full-monodromy prime/order route dead; prefix/additive refinements remain untested but require a new consumer.**

---

## 7. Candidate architecture 3 — global integer permutation / Vandermonde spacing

This was the strongest genuinely different construction found in RL79 before red-teaming.

Let `X` be a primitive positive `T_s` cycle, partitioned into the even-input states `E` and odd-input states `O`. Put

`e=|E|=A-L`, `o=|O|=L`.

### New theorem E — cross-parity Vandermonde product identity

Because `T_s` permutes the distinct cycle states, the Vandermonde product is preserved up to sign. Pairwise differences transform as:

- even/even: `(e_1-e_2)/2`;
- odd/odd: `3(o_1-o_2)/2`;
- even/odd: `(e-3o-s)/2`.

Cancelling the within-parity Vandermonde factors gives

`boxed:`

`2^(C(A,2)) |prod_(e in E,o in O)(e-o)|`

`=3^(C(L,2)) |prod_(e in E,o in O)(e-3o-s)|.`            (7.1)

Classification: **new analytic theorem**.

This is a true whole-cycle integer-permutation identity, not a rotation-numerator congruence.

### 7.1 Attractive 2-adic corollary

Because `e-o` is odd, while `e-3o-s` is even for odd `s`, (7.1) gives

`boxed: sum_(e,o) v2(e-3o-s)=C(A,2).`                   (7.2)

At first sight this is a scale-free global packing law.

### 7.2 Red-team: the 2-adic law collapses to pure word combinatorics

For odd `s`, a length-`r` parity string determines the starting residue modulo `2^r` uniquely. Therefore for two distinct phases of a primitive `T_s` cycle,

`v2(n_i-n_j)`

is exactly the longest common prefix length of the two cyclic parity rotations beginning at `i` and `j`.

Since

`e-3o-s=2(T_s(e)-T_s(o))`,

(7.2) becomes the pure cyclic-word identity

`boxed:`

`sum_(i:d_i=0, j:d_j=1) LCP(rot_(i+1) w, rot_(j+1) w)`

`= C(A-L,2)+C(L,2).`                                    (7.3)

This identity holds for every primitive binary word. A direct combinatorial proof is obtained by bijecting each same-current-bit unordered pair of rotations with the unique earlier cross-bit pair and depth at which their common suffix begins.

Thus the apparently new 2-adic determinant energy contains **no ownership information at all**.

Classification: **new all-word collapse / method barrier**.

### 7.3 Full product identity is also homogeneous in `(states,s)`

Write `e=s x_e`, `o=s x_o`. Every cross factor on both sides of (7.1) contains exactly one factor `s`:

`e-o=s(x_e-x_o)`,

`e-3o-s=s(x_e-3x_o-1)`.

There are equally many cross factors on both sides, so all powers of `s` cancel. The full Vandermonde identity is therefore an identity of the normalized rational phases `x=n/s` and is covered by the unit-increment homogeneity barrier.

It passes the RL20 fake exactly.

**Route classification:** **dead as a standalone ownership discriminator.**

A future determinant route would have to introduce a genuinely non-homogeneous lattice/content operation, not merely a homogeneous product of affine differences.

---

## 8. Candidate architecture 4 — global moment hierarchy

Summing powers of the generalized recurrence gives exact whole-cycle moment identities.

Let

`E_r=sum_(e in E)e^r`,

`O_r=sum_(o in O)o^r`,

with `O_0=L`.

For every `r>=1`, permutation of the cycle gives

`boxed:`

`(2^r-1)E_r + (2^r-3^r)O_r`

`= sum_(j=0)^(r-1) C(r,j) 3^j s^(r-j) O_j.`             (8.1)

The first cases are

`boxed: E_1-O_1=L s,`                                    (8.2)

`boxed: 3E_2-5O_2=6s O_1+L s^2,`                        (8.3)

`boxed: 7E_3-19O_3=27s O_2+9s^2 O_1+L s^3.`             (8.4)

Classification: **new analytic global identities**.

### Red-team

Each equation is homogeneous of total degree `r` in `(states,s)`. Dividing by `s^r` gives the identical rational-phase moment identity for `x=n/s`.

Therefore the entire raw moment hierarchy is denominator-blind and holds on every canonical generalized cycle, including the RL20 fake.

Simple parity/nonzero-mod-3 integer spacing does not repair this: the missing ingredient would have to be a genuinely non-homogeneous consequence of **unit** increment `s=1`, such as a unit-lattice spacing/fractional-part/basin statement not invariant under simultaneous scaling.

**Route classification:** **raw moments dead; a non-homogeneous unit-increment consumer remains a sharply named missing mechanism.**

---

## 9. Mandatory RL20 fake audit

For the exact inherited length-184, weight-116 RL20 fake,

`gcd(D,Q)=1`,

so

`boxed: s=D`.

RL79 verifies exactly that its rotation numerators `Q_m` are pairwise distinct positive integers satisfying

`2Q_(m+1)=Q_m` on `0` bits,

`2Q_(m+1)=3Q_m+D` on `1` bits,

with parity exactly equal to the fake word and `gcd(Q_m,D)=1` for every phase.

Thus it is a primitive positive integer cycle of `T_D`.

It also satisfies the new generalized moment identities and Vandermonde valuation identity exactly.

This sharpens the negative control:

> local grammar, rational least-state structure, positive primitive integer permutation structure, nonlinear whole-cycle determinant identities, 2-adic parity-vector packing, and normalized moments can all coexist while ordinary Collatz ownership fails maximally.

The missing information is the **absolute specialization `s=1`**.

---

## 10. Post-tournament impossibility map

RL79 can now organize the failed/surviving architectures more sharply.

### Class I — rotation algebra at modulus `D`

Examples: linear normalized rotation differences, quadratic minors, homogeneous cross-rotation products.

**Status:** collapsed. RL78 gives rank-one unit transport; RL79 extends this to the full polynomial rotation algebra modulo `D`.

### Class II — full denominator monodromy/order

Examples: multiplicative order of the full return multiplier, affine order of the full word modulo a prime divisor of `D`.

**Status:** collapsed. Under ownership, the full monodromy is the identity modulo every divisor of `D`.

### Class III — homogeneous global state identities

Examples: raw moments, Vandermonde products, normalized products/growth laws, determinant ratios homogeneous in states and the odd increment.

**Status:** structurally denominator-blind after canonical normalization `x=n/s`.

### Class IV — local/global parity grammar without absolute increment

**Status:** maximally nonrestrictive at the generalized-map level: every primitive above-resonance word has a positive primitive `T_s` integer realization.

### Class V — genuinely non-homogeneous `s=1` consumers

Examples in principle:

- an absolute integer-lattice spacing theorem on the normalized phases;
- an exact content/gcd obstruction that cannot be scaled away;
- a property of the actual ordinary Collatz basin of `1`;
- a non-homogeneous predecessor/ownership barrier tied specifically to the `+1` map.

**Status:** this is the genuinely live class after RL79.

---

## 11. Route re-ranking after RL79

1. **Outside-coordinate `s=1`-specific discrete consumer — highest priority.** The requested certified-basin / dyadic-blue-funnel route belongs here and is therefore a genuinely different direction, not another reparameterization of full-phase divisibility.
2. **Absolute integer-lattice/content obstruction.** Seek a theorem that uses `s=1` before normalizing, and produces a nonzero integer/fractional quantity too small to exist. Existing scale barriers make this difficult but it remains conceptually valid.
3. **Prime/prefix zero-sum route only with a non-modular consumer.** Pure full-return order is dead; sparse prefix structure could matter only if coupled to ordering, integrality, or basin membership.
4. **Existing RL75 routes** are retained as secondary references but are demoted after RL76–RL79 unless they acquire a new `s=1`-specific consumer.

No generic radius-4/5/6 case tree, q-digit extension, new homogeneous moment ladder, or nonlinear rotation-minor search is recommended.

---

## 12. Correction / demotion ledger additions

Retain all RL72–RL78 corrections and add:

1. **Generalized-increment realization added.** Every primitive above-resonance word canonically realizes as a primitive positive integer `T_s` cycle with `s=D/gcd(D,Q)`.
2. **Ownership reframed.** Genuine Collatz full-`D` ownership is exactly the specialization `s=1`; fake compatibility is not exceptional.
3. **Homogeneous `T_s` invariants demoted as ownership tests.** If simultaneous scaling `(states,s)` removes the distinction, the invariant cannot force `s=1`.
4. **Nonlinear cross-rotation modulo-`D` searches demoted.** The full polynomial rotation algebra reduces to one variable `Q_0` via unit transport.
5. **Pure denominator-prime full-monodromy order demoted.** Genuine ownership makes the full map the identity modulo `D` and every divisor.
6. **Vandermonde 2-adic route demoted.** Its scale-free valuation law is exactly a pure all-word cyclic LCP identity.
7. **Raw global moment hierarchy demoted as an ownership discriminator.** It is homogeneous in `(states,s)` and survives every canonical generalized cycle.
8. **New strategic requirement.** A successful bridge must use a non-homogeneous fact special to the ordinary `+1` map (`s=1`).

No prior closed radius-3 or Gate-A theorem is affected.

---

## 13. Exact proof state after RL79

### New proved analytic mathematics

- canonical generalized-increment cycle theorem (Section 3);
- unit-increment / homogeneity barrier (Section 4);
- polynomial rotation-algebra collapse modulo `D` (Section 5);
- owned full-word monodromy identity modulo every divisor of `D` (Section 6);
- cross-parity Vandermonde product identity (Section 7);
- collapse of its 2-adic valuation to the all-word cyclic LCP identity (Section 7.2);
- generalized global moment hierarchy (Section 8).

### New exact finite verification

The RL79 verifier checks:

- `1,578` primitive above-resonance small-word generalized cycles;
- `148,730` rotation polynomial-collapse identities;
- `9,476` monodromy identities;
- `4,734` generalized moment identities;
- `1,578` exact small-word Vandermonde identities;
- `1,578` all-word LCP-collapse identities;
- the exact RL20 fake as a primitive `T_D` integer cycle;
- RL20 fake first/second moment identities;
- RL20 fake Vandermonde 2-adic total `C(184,2)=16,836`;
- modular projections of the full fake Vandermonde identity.

The verifier is an audit/falsification certificate, not the proof of the infinite analytic statements.

### Global closure state

Unchanged:

- primitive/full-`D` radius-3 local obstruction: **closed**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

---

## 14. RL80 decision

RL79 mainly produces a rigorous common-barrier / route-elimination result rather than a new closing mechanism. The requested next-session pivot is therefore activated strongly.

RL80 should investigate:

# **The infinite proved-blue dyadic funnel and the rigorously certified basin of 1**

The reason is now sharper than the original intuition: membership in the actual basin of the ordinary Collatz map is a genuinely `s=1`-specific discrete property. It is not preserved by the generalized `T_s` construction that makes word algebra, homogeneous moments, determinant products, and local parity grammar so flexible.

RL79's surviving secondary route is the search for any other non-homogeneous unit-increment/content theorem. RL80 should preserve it, but the certified-basin route is primary.
