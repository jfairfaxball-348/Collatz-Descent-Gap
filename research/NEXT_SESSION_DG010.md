# DG010 — global least-exception transition obstruction at m divisible by 3 (READY; NOT EXECUTED)

**Execution authority:** The next owner instruction to “run next session” authorises exactly **DG010**, without a separate confirmation gate. DG009 is executed. Do substantial mathematics, not a status-only report, and commit the exact closeout. Prepare but **do not execute DG011**.

## Read first / non-negotiable objective

Read research/THEOREM_TARGET.md, research/sessions/DG009.md, research/sessions/DG008.md, research/PROOF_LEDGER.md, research/OPEN_GAPS.md and research/verification/verify_DG009.py. The only headline goal remains

E = {n>=2 : T^k(n)>=n for every k>=1} = empty,

where T(n)=n/2 when even and T(n)=(3n+1)/2 when odd. Natural-density-zero (Terras–Everett) is not an emptiness proof. Bounded hypothetical exceptional cycles and unbounded exceptional orbits are distinct; finite bridges are neither. An actual first transition from m=min E to b is available only under the *unbounded* hypothesis.

## Exact DG009 state

For u=111011010 and v=111101010, source/target progressions are

u: a=1959+2048h -> b=2791+2916h (37 mod81),
v: a=1327+2048h -> b=1891+2916h (28 mod81), h>=0.

No different strictly prefix-safe inverse word with <=6 odd bits is integral for an entire endpoint progression. Six *deeper* explicit safe roots z<a exist on full parameter subprogressions:

- u, h=1 mod3: w'=1111011010; v, h=2 mod3: 1111101010.
- u, h=5 mod9: 110111011010; v, h=0 mod9: 110111101010.
- u, h=9 mod81: 111101111001010; v, h=40 mod81: 111101111100010.

If b is the first genuine record from min E, all these full progressions are impossible; notably the last pair has a divisible-by-3 source. This is **not** an exclusion for all E or for arbitrary first-gap words.

A genuinely varying infinite 2-adic bridge schedule v u^(J_i+1) v ... with J_1=1, J_(i+1)=2J_i+2 is impossible for a fixed positive seed (expanding repeated-u divisibility), although every finite prefix has arbitrarily large positive starts 0 mod3. Do not infer that every infinite mixed schedule is unrealised.

## One priority: prove or falsify a global obstruction for m=min E with m=0 mod3

Choose ONE mathematically decisive candidate first, then test it adversarially. Prefer a complete first-record theorem applicable **regardless of the record-gap length**, or an alternate argument that also covers bounded cycles. The allowed successes are:

**A.** An actual unconditional theorem ruling out m=0(mod3) as the least element of E, including bounded trajectories. The proof must derive E membership of every proposed smaller witness (not assume it for an arbitrary iterate), and address all possible gaps or avoid record-gap arguments entirely.

**B.** A rigorous theorem that any unbounded E orbit from such an m has some actual record target b with a safe inverse z<m, including proof of a global recurrence or a first-spine-meeting invariant; no finite schedule or 2-adic compactness shortcut.

**C.** A quantified structural growth mechanism forcing a contradiction with the externally known o(X) exceptional-set bound. Give the exact number of distinct certified E elements <=X, collision proof, and growth dependence on X.

If none succeeds, deliver a mathematically specific new theorem or constructive adversary sharply identifying the failure of the chosen mechanism, beyond DG009's six certificate progressions.

## Mandatory attacks and stress tests

1. **First-record generalisation.** Derive exact affine source/target conditions for feasible first gaps 3,6,9,11,14,17 and *unbounded* gap lengths. Do not extrapolate the list up to 18 to a global cap. Take m=0(mod3) seriously: no shrinking inverse directly of m exists. Examine forced residues of b and whether b∈E yields an actual smaller z<m via strict-safe inverse words, including words with 7+ odd steps.
2. **3-adic refinement, not illicit projection.** In u/v, classify the h progressions at each true modulus 3^r where a certified alternative inverse z<a exists. Test coverage within h=0(mod3) for u and h=1(mod3) for v, the 3-divisible source cases. New residue classes must be certified for every parameter k>=0 and have a positive odd root with an actual parity word. When a branch has s>=7 odd bits, do NOT count an entire modulo81 target class.
3. **Global cross-gap arithmetic.** Derive restrictions across varying feasible gaps on one fixed positive n, not just repetitions of u or v. A genuine unbounded record orbit is allowed arbitrary large and non-alphabet gaps. If a proposed universal recurrence depends on a finite alphabet or uniformly bounded gaps, state that hypothesis, then attempt to prove or kill it independently.
4. **Adversarial models.** Falsify alleged all-gap forcing against true positive finite mixed schedules starting 0(mod3), and against infinite 2-adic but non-positive-realised paths. Test attempts to forbid bounded exceptional cycles: first-unbounded-record arguments do NOT apply to cycles. Avoid enumerations presented as an infinite proof.
5. **Collision and density accounting.** For any alternative root z below some record source, establish whether its first meeting with the *actual* orbit occurs in the associated gap; otherwise do not include it in a disjoint-root count. State whether a proved family gives only O(log X), polylogarithmic, unspecified, or at least cX certified roots.

## Deliverables and closeout

Write research/sessions/DG010.md with exact hypotheses, complete analytic arguments, explicit examples/counterexamples and status of Success A/B/C. Add and **run** a small exact Python verifier if it materially helps; explicitly name what was tested and do not claim GitHub Actions unless actually run. Update research/PROOF_LEDGER.md, research/OPEN_GAPS.md and README.md only with supported changes. Prepare the **full** research/NEXT_SESSION_DG011.md, mark it READY but NOT EXECUTED, and do not execute it.

Commit results to GitHub and provide verified file and commit links plus the full next-session prompt in the closeout. No automatic extra session, artificial audit, unsupported novelty claim, Lean/Palomar claim or claim E=empty without a complete proof.
