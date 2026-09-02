---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Credit Memo Writer

Draft a U.S. commercial real estate credit approval memorandum that an approval authority, loan review, and an examiner can all read in the same order.

---

## When to Use This Skill

Use this skill when screening, sponsor, appraisal, property, and market work is done and the credit has to be written up for an approval authority: a new-money origination, a renewal, an increase, a construction or transitional credit, or a re-underwrite at maturity. Use it as well to challenge a memo someone else drafted before it reaches committee.

This is educational decision support for lender-side credit staff. It is not legal, tax, investment, accounting, appraisal, or financing advice. Your institution's board-approved loan policy, your primary regulator, and your counsel control every conclusion. This is the lender's credit-approval frame. The borrower-side equivalents are [Recap IC Memo Writer](skills/capital-markets/recap-ic-memo-writer.md) for a debt or recapitalization ask and [IC Memo Writer](skills/underwriting/ic-memo-writer.md) for an equity investment committee; do not mix those frames into this document.

---

## What You'll Need to Provide

- Loan request: amount, facility type, purpose, term, amortization, rate, index and floor, fees, recourse, prepayment
- Screening and sizing output, including which test binds, from [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md)
- Sponsor and guarantor analysis, global cash flow, verified liquidity, contingent liabilities, from [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md)
- Appraisal or evaluation plus the completed lender review, from [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md)
- Property file: rent roll, historical and trailing operating statements, budget, lease abstracts, rollover schedule, capital plan, environmental and property condition reports
- Market data: submarket vacancy, absorption, competing supply, effective rents net of concessions, comparable sales
- Portfolio position: current concentration ratios, segment sublimit headroom, and any limit that constrains the request, from [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md)
- Renewals, increases, and re-underwrites at maturity: the current risk rating, classification, migration, and open action plan from [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md), and the covenant test results, delivery aging, and watchlist status from [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md)
- Credits already showing well-defined weaknesses: the diagnosis, classification, accrual position, and path comparison from [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md), which this memo writes up rather than re-derives
- Institution inputs: relevant loan policy sections, the internal risk rating scale, and delegated approval authorities
- Construction or ADC only: budget, plans, contracts, feasibility study, draw and inspection protocol, takeout source, preleasing or presale status

---

## Mission

Produce a memo that states the ask and the recommendation up front, proves the primary repayment source with the property's own cash flow, tests the secondary and tertiary sources in that order, shows the downside and the exit, names every policy exception with a quantified mitigant, and assigns a risk rating the file can defend.

---

## Strategy

### Step 1: Frame the Request and Verify the File Is Complete

Open with the ask in one paragraph: borrower and guarantor entities, amount, facility type, purpose, term, amortization, rate, recourse, collateral, and the recommendation. Do not bury the recommendation. Then confirm the file supports a decision. The OCC's file-read procedures assume the memo can identify the purpose of the loan and the source of repayment and assess the ability to repay, so missing items belong in the memo as gaps, not as silence. Confirm at minimum:

- Signed borrower and guarantor financial statements and tax returns; property operating statements, trailing 12, and a current rent roll
- The appraisal or evaluation **and** the lender's completed independent review; the interagency guidelines expect that review before the final credit decision, so a memo recommending approval ahead of it is out of sequence
- Title, survey, entity documents, environmental scope, insurance
- Construction add-ons: budget, plans, executed contracts, feasibility study, soil report

### Step 2: Build Sources and Uses and Test the Equity

Show total capitalization, not just the loan. For each source state amount, form, provider, and timing; for each use state the line item and its support. Decision rules:

- Hard equity means cash or unencumbered investment in the property, contributed before loan advances begin. Deferred developer profit, unearned fees, overhead, and accrued land carry are not equity.
- Related-party loans, seller paper, and preferred equity are debt or hybrid capital; show them in the stack and in global coverage, not in the equity line.
- If the credit is construction or ADC, run the HVCRE test explicitly: at least 15 percent of the property's appraised as-completed value contributed by the borrower in cash, unencumbered readily marketable assets, out-of-pocket development expenses, or contributed real property, contributed before any advance and contractually required to stay in the project until reclassification. State the conclusion and its capital consequence.

### Step 3: Underwrite Property, Market, and Cash Flow

Build in-place NOI first, then the stabilized case, and show both. Do not present the stabilized case alone.

- Rent roll: tenant, suite, SF or units, in-place rent, expiration, options, and rent versus market, with signed-not-commenced rent flagged separately
- Rollover: percentage of rent expiring before maturity and before each extension option, plus the cash cost to re-tenant it at market TI, LC, and downtime
- Expense review: reconcile trailing to budget and to appraisal and state where they diverge and why, testing taxes for reassessment on sale and insurance for renewal shock
- Market: submarket vacancy, absorption, competing construction, and effective rents net of concessions. Challenge the appraisal's market conclusions rather than restating them; restatement is the single most common weakness in a CRE memo.
- Report DSCR, debt yield, LTV, LTC, and break-even occupancy on both cases and name the binding test. Metric definitions and mechanics come from [Underwriting Calculations](knowledge/underwriting-calc.md) and are not restated here.

