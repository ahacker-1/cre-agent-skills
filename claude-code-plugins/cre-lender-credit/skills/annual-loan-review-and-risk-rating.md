---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Annual Loan Review and Risk Rating

Perform the periodic review of an existing U.S. commercial real estate loan: refresh NOI, DSCR, debt yield, and LTV, test appraisal age, rent roll and rollover, sponsor condition, covenant status, and documentation exceptions, then confirm or change the regulatory classification and the internal grade, document the migration against the prior review, and set the actions and the next review date.

---

## When to Use This Skill

Use this skill on the annual review cycle, at renewal or extension, when a covenant test or a watchlist trigger fires, when new borrower or market information arrives that could change a grade, or when credit risk review samples the credit. It is written for bank and credit union credit analysts, portfolio managers, credit officers, credit risk review staff, and special assets officers. Debt fund, life company, and CMBS credit teams can run the same analysis, but the interagency classification scale does not apply to them and the output should say so. This is educational decision support, not legal, tax, investment, accounting, or financing advice; classification, nonaccrual, charge-off, allowance, and regulatory reporting conclusions belong to the institution and its regulator, and the board-approved rating definitions control over anything here.

---

## What You'll Need to Provide

- Loan and prior review: commitment and outstanding balance, note date, maturity, rate, amortization, remaining interest-only, payment and past-due history, prior modifications, extensions and advances; and the last risk rating, classification, effective date, rationale, action plan, and watchlist status
- Property: trailing 12 and trailing 3 operating statements, current rent roll with lease expirations, budget or forecast, occupancy history, capital plan, and the most recent inspection report
- Collateral: most recent appraisal or evaluation with value type and effective date, the institution's appraisal review, tax status, insurance status, and any environmental or condition report
- Sponsor and guarantor: current financial statements, tax returns, verified liquidity, contingent liabilities, schedule of real estate owned, and the guarantee form and any burn-off conditions
- Compliance: covenant definitions, tests, measurement dates and cure rights, certificates received, and the current documentation exception list
- Institutional parameters: the internal rating scale and the criteria that map to each grade, watchlist criteria, appraisal re-order policy, review frequency policy, and nonaccrual policy

If the institution's rating scale and thresholds are not supplied, report the metrics and the supportable regulatory classification and withhold the internal grade number rather than inventing one.

---

## Mission

Produce a documented, defensible conclusion on one existing CRE credit: what the property, sponsor, and collateral actually did since the last review; whether the grade still reflects the risk over the remaining term; the regulatory classification with the specific weakness that supports it; the migration and its cause; and the actions, reporting, and next review date that follow.

---

## Strategy

### Step 1: Set the Perimeter and Restate the Prior Baseline

- Exposure: all facilities to the borrower and related entities, funded and unfunded, and whether cross-collateralization or cross-default links them. Rate the amount the institution is legally committed to fund; unfunded balances carry a contingent designation.
- Prior baseline: last grade and classification, effective date, prior NOI, DSCR, debt yield, LTV, occupancy, and the conditions the last review said would be monitored.
- Review trigger and independence: calendar annual review, renewal, covenant event, watchlist trigger, or new information, and whether the reviewer controls the loan. Supervisory guidance treats a formal annual review of every credit as the floor, with large, new, complex, higher-risk pass, and problem credits reviewed more often and ratings updated whenever relevant new information arrives. A grade that should have moved months ago is a process finding as well as a credit finding, and a review by the relationship officer is a self-assessment rather than an independent credit risk review conclusion.

### Step 2: Assemble and Age the Reporting Package

| Item | Frequency frame | Status to record |
|---|---|---|
| Operating statements, rent roll, expiration schedule | Annual may suffice for stabilized multifamily or few-tenant long-lease property; lease-up and multi-tenant nonresidential warrant monthly, quarterly, or semiannual | Period covered, as-of date, received, analyzed, reconciled |
| Borrower and guarantor financials, tax returns, covenant certificates | Financials not less than annually; certificates per loan agreement test dates | Period, signed, verified liquidity, test result |
| Real estate tax and insurance evidence | Each installment and renewal | Paid to date, coverage in force, lender named |
| Property inspection | Institution policy; more attention to troubled property or borrower | Date, condition, rent roll and vacancy verified against observation |
| Appraisal or evaluation and the institution's review | Policy-set, plus event triggers | Effective date, value type, review completed |

