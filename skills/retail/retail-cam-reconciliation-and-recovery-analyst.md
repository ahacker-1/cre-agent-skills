---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail CAM Reconciliation and Recovery Analyst

Rebuild a U.S. retail center's recoverable expense pool lease by lease, test prior CAM reconciliations, and reconcile recovery income to underwriting.

---

## When to Use This Skill

Use this skill during acquisition diligence, refinancing, annual reconciliation season, or asset review when recovery income needs to be rebuilt from the leases instead of trended from the operating statement, or when a reconciliation is late, unsupported, or disputed. This is educational decision support for U.S. retail assets, not legal, tax, investment, accounting, or financing advice. A billing error, a cap interpretation, or an audit claim is a contract question that belongs with counsel and with the property's lease administration record before it is asserted to a tenant.

---

## What You'll Need to Provide

- Rent roll with GLA by suite, occupancy dates, and recovery method by tenant; leases, amendments, side letters, and any anchor supplemental agreements
- Recorded REA / OEA / ECR and any operator budget, reconciliation, and audit correspondence
- Operating statements (T-12 and two prior calendar years) at the general ledger account level
- Prior CAM, tax, and insurance reconciliation statements as delivered to tenants, with backup
- Current year budget, monthly estimated billings, and the aged receivable for recovery charges
- Capital ledger with placed-in-service dates, useful lives, and amortization already inside CAM; property management agreement showing the fee base and rate
- The underwriting model's recovery line, occupancy assumption, and expense pool
- Business question: acquisition underwriting, lender sizing, reconciliation defense, audit response, or recapture

---

## Mission

Determine how much of the property's operating cost the leases actually permit the landlord to bill, how much was billed, where the difference came from, and whether the underwritten recovery line survives that test.

---

## Strategy

### Step 1: Build the Document Stack and Classify Every Lease by Recovery Method

Inventory what was reviewed, name what is missing, then classify each tenant into exactly one bucket, because the buckets do not reconcile the same way:

- Pro rata net (tenant pays a share of actual costs)
- Fixed CAM or fixed-rate reimbursement (stated dollar amount, often with an annual bump; no reconciliation exists for this tenant)
- Capped pass-through (pro rata subject to a cap)
- Base-year or expense-stop (tenant pays increases over a floor), or gross (no recovery; check carve-outs such as trash, metered utilities, or marketing fees)
- Anchor with a negotiated contribution, self-maintenance obligation, or approved-budget right
- Ground-leased pad or outparcel, which may participate on land area or not at all

Fixed CAM is not an exception any more. Simon's FY2025 Form 10-K states that for substantially all U.S. mall leases it receives a fixed CAM payment recognized straight-line, and Kimco's FY2025 Form 10-K states certain of its leases provide a fixed-rate reimbursement of taxes, insurance, utilities and CAM. Count the fixed-CAM GLA first. Pull recovery method, denominator language, caps, exclusions, fee language, capital treatment, audit rights, and reconciliation deadlines from the [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md) output where one exists, and the GLA and tenant detail from [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md).

### Step 2: Build the Recoverable Expense Pool from the General Ledger Up

Start from the operating statement and subtract to the lease-permitted pool. Do not start from a prior reconciliation, which is the thing being tested. Test each account against the lease exclusion list: commonly excluded are ground rent, debt service, casualty repair costs covered by insurance, tenant improvements, leasing commissions and lease-related legal fees, costs of services not available to the tenant, and above-fair-market-value costs paid to landlord affiliates (Cox, Castle & Nicholson). Commonly included despite the "common area" label are roof work, common utility systems, and exterior painting. Then resolve the items that vary by document:

- Capital: which items are recoverable, the amortization period, the interest rate, and whether an initial-years exclusion applies. Cox Castle describes capital repairs or replacements often excluded during the initial five to seven years in new development or new acquisition contexts, then amortized over useful life with interest.
- Cost pools: a food court, patio, enclosed-mall, or building-specific pool means the property has more than one denominator. Split them now. REA-level and lease-level pools are different instruments with different exclusion lists: The ICSC 2018 U.S. Shopping Center Law Conference REA materials show a model REA CAM definition excluding management fees, overhead, legal and accounting services, and capital expenditures outright.

