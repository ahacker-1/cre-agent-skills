---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Retail Underwriting Model Builder

Build a lease-by-lease U.S. retail cash flow model that carries percentage rent, capped recoveries, sales-driven renewal probability, tenant-type leasing capital, an anchor reserve, a co-tenancy downside case, and a lender sizing view.

---

## When to Use This Skill

Use this skill when you have a retail rent roll, lease abstracts, tenant sales, and an operating history and need a defensible base-case model for an acquisition, a refinance, or an asset review. It is the right tool when value turns on lease structure, tenant sales, anchor durability, and recovery leakage rather than on a stabilized rent-roll snapshot. For unit-mix multifamily assets use [Financial Model Builder](skills/underwriting/financial-model-builder.md) and [Scenario Analyst](skills/underwriting/scenario-analyst.md) instead; this skill is the lease-by-lease retail build. This is educational decision support, not legal, tax, investment, accounting, or financing advice.

---

## What You'll Need to Provide

- Rent roll with suite, GLA, tenant, commencement, expiration, base rent schedule, options, and recovery method
- Lease abstracts or leases for anchors, junior anchors, and any tenant above 5% of GLA
- Reported tenant sales and the reporting period, plus percentage rent rates and breakpoints
- Trailing 12-month and prior-year operating statements, the CAM reconciliation, and the property condition assessment or capital plan
- Format (grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use, pad, STNL), total GLA, anchor GLA share, any REA / OEA, and the purchase price or basis, hold period, and financing assumptions if available
- Market rent, downtime, and concession evidence from comps or signed LOIs

---

## Mission

Build a retail cash flow that separates contractual income from market assumptions, prices the leasing and capital cost of getting there, tests the co-tenancy and anchor downside explicitly, and reports the result in a structure a lender can reconcile.

---

## Strategy

### Step 1: Frame the Model and Classify the Rent Roll

- Confirm format and anchor GLA share, then classify every space as anchor, junior anchor, inline shop, pad, or STNL. These are different underwriting animals, not size buckets.
- Model contractual cash rent, stripping out straight-line rent, above- and below-market lease amortization, and ASC 842 fixed-CAM straight-lining. They are reporting conventions, not cash.
- Adopt the CREFC Investor Reporting Package v8.4 line structure: base rent, expense reimbursement, percentage rent, parking, and other income to EGI; operating expenses including ground rent to NOI; then leasing commissions, tenant improvements, capital expenditures, and extraordinary capital expenditures as Total Capital Items to NCF.
- Reconcile rent roll GLA and base rent to the operating statement before building anything, and note every variance. Take the rent roll, tenant mix, and sales inputs from [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md) and the lease terms from [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md).

### Step 2: Build Base Rent and Percentage Rent

- Build the base rent schedule tenant by tenant with every contractual step, mid-term bump, and free-rent period on its actual date. For each percentage rent tenant, extract the rate, the breakpoint type (natural or artificial), the gross sales definition and its exclusions, the measurement period, and the reporting and audit mechanics. Recompute the natural breakpoint at every base rent step - a single breakpoint carried across the hold overstates overage rent in every step year.

```text
Natural Breakpoint = Annual Minimum Rent / Percentage Rate
Percentage Rent Due = (Gross Sales - Breakpoint) x Percentage Rate
```

- Grow sales at a stated, sourced rate. Macerich reported comparable tenant sales up 1.2% for the trailing twelve months ended 2025-12-31 on $881 PSF with flat traffic - directional and dated for mall inline space, not a default for any other format.
- Do not underwrite percentage rent growth in strip, unanchored, pad, or STNL models. Macerich reports percentage rent at 0.6% of tenant sales, Realty Income at under 1% of rental revenue.

### Step 3: Build Recoveries With Caps and Leakage

