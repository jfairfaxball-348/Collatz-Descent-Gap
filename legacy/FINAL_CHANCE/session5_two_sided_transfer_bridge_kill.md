# FINAL_CHANCE Session 5 — two-sided ownership-transfer bridge killed

Date: 2026-09-18

## Status

**KILLED.**

This is a structural countermodel result.  It does **not** construct a cycle and
does **not** claim full ordinary ownership.  It proves that the exact
RL154-style two-sided transfer information, even when strengthened by the
physical least-state window and a complete legal nonnegative defect excursion,
still does not supply the missing global middle connection.

Cumulative FINAL_CHANCE strikes entering this session are **2/3** by explicit
user instruction.

## 1. Exact Bridge Theorem attempted

At the actual first-survivor counts

[
A=217976794617,qquad L=137528045312,
]

put

[
b_j=leftlfloor rac{Aj}{L}ightfloor,qquad
c_j=b_{j+1}-b_j.
]

The attempted **two-sided transfer closure bridge** is:

> There do not exist an odd integer
> [
> 2^{71}le m<2^{75},
> ]
> a complete nonnegative defect excursion
> [
> h_0=h_L=0,qquad
> a_j=c_j+h_j-h_{j+1}ge1,
> ]
> and physical endpoint states such that:
>
> 1. the first 75 exponents (a_0,ldots,a_{74}) are the exact accelerated
>    Collatz valuations of a genuine forward orbit starting at (m);
> 2. every state in that 75-step prefix is strictly larger than (m);
> 3. the last 75 exponents (a_{L-75},ldots,a_{L-1}) are the exact
>    accelerated Collatz valuations of a genuine physical suffix ending
>    exactly at the **same** (m);
> 4. every proper state in that 75-step suffix is strictly larger than (m);
> 5. the prefix and suffix defect heights are joined by one complete legal
>    nonnegative defect path.

Every genuine fully owned least-rooted singleton cycle necessarily satisfies
all five statements.  Therefore, if the bridge were true, it would eliminate
the whole surviving `g=1` branch without defect-area enumeration.

The theorem is false.

## 2. Why this is the correct ownership-specific interface to test

RL153 leaves the exact one-block condition

[
D=2^A-3^Lmid Q_h.
]

For an actual cycle the quotient is not merely an integer: it is the least
state itself,

[
m=rac{Q_h}{D}.
]

RL154 extracts exact endpoint consequences of this full physical identity.

For a 75-step prefix with exponent sum (S),

[
2^S y_{75}=3^{75}m+C_{m pre},
]

so (m) is fixed modulo (2^S).  Since (Sge75) and
(m<2^{75}), a chosen exact prefix selects at most one physical (m).

Similarly, a 75-step suffix ending at (m) gives an exact congruence modulo
(3^{75}).  Since (3^{75}>2^{75}), a chosen exact suffix also selects at
most one (m) in the physical state window.

Thus matching the **same** (m) at both ends is substantially stronger than
the Session 4 excursion grammar and substantially stronger than a bare
one-binomial resultant.  Session 5 tests whether that exact two-sided physical
capture is already enough to bridge the middle.

It is not.

## 3. Explicit same-`m` countermodel

Take

[
oxed{m=2^{75}-1=37778931862957161709567.}
]

Then

[
2^{71}le m<2^{75}.
]

### 3.1 Exact forward prefix

Run the genuine accelerated Collatz map from (m) for 75 odd steps.

The exact valuation word is

[
oxed{1^{74},2}.
]

Its total exponent is

[
S_{75}=76.
]

The induced defect values

[
h_j=b_j-S_j
]

are all nonnegative.  In particular

[
b_{75}=118,qquad h_{75}=118-76=42.
]

The defect area accumulated in this prefix alone is

[
sum_{j=0}^{75}h_j=1629,
]

so the construction is far inside the surviving area-at-least-three class.

Every one of the 75 proper forward states is strictly larger than (m).
The terminal prefix state is

[
304133393856678854559841996309430653.
]

Thus this is not merely a modular prefix word: it is an exact physical
least-rooted 75-step orbit segment starting at the candidate (m).

### 3.2 Exact backward suffix returning to the same `m`

Now start at (y_L=m) and construct 75 physical predecessors.

At a backward step (j), with known odd (y_{j+1}) and known
(h_{j+1}), choose the smallest positive exponent (a_j) of the parity
required by

[
2^{a_j}y_{j+1}equiv1pmod3
]

which also satisfies

[
h_j=a_j-c_j+h_{j+1}ge0
]

and for which

[
y_j=rac{2^{a_j}y_{j+1}-1}{3}
]

is not divisible by 3.  If the first parity-compatible choice gives a
multiple of 3, increase (a_j) by 2.  This preserves the mod-3 divisibility
condition and deterministically continues the physical backward chain.

For the actual 75-step suffix this produces:

- boundary phase
  [
  L-75=137528045237;
  ]
- boundary defect
  [
  oxed{h_{L-75}=53};
  ]
- maximum suffix exponent (4);
- maximum suffix defect (53);
- exact suffix-start state
  [
  371804656870741614109061597054976841273.
  ]

Replaying these 75 steps **forward** gives the exact accelerated valuations
chosen above and returns exactly to

