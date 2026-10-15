# RL75 — Global RL closure route tournament and primitive pump transversality

Date: 2026-08-24

## 0. Executive outcome

RL75 was deliberately run above the narrow Gate-A continuation thread. The incoming RL74 gate is checksum-clean and its fast verifier passes, so the RL74 frozen proof-state ledger is accepted under the verification-economy rule. RL72's global audit, lemma catalogue, correction/demotion ledger and ranked roadmap were then used as the strategic baseline, with selective GitHub recovery of RL19, RL20, RL48, RL50 and RL64 interfaces.

The global proof state remains unchanged at theorem level:

- exact primitive/full-`D` radius-3 obstruction: **closed local theorem**;
- Gate A: **open globally**;
- Gate B: **open globally**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

The tournament nevertheless produces a useful strategic change and two analytic syntheses.

### RL75 strategic conclusion

The strongest next architecture is not a pure rank/height proof, not a generic radius ladder, and not determinant-zero descent. It is a **hybrid owned-macro periodicity-or-packing route**:

> combine the RL73 giant owned height-one macro, RL74's exact full-phase Möbius law for repeated pumps, RL19/RL20 global population/packing, and RL50 defect/rank structure to prove that a genuine low-`k` owned macro cannot be both arbitrarily long and globally full-phase compatible.

The next theorem should handle the periodic and aperiodic possibilities in one quantitative framework. The desired endpoint is an upper bound below RL73's guaranteed

`40,249,491,324,522,944`

aligned `00` columns for every hypothetical odd `27<=k<=165` Gate-A violation.

### New RL75 analytic synthesis 1

RL74's Möbius determinant has an exact **physical-drift factorization**. For a genuine full-phase decomposition

`v_q=A c^q B`,

if `x` is the actual physical state entering the first copy of `c`, then the RL74 determinant is zero exactly when one copy of `c` fixes `x`. Thus, for a nonempty proper pump segment inside a primitive cycle, determinant zero is impossible: it would repeat a physical cycle state before the full period.

This repairs the strategic interpretation of RL74's determinant-zero “deletion hook”. In the genuine primitive setting the degenerate branch is not a promising descent case; it is excluded by primitivity. The surviving case is the nondegenerate Möbius branch, whose unresolved issue is **uniform context control**.

### New RL75 analytic synthesis 2

The RL48 full-phase quotient satisfies `N==3 (mod8)`. RL20 proves every phase state of a nontrivial positive cycle is nonzero modulo 3. Since both `N` and `N+4` are phase states, necessarily

`N==1 (mod3)`, hence `N==19 (mod24)`.

Therefore RL72's raw phase-residual barrier sharpens from

`|(2-N)M|>=M`

to

`|(2-N)M|>=17M`

on a genuine nontrivial positive full-phase cycle. This is a strengthening of a **method barrier**, not progress toward a small-multiple contradiction.

---

## 1. Incoming verification and authority

The incoming RL74 gate was checked exactly as requested:

1. outer RL74 `.sha256`: **PASS**;
2. freshly unpacked internal `SHA256SUMS.txt`: **PASS**;
3. `bash verification/run_fast_rl74_verifiers.sh`: **PASS**.

The RL74 fast output retained the frozen counts:

- concatenation checks: `225`;
- repeat checks: `40`;
- pump/Möbius checks: `420`;
- canonical fixed-area family checks: `61`;
- positive corrected-cap state checks: `3904`;
- `Psi` telescope checks: `61`;
- canonical-prefix specialization checks: `168`.

No historical expensive suite was recursively rerun.

The RL74 ledger therefore remains authoritative. In particular retain exactly:

- Gate A terminal even `k`: analytically impossible;
- Gate A `k<=25`: closed by exact finite-certificate corollary;
- first open terminal exponent: odd `k>=27`;
- every hypothetical odd `27<=k<=165` violation has the RL73 giant post-first-mismatch maximal height-one block with at least `40,249,491,324,522,944` aligned `00` columns;
- canonical fixed-area pumping shows endpoints, `H`, repaired `Jg`, and `Psi` do not price zero-area count;
- fixed-context full phase does see a repeated pump via the RL74 Möbius law;
- Gate A and Gate B both remain globally open.

---

## 2. New RL75 theorem — physical-drift factorization of the RL74 determinant

### 2.1 Setup

For a binary word `w`, use the standard affine map

`F_w(X)=(3^wt(w) X+Q(w))/2^|w|`.

Let

`v_q=A c^q B`

be a full half-word decomposition as in RL74. Put

