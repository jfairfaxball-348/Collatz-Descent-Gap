# Connector worker workflow

`AGENTS.md` is binding. This document is the connector-specific efficiency and resumability procedure. It changes no mathematical authority and weakens no startup, verification, concurrency, or atomic-promotion gate.

## Design goal

Connector turns have a smaller practical failure domain than an RL session. A bare `continue` should still perform meaningful research, but one turn must not depend on reaching an arbitrarily distant theorem-sized endpoint before returning control.

Use one coherent **bounded continuation work unit** at a time:

- pursue one attack far enough to produce meaningful information;
- persist durable intermediate computation before another expensive branch;
- if the theorem-sized endpoint is still materially distant, return a concise checkpoint rather than extending the same tool/computation chain;
- resume the next `continue` from the durable frontier, not from repository reconstruction.

This is not permission for trivial micro-checkpoints.

## Hot startup set

After pinning the live default-branch `BASE_HEAD` and committed `authoritative/` tree identity, the connector hot set is only:

1. `AGENTS.md`;
2. `authoritative/START_HERE.md`;
3. the exact current files explicitly named there;
4. the unique current target;
5. current verifier/red-team files required by that entry point.

Do not recursively enumerate the repository, `authoritative/`, `sessions/`, `Archive/`, or `knowledge/` during ordinary startup. Do not fetch the full generated catalogue JSONL files. Historical provenance is cold storage: open it only by exact path for a live dependency.

Once the incoming authority has been validated, inherited proof ledgers are trusted under verification economy. Do not reread or reverify them on every `continue`.

## Compact resume state

Maintain a non-authoritative connector resume record in sandbox/conversation artifact storage. Suggested machine-readable shape:

```json
{
  "format": "rl-connector-resume-v1",
  "base_head": "<commit>",
  "authoritative_tree": "<tree>",
  "incoming_rl": 0,
  "target": "authoritative/<target>",
  "validated_authority_paths": [],
  "validated_checks": [],
  "live_attack_files": [],
  "last_verified_frontier": "<compact statement>",
  "completed_artifacts": [
    {"name": "<artifact>", "sha256": "<sha256>", "scope": "<exact scope>"}
  ],
  "unpromoted_or_uncovered": [],
  "next_exact_operation": "<single next operation>",
  "do_not_recompute": [],
  "stop_and_repair_active": false
}
```

The record is a resumability aid only. It cannot promote a theorem, certificate, correction, roadmap change, or any other mathematical state.

Update it:

- after startup validation;
- before and after a long computation;
- after a material intermediate result;
- before switching attack branches;
- before a long connector/Git-object sequence;
- immediately before `CLOSEOUT_LOCK`.

## Bare `continue` fast path

On a later bare `continue`:

1. read the compact resume state first;
2. fetch only the live default-branch HEAD;
3. if HEAD still equals `BASE_HEAD` and the recorded authority tree is unchanged, reuse the validated startup gate;
4. load only the live attack files needed by `next_exact_operation`;
5. execute one bounded continuation work unit;
6. update the resume state before starting another expensive branch;
7. return a user-facing checkpoint once substantial useful work is durable, even if the theorem-sized endpoint remains farther away.

Rerun startup verifiers or reread inherited ledgers only after a changed base/authority identity, live dependency, contradiction, verifier failure, repair event, or direct user instruction.

## Connector search discipline

Prefer, in order:

1. an exact path already named by current authority or resume state;
2. an exact frozen-session path already recorded as provenance;
3. a narrow code/path search for one known filename/result identifier;
4. a catalogue query when a current catalogue is available;
5. a narrowly scoped historical audit.

Repository-wide recursive trees, broad searches across all frozen sessions, and full catalogue downloads are exceptional diagnostics, not normal continuation operations.

## Idempotent `CLOSEOUT_LOCK`

When closeout begins, create a compact non-authoritative `CLOSEOUT_STATE` alongside the resume state. Suggested shape:

```json
{
  "format": "rl-connector-closeout-v1",
  "base_head": "<commit>",
  "base_tree": "<tree>",
  "incoming_rl": 0,
  "successor_rl": 0,
  "candidate_paths": {},
  "candidate_checks": [],
  "created_blobs": {},
  "candidate_tree": null,
  "candidate_commit": null,
  "ref_advanced": false,
  "readback_complete": false,
  "remaining_operation": "<exact deterministic step>"
}
```

Closeout is deterministic and resumable:

1. freeze candidate files in sandbox before remote mutation;
2. hash candidate files and record paths/hashes;
3. run each required verifier/red team once against the frozen candidate and record the result;
4. create changed Git blobs and immediately record each returned blob OID;
5. construct the candidate tree from the recorded base tree plus only changed/deleted path entries; do not rebuild unchanged blobs or enumerate the entire repository tree;
6. record the candidate tree OID;
7. create the candidate commit once and record its OID;
8. immediately before advancing the branch ref, fetch the live default-branch HEAD and require it still equals `BASE_HEAD`;
9. advance the ref once;
10. read back the remote ref, frozen session entry point, and successor `authoritative/START_HERE.md`;
11. mark readback complete.

Git blobs, trees, and commits are immutable. If a connector turn stops after creating any of them, reuse their recorded OIDs on resume instead of recreating them. If the ref was already advanced, do not advance it again; proceed directly to readback after proving it points at the recorded candidate commit.

The atomic invariant remains unchanged: the remote ref contains the complete verified transition or no numbered transition exists.

## Concurrency checks

Do not repeatedly fetch a full repository tree for concurrency protection. `BASE_HEAD` is the transaction boundary. Pin it at startup, keep the committed `authoritative/` tree identity in resume state, and perform the final live-HEAD comparison immediately before the ref move. Any unexplained mismatch fails closed.

## Catalogue policy for connectors

The generated catalogues are cold lookup caches, not startup state. A stale catalogue never blocks a numbered transition and must not be refreshed during ordinary connector research or closeout. A connector may use a small exact metadata read to determine catalogue status, but should not load multi-megabyte JSONL catalogues unless a specific historical lookup cannot be satisfied more narrowly.

## User-facing checkpoint after interruption risk

If a coherent work unit has produced substantial useful information but another expensive branch is required, return control with:

- what was established and its classification;
- what remains open/unpromoted;
- the exact durable frontier/artifact hash if relevant;
- the exact next operation;
- the normal session recommendation required by `AGENTS.md`.

The purpose is shorter failure domains and exact resumability, not less ambitious mathematics.
