# DG008 — pressure-test 11-step inverse sieve and positive-orbit record recurrence (READY; NOT EXECUTED)

**Authority:** A new user instruction to "run next session" executes **DG008 immediately**, not DG009. No extra confirmation. Work strictly on \(E=\varnothing\), the Terras–Everett descent gap for the standard shortened positive Collatz map. No cycle-only diversion, arbitrary parity-profile games substituted for positive integers, forced audits, or huge uninformative brute force.

**Read first:** research/THEOREM_TARGET.md; research/sessions/DG007.md; research/PROOF_LEDGER.md; research/OPEN_GAPS.md; research/verification/verify_DG007.py. Respect the distinction between all-E inverse lemmas, restrictions on \(\min E\), *conditional unbounded* E-record lemmas, and finite local bridge counterexamples.

## Inherited results and hard obstruction

DG007 proves genuine unbounded exceptional-record gaps \(2,4,5,7,8,10,12\) impossible; d9 has seven local forms and d11 thirty. The genuine additive lower bound now counts distinct off-spine safe roots from long 2-mod-3 records and long \(4\bmod9\) records. But there is **no lower bound on the frequency** of either type. The 11-step strict-prefix inverse sieve newly rules out eight classes of \(\min E\) modulo 2187, taking exclusions from 1005 to 1013 out of 2187 odd classes; these exclusions are not exclusions of all E. Arbitrarily long finite *mixed* all-1-mod-3 bridge schedules remain positive-integer realisable, but that does **not** give an infinite positive exceptional orbit.

## Central DG008 decision

Aim for a genuine new theorem of either kind:

(A) Prove an actual positive-integer exceptional record tail cannot eventually avoid *both* inverse-generating classes \(2\bmod3\) and \(4\bmod9\), or prove a growth lower bound for their disjoint inverse descendants that is incompatible with natural-density-zero E; **or**

(B) Deduce non-circular least-exception exclusions on additional residue classes beyond the DG007 1013/2187, with a fully general positivity/safety proof valid even if E contains cycles; **or**

(C) Derive a necessary *global* compatibility invariant of one fixed positive seed that eliminates a nontrivial family of genuine infinite exceptional record schedules (not merely periodic/nonpositive 2-adic itineraries).

Do not imply that success at (B) alone completes (A) or the universal target.

## Mathematical attempts to execute

1. **Competing inverse words, global collisions:** For actual records b, build inverse trees containing odd and even predecessors, prove every counted root has a safe finite path from root to its first spine intersection, and organise collisions by this first-intersection time. Specifically investigate b≡1(mod9), b≡7(mod9) and longer safe words from 1-mod-3 targets. Try deriving extra distinct roots *uniformly* or explicitly falsify any density inference.
2. **Beyond eleven-step least-E sieve:** Exhaustively enumerate strict-prefix words through a defensible larger finite depth, with a concise exact generating algorithm, and isolate residue classes newly added versus 1013/2187. For each new word display affine (A,q,D), endpoint class, the first positive odd representative and a complete proof of safe integer realisation. Identify whether additions merely shrink a density of candidate minimum residues or eliminate an entire remaining family, including 0-mod-3 minima. Do not call residue percentages a Collatz proof.
3. **Actual bridge constraints:** Extend the symbolic local bridge classifier to d=13..18 and extract provable general structural restrictions (odd counts, allowed gaps, mod9 targets). Then test concatenation against *one fixed source* with exact 2-adic congruences and real-growth inequalities. Construct positive finite mixed counterexamples when claimed global obstructions fail; don't promote them to E endpoints.
4. **Least-element first-gap sharpenings:** Use the DG007 new rule \(m≡3\bmod8\), \(d\ge6\), \(b≡4\bmod9\) impossible, and the DG006 first-long-2-mod-3 prohibition. Attempt to eliminate a whole first-transition cylinder or to prove a quantified first-gap obstruction not subsumed by the existing inverse sieve. Show nonredundancy carefully.
5. **Quantitative falsification:** Provide a specific sparse possible record schedule respecting all known *numerical* restrictions, or show a proposed dynamic invariant really rules it out. Distinguish abstract schedules, bona fide finite positive segments, and genuine exceptional infinite trajectories.

## Verify and close

- Write research/sessions/DG008.md with exact hypotheses, derivations, counterexamples, test outputs, and honest impact on E. If a claim is genuinely new, amend research/PROOF_LEDGER.md and OPEN_GAPS.md; add exact arithmetic verifier only if actually run.
- Prepare the *full* NEXT_SESSION_DG009.md for the later user invocation, but **do not run DG009**.
- Commit research results and provide verified clickable GitHub file/commit links. No Lean/Palomar claims without actual external certificates, and never assert \(E=\varnothing\) absent a full proof.
