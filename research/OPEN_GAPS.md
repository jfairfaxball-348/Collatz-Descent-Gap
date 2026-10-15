# Open theorem obligations — the only live gap

**Goal DG-GAP-01:** prove that the natural-density-zero exceptional set E contains no positive integer.

## A. Positive-integer realisation obstruction (priority)
At depth k, each parity cylinder can survive temporarily; prove a uniform-in-k arithmetic restriction on *positive integers* ruling out an infinite nested chain of no-descent prefixes. 2-adic compatible infinite words exist, but a 2-adic object is not automatically an ordinary positive integer. **Required:** an actual theorem excluding each hypothetical fixed n in E; do not confuse decreasing densities with non-existence.

## B. Least-exception arithmetic
Assume n=min E (if E is nonempty); n is odd because even n descends in one step. Identify extra arithmetic forced simultaneously at every depth. Note that iterates of n need not themselves belong to E, and inverse predecessors of n need not be exceptional. Any propagation argument must prove, not presume, exception preservation.

## C. Quantitative-to-empty upgrade
Find a structural lower bound on prevalence **conditional on E nonempty** which is genuinely incompatible with the known upper bounds. Density-zero-compatible infinite sets and bounded exceptional sets are countermodels to a purely measure-theoretic deduction. A claimed conditional positive-density lemma requires independent arithmetic proof, not mere restatement of Collatz.

## Immediate falsification tests
- For each k, n=2^k t-1 survives k steps: no universal fixed k works.
- Every even n>=2 descends on step 1: multiplying a hypothetical exception by 2 does not produce a new exception.
- A local parity/residue 'certificate' must include a global compatibility or positive-integer realisation argument.
- A cycle-only exclusion is insufficient: E could in principle also include unbounded non-descending trajectories.

## Progress criterion
Advance only when an explicit mathematically verified statement genuinely narrows E or proves impossibility of a whole class of permanent survivors. No percentage, forced audits, last-chance countdowns, or automatic retirement of the programme.


## DG002 findings and precise surviving obstruction (2026-10-15)

- **Proved:** for a fixed parity block w with multiplier A=3^s, D=2^m, q>=0, t complete repetitions from integer x require D^t | (D-A)x-q. An expanding block A>D satisfies D^t <= (A-D)x+q; its infinite periodic itinerary corresponds to a negative rational 2-adic value, not a positive integer. Positive *eventually periodic* parity itineraries are actual eventual integer cycles, so the unknown nontrivial-cycle case remains open.
- **Proved, genuinely nonperiodic:** a run of t expanding w-blocks starting at orbit time J obeys D^t <= (A-D)((3/2)^J(n+1)-1)+q. For w=110 this reads 8^t <= (3/2)^J(n+1)+4. The explicit coherent infinite word built from (110)^(J_i+1) with separated odd bits (J_(i+1)=4J_i+4) has M(prefix)=infinity for every prefix yet **no positive integer** can realise the word. Hence even a fully compatible *nonperiodic*, uniformly supercritical sequence of finite cylinders is not a bridge to E nonempty.
- **Proved, true restriction on E:** each n in E has s_k >= ceil(k log2/log(3+1/n)), in particular s_k>k/2 for all k. This is necessary but allows many non-realised 2-adic paths; no proof that all positive-integer realisations eventually fail.
- **Sharp counterexamples:** n_t=8^t-5 survives (110)^t for 3t steps, attains the cross-depth lower bound, and varies with t. The usual n=2^k t-1 long-odd-prefix counterexample also remains valid.

**Open DG-GAP-01 unchanged:** E empty is unproved. The next genuinely useful bridge must rule out a **fixed positive integer n** with a nonperiodic non-descending path not blocked by the new congruence and drift inequalities, or derive an incompatible prevalence lower bound conditional on its existence. Merely excluding paths already unrealised by any positive integer is not a net elimination of E. Try combining exact DG001 prefix values at separate times with DG002 shifted congruences, not just generic exponential envelopes. See [DG002 proof](sessions/DG002.md) and [DG003 prompt](NEXT_SESSION_DG003.md).


