# FINAL_CHANCE ledger

Append-only. One entry per session. Do not edit prior entries.

## Session N — <date>

**Bridge Theorem attempted:**
<exact falsifiable statement>

**Attack attempted:**
<what was actually tried to break it — countermodel construction, structural
obstruction, or explicit statement that no attack was found>

**Outcome:** SURVIVED / KILLED / INCONCLUSIVE

**Strike this session:** Y/N — <reason if Y>

**Cumulative strikes:** <n>/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
<or "none">

**Carry-forward for next session:**
<one or two lines>


## Session 1 — 2026-09-18

**Bridge Theorem attempted:**
Capture-or-radius-3 bridge.  Let C be an arbitrary hypothetical primitive positive
non-trivial ordinary Collatz cycle, rooted at its least odd state and satisfying
full-D ownership.  After the inherited count/frontier reductions, at least one
of the following must hold:

1. an ownership-preserving reduction/descent sends C into the exact ordered
   genuine g=2, Z0>0, K<0 parent
   (a,ell)=(217976794617,137528045312), preserving the hypotheses needed by
   the RL343--RL349 full physical bridge, so its forced phase-potential-
   nondecreasing return either descends below the least state or belongs to
   O_75; or
2. the parity word of C has two cyclic rotations at adjacent-transposition
   distance at most 3, in the scope of the already-proved primitive/full-D
   radius-3 obstruction.

Thus, if O_75 is empty, the two alternatives would jointly force a
contradiction for an arbitrary hypothetical positive non-trivial cycle.

**Attack attempted:**
The rejected opening attempt merely assigned a formal object to an unbridged
branch; that was not a construction.  Reopening Session 1, I attacked the g=1
first-survivor branch with an explicit word at the actual inherited scale.

Set
A=217976794617, L=137528045312, b_j=floor(Aj/L).
Define h_2=h_4=1 and h_j=0 otherwise, and define the accelerated exponents
a_j=(b_(j+1)-b_j)+h_j-h_(j+1).
The first values are
b=(0,1,3,4,6,7,9,11,12,14,...) and
a=(1,1,2,1,2,2,2,1,2,1,...).
All a_j are positive.  The resulting binary word has length A and weight L,
so gcd(A,L)=1 makes it primitive.  Its odd-prefix positions are
S_j=b_j-h_j; hence every proper prefix satisfies S_j<=b_j and the inherited
floor lock gives 2^(S_j)<3^j.  Consequently its positive rational affine
cycle is strictly least-rooted.  It is a fully specified g=1 object, outside
the current g=2 parent, satisfying the inherited count/primitivity/least-root
geometry before ordinary ownership is imposed.

This word is obtained from the zero-defect mechanical word by moving the ones
at positions 3 and 6 one place left.  Using
s=114208327604, t=72057431991 with sL-tA=1 and
q=65470613321 with qA=1 (mod L), the exact cyclic transport calculation gives
rotation distances 5,6,7,8,9,10,11,12 for determinant residues k=1,...,8.
Every other rotation is at least 5 by the mechanical-distance bound and the
triangle inequality.  Therefore the exact minimum all-rotation radius is 5:
the closed radius-3 theorem does not reject this object.

The remaining full-D ownership condition was then tested exactly.  Writing
rho_j=2^(b_j)/3^j, the candidate numerator satisfies
Q_h/D = (sum rho_j - 68/81)/(3(2^A/3^L-1)).
The mechanical sum was evaluated by the exact Euclidean recursion
F(m,n;x,y)=sum_(j=0)^(m-1) x^j y^floor(nj/m),
F(m,n;x,y) =
[1+(y-1)(x/y)(F(n,r;x^q y,x)-1)-y^(n-1)x^m]/(1-x)
for m=qn+r, with directed 160-digit interval arithmetic.
It gives
36797780658427066316156.3903948169381259690550430756327299785479
< Q_h/D <
36797780658427066316156.3903948169381259690550430756327299785480.
Hence Q_h/D is not an integer and D does not divide Q_h.  The explicit
countermodel attempt therefore fails exactly at ordinary full-D ownership.

A structural subcase also closes.  If a g=1 nonnegative defect profile has
sum_j h_j=1, its word is one adjacent swap from the mechanical word.  The
mechanical determinant-one rotation has distance 1, so the triangle inequality
puts that owned candidate within distance at most 3 of one of its rotations.
The closed primitive/full-D radius-3 theorem excludes it.  Therefore every
genuine g=1 owner at this first survivor must have defect area at least 2.
The area-2 word above proves that least-root/nonnegative-defect geometry alone
already permits radius 5.  RL153's F_1=1 factor collapse leaves the full
one-block congruence D|Q_h as the unresolved owner datum; no existing
factor/carry/local-radius theorem reduces it for arbitrary area>=2 profiles.

**Outcome:** SURVIVED

**Strike this session:** Y — the rejected opening attempt did not complete a
genuine attack; it substituted a scope restatement/formal branch assignment
for the required construction or impossibility argument.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none; all finite arithmetic above was used directly to attack the stated
Bridge Theorem, not to tighten O_75 or Phase 4.

**Carry-forward for next session:**
Do not begin Session 2 here.  The surviving point of attack is exact ordinary
ownership in g=1 defect-area>=2 profiles: either force D not to divide Q_h
uniformly, or construct a full-D-owned radius>=4 profile.  The area-1 class is
now removed from that search.


## Session 1 numerical-method correction — 2026-09-18

This addendum corrects the computational wording in Session 1 without changing
its mathematical outcome, strike, or carry-forward.

The integers
`2^A`, `3^L`, `D=2^A-3^L`, and `Q_h` were **not** materialized.  At
`A=217976794617`, `2^A` alone has about 65.6 billion decimal digits.  The
previous phrases "tested exactly", "exact quotient", and "independently
reproduced" were therefore too strong.

The normalized quotient was evaluated through
[
 Q_h/D =
 \frac{\sum_{j=0}^{L-1}\rho_j 2^{-h_j}}
      {3(\exp(\Delta)-1)},\qquad
 \rho_j=2^{\lfloor Aj/L\rfloor}/3^j,quad
 \Delta=A\log 2-L\log 3.
]
The Beatty sum was reduced by Euclidean recursion, so the computation never
contains an object of length `A` or `L`.  The recurrence printed in the
original Session 1 entry was a transcription error.  For
[
 F(m,n;x,y)=\sum_{j=0}^{m-1}x^j y^{\lfloor nj/m\rfloor},
]
first reduce `n=q m+r` by
[
 F(m,n;x,y)=F(m,r;xy^q,y).
]
For `0<n<m`, writing `m=q n+r` and `r>0`, the recurrence actually used
for the recheck is
[
 F(m,n;x,y)=
 \frac{1-a+(y-1)a\left(
 F\!\left(n,r;\frac1{yx^q},\frac1x\right)-1\right)}
      {1-x},
 \qquad a=y^{n-1}x^m,
]
with the divisible case `r=0` handled by the corresponding finite geometric
sum.

A fresh outward-rounded interval computation at 100 decimal digits, repeated
at 120 digits as a stability check, gives for the Session 1 profile
`h_2=h_4=1`
[
36797780658427066316156.3903948169381259690550430756327299785479312583941924522984
< Q_h/D
]
and
[
Q_h/D <
36797780658427066316156.3903948169381259690550430756327299785479312583941924531107.
]
The width of this 100-digit enclosure is less than `8.13e-55`.  Thus the
reported decimal is a high-precision interval estimate, not a directly
computed giant-integer quotient.  The entire interval stays more than
`0.3903` from the nearest integer, so the numerical conclusion
`D \nmid Q_h` is robust to the stated enclosure error.

