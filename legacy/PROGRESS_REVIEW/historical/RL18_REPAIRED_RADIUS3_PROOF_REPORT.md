# RL18 repaired radius-3 proof report

This note supplies the analytic reductions that RL17 found missing and closes the two omitted branches it identified.  It is intentionally explicit about where the external LMN theorem enters and where exact finite certificates enter.

## 1. A reusable three-orbit P2 denominator theorem

Assume a modulus `D>1` coprime to 6 and a unit `rho (mod D)` with

`rho^a = 1/3`, `rho^S = 1/8`,

where `0<=u,v,w<=a`, `u+v+w=S`, and

`1 + 2 rho^u + 4 rho^(u+v) = 0 (mod D)`.

Let `lambda=rho^(-1)`, so `lambda^a=3`.  Reversing the sparse polynomial gives

`g(X)=X^(u+v)+2X^v+4`.

Because `8 rho^S=1`, cyclically rotating `(u,v,w)` gives three equivalent sparse presentations.

### Collision-free resultant bound

Take `f(X)=X^a-3`.  If the exponents `0,v,u+v` are distinct modulo `a`, the resultant is a nonzero integer divisible by `D`.  Applying AM–GM to the values of `g` at the `a` roots of `f`, and Parseval to their squared moduli, yields

`D^2 <= [ 9^((u+v)/a) + 4*9^(v/a) + 16 ]^a`.

For the three cyclic presentations put

`y_i=9^(gap_i/a)`.

Positivity in the applications gives

`y_0 y_1 y_2 = 9^(S/a) < 64`.

If every cyclic presentation had base at least 61, then

`y_(i+1)(y_i+4) >= 45` for i=0,1,2.

Since `1<=y<=9` implies `y+4<=5 sqrt(y)`, multiplication gives

`45^3 <= (product y_i)(product(y_i+4)) < 125*64^(3/2)=64000`,

contradicting `45^3=91125`.  Hence one cyclic presentation has base `<61`, so

**`D^2 < 61^a`.**

### Collision cases

The same conclusion survives all exponent collisions.

- If a gap is 0, the complementary cyclic form is a binomial `1+6 rho^r`; its reciprocal resultant has base at most `9^(r/a)+36<=45`.
- If a gap is `a`, cyclically put it in the omitted position.  The other two gap factors have product `<64/9`, giving a base `<52`.
- If exactly one pair sum equals `a`, the other two cyclic forms are collision-free.  If both had base at least 61, elementary elimination forces `y_w^2+24y_w-225>=0`, but the positive root exceeds the allowed `y_w<64/9`.
- If two pair sums equal `a`, two reduced binomial congruences imply `D|37`, which is stronger than needed except for a trivial tiny case checked directly.

Therefore the three-orbit P2 zero always implies `D^2<61^a`.

## 2. RL12 proof provenance restored

RL12's same-direction sector has

`gcd(A,L)=1`, `gcd(A,m)=3`,

and its three shift orbits reduce to the P2 congruence above with the inherited parameters.  The theorem in Section 1 is exactly the missing infinite denominator envelope.

From that envelope, the inherited RL12 argument applies the rational specialization of the Laurent–Mignotte–Nesterenko two-logarithm theorem, then Legendre/continued fractions, and finally an exact finite certificate.

Fresh execution of the inherited verifier reports:

- LMN cutoff `a<310000`;
- Legendre threshold 291;
- four continued-fraction candidates in the large finite band, all failing the exact denominator barrier;
- 26 small exact barrier parameter pairs;
- 34,620 admissible three-orbit compositions;
- zero canonical zeros.

Thus RL12 is restored as **ANALYTIC + EXTERNAL: LMN + EXACT CERTIFICATE**, not merely “a script passed”.

## 3. RL13 `j=0,P3` strict interior proof provenance restored

Write `L=3ell`.  Then

`sigma^ell=1/2`, and with `tau=sigma^(-1)`, `tau^ell=2`.

For positive gaps `x+y+z=B=A-L`, the P3 polynomial is

`4+6 sigma^x+9 sigma^(x+y)`,

whose reciprocal is

`G(X)=4X^(x+y)+6X^y+9`.

### Near density: `B/L<3/4`

Choose a cyclic orientation with `y` a smallest gap and `x` the next one.  Then

`y < B/3 < L/4 = 3ell/4`,

and

`s=x+y <= 2B/3 < L/2 = 3ell/2`.

Use the irreducible polynomial `X^ell-2`.  In the collision-free case, the same resultant/Parseval method yields

`D^2 <= [16*4^(s/ell)+36*4^(y/ell)+81]^ell < 312^ell < 569^ell`.

If `s=ell`, reduction modulo `X^ell-2` gives `17+6X^y`, with base `<391`.  If `x=ell`, reduction gives `14X^y+9`, with base `<359`.  Hence throughout the near-density region

**`D^2 < 569^ell`, equivalently `D^6 < 569^L`.**

This implies an exponentially small defect.  The inherited LMN + continued-fraction reduction then gives:

- LMN cutoff `L<183000`;
- two upper convergents with `3|L`, both failing the exact barrier;
- 403 finite near-density parameter pairs and 1,410,171 compositions;
- no zeros.

