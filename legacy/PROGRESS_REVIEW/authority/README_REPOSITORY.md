# Collatz / 3n+1 Research Repository

This repository contains an ongoing mathematical research project investigating structural approaches to the **Collatz conjecture**, with particular emphasis on ruling out hypothetical non-trivial cycles and understanding the arithmetic constraints such cycles would have to satisfy.

The project is exploratory research rather than a published proof.

For the current incoming handover and the worker-independent RL process, begin at [`START_HERE.md`](START_HERE.md).

## What is in this repository?

The work is organised as a sequence of research sessions. Each session may contain some combination of:

- mathematical derivations and lemmas;
- exact finite certificates and verification scripts;
- computational experiments;
- attempted proof routes;
- counterexamples to proposed intermediate claims;
- method barriers and abandoned approaches;
- corrections or demotions of earlier claims;
- handover documents describing the resulting research state and suggested next questions.

Later sessions build on earlier results, but the repository deliberately preserves historical work so that the development of the argument can be audited.

## Research conventions

The project distinguishes carefully between different kinds of results, including:

- **proved analytic mathematics**;
- **exact finite / machine-verifiable certificates**;
- **externally inherited computational results**;
- **computational evidence**;
- **conjectures and proposed lemmas**;
- **method barriers or dead routes**;
- **claims that have subsequently been corrected, weakened, or withdrawn**.

A statement appearing somewhere in the repository should therefore not automatically be interpreted as an established theorem. Its status should be read from the surrounding session documentation and proof-state records.

## Repository structure

The repository contains numbered research-session material together with handovers, verification code, supporting data, and archived intermediate work.

Recent handover bundles are designed to contain enough information for a new research session to continue without having to reconstruct the entire history from scratch.

Where supplied, checksum files and verification scripts are used to confirm that frozen research bundles and finite certificates have not changed.

## Mathematical setting

The standard shortened Collatz map used throughout much of the project is

\[
T(n)=
\begin{cases}
n/2, & n\text{ even},\\
(3n+1)/2, & n\text{ odd}.
\end{cases}
\]

Different parts of the repository study the problem using parity words, inverse trees, modular arithmetic, Diophantine approximation, cycle extrema, product identities, finite-state constructions, and related arithmetic structures.

Notation and specialised terminology are defined within the relevant session documents.

## Important note

This repository should be read as a **research record**, not as a claim that the Collatz conjecture has been proved.

The purpose is to develop, test, verify, reject, and combine possible mathematical routes while retaining a traceable record of what has and has not been established.

## Research provenance

This project uses AI-assisted mathematical exploration, drafting, code generation, verification, and research-state management. Mathematical claims are classified according to their proof or verification status rather than being treated as established because they were generated or reviewed by an AI system.

## Licensing and citation

Unless otherwise noted, source code and verification scripts are licensed under the MIT License, while mathematical research notes, documentation, reports, diagrams, and other non-code written material are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [`LICENSE.md`](LICENSE.md) for the licensing overview.

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Contributions and corrections are described in [`CONTRIBUTING.md`](CONTRIBUTING.md).