The review is only as good as the file, so inventory what was required, what arrived, and what is stale. Delinquent real estate taxes are treated in supervisory guidance as nearly always an indicator of a distressed property, borrower, or guarantor; do not file the notice and move on. Where items are missing, record a documentation exception with an age and an owner, keep the collection effort continuous, and rate on what exists rather than assuming performance held.

### Step 3: Rebuild Property Performance

Rebuild the numbers rather than rolling forward last year's model. Formula definitions are in [Underwriting Calculations](knowledge/underwriting-calc.md); do not restate them in the output.

- **NOI**: trailing 12 and annualized trailing 3, with the underwriting conventions applied consistently to both periods (management fee, replacement reserves, and leasing costs per the institution's convention). Show the bridge from prior-review NOI to current NOI by line item: occupancy, rate, expense, tax reassessment, insurance reset.
- **DSCR and debt yield**: DSCR on the actual payment and again as if amortizing where the loan is interest-only or partially interest-only, stating which NOI and which debt service each figure used; debt yield on in-place NOI, which, being independent of rate, amortization, and cap rate, is the cleanest year-over-year comparison when rates have moved.
- **Occupancy, rollover, and concentration**: economic versus physical occupancy, signed-not-commenced rent shown separately, percent of base rent expiring before maturity and before each extension option, top tenant and top five exposure, any termination, contraction, or co-tenancy right arriving before maturity, and the capital cost of re-tenanting that rollover.
- **Cushion and exit**: how far occupancy or rate can fall before coverage reaches 1.00x, and the projected maturity balance against a stressed value and coverage test. Origination-market averages check the exit for reasonableness and are not rating thresholds; CBRE reported Q2 2026 averages of 59.6% LTV on commercial loans, 1.43 DSCR, and 10.2% debt yield (published 2026-08-03), directional and to be re-verified.

### Step 4: Test Collateral Value and Appraisal Age

- Value matters most when repayment capacity weakens and least as a standalone downgrade trigger. State the appraisal or evaluation effective date, the value type (as-is, as-completed, as-stabilized), the appraiser, and whether the institution's own appraisal review is in the file.
- Run the validity checklist from the interagency appraisal guidelines: passage of time; local market volatility; changes in the terms and availability of financing; natural disasters; over or under supply of competing properties; improvements to the subject or competing properties; lack of maintenance; changes in economic and market assumptions such as capitalization rates and lease terms; changes in zoning, building materials, or technology; environmental contamination.
- Run the workout re-order triggers from the 2023 interagency policy statement: material deterioration in project performance; conditions for the geographic market and property type; variances between actual conditions and original appraisal assumptions; changes in project specifications; loss of a significant lease or a take-out commitment; increases in pre-sale fallout.
- Decide and document: no action, evaluation, or new appraisal. An evaluation may suffice where it updates the original assumptions to current conditions and yields a reasonable fair value estimate; where new money is advanced, the appraisal regulations govern. No interagency source sets a re-order calendar, so the interval is board policy, and the agencies reserve the right to require an appraisal for safety and soundness.
- Where the facts materially deviate from the appraisal's assumptions, adjust the value for credit analysis and say what was adjusted and why; assumptions from a qualified appraiser differing only in a limited way from norms get deference. Detail belongs to [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md).

### Step 5: Update Sponsor, Guarantor, and Global Position

- Global cash flow across all entities including personal debt service, taxes, and living expenses; verified rather than borrower-asserted liquidity; net worth and its composition; the trend against the prior review; and the total number and dollar amount of guarantees extended to all lenders, not just yours, because a guarantor stretched across other projects cannot support each of them.
- Guarantee credit in the rating requires three findings under a legally enforceable guarantee: financial ability, demonstrated willingness, and economic incentive. Note whether prior performance was voluntary or the result of enforcement; absent those findings the guarantee does not improve the grade.
- Burn-off and release: confirm whether any guarantor was released or a guarantee reduced since the last review and whether the release conditions were actually tested. Release of a guarantor critical to the original decision, without offsetting support, is a structural weakness on its own. Depth belongs to [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md).

### Step 6: Test Covenants, Structure, and Documentation

- Covenant status for each test: definition, measurement date, computed result, pass or fail, whether a waiver or amendment was granted, and whether the waiver reset the test or merely skipped it. Waived or renegotiated covenants that accommodate a borrower's failure to meet the original standard are a recognized structural weakness.
- Structural weaknesses to screen for: indefinite or overly liberal repayment programs, evergreen renewals, bullet maturities unrelated to the actual repayment source, rewrites that only defer maturity, advances that fund interest payments, no meaningful amortization, weak or absent covenants, overly aggressive advance rates, and inadequate collateral documentation or valuation.
- Documentation exceptions, aged and assigned: lien perfection, title, insurance, estoppels, organizational documents, borrowing resolutions, and the appraisal review belong on this list when missing or stale.
- Whether the loan is contractually current is one consideration, not the answer. Current status can mislead where an interest reserve, a serial extension, or a re-amortization is funding the payments while the business plan has stalled. Covenant mechanics and watchlist triggers belong to [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md).

### Step 7: Assign the Classification and Grade, Document Migration, Set Actions

Rate the risk over the remaining term, not the payment record, assessing expected performance over at least the next twelve months. Use the definitions in [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md).

| Conclusion | Supports |
|---|---|
| Pass (with or without watchlist) | Repayment supported by property cash flow, sponsor, or collateral on reasonable terms, with no potential or well-defined weakness. Watchlist marks a sound but monitored credit (a prudent renewal or restructure, a rollover concentration, a policy exception, a trend worth tracking) and is an institution designation, not a regulatory grade |
| Special mention | Potential weaknesses deserving close attention that may deteriorate repayment prospects or the credit position later: adverse operating trend, reduced collateral margin, missing current financials, unordered valuation, structural or documentation weakness. Not a compromise between pass and substandard |
| Substandard | Inadequately protected by current sound worth and paying capacity of the obligor or the collateral, with a well-defined weakness jeopardizing liquidation of the debt: inadequate coverage, unprofitable operations, inadequate liquidity, marginal capitalization, repayment dependent on collateral |
| Doubtful | All substandard weaknesses plus collection in full is highly questionable and improbable, with loss deferred pending a specific event. Use infrequently and reassess promptly; nonaccrual required |
| Loss | Uncollectible; charge off in the period the obligation becomes uncollectible |

Decision rules that keep the call defensible:

- Do not adversely classify a performing loan solely because collateral value fell below the balance, or solely because the borrower is in a distressed industry; name the well-defined weakness in repayment capacity or structure first, then use value to size the exposure. Equally, do not hold a pass on a credit with a well-defined weakness because it is current, and do not use special mention as a parking space to avoid the substandard call.
- A prudent renewal or restructure to a borrower who can repay on reasonable terms is not automatically adverse, but it must be identified in the internal grading system and may warrant close monitoring.
- Where the credit is collateral dependent, split the rating: the portion adequately secured by fair value less costs to sell generally no worse than substandard, the excess loss, and doubtful only where a pending event may mitigate full loss or the loss amount cannot be reasonably determined.
- Upgrades require correction of the weakness plus sustained performance under reasonable terms, generally six months for a formally restructured loan; a plan alone is not an upgrade. Confirm accrual status against the nonaccrual test and note whether a grade change forces a nonaccrual, charge-off, or allowance consequence.

Then record migration and next steps: prior grade to current grade, direction and number of notches, the single dominant cause, whether this is a double downgrade, how long the credit has sat in its prior grade, and what changes in reporting. Set the next review date, and where the answer is an accommodation or restructure, hand the credit to [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md). Where a renewal is being underwritten, the sizing work belongs to [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md) and the written package to [Credit Memo Writer](skills/lender-credit/credit-memo-writer.md). Aggregate migration reporting rolls up through [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md).

---

## Output Format

```markdown
# Annual Loan Review
## Borrower / Property / Market:
## Facility: $ commitment | $ outstanding | maturity | rate | amortization / IO
## Review Type: Annual | Renewal | Event-driven | Credit risk review sample
## Rating: PASS | SPECIAL MENTION | SUBSTANDARD | DOUBTFUL | LOSS (interagency scale; not applicable to non-bank lenders)
## Internal Grade: prior -> current | Accrual: Accrual | Nonaccrual | Watchlist: Yes / No
## Next Review Date:

### Performance Since Prior Review
| Metric | Prior Review | Current | Change | Note |
|---|---|---|---|---|
| NOI (T12) | | | | |
| NOI (T3 annualized) | | | | |
| DSCR (actual / as-if amortizing) | | | | |
| Debt yield | | | | |
| LTV | | | | |
| Occupancy (physical / economic) | | | | |
| % base rent expiring before maturity | | | | |

### Collateral and Valuation
- Value / type / effective date / age / appraisal review in file:
- Validity or re-order triggers fired; action: none | evaluation | new appraisal; adjustments made for credit analysis and why:

### Sponsor and Guarantor
| Item | Prior | Current | Finding |
|---|---|---|---|
| Global cash flow / coverage | | | |
| Verified liquidity / net worth | | | |
| Contingent liabilities (all lenders) | | | |
| Ability / willingness / incentive | | | Credit given in rating: Yes / No |

### Covenants and Exceptions
| Test or Item | Requirement | Result | Status | Action |
|---|---|---|---|---|

### Rating Rationale and Migration
- Weakness(es) identified (or none) and classification rationale:
- Migration: prior -> current, notches, direction, dominant cause, double downgrade Y/N, time in prior grade
- Accounting consequence (nonaccrual, charge-off, allowance):

### Recommended Actions
| Action | Owner | Due | Escalation |
|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every ratio states which NOI (trailing 12, trailing 3 annualized, underwritten) and which debt service (actual, as-if amortizing, floor rate) it used, and the same convention is applied to the prior-period figure
- The NOI bridge from prior review to current review reconciles by line item rather than asserting a change
- The rent roll ties to the operating statements and to the last inspection observation, and signed-not-commenced rent is shown separately
- The value carries a type, an effective date, an age, and the outcome of the validity and re-order checklists
- The classification names a specific weakness in repayment capacity, structure, or collateral, not a metric alone, and the internal grade is mapped to the institution's own scale or withheld with a reason
- Migration is stated with direction, notches, cause, and time in the prior grade, and a first-time downgrade of a credit that deteriorated earlier is flagged as a timeliness finding
- Documentation exceptions are aged and assigned rather than summarized, and the review says who performed it and whether that person is independent of the loan approval process

---

## Red Flags & Dealbreakers

- The loan is current only because an interest reserve, a serial extension, or a re-amortization is funding the payments while the business plan has stalled
- The grade has not moved in several reviews while NOI, occupancy, coverage, or value deteriorated in each of them
- A downgrade is proposed solely because a new appraisal came in below the balance, with no identified weakness in repayment capacity or structure, or a well-defined weakness is documented in the narrative while the grade stays pass because the loan is current
- Special mention is used to avoid the substandard call, doubtful persists across quarters without the pending event resolving, or the grade never enters the migration report at all
- Guarantor support is credited in the rating with no verified liquidity, no tally of guarantees to other lenders, and no evidence of willingness or incentive, or a critical guarantor was released without offsetting support
- Covenants have been waived or redefined repeatedly to accommodate the borrower's failure to meet the original standard, or the prior review's action plan was never executed and no one noticed until this review
- Real estate taxes are delinquent, insurance has lapsed, or the last inspection is old enough that the rent roll cannot be corroborated
- Bank classification vocabulary is applied to a debt fund, life company, or CMBS facility not subject to the interagency framework

---

## When Data is Missing

- No current operating statements or rent roll: record a documentation exception, rate on the most recent verified data, state the as-of date, and consider whether the absence of a current financial package is itself a potential weakness supporting special mention
- No current appraisal: report the existing value, its type, its effective date, and its age; run the validity and re-order checklists; recommend an evaluation or appraisal rather than computing a confident LTV from a stale figure
- No sponsor or guarantor update: state that the global analysis is unrun, do not credit the guarantee in the rating, and make the update a required action; with no institutional rating scale, report the metrics and the supportable regulatory classification and withhold the internal grade number
- No prior review file: state that migration cannot be computed, treat this as a baseline review, and flag the gap. Where covenant definitions are unavailable, test what the file supports and name the tests that could not be run

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Current operating statements, rent roll, sponsor and guarantor financials, covenant certificates, a recent inspection, and a current appraisal with the institution's review are all in the file; the prior review and rating scale are available; every metric reconciles |
| MEDIUM | Core property performance is verified but one of appraisal currency, sponsor update, inspection, or covenant certificate is missing or stale; classification is supportable with the gap disclosed |
| LOW | No current operating data, no verified rent roll, no sponsor update, or no prior review baseline; output is an indication of condition and a documentation exception list, not a rating conclusion |

---

## Related Knowledge Bases

- [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md)
- [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Annual Loan Review and Risk Rating Research](research/lender-credit/annual-loan-review-and-risk-rating-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
