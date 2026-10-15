# Independent progress review: through RL349

This directory is a frozen audit room for the Collatz-cycle research repository as of the committed end of RL349. It is deliberately outside the numbered RL research lifecycle. It is not a continuation prompt, a successor-session bundle, or a mathematical verdict.

The ultimate objective is to prove that the ordinary shortened Collatz map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

has no positive non-trivial cycle. The repository does not claim that this has been proved. The RL349 state records R1 / Parent Bridge as open, Phase 4 as open, Phase 5 as not started as authoritative work, and the global proof status as OPEN.

## Start here

1. [REVIEW_SCOPE.md](REVIEW_SCOPE.md) — boundary, inclusion policy, and snapshot identity.
2. [RL349_TRUTH_SNAPSHOT.md](RL349_TRUTH_SNAPSHOT.md) — the current claimed state in plain language.
3. [GLOBAL_PROOF_ARCHITECTURE.md](GLOBAL_PROOF_ARCHITECTURE.md) — the reduction from a hypothetical cycle to the present obligations.
4. [DEPENDENCY_GRAPH.md](DEPENDENCY_GRAPH.md) and [machine_readable/dependencies.json](machine_readable/dependencies.json) — the proposition-level route and its stopping point.
5. [CLAIM_INVENTORY.md](CLAIM_INVENTORY.md) and [OPEN_OBLIGATIONS.md](OPEN_OBLIGATIONS.md) — what is claimed, what is conditional, and what remains open.
6. [REVIEWER_GUIDE.md](REVIEWER_GUIDE.md) — how to challenge the claims independently.

The copied material in `authority/`, `historical/`, and `certificates/` is convenience evidence, not new authority. Each copy is tied to its original repository path and the RL349 snapshot commit in [provenance/SOURCE_MANIFEST.md](provenance/SOURCE_MANIFEST.md).

## Recommended verification order

Read the ordinary definitions and proof-state vocabulary, reconstruct the early local/global distinction from the RL18–RL20 material, then read the RL72/RL75/RL79 global audits. Next follow the R1/RL343–RL349 chain. Only after that inspect the finite verifiers and certificates. A green verifier confirms the exact finite proposition encoded by that verifier; it does not automatically establish the surrounding analytic scope or the global theorem.

Project labels such as RL numbers, Gates, Phases, “closed”, “certified”, and “authoritative” describe research state and provenance. Their mathematical content is translated in [TERMINOLOGY_CROSSWALK.md](TERMINOLOGY_CROSSWALK.md).

Reviewers should record challenges in a separate working copy or in [AUDIT_ISSUES.md](AUDIT_ISSUES.md) with a source pointer. Do not silently modify the copied mathematics or treat this package as permission to alter `authoritative/`.

## Package map

- `authority/`: current and load-bearing frozen sources selected from the RL349 snapshot.
- `historical/`: earlier sources retained because they explain reductions, barriers, route changes, or current dependencies.
- `certificates/`: small current verifier artifacts and exact data needed to understand the RL343/RL349 certificate chain.
- `machine_readable/`: claim and dependency records for programmatic traversal.
- `provenance/`: source paths, hashes, and snapshot identity.

This package reports repository claims and audit questions. It does not conclude that any Gate, R1–R7 stage, or the final Collatz theorem is independently verified.
