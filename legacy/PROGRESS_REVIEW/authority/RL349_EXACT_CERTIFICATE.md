# RL349 exact arithmetic certificate

Date: 2026-09-18
Status: CLOSED/FROZEN ARITHMETIC SUPPORT ONLY

This certificate promotes no new Phase-4 exclusion. It records exact arithmetic retained from the
RL349 diagnostic.

## Constants

`a=217976794617`
`ell=137528045312`
`d=a-ell=80448749305`
`n0=20390252058`

Use the inherited exact lower enclosure

`L2=15757912/22733865 < log 2`.

Then

`ell/(12 log 2) < ell/(12 L2)`

and exact reduction gives

`ell/(12 L2) = 32568166831634280/1969739
             = 16534254960.496...`.

Moreover

`(n0-1) - ell/(12 L2)
 = 7595307864868843/1969739
 > 0`.

Therefore

`ell/(12 log 2) < 16534254960.497... < n0-1`.

This is only an arithmetic implication. RL349 did not prove the live mathematical antecedent
`e_k < ell/(12 log 2)` and therefore does not obtain a contradiction from this certificate.

No finite trajectory enumeration is claimed.
