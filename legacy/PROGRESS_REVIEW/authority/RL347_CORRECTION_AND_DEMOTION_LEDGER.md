# RL347 correction and demotion ledger

Date: 2026-09-17
Status: CLOSED/FROZEN

## 1. Withdrawn scratch claim that `L=ell` is impossible

During live scratch, an argument briefly claimed that a complete half-cycle return would force all
q=0 vertices to pair across the rows and hence contradict the least-root placement.

This is invalid. The exact pairing theorem is one-way in the needed direction:

early-row q=0 => contact and matched late-row q=0.

A strict late-row q=0 vertex may have a positive-q early mate. Therefore `L=ell` is NOT eliminated.

The promoted replacement is RL347.5: every nondecreasing `L=ell` residual is a matched contact pair
with even physical separation in `[2,2^36]`.

## 2. Withdrawn scratch source-defect estimate using the wrong endpoint

A tentative skip estimate for a crossing-outside over-half return used a strong lower bound on the
right endpoint normalized defect `e_s` as though it controlled the first matched half-cycle of the
inverse-oriented long return.

The inverse q-walk orientation makes the first matched half-cycle depend on the lower/source endpoint
instead. The tentative numerical estimate was therefore withdrawn and is NOT authoritative.

A related source-defect idea is preserved only as unpromoted scratch in `RL347_SCRATCH_FRONTIER.md`.

## 3. One-unit correction to the over-half integer bound

A live checkpoint transiently stated

`R>=23135982580`, `L<=251920108044`.

Exact rational closeout arithmetic gives instead

`R > 23135982578.518...`,

so the correct integer consequence is

`R>=23135982579`, `L<=251920108045`.

Only the corrected values in RL347.3 are promoted.

## 4. No correction to inherited authority

These corrections concern RL347 uncommitted scratch/checkpoint wording only. No inherited RL342–RL346
authoritative theorem, certificate, target, or proof-state conclusion is demoted.