The radius claim was also not obtained by enumerating the
`A`-bit word or all `A` rotations.  It was inferred from the inherited
Christoffel/mechanical cyclic-transport identity plus the fact that the
profile differs from the mechanical word by two adjacent left swaps.  In
that model the mechanical determinant-residue classes `k=1,...,8` have
baseline transport distances `1,...,8`; evaluating the four sparse moved
endpoints gives the corresponding predicted distances `5,...,12`, while
the triangle inequality gives lower bound `>=5` for every class whose
mechanical distance is `>=9`.  Hence the transport model pins the minimum
at 5.  This is an analytic sparse-transport inference using small modular
integers, not a direct giant-word verification; there is no floating-point
rounding term in that small-integer transport step, but its validity is
conditional on the inherited transport identity rather than on exhaustive
enumeration.

## Session 2 — 2026-09-18

**Bridge Theorem attempted:**
First-survivor `g=1` area-collapse bridge.  Let a hypothetical primitive
positive ordinary Collatz cycle have full counts
[
(A,L)=(217976794617,137528045312),\qquad \gcd(A,L)=1,
]
be rooted at its least odd state, and have the inherited nonnegative defect
excursion
[
h_j=\lfloor Aj/L\rfloor-S_j.
]
If full ordinary ownership `D=2^A-3^L \mid Q_h` holds, then
[
\sum_{j=0}^{L} h_j \le 1.
]
Combined with the inherited radius-one exclusion for area zero and the
Session 1 radius-three argument for area one, this theorem would eliminate
the entire first-survivor `g=1` branch.

**Attack attempted:**
Area two was attacked directly.

Because `h_j` is a nonnegative integer excursion, rises by at most one, and
starts and ends at zero, total area two cannot contain height two: reaching
height two already requires a preceding positive phase, giving area at least
three.  Therefore every area-two profile is exactly a two-spike profile
[
h_p=h_q=1
]
at two phases, with all other `h_j=0`, subject to the ordinary positivity
condition on the adjacent accelerated exponents.

Put
[
S=\sum_{j=0}^{L-1}\rho_j,\qquad
\rho_j=2^{\lfloor Aj/L\rfloor}/3^j.
]
Every two-spike profile has
[
\frac{Q_{p,q}}D=
\frac{S-(\rho_p+\rho_q)/2}{3(\exp(\Delta)-1)}.
]
Thus area-two ownership is an explicit two-term arithmetic target rather than
an unstructured word search.

As a witness search, the first 1000 phases contain 584 admissible isolated
spike locations.  All `170236=binom(584,2)` pairs were screened numerically
at 90 decimal digits only to select the strongest near-integer candidate;
that screen is exploratory evidence, not a proof about the full area-two
family.  The closest candidate in that screen was
[
p=498,\qquad q=972.
]
Here
[
b_{498}=789,\qquad b_{972}=1540,
]
and the preceding mechanical increments satisfy
[
c_{497}=2,\qquad c_{971}=2.
]
Hence the modified accelerated exponents remain positive:
[
a_{497}=1, a_{498}=2,qquad
a_{971}=1, a_{972}=3,
]
with all other exponents equal to their mechanical values.  This is therefore
a concrete valid area-two nonnegative-defect object.

For this object,
[
\frac{Q_{498,972}}D =
\frac{S-2^{788}/3^{498}-2^{1539}/3^{972}}
     {3(\exp(\Delta)-1)}.
]
The same Euclidean Beatty recursion and outward-rounded 100-decimal interval
arithmetic used in the Session 1 correction gives
[
36797780658465232971971.9999989856644225955131181871237550300443905896826815483422290651487527740866811037
< Q_{498,972}/D
]
and
[
Q_{498,972}/D <
36797780658465232971971.9999989856644225955131181871237550300443905896826815491544330262718501145951158979.
]
The enclosure width is less than `8.13e-55`.  Its distance from the next
integer is greater than
[
1.0143355774044868818128762449699556\times 10^{-6}.
]
Therefore this explicit area-two near-hit still fails ordinary ownership by a
margin roughly `10^{48}` times larger than the numerical enclosure width.
No giant integer `D` or `Q` was constructed.

No area-two owner was found.  This does not prove the area-collapse theorem;
it is a genuine failed construction attempt against it.  The useful reduction
gained this session is that the whole area-two attack is now the two-spike
equation above.

**Outcome:** SURVIVED

**Strike this session:** N — a concrete falsifiable bridge theorem was stated
and directly attacked with an explicit valid area-two object; no new
local-to-global lemma was substituted for the attack.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none; the two-spike reduction and near-hit computation directly attack the
`g=1` Bridge Theorem.

**Carry-forward for next session:**
Do not repeat finite pair screening as a substitute for a theorem.  Attack the
two-spike ownership equation globally: either prove no admissible pair
`(p,q)` can make the normalized quotient integral, or produce a genuinely
owned pair.  If that route structurally fails, state the obstruction before
moving to area at least three.


## Session 1 / Session 2 verifier-artifact addendum — 2026-09-18

Both sessions remain at their recorded **SURVIVED** status, but are classified
here as **ATTEMPTED, PENDING THIRD-PARTY VERIFICATION**.  This addendum does
not advance to Session 3.

The computational claims are now backed by runnable repository artifacts:

- `FINAL_CHANCE/verifiers/verify_session1_interval.py`
  (introduced by commit `99671230c0a6b16e74d292ed71351739753e626b`);
- `FINAL_CHANCE/verifiers/verify_session2_two_spike_screen.py`
  (introduced by commit `ddd3309f790aa54cbdbd749eae221374de055f46`).

Both require only the Python standard library.  Neither materializes
`2^A`, `3^L`, `D`, or the full numerator.  The Session 1 script uses
exact rational atanh-series bounds for `ln 2` and `ln 3`, an exact rational
Taylor/remainder bound for `exp(Delta)-1`, and outward-rounded Decimal
interval arithmetic for the Euclidean Beatty recursion.  Session 2 imports
that same machinery and applies outward intervals to every one of the 170,236
admissible two-spike pairs in the stated `p,q<=1000` screen.

The verifier-produced decimal tails below supersede the earlier handwritten
interval tails in the Session 1 correction and Session 2 entry.  The
mathematical conclusions are unchanged.

### Literal stdout — Session 1 verifier

```
FINAL_CHANCE Session 1 interval verifier: PASS
A = 217976794617
L = 137528045312
profile = h_2=h_4=1, all other h_j=0
method = exact rational log/expm1 bounds + outward Decimal Beatty recursion
precision_digits = 140
Q_h/D lower = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038366708954109182102125518785
Q_h/D upper = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038369665779140219142145179179
interval width = 2.956825031037040019660394E-93
common integer part = 36797780658427066316156
distance above floor >= 0.3903948169381259690550430756
distance below next integer >= 0.6096051830618740309449569244
D divides Q_h = False
```

### Literal stdout — Session 2 verifier

```
FINAL_CHANCE Session 2 two-spike screen: PASS
A = 217976794617
L = 137528045312
screen phases = 1.. 1000
admissible spike positions = 584
screened pairs = 170236
formula = (S-(rho_p+rho_q)/2)/(3*(exp(Delta)-1))
Delta = A*ln(2)-L*ln(3)
rho_j = 2^floor(A*j/L)/3^j
S = sum_{j=0}^{L-1} rho_j
precision_digits = 140
possible owned pair in screen = False
closest pair = (498, 972)
b_p,b_q = (789, 1540)
modified exponents a_497,a_498,a_971,a_972 = (1, 2, 1, 3)
Q_pq/D lower = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983547687718525692993052787956
Q_pq/D upper = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983550644543556730033072448350
interval width = 2.956825031037040019660394E-93
nearest integer = 36797780658465232971972
closest miss distance lower = 0.000001014335577404486881812876245
closest miss distance upper = 0.000001014335577404486881812876245
second closest pair = (431, 549)
second miss distance lower = 0.000002886967966117890667541213507
second miss distance upper = 0.000002886967966117890667541213507
best-vs-second certified separation = 0.000001872632388713403785728337262
```

