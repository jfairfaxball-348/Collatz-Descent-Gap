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
5. [Next research session: DG002](research/NEXT_SESSION_DG002.md).

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

[Finite-horizon reference verifier](research/verification/finite_survival.py) checks parity/residue and affine criteria in bounded cases; it is not a certificate for infinite descent or a Lean proof. No universal Collatz proof or new major mathematical breakthrough is claimed. Mathematical claims are tagged by proof status in the ledger, with Git history recording corrections.

## Research provenance

This is AI-assisted mathematical exploration with independently checkable artefacts where supplied. Retain the distinction between paper derivation, exact finite checks, historical repository claims, externally published mathematics, and verified formalisation. Code and document licensing remain as in [LICENSE.md](LICENSE.md).
