# Global proof architecture

## Starting question

Assume a positive non-trivial cycle of the shortened Collatz map. The ordinary proof task is to derive a contradiction while preserving the cycle’s exact parity, integrality, least-state, and ownership constraints.

## Main mathematical translation

1. Encode one complete cycle by a cyclic binary parity word of length `A` with `L` odd steps. The affine composition gives the denominator-like quantity `D = 2^A - 3^L` and a word numerator `Q`.
2. A genuine integer cycle must satisfy the recorded full-denominator divisibility/ownership conditions, not merely a word-level slope or local grammar condition. The least state selects a distinguished rotation and supplies inequalities on proper prefixes/suffixes.
3. Local tools study rotation distance, sparse polynomial/resultant identities, valuation patterns, inverse gaps, q-profiles, phase tags, and physical states. Each tool has a scope: local, branch-specific, finite, conditional, or global.
4. The early radius-3 line established a local contradiction engine, but RL20 gave an exact non-cycle word satisfying the extracted local grammar while avoiding radius 3. Thus a separate global bridge is required.
5. The Gate-A line studies terminal valuation/rank/ownership and full-phase selectors. The Gate-B line studies full-denominator/ownership-sensitive encounters with bounded local obstructions. Historical audits emphasize that closing one Gate or one branch does not automatically close the other.
6. The later R1 line instead builds a full physical two-row canonical walk for an ordered genuine `g=2` parent branch. The q-profile and phase-potential machinery turns a hypothetical parent cycle into a set of phase-potential-nondecreasing complete returns. The obstruction `O_75` is the exact set of returns that have not yet been shown impossible or descending below the least state.

## Type of each transformation

| Transformation | Logical type at the recorded scope | Audit caution |
|---|---|---|
| Cycle → parity word / affine identity | Encoding/equivalence subject to stated cycle hypotheses | Check primitive, positivity, and denominator assumptions. |
| Word divisibility → `D \mid Q` / ownership | Necessary condition for a genuine integer cycle | Word identities also hold for generalized-increment or fake families. |
| Radius-3 case analysis | Local implication | Does not supply an encounter theorem for arbitrary cycles. |
| Gate-A reductions | Conditional reductions within selected terminal/full-phase architecture | Branch selectors must be proved for every hypothetical cycle before global use. |
| Gate-B local consumers | Local contradiction/sufficient obstruction once encounter hypotheses hold | The global encounter/ownership bridge is separate. |
| RL343 full physical bridge | Analytic bridge within the inherited ordered genuine `g=2` parent scope | Does not cover all `g=2`, all `g>1`, or `g=1`. |
| Phases 1–3 | Exact methodological/profile reductions and one promoted terminal certificate | “Phase closed” means the prescribed reduction stage, not global cycle elimination. |
| Phase 4 | Singleton/interface/CRT/ownership/descent residual | `O_75` remains open. |
| R1 → R2–R7 | Proof architecture, not yet discharged mathematics | Each transition has its own theorem-level criterion. |

## Current stopping point

The most explicit current live chain is:

`ordered genuine g=2 parent`
→ full two-row q=0 canonical walk
→ phase-potential-nondecreasing complete-return obstruction `O_75`
→ [missing] eliminate every short, half-cycle, and over-half residual with all row/wrap/CRT/ownership hypotheses
→ R1 closure.

The missing arrow is not filled by RL349’s arithmetic diagnostic because the orientation/sign antecedent was not proved.
