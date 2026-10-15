# RL72 — Global audit, lemma catalogue, synthesis, closure matrix, and roadmap

Date: 2026-08-24

## 0. Executive conclusion

RL72 was run as the planned **global audit / lemma inventory / synthesis / roadmap** session. The incoming RL71 gate is clean: outer sidecar, fresh internal manifest, and `verification/run_fast_rl71_verifiers.sh` all pass. GitHub `authoritative/` contains the expected RL71 authoritative artifacts, and the historical `sessions/RLXX/` mirrors were used selectively under the verification-economy rule.

The global proof state remains:

- exact radius-3 local obstruction: **closed**, under its exact primitive/full-`D` hypotheses and inherited dependency ledger;
- Gate A: **open globally**;
- Gate B: **open globally**;
- RL / nontrivial-cycle exclusion: **not closed**;
- Collatz conjecture: **not proved**.

However, the audit yields one important closure clarification and two new method-barrier syntheses:

1. **Low-`k` Gate-A sector is already closed by the inherited exact finite certificate.** RL62's independent H<=24 certificate implies that every hypothetical terminal Gate-A violation must have `H>=25`; hence, since a violation has `H<k`, every terminal `k<=25` is excluded. Combined with RL66's analytic elimination of all even `k`, the first globally open terminal exponent is therefore odd `k>=27`. This is an **exact finite-certificate corollary**, not a uniform analytic theorem.
2. **RL19 weighted-difference + RL48 half-rotation/full-phase four-swap collapses exactly to the already-known RL48 proper-factor identity.** It is a coboundary/repackaging, not a new Gate-B contradiction.
3. **RL65's raw full-phase defect numerator can never support a `0<|W|<M` contradiction.** Its quotient is exactly `2-N`; since `N>0` and `N==3 (mod8)`, its absolute value is at least one, so the raw multiple has size at least `M`.

The main remaining obstruction is not another q-digit. It is the absence of an **ownership-sensitive coupling that prices zero-area synchronized depth / active-rank weight**. That missing coupling blocks both the RL48/RL50 defect route and the RL71 residue-floor route.

---

## 1. Verification and provenance

### Current RL71 gate

Fresh RL72 checks:

- RL71 outer sidecar: **PASS**;
- RL71 freshly unpacked internal `SHA256SUMS.txt`: **PASS**;
- `bash verification/run_fast_rl71_verifiers.sh`: **PASS**;
- RL71 fifth-backward-digit verifier: **PASS** with the frozen counts in the incoming ledger.

The first internal-manifest command was issued one directory above the ZIP's top-level bundle directory and therefore returned a path error only. The command was immediately rerun from the actual bundle root and passed. No checksum or mathematical verifier failed.

### GitHub provenance

The connected repository is:

`jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`

GitHub `authoritative/` contains the RL71 ZIP, sidecar, session ledger, mathematics note, fresh-unpack record, and RL72 audit target note. Historical provenance/source mirrors under `sessions/RLXX/` were used for discovery and exact theorem interfaces. Load-bearing historical sources opened in RL72 include RL19, RL20, RL43, RL45, RL47–RL50, RL54, RL61–RL71.

No historical expensive verifier suite was recursively replayed.

---

## 2. Global closure tree after audit

```text
Inherited RL reductions
  |
  +-- Exact radius-3 primitive/full-D case tree ---------------- CLOSED LOCAL THEOREM
  |      |
  |      +-- final cubic skew leaf ------------------------------ CLOSED RL19 analytic
  |
  +-- Retained one-excursion/full-phase architecture
         |
         +-- Gate A: terminal area/valuation H >= k ------------- OPEN UNIFORMLY
         |      |
         |      +-- terminal even k ----------------------------- IMPOSSIBLE analytic (RL66)
         |      +-- terminal k=3 -------------------------------- SAFE analytic (RL67)
         |      +-- terminal k<=25 ------------------------------ SAFE exact finite certificate (RL72 corollary of RL62 H<=24)
         |      +-- first globally open terminal k -------------- odd k>=27
         |      +-- nested g=0 local ladder --------------------- strong compatibility, no contradiction
         |             +-- H>=6 analytic inherited
         |             +-- delta_* mod162, H>=delta_p+c162
         |             +-- delta_*=c162 in any violation k<=165
         |
         +-- Gate B: global RL -> closed obstruction/direct contradiction ---- OPEN
                |
                +-- local endpoint grammar -> radius<=3 -------- DEAD (RL20 countermodel)
                +-- RL48 half-period -> exact radius3 ----------- DEAD (RL49 even-distance identity)
                +-- raw block/proper-factor polynomial ---------- COBoundary / DEAD alone (RL20)
                +-- balanced-return weighted difference -------- OPEN, but raw RL19+RL48 splice collapses (RL72)
                +-- strict-excursion packing -------------------- OPEN
                +-- new non-coboundary ownership bridge -------- OPEN
```

