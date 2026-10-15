# DG003 — cross-depth restrictions for genuinely integer-realised nonperiodic survival (EXECUTED 2026-10-15; historical invocation prompt)

**Execution record:** [DG003 result and proof](sessions/DG003.md); [DG004 is the next unexecuted prompt](NEXT_SESSION_DG004.md). Instructions below are retained as the historical DG003 invocation text. They do not authorise DG004.

**Owner instruction to run this named session suffices; do not request confirmation.** Execute DG003 only. No automatic DG004.

Read, in order: research/THEOREM_TARGET.md, research/PROOF_LEDGER.md, research/OPEN_GAPS.md, research/sessions/DG002.md, and (as needed) research/sessions/DG001.md. DG002 proved exact block congruence (D^t divides (D-A)x-q), expanding-block integer growth, shifted run inequalities, positive eventual-periodic itinerary => cycle, a nonperiodic 2-adic non-realisation example, and the necessary all-prefix odd-count bound. These are **not** a proof that E is empty; the only target remains Terras–Everett almost-all descent to all-positive-integer descent.

**Sole mathematical goal:** find a *new, non-circular, infinite-horizon restriction on an actual fixed positive integer n in E*, ideally eliminate an explicitly stated numerical or dynamical subclass of E not already discharged by a finite-prefix descent check. Work beyond merely excluding fake 2-adic itineraries.

Mandatory attacks (attempt more than one substantial proposition):
1. Combine DG002's **exact** affine prefix at depth J, T^J(n)=(3^{s_J}n+q_J)/2^J, with its shifted expanding-block congruence (2^{mt} divides (2^m-A)T^J(n)-q). Seek arithmetic restrictions on a single integer n across distinct depths J, not merely generic real growth bounds. Test a nonperiodic sequence of varying blocks, including patterns with short or no long periodic runs.
2. Try a least-exception n=min E argument using odd-prefix balance and the exact first failure of an expanding block. Do **not** infer T^J(n) is in E, and do not assume that the inverse Collatz tree propagates exceptions.
3. Look for a theorem that rules out a **concrete infinite family of positive starting values from E** by a common argument stronger than checking each value's finite descent. Specify exactly how it improves what is known. If none is available, prove a sharp obstruction explaining why DG002's inequalities cannot do this.
4. Actively falsify tempting lemmas: n=2^k t-1 (arbitrarily long odd prefixes), n=8^t-5 (arbitrarily long surviving mixed prefixes), an explicit compatible supercritical but positive-integer-free nonperiodic path from DG002, finite residue cylinders, and real/negative/2-adic rational countermodels. Check exact arithmetic independently where feasible.
5. Keep density zero vs emptiness distinct; prove the integer realisation step if invoking it. No cycle-only pivot, no giant computation as surrogate proof, no invented novelty, no Lean/Palomar certification claims without running them.

Deliver research/sessions/DG003.md with exact statements, proofs and failed implications; update research/PROOF_LEDGER.md and research/OPEN_GAPS.md, add an executable checker if meaningful; draft the **complete** DG004 handoff without executing it. Close with proved claims, killed claims, still-open E=empty gap and precise GitHub commit/file URLs. No forced audits, countdowns or process padding.