`n=|c|`, `s=wt(c)`, `P=2^n`, `R=3^s`, `C=Q(c)`, `delta=R-P`.

Let

`L_A=|A|`, `w_B=wt(B)`,

`X0=2^(|A|+|B|)`, `Y0=3^(wt(A)+wt(B))`.

RL74 defines

`A_* = delta 3^w_B Q(A) + 2^L_A 3^w_B C + 4 delta Y0`,

`B_* = delta 2^L_A Q(B) - 2^L_A 3^w_B C`,

`D_* = A_* X0+B_* Y0`,

and

`M_q=X0 P^q-Y0 R^q`.

Assume the full-phase quotient is

`N=(Q(v_q)+4*3^wt(v_q))/M_q`,

so on the RL48 four-swap trajectory

`F_{v_q}(N+4)=N`.

Define the actual physical states

`x=F_A(N+4)`

at pump entry and

`y=F_c^q(x)`

at pump exit, before `B`.

### 2.2 Exact factor identities

Then

`boxed: A_*+delta N Y0 = 2^L_A 3^w_B (delta x+C)`,

and

`boxed: delta N X0-B_* = 2^L_A 3^w_B (delta y+C)`.

Also one pump copy satisfies

`delta F_c(X)+C=(R/P)(delta X+C)`,

so

`boxed: delta y+C=(R/P)^q(delta x+C)`.

Substituting into `D_*` gives the two equivalent factorizations

`boxed: D_*=2^L_A 3^w_B (delta x+C) M_q/P^q`,

`boxed: D_*=2^L_A 3^w_B (delta y+C) M_q/R^q`.

These are exact identities.

### 2.3 Determinant-zero is physical pump closure

Whenever `M_q!=0`,

`D_*=0`

if and only if

`delta x+C=0`.

But

`F_c(x)-x=(delta x+C)/P`.

Therefore

`boxed: D_*=0 <=> F_c(x)=x.`

So the Möbius degeneracy is not merely an abstract constant-quotient coincidence. It says that the actual physical state entering the pump is already periodic under the proper segment `c`.

### 2.4 Primitive-cycle corollary

If `c` is a nonempty proper segment of a genuine primitive cycle trajectory, `F_c(x)=x` repeats a physical phase state before the full cycle period. That contradicts primitivity.

Hence:

> **RL75 primitive pump nondegeneracy theorem.** In a genuine primitive full-phase cycle, every nonempty proper repeated pump segment has `D_*!=0`.

This consumes exactly the primitiveness caveat left open in RL74.

### 2.5 Special pumps

For `c=10`,

`P=4`, `R=3`, `C=1`, `delta=-1`,

and the fixed-point equation is `x=1`. A positive nontrivial cycle cannot contain the state `1`, so

`D_*<0`

for every positive nontrivial occurrence.

For `c=101`,

`P=8`, `R=9`, `C=7`, `delta=1`,

and the fixed point is `x=-7`. Hence for positive physical `x`,

`D_*>0`.

Thus the two RL74 special pumps are automatically nondegenerate by positivity/nontriviality alone.

### 2.6 Exact adjacent-repeat difference

For fixed context `(A,B,c)`, RL74 gives a Möbius function of `z_q=(R/P)^q`. Direct subtraction yields

`boxed: N_(q+1)-N_q = D_* (PR)^q/[M_q M_(q+1)]`

whenever the displayed denominators are nonzero.

In particular the nondegenerate quotient moves strictly monotonically with repeat count when the sign is fixed. If two repeat counts both happen to be genuine nontrivial full-phase integer completions, their quotients are both `19 mod24`, so their difference is a nonzero multiple of 24.

This remains **fixed-context** information. It does not by itself provide a uniform Gate-A repeat bound because the context coefficients and physical pump-entry state vary across hypothetical RL objects.

### 2.7 Important red-team qualification

The identities

`delta y+C=(R/P)^q(delta x+C)`

also imply familiar 2-adic/3-adic divisibility requirements for an integral legal repeated pump. Those valuation facts are largely **local pump-integrality consequences**, not the missing ownership theorem. RL75 does not promote them as global closure.

The genuinely new strategic content is the exact interpretation and elimination of the determinant-zero branch in the primitive full-phase setting.

Classification: **analytic theorem + analytic strategic corollary**. The bundled verifier is an exact finite algebra audit, not the proof.

---

## 3. New RL75 residue synthesis — `N==19 (mod24)`

RL48 gives the physical half-cycle pair

`N --u--> N+4 --v--> N`

with

`N==3 (mod8)`.