Session 2's screen therefore contains no interval that meets an integer, and
the nearest screened miss is `(498,972)`; its certified miss interval is
strictly separated from the second-place pair.  This remains only a finite
screen of `p,q<=1000`, not a theorem for all area-two profiles.

No Session 3 work has begun.


## Independent-audit repair addendum — 2026-09-18

Sessions 1 and 2 remain **SURVIVED** and remain **ATTEMPTED, PENDING
THIRD-PARTY RE-VERIFICATION OF THE REPAIRED ARTIFACTS**.  No Session 3 work
has begun.

An independent audit of the first committed verifier versions returned
`VERIFIED WITH NON-MATERIAL CORRECTIONS` for both numerical conclusions,
but identified verification-integrity defects in the repository artifacts:

1. `Decimal.__pow__` is not guaranteed correctly rounded in every case, so
   the old `ipow` implementation did not by itself prove outward containment.
2. The Session 2 filter omitted 415 admissible adjacent-spike profiles, making
   the correct `p,q<=1000` count 170651 rather than 170236.
3. Nearest-integer distance subtractions were occurring in the default
   28-digit Decimal context.
4. The old closest-pair assertion compared the winner only with the pair having
   the second-smallest upper bound rather than with the minimum lower bound
   over the entire remaining field.
5. No RL20-style verifier exists for the Session 1 radius-5 claim.

The independent audit separately recomputed the ownership quotient with a
different exact-integer/binary interval implementation and found the Session 1
quotient strictly inside the old printed interval.  It also screened the 415
omitted Session 2 profiles and found no owner; the closest pair remained
`(498,972)` and the second closest remained `(431,549)`.  Those facts
motivated repairs but do not substitute for the repository artifacts below.

### Repairs committed

`FINAL_CHANCE/verifiers/verify_session1_interval.py` was repaired in commit
`359e73b0fd3f2e805464c200f457910a05dd6c34`.

The verifier now:

- forms integer powers by binary exponentiation through directed interval
  multiplication, never through `Decimal.__pow__`;
- uses explicit directed contexts for interval width and distance-to-integer
  bounds;
- keeps integer-candidate arithmetic in Python integers.

`FINAL_CHANCE/verifiers/verify_session2_two_spike_screen.py` was repaired in
commit `e6e69c9b0e7fa77300b6ec36d9658a3c135966c6`.

The verifier now:

- includes the adjacent case `q=p+1`, for which there is no second rise and
  therefore no requirement `c_(q-1)=2`;
- screens all 170651 admissible pairs with `1<=p<q<=1000`;
- keeps scanning the full field even if an integer-containing interval were
  encountered;
- computes nearest-integer distance bounds with explicit directed rounding;
- proves the winner against the entire field by asserting that its upper
  miss-distance bound is below the minimum lower miss-distance bound of every
  other pair.

The phrases "certified" in the previous verifier-artifact addendum are
superseded by the concrete statement "rigorous outward interval computation";
no such adjective is being used as evidence for the Bridge Problem.

### Literal stdout — repaired Session 1 verifier

```
FINAL_CHANCE Session 1 interval verifier: PASS
A = 217976794617
L = 137528045312
profile = h_2=h_4=1, all other h_j=0
method = exact rational log/expm1 bounds + directed-multiplication Decimal intervals
precision_digits = 140
Q_h/D lower = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038366696764940912155771739196
Q_h/D upper = 36797780658427066316156.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038369677968308489230176038872
interval width <= 2.981203367577074404299676E-93
common integer part = 36797780658427066316156
distance above floor >= 0.390394816938125969055043075632729978547931258394192452757576388503574803981634883377308038366696764940912155771739196
distance below next integer >= 0.609605183061874030944956924367270021452068741605807547242423611496425196018365116622691961630322031691510769823961128
D divides Q_h = False
```

This artifact establishes, subject to third-party execution/review of the
repaired code, that the Session 1 profile `h_2=h_4=1` fails ordinary
ownership.  It does not establish the Bridge Theorem.

### Literal stdout — repaired Session 2 verifier

```
FINAL_CHANCE Session 2 two-spike screen: PASS
A = 217976794617
L = 137528045312
screen phases = 1.. 1000
rise-admissible spike positions = 584
additional admissible adjacent pairs = 415
screened admissible pairs = 170651
formula = (S-(rho_p+rho_q)/2)/(3*(exp(Delta)-1))
Delta = A*ln(2)-L*ln(3)
rho_j = 2^floor(A*j/L)/3^j
S = sum_{j=0}^{L-1} rho_j
precision_digits = 140
possible owned pair in screen = False
closest pair = (498, 972)
b_p,b_q = (789, 1540)
modified exponents a_497,a_498,a_971,a_972 = (1, 2, 1, 3)
Q_pq/D lower = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983547675529357423046699008367
Q_pq/D upper = 36797780658465232971971.999998985664422595513118187123755030044390589682681548801387011151199258355596930463501983550656732725000121103308044
interval width <= 2.981203367577074404299677E-93
nearest integer = 36797780658465232971972
closest miss distance lower = 0.000001014335577404486881812876244969955609410317318451198612988848800741644403069536498016449343267274999878896691956
closest miss distance upper = 0.000001014335577404486881812876244969955609410317318451198612988848800741644403069536498016452324470642576953300991633
second closest pair = (431, 549)
second miss distance lower = 0.000002886967966117890667541213506789605844024301530936807294231097712126549732283140007262351235722505847156937230596
second miss distance upper = 0.000002886967966117890667541213506789605844024301530936807294231097712126549732283140007262354216925873424231341530273
minimum lower bound over all OTHER pairs = 0.000002886967966117890667541213506789605844024301530936807294231097712126549732283140007262351235722505847156937230596
winner separated from whole field by >= 0.000001872632388713403785728337261819650234613984212485608681242248911384905329213603509245898911251863270203636238963
```

This artifact establishes, subject to third-party execution/review of the
repaired code, that no admissible area-two profile with
`1<=p<q<=1000` has an ownership interval meeting an integer.  It remains a
finite screen only; it does not establish the area-collapse Bridge Theorem or
exclude arbitrary area-two profiles.

### Radius-5 correction

The prior Session 1 sentence "the exact minimum all-rotation radius is 5" is
not treated as verified.  What is presently supported is an analytic
sparse-transport inference conditional on the inherited mechanical transport
identity.  No committed verifier independently establishes the all-rotation
minimum at the RL20 standard.  Until such an artifact exists, radius 5 does
not count as independently verified evidence in FINAL_CHANCE.

### Verification state

- Session 1 outcome remains `SURVIVED`; strike remains `Y`; cumulative
  strikes remain `1/3`.
- Session 2 outcome remains `SURVIVED`; strike remains `N`; cumulative
  strikes remain `1/3`.
- The repaired numerical ownership artifacts are ready for independent
  re-verification.
- Session 3 is not opened.


## Verification acceptance note — 2026-09-18

The user reports that the repaired Session 1 and Session 2 verifier artifacts
have both passed independent verification.  Their previous
`ATTEMPTED, PENDING THIRD-PARTY RE-VERIFICATION` flags are therefore cleared.
Their recorded mathematical outcomes and strikes are unchanged:

- Session 1: `SURVIVED`, strike `Y`;
- Session 2: `SURVIVED`, strike `N`;
- cumulative strikes entering Session 3: `1/3`.

The separately downgraded radius-5 wording remains scoped exactly as recorded:
it is not needed for the Session 3 attack below.

## Session 3 — 2026-09-18

**Bridge Theorem attempted:**
First-survivor `g=1` area-collapse bridge.  Let a hypothetical primitive
positive ordinary Collatz cycle have full counts

[
(A,L)=(217976794617,137528045312),
]

be rooted at its least odd state, satisfy full ordinary ownership
`D=2^A-3^L | Q_h`, and have the inherited nonnegative defect excursion

[
h_j=lfloor Aj/Lfloor-S_j.
]

