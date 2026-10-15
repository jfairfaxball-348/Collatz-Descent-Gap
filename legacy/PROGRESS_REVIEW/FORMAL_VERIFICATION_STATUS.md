# Formal verification status

The repository contains executable Python verifiers and exact finite certificates. Those are not the same as a formal proof in Lean, Isabelle, Coq, or another proof assistant.

The curated sources available here show no completed external formalisation of the global Collatz no-nontrivial-cycle theorem. The package therefore records:

- **Formalised global theorem:** not identified in the snapshot.
- **Formalised local theorem:** not identified in the snapshot; executable verifiers are present, but their proof-assistant status is not established by repository evidence.
- **Executable exact verification:** present for selected finite arithmetic, profile, bridge, and red-team artifacts.
- **External mathematical dependency:** RL18/RL19 sources explicitly refer to an external LMN/logarithmic-form theorem in their local proof chain. Its use, exact statement, and imported hypotheses require independent checking.

A future reviewer should not infer whole-program formal verification from the presence of a verifier, a green closeout, or the word “certified”. If an external Lean repository is later supplied, record its exact commit, theorem names, imported axioms, and the precise research claim it formalises. Do not widen a local formalisation into verification of R1–R7.