A direct full-phase impossibility theorem could still bypass the Gate-A/Gate-B split, but the obvious raw quotient numerator cannot furnish the required small multiple.

---

## 3. Session coverage map RL18–RL71

This table is deliberately a **current-use map**, not a claim that every historical file was re-proved in RL72. Intermediate sessions whose live content is fully absorbed by a later audited ledger are marked as such.

| Session(s) | Current reusable content / current status |
|---|---|
| RL18 | repaired radius-3 case tree; arbitrary-radius orbit/divisibility identity; dependency audit. Live through RL19/RL61. |
| RL19 | final cubic radius-3 closure; positive lift; arbitrary-rotation weighted difference; weighted populations; state packing; odd-step product. Live. |
| RL20 | exact radius-4 local-grammar countermodel; canonical block coboundary theorem; coprime-6 packing/CF gate; balanced-return and strict-excursion global routes. Live selectively. |
| RL21–RL42 | historical bridge/phase/proper-factor/near-resonance development. Their currently load-bearing interfaces are consumed and restated by RL43/RL45/RL47/RL61. No standalone RL21–42 claim was newly promoted in RL72. |
| RL43 | defect-support compression, one-excursion phase polynomial, short binomial, resultant gateway; finite `e` work. Live as inherited phase/defect interface; finite frontiers remain finite only. |
| RL44 | audit/repair stage feeding RL45; stronger size invariant rejected; current live replacement is RL45 valuation quotient. |
| RL45 | exact `(d,H,J)` Markov quotient; valuation target `J>0 => v2(J)<=K`; finite H certificate. Live. |
| RL46 | exact one-excursion Gate-A reduction `H>=t+3`; terminal geometry/prefix-cap refinements. Live through RL47/RL61. |
| RL47 | exact rank displacement `H=sum(a_j-b_j)`; rank-transport identity; phase coordinate; q-specific exact certificates; separable relaxation inputs. Live, but the relaxation is later barrier-limited. |
| RL48 | separable rank-relaxation barrier; canonical same-root selector; exact full-word reconstruction; four-swap/full-phase pair; rank-defect congruence. Live selectively; direct radius-3 claim later corrected. |
| RL49 | exact half-rotation distance correction; full-phase squeeze; height-one/zero-position telescopes. Direct radius-3 splice dead. |
| RL50 | normalized lifts, height-one shortcut-Collatz conjugacy warning, defect energy, zero-displacement coupling, safe-CF stress refinements. Live structurally; fixed-survivor constants are not uniform. |
| RL51–RL54 | fixed-survivor/defect/terminal reductions; RL54 uniform late-zero reduction is analytic within the fixed safe-CF hypotheses. Not a global Gate-A theorem. |
| RL55–RL58 | aggregate/terminal-tail bootstrap campaign. Retain only claims that survive RL62's correction ledger; no RL72 upgrade. |
| RL59 | decreasing-height terminal potential **false**; dependent mass/tail consequences demoted by RL62. Raw shortcut terminal-ancestor searches remain finite facts. |
| RL60 | fixed-survivor freeze based partly on RL59 route; downstream z-floor/K reductions using false mass premise demoted. |
| RL61 | whole-tree audit baseline: radius3 closed local; Gate A and Gate B global obligations identified; safe-CF survivor correctly classified as restricted subtree. Later corrected by RL62 where it inherited RL59. |
| RL62 | stop-and-repair of RL59 sign error; correct positive potential; H<=24 exact finite certificate in two independent C++ encodings. Live and load-bearing. |
| RL63 | exact synchronized dangerous-cylinder selector; infinite unrestricted all-11 dangerous family; proves local synchronized dynamics alone cannot close Gate A. Live. |
| RL64 | exact **full-phase extendable** ownership definition; all-word cylinders; terminal-owned synchronized equality; all-11 terminal collapse. Live ownership framework. |
| RL65 | `H=sum delta_j`; exact full-phase quotient `(2-N)M=...`; terminal rank-tail factorization and 3-adic selector; even-k terminal synchronized-word split. Live. |
| RL66 | last-active rank; ordered defect recursion; rank-tail digit ladder; analytic elimination of all even terminal `k`. Live. |
| RL67 | at least two active ranks; `H>=3`; analytic `k=3` safety; previous-active interfaces; `J<=2^H` remains conjectural bounded evidence. Live. |
| RL68 | nested `g=0` ordered descent/backward state ladder; nested parity obstruction closed; nested `H>=5`. Live. |
| RL69 | deeper nested state lift; q=3 match; `delta_* mod54`; nested `H>=6`. Live. |
| RL70 | q=4 state/phase match; rigorous `c54` residue floor and exact-value window `k<=57`. Live but compatibility only. |
| RL71 | finite-window backward operator; q=5 match; `delta_* mod162`; floor `H>=delta_p+c162`; exact `delta_*=c162` in any nested violation with odd `k<=165`. Live. |

