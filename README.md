# Collatz Descent Gap Programme

**Reopened: 15 October 2026. Status: ACTIVE — conjecture OPEN.**

The sole target is to bridge the Terras–Everett theorem that almost all positive integers eventually descend below their starting value to the assertion that **every integer n>1 does**. This is equivalent to the Collatz conjecture, but the research stays strictly on the gap between density-zero exceptions and no exceptions.

For the shortened map T(n)=n/2 for even n, T(n)=(3n+1)/2 for odd n, define
\[
E=\{n\ge2:\ T^k(n)\ge n\text{ for all }k\ge1\}.
\]
**Known externally:** E has natural density zero (Terras 1976, Everett 1977). **Unknown:** E is empty.

## Start working here

1. [Exact target and definitions](research/THEOREM_TARGET.md).
2. [Active proof/evidence ledger](research/PROOF_LEDGER.md).
3. [Open logical gaps](research/OPEN_GAPS.md).
4. [DG001 — baseline mathematical results](research/sessions/DG001.md).
5. [DG002 — integer-realisation obstruction, sharp mixed-prefix counterexamples and exact verifier](research/sessions/DG002.md).
6. [DG003 — exact cross-depth collapse, least-exception inverse sieve and tail minima](research/sessions/DG003.md).
7. [DG004 — deeper least-E inverse sieve and quantitative exceptional tail minima](research/sessions/DG004.md).
8. [DG005 — actual-tail-minimum geometry, off-orbit inverse root and unbounded-depth descent progressions](research/sessions/DG005.md).
9. [DG006 — exact record bridge gaps, all-1-mod-3 finite stress tests, weighted disjoint inverse chains](research/sessions/DG006.md).
10. [DG007 — new least-E residue exclusions, safe 1-mod-3 ancestor roots and exact gap sieve](research/sessions/DG007.md).
11. [DG008 — gap lengths 13–18, depth-17 safe inverse classes, 10-mod-81 branch and mixed finite obstruction](research/sessions/DG008.md).
12. [DG009 — six conditional first-record inverse-root obstructions and an infinite non-integer 2-adic mixed schedule](research/sessions/DG009.md).
13. [DG010 — all-length finite bridge adversary, divergent 3-adic first-record roots, two-gap collision lemma](research/sessions/DG010.md).
14. [DG011 — sharp seven-odd-step mod-9 inverse shield, finite 3-adic mountain interpolation, fixed-orbit odd-run budget](research/sessions/DG011.md).
15. [DG012 — bridge-index odd-run budget, repeated-word divisibility and theorem barring EVERY eventually nondecreasing infinite mountain itinerary on a fixed positive orbit](research/sessions/DG012.md).
16. [DG013 — oscillating paired mountains, general repeated-superword budget, and logarithmic staircase nonrealisation](research/sessions/DG013.md).
17. [DG014 — square-free mountain obstruction to symbolic repetition forcing, sharp local 3/2 ceiling and conditional cycle precursor](research/sessions/DG014.md).
18. [Next research session: DG015 — fixed-positive integer realisation beyond square-free schedules](research/NEXT_SESSION_DG015.md) (READY; NOT EXECUTED).

The [research plan](research/RESEARCH_PLAN.md), [sources](research/SOURCES.md), and [lightweight protocol](research/SESSION_PROTOCOL.md) explain scope and verification. A named session prompt is an instruction to run that session, not merely to prepare it.

## What was retained from the prior programme?

The repository previously pursued hundreds of sessions on excluding non-trivial Collatz **cycles**. There are significant analytic reductions, computational verifiers, explicit countermodels, correction records, and extensive proof ledgers, but they do **not** prove universal descent.

For source-quality material see [legacy result index](research/LEGACY_RESULT_INDEX.md) and curated, unchanged historical evidence in [legacy/](legacy/):
- [independent progress review, claim inventory and source copies](legacy/PROGRESS_REVIEW/README.md);
- [RL342–RL349 authoritative-at-the-time proof ledgers](legacy/authoritative/START_HERE.md);
- [old FINAL_CHANCE verdict and its mathematical countermodels](legacy/FINAL_CHANCE/VERDICT.md).

**The full, unmodified old repository** (including ~13,800 session-directory entries, transport bundles and indexing data) is safe on the snapshot branch [archive/pre-descent-gap-relaunch-2026-10-15](https://github.com/jfairfaxball-348/Collatz-Descent-Gap/tree/archive/pre-descent-gap-relaunch-2026-10-15). No historical original was rewritten to fit the new objective.

The old RL conveyor, cycle-specific R1–R7 stages, compulsory process audits and six-session stop rule are **retired as active instructions**. Past proof/correction ledgers are evidence, not authority for the new target. The new programme has one compact live ledger, direct mathematical sessions, and truthful proof status.

## Verification and limits

[Finite-horizon reference verifier](research/verification/finite_survival.py), [DG002 exact block checker](research/verification/verify_DG002.py), [DG003 inverse/cylinder checker](research/verification/verify_DG003.py), and [DG004 inverse/record checker](research/verification/verify_DG004.py), [DG005 tail-minimum checker](research/verification/verify_DG005.py), and [DG006 exact bridge/inverse-chain checker](research/verification/verify_DG006.py), [DG007 exact bridge/least-exception sieve checker](research/verification/verify_DG007.py), [DG008 exact bridge, inverse-residue and mixed-schedule checker](research/verification/verify_DG008.py), [DG009 first-record and integer-realisation checker](research/verification/verify_DG009.py), [DG010 true-modulus and unbounded-gap finite checker](research/verification/verify_DG010.py), [DG011 sharp mod-9 and mountain interpolation checker](research/verification/verify_DG011.py), and [DG012 repeat-block and mountain regression](research/verification/verify_DG012.py), and [DG013 paired-superword and logarithmic-schedule exact regression](research/verification/verify_DG013.py), and [DG014 square-free and finite strict-witness checks](research/verification/verify_DG014.py) check only their specified finite instances. DG002 and DG003's infinite-horizon lemmas have elementary paper proofs, not Lean or Palomar certificates. No universal Collatz proof is claimed. DG012 proves a scoped infinite fixed-positive-orbit nonrealisation theorem for eventually nondecreasing mountain tails; DG013 extends nonrealisation to alternating fixed-small / eventually nondecreasing large mountain parameters, and derives a general periodic-island size bound. DG014 shows that abstract square-free infinite mountain schedules can evade all consecutive repeated-superword tests, including unbounded sparse-spike versions with every finite positive prefix; no single fixed positive infinite realisation has been found. DG014 also proves the local 3/2 growth ceiling is sharp among finite strict bridges and analyses a conditional 3-divisible precursor of hypothetical cycle minima. These restricted tails are not known to describe arbitrary E orbits. Mathematical claims are tagged by proof status in the ledger, with Git history recording corrections.

## Research provenance

This is AI-assisted mathematical exploration with independently checkable artefacts where supplied. Retain the distinction between paper derivation, exact finite checks, historical repository claims, externally published mathematics, and verified formalisation. Code and document licensing remain as in [LICENSE.md](LICENSE.md).
