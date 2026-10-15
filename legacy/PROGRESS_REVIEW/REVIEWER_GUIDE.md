# Guide for an independent reviewer

Treat this package as evidence to challenge, not as a proof certificate. In particular, do not trust a claim merely because it is labelled authoritative, green, closed, certified, inherited, or proved in a ledger.

For every important claim:

- restate the proposition without project shorthand;
- list every hypothesis and identify whether it is global, branch-specific, conditional, or finite;
- check that the cited proof establishes the exact conclusion and quantifiers;
- distinguish equivalence from implication, necessary conditions from sufficient conditions, and contradiction assumptions from definitions;
- check degenerate cases, boundary indices, row/wrap conventions, and primitive/non-primitive reductions;
- verify that a finite computation covers exactly the claimed domain and that the verifier is independently meaningful;
- trace each downstream use back to a source that proves no stronger statement than it actually does;
- test whether a normalized or generalized-increment argument still holds for `s != 1`;
- check that local, branch, selector, and first-survivor results are not promoted to global statements;
- inspect correction/demotion ledgers for every apparently stronger historical claim;
- and finally verify the implication back to the ordinary Collatz map, including all `g=1`, `g=2`, and `g>1` cases required by the roadmap.

## Suggested order

Begin with the definitions and `PROOF_STATE_CLASSIFICATIONS.md`. Reconstruct the early radius-3/global distinction from RL18–RL20. Read the RL72/RL75/RL79 audit material to understand the major method barriers. Read the RL314 audit for the late global scope map. Then follow the RL343–RL349 sources in order and reproduce the small current verifiers. Use `AUDIT_ISSUES.md` as a checklist, not as a conclusion.

Keep independent findings separate from the snapshot. If a source is ambiguous, record the ambiguity and the exact citation; do not silently repair the theorem or alter the package’s copy.
