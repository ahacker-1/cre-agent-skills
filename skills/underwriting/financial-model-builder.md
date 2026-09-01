---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Financial Model Builder

Build a complete 5-year pro forma and return metrics analysis for a multifamily CRE acquisition from due diligence data.

---

## When to Use This Skill

Use this skill when you have completed due diligence on a multifamily property and need to build the base case financial model. It takes rent roll, operating expense, physical inspection, and market data and produces a fully auditable 5-year pro forma with all key investment metrics — Cap Rate, IRR, Equity Multiple, DSCR, Cash-on-Cash, and Debt Yield. This is the foundation document for scenario analysis and any investment committee memo.

---

## What You'll Need to Provide

- **Rent roll data**: Unit count, unit mix, in-place rents per unit, current occupancy, any active concessions, loss-to-lease (gap between in-place and market rents)
- **Operating expense data**: Validated/adjusted expense line items by category (taxes, insurance, management, payroll, maintenance, utilities, G&A, reserves), stated on a per-unit or total annual basis
- **Physical inspection findings**: CapEx schedule by year, deferred maintenance items, major systems remaining useful life
- **Market data**: Market rents, submarket vacancy rate, rent growth projections (or acknowledge if not available)
- **Deal terms**: Purchase price, loan amount or LTV, interest rate, loan term, amortization period, any interest-only period, hold period (typically 5 years), target exit cap rate
- **Investment thresholds** (optional but recommended): Your minimum DSCR, IRR, equity multiple, cap rate, cash-on-cash, LTV, and debt yield targets
- **Value-add plan** (if applicable): Renovation cost per unit, number of units to renovate per year, expected rent premium per renovated unit

---

## Mission

Build the base case financial model (5-year pro forma) from due diligence data. Calculate all key investment metrics including Cap Rate, IRR, Equity Multiple, DSCR, Cash-on-Cash, and Debt Yield. Produce a complete, auditable pro forma that serves as the foundation for scenario analysis and the IC memo.

---

## Strategy

### Step 1: Build Year 1 Income Schedule

Construct the full income waterfall from validated due diligence data:

```
Gross Potential Rent (GPR)
  Source: rent roll data (in-place rents + loss-to-lease capture)
  - Use validated unit count and in-place rent per unit
  - Annualize: monthly rent x 12 x total units

(-) Loss to Lease Adjustment
  - Current gap between in-place rents and market rents
  - Capture schedule: X% recaptured in Year 1 (from deal terms or default 50%)

(-) Vacancy & Credit Loss
  - Physical vacancy: from market study occupancy data
  - Economic vacancy: credit loss allowance (default 1-2% of GPR)
  - Combined rate applied to GPR

(-) Concessions / Free Rent
  - From rent roll analysis: any active concession programs
  - Annualized concession cost

(+) Other Income
  - Laundry revenue
  - Parking revenue
  - Pet rent / pet deposits (amortized)
  - RUBS (Ratio Utility Billing System) income
  - Late fees, application fees, other ancillary

= Effective Gross Income (EGI)
```

### Step 2: Build Year 1 Expense Schedule

Use the adjusted expenses provided by the user (or validated DD data):

```
Property Taxes
  - Current assessed value or trailing actuals
  - Apply annual escalation rate (from market data or default 2-3%)

Insurance
  - From OpEx analysis (validated/adjusted)

Management Fee
  - % of EGI (from deal terms, typically 5-8%)

On-Site Payroll
  - From OpEx analysis (staffing model)

Maintenance & Repairs
  - From OpEx analysis (per-unit benchmark)

Turnover Costs
  - Per-turn cost x expected annual turns (from occupancy/lease data)

Utilities (owner-paid portion)
  - Net of RUBS recovery

General & Administrative
  - Marketing, legal, accounting, misc

Replacement Reserves
  - Per unit per year (from physical inspection CapEx schedule)

= Total Operating Expenses
```

### Step 3: Calculate Year 1 NOI

```
Net Operating Income = Effective Gross Income - Total Operating Expenses
```

Validate NOI against:
- Seller's stated NOI (note variance)
- Market cap rate implied value
- Per-unit NOI benchmarks from the Multifamily Benchmarks knowledge base

### Step 4: Project Years 2–5

Apply growth assumptions to build multi-year pro forma:

**Revenue Growth:**
- Organic rent growth: from market data projections (e.g., 3% per year)
- Value-add rent premium: from renovation schedule (e.g., $150/unit after renovation)
- Loss-to-lease capture: scheduled reduction over Years 1–3
- Vacancy improvement: if below market, model stabilization trajectory
- Other income growth: tied to occupancy improvement and new programs

**Expense Growth:**
- Default: 3% annual escalation across all categories
- Property taxes: may have reassessment event at acquisition (model step-up)
- Insurance: adjust if market is hardening (4–5%)
- Management: recalculates as % of EGI each year
- Payroll: 3% default
- Reserves: flat or per physical inspection schedule