RL20's global cycle argument proves no phase state of a nontrivial positive cycle is divisible by 3. Therefore neither `N` nor `N+4` is `0 mod3`.

If `N==2 mod3`, then `N+4==0 mod3`, impossible. If `N==0 mod3`, `N` itself is impossible. Hence

`N==1 mod3`.

Combining with `N==3 mod8` gives

`boxed: N==19 mod24`.

Consequently `N>=19` and the raw RL65 phase residual obeys

`|(2-N)M|=(N-2)M>=17M`.

Classification: **analytic synthesis / strengthened method barrier**.

This makes direct raw small-multiple closure less plausible, not more.

---

## 4. Tournament scoring principles

The route tournament was judged by:

- closure leverage if its target theorem succeeds;
- how much exact RL machinery already points in its direction;
- independence from known dead/coboundary routes;
- whether a cheap falsification test exists;
- dependence on unproved external theory or large finite work;
- whether RL73/RL74 materially improved the route;
- whether the route attacks a theorem-sized missing edge rather than extending compatibility data.

A route is not promoted merely because it could in principle prove RL. It must have a credible next theorem whose hypotheses are actually available.

---

## 5. Route 1 — Gate A rank / height / area closure

1. **Exact closure theorem.** Prove `H>=k` at every canonical terminal state `J=2^k`.
2. **Supporting lemmas.** RL45 valuation quotient; RL47/RL65 `H=sum delta_j`; RL62 H<=24 exact certificate; RL66 odd-`k`; RL68–RL71 rank-tail selectors; RL73 giant macro; RL74 pump barrier/law.
3. **Missing lemma.** A global ownership-sensitive lower bound that prevents zero-area synchronized depth from hiding arbitrarily large rank/time complexity at fixed `H`.
4. **Scope.** Gate A globally if uniform; low-`k` band if restricted to `27<=k<=165`.
5. **Independence test.** A proof using only endpoints, `H`, local `J`, repaired `Jg`, `Psi`, or separable rank weights is not independent; RL48/RL74 already barrier those forms.
6. **Known barriers.** RL48 separable relaxation; RL50 height-one Collatz conjugacy; RL63/64 dangerous local cylinders; RL74 fixed-area canonical pump and bounded `Psi` mass.
7. **Cheapest red-team.** Test any proposed invariant against the RL74 canonical `(101)^p ... (10)^q0` family and ask whether full phase is actually used.
8. **Best first theorem.** Not another direct `H>=k` inequality. Prove a quantitative owned-macro periodicity/packing theorem that controls the zero-area sector.
9. **Downstream closure value.** Potentially all Gate A; at minimum the first open low-`k` band.
10. **Stop/pivot.** If the candidate theorem remains valid/invalid on unrestricted height-one dynamics without using global completion, abandon it.
11. **Assessment.** Very high leverage and excellent fit with exact machinery, but a pure Gate-A local proof is no longer the best formulation. Merge into the hybrid route below.

**Tournament status:** strong ingredients, but **merged into Route 10 hybrid** rather than ranked independently.

---

## 6. Route 2 — bounded-radius / owned-rotation Gate B

1. **Exact closure theorem.** Show every genuine RL object has two owned primitive full-`D` rotations in a locally closed radius sector; radius 3 would close immediately, or radius `<=R0` plus local closure through `R0` would close Gate B.
2. **Supporting lemmas.** Closed radius-3 tree RL7–RL19; RL19 weighted rotations; RL20 exact radius-4-packed fake local model; RL48/RL64 full phase/ownership.
3. **Missing lemma.** A `D|Q`/ownership-sensitive absolute radius bound.
4. **Scope.** Gate B, potentially all RL when combined with Gate A architecture.
5. **Independence test.** Any bridge based only on local root/final grammar is dead; it must discriminate against RL20's fake `D∤Q` model.
6. **Known barriers.** RL20 local-grammar countermodel; RL49 even-distance correction kills the RL48 half-period radius-3 shortcut.
7. **Cheapest red-team.** Apply any candidate bound to the frozen RL20 radius-4 model. If it cannot see `D∤Q`, it is not the missing bridge.
8. **Best first theorem.** Derive one nonlocal `D|Q`-sensitive transport/packing inequality that forces a close owned pair. Do not first build a generic radius-4/5/6 case tree.
9. **Downstream closure value.** Enormous: a radius-3 bridge closes Gate B; an `R0>3` theorem would make finite local extension relevant.
10. **Stop/pivot.** If every candidate close-pair inequality collapses to state coboundary/proper-factor identities, deprioritize.
11. **Assessment.** Highest theoretical leverage, but currently lower plausibility than the owned-macro route because no modern theorem yet points to an absolute radius constant.

