# Retail Lease Structures

Last updated: 2026-09-01

Scope: U.S. retail leases, REAs, and recovery provisions for grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use retail, pad, and single-tenant net lease (STNL) assets, used for acquisition diligence, refinancing, and asset review. This is an educational issue-spotting reference, not legal, tax, accounting, or financing advice. Lease and REA interpretation, and the enforceability of co-tenancy, radius, continuous-operation, and liquidated-damages provisions, are state-law specific. Confirm with counsel and confirm time-sensitive market conditions locally.

---

## Current Context

- Anchors and small shops are different lease animals. Brixmor's FY2025 Form 10-K (filed February 2026) states anchor tenants generally have original terms of 10 to 20 years while smaller tenants typically run 5 to 10 years, with contractual base rent increases over original and renewal terms.
- Fixed CAM is now the mall norm and appears in open-air portfolios too. Simon's FY2025 Form 10-K states that for substantially all U.S. mall leases it receives a fixed payment for the CAM component, recognized straight-line under ASC 842. Kimco's FY2025 Form 10-K says certain of its leases provide for a fixed-rate reimbursement of taxes, insurance, utilities, and CAM.
- Percentage rent is format-dependent, and sales reporting is a live risk. Brixmor recognized $9.6 million of percentage rent in FY2025 against $1,369.5 million of rental income, roughly 0.7%; Simon discloses overage rent as income that directly depends on tenant reported sales, and warns that omnichannel activity may cause tenants to underreport sales through curbside pickup, store-fulfilled online orders, and online returns processed in store.
- California moved on co-tenancy enforceability. In JJD-HOV Elk Grove, LLC v. Jo-Ann Stores, LLC (S275843), the Supreme Court of California affirmed the judgment in full on 2024-12-19, treating a negotiated substitute-rent co-tenancy provision as valid alternative performance rather than a penalty. That holding is California only.

---

## Retail Lease Forms

| Structure | Who Pays Operating Costs | Retail Use Case | Main Diligence Issue |
|---|---|---|---|
| Triple net (NNN) | Tenant pays proportionate share of operating expenses, taxes, and insurance | Open-air, power, strip, pad, most in-line retail | Whether roof, structure, and capital replacements are landlord or tenant; caps and exclusions that break the "net" label |
| Absolute net / bond | Tenant pays everything including roof, structure, and casualty risk | STNL and many pad deals | Whether the lease is truly absolute or has landlord carve-outs; residual and rollover risk at expiry |
| Fixed CAM | Tenant pays a stated dollar amount, often with a fixed annual bump, instead of a pro rata share | Mall in-line; increasingly small shop in open-air | Landlord keeps expense inflation risk; recovery ratio decays if costs outrun the bump |
| Modified gross / base year | Landlord absorbs a base level; tenant pays increases | Mixed-use retail, some urban street retail, office-adjacent retail | Base year integrity, gross-up, controllable caps |
| Gross | Landlord pays operating costs from base rent | Small urban retail, temporary and specialty leasing | Carve-outs that make it not gross: utilities, trash, merchant association dues |
| Ground lease (landlord as fee owner) | Tenant owns and pays for everything on the pad | Outparcels, pads, ground-leased anchors | Reversion, leasehold financeability, rent resets, no recovery participation |

The label does not control. Read the recovery article, the exclusions list, and the capital provisions before classifying any retail lease.

---

## Base Rent and Percentage Rent

| Item | What to Extract | Why It Matters |
|---|---|---|
| Base rent schedule | Rent per SF, step dates, mid-term bumps, option-period rent | Reconciles the rent roll and drives the percentage rent breakpoint |
| Percentage rate | Rate applied to gross sales above the breakpoint | Drives overage rent; no defensible market table by category, so read the lease |
| Breakpoint type | Natural vs artificial, and whether stated in dollars | Changes when overage rent starts and whether it moves with rent steps |
| Gross sales definition | Included channels and stated exclusions | Determines whether omnichannel sales count at all |
| Measurement period | Lease year, calendar year, monthly with annual true-up | Seasonal tenants can pay or avoid overage purely on period choice |
| Reporting and audit | Report frequency, records retention, audit window, cost shifting | The only enforcement mechanism landlords actually have |

Formulas:

```text
Natural Breakpoint = Annual Minimum Rent / Percentage Rate
Percentage Rent Due = (Gross Sales - Breakpoint) x Percentage Rate
```

Holland & Knight's worked example: $140,000 annual rent at 7% gives a $2,000,000 natural breakpoint. An artificial breakpoint is any negotiated figure set independently of that math, usually to trade minimum rent against overage. Common gross sales exclusions include customer refunds, employee discounts, accommodation sales, coin-operated devices, third-party credit card commissions, inter-store transfers, returns to manufacturers, and sales taxes collected. For deal-level rent and NOI mechanics use [Underwriting Calculations](knowledge/underwriting-calc.md) rather than rebuilding them here.