---

## 4. Global lemma catalogue — current reusable interfaces

### G: global cycle/divisibility identities

**G1 — arbitrary-radius orbit/divisibility identity (RL18).**  
Input: primitive/full parity cycle word, `D=2^A-3^L`.  
Output: standard word numerator condition `D|Q` and equivalent shift/orbit polynomial formulation.  
Status: analytic inherited.  
Consumer: all genuine global Gate-B/direct-full-phase routes.  
Countermodel discrimination: yes, because RL20 radius-4 model has `D∤Q`.

**G2 — positive lift (RL19).**  
`Z=sum_i 2^i3^{-P_i}=(lambda-1)(4R+1)`.  
Status: analytic.  
Use: proves raw positivity of the whole orbit polynomial is tautological, not contradictory.

**G3 — arbitrary-rotation weighted difference (RL19).**  
`sum_i q_i(3^{-G_i}-1)=4(lambda-1)(R_m-R)`.  
Status: analytic.  
Use: live only if combined with information that prevents collapse to the state-difference coboundary.

**G4 — weighted populations/state packing (RL19).**  
`sum_(d_i=1)q_i=3R(lambda-1)`, `sum_(d_i=0)q_i=(R+1)(lambda-1)` plus least-state packing inequalities.  
Status: analytic; numerical consequences may use external least-state floor.

**G5 — odd-step product (RL19).**  
`lambda=prod_(odd phases)(1+1/(3x_i))`.  
Status: analytic.  
Use: radius-independent near-resonance/huge-length dichotomy.

**G6 — canonical gcd-block coboundary (RL20).**  
Normalized block coefficients satisfy `c_j=Xy_(j+1)-Yy_j`; the whole block polynomial telescopes to cycle closure.  
Status: analytic method barrier.  
Use: retire raw block polynomial divisibility as standalone contradiction.

**G7 — balanced-return weighted-difference route (RL20).**  
Input: genuine RL balanced canonical cut.  
Target: nonzero small full-`D` multiple or impossible ordering.  
Status: open programme; RL72 shows the simplest RL19+RL48 half-rotation splice is tautological.

**G8 — strict-excursion packing route (RL20).**  
Input: genuine RL strict canonical excursion plus global divisibility/ownership.  
Target: population/strip-width contradiction.  
Status: open programme.

### R3: exact radius-3 obstruction

**R3.0 — exact primitive radius-3 theorem (RL7–RL19, audited RL61).**  
Input contract: primitive `D`-divisible self-rotations, exact cyclic adjacent-transposition distance 3, and branch-specific support/orientation/gcd hypotheses.  
Output: contradiction.  
Status: closed local theorem; older branches retain explicit external LMN/finite dependencies, final cubic leaf is RL19 analytic.  
Use: immediate contradiction only after *all* hypotheses are manufactured globally.

**R3.dead1 — local grammar bridge (RL20).**  
Status: false/dead route. Exact radius-4 packed countermodel satisfies local envelopes but has `D∤Q`.

**R3.dead2 — RL48 half-period pair (RL49 correction).**  
`dist_cyc(uv,vu)=2(a-t-3+H)`, always even.  
Status: dead route permanently; later phase digits cannot change this word metric.

### A: Gate-A valuation/area core

**A1 — terminal valuation reduction (RL45/RL46).**  
Exact Markov state `(d,H,J)`, `K=H+d(d+1)/2-1`; at terminal `d=1`, Gate A is `v2(J)<=H`.  
Status: analytic reduction.

