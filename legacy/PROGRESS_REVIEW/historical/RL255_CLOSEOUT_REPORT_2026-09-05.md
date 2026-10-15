# RL255 closeout report — high-beta capacity and parity frontier

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

RL255 adds a genuine Branch-C capacity theorem:

`beta(P)+2 <= floor((a-3 beta(P)+1)^2/4)`.

It comes from isolated `-1` roots, cyclic gap at least three, and the exact 1-Lipschitz tent capacity between successive negative roots.

Combined with the RL254 parity floors, zero budget, exact resonance, and determinant selector, this contracts the uniform first arithmetic frontier to the unique halving selector

`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`.

Therefore every retained Branch-C object has `a>=1100`, `z>=406`, `ell>=694`. The resonance corridor sharpens to `a/ell<=233/147`, hence `H/a<=3/233`.

In the non-halving branch, the sharper corridor allows all 38 useful 38-windows to be used. Their disjoint segments force `beta(P)>=356`. A new physical complement-packing argument then gives `a-36H>=1068`, pushing the first non-halving arithmetic selector to

`(1986,1253,733,1352,853,25,17)`.

At the uniform first halving frontier, `K=7`, `t=2`, `260<=beta(P)<=354`, and `31<=k<=150`.

Gate A/B remain open. Radius 4 is not invoked. Radius 5 remains inactive. No global cycle exclusion is claimed.

RL256 is prepared to attack the exact first halving frontier rather than re-run generic high-beta bounds.

Knowledge catalogues: stale/deferred.
