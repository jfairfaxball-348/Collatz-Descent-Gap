# DG012 — Fixed-seed consistency of infinite mountain-record chains (READY; NOT EXECUTED)

**Execution authority:** A subsequent owner instruction "run next session" executes **DG012 only**. DG011 has been executed; **do not execute DG013** during DG012. Maintain the sole research goal \(E=\varnothing\) for shortened Collatz \(T(2x)=x,\ T(2x+1)=3x+2\). No density-zero-to-empty or finite-to-infinite shortcut is allowed.

## Read first

- research/THEOREM_TARGET.md, research/sessions/DG010.md, research/sessions/DG011.md;
- research/PROOF_LEDGER.md, research/OPEN_GAPS.md;
- research/verification/verify_DG010.py, verify_DG011.py;
- research/sessions/DG009.md §C for earlier long-run 2-adic nonrealisation.

DG011 proved: (i) any *expanding* inverse word hitting b=7(mod9) requires ≥7 odd steps, and this is sharp; (ii) arbitrary **finite** prescribed 3-adic endpoint lifts inside 7(mod9) occur in real positive integer mountain bridge concatenations; (iii) an all-odd run of length s starting at global time t on a **fixed positive integer** obeys \(2^s\le(3/2)^t(n+1)\), giving an explicit non-realisable infinite growing mountain schedule. These are **not** an E-orbit recurrence or a Collatz proof.

## ONE primary mathematical target: real positive infinite mountain sequences

Investigate whether **any** fixed ordinary positive integer n can have an infinite actual suffix-record tail consisting entirely of strict mountain bridge words \(w_r=1^{s(r)}0^r\), \(r\ge5,\ r=5\bmod6\), \(s(r)=\min\{s:(3/2)^s>2^r\}\), rather than DG011's deliberately fast-growing r_j. Prove an obstruction for a *genuinely wider* explicitly quantified infinite class of varying r_j, or exhibit a necessary arithmetic criterion that rules out a new class on one fixed n. This is a proper subproblem of \(E=\varnothing\), not a replacement target.

Mandatory proof attack, in order:

1. **Exact all-time divisibility.** For each mountain bridge at global time \(t_j\) write the full affine map, parity cylinder, \(2^{s_j}\mid(x_{t_j}+1)\), and growth budget. Seek constraints coupling *successive* r values beyond the trivial individual bound \(2^{s_j}\le(3/2)^{t_j}(n+1)\). Work algebraically with \(x_{t_j+1}\), 3-adic endpoints \(-2^{-r_j}\), and 2-adic next odd-run congruences. Distinguish an independent cylinder tautology from a true cross-time arithmetic constraint (DG003 warns of this).

2. **Force or falsify an eventual contradiction.** Attempt explicit hypotheses weaker than \(r_j\ge t_j\) (for example, \(r_j\) proportional to earlier total length or a conditional lower bound on \(\max_{i\le j}r_i\)), and derive a **rigorous** sharp threshold for failure of fixed-positive-seed realisability. If all candidate inequalities are compatible with genuinely varying infinite lists, state a falsifying 2-adic/finite positive schedule and precisely why fixed-integer realisability remains unknown.

3. **Connect to the actual E target.** Determine whether the new necessary arithmetic restriction could follow *unconditionally* from the suffix-minimum geometry of an actual orbit in E. Do not impose a mountain-only hypothesis on all genuine records or assume bounded gaps. If a theorem covers only the mountain subclass, say exactly so. A root claimed in E must reach a proven E endpoint with a safe finite trajectory. A new off-spine count requires a proven first-meeting window and disjointness, and a contradiction with \(o(X)\) requires a quantitative lower bound, not merely infinitely many roots.

4. **Secondary bounded-cycle gate, only after genuine primary proof attempts.** Analyze the preperiodic least-E multiple of 3 scenario below a nontrivial cycle. Give an exact new exclusion or explicitly retain the possibility; ruling out 3-divisible cycle *members* is insufficient.

## Adversarial checks

- Re-run the DG011 s≤6 shield; note that its sharp witness w=11111101000 has s=7, d=11, so strict-safe inverse paths to b=7(mod9) shorter than 11 steps cannot exist. In particular DG010's two-gap window bound cannot be used there when \(d_{j-1}+d_j\le11\). Test this corollary on feasible lengths 3,6,9,11,14,17 and do not assert general bounded gaps.
- Reproduce the exact r_j schedule first terms \((0,5,9),(14,17,30),(61,65,112),(238,239,409)\). Check both the odd-run budget and the numerical inequalities independently.
- For any computational search beyond a manageable local test, provide a deterministic script and optionally configure GitHub Actions; do not claim a remote run unless the actual run and status are inspected.
- Finite positive prefixes, compatible 2-adic cylinders, and bounded exhaustive checks do not prove one ordinary integer orbit exists forever. Do not claim mathematical novelty without checking sources.

## Exit / deliverables

Prefer one of (A) genuine new fixed-positive-orbit prohibition for a meaningful infinite mountain class; (B) a strong arithmetic criterion coupling consecutive genuine record gaps that is not equivalent to a single parity cylinder; (C) an unconditional bounded/preperiodic least-E exclusion. If none succeeds, deliver one **proved specific falsification** of the leading proposed mechanism, with full equations and finite witnesses.

Write research/sessions/DG012.md with clear proofs, falsified statements, test evidence, and A/B/C verdict. Add a standalone exact verifier if appropriate. Update research/PROOF_LEDGER.md, research/OPEN_GAPS.md, and README.md without overstating scope. Create research/NEXT_SESSION_DG013.md **READY, NOT EXECUTED**, commit changes, and link exact artifacts. Do not run DG013 automatically.
