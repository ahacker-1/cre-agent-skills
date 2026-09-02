---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Development Budget and Yield on Cost Analyst

Build or audit a U.S. ground-up or heavy-redevelopment budget, tie it to sources and uses, and test it with untrended and trended yield on cost, development spread, residual land value, profit margin, and overrun sensitivity. This is educational decision support, not legal, tax, investment, accounting, or financing advice; every cost level, cap rate, and escalation figure referenced is directional as of its stated date and must be re-validated against current local pricing and lender feedback.

---

## When to Use This Skill

Use this skill when a development budget needs to be built from scratch, audited before it goes to an investment committee or a construction lender, or re-tested after a bid, a change order, or a repricing. It covers ground-up and heavy redevelopment of income-producing property across multifamily, industrial, retail, office, and mixed-use. Stabilized-asset operating assumptions come from the sector packs; this skill consumes them, it does not restate them. For the acquisition of a standing asset, the pro forma and return work belongs to [Financial Model Builder](skills/underwriting/financial-model-builder.md) and [Scenario Analyst](skills/underwriting/scenario-analyst.md); this skill covers the development cost side those skills do not build.

---

## What You'll Need to Provide

- Draft development budget or pro forma, at whatever level of detail exists
- Site facts: land price or basis, site area, buildable area, unit or bay count, gross and net rentable area, parking type and count
- Design stage (concept, design development, 75% or 90% construction documents, final) and schedule: predevelopment start, construction start, completion, stabilization
- Stabilized income assumptions: market rent, vacancy, other income, operating expenses, replacement reserve, and their source
- Cap rate evidence: submarket, quality-matched going-in cap rate comparables with dates
- Debt and equity terms if known: loan amount or LTC, rate, term, interest reserve, fees, sponsor and LP contributions, developer fee treatment, preferred return
- GC pricing: GMP, schedule of values, allowances, contingency, escalation, alternates
- Business question: go or no-go, land price ceiling, lender submission, IC approval, or rebudget after an overrun

---

## Mission

Produce a budget a lender and an equity partner can both underwrite, a defensible total development cost denominator, and the return math that says whether the project creates value at today's rents, at forecast rents, and under stress.

---

## Strategy

### Step 1: Fix Scope, Basis, and Definitions Before Any Math

