# RL344 closeout verification

Date: 2026-09-17

Transport: committed flat Git-tree authority. No current ZIP or sidecar is used. Git tree/blob identities plus commit/readback are the lossless transport checks permitted by `docs/VERIFICATION_AND_CLOSEOUT.md`.

Incoming mathematical BASE_HEAD: `6929776ecd7093b6673e235a9aa8ca25bd2dc67f`
Incoming authoritative tree: `281e551a494c6fcf8fc51f1e4efceec0d3989a07`
Successor: RL345.

Candidate gate:

- research was frozen before CLOSEOUT_LOCK and no new mathematics was performed during packaging;
- current authority was accepted under the connector-equivalent flat-tree start gate and verification economy;
- promoted RL344 results are analytic structural reductions; the un-red-teamed endpoint-cylinder scans and Phase-5 work are explicitly scratch-only;
- `verification/verify_rl344_fast.py` -> `RL344_FAST_GREEN`;
- `verification/red_team_rl344.py` -> `RL344_RED_TEAM_GREEN`;
- the independent red team re-derives the `<2^37` Phase-4 width inequality by integer cross multiplication and independently finds 24 as the first power-of-three prefix depth exceeding that width;
- successor `START_HERE.md` names exactly one live target, `RL345_R1_METHODICAL_COMPLETION_TARGET.md`;
- knowledge catalogues are stale/deferred and are not part of the mathematical promotion gate.

Mechanical closeout note: after the initial concurrency check and candidate-tree creation, a connector mis-invocation created commit `c2b83b21ad2dff82316c7843a830ff746f72cc54` on `main` with message `x`. Exact commit comparison against the incoming BASE_HEAD proves that commit added only the one-line path `dummy`; it changed no authoritative, session, mathematical, or verification file. Published history was not force-rewritten. The final RL344 transition uses that mechanical commit as parent, removes `dummy`, and installs the already-verified RL344/RL345 candidate tree. The mathematical incoming authority therefore remained unchanged throughout.

R1 remains OPEN. The committed roadmap advances to 92% obligation-level progress.
