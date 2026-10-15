# RL345 closeout verification

Date: 2026-09-17

Transport: committed flat Git-tree authority. Git tree/blob identities plus atomic commit/readback are the lossless transport checks permitted by `docs/VERIFICATION_AND_CLOSEOUT.md`.

Incoming BASE_HEAD: `f10996208efb8cc437f0b364384054f3a55a3fb8`
Incoming repository tree: `31ecb9af55ec804aadfc021f5c689184691d966c`
Successor: RL346.

Candidate gate:

- research froze on the user's `finish up`; no Phase-5 work or depth-71 extension was performed after CLOSEOUT_LOCK;
- inherited RL344 width constants were replayed connector-equivalently and remained green;
- `verification/verify_rl345_fast.py` -> `RL345_FAST_GREEN`;
- `verification/red_team_rl345.py` -> `RL345_RED_TEAM_GREEN`;
- both RL345 implementations reconstruct all 67,070 exceptional 72-gap words and all 135,356 exact q=0-band endpoint lifts, with no sampling;
- both require universal descent below `2^71`, maximum depth 446, unique extremal endpoint `32854878509085218570239`, and digest `2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d`;
- source-side verification requires `2*3^22 < 2^37 < 2*3^23`;
- unfinished overlap/depth-71 ideas are explicitly non-promoted;
- successor `START_HERE.md` names exactly one live target, `RL346_R1_CRT_COMPLETION_TARGET.md`;
- knowledge catalogues are stale/deferred and outside the mathematical promotion gate.

R1 remains OPEN.
