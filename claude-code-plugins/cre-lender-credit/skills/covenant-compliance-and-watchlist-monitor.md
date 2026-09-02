---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Covenant Compliance and Watchlist Monitor

Test a closed U.S. commercial real estate loan against its covenants, reporting obligations, and structural triggers, then recommend watchlist placement, retention, or removal with a written action plan.

This is educational credit-side decision support, not legal, tax, investment, accounting, or financing advice. Default declarations, notices, reservations of rights, waivers, forbearance, classification, nonaccrual, and charge-off decisions belong to the institution and its counsel.

---

## When to Use This Skill

Use this skill between annual reviews, when financials or a rent roll arrive, when a covenant certificate is delivered or missed, when a trigger event is reported, when a maturity moves inside the monitoring window, or when preparing the monthly or quarterly watchlist package for a credit committee or board. Do not use it to grade a loan for regulatory classification on its own: it produces the evidence and the recommendation, and the rating decision belongs to [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md).

---

## What You'll Need to Provide

- Loan agreement, note, mortgage or deed of trust, guaranty, cash management or lockbox agreement, and every amendment, modification, forbearance, or waiver letter. This skill reads those documents to extract and test the obligations a closed loan actually carries; the borrower-side negotiation review of the same documents before closing is [Loan Document Reviewer](skills/legal/loan-doc-reviewer.md)
- The approved credit memo or term sheet showing the original underwritten DSCR, debt yield, LTV, occupancy, and sponsor tests, as produced by [Credit Memo Writer](skills/lender-credit/credit-memo-writer.md)
- Delivered financials for the test period: operating statement, trailing twelve month statement, rent roll, borrower and guarantor statements, tax returns, and covenant compliance certificate
- Payment history, escrow and reserve balances, servicing advances, current tax and insurance status
- Most recent appraisal or evaluation and its date, any property inspection report, current watchlist status, risk rating, waiver history, and prior action plan
- The institution's watchlist and covenant policy, reporting calendar, and exception process

---

## Mission

Determine whether every tested obligation was met on the definition written into the loan documents, identify the conditions that are deteriorating before payment status does, and produce a defensible watchlist recommendation with a dated action plan and a stated release threshold.

---

## Strategy

### Step 1: Build the Obligation Inventory

Read the documents before touching the numbers. List, with a document and section citation for each:

