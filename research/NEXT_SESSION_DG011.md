# DG011 — Genuine divergent roots on noninitial exceptional records (READY; NOT EXECUTED)

**Execution authority:** The next owner instruction "run next session" executes **DG011 only**. DG010 has been executed; DG012 should be prepared but **not executed** during DG011. Continue the reopened Collatz Descent Gap goal \(E=\varnothing\), not cycle-only research.

Read first: research/THEOREM_TARGET.md; research/sessions/DG009.md; research/sessions/DG010.md; research/PROOF_LEDGER.md; research/OPEN_GAPS.md; research/verification/verify_DG010.py. The known external \(E=o(X)\) result is not \(E=\varnothing\).

## Single priority: produce a genuinely new orbit-wide theorem

Consider an **actual** positive unbounded E-orbit, with increasing suffix-minima \(a_j=x_{t_j}\), gaps \(d_j=t_{j+1}-t_j\), and \(j\ge1\). All these later sources are **nonzero mod 3**. Seek a **divergent** alternative safe inverse root \(z_j<a_j\) of \(b=a_{j+1}\) whose word is **not** merely a prefix prepended to the actual bridge word. Prove it must occur with quantified frequency on **one fixed positive exceptional orbit**, or prove a global contradiction for that orbit. If impossible, prove one mathematically specific structural obstruction or hostile constructive adversary; do not replace this with a larger finite enumeration alone.

DG010 corrections that are binding:
- The four DG009 source-ancestor rows based on 1+u/v and 110+u/v simply reproduce DG003/DG006/DG007 inverses. They are not new globally countable inverse families.
- The remaining DG009 length-15 divergent rows, and DG010's eight more modulo-729 parameter classes, have **3-divisible sources** and so can only address **the first** record transition, never recurrent later records. The DG010 search is limited to inverse words of length \(\le18\), odd count \(7\le s\le12\), and full progression growth \(3^s/2^d>729/512\). It certifies 13/243 parameter classes of each specified original bridge. Never project higher moduli to lower ones.
- DG010 proved a **two-gap first-meeting lemma**: if one certifies \(z_j<a_j\to a_{j+1}\) in \(\ell_j<d_{j-1}+d_j\) safe steps, then the new root is off-spine and first meets the spine within \((t_{j-1},t_{j+1}]\). Same-parity record indices have disjoint windows; at least half the certified indices yield distinct off-spine roots. No automatic disjointness from the older Q2/Q4/Q10 families was proved.
- DG010 also proved **arbitrarily long finite mountain bridges** with words \(w_r=1^{s(r)}0^r\), \(r\ge5,\ r\equiv5\pmod6\), \(s(r)=\min\{s:(3/2)^s>2^r\}\). Every finite prescribed mixed list has arbitrarily large positive seeds divisible by 3 with strictly increasing local endpoints **7 mod 9**, avoiding Q2/Q4/Q10 target classes. These are only finite bridges, not E-members, and do **not** justify bounded gaps or eventual periodicity.

## Required research attacks

1. **Select one candidate forcing mechanism first.** Try pair-of-gap compatibility for noninitial record sources \(1,2\pmod3\), genuinely divergent roots and either a first-meeting invariant or arithmetic recurrence. Derive affine/parity constraints for any gap word and test feasible gaps 3,6,9,11,14,17 and unbounded mountain examples. If a theorem assumes bounded gap length, prove that assumption separately or reject the global upgrade.

2. **Conditional implication, not wishful E membership.** Show every proposed smaller safe root \(z\) really is in E **only** when its target is proven in E, and show whether its first meeting lies in the assigned window. If \(\ell_j\ge d_{j-1}+d_j\), do not invoke the DG010 two-gap lemma. If two root families share possible first-meeting windows, do not add their counts. Prove a bound on distinct roots \(\le X\) explicit in X, and test it against the externally established \(o(X)\) bound, not against a fictitious zero-count claim.

3. **Hostile models.** Attempt to falsify every purported finite-horizon category forcing theorem on exact finite mixed mountain schedules with unbounded gap lengths. Test a coherent 2-adic path that may be impossible for a fixed positive seed; never use nested finite cylinders as proof of infinite ordinary-integer realisation. Seek genuine global constraints on *one fixed orbit*.

4. **Independent bounded-cycle/preperiodic route.** A nontrivial bounded E orbit is eventually periodic; no positive cycle contains a multiple of 3, but a 3-divisible least E integer could conceivably be a *preperiodic* seed below such a cycle. Find an exact theorem excluding this or mark it open. An argument for first unbounded records does not cover this case.

5. **Novelty and proof discipline.** Keep elementary proof, exact finite computation, conjecture, conditional orbit argument, published external results, and Lean/Palomar formalisation distinct. Do not claim a complete Collatz proof or mathematical originality without independent support.

## Exit and deliverables

The target successes are: **A** an unconditional elimination of all least-E multiples of 3 including bounded cases; **B** a positive-integer orbit-wide divergent-root recurrence / global contradiction; **C** an explicit collision-free abundance bound logically inconsistent with \(E=o(X)\). If A/B/C fail, obtain a **proved new structural theorem or constructive adversary** identifying the precise failed mechanism, not an empty status report.

Write research/sessions/DG011.md with proofs, exact counterexamples, tested-verifier details and A/B/C verdict; update research/PROOF_LEDGER.md, research/OPEN_GAPS.md, README.md with only supported changes; prepare the complete research/NEXT_SESSION_DG012.md **READY, NOT EXECUTED**; commit to GitHub and provide exact links. Do not automatically run DG012, claim a GitHub Actions run that did not happen, or claim an infinite exceptional positive integer.
