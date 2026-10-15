# RL state machine

`AGENTS.md` is the binding contract. This document defines repository-state transitions and failure handling.

## Terms

- **Incoming RL**: the job and target identified by `tools/rl_conveyor.py startup`.
- **Handover generation**: the completed generation currently represented in `authoritative/`.
- **Successor RL**: the new incoming authority created only after the current job is verified and promoted.
- **Local checkpoint**: ignored, non-authoritative state under `.rl-work/RL<incoming_rl>/`.
- **Committed authority**: the remote-ref commit whose `authoritative/` generation has passed post-commit readback.

## State flow

```text
Committed authority
  → start gate (HEAD + authoritative snapshot + incoming verification)
  → ignored local research/checkpoints
  → candidate handover under .rl-work/
  → closeout reserve reached OR user requests finish/handover/commit-push
  → CLOSEOUT_LOCK (no new research)
  → verified candidate + clean fresh unpack
  → one atomic RL transition commit
  → push/advance intended remote branch/ref
  → post-commit readback of sessions/ + authoritative/
  → successor committed authority
```

No other path creates mathematical authority.

## Start transition

The start gate is defined in `docs/CODEX_OPERATIONS.md`. A passing gate records `BASE_HEAD` and an authoritative snapshot, verifies the current handover, and creates an ignored checkpoint. Only then may ordinary research begin.

A failing start gate enters repair without mutating `authoritative/`. Freeze the last committed authority and identify whether the failure is:

- **mechanical**: checksum, manifest, packaging, transport, catalogue, path, or tooling integrity; or
- **mathematical/proof-state**: contradiction, invalid dependency, scope error, failed mathematical verifier/red team, or a recorded claim no longer supported.

Repair a mechanical failure as a mechanical defect; do not create a correction/demotion merely because transport or packaging failed. A genuine proof-state failure must identify the first invalid dependency and explicitly record the resulting correction/demotion before any later promotion.

## Research and candidate transitions

All research and candidate construction remain under `.rl-work/`. A checkpoint, candidate theorem, partial scan, generated bundle, or local verifier success does not change committed authority.

An interruption from research or candidate state returns operational control to the last committed authority:

- account for or terminate outstanding processes;
- refresh the local checkpoint;
- leave `authoritative/` and `sessions/` untouched;
- make no research-state commit;
- report the last fully verified checkpoint and exact unpromoted remainder.

If repository state no longer matches `BASE_HEAD` for an unexplained reason, stop. Do not discard changes blindly; identify their ownership and restore a trustworthy frontier before proceeding.

## Stop-and-repair transition

Stop-and-repair freezes the last unquestionably valid state, identifies the first invalid dependency, and reruns only the checks required to restore trust. It may return to research only when the failure arose before closeout and the repair has restored the start/research frontier.

If repair begins during `CLOSEOUT_LOCK`, the lock remains active. Fix only the invalid dependency or mechanical defect, rebuild/reverify the candidate, and return directly to the closeout gate. Do not use repair as an opportunity to reopen research.

## CLOSEOUT_LOCK transition

`CLOSEOUT_LOCK` is one-way for the incoming RL unless the user explicitly instructs the worker to resume mathematical research. Its triggers and compact state requirements are defined in `docs/CLOSEOUT_LOCK.md`.

While locked, the only permitted path is candidate freeze → required verification → atomic transition → remote-ref advancement → readback, with the minimum repair loop described above. Packaging or hash mismatches do not unlock research.

## Promotion and terminal state

The full gate and atomic transaction are defined in `docs/VERIFICATION_AND_CLOSEOUT.md`. A local commit is an intermediate state, not completion. Promotion becomes terminal only when:

1. the intended remote branch/ref resolves to the new commit;
2. the committed frozen session path exists and has the expected generation;
3. the committed `authoritative/` entry point is the verified successor generation;
4. the worktree and repository sanity checks show no half-transition.

If push or readback fails, remain in closeout. Do not call the job promoted and do not begin the successor RL.

## Macro-session loop

After terminal readback, treat the successor authority as a fresh incoming state. Record a new `BASE_HEAD`, snapshot it, and rerun the start gate. A long worker session may repeat the loop only when enough capacity remains to complete another full transition. Numbered RL jobs are never combined into one commit.
