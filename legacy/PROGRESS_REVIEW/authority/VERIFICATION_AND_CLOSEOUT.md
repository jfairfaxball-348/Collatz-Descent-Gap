# Verification and atomic closeout

`AGENTS.md` is binding. This procedure applies after `CLOSEOUT_LOCK`.

## Bundle convention

Preserve the established handover convention:

- authoritative ZIP or documented lossless transport;
- outer `.zip.sha256` sidecar for ZIP/reconstructible-bundle transports;
- internal `SHA256SUMS.txt` for ZIP/reconstructible-bundle transports;
- portable fast verifier scripts;
- current report, proof/correction ledgers, session state, successor target, certificates, and required provenance.

Follow the actual current naming/layout.

A connector worker may also promote a **committed flat Git-tree authority** when its available Git-object interface makes the committed tree itself the lossless transport. In that representation the cryptographic Git tree/blob identities plus the atomic commit/readback replace the current ZIP outer-sidecar/internal-manifest transport checks. The successor `authoritative/START_HERE.md` must explicitly declare the incoming RL and name exactly one target for that RL, the predecessor closeout-verification record must describe the connector packaging/readback, and the current portable verifier and independent red team must be present in `authoritative/verification/`. Older inherited ZIPs and targets may remain as provenance; they are not the current transport. A subsequent shell worker verifies this form with `python3 tools/rl_flat_authority_preflight.py`, including checksum verification for any historical ZIP/sidecar pair; it must not rename/delete mathematical authority merely to make the legacy ZIP scanner pass.

## Candidate gate

Before changing remote authority:

1. Freeze the exact proposed proof/research state.
2. Classify every promoted item.
3. Record successes, barriers, corrections/demotions, dependencies, open obligations, exact scope, and verifier status.
4. Prove promoted finite certificates are gap-free over their exact claimed ranges where applicable.
5. Run required current red teams and target-specific verifiers.
6. Recompute target-required live constants/minima/floors/support edges as applicable.
7. Build the complete handover/bundle or committed flat Git-tree transport.
8. Compute/check the outer sidecar when the transport uses one; otherwise record the committed tree/blob identities.
9. Fresh-unpack/reconstruct ZIP-based transports in clean temporary storage; for flat Git-tree transport, read back the committed authority tree into a clean worker context.
10. Verify the internal manifest when the transport uses one; for flat Git-tree transport, verify the committed tree/blob identity and exact promoted path set.
11. Run the complete portable fast verifier suite from the clean unpack/reconstructed/committed authority.
12. Confirm the verified transport reproduces the frozen candidate state.
13. Confirm the incoming `authoritative/` still matches `BASE_HEAD`/the recorded snapshot.
14. Confirm the proposed successor is exactly one RL number ahead and authority will not mix generations.

Shell workers should additionally run the repository structural helpers (`check-promotion`, `check-snapshot`, `preflight`) when available. Connector workers may perform their underlying structural checks directly from candidate files, hashes, repository reads, and Git identities. Not having a repository shell is not a failure.

If a mathematical or packaging/authority-integrity step fails, do not promote.

## Knowledge catalogues

Generated knowledge catalogues are explicitly outside the proof-state promotion gate.

For a shell worker, the preferred final-tree maintenance is:

```sh
python3 tools/rl_conveyor.py index-build
python3 tools/rl_conveyor.py index-validate
```

For a connector worker, these commands may be deferred. Do not block or split a numbered RL transition because they cannot be executed. Leave tracked catalogue files unchanged, mark them `stale/deferred`, and avoid claiming they cover the new generation.

Catalogue freshness can be restored later in a separate infrastructure commit or any shell-capable session. Such maintenance consumes no RL number.

## Atomic repository transaction

Only after the candidate gate passes:

1. Reconfirm the remote/default branch still equals `BASE_HEAD`.
2. Freeze the completed incoming generation under the established `sessions/RL.../` location.
3. Replace `authoritative/` with **only** the verified successor generation.
4. Preserve historical paths/provenance.
5. If shell-capable and practical, rebuild/validate catalogues; otherwise defer them as above.
6. Inspect the complete intended final path set/tree. No unrelated cleanup.
7. Create one atomic RL-transition commit.
8. Advance/push the intended remote branch/ref once.
9. Read the remote ref back and require its SHA to equal the new commit.
10. Read back the committed frozen session and successor `authoritative/START_HERE.md`.
11. Confirm the new authoritative state uniquely resolves the successor target from `START_HERE.md` (historical target provenance may remain only when explicitly inherited and must not be mistaken for the live target).
12. Confirm no half-transition remains.

With local Git, staging plus `git diff --cached` is the inspection mechanism. With GitHub Git-object tooling, the explicit tree entries/base tree and resulting commit are the equivalent inspection mechanism.

The invariant is:

> The remote commit contains the complete verified numbered transition, or the numbered transition does not exist.

## GLOBAL PROOF ROADMAP closeout requirement

`docs/GLOBAL_PROOF_ROADMAP.md` is the permanent high-level logical navigation protocol for the research programme.

Every authoritative numbered closeout must include a section headed exactly:

`GLOBAL PROOF ROADMAP STATUS`

and must carry all nine required fields defined there:

- `CURRENT_STAGE`;
- `CURRENT_STAGE_NAME`;
- `CURRENT_STAGE_PROGRESS`;
- `THIS_SESSION_ADVANCE`;
- `CURRENT_STAGE_BLOCKER`;
- `ADVANCE_CRITERION`;
- `REMAINING_STAGES`;
- `ROADMAP_DELTA`;
- `GLOBAL_PROOF_STATUS`.

Progress is obligation-based, never session-count- or effort-based. Stage transitions require the theorem-level advance criterion, not merely substantial local progress.

Every successor handover must preserve the current roadmap state and instruct the successor to work on the smallest theorem that advances the current stage, unless a strategic audit explicitly identifies an upstream dependency elsewhere.

A correction/demotion may reduce the percentage or produce `REGRESSION/CORRECTION`. `GLOBAL_PROOF_STATUS` remains `OPEN` unless the complete R7 end-to-end proof has actually been assembled and audited.

## Post-commit result

Report:

- commit SHA and remote ref;
- frozen session path;
- successor authoritative target/path;
- bundle/fresh-unpack/verifier status, or committed-flat-tree identity/readback status;
- catalogue status (`current` or `stale/deferred`);
- post-commit readback result;
- the committed `GLOBAL PROOF ROADMAP STATUS`.

Catalogue staleness must be transparent but does not make a mathematically valid atomic RL transition incomplete.
