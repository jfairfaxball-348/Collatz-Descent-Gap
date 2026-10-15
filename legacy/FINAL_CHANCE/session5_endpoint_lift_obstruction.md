# FINAL_CHANCE Session 5 — two-sided endpoint lifts and the resonant-span obstruction

Date: 2026-09-18

Status: Session 5 mathematical result complete.

Incoming cumulative strikes: **2/3**.

Scope: the first-survivor `g=1` branch at

[
A=217976794617,qquad
L=137528045312,qquad
D=2^A-3^L>0,
]

with the independently accepted Session 3 exclusion of defect area exactly two
and the Session 4 structural killing of the uniform sparse/degree/Parseval
route.

No area-by-area enumeration is used here.

## 1. Exact Bridge Theorem attempted

For a legal nonzero nonnegative defect excursion let

[
b_j=lfloor Aj/Lfloor,qquad
h_j=b_j-S_j,qquad
H=max h_j,
]

and let

[
p=min{j:h_j>0},qquad
q=max{j:h_j>0}.
]

Write the real ordinary quotient

[
m_h=rac{Q_h}{D}.
]

Every actual fully owned cycle in the inherited branch has integer
`m_h=m` and, by the inherited external state bounds,

[
2^{71}le m_h<2^{75}.
]

Let the Bezout data be

[
P=65470613321,quad U=103768467013,
]

[
T=L-P=72057431991,quad
S=A-U=114208327604,
]

so that

[
AP-UL=1,qquad AT-SL=-1.
]

Session 5 tested the following exact global bridge:

> **Two-sided endpoint-lift bridge.** Every legal nonnegative nonzero defect
> excursion with (sum h_jge3) and
> (2^{71}le Q_h/D<2^{75}) has at least one endpoint ownership lift whose
> canonical positive integer representative lies strictly between zero and
> (D).

The two lifts are derived below.  If the theorem were true, a fully owned
profile would make **both** lifts divisible by `D`, so the existence of even
one nonzero lift below `D` would be a contradiction.  This would eliminate
all surviving `g=1` profiles at once.

The theorem is false.  However, deriving it yields a new global endpoint-span
theorem for every actual owner.

## 2. Ownership collapse used

Retain the exact Session 4 collapse

[
E_h(X)=2^{H-1}+(X-1)G_h(X),
]

where

[
G_h(X)=sum_{j<L}d_jX^{r_j},qquad
d_j=2^H-2^{H-h_j},qquad
r_j=Ajmod L.
]

Full ownership implies

[
E_h(ho)equiv0pmod D,
]

with the two physical Bezout representations

[
hoequiv 2^U3^{-P}equiv3^T2^{-S}pmod D.
]

Also

[
ho^{r_j}equiv2^{b_j}3^{-j}
equiv3^{L-j}2^{b_j-A}pmod D.
]

These are the only ownership inputs used.

## 3. Last-defect 3-denominator lift

Let `q` be the last positive-defect phase.  Multiply
`E_h(rho)` by `3^(P+q)`.  Since there are no defects after `q`,

[
Dmid
2^{H-1}3^{P+q}
+
(2^U-3^P)
sum_{jle q}d_j2^{b_j}3^{q-j}.
]

Use

[
d_j2^{b_j}
=
2^Hleft(2^{b_j}-2^{b_j-h_j}ight).
]

The whole lift has the exact factor `2^(H-1)`.  Since `D` is odd, it may
be cancelled.  Define

[
R_3(q)=
sum_{jle q}
3^{q-j}
left(2^{b_j}-2^{b_j-h_j}ight)
]

and

[
oxed{
K_3(q)
=
3^{P+q}
+
2(2^U-3^P)R_3(q).
}
]

Every fully owned profile satisfies

[
oxed{Dmid K_3(q).}
]

Put

[
x_3=Plog3-Ulog2>0.
]

Then

[
rac{3^P-2^U}{3^P}
=
1-e^{-x_3}
<
x_3.
]