- Classify each lease by recovery method: pro rata, fixed CAM, capped pass-through, base year, gross, or hybrid by expense category. Fixed-CAM tenants do not participate in expense inflation at all. For every cap, model whether it is cumulative or non-cumulative and which expenses it covers - caps normally apply to controllable expenses only, with taxes, insurance, security, and utilities uncapped.
- Set the denominator explicitly - total GLA, leased GLA, or occupied GLA - and state whether anchors are in or out. Malls commonly exclude anchors and use occupied floor area; power centers commonly use floor area ratios; ground-leased parcels commonly use land area. Gross up variable expenses to a stated occupancy so vacancy cost is not shifted onto occupied tenants, and carry the vacancy share as landlord leakage. Model management and administrative fees separately and confirm the fee base - Cox Castle describes management fees of 2.5%-4% of gross revenues layered with administrative fees of 10%-15% of other CAM (2014, a negotiating range, not a rule).
- Compute the recovery ratio each year and reconcile it against the CAM reconciliation. Take the leakage detail from [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md).

### Step 4: Build the Rollover Engine

Model anchor and shop as separate rollover populations - Brixmor discloses anchor original terms of 10 to 20 years against 5 to 10 years for smaller tenants, so shop GLA rolls two to three times as often. Set a renewal probability for every expiring lease and state its basis. There is no published national default; use this rule:

| Signal | Pushes Renewal Probability Up | Pushes It Down |
|---|---|---|
| Occupancy cost vs the tenant's own fleet | At or below fleet average | Materially above fleet average |
| Sales trend | Growing, or stable with growing traffic | Declining, or a kick-out threshold in reach |
| Option rent vs market | Option below market and unexercised | No option, or option at or above market |
| Co-tenancy status | No trigger armed | Trigger armed or already running |
| Capital and category | Renewal-level allowance; necessity, service, F&B, off-price, medical | New-deal allowance and demising work; categories whose growth runs in the non-store channel |

- Renew at the contractual option rent wherever an unexercised option exists, never at market. Brixmor achieved 38.7% new-lease spreads in 2025 against 21.7% blended excluding options and 16.4% including options - option exercises absorbed roughly a third of the blended spread. Mark non-renewals to comp-supported market rent and state the mark-to-market. Brixmor's anchor expirations through 2028 carry a weighted average expiring ABR of $11.37 PSF against $17.84 PSF on new anchor leases signed in 2025.
- Set downtime months by tenant type from signed LOIs, local comps, and the property's own leasing history, sourced through [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md). Sanity-check the signature-to-rent-commencement lag: Brixmor reported a 350 basis point leased-to-billed spread at 2025 year end, with 2.7 million SF and $62.3 million of ABR signed but not yet commenced.

### Step 5: Price Leasing Capital and Property Capital

- Size TI/TA and LC per deal, by tenant type and by new versus renewal. Renewal capital is the dominant lever: Regency's FY2025 pro-rata disclosure shows anchor new at $28.67 allowance and $4.65 commissions PSF against anchor renewal at $0.65 and $0.41, and shop new at $51.12 and $17.37 against shop renewal at $1.45 and $1.30. Do not adopt those as defaults - the same table for FY2024 shows anchor new allowance at $61.64 PSF. Size from actual deal terms and current concession posture, and cite the year of any benchmark used.
- Carry a separate anchor reserve sized to the cash cost of the anchor case - allowance, commissions, demising, facade and entry work, downtime, and any landlord base-building obligation - never to a PSF rule of thumb. Build property capital from the property condition assessment: immediate repairs, then roof, parking lot and site, facade, and HVAC on their own replacement timing. Show the recurring reserve and one-time replacements separately, matching the CREFC split between capital expenditures and extraordinary capital expenditures.
- Read roof, structure, and parking responsibility off the lease stack rather than assuming it by format - Kimco discloses that many of its leases require the landlord to make roof and structural repairs while a number place that responsibility on the tenant. Model ground rent as an operating expense on any ground-leased parcel and confirm whether that parcel participates in CAM at all.

### Step 6: Run the Downside Cases and Set the Exit

