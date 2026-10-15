# RL19 session closeout

Date: 2026-08-20

## 1. Radius-3 result

The final one-orbit cubic leaf `gcd(A,L)=3, gcd(A,m)=1` has an analytic closure proof in `RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md`.

A strengthened verifier initially found a **real omitted boundary**: skew triples with one gap exactly `a` (smallest pattern type `(1,2,3)` at `a=2`). Work stopped and the proof was repaired rather than ignoring the failure. The repaired proof isolates this boundary and excludes it with the short-order lemma `rho^h != 1 (mod C)` for `0<|h|<a`.

After repair, `verify_rl19_cubic_skew_closure.py` passes the weak-interlacing criterion, RL10 structural conventions, the one-gap-`a` boundary, the interior Eisenstein lift, the two extreme resultant sectors, and equal-gap nonprimitivity.

Status: **CLOSED for primitive words**, conditional on the inherited audited RL10/RL17 reduction chain and older dependencies in other radius-3 branches.

## 2. Global results

RL remains **OPEN**.

New analytic identities/results:

- exact positive lift `Z=(lambda-1)(4R+1)`;
- arbitrary-radius weighted difference
  `sum q_i(3^(-G_i)-1)=4(lambda-1)(R_m-R)`;
- exact odd/even weighted populations;
- least-state parity-separated state packing;
- exact odd-step product
  `lambda=prod_(d_i=1)(1+1/(3x_i))`;
- strengthened logarithmic bound
  `log lambda <= 1/(3R#)+(1/6)log(1+2(L-1)/R#)`.

These force a near-resonance/huge-length dichotomy but no contradiction.

## 3. Routes pruned

- Positivity of the entire raw RL18 orbit sum cannot be the global contradiction because its exact positive quotient is known.
- Local root/final-return grammar does not currently provide a proved bridge to bounded transposition radius.
- An in-session length-184 countermodel was found against the local-grammar-only bounded-radius hope, but its exact word was not preserved as an artifact. Therefore this handover does **not** elevate that countermodel to an exact certificate. Reconstruct it next session before formally retiring the bridge.
- Enlarging the old cubic `a<=80` scan is unnecessary and must not be used as proof.

## 4. Distances

### Exact radius 3

**Closed**, modulo the inherited audited reduction chain. The next session should audit the new closure once, then avoid redoing it absent a failure.

### Actual RL contradiction

**Open and still substantial.** No theorem forces an RL object into radius 3. The best global progress is the new exact weighted/product structure and near-resonance/huge-length dichotomy.

## 5. Best next move

Try to combine the logarithmic upper bound depending on `R#` with the lower-bound/arithmetic structure of `A log2-L log3`, while simultaneously exploiting RL-specific root/final-return ownership. A failed global route with a frozen counterexample is preferable to a new unexplained cutoff.
