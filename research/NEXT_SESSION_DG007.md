# DG007 — eliminate or constrain a genuine all-1-mod-3 exceptional record tail (READY; NOT EXECUTED)

**Direct authority:** The owner's next instruction to run a session executes **DG007** immediately; do not require a second confirmation. It does not authorise DG008. Work solely on the Terras–Everett exceptional-set gap \(E=\varnothing\) for the shortened positive Collatz map. Do not pivot to cycle-only results, unrelated Collatz variations, generic parity-sequence enumeration divorced from a fixed positive seed, process audits, huge stopping-time brute force, or an inference from zero density to emptiness.

**Read first:** research/THEOREM_TARGET.md; research/sessions/DG006.md; research/PROOF_LEDGER.md; research/OPEN_GAPS.md; consult DG003–DG005 for precise hypotheses. All positive-unbounded-orbit statements are conditional; bounded exceptional orbits remain an independent possibility.

## Exact inherited mathematics

DG006 proved: an actual unbounded \(E\)-orbit has exceptional, strictly increasing suffix records \(a_j\equiv3\bmod4\). Gaps \(2,4,5\) cannot occur. Gap \(3\) is exactly the local \(110\) shape \(a=27+32h\to b=31+36h\), always \(b\equiv1\bmod3\). Gap \(6\) has only the finite bridge word shapes \(111010\) (\(a=71+256h,b=91+324h,b\equiv1\bmod3\)) and \(111100\) (\(a=207+256h,b=263+324h,b\equiv2\bmod3\)). No finite bridge is asserted to have \(E\) endpoints. Every long-gap target \(b\equiv2\bmod3\) produces \(r=v_3(b+1)\) distinct exceptional odd roots
\(z_i=2^i(b+1)/3^i-1<a_j\), outside the spine, with disjoint chains for distinct targets, giving
\[
|E\cap[2,X]|\ge R(X)+
\sum_{\substack{j:a_{j+1}\le X\\d_j\ge3,\ a_{j+1}\equiv2\ (3)}}v_3(a_{j+1}+1).
\]
There is no lower bound on the sum. First long gap from \(m=\min E\) cannot target \(2\bmod3\), but later ones might.

The actual finite family \(n_r=12\cdot8^r-5\) follows \(r\) consecutive local record bridges \(110\), with all finite records \(1\bmod3\). Every fixed \(r\) is realised by a *different* positive seed; an infinite eventually-\(110\) tail would force a positive integer to equal \(-5\), impossible. The remaining obstruction is **varying nonperiodic bridges in one fixed positive integer orbit**; arbitrary finite bridge constructions do not resolve it.

## Single main target

Try proving either:
(A) an unbounded *genuine* exceptional record tail with finitely many long-gap \(2\bmod3\) targets is impossible; **or**
(B) the weighted off-spine safe-ancestor count is at least \(cX\) along an unbounded \(E\)-orbit for some \(c>0\), contradicting Terras–Everett; **or**
(C) a valid new positive-integer elimination theorem on a nontrivial residue family of the least or of all exceptional integers, without smuggling in the conjecture.

Partial rigorous theorems are welcome; do not pretend finite classifications close the target.

## Executable proof attempts (attack and falsify)

1. **Global coupling of bridge words.** Develop the exact affine transition maps at all locally admissible lengths \(d=3,\ldots,12\), including parity-cylinder congruences \(a\bmod 2^{d+2}\), intermediate \(>b\), and mod-3 type of \(b\). Classify all \(d=7,8,9\) first. Prove any transition restrictions that survive *concatenation* in the same positive-integer orbit, not just independently feasible rows. Does a hypothetical eventually-all-\(1\bmod3\) chain need infinitely many geometrically distinct bridge words? Could it still be nonperiodic? Do not mistake a 2-adic path for a positive integer.
2. **First-entry inverse forest beyond odd-only chains.** Starting at a genuine long-gap target \(b\), enumerate finite safe inverse words (including temporary even-inverse expansions) leading to **smaller** positive roots. Prove exactly when they are in \(E\), and whether their first meeting with the original orbit is \(b\). Prove collision disjointness by first entrance before counting; compare with DG006's \(v_3(b+1)\) bound. Explicitly investigate \(b\equiv1\bmod3\), the uncounted case.
3. **Least-exception first-transition gate.** Assume \(m=\min E\) and its orbit unbounded. Use \(m\equiv0,1\bmod3\), the DG006 exclusion of first long-gap \(2\bmod3\) targets, and actual bridge endpoints to test whether the first record transition is forced into a strictly smaller set of positive integer cylinders. Any assertion that a finite endpoint lies in \(E\) must have a legitimate infinite-tail reason.
4. **Genuine weighted abundance or a killer model.** Either derive an explicit quantitative lower bound for the weighted roots
   \(\sum v_3(b+1)\) along the *actual* record chain, or construct precise arbitrarily long *finite* positive-integer bridge chains defeating proposed lower bounds. If presenting an abstract schedule, state separately that it is not an orbit. Any density claim must compare \(|E\cap[2,X]|\) with \(o(X)\), not only with \(O(\log X)\).
5. **Realisation and falsification.** For proposed endless bridge-pattern rules, write the exact congruences for one fixed positive starting integer and show where real integer realisation fails or survives. Regress examples from DG006 (including \(763\to859\to967\), \(207\to263\), \(2815\to3383\) and the two odd predecessors \(2255,1503\)), alongside \(2^k t-1\), \(8^t-5\), and DG005 whole descent progressions \(k=2,\ldots,7\). Test only finite scopes with exact arithmetic; no statistical conjecture promotion.

## Deliver and close

Write research/sessions/DG007.md with complete proofs, counterexamples, precise conditional scope and a candid E-consequence; update research/PROOF_LEDGER.md and OPEN_GAPS.md with genuine changes; commit any executable bounded checker actually run; draft the **full DG008 successor prompt** but do not execute it. Include exact verification commands/output and verified GitHub links. No forced audit or extra owner confirmation.