- Build a co-tenancy downside case, not a footnote. Model the remedy ladder actually in the leases: abatement (commonly 50% of fixed rent or percentage rent only), then the decision point at roughly six to twelve months where the tenant returns to full rent, terminates, or is recaptured.
- Build an anchor loss case: anchor goes dark or does not renew, co-tenancy triggers fire, inline sales fall, kick-out thresholds come into reach, and the backfill carries new-deal capital and full downtime. Test the backfill pool against recorded REA exclusives and prohibited uses before assuming any replacement tenant, using the trigger map from [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md).
- Set the exit cap from a comp-supported going-in cap plus an explicit spread, justified by WALT at exit, anchor status, format, and capital condition. No format cap-rate matrix is asserted here. For STNL and pad only, the Boulder Group reported Q2 2026 asking cap rates of 6.82% overall and 6.60% retail, premium ground leases at 4.45% and drug store at 7.85% (2026-07-07, directional and dated); never apply STNL asking caps to a multi-tenant center. Capitalize durable NOI at exit, excluding percentage rent, specialty and temporary income, and signed-not-open rent unless you can defend each as durable.

### Step 7: Build the Lender Sizing View and State the Verdict

- Report DSCR on both NOI and NCF, plus debt yield on in-place NOI, LTV, and loan PSF against basis. Formulas come from [Underwriting Calculations](knowledge/underwriting-calc.md), risk weighting from [Risk Scoring](knowledge/risk-scoring.md). Pre-screen the base and downside cases against CREFC Servicer Watchlist triggers: NCF DSCR below 1.10x (1E); NCF DSCR below 1.40x and below 75% of underwritten (1F); occupancy below 80% of underwritten (4A); a tenant above 30% of NRA expiring within 12 months for loans at or above $30 million or within 6 months below that (4C); top-three tenants each at least 5% and cumulatively above 30% expiring within 6 months (4D); a major tenant above 30% of NRA dark, defaulted, or terminated (4F).
- Expect a haircut between your NOI and a lender's sustainable cash flow, and run a sustainable-NCF sensitivity. KBRA reported KNCF 10.4% below issuer cash flow and values 40.0% below third-party appraisals on a conduit pool 43.0% retail (2024-02-15). Give percentage rent no debt-service credit - carry it as equity upside and a tenant-health signal.
- State what the base case actually depends on: durable in-place income, mark-to-market capture, anchor renewal, a backfill execution, or a capital-led repositioning. Hand the sized result to [Retail Financing Fit](skills/retail/retail-financing-fit.md) and the narrative to [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md).

---

## Output Format

