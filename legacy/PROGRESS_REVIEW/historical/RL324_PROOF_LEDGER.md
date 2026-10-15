# RL324 proof ledger — adjacent ownership bridge, canonical half-branch bound, and propagation barrier

Date: 2026-09-14
Status: FROZEN CANDIDATE FOR RL324 CLOSEOUT
BASE_HEAD: `71cd114d91e940a22fd6380abdb41f0a7a8d0e05`

## Scope retained

Work remains in the ordered genuine `g=2` late-row branch inherited from RL315–RL323.

At the conditional first external survivor,

`(a,ell)=(217976794617,137528045312)`,

put

`X=2^a`, `Y=3^ell`, `D0=X-Y`, `H=X+Y`,
`d=a-ell=80448749305`.

The inherited external least-state window remains conditional:

`2^71 <= m < 2^75`.

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.

Gate A remains OPEN. Gate B remains OPEN. Global positive non-trivial-cycle exclusion remains OPEN. `g=1` remains separate.

RL324 starts from the frozen RL323 physical `H`-carry crossing, genuine full `D0/H` ownership identities, zero-carry matched rank, bottom-third residual, and conditional bound

`r<=77265916075`.

## RL324.1 — validated adjacent zero-carry -> unit-minus-one matched rank

For matched odd rank `i`, write

`d_i=u_i-v_i`,
`P_i=U_(u_i)`,
`Q_i=V_(v_i)`,
`Delta_i=2^(d_i)P_i-Q_i`.

At the RL323 zero-carry matched rank `j`,

`d_j=r`,
`Q_j=z=2^r P_j+eta`,
`0<eta<2^r/3`,

so

`Delta_j=-eta<0`.

RL323 gives crossing height `h>=2`. At the final late-row odd rank `u_ell`, the early row can lead by only one odd event immediately before `u_ell`; hence the crossing rank cannot be final:

`j<ell`.

Therefore the legitimate interior recurrence applies, without using the withdrawn RL323 cyclic-wrap claim. Put

`a_j=u_(j+1)-u_j`,
`b_j=v_(j+1)-v_j`.

Then

`2^(b_j) Delta_(j+1)=3 Delta_j+2^(d_j)-1`
`                         =2^r-1-3eta`.

Because `eta<2^r/3`, the right side is nonnegative. Equality is impossible:

- if `d_(j+1)>0`, `Q_(j+1)=2^(d_(j+1))P_(j+1)` contradicts odd parity;
- if `d_(j+1)=0`, equality of the matched physical odd states contradicts primitivity.

Hence

`Delta_(j+1)>0`.

Moreover

`Delta_(j+1)<2^(r-b_j)=2^(d_(j+1)-a_j)`.

Writing `nu=Delta_(j+1)`, the next matched physical state has the exact Euclidean form

`Q_(j+1)=2^(d_(j+1))(P_(j+1)-1)+eta_(j+1)`,

where

`eta_(j+1)=2^(d_(j+1))-nu`

and

`0<nu<2^(d_(j+1)-a_j)<=2^(d_(j+1)-1)`.

Equivalently,

`floor(Q_(j+1)/2^(d_(j+1)))=P_(j+1)-1`.

Classification: **analytic ordinary-physical theorem, support-uniform**.

## RL324.2 — genuine full-ownership sign flip and unique linear matched-rank transition

Let `A_i,C_i` be the genuine complementary `ell`-odd ordinary numerators at matched rank `i`. The frozen RL321/RL323 proper-factor identity gives

`2^(d_i)A_i-C_i = -H Delta_i`.

Therefore at the adjacent pair,

`2^(d_j)A_j-C_j = H eta > 0`,
`2^(d_(j+1))A_(j+1)-C_(j+1) = -H nu < 0`.

This is a sign flip inside genuine full ordinary ownership, not an affine surrogate.

The genuine prefix numerator satisfies

`A_i=D0 P_i-2^(p_i)Delta_i`,
`p_i=a-d_i`.

Thus

`A_j=D0P_j+2^(p_j)eta>D0P_j`,

while

`A_(j+1)=D0P_(j+1)-2^(p_(j+1))nu<D0P_(j+1)`.

The interior recurrence makes positivity of `Delta_i` forward-absorbing, and `Delta_i=0` is physically impossible by the same parity/primitivity argument. Since `Delta_j<0<Delta_(j+1)`, this is the unique sign transition along the linear matched-rank sequence:

- every matched rank through `j` has `Delta_i<0`;
- every matched rank from `j+1` onward has `Delta_i>0`.

No cyclic conclusion is claimed.

Classification: **analytic ordinary-owned sign theorem, support-uniform**.

## RL324.3 — bridge back to the original least-root canonical interface

Let `k` be the RL321 canonical least-root matched rank. There

`z=2^r M+eta`,
`c0=M-m`,
`0<eta<2^r`.

Hence its matched defect is

`Delta_k=2^r m-z=-2^r c0-eta`.

Therefore

`c0>=0  <=> Delta_k<0 <=> k<=j`,
`c0<=-1 <=> Delta_k>0 <=> k>=j+1`.

RL321 also gives

`K=3^s c0+J`,
`0<J<3^s`,

so

`K>0 <=> c0>=0`,
`K<0 <=> c0<=-1`.

This synchronizes the original least-root canonical sign with the physical RL323/RL324 matched-rank transition.

Classification: **analytic parent-interface localization theorem, support-uniform**.

## RL324.4 — original canonical interface is absolutely bounded on the K>0 half-branch

For the original canonical prefix,