Then

[
sum_{j=0}^{L} h_j le 1.
]

Together with the inherited zero-defect and area-one radius obstructions,
this would eliminate the entire first-survivor `g=1` branch.

**Attack attempted:**
The carry-forward required a global attack on area two rather than another
bounded pair screen.  Session 3 eliminates the entire defect-area-two layer.

By the Session 2 excursion classification, area two is exactly

[
h_p=h_q=1,qquad 0<p<q<L,
]

with all other defects zero.

Put

[
M=A-L=80448749305,qquad
r_j=Ajmod L.
]

Use the corrected RL157 phase normalization.  For height one,

[
P_h(T)=2(1+T+cdots+T^{L-1})-T^{r_p}-T^{r_q},
]

and ownership is equivalent to

[
P_h(ho)=0pmod D,
]

where (ho) also satisfies

[
2ho^L=1pmod D.
]

Multiplying by (ho-1) collapses the dense geometric part.  Every owned
two-spike profile must therefore satisfy

[
E_{r,s}(ho)=0pmod D,
]

where (r=r_p), (s=r_q), and

[
E_{r,s}(T)=1+(T-1)(T^r+T^s).
]

This is the new global lever: the (L)-term ownership polynomial has become
a five-term polynomial without losing the necessary full-(D) condition.

### 3A. Non-adjacent spikes: global resultant contradiction

If the two spikes are non-adjacent, each is entered from defect zero.  The
excursion grammar therefore requires

[
c_{p-1}=c_{q-1}=2,
qquad
c_j=lfloor A(j+1)/Lfloor-lfloor Aj/Lfloor.
]

Because (A=L+M), the exact residue update shows

[
c_{j-1}=2 iff 1le r_j<M
]

for every proper phase.  Hence for a non-adjacent area-two profile,

[
1le r,s<M.
]

Let

[
B(T)=2T^L-1.
]

The reciprocal of (B) is, up to a unit, the Eisenstein polynomial
(T^L-2); hence (B) is irreducible over (mathbb Q).  Since
(deg E_{r,s}le M<L) and (E_{r,s}
e0),

[
R_{r,s}:=operatorname{Res}(B,E_{r,s})
e0.
]

The simultaneous congruences (B(ho)=E_{r,s}(ho)=0pmod D) imply

[
Dmid R_{r,s}.
]

Now put (alpha=2^{-1/L}) and (m=deg E_{r,s}le M).
The roots of (B) are (alphazeta), (zeta^L=1).  Discrete Parseval
and AM-GM give

[
|R_{r,s}|
le
2^m V_m^{L/2},
]

with

[
V_m
=
1+alpha^2+alpha^4+alpha^{2m-2}+alpha^{2m}.
]

If coefficient cancellation occurs, this only decreases the right-hand side.
For real (x), the logarithmic derivative of
(2^xV_x^{L/2}) is

[
(log 2),
rac{1+alpha^2+alpha^4}{V_x}>0,
]

so the bound is increasing in (m) and is maximal at (m=M).

Since (D>0),

[
2^M>(3/2)^L,
]

hence (alpha^{2M}<4/9).  Also (L>14) gives
(alpha^{-2}=2^{2/L}<10/9).  Therefore

[
V_M<3+rac{4}{9}left(1+rac{10}{9}ight)
=rac{319}{81}.
]

Thus

[
|R_{r,s}|
<
2^M(319/81)^{L/2}
=
2^A(319/324)^{L/2}.
]

The exact finite inequality

[
(319/324)^{1828}<2^{-41},
]

together with (L/2>1828), gives

[
|R_{r,s}|<2^{A-41}.
]

Finally, with

[
Delta=Alog2-Llog3,
]

the exact rational log enclosure in the Session 3 verifier proves

[
Delta>rac1{2^{41}-1}.
]

Since (1-e^{-Delta}>Delta/(1+Delta)),

[
D=2^A(1-e^{-Delta})>2^{A-41}.
]

Therefore

[
0<|R_{r,s}|<D,
]

contradicting (Dmid R_{r,s}).  **No non-adjacent defect-area-two owner
exists.**

### 3B. Adjacent spikes: two global size lifts plus a 52-case residual

It remains to take (q=p+1).

Choose the exact Bezout data

[
P=65470613321,qquad U=103768467013,
]

with

[
AP-UL=1.
]

Put

[
T=L-P=72057431991,qquad
S=A-U=114208327604,
]

so

[
AT-SL=-1.
]

The distinguished phase can be represented both as

[
ho=2^U3^{-P}=3^T2^{-S}pmod D.
]

Also

[
ho^{r_j}=2^{b_j}3^{-j}pmod D,
qquad b_j=lfloor Aj/Lfloor.
]

Clearing powers of (3) in
(1+(ho-1)(ho^{r_p}+ho^{r_q})=0) gives the necessary integer
congruence

[
Dmid N_3,
]

where

[
N_3=
3^{P+q}
+
(2^U-3^P)
left(2^{b_p}3^{q-p}+2^{b_q}ight).
]

The inherited floor lock gives (0<2^{b_j}/3^j<1), while
(1/2<2^U/3^P<1).  Hence

[
0<N_3<3^{P+q}.
]

The same exact log lower bound gives
(D>3^{L-26}).  Therefore every adjacent owner with

[
qle T-26
]

is impossible.

Using the complementary representation and clearing powers of (2) gives

[
Dmid N_2,
]

where

[
N_2=
2^{S+A-b_p}
+
(3^T-2^S)
left(3^{L-p}+3^{L-q}2^{b_q-b_p}ight).
]

Here the complementary normalized phase terms are strictly between zero and
one and (1/2<3^T/2^S<1), so

[
0<N_2<2^{S+A-b_p}.
]

Exact floor arithmetic gives

[
b_{T+26}=S+41.
]

Since (D>2^{A-41}), every adjacent owner with

[
pge T+26
]

is impossible.

Thus only

[
T-26le ple T+25,qquad q=p+1,
]

survive the two analytic size arguments: exactly 52 adjacent pairs.

These 52 are checked by the committed artifact

`FINAL_CHANCE/verifiers/verify_session3_area2_global.py`.

It evaluates the necessary ratio (N_3/D) with the repaired directed
interval machinery.  No interval meets an integer.  The closest residual
pair is

[
(p,q)=(72057432000,72057432001)=(T+9,T+10),
]

for which the reproduced enclosure is

[
65708206692263066.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505377
<
N_3/D
]

and

[
N_3/D
<
65708206692263066.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505380.
]

Its interval width is at most (3	imes10^{-123}), and its distance from
the nearest integer is greater than

[
0.0018280877234863993371834006230972.
]

Therefore none of the 52 residual adjacent profiles can satisfy (Dmid N_3).

Combining 3A and 3B:

> **Session 3 theorem:** there is no fully owned `g=1` first-survivor
> defect profile of total defect area exactly 2.

This is global over the complete area-two family; it is not a bounded
`p,q` screen.

The verifier also checks all finite constants used by the resultant/size
bounds and the 52 residual intervals.  Its headline output is:

```
FINAL_CHANCE Session 3 global area-2 verifier: PASS
A,L,M = (217976794617, 137528045312, 80448749305)
Bezout P,U = (65470613321, 103768467013)
complement T,S = (72057431991, 114208327604)
Delta lower > 1/(2^41-1) = True
non-adjacent resultant cutoff exponent = 1828
(319/324)^1828 < 2^-41 = True
non-adjacent area-2 owner possible = False
adjacent low exclusion: q <= 72057431965
adjacent high exclusion: p >= 72057432017
residual adjacent pairs checked = 52
residual integer hit = False
closest residual pair = (72057432000, 72057432001)
offsets from T = (9, 10)
N3/D lower = 65708206692263066.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505377
N3/D upper = 65708206692263066.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505380
interval width <= 3E-123
nearest integer = 65708206692263066
closest miss distance lower = 0.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505377
closest miss distance upper = 0.001828087723486399337183400623097221704182119314116522218285438960636764365133134387734154319193925510487833781568851505380
GLOBAL defect-area-2 owner possible = False
```

