# RL347 exact analytic certificate

Date: 2026-09-17
Status: CLOSED/FROZEN SUPPORT FOR RL347_PROOF_LEDGER.md

This certificate records only exact arithmetic used by RL347's promoted analytic results.

## Constants

`a = 217976794617`
`ell = 137528045312`
`2ell = 275056090624`
`gcd(a,ell)=1`

The exact inverse is

`a^(-1) mod ell = 65470613321`.

## Decorated-rank identity

With

`H_t=ceil(a t/ell)`,
`u_t=ell H_t-a t`,
`c_t=ell-u_t` with `u_t=0 => c_t=ell`,

one has

`c_t == a t (mod ell)`.

Therefore `c_t` determines `t mod ell`, and the explicit row identity determines the absolute rank
in the two-row traversal.

## Over-half exact bound

Use

`n0=20390252058`

and the exact lower bound

`L2=15757912/22733865 < log 2`.

Then

`S < ell/(2L2)-1/2`.

The inequality

`n-1 < (S+R+1)/6`

implies

`R > 6(n0-1)-1-[ell/(2L2)-1/2]`

and the right side is exactly

`91143694376456377/3939478`

which lies strictly between

`23135982578` and `23135982579`.

Hence

`R>=23135982579`,
`L<=2ell-R<=251920108045`.

## Half-cycle physical separation

For a nondecreasing `L=ell` contact return,

`3^ell E = 2^a S-C`, `C>0`,

so `E<lambda S`. With

`lambda-1<2^-40`,
`S<2^76+2^36`,

one gets

`0<E-S<2^36+1/16`.

Since `E-S` is a positive even integer,

`2<=E-S<=2^36`.

## H-carry quotient algebra

At matched rank `i`,

`h_i=Q_i/(2^(d_i)P_i)=1-e_i/P_i`.

From

`A_i=D0 P_i-Xe_i>0`

one obtains

`e_i/P_i<D0/X=1-1/lambda`;

after the crossing, `e_i>0`, hence

`1/lambda<h_i<1`.

For consecutive ranks,

`P_(i+1)=(3P_i+1)/2^(a_i)`,
`Q_(i+1)=(3Q_i+1)/2^(b_i)`,
`d_(i+1)=d_i+a_i-b_i`,

which eliminates `a_i,b_i` exactly and yields

`h_(i+1)=(3h_iP_i+2^(-d_i))/(3P_i+1)`.

No RL347 finite trajectory enumeration is promoted.
