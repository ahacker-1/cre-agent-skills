---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Loan Request Screening and Sizing

Screen an incoming U.S. commercial real estate loan request for product and policy fit, size it under every applicable test, identify the controlling test, and return a pursue / pursue with structure / decline verdict with an indicative structure.

---

## When to Use This Skill

Use this skill at intake, when a broker package, borrower request, or relationship officer memo first reaches the credit side and someone has to decide whether the request is worth full underwriting. It answers four questions: does this belong in our book, how much will it actually support, which test binds, and what would have to be added to make it approvable. It is written for bank and credit union credit analysts and underwriters, and for debt fund, life company, agency, and CMBS originations and credit staff. It is educational decision support, not legal, tax, investment, accounting, or financing advice; your institution's board-approved credit policy, delegated authorities, and exception process control over anything here.

This is the credit side of the transaction. The borrower-side mirrors live in other packs: [Office Financing Fit](skills/office/office-financing-fit.md), [Retail Financing Fit](skills/retail/retail-financing-fit.md), and [Industrial Financing Fit](skills/industrial/industrial-financing-fit.md) pick a lender lane for an owner, [Quote Comparator](skills/financing/quote-comparator.md) levels the quotes an owner receives, and [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md) sizes a ground-up request from the developer's seat. Use those when the question is what a borrower should ask for; use this one when the question is what the institution should offer.

---

## What You'll Need to Provide

- The ask: loan amount requested, purpose (acquisition, refinance, cash-out, construction, bridge to stabilization, recapitalization), and requested term, amortization, interest-only period, rate basis, and recourse posture
- Property and income: type, subtype, market, year built, size (units, square feet, keys), occupancy, condition or capital plan; trailing 12 and trailing 3 operating statements; current rent roll with lease expirations; budget or pro forma
- Value and cost: purchase price and sources and uses, or existing basis and payoff; any existing appraisal with its effective date and value type (as-is, as-completed, as-stabilized)
- Sponsor: ownership structure, sponsor and guarantor names, experience with the property type and market, and the proposed guarantee form
- Your institution's parameters: minimum DSCR, minimum debt yield, maximum LTV and LTC by property type, maximum tenor and amortization, interest-only policy, trade area, lending authority levels, and any current property-type, geographic, or concentration sublimits. If these are not supplied, size the request under each test and report proceeds by test rather than issuing a threshold-based verdict.

---

## Mission

Convert an unstructured loan request into a defensible screening decision: the product lane it fits, the proceeds each sizing test supports, the single test that controls, the policy exceptions it would require, and the structure that would make the credit bankable, all traceable to the institution's policy or to a published standard.

---

## Strategy

### Step 1: Intake and Classify the Request

Restate the request in the lender's own terms before analyzing it:

- Purpose, collateral, requested proceeds, requested structure, and requested closing date
- Whether repayment comes primarily from third-party rental income or from an operating business. The 2006 interagency concentration guidance defines CRE loans as those where 50% or more of repayment comes from third-party, non-affiliated rental income or from sale, refinancing, or permanent financing proceeds, and excludes owner-occupied property. An owner-occupied request is a business credit secured by real estate and is screened on the business, not the rent roll.
- Whether the collateral is stabilized, transitional, or construction and land development. Construction and heavy repositioning also carry an HVCRE capital test.
- Whether the request is inside the trade area, inside product policy, and within someone's lending authority

Flag anything here that would end the conversation regardless of the math. A request that is really a renewal, extension, or restructure of an existing credit is not a new-money screen: route it to [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md) or, where the borrower is already in difficulty, to [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md).

### Step 2: Confirm Product and Policy Fit

Match the request to a lane before sizing it, using the lane matrix and structure signatures in [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md). Three fit questions decide it:

- Do the collateral, loan size, and borrower structure qualify for the program at all (agency multifamily and FHA have eligibility gates before any sizing test), and does the lane fund the asset in its current condition (stabilized, transitional, under construction)?
- Does the requested structure match the lane (recourse and covenants for a bank, long fixed low-leverage for a life company, cash management and rigid documents for CMBS, milestones and holdbacks for a bridge)?
- Is the request inside the trade area, inside the property-type and geographic sublimits, and within a delegated approval authority?

Then confirm the portfolio question. The 2006 interagency guidance screens on two criteria, both measured against tier 1 capital plus the allowance for credit losses attributed to loans and leases since March 31, 2020: construction, land development, and other land at 100% or more of that denominator, and total CRE at 300% or more of it combined with 50% or more growth over the prior 36 months. Where the institution is at or approaching either, a request can be declined on portfolio grounds while passing every credit test, and a segment sublimit or the LTV exception basket can bind before the headline ratio does. Hand that analysis to [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md).

### Step 3: Build the Cash Flow and Value Cases

Never size from a single NOI. Build and label at least two, three for transitional deals:

