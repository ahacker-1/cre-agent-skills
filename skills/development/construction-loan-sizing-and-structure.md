---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Construction Loan Sizing and Structure

Size a U.S. construction loan against every controlling test, quantify the cash equity requirement, structure the interest reserve, guaranty package, draw controls, and takeout, and produce a structure recommendation with a lender-lane fit.

---

## When to Use This Skill

Use this skill when a development budget is firm enough to finance: before a term sheet is requested, when comparing quotes from different lender lanes, when an equity partner asks how much cash the deal actually needs, when a term sheet needs to be read against what the project can survive, or when a construction loan is being resized after a budget or schedule change.

This is educational decision support, not legal, tax, investment, accounting, or financing advice. Confirm live appetite, proceeds, covenants, and legal terms with active lenders and counsel. Bank supervisory thresholds cited below apply to U.S. banks and savings institutions; non-bank lenders are not bound by them.

This skill sits in the borrower's seat. The same request from the institution's credit side belongs to [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md). For permanent debt on a stabilized asset, [Quote Comparator](skills/financing/quote-comparator.md) levels competing quotes and [Term Sheet Builder](skills/financing/term-sheet-builder.md) formalizes the selected one; use those rather than this skill once construction risk is gone.

---

## What You'll Need to Provide

- Total development budget by line item, with hard costs, soft costs, contingency, developer fee, financing costs, and reserves shown separately
- Stabilized pro forma: NOI at stabilization, the rent and expense assumptions behind it, and whether it is trended or untrended
- Appraisal or valuation support: as-is, as-complete, and as-stabilized value opinions if available, and the cap rate evidence behind them
- Construction schedule and lease-up or absorption assumptions, with the delivery date and the stabilization definition being used
- Entitlement status and remaining permit conditions, from [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md) or equivalent
- Equity stack: cash equity, land basis and how it was acquired, deferred fees, preferred equity or mezzanine, and when each dollar funds
- Term sheet or quote if one exists: LTC, LTV, rate and index, term and extensions, reserves, guaranties, covenants, fees
- Sponsor and guarantor financials: net worth, liquidity, contingent liabilities, and track record on comparable product
- The construction contract type and whether contractor and borrower are related
- The business question: how much can we borrow, how much cash do we need, which lender lane, or is this term sheet acceptable

---

## Mission

Determine the largest defensible loan amount, name the test that controls it, quantify the resulting cash equity gap, structure the reserves, guaranties, and draw controls that make the loan survivable through completion and lease-up, and state which lender lane the deal actually fits.

---

## Strategy

### Step 1: Frame the Project and Identify the Lender Lane

Before any math, establish what kind of lender can hold this loan. The constraint set changes entirely.

| Lane | Fit | Binding constraints to expect |
|---|---|---|
| Relationship bank | Sponsor with deposits and track record, moderate leverage, conventional product | Supervisory LTV limits, HVCRE capital treatment, C&D concentration, sponsor guaranties |
| Debt fund / private credit | Speculative product, higher leverage, complex or transitional story, speed | Higher coupon and fees, tighter milestones, heavier reserves, no supervisory ceiling |
| Life company construction-to-perm | Pre-leased or credit-tenant product, long hold, single closing | Low leverage, conservative stabilized underwriting, conditions to the permanent conversion |
| HUD Section 221(d)(4) | Multifamily new construction and substantial rehab, long timeline tolerated | Published program criteria, Davis-Bacon, cost certification, processing duration |

Note the lender's own balance sheet, not just the deal. OCC Bulletin 2006-46 (2006-12-06) screens banks for further supervisory analysis at construction, land development, and other land loans of 100% or more of total risk-based capital, and at total non-owner-occupied CRE of 300% or more with 50% or greater growth over 36 months. Those are screens, not caps, but they explain a decline that has nothing to do with the project. Directional and dated: the FDIC Quarterly Banking Profile for Q2 2026 reported bank C&D balances of $453.5 billion, down 3.4% year over year, and CBRE reported on 2026-08-03 that alternative lenders took 38% of Q2 2026 non-agency closings against banks at 30%. Re-validate current appetite in [Construction Lending Criteria](knowledge/construction-lending-criteria.md).