### Far density: `t=B/L>=3/4`

Choose a cyclic orientation omitting a largest gap, so `x+y<=2B/3`.  Pointwise resultant bounds give

`D <= (10*2^(2t)+9)^(L/3)`.

Define

`m(t)=(1+t)log 2 - (1/3)log(10*2^(2t)+9)`.

It is increasing and `m(3/4)>0.0068`.  For `L>=102`, the resulting defect bound is already incompatible with the density inequalities, so `L<102`.  A second coarse bound gives `t<3`, so `A<4L` and the tail is finite.

Fresh execution checks 1,761 far-density parameter pairs and 17,411,907 compositions, with no zeros.

Thus RL13 is restored as **ANALYTIC + EXTERNAL: LMN + EXACT CERTIFICATE**.

## 4. Omitted coefficient-3 P2 boundary: `j=1`

The omitted boundary is

`3+4 sigma^t=0 (mod D)`, `1<=t<L`.

Set `tau=sigma^(-1)`, so equivalently

`3 tau^t+4=0 (mod D)`.

In the `j=1` P2 sector write

`A=2L+3h`, `h>=1`.

The defining power relations give

`tau^h=3/4 (mod D)`.

Therefore `tau` is a common root modulo `D` of

`4X^h-3` and `3X^t+4`.

These two binomials have no common complex root: their roots have incompatible absolute values.  Hence their integer resultant `R` is nonzero, while `D|R`.

A root-product bound gives

`|R| < 4^t 7^h <= 4^(L-1)7^h <= (7/32)2^A`.

On the other hand

`D=2^A-3^L > (29/32)2^A`.

Thus `0<|R|<D` and `D|R`, impossible.

**Conclusion:** the `j=1` coefficient-3 P2 boundary is closed elementarily.  No LMN theorem is used here.

## 5. Omitted coefficient-3 P2 boundary: `j=2`

Write

`A=L+3h`, `h>=1`.

Then

`tau^h=3/2 (mod D)`.

The boundary has two equivalent forms:

`3 tau^t+4=0`,

and, with `z=L-t`,

`tau^z+6=0`.

Choose the shorter exponent `min(t,z)<=L/2`.  Taking the binomial resultant against `2X^h-3`, and using the exact binomial-resultant formula after dividing exponents by their gcd, gives in both cases

`0<|R| < 2^L 7^h`.

A boundary zero therefore forces

`D < 2^L 7^h = 2^A (7/8)^h`.

Positivity gives `L<6h`, hence

**`D/2^A < (7/8)^(L/6)`.**

This exponential defect is incompatible with the LMN lower bound once `L>=335000`.  Legendre reduction applies from `L=341`.  In the intermediate band the only relevant upper convergent satisfying the `j=2` congruence is

`(A,L)=(24727,15601)`,

and it fails the exact denominator barrier.

Below 341 the barrier leaves exactly 13 `(A,L)` pairs.  The `L=1` pair has no boundary exponent; the remaining pairs give 456 exact `t` tests and no zeros.

**Conclusion:** the `j=2` coefficient-3 boundary is closed by ANALYTIC resultant barrier + EXTERNAL: LMN + CF + EXACT CERTIFICATE.

## 6. Omitted `gcd(A,L)=gcd(A,m)=3` sector

Normalize

`A=3a`, `L=3ell`, `m=3n`.

For same-direction radius 3 the discrepancy equation becomes

`a p - 3n ell = 1`.

Let

`rho=2^m 3^(-p) (mod D)`, `D=8^a-27^ell`.

Then

`rho^a=1/3`, `rho^(3ell)=1/8`.

Rotation by `m` has exactly three shift orbits.  The radius-3 prefix flow contains exactly three `-1` events.  Orbit consistency forces one event in each shift orbit.  If `ell_0,ell_1,ell_2` are the three residue-orbit populations, then

`0<=ell_i<=a`, `ell_0+ell_1+ell_2=3ell`,

and the exact orbit telescope gives

**`D|Q(d)` iff `1+2rho^ell_0+4rho^(ell_0+ell_1)=0 (mod D)`.**

Thus this supposedly new cubic sector is governed by the same three-orbit P2 polynomial as RL12.  Section 1 gives

`D^2<61^a`.

Applying LMN and continued fractions gives cutoff `ell<195000` and Legendre threshold 149.  The four large-band upper convergents all fail the exact barrier.  Below 149 only ten parameter pairs remain.  The exact population scan checks 19,630 compositions and finds one arithmetic zero:

`(a,ell; ell_0,ell_1,ell_2)=(2,1;1,1,1)`.

At this parameter set the structural equations force `A=6,L=3,m=3,p=2`.  Exhausting the structural words gives exactly

`101010=(10)^3`,

which is nonprimitive.

**Conclusion:** the omitted `gcd(A,L)=gcd(A,m)=3` sector contains no primitive `D`-divisible radius-3 survivor.

## 7. Verification boundary

The finite checks above certify only the finite tails after the written analytic reductions.  The scripts are not substitutes for the LMN theorem or for the resultant arguments.

Run `verify_rl18_repairs.py`, plus the inherited RL12/RL13 verifiers, to reproduce the finite parts and constants.