### Step 4: Work the Repayment Waterfall in Order

The OCC handbook names three tiers and they are not interchangeable. Write a subsection for each.

| Tier | Source | What the memo must prove |
|---|---|---|
| Primary | Property cash flow; for owner-occupied, the occupying business | Coverage from in-place cash flow, with NOI, vacancy, and expense trends, tenant quality and mix, and the effect of scheduled turnover on future coverage |
| Secondary | Guarantors, sponsors, endorsers | Financial capacity and ability to support through payments, curtailments, or re-margining; a guarantee adequate in whole or in part over the remaining term; written and legally enforceable; verified liquidity, global cash flow, contingent liabilities, and the total number and dollar amount of guarantees to all lenders |
| Tertiary | Collateral value | Current and projected vacancy and absorption, lease renewal trends and anticipated rents, effective rents or prices net of concessions, time to stabilized occupancy or sellout, past-due lease volume, and NOI versus budget |

Decision rules for the tiers:

- Where the primary source is satisfactory, the guarantor is supplemental to the rating, not a substitute for coverage. Sponsor comfort that is not a written guarantee gets credit only with documented history of support plus economic incentive, capacity, and stated intent; absent a documented commitment of continued support, do not carry it into the rating.
- Collateral value becomes rating-relevant only once primary and secondary sources are inadequate or questionable. If the memo leans on value early, say so plainly and rate accordingly.
- Owner-occupied test: where 50 percent or more of the primary repayment source comes from third-party unaffiliated income, treat the property as non-owner-occupied and underwrite it as investment CRE.

### Step 5: Stress the Deal and Test the Exit

Supervisory guidance names the variables, not the shocks. State each shock, its basis, and its effect on coverage, leverage, and the exit. Run at minimum:

- Interest rate: index shock plus a refinance rate above the underwriting rate
- Capitalization rate: exit cap above the appraisal's going-in rate, applied to stabilized NOI
- Vacancy and absorption: a downside occupancy path and a slower lease-up; operating expenses: tax reassessment, insurance renewal, and a general expense shock
- Covenant breach: state the NOI, occupancy, or value level at which the DSCR, debt yield, or LTV covenant fails, and how far the base case sits from it
- Exit test: can the loan be refinanced at maturity on stated stress assumptions, or is repayment dependent on sale? Show the paydown required to clear it. An exit that clears only on cap rate compression or rate relief is not an exit; say so in the memo rather than in a footnote.

### Step 6: Set Structure, Covenants, Exceptions, and the Rating

- Covenants and reporting: the common menu for income-producing CRE is debt yield, DSCR, LTV, LTC, and borrower or guarantor minimum net worth or liquidity. For each, state the test, the measurement date, the definition of income and expenses, the cure, and the consequence, and reconcile the covenant DSCR definition to the underwriting DSCR. Scale reporting frequency to stability: annual statements and rent rolls can fit a stabilized, long-leased asset, while lease-up and multi-tenant assets warrant quarterly or monthly. Name who collects and who analyzes.
- Interest-only: if the structure is IO, run the as-if-amortizing coverage test and consider sizing to the balance an equivalent amortizing loan would reach at maturity. Treat an IO renewal, refinance, or extension on stabilized property as a warning sign, not a neutral choice.
- Exceptions: name each one, quantify how it fails to conform, state the mitigant, and note the approval level and reporting path. Supervisory LTV limits are 65 percent raw land, 75 percent land development or improved lots, 80 percent commercial, multifamily, and other nonresidential construction, 85 percent one- to four-family construction, and 85 percent improved commercial, multifamily, and other nonresidential. Loans above them are identified in the records, reported at least quarterly to the board, and counted at full outstanding balance against the 100 percent of total capital aggregate basket and the 30 percent commercial sub-basket. A loan that met the limit at origination and later exceeded it because value fell is not an exception.
- Rating: assign the proposed rating and write the rationale against the institution's own definitions, covering both the obligor's ability and willingness to repay and the loss protection from structure and collateral. If a rationale can be written for re-amortizing a maturing balance, diverting cash flow from the lender to the borrower, that rationale belongs in this memo by name.

### Step 7: Write the Recommendation and Conditions

Close with a recommendation an approver can act on: approve, approve with conditions, decline, or return for restructure. Draft every condition so it can be carried into the loan documents verbatim, separate conditions precedent to closing from ongoing conditions, and hand the ongoing ones to [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md) and the first annual cycle to [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md).

---

## Output Format

