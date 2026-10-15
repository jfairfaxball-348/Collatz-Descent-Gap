# RL346 correction and demotion ledger

Date: 2026-09-17

No inherited authoritative theorem is demoted or corrected.

## RL346 scratch correction — attempted `G_72=76` enumeration

During live RL346 exploration, an attempted exact enumeration of the first unresolved total-gap class
`G_72=76` used the wrong orientation for the inherited terminal-60 filter.

The inherited RL345 convention is endpoint-forward on the 72-gap suffix. The terminal-60 theorem
requires at least one excess gap unit among positions 13..72 (1-based), i.e. not all excess confined
to positions 1..12. The scratch implementations instead required an excess among positions 1..60.

Therefore the scratch counts, digest and escape maximum produced by that run are NOT a certificate
for the complete `G_72=76` class. They are frozen only as forensic scratch and must not be cited as
proof that `G_72=76` is eliminated.

A live user-facing checkpoint briefly described that class as certified before the orientation issue
was fully reconciled. This closeout explicitly corrects that description. Nothing from the faulty
enumeration was committed or promoted, and RL345 authority is unaffected.

RL346's promoted terminal-cone theorem uses only:

- the analytic RL344 record identity;
- the inherited terminal-60 theorem;
- RL345's independently verified `G_72=73,74,75` certificate;
- the analytic modulus-width argument for fixed words with `G_72>=76`.

It does not use any `G_72=76` escape enumeration.

## Other non-promotions

1. A source-side 23-step growth-envelope observation was not developed into a theorem and is not
   needed after the cyclic predecessor-signature reduction.
2. The older RL303/RL304 P/Q commutation algebra was inspected as a possible cross-era shortcut,
   but no theorem bridges those Bellman/cascade states to the live RL346 genuine q=0 return
   interface. No P/Q consequence is promoted here.
3. RL346 does not claim that row/wrap decoration automatically chooses one of the at-most-two
   length representatives. Row identity/contact/wrap remain explicit accept/reject conditions.
4. No deterministic skip/pumping/ranking theorem for the full middle decoder was proved. This is the
   live successor obligation.

Phase 5 remains scratch-only and was not resumed.
