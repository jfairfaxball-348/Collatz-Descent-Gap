# FINAL_CHANCE Session 4 — uniform (X-1)P_h collapse obstruction

Date: 2026-09-18

Status: **ATTEMPTED, PENDING INDEPENDENT VERIFICATION**

Scope: first-survivor `g=1` branch at

[
A=217976794617,qquad L=137528045312,qquad
M=A-L=80448749305,
]

after the independently verified Session 3 exclusion of total defect area exactly
two.  This note does not assert ownership for any countermodel constructed
below.  The countermodels are used exactly as permitted by the Session 4
mandate: to test what follows from the already-proved nonnegative excursion
grammar alone.

## 1. Exact Bridge Theorem attempted

Let `h=(h_j)_{0le jle L}` be any nonzero legal nonnegative first-survivor
defect excursion with `h_0=h_L=0`, total defect area at least three, and let

[
H=max_j h_j,qquad r_j=Ajmod L.
]

Let

[
P_h(X)=sum_{j<L}2^{H-h_j}X^{r_j},
]

and let `rho` be the physical phase satisfying

[
2ho^L=1pmod D,qquad D=2^A-3^L.
]

Define the exact collapsed ownership polynomial `E_h` as in Section 2 below,
and whenever it has an `X^L` term reduce it with `2X^L-1` to the canonical
degree-`<L` representative, clearing only the forced power-of-two denominator
and then dividing by the integer content.  Call the resulting primitive
polynomial `widetilde E_h(X)=sum_{k=0}^m e_kX^k`.

The Session-3-style uniform bridge tested in this session is the following
precise sufficient statement:

> **Uniform collapsed-Parseval bridge.** For every such legal defect excursion
> with total defect area at least three, `m<L` and, with
> `alpha=2^{-1/L}` and
> [
> V(widetilde E_h)=sum_{k=0}^{m}e_k^2alpha^{2k},
> ]
> one has
> [
> 2^m V(widetilde E_h)^{L/2}<D.
> ]

If true, this would eliminate every surviving profile at once.  Indeed
ownership gives `widetilde E_h(ho)=0pmod D`.  Since
`B(X)=2X^L-1` is irreducible and `m<L`,
`R_h=operatorname{Res}(B,widetilde E_h)
e0` and `Dmid R_h`.  Discrete
Parseval plus AM-GM gives

[
|R_h|le 2^mV(widetilde E_h)^{L/2}<D,
]

a contradiction.

This is the exact generalization of the Session 3 resultant/Parseval mechanism
being tested.  The theorem is false.

## 2. General collapse derived from the corrected RL157 normalization

Put

[
w_j=2^{H-h_j}.
]

Because (gcd(A,L)=1), `j -> r_j` permutes
`0,1,...,L-1`.  If

[
P=A^{-1}pmod L,qquad sigma(r)=Prmod L,
]

then the coefficient of `X^r` in `P_h` is

[
a_r=w_{sigma(r)}.
]

Therefore, before using the binomial relation,

[
(X-1)P_h(X)
=
a_{L-1}X^L-a_0
+sum_{r=1}^{L-1}(a_{r-1}-a_r)X^r.
]

This already identifies the central structural point: multiplication by
`X-1` differentiates the weights in **residue/exponent order**.  It does not
differentiate them in chronological phase order.  Consecutive exponents
correspond to phases separated by `P`:

[
sigma(r-1)-sigma(r)equiv-Ppmod L.
]

Thus chronological connectedness of a defect excursion does not imply sparse
boundary support after the phase permutation.

There is also an exact level-set form.  For

[
F_ell(X)=sum_{j:,h_jgeell}X^{r_j},
]

the identity

[
2^{H-h_j}
=
2^H-sum_{ell=1}^{h_j}2^{H-ell}
]

gives

[
P_h(X)
=
2^H(1+X+cdots+X^{L-1})
-
sum_{ell=1}^{H}2^{H-ell}F_ell(X).
]

If ownership holds, multiply by (ho-1) and use
(ho^L=1/2).  One obtains the exact necessary congruence

[
E_h(ho)=0pmod D,
]

where

[
oxed{
E_h(X)
=
2^{H-1}
+
sum_{ell=1}^{H}2^{H-ell}(X-1)F_ell(X).
}
]

Equivalently, set

[
d_j=2^H-2^{H-h_j}
]

and

[
G_h(X)=sum_{j<L}d_jX^{r_j}.
]

Then

[
oxed{E_h(X)=2^{H-1}+(X-1)G_h(X).}
]

This is the general `(X-1)P_h` collapse.  It is exact and height-independent
as an identity, but it is not uniformly sparse.

