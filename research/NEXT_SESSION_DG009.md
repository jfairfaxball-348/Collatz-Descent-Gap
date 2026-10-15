# DG009 — force recurrence of inverse-generating exceptional records, or kill its proposed mechanism (EXECUTED; historical prompt)

**Execution status:** DG009 was authorised and executed on 2026-10-15. This is the preserved historical execution prompt, not the active handoff. Results: [sessions/DG009.md](sessions/DG009.md). Active next prompt: [NEXT_SESSION_DG010.md](NEXT_SESSION_DG010.md), READY but NOT EXECUTED. DG008 was executed previously.

**Read first:** research/THEOREM_TARGET.md; research/sessions/DG008.md; research/sessions/DG007.md; research/PROOF_LEDGER.md; research/OPEN_GAPS.md; research/verification/verify_DG008.py. Target remains **E=empty** for the positive shortened Collatz map, not a cycle-only theorem, finite parity-cylinder classification, or 2-adic non-realisation alone. Distinguish actual E-orbit tail minima, finite local bridges, candidate least-E residue locations, and external natural-density-zero theorems.

## Exact inherited status

DG008 has ruled out exceptional-record gaps 13, 15, 16, 18 in addition to 2,4,5,7,8,10,12. It identified 113 finite bridge words at gap14 and 525 at gap17; those are NOT E-orbits. The strict-prefix safe-inverse sieve excludes 82429 of 177147 possible odd residue *locations of min E* using words length≤17 with ≤11 odd steps; this does not apply to all E. The new E-safe \(111010\) inverse of \(b\equiv10\bmod81\) yields a disjoint off-spine root if a genuine target follows a gap≥9. Thus the proven conditional E-count is
\[
|E\cap[2,X]|\ge R(X)+\sum_{d_j\ge3,\ a_{j+1}\equiv2(3),\ a_{j+1}\le X}v_3(a_{j+1}+1)+Q_4(X)+Q_{10}(X).
\]
**No positive lower frequency** of the three added terms exists. In addition DG008's *real positive finite* arbitrary mixed gap-9 schedules from \(u=111011010,\ v=111101010\), with starting seed \(0\bmod3\), keep every target in residue 37 or 28 mod81. Hence any **finite-schedule** necessity of 2mod3, 4mod9 or 10mod81 targets is false. They do not construct an *infinite* exceptional orbit.

## Single priority: a global genuine-orbit theorem

Attempt to establish, for **one fixed positive starting integer \(n\in E\)** whose orbit is unbounded, a recurrence or obstruction genuinely incompatible with perpetual avoidance of the inverse-generating record categories:
\[
a_{j+1}\equiv2\pmod3,\qquad
d_j\ge6,\ a_{j+1}\equiv4\pmod9,\qquad
d_j\ge9,\ a_{j+1}\equiv10\pmod{81}.
\]

**Success A:** prove every such exceptional record tail must hit at least one of the three categories infinitely often, by a non-circular argument using exact integer realisation, cross-gap arithmetic and real orbit inequalities. This is *not sufficient* to contradict density zero; say so, and then seek a rigorous quantitative frequency bound.

**Success B:** derive a structural bound on distinct safe off-spine E-roots per exceptional record that forces \(|E\cap[2,X]|\not=o(X)\); establish collision-freeness by **first meeting with the actual orbit**, and track root size \(\le X\).

**Success C:** prove an independent obstruction for any actual positive exceptional seed divisible by 3 (the current inverse sieve is powerless there), with a theorem valid even if the candidate lies on a bounded cycle.

If none succeeds, supply a *precise negative theorem / adversarial integer family* identifying why the proposed approach cannot imply E=empty, not merely a list of unsuccessful searches.

## Mandatory attacks

1. **Focus on 28/37 mod81.** Study genuine conditional record chains whose long targets all fall in these two classes. For the two viable length-nine blocks \(u,v\), compute exact cross-block coefficients and integer-realisation restrictions on a **single fixed** seed; try proving infinite mixed \(u,v\) schedules cannot occur in one ordinary positive integer, without mistaking 2-adic uniqueness for positive-integer exclusion. Explicitly allow unbounded gaps outside the two-word alphabet unless separately prohibited.
2. **Improve inverse branch coverage without collisions.** Search safe ancestors of 28/37 mod81 targets, using longer words or competing words, and prove any purported extra E-root is (i) a true positive integer, (ii) safe up to its E endpoint, (iii) outside the original orbit, and (iv) distinct from prior roots. If a residue class can only be covered after additional 3-adic digits, state the exact modulus, not an illicit projection. Attempt a local “all long gaps produce extra roots” lemma, and falsify it against gap6 and gap9 families.
3. **Attack least-E divisible by 3 directly.** Since any multiple of 3 has only larger inverse ancestors, do not attempt to extend the shrinking-inverse sieve mechanically. Instead examine the *first actual exceptional record transition* from \(m=\min E\equiv0\bmod3\) and whether the E-membership of the next record creates a distinct certified E-seed below m; allow all viable first-gap lengths including arbitrarily large ones. A certificate that assumes the target is in E is allowed for a conditional least-element contradiction, but may not be advertised as an all-E congruence exclusion.
4. **Adversarial finite models.** Test any new claim against arbitrary finite concatenations of \(u,v\), with initial seed \(0\bmod3\) and strictly valid local bridge inequalities; test mixed gap1/3 schedules and a genuinely varying infinite *2-adic* cylinder for potential false positive-integer-realisation inference. If an attempted universal bound is really fixed-length, explicitly restrict its quantifiers.
5. **Quantitative falsification.** For any proposed density contradiction, exhibit the precise number and size of distinct roots below X that the proof forces and compare to \(o(X)\). A sparse set with \(O(\log X)\), \(O((\log X)^k)\) or unspecified root growth remains possible. Bounded hypothetical exceptional cycles remain live until directly addressed.

## Deliver and close

- Write research/sessions/DG009.md with exact statements, complete proofs, counterexamples, and outcome of the single global-orbit priority. Mark clearly which results hold for all E, for min E, conditionally for unbounded exceptional orbits, or just for finite bridges.
- Add and **run** an exact verifier if useful (no massive brute-force masquerading as an infinite result), update research/PROOF_LEDGER.md and research/OPEN_GAPS.md, and update the README index.
- Draft the **full** research/NEXT_SESSION_DG010.md, marking it READY but NOT EXECUTED; do not run DG010.
- Commit everything and give verified GitHub file and commit links. No forced audits, session countdowns, unearned mathematical novelty or Lean/Palomar claims. **Only declare E empty if a complete universal proof is actually obtained.**
