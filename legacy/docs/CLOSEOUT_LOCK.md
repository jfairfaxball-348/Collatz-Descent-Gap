# CLOSEOUT_LOCK and reserved completion budget

`AGENTS.md` is binding. This document is the canonical detailed procedure for closing an RL in either a shell worker or connector worker.

## Purpose

An incoming RL job is not complete when research stops. Classification, candidate freeze, packaging, clean verification, atomic repository promotion, remote-ref advancement, and post-commit readback are part of one transaction.

The worker must not require the user to migrate the job between Codex/local and ChatGPT/cloud merely to finish routine closeout.

## Lock triggers

Enter `CLOSEOUT_LOCK` when the user asks to finish/close/hand over/commit/push/promote, or when continued research threatens a complete closeout.

Only an explicit instruction to resume mathematics unlocks the job before successful promotion.

## Compact closeout state

Maintain a compact non-authoritative closeout record sufficient to finish without conversation memory. Shell workers normally use:

`.rl-work/RL<incoming_rl>/CLOSEOUT_STATE.md`

Connector workers must keep the equivalent compact state in sandbox artifacts; use the idempotent schema/procedure in `docs/CONNECTOR_WORKFLOW.md`.

Record at least:

- `BASE_HEAD` and authoritative snapshot/tree identity;
- incoming and successor RL;
- exact target;
- promoted results and classifications;
- corrections/demotions;
- barriers/dependencies/open obligations;
- candidate paths/hashes;
- verifier/red-team results;
- bundle/sidecar/manifest/fresh-unpack status;
- intended session and successor-authority paths;
- intended commit/ref;
- for connector workers, already-created blob/tree/commit OIDs;
- catalogue freshness status (`current`, `stale/deferred`, or `not checked`);
- exact remaining deterministic operation.

Update this state after every completed deterministic closeout step before starting the next expensive/tool-heavy step.

## Behaviour while locked

1. Start no new mathematics, scans, historical audits, route exploration, or opportunistic improvements.
2. Do not alter remote `authoritative/` or `sessions/` until the candidate verification gate passes.
3. Execute only: candidate freeze/classification → required red teams/verifiers → bundle/sidecar or flat-tree candidate → clean verification → authority snapshot check → atomic Git transition → push/ref update → post-commit readback.
4. Treat packaging, hash, transport, path, catalogue, and execution-environment limitations as mechanical matters unless they expose a proof-state problem.
5. If a genuine proof-state error appears, make the smallest explicit correction/demotion necessary, rebuild/reverify, and return directly to closeout.
6. Prefer one atomic Git transition. Ordinary Git and direct Git-object tooling are both valid.
7. Do not amend a published RL commit or combine numbered transitions.
8. Do not call the job complete until the intended remote ref points at the new commit and committed `sessions/` plus `authoritative/` have been read back.

## Connector idempotency

Connector closeout must be resumable without replaying completed deterministic work.

- Freeze candidate files in sandbox before remote mutation and record their hashes.
- Run required candidate verifiers/red teams against that frozen candidate and record results once.
- Create only changed blobs and record each returned immutable blob OID immediately.
- Construct the candidate tree from the recorded base tree plus changed/deleted entries; do not enumerate the full repository tree merely to reconstruct unchanged paths.
- Record the candidate tree OID and candidate commit OID as soon as each exists.
- If interrupted, reuse recorded immutable Git objects rather than recreating them.
- Perform the final live/default-branch `BASE_HEAD` comparison immediately before the single ref advance.
- If the ref already equals the recorded candidate commit after an interruption, do not advance it again; continue with readback.

This reduces closeout failure-domain length without weakening the atomic-transition invariant.

## Catalogue handling

Knowledge catalogues are optional optimisation caches. They are not part of the mathematical promotion gate.

If a shell is available, refresh/validate them when practical. If no repository shell is available, or catalogue regeneration would otherwise force an environment handoff, leave them unchanged and explicitly report them as stale/deferred. This does not block the RL commit.

Connector workers must not fetch the multi-megabyte catalogue JSONL files merely to close a current RL.

Never hand-edit generated catalogue files to simulate a successful build.

## Failure or interruption

If safe atomic promotion cannot be completed:

- preserve the candidate/closeout record;
- preserve already-created immutable Git object IDs for connector resumption;
- leave the last remotely committed authority as truth;
- make no partial research-state promotion;
- report the first failing gate and exact resume operation.

A stale catalogue alone is not such a failure.