**Outcome:** SURVIVED

The Bridge Theorem was not proved: a surviving owned profile could still have
defect area at least 3.  But the attack removes the entire area-two layer,
globally, rather than merely extending the Session 2 finite search.

**Strike this session:** N — the current Bridge Theorem was stated and
attacked directly, and one complete global residual class (all area-two
profiles) was removed.  No new local-to-global bridge was substituted for the
open theorem.

**Cumulative strikes:** 1/3

**Local work done (if any) and its stated connection to the Bridge Problem:**
none.  The resultant collapse, global size bounds, and 52-case residual are
all parts of the direct attack on the stated area-collapse Bridge Theorem.

**Carry-forward for next session:**
Do not continue by merely screening defect area 3, 4, 5, ... one layer at a
time.  The next attack must test whether the ((T-1)P_h) sparse-collapse
mechanism admits a **uniform area>=3/height-independent bound**, or else give
a structural reason it cannot.  The surviving owner class is now exactly
(sum h_jge3).

Session 3 is **ATTEMPTED, PENDING INDEPENDENT VERIFICATION** of the new
analytic argument and `verify_session3_area2_global.py`.  Do not open
Session 4 until that verification state is resolved.


## Session 3 independent verification acceptance — 2026-09-18

The user reports that Session 3 has passed independent verification with verdict
**VERIFIED WITH NON-MATERIAL CORRECTIONS**.  The verified theorem is unchanged:
there is no fully owned `g=1` first-survivor defect profile of total defect area
exactly 2 at
`A=217976794617`, `L=137528045312`.  This is global over the complete
area-two family.  The Session 3 Bridge Theorem itself remains unproved, so the
surviving `g=1` owner class is `sum_j h_j >= 3`.

The independent audit identified three non-material verification-integrity
corrections, recorded here without reopening Session 3:

1. the Session 3 quoted verifier stdout was abridged rather than literally
   complete;
2. the global floor-lock premise is true but was not asserted in the committed
   verifier; the useful exact check is essentially `delta_hi * L < l2_lo`;
3. the Parseval prose should say that coefficient cancellation decreases the
   **Parseval sum / left-hand side**.  The degree `m` and the quantity `V_m`
   remain unchanged because the leading term does not cancel.

These corrections do not alter the Session 3 theorem, outcome, strike, or
carry-forward.  Session 4 is now open under the mandated uniform
height-independent `(X-1)P_h` attack.


## Session 4 — 2026-09-18

**Bridge Theorem attempted:**
Uniform collapsed-Parseval bridge.  For every legal nonnegative first-survivor
`g=1` defect excursion with `sum_j h_j >= 3`, let `H=max h_j`, let
`P_h(X)=sum_(j<L) 2^(H-h_j) X^(Aj mod L)`, and form the exact collapsed
ownership polynomial

```
E_h(X) = 2^(H-1)
         + sum_(ell=1)^H 2^(H-ell) (X-1) F_ell(X),
F_ell(X) = sum_(j: h_j>=ell) X^(Aj mod L).
```

Reduce any `X^L` term with `2X^L-1` to the canonical degree-`<L`
representative, clear only the forced power-of-two denominator, and divide by
integer content.  Write the resulting primitive polynomial as
```
Etilde_h(X)=sum_(k=0)^m e_k X^k,
```
and put `alpha=2^(-1/L)` and
```
V(Etilde_h)=sum_(k=0)^m e_k^2 alpha^(2k).
```
The attempted universal statement was
```
m < L
and
2^m V(Etilde_h)^(L/2) < D,
D=2^A-3^L.
```
If true, ownership would give `D | Res(2X^L-1,Etilde_h) != 0`, while
Parseval/AM-GM would give absolute resultant strictly below `D`, eliminating
all surviving profiles at once.

**Attack attempted:**
The general collapse was derived rather than guessed.  With
`w_j=2^(H-h_j)`, `r_j=Aj mod L`, `P=A^(-1) mod L), and
`sigma(r)=Pr mod L`, write the coefficient of `X^r` in `P_h` as
`a_r=w_(sigma(r))`.  Then
```
(X-1)P_h
 = a_(L-1) X^L - a_0
   + sum_(r=1)^(L-1) (a_(r-1)-a_r) X^r.