### Step 2: Run Every Sizing Test and Take the Minimum

Compute all five. The loan is the lowest result. Show every number, not just the winner.

| Test | Formula | Notes and sourced limits |
|---|---|---|
| LTC | Loan / total development cost | Lender policy, quote-driven. The OCC Comptroller's Handbook directs banks to set LTC limits alongside LTV so the borrower contributes real equity, but prescribes no level. Do not default one |
| LTV as-complete | Loan / as-completed appraised value | For banks, the Interagency Guidelines for Real Estate Lending Policies set supervisory limits of 80% for commercial, multifamily, and other nonresidential construction, 85% for 1-4 family residential construction, 75% for land development, 65% for raw land. A multi-phase loan takes the limit for the final phase funded |
| LTV as-stabilized | Fully funded loan / as-stabilized value | Governs the refinance exit. Stress the exit cap rate; do not assume compression |
| DSCR at stabilization | Stabilized NOI / permanent-loan debt service | Lender-specific for conventional debt. HUD publishes minimums (below) |
| Debt yield at stabilization | Stabilized NOI / fully funded loan | Independent of rate, amortization, and cap rate. Often binds when exit values are uncertain. Threshold is lender-specific |

Loan = min(LTC result, as-complete LTV result, as-stabilized LTV result, DSCR result, debt yield result).

Published reference grid, HUD Section 221(d)(4) new construction and substantial rehabilitation, per Mortgagee Letter 2025-03 (2025-01-08): market rate or LIHTC without rent advantage at 87% LTV/LTC, 1.15 DSCR, 7% vacancy factor; LIHTC affordable with rent advantage at 90%, 1.11, 5%; properties with 90% or greater units carrying rental assistance at 90%, 1.11, 3%. HUD sizes the loan as the lesser of the requested amount, statutory limits, the DSCR-supportable amount, and the ratio-supportable amount. Use it as a reference lane, not as a conventional benchmark.

Then run three stresses and report which test controls under each: exit cap rate widened 50 and 100 bps; stabilized NOI down 10%; delivery six months late with lease-up starting into a later market. Pull the cost and yield inputs from [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md) and the absorption assumptions from [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md).

### Step 3: Compute the Equity Requirement and Test HVCRE Separately

Equity first, and cash equity separately from total contributed capital. These are different questions and a deal can pass one while failing the other.

- Cash equity requirement equals total development cost minus the controlling loan amount, plus any non-mortgageable costs and out-of-pocket reserves the lender will not fund
- Timing: the OCC handbook states bank policy should require equity contributed before construction loan disbursements begin, and that deferring it "can significantly increase completion risk"
- Form: deferred developer profit, unearned developer fees, incurred overhead, and interest or holding fees paid or accrued on contributed land are generally not equity. Cash, marketable securities, land purchased with cash, and up-front architect, engineering, and permit costs generally are. A guarantor's unpledged assets are not a substitute for project equity
- If land is contributed at appreciated value, state the appraised contribution and the cash actually invested as two separate lines

For a bank lender, run the HVCRE test on top. Under the December 2019 HVCRE final rule, effective 2020-04-01, an ADC exposure carries a 150% risk weight unless it qualifies for an exclusion. The commercial real property exclusion requires all four: LTV at or below the applicable supervisory LTV ratio; borrower-contributed capital of at least 15% of the property's appraised as-completed value; that capital contributed before the bank advances funds other than nominal lien-securing sums; and a contractual requirement that it remain in the project until reclassification, which requires substantial completion plus cash flow covering debt service and expenses under the bank's own permanent-financing standards. Each financed phase generally needs its own as-completed appraisal to be a separate project for the test. Flag it when the 15% test passes on contributed land value while cash at risk is thin: that is a capital-treatment pass, not an alignment pass.

### Step 4: Size the Interest Reserve and the Carry Reserve

Model the reserve; do not ratio it.

