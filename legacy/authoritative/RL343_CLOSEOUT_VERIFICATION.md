# RL343 closeout verification

Date: 2026-09-17

Transport: committed flat Git-tree authority. No current ZIP or sidecar is used. The Git tree/blob identities and post-commit readback are the lossless transport checks permitted by `docs/VERIFICATION_AND_CLOSEOUT.md` for this established connector-produced layout.

Incoming BASE_HEAD: `6ddf2693a2ea2983bbe454e8b3fbc426bd36af60`; incoming authoritative tree: `686edcbe04a8a53a38926d62917d492fa0bf94be`. Successor: RL344.

Candidate gate:

- research was frozen before CLOSEOUT_LOCK; no new mathematics was performed during packaging;
- RL343 proof, exact-certificate, correction, frontier, and roadmap ledgers classify every promoted result and preserve the external floor qualification;
- `verification/verify_rl343_fast.py`: `RL343_FAST_GREEN`;
- `verification/red_team_rl343.py`: `RL343_RED_TEAM_GREEN`, independently replaying all 63,488 terminal-tail endpoints and reproducing depth 403, first maximizer `k=58658`, and the SHA-256 digest `6b865b436278792435dc59fcf4f15975f9e4961f403af18a4cbd2ff12be616ad`;
- inherited `verification/verify_rl342_fast.py`: `RL342_FAST_GREEN`;
- inherited `verification/red_team_rl342.py`: `RL342_RED_TEAM_GREEN`, replaying all 238,329 inherited family members;
- current candidate tree has exactly one live target, `RL344_R1_RESIDUAL_CRT_RETURN_TARGET.md`; historical targets remain provenance only;
- clean candidate readback was performed from the candidate authority directory, and the verifier scripts are self-contained under `verification/`;
- incoming authority and remote `main` were unchanged at the recorded BASE_HEAD before staging.

The RL343 transition does not close R1. The committed roadmap remains R1 OPEN at 90%, with the exact residual `O_75` obligation handed to RL344. Knowledge catalogues are stale/deferred and are not part of the mathematical promotion gate.