**A2 — exact finite valuation certificate (RL62).**  
No positive reachable state with `v2(J)>K` through `H<=24`, independently cross-implemented; 8,664,154 states at H=24.  
Status: exact finite certificate, length-independent in the quotient.

**A3 — RL72 low-k corollary.**  
Any terminal violation has `H<k`. If `k<=25`, then `H<=24`, contradicting A2.  
Output: **all terminal k<=25 are Gate-A safe** within the canonical architecture.  
Status: exact finite-certificate corollary.  
This closes an entire low-k terminal sector but is not uniform analytic Gate A.

**A4 — rank displacement identity (RL47/RL65).**  
`H=sum_j delta_j`, `delta_j=a_j-b_j>=0`.  
Status: analytic.  
Use: turns Gate-A area into ordered matched-rank displacement.

**A5 — exact rank-transport identity (RL47).**  
Normalized terminal sum `sum_j (2^{a_j}/3^j)(3-2^{-delta_j})` equals exact terminal target.  
Status: analytic.

**A6 — separable rank-relaxation barrier (RL48).**  
For `z>=42`, the cap/room + total-displacement relaxation necessarily lies above the terminal target.  
Status: analytic method barrier, not a Gate-A counterexample.

**A7 — height-one Collatz conjugacy warning (RL50).**  
Unconstrained synchronized height-one odd-preserving dynamics is shortcut Collatz under `n=(J-1)/2`.  
Status: analytic methodological warning.

**A8 — defect/zero-position coupling (RL49/RL50).**  
Exact zero-position telescoping and, in the relevant safe-CF normalization, `E=sum_j w_j[1-(2/3)^{delta_j}]`; `H` and `E` measure the same displacement vector with different weights.  
Status: analytic, but small numerical E bounds such as `E<5/3` are fixed-survivor, not uniform Gate A.

**A9 — synchronized dangerous cylinders (RL63/RL64).**  
Every local synchronized word has a unique first-even 2-adic entry cylinder and dangerous lifts of arbitrarily high exit valuation.  
Status: analytic.  
Consequence: local synchronized dynamics alone cannot prove Gate A; full-phase extendability must restrict entries.

**A10 — full-phase extendability definition (RL64).**  
Exact existential ownership predicate combining legal internal path, canonical terminal `J=2^k`, full words `u,v`, and `M|Q(v)+4Y`.  
Status: exact RL64 definition; operative ownership framework.

**A11 — terminal synchronized ownership equality (RL64).**  
For terminal synchronized word `w`, `3^s(J_0+1)+2D(w)=2^n(2^k+1)`. For all-11, `3^n q=2^k+1`, so `n<=1+v3(k)` when nonempty.  
Status: analytic.

**A12 — full-phase defect quotient (RL65).**  
`(2-N)M=12 mathcalD+2^(a-k+1)-237*3^r`, with `N>0`, `N==3 mod8`.  
Status: analytic.

**A13 — rank-tail factorization/selectors (RL65–RL71).**  
Terminal synchronized suffix strips powers of 3 from `mathcalD`; successive active ranks determine successive full-phase 3-adic digits.  
Status: analytic ladder; state/phase matches are compatibility, not contradiction.

**A14 — terminal parity and first low-H analytic closures (RL66/RL67).**  
All terminal `k` are odd (RL66); every terminal path has `H>=3`; `k=3` is analytically safe (RL67).  
Status: analytic.

**A15 — nested interface floors (RL68–RL71).**  
Nested `g=0` has exact ordered backward operator; nested `H>=6`; RL71 selects `delta_* mod162` and gives `H>=delta_p+c162`. In any hypothetical nested violation with odd `k<=165`, `delta_*=c162` exactly.  
Status: analytic.

**A16 — finite-window theorem (RL71).**  
Modulo `3^M`, only a bounded latest-rank suffix affects one backward crossing; each extra 3-adic digit exposes at most one earlier rank.  
Status: analytic method theorem.  
Consequence: q=6/q=7 digit extension is expected compatibility unless a downstream theorem consumes those digits.

### B: Gate-B/full-phase bridge interfaces

**B1 — canonical same-root selector (RL48).**  
At the unique common root of `3T^q-2` and `2T^ell-1` modulo `M`, full phase is equivalent to `M|Q(v)+4*3^ell`.  
Status: analytic.

