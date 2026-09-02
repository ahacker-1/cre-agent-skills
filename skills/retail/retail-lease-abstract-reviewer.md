---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Lease Abstract Reviewer

Abstract U.S. retail leases into decision-ready economic, recovery, and control-right summaries, and flag the investor, lender, and rent-roll conflicts that change value.

---

## When to Use This Skill

Use this skill during acquisition diligence, refinancing, or asset review of grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use retail, pad, or single-tenant net lease (STNL) assets, when leases must become an abstract that underwriting, lending, and legal teams can act on. Retail is lease-driven and sales-driven: percentage rent, co-tenancy, exclusives, go-dark, radius, and CAM structure control value, and none of them appear on a rent roll.

In a mixed-use asset, abstract the non-retail space with the pack that matches it: [Office Lease Abstract Reviewer](skills/office/office-lease-abstract-reviewer.md) for office suites and [Industrial Lease Abstract Reviewer](skills/industrial/industrial-lease-abstract-reviewer.md) for warehouse and flex space. Tracking estoppel delivery and review across a whole roster is [Estoppel Tracker](skills/legal/estoppel-tracker.md); this skill abstracts the lease each estoppel is checked against.

This is educational decision support, not legal, tax, investment, accounting, or financing advice. Lease and REA interpretation, and the enforceability of co-tenancy, radius, continuous-operation, liquidated-damages, and guaranty provisions, are state-law specific and require counsel.

---

## What You'll Need to Provide

- Lease, all amendments, and any prior abstract or lease summary
- Rent roll line for the tenant: suite, GLA, in-place rent, recovery method, expiration, option status
- Center type and total GLA, plus the site plan and recorded REA / OEA if the center is multi-parcel
- Side letters, work letters, commencement agreements, guaranties, SNDAs, estoppels, assignments, subleases, and consents
- Tenant sales reports and CAM reconciliation history if available, plus the business question: acquisition diligence, lender review, renewal or backfill decision, co-tenancy exposure, or dispute issue spotting

---

## Mission

Extract every retail lease term that drives cash flow, recovery, rollover, and tenant control, reconcile it against the rent roll and estoppel, and report each conflict with severity and a next step. The output is an abstract someone can underwrite from, not a summary of the lease.

---

## Strategy

### Step 1: Build and Test the Document Stack

List every document reviewed and every document expected but missing: original lease and all amendments; commencement or rent commencement letter; work letter and allowance disbursement records; guaranty and the entity chain from lease signatory to guarantor; estoppels and SNDAs; assignments, subleases, and landlord consents; side letters, co-tenancy waivers, and rent relief agreements; recorded REA / OEA, site plan, sign criteria, and any memorandum of lease.

- An abstract built from a lease without its amendments is incomplete. Say so in the verdict, do not bury it.
- If a signed estoppel disagrees with the lease documents, treat the estoppel as the higher-risk document. Recitals in an estoppel can bind the signer even where they misstate the lease, so a conflict is a diligence exception, not a rounding difference.
- Note whether the premises sit on a fee parcel, a ground-leased pad, or an owned anchor tract. That determines whether the REA, not the lease, governs parking, signage, and use.

### Step 2: Abstract Base Rent, Percentage Rent, and the Sales Definition

Extract: premises, suite, GLA and measurement basis; commencement, rent commencement, expiration, and the trigger for each; the full base rent schedule with every step date in dollars and PSF; free rent, abatement, and any deferral still unwinding; percentage rate, breakpoint type, and the stated breakpoint dollar figure; the gross sales definition with every exclusion and whether e-commerce fulfilled from or returned to the store counts; reporting frequency, records retention, audit window, and audit cost shifting; security deposit or letter of credit and burn-down conditions.

Decision rules:

- Natural breakpoint = annual minimum rent / percentage rate. Recompute it. A stated breakpoint that does not equal that math is artificial and must be labeled artificial, because it does not move with rent steps. Formulas live in [Retail Lease Structures](knowledge/retail-lease-structures.md).
- Watch for exclusions that make reported sales unusable for both percentage rent and any sales-based kick-out test: customer refunds, employee discounts, accommodation sales, coin-operated devices, third-party credit card commissions, inter-store transfers, returns to manufacturers, and sales taxes collected. Retail sales exclusions and reporting risk are detailed in [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md).
- Term screen: issuer disclosures differ, so use both bands and attribute them. [Retail Lease Structures](knowledge/retail-lease-structures.md) carries Brixmor's FY2025 disclosure of anchor original terms of 10 to 20 years against 5 to 10 years for smaller tenants; Regency Centers and Federal Realty disclose space under 10,000 SF at three to seven years, space over 10,000 SF in excess of five years, and retail leases broadly three to ten years with anchors longer (FY2025 Form 10-K filings, February 2026, directional). Read shop terms as roughly three to ten years and anchor terms as roughly ten to twenty. A term far outside its size band is a question, not an error.