```
Thus `X-1` differentiates in residue/exponent order, not chronological
phase order.  Consecutive exponents compare phases separated by
`P=A^(-1) mod L`.

Using
```
2^(H-h_j) = 2^H - sum_(ell=1)^(h_j) 2^(H-ell)
```
and `2 rho^L=1 mod D`, ownership gives exactly
```
E_h(rho)=0 mod D,
E_h(X)=2^(H-1)+sum_(ell=1)^H 2^(H-ell)(X-1)F_ell(X).
```
Equivalently, with
`d_j=2^H-2^(H-h_j)` and
`G_h=sum_(j<L)d_j X^(r_j)`, one has
```
E_h(X)=2^(H-1)+(X-1)G_h(X).
```
If `g_r=d_(sigma(r))`, the coefficients are
`e_0=2^(H-1)`, `e_r=g_(r-1)-g_r` for `1<=r<L`, and
`e_L=g_(L-1)`.  The collapse is therefore a weighted boundary measure in
permuted residue order.

Two structural countermodel families then break the attempted uniform
consequence.

First, at the actual survivor
```
P=A^(-1) mod L = 65470613321,
T=L-P = 72057431991,
c_1=2.
```
For every `3<=N<=P-1`, the single connected height-one excursion
```
h_j=1 for 2<=j<=N+1,
h_j=0 otherwise
```
is legal and has defect area `N`.  If two of its defect residues were
adjacent, their phase separation would be congruent to `+/-P mod L`; but
all positive separations in the interval are at most `N-1<=P-2<P<T`.
Hence every defect residue is isolated in exponent order.  Since the unique
phase of residue `L-1` is `T>P`, no endpoint wrap occurs.  Therefore
```
E_h(X)=1+(X-1) sum_(j=2)^(N+1) X^(r_j)
```
has exactly `2N+1` nonzero coefficients.  At `N=P-1` this is
`130941226641` terms.  So one connected chronological excursion already
produces residue-order complexity growing linearly with defect area.

The first member, `N=3`, has
```
(r_2,r_3,r_4)
=(23369453298,103818202603,46738906596),
```
so
```
deg E_h = 103818202604 > M = 80448749305.
```
Thus the Session 3 `deg E<=M` window fails immediately for a legal connected
area-three profile.

Second, coefficient size is not height-uniform.  The ramp
```
d_j^ramp = floor(Aj/L)-j
```
has increments `c_j-1 in {0,1}`, starts at zero, and reaches `M-1` at
`j=L-1`.  Hence every height `1<=H<=M-1` occurs.  Following the ramp to the
first phase at height `H` and then dropping to zero is legal.  Its primitive
collapse retains constant coefficient `2^(H-1)`: the unique maximum has
weight deficit `2^H-1`, which is odd, while all lower-level deficits are
even, so the power-of-two constant cannot be removed as content.

An explicit height-three member is
```
(h_0,...,h_7)=(0,0,1,1,2,2,3,0),
```
with area nine.  Its five positive-phase deficit weights are
`4,4,6,6,7`, its collapsed polynomial is primitive, has degree below `L`,
and has constant coefficient `4`.  Therefore its Parseval quantity satisfies
`V>=16`, so the exact Session-3-style sufficient upper bound satisfies
```
2^m V^(L/2) >= 16^(L/2) = 2^(2L).
```
But
```
2L=275056090624 > A=217976794617
```
and `D<2^A`.  Hence this Parseval upper bound is already greater than `D`
from the constant term alone.  The attempted universal inequality is false.

These countermodels do not assert full ownership; they disprove the claimed
structural/norm/degree implication from the already-proved excursion grammar,
which is exactly the permitted Session 4 countermodel use.  The exact collapse
identity survives.  What is killed is the promotion of the Session 3
sparse-collapse/degree/Parseval mechanism to a height-independent ownership
contradiction using the presently known defect grammar alone.

The detailed proof is committed at
`FINAL_CHANCE/session4_uniform_collapse_obstruction.md` and the exact arithmetic
artifact is
`FINAL_CHANCE/verifiers/verify_session4_uniform_collapse_obstruction.py`.

Literal verifier stdout:

```
FINAL_CHANCE Session 4 uniform-collapse obstruction verifier: PASS
A,L,M = (217976794617, 137528045312, 80448749305)
inverse phase P,U = (65470613321, 103768467013)
complement T = 72057431991
connected height-one family N range = [3, 65470613320 ]
support count formula = 2N+1
maximum certified family support = 130941226641
area-3 residues = (23369453298, 103818202603, 46738906596)
area-3 collapsed degree = 103818202604
Session-3 degree window M = 80448749305
degree window violated = True
height-3 ramp h[0:8] = (0, 0, 1, 1, 2, 2, 3, 0)
height-3 defect area = 9
height-3 primitive collapsed constant = 4
height-3 collapsed support = 11
2L>A = True
Parseval sufficient bound already > D from e0 alone = True
legal ramp heights include every H in [1, 80448749304 ]
scope=structural grammar countermodels; ownership not asserted
```

**Outcome:** KILLED

The attempted uniform collapsed-Parseval Bridge Theorem is false.  More
structurally, the Session 3 `(X-1)P_h` sparse-support, `M`-degree, and
Parseval-norm mechanism cannot be made height/area independent from the
currently known defect excursion grammar.  The reason is the mismatch between
chronological locality and residue-order differentiation.

**Strike this session:** N — Session 4 stated an exact universal bridge,
derived its general collapse, and attacked it directly with parametric and
explicit legal countermodels.  The negative result is the mandated Outcome C,
not a substitute local computation.

**Cumulative strikes:** 1/3

**Local work done and connection to Bridge Problem:**
No unrelated local work.  The committed verifier checks only the exact
arithmetic and grammar facts needed for the direct structural countermodels.
It does not enumerate area-three owners and does not test ownership.

**Carry-forward:**
Do not open Session 5 until this result is independently audited.  If verified,
do not retry the Session 3 sparse/degree/Parseval argument from excursion
grammar alone and do not start area-by-area enumeration.  Any future bridge
using `E_h` must import genuinely new ownership-specific information coupling
phases separated by `P=A^(-1) mod L`, or a genuinely global complementary-lift
mechanism not reducible to the failed residue-order norm/degree bound.

Verification status: **ATTEMPTED, PENDING INDEPENDENT VERIFICATION**.


## Strike-count / Session 4 verification disposition — 2026-09-18

By explicit user instruction, the cumulative FINAL_CHANCE strike count entering
Session 5 is **2/3** across the full FINAL_CHANCE programme.  This supersedes
the `1/3` count written in the Session 4 entry without editing that append-only
historical entry.

The user also accepts the nature of the Session 4 result as a structural
`KILLED` countermodel result and explicitly waives independent verification as
a prerequisite to opening Session 5.  Session 4 is therefore treated as
closed for programme-flow purposes.  Its mathematical scope remains exactly as
stated: the uniform sparse/degree/Parseval consequence from the present defect
grammar is killed; no full-owner countermodel was claimed.

Session 5 is now open at cumulative strikes **2/3**.  If Session 5 incurs a
strike, the count becomes `3/3` and the next session must mechanically file a
STOP verdict under `FINAL_CHANCE/README.md`.


## Session 5 — 2026-09-18

**Bridge Theorem attempted:**
Two-sided endpoint-lift bridge.  Let `h` be any legal nonzero nonnegative
first-survivor `g=1` defect excursion with `sum h_j>=3`, and suppose its real
ordinary quotient lies in the inherited state window
```
2^71 <= Q_h/D < 2^75,
D=2^A-3^L.
```
Let
```
p=min{j:h_j>0},
q=max{j:h_j>0}.
```
Using the exact endpoint lifts `K_3(q)` and `K_2(p)` defined below, the
attempted universal statement was:

> at least one of `K_3(q)` or `K_2(p)` is a positive integer strictly below
> `D`.

Every actual full owner makes both endpoint lifts divisible by `D`.  Thus the
statement, if true, would exclude every surviving profile at once.

**Attack attempted:**
Write the inherited Bezout data as
```
P=65470613321, U=103768467013,
T=L-P=72057431991, S=A-U=114208327604,
AP-UL=1, AT-SL=-1.
```
Retain the exact collapse
```
E_h(X)=2^(H-1)+(X-1)G_h(X),
G_h(X)=sum d_j X^(r_j),
d_j=2^H-2^(H-h_j),
r_j=Aj mod L,
```
with full ownership implying `E_h(rho)=0 mod D`, and
```
rho=2^U 3^(-P)=3^T 2^(-S) mod D,
rho^(r_j)=2^(b_j)3^(-j)=3^(L-j)2^(b_j-A) mod D.
```

For the last defect `q`, multiply by `3^(P+q)`.  The exact factor
`2^(H-1)` cancels because `D` is odd.  With
```
R_3(q)=sum_(j<=q) 3^(q-j)(2^(b_j)-2^(b_j-h_j)),
```
every owner satisfies
```
D | K_3(q),
K_3(q)=3^(P+q)+2(2^U-3^P)R_3(q).
```
Put `x_3=P log3-U log2>0`.  The floor lock gives
`1/2<2^(b_j)/3^j<1`, hence
```
0<R_3(q)/3^q<q+1.
```
Since `1-exp(-x_3)<x_3`, the exact rational-log check
```
2 x_3 (T-25) < 1
```
shows `K_3(q)>0` for every `q<=T-26`.  Also
```
K_3(q)<3^(P+q)<=3^(L-26)<D.
```
Therefore every actual owner has
```
q >= T-25 = 72057431966.
```

For the first defect `p`, one has `h_p=1`.  Since the exponent sums
`S_j=b_j-h_j` are strictly increasing, `S_j>=b_p-1` for `j>=p`, making
```
R_2(p)=sum_(j>=p) 3^(L-j)
       (2^(b_j-b_p+1)-2^(b_j-h_j-b_p+1))
```
an integer.  The complementary lift gives
```
D | K_2(p),
K_2(p)=2^(S+A-b_p)+(3^T-2^S)R_2(p).
```
Put `x_2=S log2-T log3>0`.  Since
```
3^(L-j)2^(b_j-A)<1,
R_2(p)/2^(A-b_p)<2(L-p),
```
and `1-exp(-x_2)<x_2`.  The exact check
```
2 x_2 (P-26) < 1
```
therefore gives positivity for `p>=T+26`.  Exact floor arithmetic gives
```
b_(T+26)=S+41,
```
so in that range
```
0<K_2(p)<2^(A-41)<D.
```
Thus every actual owner has
```
p <= T+25 = 72057432016.
```

This proves the global owner reduction
```
p <= 72057432016,
q >= 72057431966.
```
It is uniform in height, total defect area, component count, and run length.
It does not assert that a defect occurs inside the central 51-phase window;
early/late components may be separated by zero defect.

The full endpoint-size Bridge Theorem was then attacked by the single connected
height-one excursion
```
h_j=1 for 2<=j<=T,
h_j=0 otherwise.
```
It is legal because `c_1=2`, has
```
p=2, q=T, sum h_j=T-1=72057431990,
```
and is not an area-by-area construction.

Using only the verified global floor lock `1/2<rho_j<1`, its real quotient is
bounded by
```
(P+1)/2+(T-1)/4
 < sum rho_j 2^(-h_j)
 < (P+1)+(T-1)/2.
