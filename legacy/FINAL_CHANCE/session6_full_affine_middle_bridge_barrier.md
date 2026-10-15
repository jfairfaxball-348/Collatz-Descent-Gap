# FINAL_CHANCE Session 6 — full-affine middle bridge barrier

Date: 2026-09-18

Status: **KILLED — final programme verdict follows.**

Incoming cumulative strikes: **2/3**.

This is the sixth and final budgeted FINAL_CHANCE session.

## 1. Exact Bridge Theorem attempted

Retain the actual first-survivor counts

A = 217976794617,
L = 137528045312,
D = 2^A - 3^L > 0.

For a positive accelerated exponent word a_0,...,a_(L-1), write

S_j = sum_(i<j) a_i,
b_j = floor(Aj/L),
h_j = b_j - S_j.

The attempted final-session theorem was:

> **Full-affine middle bridge.** There is no positive cyclic solution over the rationals to the ordinary accelerated +1 equations
>
> 3 y_j + 1 = 2^(a_j) y_(j+1)
>
> satisfying all of:
>
> 1. a_j >= 1 and sum a_j = A;
> 2. h_0 = h_L = 0 and h_j >= 0 at every phase;
> 3. total defect area at least three;
> 4. y_0 is the strict least state;
> 5. 2^71 <= y_0 < 2^75;
> 6. if p and q are the first and last positive-defect phases, then p + (L-q) <= 37.

Every hypothetical fully owned least-rooted integer g=1 cycle in the current first-survivor branch is a special case. If the theorem were true, the remaining branch would close using the actual global middle affine dynamics rather than local defect grammar or endpoint residues.

The theorem is false.

## 2. Explicit full-period rational countermodel

Define

h_0 = h_1 = h_L = 0

and

h_j = 1 for 2 <= j <= L-1.

Then

p = 2,
q = L-1,

so

p + (L-q) = 3.

This lies far inside the Session 5 boundary-collar reduction p + (L-q) <= 37.

The defect area is

L-2 = 137528045310,

so this is not a bounded-area construction.

Put c_j = b_(j+1)-b_j. The exponent word is recovered by

a_j = c_j + h_j - h_(j+1).

At the actual survivor,

c_0 = 1,
c_1 = 2,
c_(L-1) = 2.

Therefore

a_0 = 1,
a_1 = 1,
a_(L-1) = 3,

and every other interior exponent is c_j in {1,2}. All exponents are positive.

Because h_0 = h_L = 0, telescoping gives

sum a_j = sum c_j = A.

Thus the word has exactly the inherited (A,L) counts.

## 3. The unique full affine +1 return

For any positive word with D > 0, composing the ordinary accelerated recurrence around one full period gives

2^A y_0 = 3^L y_0 + Q_h,

hence the unique rational closing value is

y_0 = Q_h / D.

Since Q_h > 0, this gives a positive rational cyclic solution. All other phase values are obtained by the actual ordinary +1 recurrence, so the entire middle interval is genuinely connected by the full affine dynamics over the positive rationals.

For the present profile, let

rho_j = 2^(b_j)/3^j,
S = sum rho_j.

Then

Q_h/D =
[sum rho_j 2^(-h_j)] / [3(exp(Delta)-1)],

where Delta = A log 2 - L log 3.

Because h_j = 1 exactly for 2 <= j <= L-1,

sum rho_j 2^(-h_j)
=
S/2 + (rho_0+rho_1)/2
=
S/2 + 5/6,

using rho_0 = 1 and rho_1 = 2/3.

A rigorous outward-rounded computation gives

18398890329678333925084.865203331289733771357436326005784942633867092203763859573970283284744380731873371091868324264839575846945736746080741

< Q_h/D <

18398890329678333925084.865203331289733771357436326005784942633867092203763859573970283284744380731873371091868324266330177530734273948230581.

The enclosure width is at most

1.490601683788537202149840e-93.

Therefore

2^71 < Q_h/D < 2^75.

The whole interval lies strictly between the consecutive integers

18398890329678333925084

and

18398890329678333925085.

Hence

D does not divide Q_h.

The full affine return exists over positive rationals but is not an ordinary integer Collatz cycle.

## 4. Strict least-root order

For every proper phase 0 < j < L,

S_j = b_j - h_j <= b_j.

The inherited first-survivor floor lock gives

2^(b_j) < 3^j,

hence

2^(S_j) < 3^j.

The exact affine prefix identity has the form

2^(S_j) y_j = 3^j y_0 + C_j

with C_j > 0. Therefore

y_j > (3^j / 2^(S_j)) y_0 > y_0.

Thus y_0 is the strict least state of the full rational affine cycle.

The countermodel simultaneously satisfies:

- the exact (A,L) counts;
- positive accelerated exponents;
- a complete nonnegative defect excursion;
- arbitrarily large surviving defect area;
- the Session 5 boundary collar, with collar size 3;
- the inherited least-state window;
- strict least-root order;
- the actual ordinary +1 affine recurrence through the entire middle;
- exact cyclic full-period closure over positive rationals.

It fails only integer ownership.

## 5. Why this exhausts the present Bridge family

For a fixed positive exponent word, full-period closure is exactly

D m = Q.

Therefore

m is an integer if and only if D divides Q.

RL167 already proves the cyclic propagation theorem: once one full affine numerator is divisible by D, all rotated affine quotients are automatically positive integers satisfying the ordinary accelerated equations.

So integer physical middle closure is exactly full ordinary ownership. It is not an intermediate consequence weaker than ownership.

Across FINAL_CHANCE, the natural attempts to force that last arithmetic step have now been exhausted in this family:

1. local/radius and defect-grammar data do not force ownership;
2. area two can be eliminated globally, but Session 4 proves the sparse-support / degree / Parseval mechanism cannot be uniformized to arbitrary area or height;
3. Session 5 proves exact physical endpoint capture, a matching least-state candidate, the state window, and a complete legal defect path do not force the middle connection;
4. the corrected dense phase polynomial, one-binomial resultant, joint distinguished-root/SNF interface, and all-phase affine closure reduce to the same ownership datum rather than supplying an independent discriminator;
5. Session 6 proves that even the entire ordinary +1 middle recurrence over positive rationals, together with least-root order, the state window, and the strongest boundary-collar reduction, still does not force integrality.

The only surviving strengthening is to prove D divides Q_h for the full word. That is the original ownership problem itself, not a bridge from the already-proved local/finite/branch-restricted results.

## 6. Verification

Exact artifact:

FINAL_CHANCE/verifiers/verify_session6_full_affine_middle_barrier.py

The verifier uses the already committed rigorous interval primitives from the Session 1 verifier and does not materialize 2^A, 3^L, D, or Q_h.

Local replay during closeout reproduced the interval and all exact grammar arithmetic above.

## 7. Session 6 outcome

**Outcome: KILLED.**

**Strike this session: N.**

A concrete falsifiable global bridge was stated and attacked directly with an explicit full-period ordinary +1 affine countermodel.

**Cumulative strikes: 2/3.**

The six-session budget is exhausted. The programme-level verdict is recorded in FINAL_CHANCE/VERDICT.md.