**B2 — exact full-word factorization/four-swap (RL48/RL64).**  
Full phase gives a positive pair `N --u--> N+4 --v--> N`, with `N==3 mod8`, `N+4==7 mod8`.  
Status: analytic under full-phase extendability.

**B3 — half-period radius-3 bridge.**  
Status: dead by RL49 exact even-distance identity.

**B4 — direct phase quotient small-multiple route.**  
Status after RL72: raw numerator is provably too large to yield `0<|W|<M`; any successful direct full-phase contradiction must subtract/normalize additional non-coboundary structure.

---

## 5. Correction and demotion ledger

The following are mandatory and remain in force:

1. **RL59 decreasing-height terminal potential:** false; corrected by RL62 to an increasing-height bound. All dependent terminal-mass consequences remain demoted.
2. **RL61 downstream tail/z-floor entries using the false RL59 mass premise:** demoted, including the derived z-floor column and the then-proved interface to the external K<=129 reduction. Raw shortcut ancestor data remain finite facts.
3. **H<=24:** exact finite certificate only. RL72 uses it to close `k<=25`, but does not call it a uniform analytic theorem.
4. **RL48 separable rank relaxation:** barrier theorem about a method, not falsification of Gate A.
5. **RL49 correction:** the RL48 half-period pair has even cyclic distance; no direct exact-radius-3 invocation.
6. **RL50 height-one conjugacy:** any argument that discards full-phase ownership and solves arbitrary synchronized pumping risks re-embedding shortcut Collatz.
7. **RL64 ownership:** use the exact existential full-phase-extendable definition, not remembered informal ownership language.
8. **State/phase q-digit agreement:** compatibility only.
9. **Local congruence + CRT:** not Gate-A closure; residue classes are not upper bounds.
10. **`J<=2^H`:** conjectural bounded evidence only.
11. **Fixed safe-CF constants (`E<5/3`, strengthened `Zx`, late-tail constants):** remain fixed-survivor only unless separately re-proved uniformly.
12. **Ansari stronger external floor:** remains demoted by RL50's audit; stable accepted floor is the peer-reviewed `2^71` computation where needed.

---

## 6. New RL72 synthesis attempts

### S1 — low-k Gate-A closure from the H<=24 certificate — SUCCESS (finite-certificate sector)

**Candidate.** Combine RL45 terminal valuation reduction with RL62 H<=24 exact certificate.

**Hypotheses.** Canonical terminal path, terminal `d=1`, `J=2^k`, violation `H<k`.

**Derivation.** At terminal, `K=H` and `v2(J)=k`. A violation means `v2(J)>K`. If `k<=25`, then `H<=k-1<=24`, but RL62 certifies that no positive reachable state through H=24 has `v2(J)>K`.

**Conclusion.** Every terminal `k<=25` is Gate-A safe in the canonical architecture. Since RL66 also proves terminal k is odd, the first globally open terminal exponent is odd `k>=27`.

**Classification.** Exact finite-certificate corollary. It closes an infinite set of paths/word lengths for a finite set of terminal exponents; it is not uniform analytic Gate A.

**Reusable lesson.** The finite certificate has more global scope than a q-specific scan because the quotient is independent of excursion length.

---

### S2 — RL19 weighted difference + RL48 half-rotation four-swap — EXACT COLLAPSE / RETIRE RAW ROUTE

Let the full cycle word be `d=uv`, with each half length `a`, weight `ell`, and `zeta=2^a/3^ell`. Full phase gives half-rotation states `N` and `N+4`.

For `0<=j<a`, define

`h_j=P_v(j)-P_u(j)`,

`q_j=2^j 3^(-P_u(j))`.

For the half rotation, the RL19 prefix-flow differences are

`G_j=h_j`, `G_(a+j)=-h_j`,

and

`q_(a+j)=zeta q_j 3^(-h_j)`.

Pairing the two RL19 weighted-difference terms gives exactly

`q_j(3^(-h_j)-1)+q_(a+j)(3^(h_j)-1)`

`=(zeta-1) q_j(1-3^(-h_j))`.

RL19 then yields

`(zeta-1) sum_(j<a) q_j(1-3^(-h_j))`

`=4(zeta^2-1)((N+4)-N)`

`=16(zeta^2-1)`.

Hence

`boxed: sum_(j<a) q_j(1-3^(-h_j))=16(zeta+1).`

But the left side is simply `Z_u-Z_v`, the difference of the two half-word positive lifts. The general lift identity gives