## DG003: exact new restrictions and sharper unsolved obligation (2026-10-15)

- **Cross-depth collapse (DG-003-A):** If prefix u (length J) is followed by w^t (length mt), the congruence \(2^{J+mt}\mid(2^m-3^{s(w)})(3^{s(u)}n+q_u)-2^Jq_w\) is **equivalent** to the single cylinder for uw^t. Different depths of the *same* parity itinerary do not secretly give an independent constraint on a fixed positive integer. Repeating this approach without new non-cylindrical input is not a bridge.
- **Safe inverse-ancestor theorem (DG-003-B):** A safe finite rising predecessor z≥2 below y∈E must itself lie in E. Thus if m=min E, then m is *not* 5 modulo 6, 13 modulo 18, or 91 modulo 162. Those three disjoint infinite classes account for 37/81 of the odd residues mod 162 as candidate locations of **min E**. This does NOT show they contain no nonleast E-members.
- **Dynamical consequence (DG-003-C):** Any unbounded forward orbit of n∈E contributes infinitely many unbounded values in E, via tail minima. Hence E nonempty implies a nontrivial periodic orbit OR infinite E. This is **compatible** with Terras–Everett's zero density (infinite sparse sets can have zero density).
- **Inverse method barrier (DG-003-D):** For any m divisible by 3, the only backward Collatz ancestors are 2^j m, all larger than m. Safe shrinking inverse methods alone cannot rule out least exceptions divisible by 3.
- **Unsolved:** Establish a non-circular universal obstruction for possible remaining least exceptions (including multiples of 3), or a provable quantitatively incompatible abundance of genuine exceptional integers. A correct theorem must apply to actual positive-integer orbits, not merely coherent 2-adic parity cylinders. Next prompt: [DG004](NEXT_SESSION_DG004.md).


## DG004: record-minimum abundance and deeper least-element exclusions (2026-10-15)

- **DG-004-A/B proved:** strict prefix-expanding parity words `w` provide safe smaller inverse ancestors on exact `3^{s(w)}`-adic endpoint classes, whenever `z=(2^{|w|}y-q_w)/3^{s(w)}>=2`. Two nonredundant nine-step words ban `min E≡433,1333 (mod 1458)`. With DG003, 335 of 729 **odd** residues at modulus 1458 are forbidden locations of `min E`. This is **not** an E-density result or exclusion of all E in those progressions. A systematic length<=9 strictly expanding word enumeration checked 89 candidates; broader safe words are not exhausted.
- **DG-004-C proved:** If an E-orbit is unbounded, its successive actual exceptional tail minima `a_j` satisfy `a_j<a_(j+1)<=T(a_j)`, with `a_j≡3 mod4`. Therefore for `X>=n`, `|E∩[2,X]|>=1+floor(log_(3/2)((X+1)/(n+1)))`. If `a_j≡3 mod8`, the next minimum is at most `(9a_j+5)/8`. This *rules out excessively sparse record-minimum schedules*, but remains consistent with E having density zero.
- **Falsification:** the abstract sequence `4floor(10(5/4)^j)+3` is `3 mod4`, grows within the same adjacent record bound, yet its set has density zero. It is not an actual Collatz trajectory; it prevents inferring density from the bounds **alone**.
- **Precise unresolved bridge:** demonstrate a Collatz-specific coupling or overlap restriction between *actual* consecutive record minima and their safe ancestors strong enough to contradict density zero, or eliminate possible least-E roots (including `m≡0 mod3`) by a non-circular global mechanism. DG003's no-shrinking-inverse obstruction for multiples of three still holds. No whole-E family with parameter-unbounded descent horizon was proved. [Full DG004](sessions/DG004.md); [next DG005](NEXT_SESSION_DG005.md).


## DG005: 3-adic record coupling and live obstruction (2026-10-15)