```markdown
# CRE Credit Approval Memorandum
## Borrower / Guarantor:
## Property / Collateral / Facility:
## Recommendation: APPROVE | APPROVE WITH CONDITIONS | DECLINE | RETURN FOR RESTRUCTURE
## Proposed Risk Rating:

### Request, Sources, and Uses
| Sources | Amount | Form / Provider / Timing | Uses | Amount |
|---|---|---|---|---|

Structure: amount / facility / purpose / term / amortization / rate / recourse / prepayment / fees
Hard equity: $ / % of cost | HVCRE test (ADC only): PASS | FAIL | N/A

### Property, Market, and Cash Flow
| Metric | In-Place | Stabilized | Basis / Source |
|---|---|---|---|
| Occupancy / NOI | | | |
| DSCR / debt yield | | | |
| LTV (premise: as-is / as-complete / as-stabilized) / LTC | | | |
| Break-even occupancy | | | |

Binding test: | Rollover before maturity: % of rent | Cost to re-tenant: $

### Repayment Sources
| Tier | Source | Evidence | Adequacy |
|---|---|---|---|
| Primary | | | |
| Secondary | | | |
| Tertiary | | | |

### Stress and Exit
| Scenario | Shock and Basis | DSCR | Debt Yield | LTV | Result |
|---|---|---|---|---|---|
| Base | | | | | |
| Rate | | | | | |
| Cap rate / value | | | | | |
| Vacancy, absorption, expense | | | | | |
| Covenant breach point | | | | | |

Exit test at maturity: PASSES | PASSES WITH PAYDOWN $ | FAILS

### Covenants, Reporting, and Policy Exceptions
| Covenant / exception | Test or nonconformity | Measurement / quantification | Cure, mitigant, approval, reporting |
|---|---|---|---|

### Risk Rating Rationale
### Conditions Precedent to Closing and Ongoing Conditions

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The recommendation and proposed rating appear on the first screen, not the last page
- In-place coverage is shown, not only stabilized, the binding test is named, and each repayment tier has its own evidence with collateral not doing work assigned to cash flow
- Guarantor analysis carries verified liquidity, global cash flow, contingent liabilities, and total guarantees to all lenders
- The appraisal review is complete, its value premise matches the LTV reported, and market conclusions are challenged against independent data rather than restated from the appraisal
- Every stress scenario states its shock and basis, and a covenant breach point is identified
- Covenant income and expense definitions reconcile to the underwriting definitions
- Every exception is quantified with a mitigant, an approval level, and a reporting path, and every condition is drafted so it can be lifted into the loan documents unchanged

---

## Red Flags & Dealbreakers

- The loan is sized on stabilized NOI and in-place coverage is never shown or fails, or repayment depends on refinancing or sale with no amortization, no cash flow growth, and no stated paydown, or the exit clears only on cap rate compression or rate relief
- Equity is deferred past the first advance, or consists of developer profit, unearned fees, or accrued land carry
- Loan production ordered or influenced the appraisal, the borrower supplied it, or the memo recommends approval before the review is complete
- Guarantor net worth is quoted with no liquidity, no contingent liabilities, and no tally of guarantees to other lenders, or sponsor comfort with no written, enforceable guarantee is carried into the rating as recourse
- An interest reserve, an IO renewal, or a re-amortization is keeping a stalled project current
- Exceptions are listed but not quantified, not mitigated, or not reported upward, or the memo promises a covenant, reserve, curtailment, or cash management condition that is never drafted as one
- Bank classification and supervisory-limit vocabulary is applied to a debt fund, life company, or CMBS facility not subject to that framework

---

## When Data is Missing

- No completed appraisal review: do not recommend approval. Recommend approval subject to a satisfactory review, and say what would change the conclusion.
- No trailing 12 or current rent roll: underwrite from what exists, label it, and make delivery a condition precedent. No guarantor tax returns or verified liquidity: treat the guarantee as unquantified support and rate the credit on the primary source alone.
- No construction budget, contracts, or feasibility study: the credit is not ready for committee; return for restructure. No submarket data: use the appraisal's data but label it unverified and widen the stress cases.
- Concentration position unknown: flag it and route the portfolio question to [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md). Credit already shows well-defined weaknesses: this is not a new-money memo, so route it to [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md).

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Complete file: appraisal plus completed review, trailing operating statements, current rent roll and leases, verified guarantor financials, independent market data, and the institution's policy and rating scale in hand |
| MEDIUM | Core underwriting is supportable but one input is stale or unverified: an older appraisal, an unaudited operating statement, borrower-asserted liquidity, or market data taken only from the appraisal |
| LOW | Sizing rests on projections without in-place support, the valuation or its review is missing, guarantor capacity is unquantified, or the property and market inputs cannot be reconciled to each other |

---

## Related Knowledge Bases

- [Credit Memo and Appraisal Review Standards](knowledge/credit-memo-and-appraisal-review-standards.md)
- [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md)
- [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md)

## Research Basis

- [Credit Memo Writer Research](research/lender-credit/credit-memo-writer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