`Z_u-Z_v=4(Q(u)-Q(v))/3^ell`,

and RL48 already proves

`Q(u)-Q(v)=4(2^a+3^ell)`.

Therefore the derived identity is **exactly the RL48 proper-factor identity in RL19 weighted-difference coordinates**.

**Conclusion.** No new divisor/size gap appears. This specific balanced half-rotation synthesis is a state coboundary/repackaging and should be retired unless an additional inequality is introduced that is not already implied by the proper-factor identity.

**Gate-B unit test.** This route uses genuine full phase and therefore is not refuted by the RL20 `D∤Q` radius-4 model; nevertheless it still fails because it is tautological even on genuine full-phase data.

---

### S3 — direct full-phase `D|W`, `0<|W|<D` from the RL65 defect numerator — EXACT SIZE BARRIER

RL65 proves

`W_phase := 12 mathcalD + 2^(a-k+1)-237*3^r = (2-N)M`,

with `M>0`, `N>0`, `N==3 (mod8)`.

Thus `N>=3`. Therefore

`|W_phase|=|2-N|M=(N-2)M>=M`.

If `N=3`, then `|W_phase|=M`; if `N>=11`, then `|W_phase|>=9M`.

**Conclusion.** The raw RL48/RL65 phase-defect numerator can **never** satisfy `0<|W|<M`. Its full-modulus divisibility is exactly quantified by a quotient whose magnitude is already at least one.

**Classification.** New RL72 analytic method barrier / synthesis corollary.

**Reusable lesson.** A direct full-phase impossibility theorem needs a *new normalized residual* obtained after subtracting a genuine state coboundary or exploiting a second independent relation. Reusing the raw phase numerator cannot work.

---

### S4 — RL50 defect energy + RL71 mod-162 residue floor — PRECISE MISSING EDGE

Attempt to combine the weighted displacement defect

`E=sum_j w_j[1-(2/3)^(delta_j)]`

(where its small numerical bound is available only in the fixed safe-CF survivor) with the RL71 nested floor

`H>=delta_p+c162`.

In a hypothetical nested violation with odd `k<=165`, RL71 strengthens this to exact `delta_*=c162`. The last active rank then contributes at least

`w_* [1-(2/3)^(c162)]`

to the weighted defect.

To turn a small-E bound into an area contradiction one therefore needs a **positive lower bound on the normalized active-rank weight `w_*`**, or an aggregate lower bound on the weights of all active ranks.

No such uniform lower bound is currently proved. The available universal prefix estimate is an **upper** cap. RL48's barrier theorem and RL63/RL64 synchronized-cylinder analysis explain the structural reason: zero-area synchronized motion can create arbitrarily many rank/time steps without increasing H, and the local normalized weights can become arbitrarily small unless full-phase ownership supplies a new restriction.

**Conclusion.** The synthesis does not close Gate A. The exact missing edge is now explicit: an ownership-sensitive zero-area-depth/active-weight theorem.

**Classification.** Exact failure diagnosis, not an impossibility theorem for all future defect arguments.

---

### S5 — low-k exact `delta_*=c162` + terminal-tail state residues — LOCAL MODULUS CANNOT CONTROL ZERO-AREA DEPTH

RL71 gives exact `delta_*=c162` in any nested violation with odd `k<=165`. A natural idea is to combine this with terminal `R mod243` and the inherited tail classes.

The obstruction is clearest for an all-`00` terminal synchronized suffix. RL65 gives the exact local entry

`R=2^n(2^k-1)+1`.

Modulo `243`, `2` has order `162`. Therefore the local terminal state residue satisfies

`R(n+162) == R(n) (mod243)`.

Thus the RL71 mod-243 / mod-162 terminal selector sees terminal all-`00` depth only modulo 162. The physical entry can grow enormously while the local residue repeats, and the synchronized suffix contributes zero area H.

This is not a construction of full-phase completions for arbitrary `n+162`; the full denominator changes and ownership may exclude them. It is a method limitation: **the local mod-243 selector itself cannot bound zero-area terminal depth.** Any low-k closure must invoke the global full-phase denominator/ownership or another nonlocal size relation.

**Conclusion.** The low-k exact-value theorem remains valuable, but by itself cannot close the all-`00`/mixed depth freedom.

---

## 7. Closure matrix after RL72