The global floor lock gives

[
rac12<
ho_j:=rac{2^{b_j}}{3^j}
<1.
]

Therefore

[
0<
rac{R_3(q)}{3^q}
=
sum_{h_j>0}
ho_j(1-2^{-h_j})
<
q+1.
]

Hence, whenever `q<=T-26`,

[
K_3(q)
>
3^{P+q}left(1-2x_3(q+1)ight)>0.
]

The exact rational-log verifier proves

[
2x_3(T-25)<1.
]

Also

[
K_3(q)<3^{P+q}le3^{L-26}.
]

The inherited exact log bound gives

[
D>3^{L-26}.
]

Thus

[
0<K_3(q)<D,
]

contradicting `D|K_3(q)`.

Therefore every actual owned nonzero excursion obeys

[
oxed{qge T-25=72057431966.}
]

This generalizes the Session 3 low adjacent-pair lift to **arbitrary height,
area, component count, and run length**.

## 4. First-defect 2-denominator lift

Let `p` be the first positive-defect phase.  Since `h_(p-1)=0` and rises
are at most one,

[
h_p=1.
]

The accelerated exponent sums `S_j=b_j-h_j` are strictly increasing, so for
every `j>=p`,

[
S_jge S_p=b_p-1.
]

Using the complementary representation and multiplying by
`2^(S+A-b_p)` gives

[
Dmid
2^{H-1}2^{S+A-b_p}
+
(3^T-2^S)
sum_{jge p}d_j3^{L-j}2^{b_j-b_p}.
]

The monotonicity just noted makes

[
2^{b_j-b_p+1}-2^{b_j-h_j-b_p+1}
]

an integer for every defect phase `j>=p`.  Hence the same global
`2^(H-1)` factor cancels.  Define

[
R_2(p)=
sum_{jge p}
3^{L-j}
left(
2^{b_j-b_p+1}
-
2^{b_j-h_j-b_p+1}
ight)
]

and

[
oxed{
K_2(p)
=
2^{S+A-b_p}
+
(3^T-2^S)R_2(p).
}
]

Every full owner satisfies

[
oxed{Dmid K_2(p).}
]

Put

[
x_2=Slog2-Tlog3>0.
]

Then

[
rac{2^S-3^T}{2^S}=1-e^{-x_2}<x_2.
]

Moreover

[
3^{L-j}2^{b_j-A}
=
rac{3^L}{2^A}ho_j<1,
]

so

[
0<
rac{R_2(p)}{2^{A-b_p}}
<
2(L-p).
]

For `p>=T+26`, one has `L-p<=P-26`, and the exact verifier proves

[
2x_2(P-26)<1.
]

Therefore

[
0<K_2(p)<2^{S+A-b_p}.
]

Exact floor arithmetic gives

[
b_{T+26}=S+41.
]

Hence `p>=T+26` implies

[
K_2(p)<2^{A-41}<D.
]

This contradicts `D|K_2(p)`.

Therefore every actual owned nonzero excursion obeys

[
oxed{ple T+25=72057432016.}
]

Again this is uniform in height, area, number of components, and run length.

## 5. New global owner reduction

Combining the two endpoint lifts gives:

> **Session 5 endpoint-span theorem.**  
> Every hypothetical fully owned surviving `g=1` nonnegative defect
> excursion must have
> [
> oxed{
> ple72057432016,qquad
> qge72057431966.
> }
> ]
> Equivalently, its first-to-last defect span must cross the 51-phase
> resonant window centered at the Bezout-complement phase `T`.

This does **not** say that a defect itself must occur inside that window.  A
profile may have an early component and a late component separated by a
zero-defect gap.  No independent ownership of the components is inferred.

This is a genuine global reduction on actual owners, not an area cutoff.

## 6. Countermodel attack on the full endpoint-size bridge

The remaining question was whether the two complementary lifts together force
one endpoint lift below `D` for every legal candidate already lying in the
inherited real state window.