**Special radius judgment.** `R0=4` is the smallest sensible *experimental* candidate because radius 3 is closed and the sharp fake local model has minimum 4. This is not evidence that genuine RL has radius `<=4`. A generic radius ladder should not be launched before a global bridge makes it relevant.

---

## 7. Route 3 — direct full-phase arithmetic contradiction

1. **Exact closure theorem.** Produce a genuinely new residual `W` with `M|W` and `0<|W|<M`, or another sign/integrality contradiction, from full phase.
2. **Supporting lemmas.** RL48 same-root selector/full-word factorization; RL64 ownership; RL65 defect quotient; RL74 Möbius pump law; RL75 physical-drift factorization.
3. **Missing lemma.** A second independent relation that removes the state coboundary and leaves a small residual.
4. **Scope.** Could bypass Gate A/Gate B entirely.
5. **Independence test.** Reject raw `(2-N)M`, RL20 block coboundary, RL48 proper-factor identity, and any rotation state difference multiple.
6. **Known barriers.** RL72 proves the raw residual has magnitude at least `M`; RL75 strengthens this to at least `17M` on genuine nontrivial full phase.
7. **Cheapest red-team.** Symbolically divide proposed `W` by `M`; if the quotient is an already-known integer state/phase difference, retire it.
8. **Best first theorem.** Search only for a normalized residual tied to a proper owned substructure, not the whole-word phase numerator.
9. **Downstream closure value.** Potentially complete RL contradiction.
10. **Stop/pivot.** Two consecutive candidates collapsing to known coboundaries is enough to stop a session.
11. **Assessment.** High leverage but currently low-to-medium plausibility. RL75's residue refinement makes the obvious route worse.

**Tournament status:** not top four as a standalone route; keep only as a subtool inside hybrid/Diophantine work.

---

## 8. Route 4 — global invariant / defect-energy route

1. **Exact closure theorem.** Find a sign-definite or two-sided global quantity forcing `H`/defect/phase incompatibility.
2. **Supporting lemmas.** RL47 rank displacement; RL49 zero-position telescope; RL50 exact defect energy and `H/E` common displacement vector; RL64 ownership; RL73 giant macro; RL74 `Psi` barrier.
3. **Missing lemma.** A uniform lower bound on active-rank weight or a global way to charge zero-area depth.
4. **Scope.** Gate A, possibly a broad direct contradiction.
5. **Independence test.** If the invariant is only an upper mass cap or endpoint telescope, RL74 already gives a counterfamily.
6. **Known barriers.** Fixed safe-CF small-`E` constants are not uniform; late tiny weights can hide large unweighted `H`; RL74 count can have bounded `Psi` mass.
7. **Cheapest red-team.** Evaluate on the canonical RL74 family with `p=3q+15`.
8. **Best first theorem.** Derive an owned lower weight/packing inequality from full phase, not a new scalar potential.
9. **Downstream closure value.** If uniform, could close Gate A.
10. **Stop/pivot.** If only upper bounds emerge, merge into packing rather than continuing scalar-energy work.
11. **Assessment.** Strong mathematical fit, but not strategically independent of the owned-macro missing edge.

**Tournament status:** **merged into Route 10 hybrid**.

---

## 9. Route 5 — minimal-counterexample / descent

1. **Exact closure theorem.** Construct a legal transformation from a hypothetical minimal RL object to a strictly smaller genuine RL object preserving all required full-phase/primitive conditions.
2. **Supporting lemmas.** RL74 determinant-zero constant-quotient pump law.
3. **Missing lemma.** A nondegenerate deletion/replacement that preserves full phase, or a different well-founded transformation.
4. **Scope.** Potentially all RL.
5. **Independence test.** Merely deleting a locally closed quotient pump is not enough; full phase and physical legality must remain.
6. **Known barriers.** RL75 now proves determinant zero means the physical pump itself fixes its entry state. In a primitive cycle this branch is impossible before any descent is performed. When determinant is nonzero, RL74 does not preserve full phase under deletion.
7. **Cheapest red-team.** For any proposed deletion, compute the RL74 determinant / physical state image and check the full-phase quotient before and after.
8. **Best first theorem.** None currently strong enough to justify a dedicated session; a new transformation would have to come from another route.
9. **Downstream closure value.** High if found.
10. **Stop/pivot.** Immediate unless an explicit legality/full-phase-preserving map is written down.
11. **Assessment.** **Major demotion in RL75.** The exact degeneracy that looked like a descent hook is actually primitive-subcycle closure, while the nondegenerate case lacks a descent map.