| Object / sector | Status | Evidence type | What is still needed |
|---|---|---|---|
| Exact primitive radius-3 tree | CLOSED | analytic + inherited external/finite dependencies | only a valid global bridge to invoke it |
| RL19 final cubic radius-3 leaf | CLOSED | analytic | none |
| Local-grammar -> radius<=3 | DEAD route | exact finite countermodel | stronger global hypothesis required |
| RL48 half-period -> radius3 | DEAD route | analytic even-distance identity | different owned pair/construction required |
| Gate A, terminal even k | CLOSED / impossible | analytic RL66 | none |
| Gate A, k=3 | CLOSED | analytic RL67 | none |
| Gate A, all k<=25 | CLOSED within canonical architecture | exact finite-certificate corollary | no analytic upgrade claimed |
| Gate A, first open terminal exponent | odd k>=27 | open | ownership-sensitive coupling |
| Nested g=0, k<=165 hypothetical violation | `delta_*=c162` exact | analytic RL71 | contradiction with full phase/area/tail still missing |
| Nested g=0 generally | strong state/phase compatibility | analytic | size/order/ownership contradiction |
| Safe-CF fixed survivor | restricted stress object; prior RL59 mass route repaired/demoted | mixed | not equivalent to global Gate A |
| Gate B balanced-return raw half-rotation splice | RETIRED as tautology | RL72 analytic synthesis | non-coboundary residual needed |
| Gate B strict-excursion packing | OPEN | programme | genuine full-D quantitative packing theorem |
| Raw full-phase phase-defect small-multiple route | RETIRED in raw form | RL72 analytic size barrier | subtract/normalize extra independent structure |
| Gate B globally | OPEN | — | exhaustive owned bridge or direct contradiction |
| RL closure | OPEN | — | Gate A + Gate B or stronger bypass theorem |

---

## 8. Updated dependency DAG

```text
RL18/RL19 global D|Q + weighted identities
        |                            \
        |                             \--> exact radius-3 local theorem -------- CLOSED
        |                                      ^
        |                                      |
        +--> RL20 countermodel ----------------+-- says any bridge must use global ownership
        |
        +--> RL20 balanced/strict global routes ------------------------------- OPEN

RL43 phase/defect ----> RL45 valuation quotient ----> RL47 rank displacement/transport
                                  |                              |
                                  |                              +--> RL48 separable barrier
                                  |
                                  +--> RL62 H<=24 certificate --> RL72 k<=25 closure

RL48 same-root/full-word ----> RL49 correction/telescopes ----> RL50 defect/conjugacy
            |
            +--> RL64 exact full-phase ownership
                    |
                    +--> RL65 defect quotient/rank tail
                           |
                           +--> RL66 last active / odd k
                                  |
                                  +--> RL67 H>=3 / previous active
                                         |
                                         +--> RL68-RL71 nested backward finite-window ladder
                                                |
                                                +--> delta_* mod162 + area floor
                                                |
                                                +--> [MISSING EDGE]
                                                     ownership-sensitive zero-area depth / size coupling
                                                     |
                                                     +--> desired uniform Gate A

Gate B direct full-phase path:
RL48/RL64 full phase + RL19/RL20 global identities
        |
        +--> half-rotation weighted diff ---- RL72: tautological collapse
        +--> raw phase numerator ------------ RL72: quotient-size barrier
        +--> [MISSING] non-coboundary owned residual / strict packing theorem
```

---

## 9. Ranked roadmap — only three primary targets

### Target 1 — Full-phase zero-area depth / active-weight coupling (highest leverage)

**Exact theorem target.** Prove a quantitative restriction, under RL64 full-phase extendability, on zero-area synchronized pumping at fixed H. A sufficient form would bound the number/placement of zero-displacement ranks before/after the last active ranks, or give a positive lower bound on the normalized weights of the active ranks in terms of `(H,k)`.

**Why global leverage.** This is the precise missing edge in S4/S5. It would let the RL50 defect/zero-position machinery and RL71 residue floors become size inequalities rather than compatible residues. It also prevents the proof from degenerating into unrestricted shortcut-Collatz dynamics.

**Already proved prerequisites.** RL63 local cylinder obstruction; RL64 exact ownership definition; RL65–RL71 ordered rank-tail/finite-window selectors; RL48 separable barrier.

**Smallest missing step.** Translate full-phase divisibility `M|Q(v)+4Y` into a restriction on a maximal synchronized zero-area macro entry/length that is not already a local affine identity.