```markdown
# Retail Underwriting Model
## Property:
## Format / GLA / Anchor GLA Share:
## Verdict: SUPPORTS BASIS | MARGINAL | DOES NOT SUPPORT BASIS

### Model Frame
| Item | Assumption | Basis |
|---|---|---|
| Hold period / sales growth | | |
| Market rent, expense growth | | |
| Exit cap (going-in + spread) | | |
| Financing | | |

### Cash Flow (CREFC line structure)
| Line | Yr 1 | Yr 3 | Yr 5 | Exit Yr |
|---|---|---|---|---|
| Base rent | | | | |
| Expense reimbursement | | | | |
| Percentage rent | | | | |
| Other / parking / specialty | | | | |
| Effective Gross Income | | | | |
| Operating expenses (incl. ground rent) | | | | |
| Net Operating Income | | | | |
| Leasing commissions / tenant improvements | | | | |
| Capital expenditures / extraordinary capital | | | | |
| Net Cash Flow | | | | |

### Rollover and Renewal Assumptions
| Tenant | Type | GLA | Expiry | Occ Cost % | Option Rent vs Market | Renewal Prob | Downtime (mo) | TI PSF | LC PSF | Basis |
|---|---|---|---|---|---|---|---|---|---|---|

### Recovery Structure
| Group | Method | Cap (cum / non-cum) | Denominator | Anchors In/Out | Modeled Recovery Ratio | Leakage Driver |
|---|---|---|---|---|---|---|

### Capital Plan
| Item | Timing | Cost | Recoverable? | Source |
|---|---|---|---|---|
| Immediate repairs | | | | |
| Roof / facade | | | | |
| Parking lot and site | | | | |
| HVAC | | | | |
| Anchor reserve | | | | |

### Scenarios
| Case | NOI (stabilized) | NCF | Exit Value | Levered Return | Comment |
|---|---|---|---|---|---|
| Base | | | | | |
| Co-tenancy downside | | | | | |
| Anchor loss | | | | | |

### Lender Sizing View
| Test | Base Case | Downside | Watchlist Trigger Tripped? |
|---|---|---|---|
| NOI DSCR / NCF DSCR | | | 1E / 1F |
| Debt yield (in-place NOI) | | | |
| LTV / loan PSF vs basis | | | |
| Occupancy vs underwritten | | | 4A |
| Major tenant rollover in term | | | 4C / 4D / 4F |

### What the Base Case Depends On
- 

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Rent roll GLA and base rent reconcile to the operating statement, with every variance noted, and straight-line rent, above- and below-market amortization, and fixed-CAM straight-lining are excluded from cash flow
- Every percentage rent breakpoint is recomputed at each base rent step
- Every lease is assigned a recovery method, a cap type, and a denominator, and the modeled recovery ratio reconciles to the CAM reconciliation
- Every expiring lease carries a stated renewal probability with a stated basis, and renewals with unexercised options are modeled at option rent
- Anchor and shop carry separate rollover, capital, and downtime assumptions, and Total Capital Items are shown separately so NOI-DSCR and NCF-DSCR are both reportable
- Exit cap is stated as going-in plus a justified spread with the comp named, and every time-sensitive figure carries a date and a source

---

## Red Flags & Dealbreakers

- Fixed-CAM leases modeled as pro rata recoveries, so modeled recovery growth does not exist; a single natural breakpoint carried across the hold while base rent steps up; or every tenant renewed at market rent while below-market options sit unexercised
- Anchor replacement modeled as an ordinary leasing assumption, with no reserve and no REA exclusive check
- Percentage rent, specialty income, or signed-not-open rent carried into exit NOI as durable
- Ground rent omitted on a ground-leased parcel, or a ground-leased pad modeled as a CAM participant
- Co-tenancy relief already running and shown as in-place rent, or a downside case with abatement but no termination or recapture decision point
- Roof, structure, or parking capital assumed by format rather than read off the lease stack
- Exit cap equal to going-in cap with no spread and no comp while WALT shortens materially, or debt sized to a stabilized pro forma that fails an in-place DSCR or occupancy test in year one
- STNL or pad underwritten with center-level metrics, or STNL asking caps applied to a multi-tenant center

---

## When Data is Missing

- If tenant sales are missing, do not model percentage rent and do not assert an occupancy cost ratio. Model base rent and recoveries only, and flag the gap as a renewal-probability blind spot.
- If the CAM reconciliation is missing, model recoveries from the lease language and show the unreconciled recovery ratio as an open item. If lease abstracts are missing for anchors or any tenant above 5% of GLA, treat the model as incomplete rather than defaulting the recovery method.
- If the property condition assessment is missing, do not set capex to zero. Carry a stated placeholder, label it unsupported, and list roof, parking, facade, and HVAC as unpriced.
- If market rent and downtime comps are missing, show the model at in-place rent with no mark-to-market and state that the rollover case is unsupported. If the REA / OEA is missing, do not model a backfill or a pad split.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full rent roll, anchor and major-tenant leases, reported tenant sales, CAM reconciliation, two years of operating statements, PCA, and market comps are available and reconciled |
| MEDIUM | Rent roll and core leases available, but sales are partial, the CAM reconciliation is stale, or downtime and market rent rest on limited comps |
| LOW | Rent roll only, no tenant sales, no CAM reconciliation, no PCA, or anchor lease and REA terms unavailable |

---

## Related Knowledge Bases

- [Retail Benchmarks](knowledge/retail-benchmarks.md)
- [Retail Lease Structures](knowledge/retail-lease-structures.md)
- [Retail Lender Criteria](knowledge/retail-lender-criteria.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)
- [Risk Scoring](knowledge/risk-scoring.md)

## Research Basis

- [Retail Underwriting Model Builder Research](research/retail/retail-underwriting-model-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