- Build the draw curve from the schedule, apply the rate (index plus spread, plus any cap or floor), and carry interest through anticipated completion and lease-up, sale, or occupancy
- Stress the inputs the OCC handbook names: potential interest-rate changes, timing of disbursements and paydowns, and time required for completion and lease-up. Add the six-month delay case from Step 2
- Ask whether the lender could fund interest within its LTC and LTV limits if the borrower stopped paying it from its own funds. If not, the reserve is understated
- Apply project cash flow to interest before the reserve during lease-up; once cash flow covers interest, reserve draws should stop
- Confirm whether a separate carry reserve or carry guaranty covers operating expenses, taxes, insurance, and utilities during lease-up. These are different line items and a term sheet may provide only one
- Treat a plan to replenish a depleted reserve with new loan proceeds as a credit-deterioration signal, not a budget amendment; supporting a repack calls for a new appraisal or evaluation and a fresh feasibility review
- Interest reserves are generally inappropriate for stabilized properties or speculative raw land. The OCC handbook is explicit that "the presence of an interest reserve may not accurately reflect a borrower's ability to pay"; a funded reserve is a budget line, not coverage

### Step 5: Structure the Guaranty Package and Recourse Posture

Name each guaranty, what it covers, its cap, and the measurable test that releases it.

| Guaranty | Covers | Release or burn-off |
|---|---|---|
| Completion | Lien-free completion by an outside date substantially per lender-approved plans | Capped at the amount needed to complete less undisbursed loan proceeds and balancing reserves. Released on completion plus expiry of the statutory mechanics lien filing period, and on repayment in full |
| Carry | Operating and maintenance costs, taxes, insurance, utilities while cash flow is insufficient | Repayment in full, or the property reaching a stipulated DSCR or debt yield test. Often a post-foreclosure tail of thirty days to one year |
| Repayment | All or a stated portion of principal | Repayment in full, or reduction and burn-off on agreed thresholds such as a sustained DSCR. Foreclosure or deed in lieu does not release it |
| Non-recourse carve-out | Fraud, misrepresentation, voluntary or collusive bankruptcy, unapproved liens, waste, prohibited transfers, diversion of funds | Effectively performed on repayment. Distinguish full-recourse triggers from loss-only triggers; certain acts survive foreclosure |
| Environmental indemnity | Environmental conditions and claims | Often a sunset one to three years after repayment or transfer, conditioned on a clean current report and no outstanding claim |

Decision rules:

- For every burn-off, capture the exact metric, who measures it, on what schedule, and whether the lender must test and document it. An untested burn-off leaves the guaranty in place
- Where multiple guarantors sign, confirm several rather than joint and several liability, and confirm replacement-guarantor standards are stated in the documents rather than left to lender discretion
- Verify guarantor liquidity and net worth against the completion and carry exposure, not against the loan amount
- Price the recourse tradeoff explicitly. Practitioner commentary (Commercial Property Executive, 2018-10-17) frames it directionally: a recourse lender might offer 70% loan to cost where a non-recourse lender caps near 50%, at higher pricing. That is a dated characterization, not a quote. Compute both cases against the actual budget and see which the sponsor can fund

### Step 6: Set the In-Balance Test, Draw Controls, and Retainage

The in-balance test, run at every draw:

Remaining loan commitment + unfunded borrower equity + remaining contingency must be at least cost to complete + remaining interest and carry.

If it fails, the loan is out of balance and the borrower funds the gap before further advances. Confirm the loan documents say exactly that, and who determines cost to complete.

Controls to confirm in the loan agreement:

| Control | Standard to confirm |
|---|---|
| Draw support | Architect or engineer inspection report with each draw; percentage-complete verified independent of the lending function; inspections on an irregular schedule and before draw requests |
| Lien protection | Lien waivers or releases from subcontractors and suppliers before disbursement, lien searches, and a title update with each draw. Whether mechanics liens can prime the mortgage is state-specific and is a counsel item |
| Retainage | Commercial progress payment plans typically hold back 10% to 20% of each payment |
| Final draw | Holdback released only after all lien waivers, a final inspection confirming completion to specification, and a certificate of occupancy |
| Contingency and fees | Contingency typically 5% to 10% of the overall budget, with overruns from poor projections or management ordinarily borrower-funded; developer fee, distinct from developer profit, typically does not exceed 4% of project cost and is often deferred or paid on percentage of completion, while developer profit is funded by sales, by loan funds on completion and lease-up, or by term financing, not during construction |
| Contract and change orders | A fixed-price contract mitigates overrun risk; where borrower and contractor are related the contract should be cost plus a fee with a guaranteed maximum price, and such a contractor generally cannot be bonded. Change orders reviewed by qualified staff or a consultant, approved and documented by the lender and any take-out lender, and reflected in the budget |

Front loading, where the builder overstates the cost of early-stage work, is the failure mode these controls exist to catch. Undetected, it leaves insufficient funds to complete on default. Route contract terms to [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md) and ongoing draw testing to [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md).

### Step 7: Test Tenor, Extension, Mini-Perm, and Takeout, Then Recommend

- Tenor should cover construction plus stabilization or sale and never be shorter than the time required for completion. A common structure runs construction financing into a bridge or mini-perm facility for the stabilization period; the OCC handbook notes bridge loans are usually written for up to three years
- Extension option length should match expected construction time plus projected absorption. For each extension, list the test, the measurement date, the fee, and who calculates it. Typical tests combine completion, a minimum DSCR or debt yield, an occupancy or leasing threshold, and no default. Model the case where one test misses and say what happens
- Classify the takeout: firm forward commitment, standby, loan assumption, sale, or refinance into an unidentified market. A standby is priced to discourage use; a forward requires completion and is almost always conditioned on lease-up to break even or better at minimum rents, and the OCC handbook warns such commitments "may mitigate little of the risk" the construction lender assumes. Where a third-party takeout is relied on, confirm counsel review of the agreement, the permanent lender's financial capacity, a tri-party buy and sell agreement executed before the construction loan closes, and an automatic completion-date extension for delays beyond the builder's control
- Where preleasing or presale is a condition, confirm the commitments are bona fide with meaningful deposits collected, and cross-check the schedule against [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md)

Close with a single recommended structure: loan amount, controlling test, cash equity requirement, reserve sizing, guaranty package, and lender lane, plus the one change that would most improve proceeds or reduce risk. Feed the result into [Development IC Memo Writer](skills/development/development-ic-memo-writer.md).

---

## Output Format