Writing `g_r=d_{sigma(r)}`, its coefficients before any possible
`X^L` reduction are

[
e_0=2^{H-1}-g_0=2^{H-1},
]

because `h_0=0`, and

[
e_r=g_{r-1}-g_rquad(1le r<L),qquad e_L=g_{L-1}.
]

So the collapsed polynomial is a weighted boundary measure of the defect
weights in **permuted residue order**, not of chronological level-set
boundaries.

## 3. Countermodel family 1: one connected height-one run gives 2N+1 terms

The inherited excursion grammar can be written

[
a_j=c_j+h_j-h_{j+1}ge1,
qquad
c_j=leftlfloorrac{A(j+1)}Lightfloor
-leftlfloorrac{Aj}Lightfloorin{1,2}.
]

Equivalently,

[
h_{j+1}-h_jle c_j-1.
]

At the actual survivor,

[
c_1=2.
]

For any integer

[
3le Nle P-1,
]

define the single connected excursion

[
h_j=
egin{cases}
1,&2le jle N+1,\
0,&	ext{otherwise}.
end{cases}
]

The only rise is `h_1=0 -> h_2=1`, and `c_1=2`, so it is legal.  Staying
at height one is always legal, and the final drop is unrestricted by the
one-step-rise condition.  Its defect area is exactly `N`.

At the actual scale,

[
P=A^{-1}pmod L=65470613321,
]

and

[
T=L-P=72057431991.
]

If two defect residues in the family were adjacent in exponent order, then

[
r_k-r_jequivpm1pmod L
]

would imply

[
k-jequivpm Ppmod L.
]

But for `2le j,kle N+1`,

[
|k-j|le N-1le P-2<P<T.
]

Hence no two defect residues are adjacent.  Also the unique phase with
residue `L-1` is `T`, while `N+1le P<T`, so the family never creates an
`X^L` endpoint term.

Because `H=1`,

[
E_h(X)
=
1+(X-1)sum_{j=2}^{N+1}X^{r_j}.
]

Every defect residue therefore contributes two distinct nonzero coefficients,
one at `r_j` and one at `r_j+1`, in addition to the constant term.  Thus