Produce the pool three ways: gross recoverable expenses, net pool after anchor and fixed-CAM contributions are backed out, and the non-recoverable residual the landlord eats.

### Step 3: Set the Denominator and Compute Tenant Shares

The denominator is a lease term, not a rent-roll field. Cox Castle documents three conventions:

| Format | Customary Denominator | Watch For |
|---|---|---|
| Regional / super-regional mall | Store floor area occupied and open for business, excluding anchors above a stated size, with the anchor contribution first backed out of the pool | Negotiated minimum-percentage floor in the denominator |
| Power / neighborhood / community | Tenant floor area over floor area of other buildings in the center | Minimum denominator tied to the approved site plan so tenants do not subsidize unbuilt outparcels |
| Ground lease / pad | Land area of the leased premises over total land area of the center | Restaurant and drive-thru pads carrying more parking area than in-line use |

Then choose the occupancy basis and defend it. Leased occupancy over-collects on paper: Brixmor's FY2025 Form 10-K reports portfolio percent billed of 91.6% against percent leased of 95.1% at December 31, 2025, a 350 basis point spread concentrated in smaller units, and Kite Realty's FY2025 Form 10-K reports same-property leased occupancy of 95.0% against economic occupancy of 91.7% on the same date. Use billed or economic occupancy; where the lease sets a minimum denominator, that floor controls and the landlord absorbs the rest. Retail rarely uses the office-style gross-up of variable expenses to a stabilized occupancy, and the minimum-denominator floor is the retail equivalent. Where a mixed-use or urban retail lease is written on a base-year or modified gross form, test base-year integrity and gross-up together, because an ungrossed base year set in a low-occupancy year permanently overstates every future pass-through; the office-form mechanics for base year, stop, gross-up, and controllable caps are abstracted in [Office Lease Abstract Reviewer](skills/office/office-lease-abstract-reviewer.md).

### Step 4: Apply Caps, Fixed Contributions, and Fee Recoverability

For each capped lease extract five things: the cap rate, the base it applies to, cumulative or non-cumulative, whether it compounds, and which categories are controllable. Caps are normally negotiated on controllable expenses only, with real property taxes, insurance, security, and utilities excluded at a minimum (Cox Castle). The cumulative distinction is the single largest modeling error in this work. Lowndes gives the arithmetic at a 5% cap: expenses rising 3% in year 2 leave 2% of unused capacity, so a cumulative cap permits billing up to 7% in year 3 while a non-cumulative cap holds at 5%.

```text
Cumulative Cap Ceiling (year n)     = Prior Billable Base x (1 + cap) + Unused Cap Carryforward
Non-Cumulative Cap Ceiling (year n) = Prior Billable Base x (1 + cap)
```

For fees, separate the charges and check the base of each. Cox Castle reports an administrative fee of 10-15% of other CAM expenses, often cut from 15% to 10% in anchor deals and calculated exclusive of real property taxes and insurance, against a third-party management fee of 2.5-4% of gross project revenues; Macerich's FY2025 Form 10-K discloses management company fees generally ranging from 1.5% to 4.0% of gross monthly rental revenue; and the ICSC REA materials describe an operator administrative fee of 4% to 7% of the annual CAM budget where management fees and overhead are excluded from that budget. These are negotiating ranges from three vantage points, not market rules, and the recurring audit exposure is an administrative fee charged on taxes, insurance, and utilities that pass through at cost.

For anchors, confirm whether the contribution is pro rata, a negotiated fixed amount, a self-maintenance obligation on its own tract, or subject to an approved-budget right. The ICSC materials note enclosed-mall anchors commonly pay pro rata on exterior common area and a fixed amount on interior mall maintenance set in a supplemental agreement between developer and anchor, which will not be in the REA and is often not in the data room.

### Step 5: Test the Prior Reconciliations

Rebuild the last two delivered reconciliations rather than reading them, then classify every variance as under-billing (recoverable and not billed), over-billing (billed and not recoverable), or timing. For each year:

- Confirm delivery and timing against the lease or REA deadline. The ICSC materials describe an operator reconciliation delivered within 90 or 120 days after year end.
- Tie the reconciliation pool to the audited or reviewed operating statement account by account, identify every reclassification, and recompute two or three representative tenants in each bucket, including one anchor, one capped shop, one fixed-CAM tenant, and one pad.
- Compare estimated monthly billings to the final reconciled amount and confirm the true-up direction. Simon's FY2025 accounting policy states differences between estimated recoveries and final billed amounts are recognized in the subsequent year, so a missing true-up appears as a stale receivable or an unrecorded credit.
- Check whether tenant credits were actually issued, whether recovery receivables over 90 days are collectible or disputed, and whether any audit demand, finding, or settlement met the cost-shifting threshold. Cox Castle reports a tenant reimbursement threshold typically ranging from 3-5% overstatement; the ICSC REA materials use 3% or 5% at the owner-operator level.

### Step 6: Compute the Recovery Ratio, Size Leakage, and Reconcile to Underwriting

Use the definition Phillips Edison publishes in its FY2025 Form 10-K: recovery rate is total recovery income divided by total recoverable expenses for the period.

```text
Recovery Ratio        = Total Recovery Income / Total Recoverable Expenses
Recovery Leakage ($)  = Recoverable Expenses in Pool - Recovery Income Billed
Value Impact ($)      = Sustainable Annual Leakage Recovered / Exit Cap Rate
```

Always state the denominator. Excluding the management fee at Rock River Plaza in the Wells Fargo Commercial Mortgage Trust 2026-5C10 prospectus gives a roughly 83% underwritten recovery ratio; including it gives roughly 70%. Directional, dated, format-specific reference points:

| Reference | Recovery Ratio | Basis |
|---|---|---|
| Grocery-anchored / open-air portfolio | ~86% | Regency Centers FY2025 pro-rata same-property recoveries of $404.3M over operating and maintenance of $265.6M plus real estate taxes of $205.7M |
| Anchor-heavy center (Walmart and Lowe's, 389,330 SF) | ~82-83% | Rock River Plaza, WFCM 2026-5C10: 2025 actual recoveries $452,376 and UW $531,720 against taxes, insurance, and other operating expenses |
| Urban street retail with a modified gross anchor | ~77% | Astor Place Retail, WFCM 2026-5C10: UW recoveries $1,368,446 against UW taxes, insurance, and other operating expenses of $1,775,605 |

Anchor-heavy centers legitimately recover less; a stabilized open-air center materially below the mid-80s needs a structural explanation such as caps, exclusions, gross leases, anchor fixed-CAM deals, or vacancy leakage. Then put the rebuilt pool next to the model. Lender underwriting states recoveries as one line inside a fixed format: the WFCM 2026-5C10 prospectus shows Base Rent, Grossed Up Vacant Space, Gross Potential Rent, Total Recoveries, then Vacancy and Credit Loss. Test three seams. First, does the underwritten recovery line exceed trailing actual recoveries, and what lease-level change supports it? At Rock River Plaza the underwriter carried $531,720 against 2025 actuals of $452,376 while also cutting to 95.0% economic occupancy from 100.0% physical. Second, is vacancy counted twice, once in the recovery denominator and again in the vacancy and credit loss deduction? Third, does the model grow recoveries on tenants who are on fixed CAM, capped, gross, or self-maintaining, where that growth does not exist?

Use [Underwriting Calculations](knowledge/underwriting-calc.md) for NOI and value math and [Risk Scoring](knowledge/risk-scoring.md) for severity. Hand the corrected recovery line to [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md), the debt-sizing consequences to [Retail Financing Fit](skills/retail/retail-financing-fit.md), and the conclusions to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md). Anchor self-maintenance, go-dark, and co-tenancy facts that change the pool belong with [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md); expense inflation tied to submarket conditions belongs with [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md).

---

## Output Format