---

## CAM, Tax, and Insurance Recovery

Abstract every one of these before modeling recoveries:

- Recovery method: pro rata share, fixed CAM, capped pass-through, or a hybrid by expense category.
- Cap structure: whether a cap exists, whether it is cumulative or non-cumulative, and what it applies to. Caps are normally negotiated on controllable expenses only, with taxes, insurance, security, and utilities uncapped.
- The cumulative distinction is real money. At a 5% cap, if year 2 expenses rise 3%, a cumulative cap lets the landlord bill up to 7% in year 3 by carrying the unused 2%; a non-cumulative cap resets and holds year 3 to 5% (Lowndes).
- Denominator: total GLA, leased GLA, or occupied GLA, and whether anchors are in or out. Convention varies by format - malls commonly exclude anchors, power centers commonly use gross square footage ratios, ground-leased parcels commonly use land area (Cox Castle).
- Anchor contributions and gross-up: whether anchors pay standard CAM, a negotiated fixed contribution, or self-maintain their tract, and whether variable expenses are grossed up to a stabilized occupancy so vacancy cost is not shifted onto occupied tenants.
- Administrative and management fees: whether both are charged, the fee base, and whether the fee applies to uncontrollable pass-throughs. Cox Castle describes administrative fees as often 10-15% of other CAM expenses; treat that as a negotiating range, not a market rule.
- Capital treatment and exclusions: which capital items are recoverable, over what useful life and at what interest rate, whether early lease years are excluded, and what the exclusion list covers - typically ground rent, debt service, casualty repairs, tenant improvements, leasing commissions, and above-market costs.
- Cost pooling: whether the landlord may allocate an expense only among the tenants it benefits.
- Audit rights: frequency, window, CPA requirement, and the cost-shifting threshold, commonly a 3% to 5% overstatement (Cox Castle; ICSC REA materials use the same 3% or 5% convention at the operator level).

Leased occupancy and billed occupancy are different numbers with different revenue. Brixmor reported FY2025 total leased occupancy of 95.1% with a 350 basis point spread to billed occupancy, and 92.2% leased for spaces under 10,000 square feet. Never reconcile recoveries off a leased-occupancy denominator without checking which tenants are actually paying.

---

## Tenant Control Rights

| Right | What to Extract | Investor / Lender Impact |
|---|---|---|
| Opening co-tenancy | Named anchors or occupancy threshold required before the tenant must open or pay full rent | Delays rent commencement; can strand a lease-up |
| Ongoing co-tenancy | Trigger, cure period, remedy (abatement, substitute rent, delayed opening, termination), sunset or snap-back | Converts one anchor vacancy into portfolio-wide rent relief |
| Exclusive use and prohibited uses | Scope of the protected use, center-wide bans, carve-outs, remedies, whether the restriction also lives in a recorded REA | Blocks leasing of vacant space to the obvious replacement |
| Continuous operation | Required hours, permitted closures, remedy on breach | Dark space kills traffic and trips other leases |
| Go-dark right | Whether the tenant may cease operating while paying rent, and for how long | Must be tested against every other co-tenancy clause at the center |
| Radius restriction | Distance, measuring point, parties bound, carve-outs, remedy | Protects the sales base behind percentage rent and kick-out tests |
| Kick-out and early termination | Sales threshold, measurement period, one-time or recurring, notice window, fee, payback of free rent and allowances | Hidden rollover inside a loan term; check whether unamortized TI and commissions are recaptured |
| Relocation | Landlord's right to move the tenant, cost allocation, size and visibility parameters | Redevelopment flexibility, or the lack of it |
| ROFR / ROFO | Trigger, scope (space or the property), timing | Can chill a sale or a pad split |
| Signage and pylon | Panel position, size, whether rights are exclusive or shared | Backfill value and REA sign-band conflicts |

Co-tenancy conventions from practitioner sources: key tenants are usually named anchors or mini-majors of roughly 15,000 to 30,000 square feet; landlords negotiate for a cure period, a replacement-tenant standard, proof of a sales decline, remedies as sole relief, and a forced election between reduced rent and termination; termination typically becomes available after 6 to 12 months or more of continued violation, with full rent restored or landlord recapture once the violation runs past about a year (Cox Castle). Specific occupancy thresholds, alternate-rent levels, and radius mileage are pure negotiation outputs with no defensible default - read them, do not assume them.