- **In-place NOI**: trailing 12 or annualized trailing 3, occupancy as it stands, no signed-not-commenced rent, no growth
- **Underwritten NOI**: in-place adjusted to lender conventions. The OCC handbook's underwriting conventions are management fees of 3% to 5% of effective gross income for office, retail (exclusive of reimbursements), and industrial and 5% of revenue for multifamily; leasing commissions of 4% of total lease payments for new leases and 2% for renewals; replacement reserves per square foot per year for office, retail, and industrial and per unit per year for multifamily; and multifamily operating expenses usually running 35% to 45% of revenue
- **Stabilized NOI**: transitional requests only, with the cost and time to get there stated

Label the value the same way. Under the Interagency Appraisal and Evaluation Guidelines, the valuation function is independent of loan production and the appraisal or evaluation is reviewed before the final credit decision, so any value used at screening is indicative until that happens. An evaluation is permitted in lieu of an appraisal where the loan amount is $500,000 or less, or for a business loan of $1 million or less where real estate income is not the primary repayment source; a state-certified appraiser is required at $1 million and above, and at $500,000 and above for nonresidential transactions. Detail belongs to [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md).

### Step 4: Run Every Sizing Test and Name the Controlling One

Size the request as the lesser of all applicable tests. HUD states the rule plainly for its programs: the maximum loan is the lesser of the requested amount, the amount allowed by statutory or program limits, the amount supportable by the debt service coverage ratio, and the amount supportable by the applicable loan ratios (Mortgagee Letter 2025-03). Formula definitions live in [Underwriting Calculations](knowledge/underwriting-calc.md) and are not restated in the output.

| Test | Input to use | Note |
|---|---|---|
| LTV | Appraised or indicative value, value type stated | Supervisory limits (85% improved, 80% commercial and multifamily construction, 75% land development, 65% raw land) are ceilings and exception triggers, not targets, and are not a safe harbor |
| LTC | Total verified project cost | Controls on acquisitions above value, construction, and heavy repositioning |
| DSCR | In-place and underwritten NOI, tested as-if amortizing | Lower coverage may be prudent for stable long-term net-leased cash flow; volatile cash flow such as hospitality warrants more |
| Debt yield | In-place NOI first, then underwritten | Independent of rate, amortization, and cap rate; the OCC handbook says use it alongside DSCR and LTV, not instead of them |
| Loan per unit / per SF | Proceeds divided by units or rentable square feet | A basis check against comparable sales and replacement cost, not a published threshold |
| Exit / refinance test | Projected maturity balance against stressed value and coverage | Fannie Mae's published example stresses the exit with a reversion cap at least 2.0% above the initial cap rate and a refinance rate at least 2.25% above its 10-year amortizing underwriting floor |

Report proceeds under each test, then state the controlling test and the gap between requested and supportable proceeds in both dollars and percent.

### Step 5: Test the Requested Structure

Structure is part of the screen, not a later negotiation:

- **Tenor and amortization**: the OCC handbook treats 30 years as a reasonable maximum amortization for income-producing CRE, with 15 to 30 years appropriate in most cases: stabilized multifamily up to 30, office, retail, and industrial generally 25, hospitality generally not more than 20
- **Interest-only**: IO tenors are usually three to five years maximum, coverage is tested as if amortizing, and LTV and coverage standards for IO are generally more conservative than for amortizing loans. The handbook's named mitigant is to originate at the balance the loan would have amortized to at maturity. An IO renewal, refinance, or extension on stabilized property reads as a possible troubled credit.
- **Reserves and recourse**: tax and insurance escrows, replacement reserves, and TI/LC or capital holdbacks sized to the rollover and capital plan, with interest reserves only where policy permits and never repacked; recourse (full, partial principal, payment or carry guaranty, completion guaranty, or non-recourse with standard carve-outs) matched to the risk the property cannot yet carry
- **Covenants**: the handbook's list for income-producing CRE is debt yield, DSCR, LTV, LTC, and guarantor minimum net worth or liquidity. State the measurement date, the NOI definition, and the cure, because covenant coverage can differ from underwriting coverage.
- **HVCRE**: for construction and heavy repositioning, confirm at least 15% of as-completed appraised value contributed before the first advance and LTV at or below the supervisory limit

Where the request depends on the sponsor carrying risk the property cannot, hand the analysis to [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md).

### Step 6: List Policy Exceptions and the Approval Path

Every gap between the request and policy is an exception with a name, a level, and a report line:

- Supervisory LTV exception (origination LTV above the interagency limit for that category), which counts against the aggregate baskets at full outstanding balance
- Internal policy exception: LTV, LTC, DSCR, debt yield, tenor, or amortization outside internal limits, or sponsor liquidity, net worth, or global coverage below minimum
- Structural exception: recourse below policy, deferred equity, IO on stabilized property, interest reserve outside limits
- Documentation exception (missing or stale financials, rent roll, appraisal, or environmental) and pricing exception (coupon or fee below the policy return threshold)

For each, state what it is, why it fails to conform, what mitigates it, and the approval level required. Exceptions permitted only on a limited basis, documented, approved at the right level, and reported to the board is the supervisory expectation, not a formality.

### Step 7: Issue the Verdict and the Indicative Structure