[
m=2^{75}-1.
]

Every proper suffix state is also strictly larger than (m).

Therefore the exact prefix and exact suffix independently select and physically
realize the **same** candidate least state.

## 4. The complete legal defect path can also be joined

It remains to test whether the two physical ends conflict already at the
defect-grammar level.  They do not.

The prefix ends at

[
h_{75}=42.
]

Drop immediately to zero at phase 76.  This is legal because downward defect
jumps are unrestricted by the positivity condition:

[
a_{75}=c_{75}+42>0.
]

Keep (h=0) through the long middle.

Let

[
j_0=(L-75)-90=137528045147.
]

Starting from (h_{j_0}=0), use the tight legal recurrence for 90 steps,

[
h_{j+1}=h_j+c_j-1.
]

Since (c_jin{1,2}), this rises only by 0 or 1 per step and has

[
a_j=c_j+h_j-h_{j+1}=1.
]

At the actual counts the 90-step ramp accumulates exactly 53 rises, hence

[
h_{L-75}=53,
]

which matches the physical suffix boundary exactly.

The already constructed suffix then carries the defect path from 53 back to

[
h_L=0.
]

Thus there is one complete nonnegative path from (h_0=0) to (h_L=0)
whose associated exponents are positive everywhere and whose first and last
75 steps are the two exact physical orbit segments above.

Because

[
a_j=c_j+h_j-h_{j+1},
]

telescoping over the full path gives automatically

[
sum_{j=0}^{L-1}a_j
=
sum_{j=0}^{L-1}c_j+h_0-h_L
=
A.
]

So even the exact global ((A,L)) counts are preserved.

## 5. What fails

The countermodel deliberately does **not** assert that the physical state
reached after the prefix evolves through the enormous middle into the physical
state at the start of the suffix.

That is the only missing condition.

This is therefore a direct structural kill of the attempted bridge:

> exact physical prefix capture + exact physical suffix capture + the same
> state (m) + the physical state window + least-root behavior on both ends +
> a complete legal nonnegative defect excursion **do not imply the global
> physical middle connection**.

Equivalently, the RL154 two-sided residue/transfer interface cannot be turned
into a global owner exclusion without a genuinely new theorem controlling the
middle physical orbit.

This is the same Bridge Problem in a sharper form, not a finite-search
failure.

## 6. Preliminary quotient-window red team

Before the stronger same-`m` construction above, Session 5 also tested the
coarser ownership consequence

[
m=Q_h/D,qquad 2^{71}le m<2^{75}.
]

That size information is far too weak to repair Session 4.

The committed supporting verifier shows that:

- the zero-defect quotient is already below (2^{75}), so the upper state
  ceiling is automatic for every nonnegative defect profile;
- the maximal Session-4 connected height-one run
  (N=P-1=65470613320), whose collapsed support is
  (130941226641), still remains above the (2^{71}) floor under a rigorous
  worst-case loss bound;
- a legal ramp cut after (10^9) phases reaches height
  (584962500) while the same worst-case quotient bound still remains above
  (2^{71}).

Thus neither state-window endpoint controls the two obstructions isolated in
Session 4: residue-order support and defect height.

This preliminary negative result is not needed for the exact same-`m`
countermodel, but it explains why the stronger two-sided transfer was the
correct Session 5 attack.

## 7. Verification artifacts

The main exact countermodel is checked by

`FINAL_CHANCE/verifiers/verify_session5_two_sided_transfer_countermodel.py`.

It uses only integer arithmetic and directly replays both physical 75-step
segments.

Its literal reproduced stdout is:

```
FINAL_CHANCE Session 5 two-sided transfer countermodel verifier: PASS
A,L = (217976794617, 137528045312)
m = 37778931862957161709567
m window = (2361183241434822606848, 37778931862957161709568)
prefix exact exponents = 1^74,2
prefix total exponent S_75 = 76
prefix terminal defect h_75 = 42
prefix defect area through 75 = 1629
prefix terminal state = 304133393856678854559841996309430653
suffix cut = 137528045237
suffix boundary defect h_(L-75) = 53
suffix start state = 371804656870741614109061597054976841273
suffix maximum exponent = 4
suffix maximum defect = 53
middle tight-ramp length = 90
middle tight-ramp terminal height = 53
same m selected by exact physical prefix and suffix = True
complete nonnegative positive-exponent defect grammar = True
global middle physical connection = NOT ASSERTED
scope=countermodel to two-sided-transfer bridge; not a cycle
```

The preliminary state-window calculation is separately encoded in

`FINAL_CHANCE/verifiers/verify_session5_ownership_window_barrier.py`.

## 8. Session 5 conclusion

The attempted two-sided ownership-transfer Bridge Theorem is **KILLED**.

The surviving requirement for any final-session attack is now extremely
specific:

> it must impose the **actual global physical middle connection** between
> ownership-compatible endpoint data.

A theorem that only supplies local defect grammar, state-window bounds,
prefix residues, suffix residues, a matching candidate (m), phase
polynomials, bare resultants, or equivalent distinguished-root encodings
cannot close the branch; those interfaces have now been explicitly separated
from the missing global connection.

No area-by-area enumeration was used.
