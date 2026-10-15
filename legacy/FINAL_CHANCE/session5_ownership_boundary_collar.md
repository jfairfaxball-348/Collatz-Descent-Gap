# FINAL_CHANCE Session 5 — ownership boundary-collar bridge

Date: 2026-09-18

Status: **ATTEMPTED, PENDING INDEPENDENT VERIFICATION**

Incoming cumulative strikes: **2/3**.

Scope: the fixed first-survivor `g=1` branch

[
A=217976794617,qquad L=137528045312,
]

with the inherited nonnegative defect path

[
h_j=leftlfloor rac{Aj}{L}ightfloor-S_j,
]

full ordinary physical ownership, least-rooting, the internally proved
`m<2^75` ceiling for `g=1`, and the inherited external least-cycle input
`mge 2^71`.  As elsewhere in the project, the lower bound remains
externally sourced/computationally classified.

Session 4 killed the attempt to deduce a height-independent contradiction
from residue-order sparsity, degree, or Parseval norm alone.  Session 5
therefore attacks ownership through the exact physical state at the two ends
of the defect excursion.

## 1. Bridge Theorem attempted

Let `p` be the first phase with `h_p>0`, and let `q` be the last phase
with `h_q>0`.

The attempted Session 5 Bridge Theorem is:

> **Two-sided boundary-cylinder bridge.** For every hypothetical fully owned
> `g=1` first-survivor defect excursion with `sum h_j>=3`, the exact
> 2-adic cylinder forced by the first positive defect and the exact 3-adic
> cylinder forced by the last positive defect are incompatible, inside the
> inherited least-state window, with the actual forward accelerated Collatz
> orbit and nonnegative-defect/least-root conditions.  Hence no such owner
> exists.

The full theorem is not proved in Session 5.  A global, height-independent
reduction is proved:

[
oxed{p+(L-q)le 37.}
]

Thus every surviving owner must have its first positive defect and last
positive defect inside a total cyclic boundary collar of width at most 37.

This is not an area cutoff, a height cutoff, or a bound on the number of
defect components.

## 2. First-defect cylinder

Write

[
b_j=leftlfloorrac{Aj}{L}ightfloor,qquad
c_j=b_{j+1}-b_jin{1,2}.
]

The accelerated exponent is

[
a_j=c_j+h_j-h_{j+1}.
]

If `p` is the first positive defect phase, then

[
h_0=cdots=h_{p-1}=0.
]

Because rises are at most one, necessarily

[
h_p=1.
]

Therefore the first `p-1` exponents are mechanical and the `p`-th
exponent is exactly one.  This fixes the least state `m` in one exact
2-adic cylinder modulo

[
2^{b_p}.
]

The oddness of the phase-`p` state selects one of the two possible lifts
from modulo `2^{b_p-1}` to modulo `2^{b_p}`.

There is also a universal early bound.  If no positive defect occurs through
phase 47, then the exact mechanical prefix through phase 47 has only one
least-state candidate in the inherited window:

[
m=23587405242550913489915.
]

Its actual next accelerated step has negative defect at phase 48.  Hence every
physical owner satisfies

[
oxed{ple47.}
]

The possible first-defect phases through 47 are exactly

[
2,4,6,7,9,11,12,14,16,18,19,21,23,24,26,28,30,31,33,35,36,38,40,42,43,45,47.
]

## 3. Last-defect cylinder

Put

[
n=L-q.
]

If `q` is the last positive defect phase, then

[
h_{q+1}=cdots=h_L=0.
]

Over the final `n` accelerated steps the exact cycle-closing affine equation
has the form

[
2^T m = 3^n y_q + C.
]

Therefore

[
mequiv 2^{-T}Cpmod{3^n}.
]

This gives an exact 3-adic least-state cylinder.

The only remaining datum from the potentially enormous terminal height
`h_q` is its parity.  If `h_q` is increased by two, the extra factor four
appears in every post-first-term power of two and cancels against the total
`2^T`; the exceptional first term is multiplied by `3^{n-1}`, so modulo
`3^n` only `2^{-h_q} mod 3` remains.  Thus the suffix residue depends only
on

[
h_qmod2.
]

This is checked exactly for every `1le nle48` by the verifier.

