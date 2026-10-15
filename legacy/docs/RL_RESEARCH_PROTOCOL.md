# RL research protocol

`AGENTS.md` is the binding contract. This document is the on-demand procedure for the research phase; it does not replace or weaken that contract.

## Conveyor and job start

The conveyor is:

`authoritative/` → one incoming RL job → verified freeze in `sessions/RL.../` + successor `authoritative/`

The single incoming state is `authoritative/`. Frozen sessions and `Archive/` are provenance, not startup material. Conversation history and ignored scratch work are non-authoritative.

Complete the start gate in `docs/CODEX_OPERATIONS.md` before mathematics. Record `BASE_HEAD`, the generated authoritative snapshot, incoming RL, exact target, named proof/correction ledgers, red teams, and verifier commands. Once the incoming integrity and fast checks pass, apply verification economy: do not replay expensive history unless a live dependency, verifier failure, contradiction, repair event, or explicit handover instruction requires it.

Connector workers additionally follow `docs/CONNECTOR_WORKFLOW.md`: pin `BASE_HEAD` plus authoritative tree identity, keep a compact resume state, and reuse the validated startup gate on later `continue` turns while that identity remains unchanged.

## Research working area

Work only under:

`.rl-work/RL<incoming_rl>/`

The standard checkpoint created by `tools/rl_conveyor.py init-checkpoint` contains:

- `CHECKPOINT.md`;
- `STATE.json`;
- `commands.log`;
- `authoritative-snapshot.json`;
- `artifacts/`;
- `CLOSEOUT_STATE.md` when closing.

Connector workers keep the equivalent compact resume/closeout state in sandbox artifacts. These files are ignored/non-authoritative and only as durable as the environment that stores them. If guaranteed cross-machine survival of unfinished work is needed, use a separate user-approved non-authoritative branch or external artifact/issue store. Never weaken the no-partial-promotion rule to preserve scratch work.

## Bounded continuation work units

A kickoff research turn or bare `continue` executes one coherent bounded continuation work unit. The preferred endpoint is still a meaningful mathematical checkpoint: theorem-sized advance, exact certificate/material contraction, repaired claim, decisive barrier, useful invariant, or another coherent result that materially changes the live attack.

Do not stop at trivial algebra, tiny count changes, routine lookups, or other micro-steps merely to shorten a turn. But a theorem-sized endpoint is not a requirement to keep one interactive turn running indefinitely.

If substantial useful work has become durable and the next meaningful endpoint requires another expensive branch, long computation, or long connector/tool chain, checkpoint the exact frontier and return control. The next `continue` must resume from that frontier without reconstructing authority or repeating completed work.

Before an expensive branch, record inputs, intended output, resource/range bounds, and resume plan. After a material intermediate result, update the checkpoint before beginning another expensive branch.

## Checkpoint discipline

Refresh the checkpoint after any materially useful event, including:

- a meaningful exact scan batch;
- a theorem or lemma candidate;
- exact interval propagation;
- a support-edge/geometric crossover or new live minimum;
- a correction or demotion;
- a verifier milestone;
- before and after a long computation;
- before a route switch;
- before a long connector sequence;
- before a likely context, credit, or environment boundary;
- immediately before or on entry to `CLOSEOUT_LOCK`.

At minimum record:

- `BASE_HEAD`, incoming RL, authoritative target, and timestamp;
- authoritative tree/snapshot identity;
- files actually needed by the live attack;
- last fully verified mathematical checkpoint;
- new results with their recorded classification and exact scope;
- completed finite certificates with gap-free ranges;
- incomplete computations marked **NOT PROMOTED**, including exact uncovered ranges;
- current live constants, minima, floors, or endpoints when relevant;
- verifier commands run and results;
- failed commands, counterexamples, and abandoned routes;
- files/artifacts produced and hashes where useful;
- exact next intended command/operation;
- things explicitly not to recompute;
- whether stop-and-repair is active.

A successful local milestone is a checkpoint, not automatically a promotion trigger. Continue through adjacent productive work while the route remains useful, exact verification is reliable, scope remains controlled, and closeout capacity is safe; return control once the current coherent work unit is durably complete and another costly branch would materially enlarge the failure domain.

## Proof-state and scope discipline

Use the categories in `docs/PROOF_STATE_CLASSIFICATIONS.md`. Preserve every branch qualification and named red team carried by the handover. Do not restart a recorded dead route unless the live target explicitly reopens it or genuinely new structure invalidates its recorded barrier.

A finite computation is exact only when its claimed range is gap-free and reproducible. If a parallel or chunked run partially fails, retain completed chunks only when individually trustworthy, record the precise missing ranges, rerun those ranges safely, and promote nothing until aggregation proves full coverage.

On an integrity failure, follow `docs/RL_STATE_MACHINE.md`. Mathematical invalidity may require an explicit correction/demotion. A mechanical checksum, packaging, transport, catalogue, or tooling defect is recorded and repaired mechanically and does not by itself change proof classification.

## Compute discipline

Use compute aggressively but reproducibly without consuming the closeout reserve. Prefer:

- deterministic exact arithmetic when proof state requires it;
- bounded parallelism over uncontrolled oversubscription;
- chunked scans with explicit ranges;
- resumable, machine-readable outputs;
- checksums and manifests;
- independent aggregation and verifier passes.

Before a long run, checkpoint its command, input range, expected outputs, resource bounds, and resume plan. After it ends, record completed and uncovered ranges before starting anything else. Do not launch a new long computation if it could prevent a clean closeout or if the current turn already has a durable meaningful frontier that should be returned to the user first.

## Sustained attack and closeout reserve

An RL job should remain auditable, but a successful theorem, scan chunk, endpoint elimination, support change, or local milestone does not by itself require closing. Continue adjacent productive steps while correctness and capacity remain healthy.

Reserve sufficient context, compute, and tool capacity for classification, packaging, fresh-unpack verification, atomic promotion, remote-ref advancement, and post-commit readback. When capacity can be estimated, approximately the final 15–20% is reserved for closeout. Otherwise act conservatively after a meaningful result or verifier milestone. A marginal extra result is lower priority than a complete transition.

When the lock trigger in `AGENTS.md` occurs, stop research and load `docs/CLOSEOUT_LOCK.md`. Do not interleave research with closeout.

## Portability

Assume the next worker is a different system with no conversational memory. Never make “as discussed above” load-bearing. A promoted handover must state all required definitions, constants, scope, dependencies, obligations, corrections/demotions, external-certificate provenance, exact verifier commands, and next target in repository files.

The repository is the state machine. Transcripts may be optional context but cannot carry proof state.

## Multiple RL jobs

After a successful atomic transition and remote readback, treat the successor `authoritative/` as a fresh incoming generation. Record a new `BASE_HEAD`, rerun the start gate, and begin another job only if enough capacity remains for its complete closeout. Each numbered transition has its own commit; never combine several RL jobs into one transaction.

## Final reporting

For a fully promoted RL job, report succinctly:

- completed incoming RL;
- main mathematical advances;
- any correction/demotion;
- exact new frontier or endpoint where relevant;
- verifier and fresh-unpack status;
- successor RL and target;
- promotion commit SHA;
- confirmation that the intended remote branch/ref points at it.

For an unpromoted job, report instead:

- no authoritative transition was committed or pushed;
- the last committed incoming authority remains unchanged;
- the last fully verified local checkpoint;
- exact incomplete work remaining unpromoted;
- exact durable resume frontier and next operation.

Never describe uncommitted or unpushed work as authoritative.