### Step 3: Abstract the Recovery Structure

State each of these explicitly: recovery method (pro rata, fixed CAM, capped pass-through, base year, gross, or hybrid by category); denominator (total, leased, or occupied GLA) and whether anchors are in or out; cap coverage and whether it is cumulative or non-cumulative; gross-up to stabilized occupancy; administrative and management fee, fee base, and whether either is charged on taxes, insurance, and utilities; capital pass-through scope, useful life, interest rate, and early-year exclusions; the exclusions list, cost pooling, and audit rights; and who pays roof, structure, HVAC replacement, and parking lot capital.

Decision rules:

- The rent roll's recovery label is not evidence. Classify from the recovery article and the exclusions list.
- Test fees and audit terms against practitioner negotiating ranges: administrative fees often 10-15% of other CAM expenses, third-party management fees often 2.5-4% of gross project revenues, capital commonly excluded for the first 5-7 years of a new development, and audit costs shifted to the landlord at a 3-5% overstatement (Cox, Castle & Nicholson). Ranges to test against, not market rules.
- Denominator convention follows format: malls commonly exclude anchors above a stated size, power and neighborhood centers commonly use a floor-area ratio, and ground-leased parcels commonly use a land-area ratio. A cumulative cap carries unused cap room forward while a non-cumulative cap resets, and modeling the wrong one misstates recovery growth for the whole hold.

### Step 4: Abstract Use, Co-Tenancy, and Operating Covenants

| Clause | Extract | Test |
|---|---|---|
| Permitted use | Scope, trade name, consent standard for use changes | Does it permit the backfill the business plan assumes? |
| Exclusive use | Protected use, carve-outs for existing tenants and anchors, landlord notice covenant, remedies, whether recorded | Overbroad exclusives block leasing; narrow ones fail to protect |
| Prohibited uses | The list, whether remedies are express or damages-only, sunset and recapture | National-brand lists quietly bar service, medical, and entertainment backfill |
| Opening co-tenancy | Named tenants or occupancy threshold, and the consequence if unmet | Expires once satisfied; confirm whether it already did |
| Ongoing co-tenancy | Trigger, cure, remedy, sunset, snap-back, recapture, replacement-tenant standard | Runs the full term; converts one vacancy into center-wide relief |
| Continuous operation | Required hours, permitted closures, remedy on breach | Liquidated damages, recapture, or nothing? |
| Go-dark | Right to cease operating while paying, notice, duration | Test against every other co-tenancy clause at the center |
| Radius | Distance, measuring point, parties bound, carve-outs, remedy | Trade-name-only or single-entity clauses give no real protection |

Screens from practitioner sources, to be tested rather than assumed: key tenants are usually named anchors or mini-majors of roughly 15,000 to 30,000 SF, or occupancy thresholds such as 75% of shop spaces or at least 100,000 SF; ongoing co-tenancy conditions commonly must persist 120 to 365 days before remedies trigger; landlord cure runs at least six months and often a year; abatement is commonly around 50% of rent; and at roughly a year, or on a 12 to 24 month sunset, the tenant elects between terminating and resuming full rent or the landlord recaptures. Exclusive-use remedies seen in practice include reduced rent of 2-4% of gross sales capped at the otherwise payable monthly rent, or 50% of base rent, plus termination on failure to cure, with a rogue tenant provision cutting off the remedy where the violating tenant's own lease already bars the use. Continuous operation is enforced through damages, termination, or recapture far more often than specific performance.

Hand the clause inventory to [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md) and the recovery findings to [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md).

### Step 5: Abstract Termination, Options, and Transfer Rights

