# RL346 scratch frontier

Date: 2026-09-17
Status: NON-AUTHORITATIVE SUPPORTING FRONTIER FROZEN FOR RESUMPTION/FORENSICS

## Invalid `G_72=76` enumeration — do not use as proof

A scratch enumeration of excess-4 final-72 words combined the exact RL344 record-prefix inequality
with endpoint residue lifting and deterministic escape. The run reported, under its own filter:

- 1,141,040 record-compatible words;
- 1,105,989 q=0-band endpoint lifts;
- all tested endpoints descending below `2^71`;
- maximum escape depth 452;
- reported maximizer excess positions `(7,9,20,64)` and endpoint
  `60730717507988140933759`;
- reported digest
  `9e815f02638de8d338e10a5ad35680634a895580b5536216c4fe06f63bd6473a`.

These figures are NOT authoritative because the terminal-60 filter used the wrong positional
orientation. The inherited endpoint-forward convention requires an excess among positions 13..72,
whereas the scratch implementations filtered for an excess among positions 1..60. The class was
not recomputed before CLOSEOUT_LOCK. Preserve the numbers only so the failed run can be diagnosed;
do not reuse its counts/digest/max as a certificate.

## Structural leads that were superseded or left unpromoted

1. A first-23-step source growth envelope exists because each accelerated odd step obeys
   `x'+1 <= (3/2)(x+1)`. It was not needed after the stronger cyclic predecessor-signature
   reduction and was not developed/promoted.
2. RL303/RL304 fixed-96 P/Q commutation was inspected for a cross-era bridge. No exact map from those
   Bellman/cascade states to the live genuine q=0 return interface was proved.
3. The useful organizing observation is now cyclic: a q=0 source is the endpoint of the previous
   complete return, so bounded predecessor data can replace an unbounded current-source prefix.

## Durable research direction

Do not continue total-gap enumeration. The live unbounded object is the deterministic decoder
trajectory between bounded cyclic signatures. The next useful theorem must skip, pump, rank, or
quotient that trajectory uniformly in its length.