- **Pursue**: fits the lane, clears policy on every test, no exception or one minor documented exception, sponsor and market support it
- **Pursue with structure**: supportable at reduced proceeds or with added structure (lower leverage, amortization, reserves, recourse, covenants, or a shorter term). Say exactly what changes and what it costs the borrower in proceeds.
- **Decline**: no lane fits, the controlling test cuts proceeds below what the request needs to function, the exception stack exceeds what the exception process should carry, portfolio limits are full, or the exit is not credible

Then write the indicative structure: proceeds, term, amortization, IO, rate basis, reserves and escrows, recourse, covenants, and the conditions that would have to be verified. What survives this step feeds [Credit Memo Writer](skills/lender-credit/credit-memo-writer.md), and the covenants set here become the monitoring set for [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md).

---

## Output Format

```markdown
# Loan Request Screen
## Borrower / Sponsor:
## Property / Market:
## Request: $ | Purpose | Term | Amortization | IO | Recourse
## Verdict: PURSUE | PURSUE WITH STRUCTURE | DECLINE
## Controlling Test:

### Product and Policy Fit
- Lane / program eligibility:
- Property type, subtype, condition:
- Trade area and approval authority:
- Concentration and sublimit headroom:

### Cash Flow and Value Cases
| Case | NOI | Basis | Notes |
|---|---|---|---|
| In-place | | | |
| Underwritten | | | |
| Stabilized (if transitional) | | | |
| Value used | | As-is / as-completed / as-stabilized | Appraisal status and effective date |

### Sizing Tests
| Test | Threshold Used | Source of Threshold | Supportable Proceeds | Binding? |
|---|---|---|---|---|
| LTV | | | | |
| LTC | | | | |
| DSCR (as-if amortizing) | | | | |
| Debt yield (in-place) | | | | |
| Loan per unit / per SF | | | | |
| Exit / refinance test | | | | |

Requested: $ | Supportable: $ | Gap: $ ( %)

### Policy Exceptions
| Exception | Category | How It Fails to Conform | Mitigant | Approval Level |
|---|---|---|---|---|

### Indicative Structure
- Proceeds / term / amortization / IO / rate basis:
- Reserves, escrows, holdbacks:
- Recourse:
- Covenants (test, measurement date, cure):
- Conditions to verify:

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Every ratio states which NOI (in-place, underwritten, stabilized) and which debt service (actual, as-if amortizing, floor rate) it used, and the value carries a type and an appraisal status so an indicative value is never presented as an appraised value
- All applicable tests are run and the lowest proceeds figure is the sizing answer, with the controlling test named
- Interest-only requests are coverage-tested as if amortizing, and any leverage reduction is shown
- Thresholds are attributed to institutional policy or a published program grid, never to a market average, and market figures carry a date and a source
- Exceptions are enumerated with category and approval level, and concentration and sublimit headroom is checked before the verdict, not after

---

## Red Flags & Dealbreakers

- Proceeds sized to stabilized NOI or as-stabilized value while in-place cash flow fails coverage, with no reserve, holdback, or guaranty bridging the gap, or a request that only works interest-only and fails coverage the moment an amortizing payment is applied
- Sizing to the supervisory LTV limit as if it were a target, or treating conformity with it as evidence the loan is sound
- Cash-out proceeds that raise basis above a defensible value while income is flat or declining, or an exit that depends on cap rate compression or rate relief rather than amortization and cash flow growth clearing a stated refinance test
- Equity deferred past the first advance, or composed of deferred developer profit, unearned fees, or accrued land carry; or guarantor liquidity taken from an unverified personal financial statement
- A major tenant or a large share of rent expiring before maturity with no reserve, signed renewal, or reduction in proceeds
- A stack of exceptions across leverage, coverage, structure, and pricing on a single request, which is a decline dressed as a structuring exercise

---

## When Data is Missing

- No institutional thresholds: size under each test at a stated range of assumptions, present proceeds by test, and withhold the verdict rather than inventing a policy minimum
- No appraisal: use an indicative value, label it, make the ordered and reviewed appraisal a condition, and do not compute a final LTV from a borrower-supplied value
- No trailing operating statements: underwrite from the rent roll with conservative expense conventions and mark the NOI as unverified; with no rent roll or expiration schedule, treat rollover risk as unquantified and credit no renewal assumptions
- No sponsor financials: screen the property only and state that the sponsor test is unrun
- Sources and uses incomplete, or no environmental, structural, or capital plan information: LTC cannot be computed and reserve sizing is preliminary; say so rather than defaulting to LTV alone

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Trailing 12 and trailing 3 statements, current rent roll, sources and uses, sponsor financials, and a current appraisal or credible value support are available; institutional thresholds are known; all tests run and reconcile |
| MEDIUM | Core operating and rent data available but one of appraisal, sponsor financials, or capital plan is missing or stale; thresholds partly known; proceeds range stated |
| LOW | Broker package or pro forma only, no verified in-place cash flow, no value support, or no institutional thresholds; output is an indication of proceeds by test, not a screening verdict |

---

## Related Knowledge Bases

- [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Loan Request Screening and Sizing Research](research/lender-credit/loan-request-screening-and-sizing-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
