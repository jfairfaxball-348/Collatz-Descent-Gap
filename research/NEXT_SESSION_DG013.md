# DG013 — Oscillating mountain itineraries and the actual-E bridge gap (READY; NOT EXECUTED)

**Authority:** The owner's next "run next session" executes DG013 only. Do NOT silently execute DG014. The unique target remains \(E=\varnothing\) for the standard shortened Collatz map; do not replace it by a mountain-only problem.

## Mandatory reading

- research/THEOREM_TARGET.md; research/sessions/DG011.md and DG012.md;
- research/PROOF_LEDGER.md, research/OPEN_GAPS.md;
- research/verification/verify_DG012.py, research/sessions/DG010.md §4.

DG012 proves: (i) fixed-n strict mountain record parameter bound \(r_j<\mu^2j+\mu\log_2(n+1)\), \(\mu=\log_2(3/2)\); (ii) repeated word divisor \(2^{K(s+r)}\mid(3^s-2^{s+r})x+(3^s-2^s)\); (iii) no infinite eventually nondecreasing mountain r list can occur on ONE positive orbit. **None** implies no oscillating list, no arbitrary actual E record gap, or no bounded/preperiodic E.

## Aggressive direct proof goals, in order

1. **Try to remove monotonicity, not merely extend constants.** Develop an arithmetic potential or exact congruence involving *nonconsecutive repeated words*, especially with interspersed short r=5 blocks, that proves nonrealisability for a new oscillating infinite mountain class. Try \(r_{2j}=5\), \(r_{2j+1}=5+6\lfloor\log_2(j+2)\rfloor\) (or an exact bounded-run aperiodic 5/11 schedule). Exhibit a rigorous obstruction on a fixed positive n, or show why the DG012 plateau bound and odd-run budget cannot exclude it. Separate finite-prefix CRT shadows from fixed-positive orbits.

2. **Attempt ALL mountain itineraries.** Either prove no positive integer can follow any infinite strict mountain list (allowing arbitrary oscillation), or provide a precisely stated indispensable missing inequality/countermodel showing why the attempted proof does not work. A theorem covering all mountain lists would remain conditional for E unless arbitrary E records are shown to decompose into mountain words.

3. **Reconnect to arbitrary genuine E record bridges.** From strict suffix-minimum conditions derive a recurrence or alternative inverse-root production theorem that applies irrespective of mountain shape and regardless of unbounded record gaps. Quantify first spine meeting/disjointness and growth strongly enough to challenge Terras–Everett's o(X), **or** attack least E divisible by3 including the preperiodic bounded-cycle scenario. Do not assume all gap lengths are ≤18, 7(mod9) endpoints, an all-odd prefix, or a positive proportion of off-spine roots.

4. **Adversarial audit.** Check repeated-block modular arithmetic is not mistaken for an independent constraint, that any constructed positive integer is finite-horizon only unless proved otherwise, and that affine endpoint positivity and parity-cylinder membership are rigorously established. Run local deterministic exact checks; optionally add independent verifier. A conditional theorem is not a universal Collatz proof.

## Exit

Deliver a proved theorem (with all quantifiers), a mathematically specific falsification, or a precise obstruction/conditional reduction; choose genuine proof pressure over paperwork. Update research/sessions/DG013.md, ledger, gap file, README, verifier as warranted. Create DG014 READY but do not execute it. State plainly whether E=empty, bounded/preperiodic least E, and an arbitrary oscillating mountain tail are still open. Preserve DG012's full proof and scope.
