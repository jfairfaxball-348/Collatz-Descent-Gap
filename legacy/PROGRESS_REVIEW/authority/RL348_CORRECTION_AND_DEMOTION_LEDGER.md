# RL348 correction and demotion ledger

Date: 2026-09-18
Status: CLOSED/FROZEN

## 1. Half-cycle `2m` strengthening not promoted

Live RL348 scratch proposed that both nondecreasing half-cycle contact endpoints satisfy
`m<=S<E<2m`, which would sharpen the even difference bound to `D<=2^36-2`.

That strengthening was not frozen with a complete orientation proof during RL348 and is therefore
NOT PROMOTED. The authoritative half-cycle state bound remains the RL347 result

`2<=D<=2^36`, `D` even.

Consequently the promoted physical parity-synchronization window is at most 36 binary phases, not
the stronger scratch value 35.

This is a proof-state conservatism decision, not a demotion of inherited authority.

## 2. Equal-gap contact is not automatically q=0

A live shortcut considered whether a `(1,1)` matched-gap step from a q=0 contact would immediately
create another q=0 contact and contradict completeness.

The step does preserve matched contact, but the next contact may lie at positive profile height.
Therefore no completeness contradiction is promoted from contact preservation alone.

## 3. Correct pre-crossing count

The valid inherited crossing-to-root strict-rank bound is

`K_+>=3n-4`.

A transient scratch expression `3n-3` was one unit too strong and is NOT used. At the inherited
floor the promoted value is

`3*20390252058-4=61170756170`.

## 4. Correct post-crossing complement integer boundary

The valid RL348 post-crossing calculation gives

`t > 23135982579.518...`

and hence

`t>=23135982580`.

No `t>=23135982581` or `R>=23135982581` statement is promoted.

## 5. Source-side residual inequalities remain scratch

Late in RL348, source-side decompositions relating the over-half residual length, source
displacement, normalized H-carry defect and terminal excess were explored. They were not integrated
with every inherited orientation/ownership acceptance test before CLOSEOUT_LOCK.

They are preserved only in `RL348_SCRATCH_FRONTIER.md` as diagnostics for RL349. They are not
authoritative theorems.

## 6. No inherited theorem demoted

RL348 makes no correction or demotion to the committed RL342--RL347 authority.