**Tournament status:** not ranked.

---

## 10. Route 6 — product / growth / weighted-population route

1. **Exact closure theorem.** Combine the RL19/RL20 near-resonance/huge-length dichotomy with RL-specific full-phase/terminal restrictions to eliminate both branches.
2. **Supporting lemmas.** RL19 odd-step product; weighted populations/state packing; RL20 coprime-6 packing and CF gate; branch-specific global numerator lower bound; RL48/RL64 full phase; modern terminal restrictions.
3. **Missing lemma.** An RL-specific restriction on the reduced ratio `(A/g,L/g)`, on `g=gcd(A,L)`, or on the admissible CF/convergent index coming from phase/ownership.
4. **Scope.** Very broad global RL/cycle sector.
5. **Independence test.** It is independent of the Gate-A local selector if the new restriction uses the whole word/denominator, not safe-CF survivor constants.
6. **Known barriers.** Existing CF bounds leave an enormous unbounded branch; concrete numerical floors may rely on inherited external `R#>=2^71`.
7. **Cheapest red-team.** Derive the candidate restriction symbolically before running any CF scan. If it is only another approximation to `log_2 3`, it adds nothing.
8. **Best first theorem.** Upgrade RL20's branch-specific two-sided logarithmic window to a full-phase-wide window, or derive a congruence/size restriction on the reduced convergent denominator from the four-swap pair/terminal `k`.
9. **Downstream closure value.** Could kill a global branch and perhaps bypass Gate A/Gate B.
10. **Stop/pivot.** If the only new information is a larger finite convergent cutoff, stop.
11. **Assessment.** **Strong deliberate alternative.** Global, independent, well-supported, but more external/arithmetic and less directly sharpened by RL73/RL74 than the winning hybrid.

---

## 11. Route 7 — global combinatorial packing / cyclic-word route

1. **Exact closure theorem.** Force either a close owned-rotation pair or an impossible number/density of globally legal states/macros.
2. **Supporting lemmas.** RL19 state packing; RL20 strict-excursion programme; RL73 giant macro; RL74 pump law.
3. **Missing lemma.** A global packing budget that charges long synchronized zero-area structure despite local freedom.
4. **Scope.** Gate B or Gate A depending formulation.
5. **Independence test.** Pure word grammar is insufficient; `D|Q`/physical-state ownership must enter.
6. **Known barriers.** RL20 radius-4 fake word defeats local packing-to-radius3; RL74 canonical family defeats endpoint/count-only macro packing.
7. **Cheapest red-team.** Test on both the RL20 fake radius-4 word and RL74 canonical pump family.
8. **Best first theorem.** A periodicity-or-distinct-state dichotomy for an owned height-one macro, with the distinct-state branch charged by RL19 population packing.
9. **Downstream closure value.** High: this is exactly the aperiodic half of the winning hybrid.
10. **Stop/pivot.** If the packing statistic ignores `D|Q` or physical state size, retire it.
11. **Assessment.** Strong when hybridized with RL74 full phase; weak as pure combinatorics.

**Tournament status:** **merged into Route 10 hybrid**.

---

## 12. Route 8 — Diophantine / approximation route

1. **Exact closure theorem.** Derive an RL-specific exponential/Diophantine incompatibility involving `2^a`, `3^ell`, phase, ownership or competing pumps.
2. **Supporting lemmas.** RL19/RL20 near resonance/CF; RL74 shrink/growth ratios `(8/9)^p(4/3)^q`; RL74 Möbius law; RL75 nondegeneracy.
3. **Missing lemma.** Eliminate varying context coefficients or show simultaneous 2-adic/3-adic/full-phase constraints force an impossible approximation.
4. **Scope.** Potentially a large Gate-A sector or all RL.
5. **Independence test.** A plain Baker/CF estimate on `A log2-L log3` without RL-specific phase is not enough.
6. **Known barriers.** Context variation; local p-adic compatibility; very large natural parameter ranges; possible external LMN/Baker dependence.
7. **Cheapest red-team.** First derive a fixed integer/exponential equation with bounded number of context parameters. If context remains arbitrary word data, do not invoke heavy Diophantine theory.
8. **Best first theorem.** For two competing closed pumps, express full phase as a two-parameter Möbius/exponential relation and determine whether its determinant/resultant can be bounded independently of context.
9. **Downstream closure value.** Could control exactly the shrink-prepayment/growth-pump phenomenon that defeats local mass bounds.
10. **Stop/pivot.** If adding a second pump only replaces one arbitrary context coefficient with several, stop.
11. **Assessment.** **Top-four alternative** with real RL74 novelty, but higher missing-theory and external-dependence risk.