[
oxed{#operatorname{supp}(E_h)=2N+1.}
]

This is not a bounded-component pathology: the chronological defect set is
one connected interval.  The support growth is created entirely by the
residue permutation.

At the maximum certified family member `N=P-1`,

[
#operatorname{supp}(E_h)
=
130941226641.
]

Therefore no Session-3-like sparse support bound independent of defect area
follows from the known excursion grammar.

## 4. Obstacle 2 is already fatal at area three

Take the first member of that family, `N=3`:

[
h_2=h_3=h_4=1,
]

all other defects zero.  This is a single connected height-one excursion of
area three.  Its exact residues are

[
r_2=23369453298,
]

[
r_3=103818202603,
]

[
r_4=46738906596.
]

Hence

[
E_h(X)
=
1+sum_{j=2}^{4}(X^{r_j+1}-X^{r_j}),
]

and

[
deg E_h=103818202604.
]

But

[
M=80448749305.
]

Thus

[
oxed{deg E_h>M.}
]

So the Session 3 degree window fails immediately for a legal area-three
profile.  The reason is structural: a long or even very short chronological
positive run can hit high residues because the map `j -> Aj mod L` scrambles
phase order.

This settles the second audit obstacle negatively: no analogue of
`deg E<=M` follows from the existing arbitrary-excursion grammar.

## 5. Obstacle 1: height makes the primitive coefficient norm grow exponentially

There is a second independent obstruction.

Let

[
d_j^{m ramp}
=
leftlfloorrac{Aj}{L}ightfloor-j.
]

Then

[
d_{j+1}^{m ramp}-d_j^{m ramp}=c_j-1in{0,1}.
]

Also

[
d_0^{m ramp}=0,
qquad
d_{L-1}^{m ramp}=M-1.
]

Therefore every integer height

[
1le Hle M-1
]

is attained.  Let `q_H` be the first phase where
`d_{q_H}^{m ramp}=H`, and define an excursion by following the ramp up to
that phase and dropping immediately to zero:

[
h_j=d_j^{m ramp}quad(0le jle q_H),
]

[
h_j=0quad(j>q_H).
]

For `j<q_H` the grammar is tight:

[
c_j+h_j-h_{j+1}=1.
]

At the drop it is strictly positive, and afterwards it is just `c_j>=1`.
Thus this is a legal excursion of height exactly `H` for every
`1le Hle M-1`.

For every such profile, the collapsed constant coefficient is

[
e_0=2^{H-1}.
]

This power of two cannot in general be divided away as polynomial content.
The first-hit maximum is unique.  At that maximum,

[
d_{q_H}=2^H-1
]

is odd, while every lower-level defect weight
`2^H-2^{H-h_j}` is even.  Consequently at least one residue-order boundary
coefficient is odd.  The primitive collapse therefore retains the
`2^{H-1}` constant.

Hence the coefficient size of the primitive collapsed polynomial is not
bounded independently of height.  It grows at least exponentially in `H`.

## 6. Explicit height-three profile kills the uniform Parseval inequality

A very small member already kills the exact Bridge Theorem attempted above.

Take

[
(h_0,ldots,h_7)=(0,0,1,1,2,2,3,0)
]

and `h_j=0` thereafter.  This is the ramp through phase six followed by a
drop.  Its defect area is nine and its height is three.

The positive-phase residues are

[
egin{array}{c|ccccc}
j&2&3&4&5&6\
hline
r_j&
23369453298&
103818202603&
46738906596&
127187655901&
70108359894
end{array}
]

and none is `L-1`; the collapsed polynomial already has degree `<L`.

Here

[
2^H-2^{H-h_j}
=
4,4,6,6,7
]

on those five phases, so

[
E_h(X)
=
4
+(X-1)
left(
4X^{r_2}
+4X^{r_3}
+6X^{r_4}
+6X^{r_5}
+7X^{r_6}
ight).
]

The five residues are mutually non-adjacent in exponent order, so there is no
coefficient cancellation.  The polynomial has content one because a
coefficient of magnitude seven is present.  Thus it is already the primitive
collapse `widetilde E_h`.

For the Parseval quantity

[
V(widetilde E_h)
=
sum e_k^2alpha^{2k},
]

the constant term alone gives

[
V(widetilde E_h)ge 4^2=16.
]

Therefore the exact Session-3-style resultant upper bound satisfies

[
2^mV(widetilde E_h)^{L/2}
ge
16^{L/2}
=
4^L
=
2^{2L}.
]

But

[
2L=275056090624>A=217976794617,
]

and

[
D=2^A-3^L<2^A.
]

Hence

[
oxed{
2^mV(widetilde E_h)^{L/2}
>
D.
}
]

The sufficient inequality in the attempted Bridge Theorem is therefore false
for an explicit legal height-three excursion before any other coefficient is
even counted.

This is not a numerical approximation and does not depend on materializing
any giant integer.

## 7. What has and has not been killed

The exact `(X-1)P_h` identity survives and is useful:

[
E_h(X)
=
2^{H-1}
+sum_{ell=1}^H2^{H-ell}(X-1)F_ell(X).
]

What fails is the hoped-for **uniform sparse/degree/Parseval consequence from
the present excursion grammar**.

Three independent facts block the Session 3 mechanism:

1. A single connected height-one excursion can have `2N+1` collapsed terms,
   with `N` ranging through more than sixty-five billion values at the actual
   survivor.
2. The `deg E<=M` window already fails for the legal connected area-three
   profile `h_2=h_3=h_4=1`.
3. Primitive collapsed coefficients are not height-uniform.  The constant
   `2^{H-1}` survives primitive normalization, and at height three alone it
   makes the Session-3 Parseval/AM-GM sufficient bound larger than `D`.

The structural reason is that `X-1` sees boundaries after the
`j -> Aj mod L` permutation.  Chronological excursion structure constrains
`h_{j+1}-h_j`, while the collapsed coefficients compare phases separated by
`P=A^{-1} mod L`.  The current grammar supplies no relation between those
long-separated phases strong enough to bound residue-order variation.

This does **not** prove that no future ownership-specific argument can use
`E_h`.  In particular, it does not disprove every conceivable global
complementary-lift or distinguished-root argument that imports genuinely new
arithmetic information.  It proves the narrower and mandated Outcome C:
the Session 3 `(X-1)P_h` sparse-collapse / degree / Parseval strategy cannot
be promoted to a height-independent contradiction from the presently known
defect grammar alone.

## 8. Verification artifact

The exact arithmetic and explicit countermodels are checked by

`FINAL_CHANCE/verifiers/verify_session4_uniform_collapse_obstruction.py`.

The artifact does not enumerate the giant phase space and does not claim
ownership for the countermodels.  It checks the modular inverse, the support
family limits, the area-three high-degree member, the height-three grammar and
primitive collapse, the Parseval obstruction inequality, and the available
ramp height range.

Verification status: **ATTEMPTED, PENDING INDEPENDENT VERIFICATION**.