- **Total development cost scope.** Use the AvalonBay 10-K definition as the standard: land acquisition, construction, real estate taxes during construction, capitalized interest and loan fees, permits, professional fees, allocated development overhead, other regulatory fees, and first-generation commercial tenant improvements and leasing commissions (AvalonBay FY2025 Form 10-K, filed February 2026).
- **Stabilization definition.** Say which test applies: 90% occupancy (Camden's), or the earlier of 90% occupancy and the one-year anniversary of completion (AvalonBay's and Prologis's). Never compare a stabilization date or a yield across sponsors without checking this.
- **Valuation basis.** As-is, as-complete, and as-stabilized are three different numbers. Yield on cost and margin are stabilized-basis metrics and must be measured against the as-stabilized value (OCC, Comptroller's Handbook: Commercial Real Estate Lending, Version 2.0).
- **Design stage and units of measure.** Design stage sets the honest contingency level and the accuracy you can claim; gross sq ft, net rentable sq ft, unit count, and parking stalls each get defined once and used consistently.

### Step 2: Build or Rebuild the Budget by Group

Rebuild every budget into the groups in [Development Benchmarks](knowledge/development-benchmarks.md) (land and acquisition, hard, soft, FF&E, financing, contingency, developer fee, reserves), then run these integrity tests:

- **Completeness.** Cost estimates must cover land and site improvement, building construction, contractor and developer profit, legal and other professional fees, and loan interest, insurance, and taxes, broken down by phase rather than on a total project basis (FDIC, Examination Modules: Construction and Land Development Lending, October 2025).
- **Hard versus soft classification.** Hard costs are on- and off-site improvements, building construction, general conditions, general contractor fees, bonding and contractor insurance. Soft costs are interest, fees, predevelopment expenses, and related-party developer fees, leasing expenses, brokerage commissions, and management fees where reasonable versus third-party pricing (OCC handbook).
- **Exclusions.** Three items do not belong in a construction budget at all: interest or preferred returns payable to equity partners or subordinated debt holders, the sponsor's general corporate overhead, and selling costs funded out of sale proceeds (OCC handbook). Find them and move them.
- **Escalation as its own line**, escalated to the midpoint of construction from a market study, or by activity where a cost-loaded schedule exists (GSA PBS P-120, November 2022). Do not adopt a national index as the project rate: Turner reported +5.15% year over year in Q2 2026 while RLB reported roughly 1% per quarter with annual city growth from Chicago at 1.42% to Honolulu at 5.93%. Price tariff-exposed scopes separately: structural steel, metal panel and decking, aluminum glazing, copper wiring, switchgear, elevators, rooftop mechanical.
- **Contingency as two separate lines**, design and construction, never buried in unit prices. Design contingency retires as documents complete; scope additions require an approved budget revision, not a contingency draw (GSA P-120).

### Step 3: Run Cost Reasonableness Checks

- **Contingency level.** Two anchors, different bases: private-market construction lender practice is 5% to 10% of the overall budget (OCC handbook); federal owner policy is 7% of cost at award for new capital construction and 10% for modernization or repair and alteration, plus design contingency of 10% at planning, 7.5% to 10% at concept, 5% to 7.5% at design development, 2% to 5% at 75% CDs, 1% to 3% at 90% CDs, and 0% at final CDs, with renovation and complex work higher (GSA P-120). Renovation or adaptive reuse carried at new-construction levels is a systematic under-budget.
- **Cost per unit and per sq ft**, computed on the stated denominators and compared only to same-market, same-product, same-parking comparables. Institutional frames are order-of-magnitude checks, not a basis: AvalonBay's 2025 completions ran $330 to $627 per rentable sq ft, and its 8,572 homes under construction carried about $386,000 per home at December 31, 2025.
- **Line-item interrogation.** Flag any line that is round, blended, missing, or expressed only as a percentage of another line. No sourced market ratio exists for soft cost, FF&E, or developer fee as a share of hard cost; refuse to default one. Name the payee relationship on related-party fees and whether the developer fee is paid current, deferred, or subordinated. Cross-check GC pricing against [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md) and site, entitlement, and impact fee costs against [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md).

### Step 4: Build Sources and Uses and Test the Funding Gap

- Uses equal the total budget from Step 2. Sources equal construction debt plus sponsor equity plus LP equity plus any mezzanine, preferred, grants, tax credits, or land contributed at value.
- Compute loan to cost, loan to as-stabilized value, and the equity requirement. LTC is the loan divided by total cost of the property plus all construction costs (OCC handbook). Program-lender sizing is the lesser of the request, statutory limits, the DSCR-supportable amount, and the ratio-supportable amount; FHA Section 221(d)(4) new construction and substantial rehabilitation sits at 87% LTV/LTC and 1.15x DSCR for market rate, 90% and 1.11x for affordable with a rent advantage (HUD Mortgagee Letter 2025-03, January 8, 2025). Full mechanics belong to [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md).
- **In-balance test.** Undisbursed loan proceeds plus committed unfunded equity must be sufficient to complete the project (FDIC examination module). Compute cost to complete as total estimated cost less cost incurred, the structure Camden discloses ($492.0M estimated against $278.2M incurred on 1,162 homes at December 31, 2025). Confirm the interest reserve was sized to the actual schedule, not an optimistic one, and state what happens to it if delivery slips two quarters. Hand ongoing monitoring to [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md).

### Step 5: Compute the Return Set

Use the conventions in [Underwriting Calculations](knowledge/underwriting-calc.md) for NOI, cap rate, DSCR, and equity multiple, plus these development-specific tests:

| Metric | Formula | Rule |
|---|---|---|
| Untrended yield on cost | Stabilized NOI at today's rents and expenses / total development cost | The controlling test |
| Trended yield on cost | Stabilized NOI at projected delivery-date rents and expenses / total development cost | Forecast; disclose the growth assumption |
| Development spread | (Yield on cost - market cap rate) x 10,000, in basis points | Submarket, quality-matched cap rate only |
| Value creation and margin | Stabilized value - total development cost; that difference divided by total development cost, net of closing costs and taxes where a sale or contribution is planned | Prologis definitions |
| Residual land value | (Stabilized NOI / target yield on cost) - all non-land development costs - required developer profit | Maximum supportable land price |
| Profit multiple | Total equity distributions / total equity contributed | Pair with project and equity IRR |

Report untrended first, always; if the project clears only on trended rents, say so in the verdict line. Directional reference points: Prologis reported a 6.7% weighted average stabilized yield and a 25.4% estimated weighted average margin on 2025 stabilizations, up from 6.2% and 19.2% in 2024 (FY2025 Form 10-K). Practitioner spread conventions published by Realty Capital Analytics (realcapanalytics.com, not MSCI Real Capital Analytics) run roughly 150 to 200 bps multifamily, 175 to 250 bps industrial, 250 to 350+ bps office, and 150 to 200 bps grocery-anchored to 300+ bps speculative retail. Those are conventions, not measured market data, and there is no defensible universal minimum.

### Step 6: Stress the Variables That Break Development Deals, Then Write the Verdict

- **Hard cost overrun**: +5%, +10%, +15% on hard costs, funded by equity. Report yield on cost, spread, margin, and equity multiple at each step, plus the overrun percentage that drives the spread to zero.
- **Rent**: -5% and -10% on stabilized rent, holding expenses flat, plus a case where lease-up runs two quarters longer, using the curve from [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md).
- **Exit cap**: current going-in cap, +50 bps, +100 bps, never below the current going-in cap. CBRE's H1 2026 Cap Rate Survey (published August 12, 2026) found the all-property average essentially flat with roughly 60% of respondents expecting no change over the next six months and more expecting increases than in the prior survey, so a compressing-cap exit needs an explicit argument.
- **Schedule**: delay is a cost line, not only a schedule line, because it compounds through carry, escalation to a later midpoint, and delivery into a different leasing market. Source the case from [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md).

Then state one verdict, the two or three findings driving it, each budget gap in dollars, and what would change the answer. Cost increases do not necessarily result in an increase in value (OCC handbook), so never net an overrun against an assumed value increase. Feed the result into [Development IC Memo Writer](skills/development/development-ic-memo-writer.md).

---

## Output Format

```markdown
# Development Budget and Yield on Cost Analysis
## Project / Product Type / Units / NRSF:
## Design Stage / Stabilization Definition Used:
## Verdict: CLEARS TARGET | MARGINAL | DOES NOT CLEAR | BUDGET NOT UNDERWRITABLE

### Budget Summary
| Group | Amount | % of Total | Per Unit | Per NRSF | Note |
|---|---|---|---|---|---|
| Land and acquisition | | | | | |
| Hard costs (incl. escalation) | | | | | |
| Soft costs | | | | | |
| FF&E and equipment | | | | | |
| Financing costs | | | | | |
| Design contingency | | | | | |
| Construction contingency | | | | | |
| Developer fee | | | | | |
| Reserves | | | | | |
| Total development cost | | 100% | | | |

### Sources and Uses
| Source | Amount | % of Total | Terms / Note |
|---|---|---|---|
| Construction loan | | | LTC: ; LTV as-stabilized: |
| Sponsor and LP equity | | | |
| Total sources | | | In balance vs uses: YES / NO, gap $ |

### Return Metrics
| Metric | Value | Input / Evidence |
|---|---|---|
| Stabilized NOI, untrended / trended | | Growth assumption: |
| Untrended yield on cost | | |
| Trended yield on cost | | |
| Market cap rate used | | Comp source and date: |
| Development spread, untrended | | bps |
| As-stabilized value / value creation / margin | | |
| Residual land value at target YOC | | Target YOC: ; vs land price: |
| Equity multiple / project IRR | | |

### Sensitivity
| Case | Yield on Cost | Spread (bps) | Margin | Equity Multiple |
|---|---|---|---|---|
| Base, untrended | | | | |
| Hard cost +10% | | | | |
| Rent -10% | | | | |
| Exit cap +50 bps | | | | |
| Exit cap +100 bps | | | | |
| Downside combination | | | | |

Break-even hard cost overrun (spread to zero): __%

### Budget Gaps and Unrealistic Line Items
| Line Item | Budgeted | Issue | Estimated Exposure | Next Step |
|---|---|---|---|---|

### Assumptions Requiring Validation
- Rent, expense, and cap rate sources with dates; escalation rate, method, and midpoint; cost estimate basis (concept, GMP, bid)

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Total development cost scope is stated and matches the yield on cost denominator
- Stabilization definition is named before any yield or date is compared
- Untrended yield on cost is reported first and separately from trended, and design and construction contingency appear as two lines with their bases stated alongside a separate escalation line run to the construction midpoint
- Equity preferred returns, sponsor corporate overhead, and sale-funded selling costs are absent from the budget
- Cost per unit and per sq ft are computed on defined denominators and compared to matched comparables
- Sources equal uses, and cost to complete is covered by undisbursed debt plus committed unfunded equity
- The cap rate used for spread and value is submarket-specific, quality-matched, dated, and sourced, and the exit cap is not below the current going-in cap unless the argument is written out
- Every sensitivity case is recomputed, not interpolated

---

## Red Flags & Dealbreakers

- Contingency embedded in unit prices, a single blended contingency line, contingency drawn for owner-directed scope additions, or renovation and adaptive reuse budgeted at new-construction contingency levels
- No escalation line on a build longer than 18 months, escalation applied at the start date rather than the midpoint, or soft cost, FF&E, and developer fee set as a percentage of hard cost with no line-item build
- Equity preferred return, sponsor corporate overhead, or sale-funded brokerage and closing costs sitting inside the construction budget
- The project clears the hurdle only on trended rents, and the trending assumption is not disclosed
- Development spread computed against a national average cap rate, or an exit cap below the current going-in cap with no widening stress case
- Modest or no developer profit in the budget, which leaves inadequate room for cost overruns and is generally not feasible (OCC handbook)
- Cost to complete exceeds undisbursed loan proceeds plus committed unfunded equity
- Interest reserve sized to a schedule the project is already behind, or previously refunded after depletion
- Tariff-exposed scopes carried at pre-2026 pricing, or a fixed-price contract assumed to absorb duty changes without checking its escalation and allowance language
- Cost increases presented as value increases, or residual land value below the contracted land price with no reprice or seller participation identified

---

## When Data is Missing

- If no cost estimate exists above concept level, label the output an order-of-magnitude screen and carry contingency at the top of the design-stage range rather than inventing precision
- If the cap rate has no comparable support, show yield on cost alone and present the spread as a range across a plausible cap band, stating that the spread is unresolved
- If stabilized rents come from a broker pro forma with no comp set, run the return at that rent and at a 10% haircut, and treat the haircut case as the working answer
- If the schedule is missing, do not estimate carry; state that financing costs and escalation are unquantified and that yield on cost and margin are therefore overstated
- If the GC number is allowance-heavy rather than a GMP, list the open allowances and their exposure instead of treating the number as fixed. Never fill a missing line with a percentage rule of thumb; show it as unpriced and quantify what it would take to break the deal

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Design development or later documents with a GMP or hard bid, a dated third-party cost estimate, submarket rent and cap rate comps, a committed debt term sheet, and a schedule tied to the escalation midpoint |
| MEDIUM | Concept or schematic budget with a cost consultant estimate, credible but partly unsupported rent assumptions, indicative debt terms, and a planned rather than contracted schedule |
| LOW | Napkin or sponsor-supplied budget with percentage-based soft costs, no cost estimate, no comp-supported cap rate, or no schedule; treat all yields and margins as directional only |

---

## Related Knowledge Bases

- [Development Benchmarks](knowledge/development-benchmarks.md)
- [Construction Lending Criteria](knowledge/construction-lending-criteria.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Development Budget and Yield on Cost Analyst Research](research/development/development-budget-and-yield-on-cost-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