---

## 13. Route 9 — genuine 2-adic / 3-adic incompatibility

1. **Exact closure theorem.** Show the same finite integer/global RL completion cannot satisfy the required 2-adic ownership cylinder, 3-adic phase selector, positivity and size constraints.
2. **Supporting lemmas.** RL63/64 all-word cylinders; RL65–RL71 digit ladder; RL74 pump law; RL75 physical-drift interpretation.
3. **Missing lemma.** A size/order theorem that consumes the p-adic information.
4. **Scope.** Gate A sectors, perhaps broader.
5. **Independence test.** More digits are not independent progress unless a global theorem turns them into size/order contradiction.
6. **Known barriers.** RL71 finite-window compatibility; local CRT is not closure; repeated-pump valuation constraints are largely local integrality.
7. **Cheapest red-team.** Ask whether the proposed incompatibility remains merely a compatible residue class modulo higher powers.
8. **Best first theorem.** Couple an existing selector to a global numerator/packing bound; do not compute q=6/q=7 by default.
9. **Downstream closure value.** High only if coupled; low standalone.
10. **Stop/pivot.** If output is another admissible residue class, stop immediately.
11. **Assessment.** Important ingredient but not a standalone top route.

---

## 14. Route 10 — hybrid owned-macro periodicity-or-packing route

1. **Exact closure theorem.** For every genuine full-phase Gate-A violation in the first open band `27<=k<=165`, prove an upper bound on the RL73 post-first-mismatch maximal height-one block strictly below `40,249,491,324,522,944` aligned `00` columns.
2. **Supporting lemmas.** RL19 weighted populations/state packing and rotation identities; RL20 strict-excursion/packing architecture; RL47/RL50 rank/defect coupling; RL64 full-phase extendability; RL65–RL71 low-`k` terminal selectors; RL73 giant owned macro; RL74 canonical barrier + Möbius pump law; RL75 primitive pump nondegeneracy.
3. **Missing lemma.** A quantitative dichotomy that controls both:
   - **periodic/repetitive macro structure** by extracting a proper closed pump and applying nondegenerate full-phase context control;
   - **aperiodic/high-complexity structure** by charging distinct states/weights to a global population/packing/size budget.
4. **Scope.** First open Gate-A band immediately; architecture can potentially extend to all odd `k`.
5. **Independence test.** Periodic branch must genuinely use full phase; aperiodic branch must use global state/word budget. Neither may reduce to endpoint `Psi`, local grammar, or separable rank relaxation.
6. **Known barriers.** RL74 proves count alone and bounded mass are insufficient. RL75 kills only the degenerate determinant branch; nondegenerate context remains variable. RL20 proves local packing alone is insufficient.
7. **Cheapest red-team.** Every proposed dichotomy must survive both exact stress objects:
   - RL74 canonical shrink/growth family;
   - RL20 radius-4 local-grammar fake model with `D∤Q`.
   If it cannot distinguish them from genuine owned full-phase data, reject it.
8. **Best first theorem.** **Owned synchronized-macro periodicity-or-packing theorem**: prove that any full-phase-owned low-`k` height-one block with `Z` aligned zeros either contains a quantitatively overdeep proper repeated pump forbidden by uniformized RL74 Möbius/context bounds, or produces enough distinct physical/state-weight mass to violate an RL19/RL20 global packing budget. Target the explicit threshold `Z=40,249,491,324,522,944`.
9. **Downstream closure value.** If established for `27<=k<=165`, it closes the entire first open low-`k` Gate-A band, not merely the nested `g=0` subcase. A uniform version could close Gate A.
10. **Stop/pivot.** If neither branch can be made quantitative without an unbounded arbitrary context coefficient, pivot to Route 6 (product/CF) or Route 2 (global bounded-radius), rather than extending local digits.
11. **Assessment.** **Tournament winner.** It directly consumes the strongest modern theorem (RL73 giant macro), the strongest ownership-sensitive new mechanism (RL74 Möbius law), the RL75 primitive nondegeneracy repair, and old global packing machinery. It has low external dependence and clear falsification tests.

---

## 15. Special bounded-radius programme

### 15.1 Can an absolute `R0` be justified now?

No inherited theorem currently justifies any absolute radius bound for every genuine RL object.

The RL20 countermodel establishes a precise negative fact: local least-root/final-return slope grammar can coexist with all-rotation minimum radius exactly `4`. It is not a genuine cycle because `D∤Q`.

