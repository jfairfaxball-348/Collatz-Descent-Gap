# Proof-state classifications

`AGENTS.md` is binding. This document is the canonical vocabulary for promoted mathematical state and conservative result lookup.

Every handover must label new material using one of these recorded categories:

- **Proved analytic mathematics:** a stated theorem with a complete proof and exact scope.
- **Exact finite certificate:** a gap-free, reproducible finite computation with its exact range and verifier.
- **Externally inherited certificate:** a certificate accepted from a frozen incoming ledger after the required current integrity/fast checks; retain exact provenance.
- **Computational evidence:** observations or experiments that do not establish a theorem.
- **Conjecture / candidate lemma:** a proposed statement still requiring proof or disproof.
- **Method barrier / dead route:** a documented failure mode, obstruction, or countermodel limiting a strategy.
- **Repaired or demoted claim:** an explicit correction identifying the first invalid dependency, the reason, and the remaining valid scope.
- **Open obligation:** a condition required for a named target, Gate, branch, or global conclusion.

No finite evidence becomes an analytic theorem, no incomplete range becomes an exact certificate, no branch result becomes global, and no repair may be silent. A large finite elimination or successful branch cannot close a global Gate, all nontrivial cycles, or the Collatz conjecture unless the recorded inherited obligations are actually discharged.

## Classification sources

Proof status may be sourced only from designated canonical records, such as:

- current or frozen certified-facts/proof ledgers;
- correction/demotion ledgers;
- explicit session-state/completion documents;
- other files explicitly designated by a handover as status-bearing.

Ordinary report prose, filenames, catalogue entries, search snippets, and model judgement do not independently assign status. Catalogues copy status and point to sources; they do not replace them.

If canonical sources conflict, preserve every pointer and mark the lookup as requiring future mathematical review. Do not adjudicate, merge, strengthen, weaken, or reinterpret the claims during indexing or infrastructure work.

## Mechanical defects

Checksum, manifest, packaging, lossless transport, catalogue, path, and Git-tree defects are mechanical unless they reveal a distinct invalid mathematical dependency. Repairing a mechanical defect does not itself promote, demote, or otherwise change a mathematical claim.

A mathematical correction/demotion is required only when a recorded proof-state dependency is invalid. It must be explicit in the next legitimately promoted handover and must preserve the remaining valid scope.