They do not.

Define one connected height-one excursion by

[
h_j=
egin{cases}
1,&2le jle T,\
0,&	ext{otherwise}.
end{cases}
]

It has

[
p=2,qquad q=T,qquad
sum h_j=T-1=72057431990.
]

This is not an area-by-area construction.  It is one parametric-scale
connected excursion.

It is legal.  The only rise is at phase `1 -> 2`, and exact arithmetic gives

[
c_1=b_2-b_1=2.
]

The plateau is automatically legal, and the final drop is unrestricted by the
one-step-rise condition.

### 6.1 It lies in the inherited real state window

For any profile,

[
rac{Q_h}{D}
=
rac{sum_{j<L}ho_j2^{-h_j}}
     {3(e^Delta-1)},
qquad
Delta=Alog2-Llog3.
]

The verified global floor lock gives

[
1/2<ho_j<1.
]

For the connected run above there are `T-1` half-weight phases and
`P+1` full-weight phases.  Therefore

[
rac{P+1}{2}+rac{T-1}{4}
<
sumho_j2^{-h_j}
<
(P+1)+rac{T-1}{2}.
]

The exact rational log/exponential bounds in the Session 5 verifier prove

[
oxed{
2^{71}<Q_h/D<2^{75}.
}
]

So the countermodel satisfies the same inherited **real** state-size window as
an owner.  It is not claimed to make `Q_h/D` integral.

### 6.2 The last-defect lift is much larger than D

Here `q=T`, so `P+q=L`.  There are `T-1` defect terms and

[
rac{K_3(T)}{3^L}
>
1-2x_3(T-1).
]

The exact verifier proves

[
1-2x_3(T-1)>rac14.
]

It also proves

[
rac{D}{3^L}=e^Delta-1<rac1{1000}.
]

Hence

[
oxed{K_3(T)>D.}
]

### 6.3 The first-defect lift is also much larger than D

Here `p=2` and `b_p=3`.  Bounding only the actual `T-1` defect terms gives

[
rac{K_2(2)}{2^{S+A-3}}
>
1-2x_2(T-1).
]

The exact verifier proves

[
1-2x_2(T-1)>rac18.
]

Therefore

[
K_2(2)>
2^{S+A-6}>2^A>D.
]

Thus

[
oxed{K_2(2)>D.}
]

The countermodel consequently satisfies the inherited grammar and real
state-size window while **both** endpoint lifts lie above the modulus.

It follows that the attempted Two-sided endpoint-lift Bridge Theorem is false.
The 26/41-exponent buffers around the resonant cut are not merely artifacts of
the area-two proof: long legal excursions can genuinely enter the resonant
region while keeping both natural complementary endpoint representatives too
large for a direct `0<N<D` contradiction.

The countermodel is not asserted to satisfy full ownership; it is used to
disprove exactly the proposed structural implication from the inherited
grammar plus the state-size window.

## 7. What survives

The endpoint-size bridge is killed, but the following theorem survives for
actual owners:

[
ple T+25,qquad qge T-25.
]

This is stronger than the pre-Session-5 state: arbitrary surviving owners may
no longer have their entire defect support confined to an early or late
one-sided region.

What remains open is genuinely two-sided ownership interaction.  A successful
final bridge would have to couple early and late defect contributions across
the resonant cut.  It cannot merely apply the two endpoint lifts separately,
and it cannot return to the Session 4 sparse/degree/Parseval mechanism.

## 8. Verification artifact

The exact arithmetic is checked by

`FINAL_CHANCE/verifiers/verify_session5_endpoint_lift_obstruction.py`.

It verifies the global floor-lock premise, both Bezout relations, the two
uniform one-sided positivity/size cutoffs, the forced owner endpoint span, the
legality and inherited real state window of the connected countermodel, and
the fact that both endpoint lifts exceed `D` for that countermodel.

No giant `2^A` or `3^L` integer is materialized.