`2^p z=Ym+A`,
`z=2^r(m+c0)+eta`,
`p+r=a`.

Therefore

`A=D0m+Xc0+2^p eta`.

If `K>0`, equivalently `c0>=0`, then

`A>D0m`.

The canonical prefix is genuine, has exactly `ell` odd events, starts at the global least odd state `m`, and every odd state it visits is at least `m`. Therefore the RL323.5 zero-count argument applies unchanged.

At the conditional first external survivor,

`q_can=p-ell>=3182833230`,

hence

`r_can=d-q_can<=77265916075`,
`s_can<=r_can`.

Thus the entire `K>0` sign half of the original least-root canonical interface satisfies an explicit absolute support-independent displacement/height bound.

Classification: **analytic reduction plus inherited exact rational constant certificate in externally conditional scope**.

This is a genuine partial realization of RL324 parent target alternative (3), but only for the `K>0` half-branch.

## RL324.5 — the adjacent lower-side prefix retains the same displacement bound

At rank `j+1`,

`A_(j+1)=D0P_(j+1)-2^(p_(j+1))nu`

and

`0<nu<2^(d_(j+1)-a_j)`.

Hence

`A_(j+1)>D0P_(j+1)-X/2^(a_j)`.

In the RL323 normalized zero-count inequality, the new subtractive loss is

`(X/Y) m /(2^(a_j) P_(j+1))`.

If `a_j=1`, the genuine odd-to-odd step gives

`P_(j+1)=(3P_j+1)/2>3m/2`,

so the loss is `<(X/Y)/3`.
If `a_j>=2`, `P_(j+1)>=m` gives the stronger loss `<= (X/Y)/4`.

Using the frozen first-survivor bound `X/Y<1+2^-40`, it is therefore enough to subtract

`(1+2^-40)/3`

from the RL323 exact lower enclosure.

The RL324 verifier checks exactly that at

`q=3182833229`

the remaining certified margin is still positive:

`>0.1224622103775`.

Therefore the same integer threshold survives:

`q_(j+1)>=3182833230`,
`d_(j+1)<=77265916075`.

Since positive integer `nu<2^(d_(j+1)-a_j)`, also

`a_j<=d_(j+1)-1<=77265916074`.

Because the crossing height is at least two, `v_(j+1)<u_j`, so

`b_j<d_j<=77265916075`,

hence

`b_j<=77265916074`.

Thus the zero-carry crossing and its next matched rank form a genuinely physical two-rank bounded box in externally conditional first-survivor scope.

Classification: **analytic reduction plus exact rational boundary certificate in externally conditional scope**.

## RL324.6 — exact local propagation barrier

The bounded two-rank box does not propagate rank-by-rank to an arbitrary later canonical rank.

Take a matched physical interface with

`d=3`,
`Delta=1`,
`Q=8P-1`

for odd `P`.

For any arbitrarily large integer `a>=2`, choose arbitrarily large odd `P` with

`v2(3P+1)=a`.

Such residue classes have arbitrarily large representatives. Then the late-row next odd state is

`P'=(3P+1)/2^a`.

Meanwhile

`3Q+1=24P-2=2(12P-1)`,

and `12P-1` is odd, so the early-row gap is exactly

`b=1`,
`Q'=12P-1`.

The next displacement and defect are

`d'=d+a-b=a+2`,

`Delta'=2^(a+2)P'-Q'=5`.

Thus

`d'=a+2`

is arbitrarily large while

`Delta'=5>0`

remains tiny. Both transitions are genuine ordinary odd-to-odd Collatz transitions. By taking a sufficiently large representative, all four physical states can exceed any prescribed least-state floor.

This is an exact local physical-run counterfamily / method barrier, not a cycle. It proves that the adjacent RL324 theorem, matched-defect recurrence, positive defect, unit-minus-one quotient geometry, and local least-state lower bounds do not by themselves propagate an absolute displacement bound to later matched ranks.

Any successful remaining parent bridge must consume genuinely global structure absent from this counterfamily: full complementary ownership over a longer interval, global least-root placement, the full phase-aligned sign path, or an actual owned descent.

Classification: **analytic exact local physical-run counterfamily / method barrier**.

## RL324.7 — remaining parent branch

RL322 already excludes `Z0<0` at the conditional first external survivor.

RL324 bounds the original canonical interface when `K>0`.

Therefore the unresolved canonical regime is

`Z0>0`,
`K<0`,
`c0=-n<=-1`,
`M=m-n<m`.

From the inherited canonical carry bound and first-survivor scale one has

`1<=n<2^35`.

Hence the genuine nearby integer `M=m-n` can agree in parity with the least-root physical trajectory for at most

`v2(n)<=34`

phases before its first mismatch. This fact alone does not meet RL141/RL142 hypotheses: those theorems concern height-one contact profiles across multiple reduced blocks and do not apply automatically in the live `g=2` branch.

The smallest remaining R1 theorem is therefore global:

> in the unresolved `Z0>0, K<0` regime, consume the genuine full-`D0/H` ownership between the bounded zero-carry/unit-minus-one box and the original least-root canonical cut to force contradiction, a strictly smaller genuinely owned reduced return, or an absolute bound on the original canonical interface.

Local recurrence iteration is explicitly barred by RL324.6.

## Final scope

R1 — Parent Bridge remains OPEN.

Gate A remains OPEN.
Gate B remains OPEN.
R2 — g=2 Closure has not started as a closed-stage claim.
Global positive non-trivial-cycle exclusion remains OPEN.
`g=1` remains separate.

`PARENT_DIFFICULTY_DELTA = EASIER`.