Therefore any absolute `R0` theorem must use at least one genuinely global ingredient absent from that model, such as:

- `D|Q` / full phase;
- actual phase-state ownership;
- weighted population/state packing;
- a non-coboundary global rotation relation.

### 15.2 Best candidate `R0`

`R0=4` is the smallest sensible reconnaissance value, not a conjectured theorem. It has two reasons only:

1. radius 3 is already closed;
2. the sharp local-grammar fake model has minimum radius exactly 4.

This means a global theorem forcing radius `<=4` would be maximally economical. It does **not** mean such a theorem is currently likely.

### 15.3 What local theorem would then be needed?

If a genuine global bridge proves `radius<=4`, one would need an exact primitive/full-`D` radius-4 local closure theorem extending the radius-3 case tree. No such general radius-4 closure is currently in the frozen ledger.

The correct order is therefore:

1. cheap global `D|Q`-sensitive radius-4 bridge reconnaissance;
2. only if evidence/theorem emerges, classify radius-4 primitive/full-`D` cases;
3. do not pre-emptively build radius 5,6,... ladders.

---

## 16. Cross-generation synthesis results

### 16.1 RL19/RL20 population + RL64 full phase

Still promising, but the most natural use is now the **aperiodic branch** of the winning macro dichotomy. Full phase must supply the ownership filter; population/packing supplies the global budget.

### 16.2 Radius-3 closure + modern ownership

Still a high-leverage Gate-B engine, but no owned close-pair theorem is presently known. The four-swap physical closeness `N,N+4` is not a word-radius bridge.

### 16.3 RL47/RL50 defects + RL64–RL71 selectors

The exact missing ingredient remains a lower active-weight/zero-depth coupling. RL74's canonical family proves no endpoint/telescope repair alone will provide it. This synthesis belongs inside the macro/packing route.

### 16.4 RL19 product bounds + modern terminal restrictions

This is the best deliberate alternative. The terminal `k`/full-phase structure may constrain admissible near-resonant ratios, but no such uniform theorem is yet proved.

### 16.5 RL20 numerator windows + full-phase quotient restrictions

Useful only if generalized beyond the branch-specific hard weak-close pattern. RL75's `N==19 mod24` is too weak by itself.

### 16.6 Rank-tail exact values + global cyclic packing

Potentially useful in the aperiodic macro branch: exact low-`k` terminal information can reduce context variability while packing controls the long zero-area middle.

### 16.7 Bounded radius + genuine `D|Q`

A valid discriminator exists in principle because the RL20 fake model explicitly has `D∤Q`. No actual radius bound follows yet.

### 16.8 RL73 giant macro + RL74 pump law

This remains the strongest modern synthesis. RL75 adds that the Möbius determinant degeneracy is unavailable in a primitive cycle, so all genuine repeated-pump work is nondegenerate.

### 16.9 RL74 determinant degeneracy + descent

**Reclassified.** Rather than enabling deletion descent, determinant zero means a proper physical subcycle and is excluded by primitivity. Standalone descent is therefore demoted.

### 16.10 Competing shrink/growth pumps + Diophantine approximation

Still a serious alternative. The canonical counterfamily demonstrates the exact phenomenon that a shrink pump can prepay a later growth pump. A successful theorem must couple both scales through full phase rather than price either locally.

---

## 17. Tournament ranking

### Rank 1 — Hybrid owned-macro periodicity-or-packing

**Leverage:** very high.  
**Plausibility:** highest among current routes.  
**External dependence:** low.  
**Exact machinery fit:** excellent.  
**Why it wins:** it directly attacks the first open band with the RL73 quantitative giant-macro theorem and uses both periodic (RL74) and aperiodic (RL19/RL20) mechanisms.

### Rank 2 — Product/growth/CF + modern full phase

**Leverage:** high/global.  
**Plausibility:** medium.  
**External dependence:** medium for numerical floors, though analytic forms are available.  
**Missing theory:** an RL-specific restriction on convergent/gcd structure.

### Rank 3 — Global bounded-radius Gate B using `D|Q`/ownership

**Leverage:** extremely high.  
**Plausibility:** medium-low at present.  
**External dependence:** radius-3 tree retains inherited dependencies.  
**Missing theory:** any actual absolute radius theorem.

### Rank 4 — Two-scale Diophantine pump incompatibility

**Leverage:** high.  
**Plausibility:** medium-low but genuinely new after RL74.  
**External dependence:** potentially high if Baker/LMN/S-unit theory enters.  
**Missing theory:** bounded-context exponential equation.

