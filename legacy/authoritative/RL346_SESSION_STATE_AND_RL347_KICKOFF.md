# RL346 session state and RL347 kickoff

Date: 2026-09-17
Status: RL346 CLOSED/FROZEN; RL347 prepared, not started.

## Frozen RL346 result

The exact live Phase-4 frontier is now a bounded cyclic-signature plus deterministic inverse-carry
decoder problem.

Promoted RL346 facts:

1. For every surviving long return, `76<=G_72<=114` and `1<=q_(L-72)<=39`.
2. Every q=0 vertex may be represented by bounded incoming predecessor data rather than by an
   arbitrarily tall prefix of the next return.
3. Exact source/end phase tags determine one residue class of `L mod ell`, hence at most two length
   representatives in `1..2ell`; `H` is then exact.
4. Fixed physical endpoints plus `(L,H)` admit at most one complete inverse gap word, recovered
   backwards from the affine carry.

The attempted `G_72=76` numerical enumeration is NOT authoritative and must not be used; see the
correction ledger.

## What remains open

Phase 4 is not closed. The unresolved task is to eliminate/reject the deterministic decoded middle
without replaying a potentially enormous number of odd events, while preserving all inherited
predecessor/successor CRT, oddness, q-profile, row contact, wrap, ownership/pruning, phase-sign and
least-state-descent conditions.

`O_75=empty` is not proved. R1 remains OPEN. Phase 5 remains scratch-only and must not resume before
Phase 4 closes.

## RL347 kickoff

RL347 is the unique next authoritative research session.

Read first:

- `START_HERE.md`;
- `RL346_PROOF_LEDGER.md`;
- `RL346_EXACT_CERTIFICATE.md`;
- `RL346_CORRECTION_AND_DEMOTION_LEDGER.md`;
- `RL346_GLOBAL_PROOF_ROADMAP_STATUS.md`;
- `RL347_R1_CYCLIC_SIGNATURE_DECODER_TARGET.md`;
- inherited `RL345_PROOF_LEDGER.md`, `RL344_PROOF_LEDGER.md`, and the RL343 full-cycle bridge as
  needed.

Primary objective: prove an all-length skip/pumping/ranking theorem or bounded mixed-adic transition
quotient for the deterministic decoder, sufficient to eliminate every phase-nondecreasing long
return in the exact cyclic-signature window.

Hard prohibitions:

- do not enumerate `G_72=77,78,...`;
- do not treat the invalid RL346 `G_72=76` scratch as a certificate;
- do not restart sigma/coefficient/q-upgrade ladders;
- do not resume Phase 5 before Phase 4 closes;
- do not import RL303/RL304 P/Q conclusions without proving a bridge to the current genuine
  physical q=0 return interface.

If the global decoder attack fails, freeze the first exact bounded signature that survives all tests
with enough information for a successor to resume from that singleton obstruction.