If the last positive defect occurred before phase `L-48`, then the final 48
defect heights would all be zero.  The exact mechanical final-48 suffix gives
one residue modulo `3^{48}`, but that residue has no representative in

[
[2^{71},2^{75}).
]

Hence every physical owner satisfies

[
oxed{L-qle48.}
]

## 4. CRT attack on the two boundaries

For every admissible first-defect phase `ple47`, every

[
1le n=L-qle48,
]

and each of the two parities of `h_q`, combine:

- the exact first-defect cylinder modulo `2^{b_p}`;
- the exact last-defect cylinder modulo `3^n`.

The moduli are coprime, so CRT gives one exact state progression modulo

[
2^{b_p}3^n.
]

The Session 5 attack tests every boundary signature with

[
p+nge38.
]

For each CRT progression, every representative in the complete inherited
least-state window is generated exactly.  The actual accelerated Collatz orbit
is then followed; a candidate is rejected as soon as either

[
h_j<0
]

or

[
y_j<m.
]

This is a finite computation over the state window, but it is not a
defect-area or defect-height enumeration.  It covers arbitrary middle
excursion geometry compatible with the two exact endpoint cylinders.

The exact verifier checks:

- boundary signatures with `p+n>=38`: **1848**;
- state candidates across those signatures: **2,056,165**;
- distinct least-state candidates: **1,370,780**;
- every candidate is rejected;
- the latest rejection occurs by phase **194**.

Therefore no physical owner can have

[
p+nge38.
]

Since `n=L-q`,

[
oxed{p+(L-q)le37.}
]

## 5. Nature of the reduction

The theorem is uniform in:

- total defect area;
- maximum defect height;
- number of defect components;
- run lengths;
- interior phase positions.

The middle interval `[p,q]` remains unrestricted except for the inherited
physical grammar and ownership conditions.  The new theorem controls only
where the defect support begins and ends around the cyclic root.

This is genuinely ownership-specific information.  Session 4 showed that the
bare defect grammar cannot control residue-order complexity.  Session 5 uses
instead the exact least-state integer simultaneously seen from the physical
forward prefix and the physical closing suffix.

## 6. Exact residual family

After the theorem, only signatures satisfying

[
p+(L-q)le37
]

remain.

There are exactly **744** boundary signatures after including the two possible
terminal-height parities, supported on exactly **21** possible first-defect
positions.  The largest remaining first-defect phase is 36.

These 744 signatures are not 744 complete defect profiles: each still allows
arbitrary middle height/area/connected-component structure.  This is why the
result is a global structural reduction rather than an area-by-area screen.

## 7. What remains open

The full Two-sided boundary-cylinder Bridge Theorem is not proved.  The
surviving problem is:

> Can full ownership and the exact accelerated recurrence eliminate the
> 744 boundary signatures with `p+(L-q)le37` without enumerating middle
> defect area or height?

A productive final-session attack should use the now-fixed short boundary
collar as an exact interface to the full one-block ownership equation.  It
must not revert to the Session 4 sparse/degree/Parseval mechanism or to an
area-3, area-4, ... programme.

## 8. Verifier

Committed artifact:

`FINAL_CHANCE/verifiers/verify_session5_boundary_collar.py`

Literal verifier stdout:

```
FINAL_CHANCE Session 5 ownership boundary-collar verifier: PASS
A,L = (217976794617, 137528045312)
least-state window = [2^71, 2^75)
mechanical-prefix-through-47 candidates = 1
mechanical-prefix candidate fails nonnegative defect at phase = 48
first-defect positions <=47 = 27
mechanical final-48 suffix has state-window candidate = False
last-defect suffix depends only on terminal-height parity = True
boundary signatures attacked with p+(L-q)>=38 = 1848
state candidates checked across those signatures = 2056165
distinct state candidates checked = 1370780
latest rejection phase = 194
surviving owner must satisfy p+(L-q) <= 37 = True
residual boundary signatures = 744
residual first-defect positions = 21
scope=full-owner boundary reduction; no defect-area/height enumeration
```

The verifier uses exact integer arithmetic throughout.  No floating-point or
interval arithmetic is used.

Verification status: **ATTEMPTED, PENDING INDEPENDENT VERIFICATION**.
