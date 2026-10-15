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