```
The exact rational log/exponential bounds prove
```
2^71 < Q_h/D < 2^75.
```
Thus it lies inside the same inherited real state-size window required of an
owner, although no integrality/ownership is asserted.

For this profile the last-defect lift has `q=T`, hence
```
K_3(T)/3^L > 1-2x_3(T-1) > 1/4,
D/3^L=exp(Delta)-1 < 1/1000,
```
so `K_3(T)>D`.

The first-defect lift has `p=2`, `b_p=3`, and the same run has only `T-1`
defect terms.  The exact bound
```
1-2x_2(T-1)>1/8
```
gives
```
K_2(2)>2^(S+A-6)>2^A>D.
```
Therefore both natural endpoint lifts exceed `D` for a legal connected
profile already in the inherited real state window.  This is a direct
countermodel to the proposed structural endpoint-size implication.  It is not
claimed to satisfy full ownership.

Detailed proof:
`FINAL_CHANCE/session5_endpoint_lift_obstruction.md`.

Exact verifier:
`FINAL_CHANCE/verifiers/verify_session5_endpoint_lift_obstruction.py`.

Literal verifier stdout:

```
FINAL_CHANCE Session 5 endpoint-lift obstruction verifier: PASS
A,L,M = (217976794617, 137528045312, 80448749305)
P,U,T,S = (65470613321, 103768467013, 72057431991, 114208327604)
global floor lock delta_hi*L < ln2_lo = True
owned last defect q <= 72057431965 = impossible
owned first defect p >= 72057432017 = impossible
owner endpoint span forced: p <= 72057432016 and q >= 72057431966
countermodel = connected height-one run 2..T
countermodel run length = 72057431990
countermodel real quotient in [2^71,2^75) = True
countermodel K3 > D = True
countermodel K2 > D = True
scope=structural endpoint-size countermodel; full ownership not asserted
```

**Outcome:** KILLED

The proposed universal assertion that one of the two endpoint lifts must be a
nonzero representative below `D` is false even after imposing the inherited
real state-size window.  The one-sided complementary-lift mechanism therefore
cannot by itself close arbitrary surviving profiles.

A nontrivial global theorem survives the attack: every actual owner must have
its first-to-last defect span cross the resonant window in the precise endpoint
sense
```
p<=T+25, q>=T-25.
```

**Strike this session:** N — an exact global bridge was stated and attacked
directly; the countermodel kills the proposed structural implication, while
the same attack proves a uniform all-height/all-area owner reduction.  No
finite area screen or substitute local lemma was used.

**Cumulative strikes:** 2/3

**Local work done and connection to Bridge Problem:**
No unrelated local work.  The only finite arithmetic consists of exact
constant/log inequalities needed for the endpoint lifts and the structural
countermodel.

**Carry-forward:**
Session 6 is the final budgeted FINAL_CHANCE session unless a STOP verdict is
triggered earlier.  Do not retry separate endpoint-size bounds, the killed
Session 4 sparse/degree/Parseval route, or area-by-area enumeration.  The only
surviving direction exposed here is a genuinely **two-sided ownership
interaction across the resonant cut**: a theorem must couple early and late
defect contributions rather than bounding either endpoint in isolation.  The
Session 5 endpoint-span theorem is the exact inherited reduction for that
attack.


## Session 5 concurrent-work integration note — 2026-09-18

While Session 5 was in progress, a second ownership-specific attack landed on
`main` under the same Session 5 scope:

- `FINAL_CHANCE/session5_ownership_boundary_collar.md`;
- `FINAL_CHANCE/verifiers/verify_session5_boundary_collar.py`;
- `FINAL_CHANCE/verifiers/verify_session5_ownership_window_barrier.py`.

This work is mathematically compatible with the Session 5 endpoint-lift entry
above and is **strictly stronger as a positive owner reduction**.  It does not
resurrect the killed endpoint-size bridge.  The connected height-one
countermodel in the ledger is explicitly non-owned and only proves that
state-window/grammar information cannot force either endpoint lift below
`D`.  The boundary-collar attack instead uses exact physical first-defect and
last-defect state cylinders, CRT, and the actual forward accelerated orbit.

Subject to its stated independent-verification status, the boundary-collar
result is
```
p + (L-q) <= 37
```
for every surviving actual owner.  Its committed exact verifier reports 1848
boundary signatures with `p+(L-q)>=38`, 2,056,165 state candidates across
those signatures, 1,370,780 distinct least-state candidates, and rejection of
every candidate by phase 194.  The residual family has 744 boundary signatures
supported on 21 possible first-defect positions, with largest first-defect
phase 36.

Programme-level interpretation of Session 5 is therefore:

- the **endpoint-size** Bridge Theorem recorded above is `KILLED`;
- a distinct **two-sided boundary-cylinder** Bridge Theorem remains unproved
  but has been reduced to 744 exact boundary signatures;
- Session 5 earns **no strike**; cumulative strikes remain **2/3**;
- the stronger boundary-collar reduction, once independently accepted, should
  supersede the weaker `p<=T+25, q>=T-25` endpoint-span theorem for Session 6
  carry-forward;
- Session 6 must not treat the 744 signatures as 744 complete defect profiles:
  arbitrary middle area, height, component count, and run structure remain.

The positive boundary-collar result remains **ATTEMPTED, PENDING INDEPENDENT
VERIFICATION** as stated in its committed report.  This addendum does not claim
that independent verification has occurred.


## Session 5 — 2026-09-18

**Bridge Theorem attempted:**
Two-sided transfer closure bridge.  At the actual first-survivor counts
`A=217976794617`, `L=137528045312`, there do not exist an odd integer
`
2^71 <= m < 2^75,
`
a complete nonnegative defect excursion `h_0=h_L=0` with
`
a_j=c_j+h_j-h_(j+1)>=1,
`
and endpoint orbit data such that all of the following hold simultaneously:

1. the first 75 exponents are the exact accelerated Collatz valuations of a
   genuine forward orbit starting at `m`;
2. every proper state in that 75-step prefix is strictly larger than `m`;
3. the last 75 exponents are the exact accelerated Collatz valuations of a
   genuine physical suffix ending at the **same** `m`;
4. every proper state in that 75-step suffix is strictly larger than `m`;
5. the prefix and suffix defect heights extend to one complete legal
   nonnegative defect path with the inherited total counts.

Every genuine fully owned least-rooted singleton cycle necessarily satisfies
all five conditions, so this theorem would eliminate the whole surviving
`g=1` branch without defect-area enumeration.

**Attack attempted:**
The theorem was attacked by constructing an explicit same-`m` countermodel.
Take
```
m=2^75-1=37778931862957161709567.
```
This lies in the physical state window
```
2^71 <= m < 2^75.
```

Running the genuine accelerated Collatz map forward from this `m` for 75 odd
steps gives the exact valuation word
```
1^74,2.
```
Its total exponent is `S_75=76`.  With
`b_j=floor(Aj/L)`, the induced prefix defect `h_j=b_j-S_j` is
nonnegative throughout and ends at
```
b_75=118,
h_75=42.
```
The prefix defect area through phase 75 is already `1629`.  Every proper
prefix state is strictly larger than `m`, and the exact terminal state is
```
304133393856678854559841996309430653.
```
Thus the prefix is an exact physical least-rooted segment, not merely a
modular word.

A physical 75-step suffix returning to the **same** `m` was then built
backwards.  At each step `j`, with known odd `y_(j+1)` and defect
`h_(j+1)`, choose the smallest positive exponent `a_j` of the parity
required by
```
2^a_j y_(j+1) == 1 (mod 3)
```
which also gives
```
h_j=a_j-c_j+h_(j+1)>=0
```
and a predecessor
```
y_j=(2^a_j y_(j+1)-1)/3
```
not divisible by 3.  If the first parity-compatible exponent produces a
multiple of 3, increase it by 2 and repeat.  For the actual final 75 phases
this deterministic exact construction gives
```
h_(L-75)=53,
```
maximum suffix exponent `4`, maximum suffix defect `53`, and suffix-start
state
```
371804656870741614109061597054976841273.
```
Replaying the suffix forward verifies every chosen exponent as the exact
2-adic valuation and returns exactly to `m`.  Every proper suffix state is
also strictly larger than `m`.

The two physical ends are compatible with one complete legal defect path.
After the prefix, drop from `h_75=42` to `h_76=0`; the corresponding
exponent is positive.  Keep `h=0` through the long middle.  At
```
j_0=(L-75)-90=137528045147
```
start the tight recurrence
```
h_(j+1)=h_j+c_j-1.
```
Across those 90 actual phases it accumulates exactly 53 rises, so it reaches
```
h_(L-75)=53,
```
matching the physical suffix boundary.  Every tight-ramp exponent equals 1.
The constructed suffix then returns the defect to `h_L=0`.

Hence one complete nonnegative positive-exponent defect excursion exists with
exact total counts.  The identity
```
a_j=c_j+h_j-h_(j+1)
```
telescopes to
```
sum a_j = sum c_j + h_0-h_L = A.
```

What is deliberately **not** asserted is that the physical state reached by
the exact prefix evolves through the enormous middle to the physical
suffix-start state.  That missing global middle connection is the only failed
condition, and it is precisely the Bridge Problem that the attempted theorem
was supposed to derive from the endpoint ownership-transfer data.

Therefore exact prefix capture + exact suffix capture + the same candidate
least state + the physical state window + least-root behavior on both ends +
a complete legal nonnegative defect excursion do **not** imply global physical
closure.

The main exact artifact is
`FINAL_CHANCE/verifiers/verify_session5_two_sided_transfer_countermodel.py`.
Its reproduced literal stdout is:

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

Session 5 also red-teamed the coarser ownership consequence
`m=Q_h/D in [2^71,2^75)`.  The supporting artifact
`FINAL_CHANCE/verifiers/verify_session5_ownership_window_barrier.py` encodes
the result that the state window alone does not control the Session 4 support
or height obstructions.  The exact same-`m` countermodel above is the stronger
Session 5 result and does not depend on that interval calculation.

**Outcome:** KILLED

The attempted two-sided ownership-transfer Bridge Theorem is false.  The
RL154-style endpoint transfers remain exact necessary information, but they do
not bridge the global middle orbit even when both ends select the same physical
least-state candidate and the complete defect grammar is simultaneously
satisfied.

**Strike this session:** N — Session 5 stated a precise universal bridge and
attacked it directly with an explicit exact structural countermodel.  This is
a genuine Bridge-Problem kill, not local enumeration or a confidence update.

**Cumulative strikes:** 2/3

**Local work done and connection to Bridge Problem:**
No unrelated local work.  Both Session 5 verifier artifacts directly test
ownership-derived state-window / endpoint-transfer information.  No defect
area was enumerated.

**Carry-forward:**
Do not begin Session 6 here.  Session 6 is the final budgeted FINAL_CHANCE
session.  It must attack a theorem that enforces the **actual global physical
middle connection** between ownership-compatible endpoint data.  Reusing
state-window bounds, local defect grammar, prefix/suffix residues, matching a
candidate `m`, bare resultants, or equivalent distinguished-root encodings is
insufficient by the Session 4--5 countermodels.  If Session 6 cannot prove or
structurally kill such a genuinely global bridge, the six-session budget is
exhausted and the programme must close under the README verdict conventions.

Verification status: exact integer countermodel reproduced by the committed
verifier; no independent audit has been supplied.


## Session 6 — 2026-09-18

**Bridge Theorem attempted:**
Full-affine middle bridge.  At the actual first-survivor counts
A=217976794617 and L=137528045312, there is no positive rational cyclic
solution of the ordinary accelerated +1 equations

3 y_j + 1 = 2^(a_j) y_(j+1)

which simultaneously has positive exponents summing to A, a complete
nonnegative defect excursion h_j=floor(Aj/L)-S_j with area at least three,
strict least root y_0, inherited state window 2^71<=y_0<2^75, and first/last
defect boundary collar p+(L-q)<=37.

Every genuine fully owned least-rooted integer g=1 cycle is a special case.
If true, this theorem would supply the missing global physical middle bridge
left by Session 5.

**Attack attempted:**
Take the explicit profile

h_0=h_1=h_L=0,
h_j=1 for every 2<=j<=L-1.

Then p=2 and q=L-1, so

p+(L-q)=3,

far inside the Session 5 collar.  Its defect area is L-2=137528045310.

With b_j=floor(Aj/L), c_j=b_(j+1)-b_j and
a_j=c_j+h_j-h_(j+1), the actual endpoint increments are

c_0=1, c_1=2, c_(L-1)=2,

hence

a_0=1, a_1=1, a_(L-1)=3,

and every other interior exponent is c_j in {1,2}.  All exponents are
positive, and telescoping h_0=h_L=0 gives sum a_j=A exactly.

For any positive exponent word with D=2^A-3^L>0, composing the entire ordinary
accelerated +1 recurrence gives the unique rational cyclic return

D y_0 = Q_h.

For this profile, with rho_j=2^floor(Aj/L)/3^j and
S=sum rho_j,

sum rho_j 2^(-h_j) = S/2 + 5/6.

Using the rigorous outward interval machinery already committed for Session 1,
a local closeout replay gives

18398890329678333925084.865203331289733771357436326005784942633867092203763859573970283284744380731873371091868324264839575846945736746080741

< Q_h/D <

18398890329678333925084.865203331289733771357436326005784942633867092203763859573970283284744380731873371091868324266330177530734273948230581.

The interval width is at most 1.490601683788537202149840e-93.  Hence

2^71 < Q_h/D < 2^75,

but the whole interval lies strictly between the consecutive integers
18398890329678333925084 and 18398890329678333925085.  Therefore D does not
divide Q_h.

For every proper phase, S_j=b_j-h_j<=b_j and the inherited floor lock gives
2^(S_j)<3^j.  The exact affine prefix identity then implies y_j>y_0.
Thus the rational full-period +1 orbit is strictly least-rooted.

The countermodel therefore has the exact (A,L) counts, positive exponents,
complete nonnegative defect grammar, huge surviving area, collar size 3, the
state window, strict least-root order, and the actual ordinary +1 recurrence
through the whole middle with exact cyclic closure over positive rationals.
It fails only integer ownership.

The structural reason is exact: for a fixed positive word,

D m = Q.

Thus integer middle closure is equivalent to D|Q.  RL167 already proves that
once one full affine numerator is divisible by D, all rotated quotients are
automatically positive integer physical states.  Full integer middle closure
is therefore not an intermediate bridge weaker than ownership; it is
ownership itself.

Detailed proof:
FINAL_CHANCE/session6_full_affine_middle_bridge_barrier.md

Verifier:
FINAL_CHANCE/verifiers/verify_session6_full_affine_middle_barrier.py

**Outcome:** KILLED

The strongest remaining natural middle bridge is false over positive rationals.
Adding integrality would make it exactly the original full-ownership condition,
not a consequence supplied by the inherited local/finite/branch-restricted
machinery.

**Strike this session:** N — a concrete global falsifiable bridge was stated
and attacked directly with an explicit full-period ordinary +1 affine
countermodel.

**Cumulative strikes:** 2/3

**Local work done and connection to Bridge Problem:**
None unrelated.  The only computation was the rigorous quotient enclosure for
the direct global countermodel.

**Carry-forward:**
None inside FINAL_CHANCE.  The six-session budget is exhausted.  The remaining
mathematical condition is full ordinary ownership D|Q_h itself.  Any future
research would need genuinely new arithmetic that attacks that condition
directly rather than another bridge from the already-proved local machinery.

Programme verdict is filed in FINAL_CHANCE/VERDICT.md.
