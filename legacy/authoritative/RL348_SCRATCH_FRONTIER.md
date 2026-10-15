# RL348 scratch frontier

Status: FROZEN, NON-AUTHORITATIVE

These are diagnostics for RL349. They are not promoted results and must be rederived against the
committed orientation before use.

## A. Half-cycle bounded contact interface

Authoritative facts:
- `L=ell`;
- matched contact endpoints;
- same decorated phase tag;
- `H=a`;
- positive even endpoint separation `2<=D<=2^36`;
- terminal endpoint-forward gap exactly one;
- endpoint phase tag `1<=c<=a-ell`;
- physical parity words disagree within at most 36 binary phases.

Live scratch suggested combining this bounded mismatch window with the RL345/RL346 predecessor and
successor mixed-adic singleton interfaces. No gap-free CRT rejection was completed.

Do not import the old RL140--RL142 height-one contact exclusion: its exterior-block hypotheses do not
hold automatically in the live `g=2` branch. RL146's height-one carry-order theorem also cannot be
used unless height one is first proved; RL147 records the height-two obstruction.

## B. Post-crossing over-half source-side route

Authoritative geometry now gives:
- all q=0 vertices lie on one strict-late complement interval `[s,e]`;
- `s<=k<=e`;
- universal `R>=23135982580`;
- if `s<=j`, the stronger `R>=61170756170`;
- if `j<s<=k`, putting `t=k-s` gives `t>=23135982580`.

The correct endpoint for the first matched half-cycle in the inverse-oriented long return is the
lower/source endpoint, not the old withdrawn right endpoint.

Live scratch produced candidate source-side inequalities by splitting the long return into an
`ell`-step matched factor and a residual `h=L-ell` segment, including a potential condition of the
form

`e_source/P_source < 1-lambda^(-h/ell)`

and a possible displacement/zero-budget relation. These were not fully frozen against every
orientation and ownership convention and are NOT PROMOTED.

RL349 should rederive them once, then either turn them into a genuine source-defect contradiction or
discard the route immediately.

## C. Sub-row long-return class

The class `75<=L<ell` remains the least geometrically consumed residual.

Use the committed deterministic interface:
- RL346 bounded incoming signatures;
- exact decorated endpoint rank/length decoder;
- exact `(L,H)` inverse-carry uniqueness;
- RL348 terminal law `g_1=1`, `q_(L-1)=1`, `c_end<=a-ell`;
- RL345 23/72 singleton constraints;
- predecessor 2-adic and successor 3-adic acceptance;
- exact q-record/profile, row/wrap, ownership and descent tests.

Do not restart total-gap enumeration or a length-by-length replay.

## D. RL349 stopping discipline

RL349 is explicitly targeted to close Phase 4 in one research session. The intended successful
output is `O_75=empty`, not another sequence of contractions.

A class-elimination theorem, an all-class merge, or a decisive proved architecture barrier is a
meaningful internal checkpoint. A one-unit bound improvement or another local window shrink is not.