- Financial covenants. The common set for income-producing CRE is debt yield, DSCR, LTV, LTC, and borrower or guarantor minimum net worth or liquidity (OCC Comptroller's Handbook, Commercial Real Estate Lending, v2.0). Construction credits usually add speculative and unsold unit limits, inventory limits, limits on additional debt, guarantees and liens, and restrictions on distributions before repayment.
- The exact covenant definition: what income, what expenses, management fee, replacement reserve, ground rent, whether debt service is actual or as-if amortizing, test period, and measurement date.
- Reporting deliverables and due dates for the property, the borrowing entity, and each guarantor.
- Structural triggers: lockbox, springing cash management, excess cash sweep, reserve springing, letter of credit posting, recourse burn-off, and release conditions.
- Cure rights, grace and notice periods, and any cap on cures per year or over the term.
- Any covenant whose definition differs across the loan agreement, guaranty, and cash management agreement. That divergence is a finding, not a formatting note.

### Step 2: Test the Financial Covenants Twice

Run each test on the document definition, then run the same test on the underwriting definition, and report both when they diverge. The OCC handbook states directly that debt service coverage calculations for covenant compliance may differ from the DSCR used for underwriting and risk-rating analysis. A pass on the document definition paired with a fail on the underwriting definition is the most common quiet deterioration in a CRE book, and it belongs on the report.

For each test show: covenant level, delivered result on each definition, the prior two test periods, and pass, fail, or not testable. Do not restate formulas; use [Underwriting Calculations](knowledge/underwriting-calc.md).

Calibration points, each labeled by source rather than treated as a policy level:

| Reference | Level | What it actually is |
|---|---|---|
| CREFC Portfolio Review Guidelines code 1E | NCF DSCR below 1.10x, or below 1.20x for healthcare and lodging | CMBS servicer watchlist Credit trigger |
| CREFC code 1F | NCF DSCR below 1.40x and below 75% of underwritten DSCR | CMBS servicer watchlist Informational trigger |
| CREFC code 1G | Floating rate DSCR below 1.0x and below 90% of underwritten in-place NOI | CMBS servicer watchlist Credit trigger |
| Freddie Mac Optigo conventional fixed-rate (4/2026) | 1.25x minimum amortizing DCR at every term | Agency origination floor, not a monitoring trigger |

An LTV covenant cannot be tested against a stale value. Before reporting an LTV result, confirm the appraisal or evaluation is still valid against the interagency validity factors: passage of time, local market volatility, terms and availability of financing, natural disasters, supply of competing properties, improvements to the subject or competitors, lack of maintenance, changes in economic and market assumptions such as capitalization rates and lease terms, changes in zoning, building materials, or technology, and environmental contamination. Route the valuation question to [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md). Test guarantor net worth, liquidity, and global coverage on verified statements, not asserted ones, and route that analysis to [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md) where the guarantor is the binding test. Where the covenant set itself looks wrong for the credit, the sizing question belongs to [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md).

### Step 3: Age the Reporting Deliverables and the Payment Record

Non-delivery is a monitored condition with its own aging, not a pending item. Build a delivery table showing what was due, when, what arrived, in what form, and how many days late.

- Set expected frequency by property stability. Annual operating statements and rent rolls may be adequate for a stabilized property with few tenants on long leases extending past maturity or for stabilized multifamily. Lease-up assets and multi-tenant properties with frequent expirations warrant monthly, quarterly, or semiannual reporting (OCC handbook).
- Note statement quality: audited, reviewed, borrower-prepared, cash basis, or annualized. Cash basis statements understate expenses when taxes went unpaid, and nothing should be annualized from fewer than six months of data.
- Track taxes, insurance, escrow balances, and servicing advances. Delinquent real estate taxes are nearly always an indicator of a distressed property, borrower, or guarantor (OCC handbook). CMBS servicing tripwires for calibration: non-escrowed taxes more than 60 days past due, property or liability insurance more than 60 days delinquent or force-placed, and servicing advances more than 30 days delinquent and over $10,000 in aggregate.
- Record payment history over the trailing twelve months, including any pattern of three or more delinquencies. Payment status is a trigger, never a screen: late or missed payments often appear only after significant deterioration, and criticized loans are usually current.

### Step 4: Check Cash Management, Sweeps, and Structural Triggers

For each structural trigger, state whether it is armed, tripped, or cured, with the measurement date.

- Lockbox type (hard, soft, or springing), whether tenant direction letters were actually issued after a trigger, and whether excess cash is flowing to the borrower or into a lender-controlled excess cash flow account.
- The trip level, the cure level, and the cure duration. Cure thresholds sit above trip thresholds and require sustained performance. Observed CMBS examples: a trip at DSCR below 1.15x cured at 1.20x for two consecutive quarters, and a trip at DSCR below 1.10x cured at 1.15x for six consecutive months.
- Reserve springing, letter of credit posting, and recourse burn-off conditions, each with the verification that the condition was actually tested.
- Any unplanned draw on a letter of credit or a reserve to pay debt service. Treat that as a deterioration signal in its own right, not as a cure.

### Step 5: Score the Early Warning Indicators

Work the published indicator set rather than inventing one. From the OCC handbook and the interagency special mention description:

- Property and leasing: declining rents or sales prices; unusually generous concessions including free rent, tenant improvement allowances, moving allowances, and lease buyouts; slower absorption than projected; delinquent lease payments from major tenants; rising vacancy and turnover; impending expiration of a major lease; a dark, defaulted, or terminated major tenant.
- Cost, carry, and sponsor: tax or insurance escalation, uninsured or underinsured exposure, deferred maintenance, code violations, casualty or condemnation, budget overruns, reallocation requests, draws ahead of schedule, mechanics liens, deterioration in the borrower's other properties or businesses, requests for additional financing, contingent liabilities to other lenders, bankruptcy of borrower, owner, or guarantor, and litigation.
- Structure: repacked interest reserves, serial extensions or renewals, or a renewal on interest-only terms without a mitigant. Repacking a depleted interest reserve with new debt is a red flag indicating possible credit deterioration.
- Maturity: any balloon inside 12 to 18 months. Track the maturing balance, the refinance capacity view, and the plan. Increased refinance risk alone does not warrant a rating change, but the loan may be flagged for management attention or the watchlist (OCC Bulletin 2024-29).
- Published tenant and occupancy tripwires, all CMBS servicing standards: occupancy below 80% of underwritten for fixed-rate loans or below 80% outright for multifamily; a single tenant or any tenant over 30% of net rentable area expiring within 12 months for loans of $30 million or more, within 6 months for smaller loans, or on any notice of non-renewal; and any top-three tenants each at 5% or more and together over 30% of net rentable area expiring within 6 months.

### Step 6: Review Cure and Waiver History

- List every prior breach, the cure or waiver, the approval level, the conditions attached, and whether those conditions were verified.
- Distinguish a cure by property performance from a cure by prepayment, letter of credit, reserve deposit, or sponsor cash injection, and distinguish a waiver from a modification that reset the covenant to the delivered number. A reset removes the test rather than curing the condition and must be disclosed as such.
- Confirm each waiver was documented, approved at the right level, and captured in the exception reporting required by policy.

### Step 7: Reach the Watchlist Verdict and Write the Action Plan

Watchlist is a management designation, not a regulatory grade. In common practice it sits inside the pass grades for credits that are acceptable but warrant more than the normal level of monitoring. It is not an adverse classification, and the escalation ladder runs watchlist, then special mention, then substandard, as set out in [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md).

| Recommendation | When it applies |
|---|---|
| NO ACTION | All tests pass on both definitions, deliverables current, no armed trigger, no material indicator, maturity beyond 18 months |
| ADD | One or more covenant fails, a trigger has sprung, deliverables are materially delinquent, or two or more early warning indicators are present |
| RETAIN | Already listed and the release threshold has not been met for the required duration |
| ELEVATE | Well-defined weaknesses now jeopardize repayment; refer for a special mention or substandard determination |
| REMOVE | The listed condition is cured against a stated release threshold and has held for the required period |

Every recommendation carries a written release threshold, an owner, and a next test date. Never remove a loan on a single improved period. Where the condition has moved past monitoring into restructure, refer to [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md); roll the listings and migration into [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md); for the borrower-side package see [Lender Update Package Builder](skills/capital-markets/lender-update-package-builder.md).

---

## Output Format

```markdown
# Covenant Compliance and Watchlist Review
## Borrower / Property:
## Loan Number / Commitment / Balance:
## Test Period / Measurement Date:
## Watchlist Recommendation: NO ACTION | ADD | RETAIN | ELEVATE | REMOVE
## Current Risk Grade / Indicated Direction:

### Covenant Tests
| Covenant | Required | Document Definition Result | Underwriting Definition Result | Prior Period | Status |
|---|---|---|---|---|---|
| DSCR | | | | | |
| Debt yield | | | | | |
| LTV | | | | | |
| Occupancy | | | | | |
| Guarantor liquidity / net worth | | | | | |

### Reporting, Escrows, and Payment Record
| Obligation | Due | Received | Form / Quality | Days Late | Status |
|---|---|---|---|---|---|

### Structural Triggers
| Trigger | Trip Level | Status | Cure Level | Cure Duration | Measurement Date |
|---|---|---|---|---|---|

### Early Warning Indicators
| Indicator | Evidence | Severity | Effect on Repayment |
|---|---|---|---|

### Cure and Waiver History
| Date | Breach | Cure or Waiver | Source of Cure | Approval Level | Conditions Verified |
|---|---|---|---|---|---|

### Maturity and Refinance View
- Maturity date, months remaining, balance at maturity:
- Refinance capacity view, plan, and owner:

### Action Plan
| Action | Owner | Due Date | Release Threshold |
|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every covenant test cites the document and section that defines it, and is run on both the document definition and the underwriting definition with divergence shown rather than reconciled away
- Reporting deliverables are aged in days rather than marked pending, and statement basis and quality are stated for every delivered financial
- The LTV result is not reported against a valuation that fails the interagency validity factors, and every armed or tripped trigger has a stated cure level and cure duration
- Payment status is used as a trigger and never as the screen, and watchlist placement is not described as a classification
- The recommendation names a release threshold, an owner, and a next test date

---

## Red Flags & Dealbreakers

- The loan is contractually current only because an interest reserve, a serial extension, or a sponsor injection is funding debt service while the property has not performed
- A depleted interest reserve was repacked with new debt, or the covenant definition differs across the loan agreement, guaranty, and cash management agreement so the same loan trips at different levels
- Delinquent real estate taxes, force-placed insurance, or unreimbursed servicing advances
- A modification reset the covenant to the delivered number instead of curing the condition, or waivers have become routine
- A trigger sprang but tenant direction letters were never issued and cash is still reaching the borrower, or occupancy passes on a leased-space definition while economic occupancy collapses through free rent or signed-not-commenced leases counted as income
- A major tenant is dark, in default, terminated, or has given non-renewal notice while the rent roll still carries it
- Guarantor covenants tested against an unverified personal financial statement, a recourse burn-off released with no documented test, or no property inspection in the current monitoring cycle
- The loan matures inside 12 to 18 months with no documented refinance capacity view

---

## When Data is Missing

- If the covenant definition is missing or ambiguous, do not compute a pass. Report the test as not testable, state the ambiguity, and request the executed document.
- If financials were not delivered, report the delivery failure as the finding and age it; do not substitute the prior period and call the test passed.
- If only cash basis or partial-period statements are available, say so, do not annualize from fewer than six months, and mark the result directional. If the valuation is stale against the validity factors, report the LTV as not testable and flag it for review rather than reporting a stale ratio.
- If waiver or amendment history is incomplete, treat the covenant set as unverified and request the full amendment stack before any removal recommendation.
- If the institution's watchlist policy is unavailable, use the Step 2 calibration points as reference only, labeled as CMBS servicing or agency program standards rather than policy levels.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full document stack including amendments, current period financials and rent roll of stated quality, verified guarantor statements, a valid appraisal or evaluation, complete payment and escrow data, and known waiver history |
| MEDIUM | Core documents and current financials available, but one input is stale or unverified, such as a guarantor statement, a property inspection, or a valuation nearing the edge of validity |
| LOW | Covenant definitions unavailable or ambiguous, financials missing or annualized from a short period, amendment stack incomplete, or the test relies on borrower-asserted figures |

---

## Related Knowledge Bases

- [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md)
- [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Covenant Compliance and Watchlist Monitor Research](research/lender-credit/covenant-compliance-and-watchlist-monitor-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
