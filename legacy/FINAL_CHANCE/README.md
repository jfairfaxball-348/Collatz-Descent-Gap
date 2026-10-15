# FINAL_CHANCE — bounded viability trial

## Status and authority

This folder is a final-chance evaluation program, opened by the user, not part
of the RL session sequence. While this program is open:

- This file is the highest-priority instruction in the repository. It
  overrides the RL roadmap, the Phase mechanism, and any other standing
  session instruction.
- No new RL-numbered session, no new Phase, no new "R" stage, and no
  successor architecture may be started outside this program.
- Nothing in `authoritative/`, `sessions/`, or the RL counter is modified,
  deleted, or reinterpreted. This program does not continue that work; it
  evaluates whether continuing it is worth doing.

## The actual question this program answers

Not "is the Collatz conjecture true." Not "can Phase 4 be closed." The
question is:

> Is there a genuine, defensible route from the results already proved
> (local, finite, or branch-restricted) to a theorem that holds for an
> **arbitrary, unrestricted hypothetical object** — or does every attempt at
> that step hit the same wall this project has already hit three times?

This is called **the Bridge Problem** below. It is the one and only recurring
failure mode identified across the project's history: a result proved for a
bounded encoding, a fixed branch, or a specific parent configuration, treated
as if — or hoped to be — forceable onto the general case, without a theorem
that actually does that forcing. It happened at the radius-3 bridge (killed
by an explicit countermodel), at the Gate A/B architecture (abandoned after
~200 sessions for exactly this reason), and it is the exact shape of RL349's
still-open orientation/sign bridge.

## Session budget

**6 sessions.** Not extendable by the AI's own judgment. If session 6 ends
without a STOP verdict (see below), the program pauses and returns control to
the user — it does not auto-continue.

## What every session must do, in order

1. **State the current candidate Bridge Theorem explicitly.** One precise
   statement: "if X holds for an arbitrary hypothetical cycle, then [already-
   proved local machinery] forces a contradiction." Not a roadmap description
   — an actual falsifiable mathematical claim.
2. **Attack it.** Genuinely try to build a countermodel or structural
   obstruction to that exact statement — the way RL20 built an explicit
   184-bit word to kill the radius-3 bridge. This is not "raise a concern
   about scope." It is: try to construct, or prove the impossibility of
   constructing, an object that satisfies every already-proved local
   condition but escapes the Bridge Theorem. Full effort is required before
   any stop verdict is permitted (see Prohibited moves).
3. **Record the outcome in `LEDGER.md`** — see template below. No session
   closes without a ledger entry.
4. Only after 1–3 are done for the session may any local/finite work
   (tightening O_75, certificates, etc.) happen, and only if it is explicitly
   justified in the ledger as narrowing what a future Bridge Theorem attempt
   would need to cover. Local work with no stated connection to the Bridge
   Problem does not happen in this program.

## Strikes

A strike is logged in `LEDGER.md` when a session:

- reveals a new required lemma with the same local-doesn't-imply-global shape
  as a previously-failed bridge, without having closed the prior one, or
- cannot produce a concrete, falsifiable Bridge Theorem statement to attack
  (stayed purely in local/finite computation), or
- reports a change in confidence/percentage with no corresponding, specific,
  named reduction in an open obligation.

**Three strikes at any point → the next session must file a STOP verdict.**
This is mechanical, not a judgment call to be argued around in the moment.

## Verdicts

Any session may close `VERDICT.md` with one of:

- **CONTINUE** — a specific Bridge Theorem attempt survived genuine attack
  this session, or was only partially attacked and has a concrete next attack
  planned. State exactly what survived and what the next attack will target.
- **STOP — NOT VIABLE** — a defensible argument that no Bridge Theorem in
  this family can close the gap (e.g. a general countermodel, an
  impossibility argument, or a demonstrated recurrence of the same failure
  with no remaining candidate route). This is a valid, accepted, complete
  outcome — not a failure of the session.
- **STOP — INCONCLUSIVE** — budget exhausted, strikes not yet at 3, no
  countermodel or proof found either way. State plainly what is known and
  unknown.

A STOP verdict of any kind ends the program. It does not get argued back
into CONTINUE within the same run.

## Prohibited moves

- Declaring "not viable" without having attempted a genuine attack this
  session (i.e. skipping step 2). Giving up without trying is not permitted.
- Continuing to add local/finite machinery as a substitute for attacking the
  Bridge Problem.
- Starting any new named phase, gate, or roadmap stage without first stating,
  in the ledger, which specific Bridge Theorem it is meant to establish.
- Using "closed," "certified," or a percentage as evidence of anything in
  this program. The only currency here is: a stated Bridge Theorem, and
  whether it survived a genuine attempt to break it.

## Files

- `README.md` — this file.
- `LEDGER.md` — one entry per session, append-only, never edited retroactively.
- `VERDICT.md` — empty until a STOP is filed.