Extract: kick-out and early termination (sales threshold, measurement period, whether ramp-up months or partial years count, notice window, interval from election to effective date, fee, and whether unamortized TI and leasing commissions are recaptured); other termination triggers (casualty, condemnation, co-tenancy, exclusive violation, failure to deliver, redevelopment); renewal options (count, length, notice deadline, and rent-setting method: fixed, fixed increase, CPI, or fair market with or without a floor); expansion, contraction, and relocation rights, with notice, seasonal blackouts, frequency limits, size and frontage parameters, cost allocation, and any tenant approval or termination out; ROFR / ROFO on adjacent space, a pad, or the property; signage panel position, size, and exclusivity; parking count, ratio, and reserved areas; assignment and sublease (consent standard, affiliate and change-of-control carve-outs, recapture, profit sharing, and whether use restrictions, exclusives, radius, and operating covenants bind successors and subtenants); and guaranty (guarantor identity, full-term versus limited versus good guy, release trigger, and whether the guarantor sits above the actual lease signatory).

Decision rules:

- Recompute every kick-out test from the lease's own definitions. A threshold measured against a gross sales definition that excludes the tenant's growing channels can hand the tenant an unearned exit.
- An option at fixed or CPI rent is an underwriting input, not a formality. Price it against market rent from [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md).
- A relocation right that no other space in the center can satisfy is not a real right. Check the site plan.
- Never underwrite a franchisor's credit for a franchisee-signed lease absent a parent guaranty. See [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md).

### Step 6: Abstract REA / OEA, Estoppel, SNDA, and Bankruptcy Exposure

For multi-parcel centers, pads, and ground-leased anchors, abstract from the recorded REA / OEA rather than the lease: approving parties and what needs their consent (site plan changes, new buildings, pad splits, parking reconfiguration, roadway and access changes, use changes); the common area regime (self-maintenance by tract, an appointed operator with budget approval and reconciliation, or a hybrid) and audit variance triggers; parking ratios by tract and by use, whether restaurant and theater carry higher ratios, and whether each tract must be self-parked; sign easements covering panel rights on a shared pylon, construction and maintenance access, power, and visibility covenants; and the REA term and expiration alongside use protections that run with the land.

Then reconcile the transaction documents:

- Estoppel: confirm rent, charges, expiration, options, completion of landlord work, absence of defaults, no offsets, and no prepaid rent beyond one month, and list every difference from the abstract.
- SNDA: confirm non-disturbance, attornment, lender cure rights, rent prepayment limits, restrictions on lease modification, and whether the lender's form carves out unfunded tenant allowances so a successor would not owe them.
- Bankruptcy: note that a nonresidential lease is deemed rejected if not assumed or rejected by the earlier of 120 days after the order for relief or plan confirmation, extendable once by 90 days for cause, and that assignment of a shopping center lease requires adequate assurance covering the assignee's financial condition and operating performance, that percentage rent will not decline substantially, compliance with radius, location, use, and exclusivity provisions in this and other leases at the center, and no disruption of tenant mix or balance (11 U.S.C. 365).

### Step 7: Flag Investor, Lender, and Rent-Roll Conflicts

For every finding state the issue, severity, why it matters, and the next step. Flag at minimum: any economic term that does not match the rent roll (GLA, rent, step dates, recovery method, expiration, option status); rights that impair sale, financing, redevelopment, or leasing (ROFR, ROFO, approving-party consent, exclusives, prohibited uses, relocation limits); termination, kick-out, or co-tenancy relief landing inside the loan term or hold period; relief already running and shown as in-place rent; unfunded landlord work or allowance with no reserve; recovery structure that cannot grow with expenses, or fees that invite an audit claim; and a guaranty that does not reach the operating entity.

Route rent and rollover data to [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md) and [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md), lender issues to [Retail Financing Fit](skills/retail/retail-financing-fit.md), and the verdict to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md).

---

## Output Format