**Capital Expenditures:**
- From physical inspection CapEx schedule
- Interior renovations: per-unit cost x units renovated per year
- Exterior/common area: scheduled by year
- Deferred maintenance: front-loaded in Years 1–2

### Step 5: Calculate Debt Service

From the deal terms provided:

```
Loan Amount = Purchase Price x LTV
  OR = specific loan amount from deal terms

Monthly Payment = Loan Amount x [rate/12 x (1+rate/12)^(amort_months)] / [(1+rate/12)^(amort_months) - 1]
  If IO period: Monthly Payment = Loan Amount x rate / 12 (during IO)

Annual Debt Service = Monthly Payment x 12
Loan Balance at Exit = remaining principal at Year 5
```

### Step 6: Build Returns Analysis

Reference the Underwriting Calculations knowledge base for exact formulas:

| Metric | Formula |
|--------|---------:|
| **In-Place Cap Rate** | Year 1 NOI / Purchase Price |
| **Stabilized Cap Rate** | Stabilized NOI / Purchase Price |
| **DSCR (by year)** | NOI / Annual Debt Service |
| **Cash-on-Cash (by year)** | (NOI - Debt Service) / Total Equity |
| **Debt Yield** | NOI / Loan Amount |
| **Exit Value** | Year 5 NOI / Exit Cap Rate |
| **Sale Proceeds** | Exit Value - Loan Balance - Closing Costs |
| **IRR (5-year)** | Solve for discount rate: -Equity + Sum(CF/(1+r)^t) + Proceeds/(1+r)^5 = 0 |
| **Equity Multiple** | (Total Cash Flow + Sale Proceeds) / Total Equity |

### Step 7: Compare Against Investment Thresholds

Compare every metric against the thresholds provided by the user (or apply the standard defaults below):

```
FOR each metric:
  IF actual_metric >= threshold: PASS
  ELSE: FLAG as below threshold

Overall verdict:
  ALL PASS → "Base case meets all investment criteria"
  ANY FAIL → "Base case fails on: [list metrics]"
  MARGINAL (within 10% of threshold) → "Base case marginal on: [list metrics]"
```

---

## Output Format

### Required Sections

```markdown
# Financial Model: {Property Name}
## Generated: {date}
## Status: {PASS | FAIL | MARGINAL}

### Model Assumptions
- Purchase Price: $X
- Financing: X% LTV, X% rate, X-year term, X-year amort, X-year IO
- Hold Period: X years
- Exit Cap Rate: X%
- Rent Growth: X% per year
- Expense Growth: X% per year
- Value-Add: {yes/no}, $X/unit, X units/year

### 5-Year Pro Forma

| Line Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|-----------|--------|--------|--------|--------|--------|
| Gross Potential Rent | | | | | |
| (-) Loss to Lease | | | | | |
| (-) Vacancy & Credit Loss | | | | | |
| (-) Concessions | | | | | |
| (+) Other Income | | | | | |
| = Effective Gross Income | | | | | |
| (-) Total Operating Expenses | | | | | |
| = Net Operating Income | | | | | |
| (-) Debt Service | | | | | |
| = Cash Flow Before Tax | | | | | |

### Operating Expense Detail

| Category | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|----------|--------|--------|--------|--------|--------|
| Property Taxes | | | | | |
| Insurance | | | | | |
| Management | | | | | |
| Payroll | | | | | |
| Maintenance | | | | | |
| Turnover | | | | | |
| Utilities | | | | | |
| G&A | | | | | |
| Reserves | | | | | |
| Total OpEx | | | | | |

### CapEx Schedule

| Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|------|--------|--------|--------|--------|--------|-------|
| Interior Renovations | | | | | | |
| Exterior/Common Area | | | | | | |
| Deferred Maintenance | | | | | | |
| Total CapEx | | | | | | |

### Returns Summary

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| In-Place Cap Rate | X% | X% | PASS/FAIL |
| Stabilized Cap Rate | X% | X% | PASS/FAIL |
| Year 1 DSCR | X.Xx | X.Xx | PASS/FAIL |
| Year 1 Cash-on-Cash | X% | X% | PASS/FAIL |
| Debt Yield | X% | X% | PASS/FAIL |
| 5-Year IRR | X% | X% | PASS/FAIL |
| Equity Multiple | X.Xx | X.Xx | PASS/FAIL |

### Exit Analysis
- Exit Value (Year 5 NOI / Exit Cap): $X
- Loan Balance at Exit: $X
- Net Sale Proceeds: $X
- Total Equity Invested: $X
- Total Cash Distributions (Years 1–5): $X
- Total Return: $X

### Key Sensitivities Identified
- [List variables with highest impact on returns]

### Base Case Verdict
{PASS | FAIL | MARGINAL}: {explanation}
```

---

## Quality Checks

Before finalizing the model, run all of the following checks:

**Schema & Completeness**
- All required pro forma line items are present and populated
- All return metrics are calculated
- All assumptions are explicitly stated

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------:|
| noi | > 0 for stabilized; can be negative for value-add | Unexpected sign |
| capRate | 0.02 – 0.15 | Outside range |
| purchasePrice | > 0 | Zero or negative |
| pricePerUnit | $20,000 – $500,000 | Outside range |
| dscr | 0.5 – 5.0 | Outside range |
| ltv | 0.0 – 1.0 | Outside range |
| cashOnCash | -0.10 – 0.50 | Outside range |
| irr | -0.20 – 1.00 | Outside range |
| equityMultiple | 0.5 – 5.0 | Outside range |
| debtYield | 0.0 – 0.30 | Outside range |
| reversion cap rate | >= going-in cap rate | Reversion < going-in |
| NOI | Must equal EGI - OpEx | Arithmetic mismatch |
| DSCR | Must equal NOI / debt service | Arithmetic mismatch |

**Cross-Reference Validation**
- Year 1 NOI is within 15% of seller's stated NOI (flag variance if outside)
- Total OpEx is between 35–55% of EGI (flag if outside range)
- Year-over-year NOI growth is reasonable (0–15%); flag anomalous years
- DSCR never falls below 1.0x in any year (flag as critical risk)
- IRR is between -10% and 40% (flag if outside range, check inputs)
- EGI - OpEx = NOI in every year (recalculate if mismatch)
- Every estimated or assumed value is documented in uncertainty_flags

## Confidence Scoring

Assign an overall confidence level:

| Level | Criteria |
|-------|----------|
| **HIGH** | All input data available and verified; no assumptions required; all calculations cross-checked |
| **MEDIUM** | Minor data gaps filled with reasonable estimates; 1-2 assumptions made; calculations verified |
| **LOW** | Significant data gaps; multiple assumptions required; limited cross-verification possible |

```json
{
  "confidence_level": "HIGH | MEDIUM | LOW",
  "confidence_score": 0.0-1.0,
  "factors": [
    { "factor": "{description}", "impact": "positive | negative", "weight": 0.0-1.0 }
  ],
  "uncertainty_flags": [
    { "field": "{name}", "reason": "{why}", "confidence": "HIGH | MEDIUM | LOW" }
  ]
}
```

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria | Threshold |
|------------|-------------------|-----------|
| DSCR critically low | Base case DSCR falls below 0.80 and the deal does not include a clear value-add thesis | DSCR < 0.80 |

**Standard investment thresholds** (use these if the user has not provided specific targets):

| Metric | Pass | Conditional | Fail |
|--------|------|-------------|------|
| DSCR | >= 1.25 | >= 1.0 | < 1.0 |
| Cap Rate Spread (vs. exit) | >= 100 bps | >= 0 bps | < 0 bps |
| Cash-on-Cash | >= 8% | >= 5% | < 5% |
| Debt Yield | >= 9% | >= 7% | < 7% |
| LTV | <= 75% | <= 80% | > 80% |
| IRR | >= 15% | N/A | < 15% |
| Equity Multiple | >= 1.8x | N/A | < 1.8x |

When a dealbreaker is detected: note it prominently in the output, flag it as CRITICAL severity, and continue the analysis to completion so the IC memo has full data.

---

## When Data is Missing

When required data is unavailable:

1. **Note the gap explicitly** — state what is missing and which output line item it affects
2. **Attempt a workaround** — use alternate calculation methods from the Underwriting Calculations knowledge base, or use conservative industry benchmarks from the Multifamily Benchmarks knowledge base. For financial modeling, bias estimates toward lower returns
3. **State the assumption clearly** — document what estimate was used and why
4. **Mark every estimated value** — add to `uncertainty_flags` with reason and confidence level
5. **Continue the analysis** — use conservative assumptions, note reduced confidence, and flag all gaps in the output

Common fallbacks:
- Missing market vacancy: use submarket average from public market data; default to 5–7% if unavailable
- Missing expense line item: use per-unit benchmark from the Multifamily Benchmarks knowledge base
- Missing CapEx schedule: use $500–$1,000/unit/year as a reserve estimate pending inspection
- Missing market rent data: flag loss-to-lease as unquantified; use in-place rent as conservative proxy

---

## Confidence Scoring Output Schema

Add to the root level of any structured output:

```json
"uncertainty_flags": [
  {
    "field_name": "",
    "reason": "estimated | assumed | unverified | stale_data | interpolated",
    "impact": "Description of what downstream analysis this affects"
  }
]
```

Every estimated, assumed, or unverified value must have a corresponding entry. These flags are consumed by scenario analysis and the IC memo to calibrate their own confidence assessments.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:

- [Underwriting Calculations](knowledge/underwriting-calc.md) — exact formulas for IRR, equity multiple, debt yield, DSCR, and all return metrics
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — per-unit expense benchmarks, market vacancy norms, and cap rate context by market tier
- [Risk Scoring Framework](knowledge/risk-scoring.md) — risk categorization methodology used in the IC memo

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
