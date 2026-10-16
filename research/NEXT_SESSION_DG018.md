# DG018 — Force a positive-exception obstruction beyond weighted complexity (READY; NOT EXECUTED)

**Authority:** Execute only on a subsequent explicit owner instruction "run next session". DG017 has been executed and closed. The target remains E empty for the ordinary positive-integer shortened Collatz map, NOT a cycle-only claim.

## Required reading

Read research/THEOREM_TARGET.md, PROOF_LEDGER.md, OPEN_GAPS.md, research/sessions/DG010.md section 4, DG011 sections 2–3, DG014 section 4, DG015 section 4, DG016 sections 1–5, DG017 sections 1–6, and research/verification/verify_DG017.py. Run python research/verification/verify_DG016.py and python research/verification/verify_DG017.py before building on their finite tests.

DG017's exact non-descending orbit upper bound is

\[
\frac{x_t+1}{m+1}\le W_m(t)
=\left(\frac32\right)^{s_t}
\left(\frac{m+2}{2(m+1)}\right)^{t-s_t}.
\]

For an unbounded E-orbit, equal length-h parity factors at p<q satisfy

\[
\max(W_m(p),W_m(q))\ge1+\frac{2^h}{m+1}.
\]

**Do not replace the max by W_m(q)** without independently establishing which of x_p,x_q is larger. That replacement is false on the actual finite trace 3->5->8->4. Shadow.lean already proves a refined odds-density floor; novel contribution from DG017 is not established.

## Aggressive mathematical assignments

1. **Primary global challenge:** Find an orbit-specific arithmetic obstruction for every *fixed ordinary positive* unbounded m in E, including those with exponentially many parity factors. The candidate should force (i) two actual suffix record-related factors contradicting the DG017 weighted collision inequality, or (ii) an integral positive strict-safe divergent off-spine inverse with guaranteed first original-orbit meeting in a DG010 two-gap window, or (iii) another unconditional mechanism killing this *individual* m. State precise quantifiers; do not merely construct 2-adic symbols.
2. **Weighted return geometry:** Prove, or kill with a completely verified positive finite countermodel, a concrete ordering hypothesis making the later-weight-only estimate valid for a carefully chosen set of record or parity-factor times. Quantify the improvement using the true numbers of odd and even steps along a fixed orbit, not a symbolic average. If no such fixed-seed argument works, exhibit the exact limiting inequality.
3. **Inverse-root frequency:** Test the high-complexity 7(mod9)-endpoint adversary against DG011's >=7 odd, >=11 total inverse shield. Separate: integrality; strict-prefix safety; smaller than the source record; divergent versus lifted; first-meeting within d_(j-1)+d_j; and injective counting across records. Derive a bound for |E intersect [2,X]| and explicitly compare its growth with o(X). A logarithmic increase is not contradictory.
4. **Bounded/preperiodic case:** Combine full hypothetical cycle arithmetic (2^L-3^s)y=Q>0 with a first external entrance y=2(mod3), integer entry-prefix formula, least-E visit floors, and m<=min cycle C. Seek a real all-words impossibility; otherwise classify the remaining conditional arithmetic precisely. Do NOT identify m, c=min C and z=(2c-1)/3.
5. **Originality/formalisation:** Compare candidates against msharpe248/collatz PrefixPower.lean, Ladder.lean, Shadow.lean, and López–Stoll (2009). If a nontrivial genuinely original candidate survives, give a compact Lean 4 target without assuming Collatz itself. Do not claim formal verification unless actually run.

## Adversarial mandatory tests

Use (a) DG016 high-complexity finite ternary Champernowne mountain prefixes (all completed endpoints 7 mod9); (b) arbitrary nonmountain positive parity cylinders; (c) unbounded possible record gaps, not merely the <=18 catalogue; (d) the DG017 3->5->8->4 weighted-max counterexample; and (e) finite 15->...->20 showing least-E floor cannot be applied to finite shadows. Never upgrade all-finite-prefix realizability to one fixed ordinary integer's infinite itinerary.

## Required closeout

Commit a mathematically complete DG018 report and any executed verifier, update PROOF_LEDGER.md, OPEN_GAPS.md, README.md, and prepare NEXT_SESSION_DG019.md as READY, **not executed**. Mark rigorously proved, refuted, unproved, externally known, computational, and Lean-certified claims separately. State whether E empty, originality, formal verification and publication-level achievement were actually obtained. Do not run DG019 automatically.