Continuous operation is enforceable in many jurisdictions when clearly drafted, but courts disfavor specific performance and prefer damages, recapture, or termination. Liquidated damages are generally upheld where actual damages are hard to calculate and the formula is a reasonable estimate; the ICSC 2025 materials cite El Centro Mall, LLC v. Payless ShoeSource, Inc., 174 Cal. App. 4th 58 (2009), which upheld a per-day charge of ten cents per square foot or $100, whichever is greater. Radius restrictions must protect a legitimate business interest and not be overly broad in location, duration, or scope; the ICSC materials state that a radius covering more than a few miles is very likely unenforceable, and that the clause should bind the tenant plus affiliates and owners, describe the business type rather than only the trade name, and state the measuring point.

---

## REA / OEA, Pads, and Ground-Leased Anchors

- An REA (also OEA, ECR, COREA) governs a multi-parcel unified development: easements for access, parking, utilities, and signage, plus a governing regime for construction, maintenance standards, architectural theme, prohibited and exclusive uses, site-plan control, and signage rights.
- Approving-party rights usually sit with the master developer plus the top few anchor parcel owners. Redevelopment, pad splits, parking reconfiguration, and use changes may need their consent even when the lease is silent.
- REA common-area maintenance is handled one of three ways: each owner maintains its own tract, the owners appoint an operator for the whole center, or a hybrid. Where there is an operator, expect an annual budget with owner approval rights, an annual reconciliation, and audit rights with a 3% or 5% variance trigger. Parking ratios are also set here, often higher for restaurant and theater uses and separate for office or residential in mixed-use, with an express choice about whether each tract must be self-parked.
- Terms run long - the ICSC materials describe easements and REA terms in the 50 to 80 year range, and note that early enclosed-mall REAs are now nearing expiration, which is a live diligence item rather than a footnote.
- Ground-leased parcels are common. Kimco's FY2025 Form 10-K reports 36 consolidated shopping centers subject to long-term ground leases where a third party owns the land, with the landlord-tenant generally bearing all building and improvement costs and the land plus improvements reverting at expiration absent extension. Simon's property schedule lists many centers held in fee and ground lease with stated expiration years. For pads and ground-leased anchors, abstract reversion, leasehold financeability, lender protections, rent resets, and whether the parcel participates in CAM at all.

---

## Assignment, Sublease, Estoppel, and SNDA

- Assignment and sublease: consent standard, affiliate and change-of-control carve-outs, recapture, profit sharing, and whether the transferee must meet financial and operational thresholds. Operating covenants, exclusives, and go-dark limits should expressly bind successors, assigns, and subtenants; if they do not, a transfer can quietly extinguish the landlord's leverage.
- Estoppel certificates confirm that the named tenant is the tenant, the lease is in full force and effect, no default has occurred, no advance rent has been paid, there is no offset claim, and no bankruptcy is pending. Practice is to obtain them at or just before closing, generally dated no more than about 30 days in advance.
- SNDAs are three-party agreements among lender, landlord, and tenant covering subordination, attornment to a foreclosure successor, and non-disturbance, often with lender cure rights, rent-prepayment limits, and restrictions on lease modification. A refused SNDA or a stale estoppel is a financing and closing problem, not a punch-list item. Reconcile every estoppel against the abstract - estoppels routinely surface co-tenancy claims, disputed CAM reconciliations, unfunded landlord work, and side letters that never reached the data room.

---

## Red Flags

- Rent roll shows a clean pro rata recovery while the leases are fixed CAM, so modeled recovery growth does not exist.
- Anchors sit outside the recovery pool and the small-shop denominator silently absorbs their share.
- A cumulative cap is modeled as a hard annual ceiling, understating recovery, or an uncapped pass-through is assumed where a cap exists, overstating it.
- Administrative or management fee is charged on taxes, insurance, and utilities that pass through at cost, inviting an audit claim.
- Percentage rent is underwritten from historical sales while the gross sales definition excludes the tenant's fastest-growing channels, or reported sales fall while foot traffic holds - usually omnichannel reporting leakage, and enough to hand a tenant an unearned kick-out.
- A go-dark consent is priced without reading every other co-tenancy clause at the center.
- Co-tenancy relief with no landlord cure period, no sales-decline proof requirement, and no snap-back or recapture at about a year - or reduced and substitute rent already running and shown as in-place rent.
- Recorded REA exclusives or prohibited uses that bar the backfill tenant the business plan depends on, an REA approaching term expiration, or a redevelopment plan that needs an approving party's consent nobody has asked for.
- Radius clause drafted only against the trade name or the single-purpose tenant entity, with no affiliate reach.
- Kick-out exercise price that does not recapture unamortized TI and leasing commissions, or missing or stale estoppels and an anchor that will not deliver an SNDA.
- Ground-leased anchor or pad whose reversion, reset, or leasehold financing terms were never abstracted.

---

## Related Research

- [Retail Lease Structures Research](research/retail/retail-lease-structures-research.md)