- **DG-005-A:** For any odd starting value, every positive-time iterate is nonzero modulo 3. Hence later suffix minima on an unbounded exceptional orbit are 1 or 2 mod 3. Successive minima cannot be two steps apart; immediate gap 1 forces the earlier record to be 7 mod 8, later record 2 mod 3; all longer gaps terminate from 2b. Infinitely many gaps are longer (>=3), but their mod-3 distribution is unknown.
- **DG-005-B:** If a longer-gap later record b is 2 mod 3, its odd inverse z=(2b-1)/3 is a *new exceptional integer outside the given unbounded orbit*, and distinct b have distinct z. This gives |E∩[2,X]|>=R(X)+Q(X). No positive lower bound for Q(X), much less a bound conflicting with o(X), is proved.
- **DG-005-C countermodel:** The abstract numbers b_j=648 floor(10(5/4)^j)+55 satisfy 7 mod 8, 1 mod 3, 55 mod 81, and the spacing / known least-E sieve numerics, yet remain a zero-density set. This is NOT a Collatz orbit; exact bridge realisation is a separate and essential obstruction.
- **DG-005-D:** For k>=2 and r=3^(k-1), N=2^k(2^r+1)/3^k-1, all integers n=N+2^(k+r)h (h>=0) follow k odd and then r even steps, descending at step k+r, with first descent later than k. This exhibits entire E-free progressions with arbitrarily large parameterised first-descent horizons. Each is a finite cylinder certificate, not a uniform theorem covering every n.
- **Open sharpened target:** Determine whether actual integer realisation of endless record transitions forces long-gap targets 2 mod 3 often enough to yield an incompatible E lower bound, or rules out an eventual all-1-mod-3 record path. Proving infinitely many long gaps alone is insufficient. Continue only with a non-circular argument about genuine positive-integer orbits. [DG005](sessions/DG005.md); [DG006 task](NEXT_SESSION_DG006.md).


## DG006: exact short bridges, all-1-mod-3 finite adversary and safe forest (2026-10-15)

- **DG-006-A (proved, conditional):** Successive exceptional suffix-minimum gaps on an unbounded E-orbit cannot equal 2, 4, or 5. Gap 3 has uniquely prescribed finite bridge \(a=27+32h\to b=31+36h\), necessarily \(b\equiv1\bmod3\). Among length-6 patterns the only locally feasible long gaps are \(111010\) with source \(71+256h\), target \(91+324h\equiv1\bmod3\), and \(111100\) with source \(207+256h\), target \(263+324h\equiv2\bmod3\). Both families are *real finite bridges*, not confirmed E endpoints. A general necessary and sufficient finite-bridge test is a parity-cylinder congruence modulo \(2^{d+2}\) plus strict linear intermediate inequalities. No classification at all lengths is claimed.
- **DG-006-B (proved with exact finite models):** A later long-gap target \(b\) is \(1\bmod3\) when the trailing even-run length is odd, \(2\bmod3\) when it is even. The positive seeds \(n_r=12\cdot8^r-5\) support \(r\) consecutive genuine finite \(110\) local record bridges, with every candidate record \(1\bmod3\). They invalidate a uniform finite-prefix ban on all-1-mod-3 schedules, but are *not* genuine infinite exceptional record chains. An eventually-all-gap-3 tail is impossible for a fixed positive seed because iterating \(110\) forces \(8^r\mid(n+5)\) for all \(r\). Therefore an unbounded E-orbit must have infinitely many gap-1 transitions **or** infinitely many gaps at least 6; mixed, varying nonperiodic schedules remain open.
- **DG-006-B, least-element gate:** If \(m=\min E\) has an unbounded orbit, its first long-gap target must be \(1\bmod3\). For a \(2\bmod3\) target \(b<T(m)\), the safe odd ancestor \((2b-1)/3\in E\) lies below \(m\), contradiction. This is conditional on the endpoint being an *actual* exceptional suffix minimum; it does not ban all seeds beginning with the six-step word \(111100\).
- **DG-006-C (proved, conditional):** Each long-gap \(2\bmod3\) record target \(b\) has \(v_3(b+1)\) distinct odd exceptional inverse ancestors \(z_i=2^i(b+1)/3^i-1<a_j\), all outside the original orbit. Chains belonging to distinct record targets are pairwise disjoint by unique first entrance onto that orbit. Hence \(|E\cap[2,X]|\ge R(X)+\sum v_3(b+1)\) over these targets \(b\le X\). The sum can be **zero** under present knowledge; there is no positive density contradiction.
- **Remaining hard obstruction:** Prove that genuine positive-integer exceptional record dynamics must eventually have an incompatible 2-mod-3 branch distribution, or construct further *safe* off-spine inverse roots from 1-mod-3 targets with a count incompatible with Terras–Everett's \(o(X)\) bound. Do not infer such a count from arbitrary inverse edges or abstract numerical candidate records. Bounded E-orbits/nontrivial cycles remain untouched by these conditional unbounded-orbit arguments. Full proof: [DG006](sessions/DG006.md); exact bounded regression: [verify_DG006.py](verification/verify_DG006.py); next focused challenge: [DG007](NEXT_SESSION_DG007.md).