```markdown
# Retail Lease Abstract Review
## Tenant / Trade Name:
## Center, Suite, and Tenant Role: grocery anchor | junior anchor | in-line | pad | STNL
## Documents Reviewed / Documents Missing:
## Verdict: CLEAN | NEEDS FOLLOW-UP | HIGH RISK

### Economic Terms
| Item | Finding | Lease Section | Matches Rent Roll? |
|---|---|---|---|
| GLA, measurement basis, term, commencement, expiration | | | |
| Base rent schedule and escalations | | | |
| Percentage rate and breakpoint (natural or artificial) | | | |
| Gross sales definition and exclusions | | | |
| Sales reporting, audit rights, security deposit / LC | | | |

### Recovery Structure
| Item | Finding | Modeling Impact |
|---|---|---|
| Method and denominator | | |
| Anchor treatment, gross-up, cap (cumulative or non-cumulative) | | |
| Admin / management fee and fee base | | |
| Capital pass-through, useful life, exclusions, pooling, audit rights, roof / structure / parking capital | | |

### Use and Control Rights
| Right | Trigger | Remedy / Tenant Position | Investor and Lender Impact |
|---|---|---|---|
| Exclusive use / prohibited uses | | | |
| Opening and ongoing co-tenancy | | | |
| Continuous operation, go-dark, radius | | | |
| Kick-out / early termination | | | |
| Renewal options and option rent | | | |
| Relocation, ROFR / ROFO, signage, parking | | | |
| Assignment, sublease, guaranty | | | |

### REA / OEA, Estoppel, and SNDA
- Approving parties and consent triggers:
- Parking ratio, self-parking obligation, sign easements, REA term:
- Estoppel differences from abstract:
- SNDA status and carve-outs:

### Diligence Issues
| Issue | Severity | Why It Matters | Next Step | Owner |
|---|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Original lease and every amendment are read together, the abstract states which amendment controls each term, and the base rent schedule reconciles to the rent roll dollar for dollar with any GLA difference explained
- The natural breakpoint is recomputed and any artificial breakpoint is labeled artificial
- Recovery method is classified from the recovery article, not from the rent roll label or a "NNN" heading
- Every co-tenancy, exclusive, radius, go-dark, and kick-out clause is cited to a section, with trigger and remedy stated separately
- Options show notice deadlines and the rent-setting method, not just "one 5-year option", and REA obligations are abstracted separately from lease obligations for any pad, ground-leased, or multi-parcel premises
- Estoppel and SNDA differences are listed, unfunded landlord obligations are quantified where known, and missing documents are reflected in the confidence level

---

## Red Flags & Dealbreakers

- Co-tenancy or exclusive-use rent relief already in effect and presented as in-place rent, or a kick-out or termination right inside the loan term or hold period that underwriting does not model, or whose fee does not recapture unamortized TI and leasing commissions
- Recovery modeled as pro rata growth while the lease is fixed CAM, or a cumulative cap modeled as a hard annual ceiling
- Administrative or management fee charged on taxes, insurance, and utilities that pass through at cost, or exclusives and recorded REA prohibited uses that bar the backfill the business plan depends on
- Approving-party consent required for the redevelopment, pad split, or parking reconfiguration in the plan, and nobody has asked for it
- Go-dark right priced without reading every other co-tenancy clause at the center, a dark-but-paying tenant carried as occupied, or a radius clause binding only the trade name with no affiliate or franchisee reach
- Guaranty that releases on surrender or sits below the actual lease signatory, or unfunded landlord work with no reserve and an SNDA that carves it out
- GLA, expiration, or option status that differs from the rent roll or a signed estoppel without explanation, an REA nearing expiration, or a ground-leased pad whose reversion, reset, and leasehold financing terms were never abstracted

---

## When Data is Missing

- If amendments are missing, mark the abstract incomplete in the verdict line and do not report the rent schedule as final
- If the work letter or allowance ledger is missing, do not assume landlord obligations are zero; state the exposure as unquantified
- If the REA is not produced for a multi-parcel center, treat parking, signage, site plan control, and use restrictions as unknown rather than absent
- If the gross sales definition is unclear, do not compute an occupancy cost ratio or a kick-out test from it; report the ambiguity. If GLA conflicts across lease, amendment, rent roll, and estoppel, show every figure and request the measurement support
- If no estoppel or SNDA exists yet, list it as a closing condition with the responsible party; where enforceability rather than language is the question, route to counsel and do not predict outcomes

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Complete lease stack with all amendments, work letter, guaranty, REA where applicable, and a current estoppel; rent, GLA, and expiration reconcile to the rent roll |
| MEDIUM | Core lease and most amendments available, but one of work letter, guaranty, REA, sales reporting, or estoppel is missing or stale, and no economic term is in conflict |
| LOW | Abstract-only review, missing amendments or economic provisions, unresolved rent roll or estoppel conflicts, or an REA that governs the premises and was not produced |

---

## Related Knowledge Bases

- [Retail Lease Structures](knowledge/retail-lease-structures.md)
- [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md)

## Research Basis

- [Retail Lease Abstract Reviewer Research](research/retail/retail-lease-abstract-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