```markdown
# Retail CAM Reconciliation and Recovery Review
## Property / Format:
## Reconciliation Years Tested:
## Documents Reviewed:
## Recovery Verdict: CLEAN | UNDER-RECOVERING | OVER-BILLED / AUDIT EXPOSURE | HIGH RISK

### Recovery Structure by GLA
| Recovery Method | Tenants | GLA | % of GLA | % of Recovery Income |
|---|---|---|---|---|
| Pro rata net | | | | |
| Fixed CAM | | | | |
| Capped pass-through | | | | |
| Base year, gross, or anchor negotiated / self-maintained | | | | |

### Recoverable Pool Build
| Line | Operating Statement | Excluded by Lease | Net Recoverable Pool | Note |
|---|---|---|---|---|
| CAM / operating | | | | |
| Real estate taxes and insurance | | | | |
| Capital amortization, admin fee, management fee | | | | |

### Denominator and Occupancy
- Denominator convention, lease citation, and separate cost pools:
- Leased vs billed / economic occupancy, minimum denominator floor, and contributions backed out:

### Reconciliation Test Results
| Year | Delivered On Time | Ties to Operating Statement | Tenants Recomputed | Under-Billing | Over-Billing | Timing |
|---|---|---|---|---|---|---|

### Recovery Ratio and Leakage
| Metric | Prior Year | Current | Underwritten | Note |
|---|---|---|---|---|
| Recovery income | | | | |
| Recoverable pool (denominator stated) | | | | |
| Recovery ratio | | | | |
| Leakage $ and value impact at exit cap | | | | |

### Issues
| Issue | Type (Under-Bill / Over-Bill / Audit / Timing) | $ Impact | Severity | Next Step |
|---|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every tenant is assigned exactly one recovery method, fixed-CAM GLA is stated as a percentage of total GLA, and the pool is built from the general ledger rather than a prior reconciliation, with anchor and fixed-CAM contributions backed out before pro rata shares are computed
- The denominator convention is quoted from the lease, separate cost pools are computed separately, and billed or economic occupancy is used with the leased-to-billed spread disclosed
- Every cap is labeled cumulative or non-cumulative and controllable or uncontrollable
- Administrative fee and management fee are shown separately with their bases, and at least two representative tenants per recovery bucket are recomputed by hand
- Every recovery ratio states its denominator, every market figure carries a date and source, and the underwritten recovery line is reconciled to the rebuilt pool rather than trended from actuals

---

## Red Flags & Dealbreakers

- Reconciliations not delivered, delivered past the lease or REA deadline, or delivered without account-level backup, or a recovery model built on leased occupancy while billed occupancy is 300 to 400 basis points lower, or on fixed-CAM, capped, gross, and self-maintaining tenants shown with pro rata recovery growth
- A cumulative cap modeled as a hard annual ceiling (understates recovery), or an uncapped pass-through assumed where a cap exists (overstates it)
- Administrative or management fee charged on taxes, insurance, or utilities that pass through at cost, or both fees inside CAM with no lease support for either
- Capital amortization carried in CAM past lease expirations that will not pick it up, or capital billed during a negotiated initial exclusion window
- Anchor approved-budget right with no approved budget for the year being billed, or cost pools ignored so a food court, patio, or enclosed-mall expense is spread across the whole center
- Open tenant audit demand, unpaid audit settlement, or a prior finding above the lease cost-shifting threshold
- Recovery receivables aged past 90 days that are disputed reconciliation balances rather than collection problems
- Underwritten recoveries above trailing actuals with no lease-level change identified

---

## When Data is Missing

- If leases or amendments are missing, do not assume pro rata. Model those suites at the property's observed billed recovery ratio and flag the GLA as unverified. If prior reconciliations are missing, treat the recovery line as untested and reduce the underwritten recovery ratio until it can be rebuilt.
- If the REA or anchor supplemental agreements are missing, do not assume anchors and pads contribute; confirm participation before including their GLA in any denominator. If capital ledgers or amortization schedules are missing, exclude capital amortization from recovery income and note the omission; if the management agreement is missing, show the fee both inside and outside the recovery ratio denominator.
- If a cap's cumulative status is ambiguous, compute both ceilings, present the range, and route the language to counsel.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full lease stack with amendments and REA, two prior reconciliations with account-level backup, general ledger detail, and representative tenants recomputed and tied |
| MEDIUM | Core leases and one reconciliation available, but anchor supplementals, capital schedules, or the REA are incomplete, or the denominator basis is inferred |
| LOW | Rent roll and operating statement only, no reconciliations or lease-level recovery language, or recovery method unknown for a material share of GLA |

---

## Related Knowledge Bases

- [Retail Lease Structures](knowledge/retail-lease-structures.md)
- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md) and [Risk Scoring](knowledge/risk-scoring.md)

## Research Basis

- [Retail CAM Reconciliation and Recovery Analyst Research](research/retail/retail-cam-reconciliation-and-recovery-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
