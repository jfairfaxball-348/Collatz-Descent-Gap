# RL346 closeout verification

Date: 2026-09-17
Status: CLOSEOUT CHECKS GREEN FOR PROMOTED ANALYTIC CONTENT

Incoming `main` remained
`11492738847ba59d0f32dcbb78eda40f2c0ad7bf`
through the research session before closeout mutation.

The following exact arithmetic was independently recomputed during closeout:

- `gcd(217976794617,137528045312)=1`;
- `72a = 114ell + 16132046856`;
- `floor(48a/ell)=76`;
- `ceil(74a/ell)=118`;
- q=0 band width
  `73196680484548220289024 < 2^76 = 75557863725914323419136`;
- `2ell=275056090624`.

The inverse-carry decoder proof was checked algebraically from

`C_j=2^(g_j)C_(j-1)+3^(j-1)`:

`C_j` is odd for every `j>=1`, hence for `j>=2`
`g_j=v2(C_j-3^(j-1))`, with exact recursive recovery of `C_(j-1)` and final recovery of `g_1`
from the fixed total gap.

No RL346 finite numerical search is certified. In particular the attempted `G_72=76` scratch run
is explicitly excluded from the promoted proof state because of the terminal-60 orientation error.

The inherited RL345 exceptional `G_72=73,74,75` certificate and red team remain the only
load-bearing finite endpoint search used by RL346.