### Deliberately not ranked as standalone

- pure defect/energy and pure Gate A rank are folded into Rank 1;
- pure p-adic digit extension is compatibility without a consumer theorem;
- raw full-phase residual is strengthened as a method barrier;
- determinant-zero descent is demoted by RL75 primitive nondegeneracy.

---

## 18. Selected RL76 theorem target

# Owned synchronized-macro periodicity-or-packing theorem

Work in the first globally open Gate-A band:

`27<=k<=165`, `k` odd, hypothetical violation `H<k`.

By RL73 there is a post-first-mismatch maximal positive height-one synchronized block with at least

`Z0=40,249,491,324,522,944`

aligned `00` columns.

The target is to prove a theorem of the following quantitative form:

> For any genuine RL64 full-phase completion in this low-`k` band, every such owned height-one block has `Z<Z0`.

The proof should establish an exhaustive dichotomy.

### Periodic branch

Extract a nonempty proper closed synchronized factor `c` occurring with repeat structure. Use:

- RL74 exact Möbius law;
- RL75 `D_*!=0` for a proper pump in a primitive cycle;
- terminal/rank selectors and physical context to make fixed-context finiteness **uniform** enough to bound repeat depth.

Do not rely on determinant-zero deletion; that branch is already excluded.

### Aperiodic branch

If no usable deep repeat exists, prove that the block necessarily generates sufficiently many distinct physical states, weighted prefix states, or rank/phase contexts. Charge those against:

- RL19 weighted populations/state packing;
- RL20 coprime-6/strict-excursion packing;
- RL50 defect/rank coupling;
- global full-phase denominator/ownership.

The final inequality must beat `Z0`.

### Required red-team tests

A candidate theorem must explicitly fail or use a missing global hypothesis on:

1. RL74's canonical fixed-area shrink/growth pump family;
2. RL20's exact radius-4 local-grammar fake word with `D∤Q`.

Passing these two stress tests is necessary before investing in large finite work.

### Stop criterion

If the periodic branch cannot be uniformized because context remains wholly arbitrary **and** the aperiodic branch cannot produce a genuine global packing budget, pivot the following session to Rank 2 (product/CF + full phase), not to another q-digit or endpoint telescope.

---

## 19. Correction / demotion ledger additions

Retain all RL72–RL74 corrections. Add:

1. **RL74 determinant-zero deletion hook — repaired interpretation.** In a genuine primitive physical cycle, determinant zero for a nonempty proper pump means the pump already fixes its physical entry state, producing a shorter state repetition. It is excluded by primitivity; do not treat it as the preferred descent branch.
2. **Standalone minimal-counterexample/descent — demoted strategically.** No nondegenerate pump deletion preserving full phase is currently proved.
3. **Raw full-phase residual barrier — strengthened.** Genuine nontrivial full phase has `N==19 mod24`, so the raw residual has magnitude at least `17M`.
4. **Repeated-pump p-adic valuations — do not overpromote.** Much of the high 2-adic/3-adic divisibility of a repeated legal pump follows from local affine integrality; it is not by itself the missing ownership coupling.
5. **`R0=4` — reconnaissance only.** No absolute radius bound is claimed.

---

## 20. Exact proof state after RL75

### New proved analytic mathematics

- physical-drift factorization of the RL74 pump determinant;
- equivalence `D_*=0 <=>` the actual pump fixes its physical entry state;
- primitive proper-pump nondegeneracy `D_*!=0`;
- fixed signs/nondegeneracy for positive `c=10` and `c=101` special pumps;
- exact adjacent-repeat quotient-difference identity;
- full-phase residue refinement `N==19 mod24` for a nontrivial positive cycle.

### New exact finite audit

`verification/verify_rl75_pump_transversality.py` checks the algebra exhaustively over bounded small word/context families, including determinant factorization, degeneracy equivalence, special pump signs and the mod-24 residue synthesis. This is an audit/falsification certificate, not the proof of the infinite statements.

### Strategic changes

- determinant-zero descent is demoted;
- hybrid owned-macro periodicity/packing is ranked first;
- product/CF + modern full phase is retained as deliberate alternative 1;
- global `D|Q` bounded-radius Gate B is retained as deliberate alternative 2;
- two-scale pump Diophantine work is retained as a fourth route, not the default next session.

### Global closure state

Unchanged:

- radius-3 primitive/full-`D` local theorem: **closed local obstruction**;
- Gate A even terminal `k`: **impossible analytically**;
- Gate A terminal `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**, with RL73 giant macro and RL74/RL75 pump interfaces;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.