**Red-team.** Reject immediately if the proposed bound remains true/false without using full phase, or if it reduces to arbitrary height-one shortcut Collatz. Test against RL63 all-word cylinders and RL48 separable witnesses.

**What closes if proved strongly enough.** Potentially Gate A globally; at minimum it could close an infinite tail/interface family.

**Stop/pivot.** If every candidate inequality can be satisfied by an exact full-phase-owned long synchronized macro or reduces to a coboundary, pivot to Target 3.

### Target 2 — Nested low-k exact-value closure for `27<=k<=165`

**Exact theorem target.** In a hypothetical nested violation with odd `27<=k<=165`, use `delta_*=c162` exactly plus the four terminal tail classes and earlier-rank area/order constraints to prove

`delta_p+c162 >= k`

or an equivalent contradiction.

**Why leverage.** RL72 has already closed `k<=25`; this is now the first finite exponent band not covered by the quotient certificate, and RL71 supplies exact—not merely congruential—last-active displacement throughout it.

**Prerequisites.** RL66 odd k; RL68–RL71 nested interface, mod162 selector, residue floor; exact tail formulas; RL64 ownership.

**Smallest missing step.** Remove the all-`00`/mixed zero-area depth freedom by one global ownership or order inequality. Pure mod243/CRT is insufficient by S5.

**Red-team.** Any proof using only `R mod243`, parity, and `delta_*=c162` must be rejected unless it also controls the global denominator or synchronized depth.

**What closes if proved.** Entire nested Gate-A sector for `k<=165`; not separated/cross or all Gate A.

**Stop/pivot.** If the only obstruction remains unbounded synchronized depth after exact tail splitting, merge this target back into Target 1.

### Target 3 — Non-coboundary Gate-B residual / strict-excursion theorem

**Exact theorem target.** From a genuine full-`D` owned balanced return or strict excursion, derive a new integer `W` such that

`D|W`, `0<|W|<D`,

or manufacture two rotations satisfying every exact radius-3 input contract.

**Why leverage.** Radius 3 is already closed. A valid exhaustive bridge closes Gate B.

**Prerequisites.** RL18/RL19 global identities; RL20 countermodel and coboundary theorem; RL48/RL64 full-phase ownership.

**Smallest missing step.** Subtract the exact state coboundary before taking divisibility, so the residual is not merely `D*(state difference)` and not the RL65 raw phase quotient.

**Red-team.** Reject if it holds in the RL20 `D∤Q` radius-4 countermodel, if it collapses to S2's proper-factor identity, or if its quotient is an integer of magnitude >=1 as in S3.

**What closes if proved.** Gate B if exhaustive; otherwise a major global branch.

**Stop/pivot.** If every candidate normalization is an exact coboundary/proper-factor restatement, focus research on Target 1 rather than inventing further radius ladders.

---

## 10. Final authoritative proof state after RL72

New RL72 upgrades are limited to:

1. **Exact finite-certificate corollary:** all terminal Gate-A cases `k<=25` are closed within the canonical architecture; therefore any Gate-A counterexample must have `H>=25` and odd `k>=27`.
2. **Analytic synthesis barrier:** the RL19 weighted-difference identity on the RL48 half-rotation four-swap pair collapses exactly to RL48's proper-factor identity and supplies no new contradiction.
3. **Analytic synthesis barrier:** the raw RL65 full-phase defect numerator is `(2-N)M`, so its absolute value is always at least `M`; it cannot be the desired small nonzero multiple.
4. **Exact failure localization:** residue-floor/defect and low-k mod162 routes both currently fail at the same missing global interface—ownership-sensitive control of zero-area synchronized depth / active-rank weight.

Everything else retains its inherited classification. In particular:

- Gate A remains open for odd `k>=27` globally;
- nested `g=0` remains open despite mod162 exact-value information;
- Gate B remains open;
- no RL closure or Collatz proof is claimed.

---

## 11. Recommended next-session kickoff

The next session should **not** be a q=6 extension by default. Start from Target 1: translate RL64 full-phase divisibility into a quantitative restriction on zero-area synchronized macro depth or active-rank weights. Use the newly clarified first open exponent `k>=27` as a stress regime, and use the nested `27<=k<=165` exact-value window as the first concrete theorem laboratory.

In parallel, one Gate-B experiment is permitted: search for a non-coboundary balanced-return/strict-excursion residual. Apply the RL72 S2/S3 tests immediately; if the expression reduces to a proper-factor/state-difference identity or has quotient magnitude >=1, retire it without further polishing.