**DG-GAP-01 stays OPEN.** There is no verified all-integer descent theorem, formal proof, or independent originality certificate.


## DG007: exact missing gaps, new 1-mod-3 safe roots, and least-exception sieve (2026-10-15)

- **DG-007-A (proved, conditional):** Genuine unbounded exceptional suffix-minimum record gaps 7, 8, 10, 12 are impossible, in addition to DG006's 2, 4, 5. Exhaustive exact affine/parity-cylinder inequality classification for lengths 3–12 gives feasible counts 1,0,0,2,0,0,7,0,30,0 respectively. Every viable fixed-length word represents a positive finite local bridge, **not** a confirmed E orbit; larger gap lengths and bounded exceptional cycles remain unresolved.
- **DG-007-B (proved, conditional):** If genuine long-gap target b≡4(mod9), the safe 110-predecessor z=(8b-5)/9 lies in E outside the original unbounded orbit when d≥6. Its first spine meeting is at an intermediate point in that record interval, disjoint from other record intervals and DG006's root first meetings. Thus \(|E\cap[2,X]|\ge R(X)+\sum_{\text{long b=2 mod3}}v_3(b+1)+Q_4(X)\), with \(Q_4\) the count of long d≥6 b≡4(mod9) targets. **No lower bound on \(Q_4\)** exists; this does not contradict E density zero. If the first record transition from \(\min E\equiv3\bmod8\) is long, it cannot target 4 mod9.
- **DG-007-C (proved, applies also to hypothetical bounded E):** Eleven-step strict-prefix expanding safe inverse words ban **eight new** odd least-E congruence classes modulo2187: 205,325,919,991,1000,1090,1171,2170. The 335/729 old banned odd classes lift to 1005/2187; exactly 1013/2187 are now banned by the specified strict-prefix words through length 11. This eliminates locations of **min E only**, not whole-E families.
- **DG-007-D (proved realisation theorem / finite-pattern countermodel):** All finite sequences of six individually viable all-1-mod-3 bridge words at gaps 3,6,9 are realised in arbitrarily large positive integers by a single common cylinder for each fixed sequence; all their finite record endpoints have the required strict local properties. 258 lists of one to three words verified. This **does not** show one positive seed survives an infinite mixed schedule.
- **Critical remaining route:** Prove that actual exceptional positive-integer record chains cannot permanently avoid both the 2-mod-3 and 4-mod-9 safe off-spine ancestor classes; or obtain a new whole-E elimination mechanism rather than just excluding more candidate least elements; or prove a global positive-integer realisation obstruction for every remaining infinite nonperiodic schedule. Neither sparse inverse-root counts nor isolated 2-adic parity cylinders close the Terras–Everett almost-all-to-all gap. See [DG007](sessions/DG007.md), [exact checker](verification/verify_DG007.py), and [next DG008](NEXT_SESSION_DG008.md).

**DG-GAP-01 remains OPEN:** no all-integers descent proof, no Lean/Palomar certificate, no independent novelty assessment.
