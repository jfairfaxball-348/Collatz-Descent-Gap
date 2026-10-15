# Computational evidence and certificates

## Current curated artifacts

| Artifact | Proposition supported | Generator/verifier | Scope and limitation |
|---|---|---|---|
| RL18 orbit identity verifier | Word numerator/orbit recurrence sanity checks | Original RL18 verifier | Small-domain check; analytic identity is load-bearing, not the experiment. |
| RL19 radius-3 verifiers | Exact finite leaves and inherited reductions | Original RL19 scripts | Dependent on stated external LMN and inherited hypotheses. |
| RL20 countermodel verifier | Exact 184-bit word, rotation distances, and non-divisibility | Original RL20 verifier | Falsifies a proposed bridge; it is not an RL cycle. |
| RL343 terminal escape data | No terminal tail of 60 unit gaps in the stated scope | `authority/terminal_ones_escape.json` and related scripts | Finite exact certificate; does not eliminate all returns. |
| RL343 bridge/pairing checks | Reconstruct the full physical bridge and matched phase pairing | `authority/verify_full_cycle_bridge.py`, `authority/verify_matched_phase_pairing.py` | Checks the recorded restricted theorem and constants. |
| RL349 arithmetic verifier | Exact rational diagnostic using `log 2 > 15757912/22733865` | `certificates/verify_rl349_fast.py` | Does not prove `e_k < ell/(12 log 2)` and therefore does not close Phase 4. |
| RL349 independent red team | Reconstructs the lower log enclosure and exact margin | `certificates/red_team_rl349.py` | Red-teams arithmetic only; written scope analysis remains load-bearing. |

The package also includes the directly relevant historical/current scripts in `certificates/`: RL18 orbit and cubic checks, RL19 product/population checks, the RL20 bounded-bridge countermodel verifier, the RL343 terminal-tail red team, and the RL343/RL344/RL345/RL347/RL348 fast-verifier and red-team pairs. These are copied verbatim; they do not turn their surrounding theorem into an independently audited result.

## Reproducibility questions for a future audit

- Check every claimed finite domain against the mathematical statement actually consumed downstream.
- Confirm whether the verifier is independent enough from the generator to catch the relevant error modes.
- Distinguish a finite certificate from an analytic all-length claim.
- Preserve exact integer/rational arithmetic and environment assumptions.
- Verify that inherited certificates are not being used outside their recorded scope.

No expensive historical computation was rerun for this setup. The package records artefact locations and source provenance so an independent reviewer can choose targeted reruns.