```markdown
# Construction Loan Sizing and Structure
## Project:
## Product Type / Units or SF:
## Total Development Cost:
## Verdict: FINANCEABLE AS PROPOSED | FINANCEABLE WITH RESTRUCTURE | EQUITY GAP | NOT FINANCEABLE AS STRUCTURED

### Sizing Stack
| Test | Input | Assumed Threshold | Indicated Loan | Controls? |
|---|---|---|---|---|
| LTC | | | | |
| LTV as-complete | | | | |
| LTV as-stabilized | | | | |
| DSCR at stabilization | | | | |
| Debt yield at stabilization | | | | |
| **Recommended loan (minimum)** | | | | |

### Stress Cases
| Case | Controlling Test | Indicated Loan | Equity Gap |
|---|---|---|---|
| Base / exit cap +50 bps / exit cap +100 bps / NOI -10% / delivery +6 months | | | |

### Equity and Contributed Capital
| Item | Amount | Form | Funded When |
|---|---|---|---|
| Cash equity / land contribution / other contributed capital / total | | | |

HVCRE 15% test (bank lenders only): PASS / FAIL / N/A. Contributed capital as a share of as-complete value:

### Reserves
| Reserve | Modeled Requirement | Term Sheet | Adequate Under Delay Case? |
|---|---|---|---|
| Interest / carry / operating deficit | | | |

### Guaranty Package and Recourse
| Guaranty | Cap | Burn-off Test | Measured By | Assessment |
|---|---|---|---|---|

### In-Balance, Draw Controls, Extension, and Takeout
| Item | Term Sheet Position | Adequate? | Risk if Missed |
|---|---|---|---|
| In-balance test | | | |
| Retainage, lien waivers, title updates, inspections | | | |
| Contingency vs cost to complete | | | |
| Extension tests, fees, mini-perm conversion | | | |
| Takeout plan | | | |

### Structure Recommendation
- Recommended lender lane:
- Recommended loan amount and controlling test:
- Cash equity requirement:
- Highest-impact change:

### Open Items
| Item | Why It Matters | Who Answers |
|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- All five sizing tests are computed and shown, the controlling test is named, and the recommended loan equals the minimum rather than the LTC result alone
- Cash equity is stated separately from total contributed capital, and land contribution shows appraised value and cash basis as two lines
- Supervisory LTV limits and HVCRE treatment are applied only to bank lenders and labeled as such
- The interest reserve is modeled from the draw curve and schedule, not set as a percentage
- Every guaranty burn-off names a measurable test, a measurement date, and who calculates it
- The in-balance test is written as an inequality with each term defined
- Stabilized NOI is identified as trended or untrended, and the exit cap rate carries evidence
- Every dated market figure carries its source and date and is labeled directional, and all numbers reconcile to the development budget and the stabilization pro forma

---

## Red Flags & Dealbreakers

- Loan sized to stabilized NOI or stabilized value while the in-balance test already fails at current cost to complete
- Deferred developer profit, unearned fees, accrued land carry, or a guarantor's unpledged net worth presented as project equity, or equity deferred to fund after construction draws begin with no proof it remains available
- Contributed land at appreciated value clearing the 15% HVCRE test with little cash at risk
- Interest reserve sized to the base schedule only with no delay case, a plan to replenish it with new loan proceeds, or only an interest reserve where the project also needs operating carry through lease-up
- Guaranty burn-off assumed in the model but never tested or documented by the lender, or a burn-off test the sponsor does not control
- Retainage below the customary range, no lien waiver or title update condition, or percentage-complete verified by the party requesting the draw
- Contingency largely consumed while the schedule has slipped
- Extension test that depends on a leasing pace the submarket is not delivering, with no fallback capital
- Takeout treated as certain when it is a standby, is conditioned on rents the project has not reached, or has no tri-party agreement
- A phase loan treated as conforming without a phase-level as-completed appraisal, or a modification that increases the loan, changes scope, or releases contributed capital without re-testing HVCRE
- Bank leverage assumed without checking whether that lender is near its own C&D or CRE concentration screens

---

## When Data is Missing

- If no appraisal exists, size from cost and stabilized NOI, state that both LTV tests are unrun, and cap confidence at MEDIUM
- If the stabilized pro forma is trended only, run the untrended case as the controlling case and show both
- If the term sheet is absent, size the loan on stated tests and label every threshold as an assumption to be confirmed, not a market standard
- If the draw schedule is unavailable, model a straight-line and an S-curve draw and report the interest reserve range rather than a point number
- If guarantor financials are missing, do not credit the guaranty package; flag completion and carry exposure as unsupported
- If the construction contract type is unknown, do not assume fixed price; test the budget as if overruns are borrower-funded
- If the lender type is unknown, run the bank case and the non-bank case side by side, because the supervisory and HVCRE constraints apply only to one

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Firm budget, appraisal with as-complete and as-stabilized opinions, executed or draft term sheet, draw schedule, guarantor financials, and a stabilization pro forma with submarket rent evidence |
| MEDIUM | Budget and pro forma available but appraisal, term sheet, or draw schedule is missing, or thresholds are assumed rather than quoted |
| LOW | Cost or NOI estimated, no valuation support, no lender indication, or a schedule and lease-up plan that has not been tested |

---

## Related Knowledge Bases

- [Construction Lending Criteria](knowledge/construction-lending-criteria.md)
- [Construction Contracts and Draw Controls](knowledge/construction-contracts-and-draw-controls.md)
- [Development Benchmarks](knowledge/development-benchmarks.md)

## Research Basis

- [Construction Loan Sizing and Structure Research](research/development/construction-loan-sizing-and-structure-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
