# The descent-exception problem (ACTIVE)

Reopened 2026-10-15. **Only research goal:** turn the Terras–Everett almost-everywhere finite stopping-time theorem into universal descent, without changing the problem.

## Exact formulation

Use the shortened Collatz map on positive integers:
\[
T(n)=\begin{cases}n/2 & n\text{ even},\\(3n+1)/2 & n\text{ odd}.\end{cases}
\]
For \(n\ge 2\), define its finite stopping time \(\sigma(n)=\min\{k\ge1:T^k(n)<n\}\), or \(+\infty\) if no such k exists. The exceptional set is
\[
E=\{n\ge2:\sigma(n)=+\infty\}
 =\{n\ge2:\forall k\ge1,\ T^k(n)\ge n\}.
\]
Terras (1976) and Everett (1977) establish \(\lim_{x\to\infty}|E\cap[1,x]|/x=0\). **The open target is E=empty.**

Universal descent is equivalent to the Collatz conjecture: by strong induction, any n>1 reaching some smaller positive value reaches 1; conversely reaching 1 descends below n. The n=1 case is excluded deliberately.

## Boundaries

Tao's stronger 'almost bounded' result concerns almost every starting value **in logarithmic density**, not universal descent; it is optional background, not a substitute proof. Density zero by itself cannot imply an empty set.

A successful intermediate theorem must state its scope (all n, one residue class, finite horizon, conditional, or density-only) and explain its logical effect on E. Avoid cycle-only goals, new Collatz variants, enormous brute-force records, or work on other conjectures.

## Non-negotiable test

At each proposed upgrade ask: does the argument rule out an individual exceptional positive integer, rather than merely make exceptional integers rarer? Can a sparse infinite set evade the new argument? Are we accidentally treating an integer-free rational/2-adic parity object as a positive integer orbit?
