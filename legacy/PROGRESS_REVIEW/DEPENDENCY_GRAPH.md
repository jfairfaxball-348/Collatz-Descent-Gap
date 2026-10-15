# Dependency graph

## Human-readable route

```text
ordinary shortened Collatz map
  -> hypothetical positive non-trivial cycle
  -> primitive parity word / affine full-D encoding [C01]
  -> genuine full-D ownership and least-state constraints [C02]
  -> one or more global closure architectures
       |-> Gate A terminal/full-phase route [C06, OPEN globally]
       |-> Gate B ownership/encounter route [C07, OPEN globally]
       |-> direct R1 parent bridge [C09]
              -> inherited ordered genuine g=2 parent
              -> full physical two-row bridge [C10]
              -> endpoint/terminal/profile reductions [C11-C17]
              -> exact owned nondecreasing-return obstruction O_75 [C18]
              -> eliminate O_75 [OPEN]
              -> R1 closure
              -> R2 -> R3 -> R4 -> R5 -> R6 -> R7
              -> end-to-end contradiction
```

## What stops the chain

The current direct R1 chain stops at `O_75 = empty`. RL349 names the first missing theorem in the `L=ell` residual as the directed half-cycle orientation/sign bridge. The shorter `75 <= L < ell` class and the over-half class remain open as inherited residuals. The current record does not justify replacing these three residual classes with a single numerical inequality.

## Scope flags

- C03 is local; C04 explicitly blocks the inference from local grammar to global encounter.
- C06 and C07 are architectural branches, not two halves already proved.
- C10–C17 are restricted to the inherited ordered genuine `g=2`, `Z0>0`, `K<0` parent and carry additional ownership, high-carry, row, and conditional least-state hypotheses.
- C20 is arithmetic support, not the missing bridge.
- No edge in the graph should be read as an equivalence unless the source explicitly says so.

The machine-readable edge list is in `machine_readable/dependencies.json`.
