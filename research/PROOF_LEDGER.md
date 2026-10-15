# Descent Gap — proof and evidence ledger

Authoritative for **new DG programme only**, beginning 2026-10-15. Prior RL and FINAL_CHANCE ledgers remain historical sources and do not bind new sessions.

| ID | Claim | Status | Evidence / exact scope | Impact on E |
| --- | --- | --- | --- | --- |
| DG-DEF-01 | T, sigma and E defined for n>=2 | DEFINITION | THEOREM_TARGET.md | Sets objective |
| DG-EXT-01 | Almost all positive integers have finite stopping time | EXTERNAL PUBLISHED THEOREM | Terras 1976; Everett 1977; exact natural-density statement; SOURCES.md | E has natural density zero, **not** empty |
| DG-EXT-02 | For all f(n)->infinity, almost all Collatz orbits reach below f(n) in logarithmic density | EXTERNAL PUBLISHED THEOREM | Tao, Forum Math Pi (2022); not proof of E empty | Optional stronger background, no universal inference |
| DG-001-A | For any fixed parity prefix, T^j(n)=(3^{s_j} n + q_j)/2^j with explicit recurrence for q | ELEMENTARY PROOF RECORDED, NOT FORMALISED | sessions/DG001.md, section 1 | Exact finite-prefix algebra |
| DG-001-B | Each length-k parity word corresponds to one residue class modulo 2^k | ELEMENTARY PROOF RECORDED, NOT FORMALISED | sessions/DG001.md, section 2 | Exact finite-prefix decomposition |
| DG-001-C | A fixed parity word's length-k survivors form either all n>=2 in that class or a bounded initial part of the class | ELEMENTARY PROOF RECORDED, NOT FORMALISED | sessions/DG001.md, section 3 | Makes finite-survivor set computable; **does not remove infinite survival** |
| DG-001-D | For each k there are infinitely many n whose first k shortened iterates do not descend | ELEMENTARY PROOF RECORDED, NOT FORMALISED | sessions/DG001.md, section 4; n=2^k t-1 | Kills any universal fixed stopping-time cap |
| LEGACY-CYCLE-01 | Parity-word/full-denominator cycle identities D=2^A-3^L and ownership conditions | REPOSITORY-CLAIMED PROVED AT CYCLE SCOPE; NOT INDEPENDENTLY REAUDITED HERE | legacy/PROGRESS_REVIEW/CLAIM_INVENTORY.md C01,C02 | Background algebra only, not a universal descent bridge |
| LEGACY-RL349 | Selected ordered genuine g=2 parent reductions and exact rational diagnostics | REPOSITORY-CLAIMED BRANCH/FINITE; OPEN RESIDUAL | legacy/PROGRESS_REVIEW/RL349_TRUTH_SNAPSHOT.md; legacy/authoritative/RL349_PROOF_LEDGER.md | Not an elimination of E |
| LEGACY-BARRIER | Historical local-to-global false bridges, rational affine countermodel and STOP | HISTORICAL COUNTERMODELS / METHOD BARRIER | legacy/FINAL_CHANCE/VERDICT.md | Warns against promoting constrained profiles to integer orbits |
| DG-GAP-01 | Derive E empty from exceptional-set arithmetic | OPEN; MAIN PROBLEM | OPEN_GAPS.md | Entire target |

**No original breakthrough, Lean-certified statement, or universal Collatz proof is claimed.** A verifier confirms only its encoded finite proposition. New corrections must explicitly name the ledger entry demoted or amended and preserve the former text via Git history.
