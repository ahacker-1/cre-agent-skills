# Operating Expense Analyst

Analyzes trailing 12-month operating expenses, benchmarks each category against market standards, identifies anomalies and understated items, and produces an adjusted expense schedule for underwriting.

---

## When to Use This Skill

Use this skill when you have a seller's T-12 income statement and need to stress-test the reported expenses before making an acquisition decision. It is most valuable during due diligence when you want to identify understated costs (missing management fee, no reserves), adjust for one-time items, and arrive at a realistic NOI for underwriting.

---

## What You'll Need to Provide

- **T-12 financials** — monthly expense data by category for the trailing 12 months
- **Seller's P&L or income statement** — as provided by the seller or broker
- **Property details** — address, unit count, total rentable square footage, year built, property class (A/B/C), and type
- **Effective Gross Income (EGI)** — needed to calculate expense ratios (can be derived from rent roll if not separately provided)

---

## Mission

Analyze trailing 12-month operating expenses. Benchmark against market standards. Identify expense anomalies, understated items, and optimization opportunities. Produce an adjusted expense schedule that reflects realistic operating costs for underwriting.

---

## Strategy

### Step 1: Parse T-12 Expense Categories

- Read T-12 financials from the provided data
- Map seller categories to standard chart of accounts:

| Standard Category        | Common Seller Labels                                    |
|--------------------------|---------------------------------------------------------|
| Property Taxes           | Real estate taxes, ad valorem taxes                     |
| Insurance                | Property insurance, liability, umbrella                 |
| Utilities                | Electric, gas, water/sewer, trash                       |
| Repairs & Maintenance    | R&M, maintenance, make-ready, turns                     |
| Contract Services        | Landscaping, pest control, elevator, fire/life safety   |
| Payroll                  | On-site staff, manager, maintenance tech, leasing       |
| Management Fee           | Property management, management company                 |
| Marketing                | Advertising, ILS, signage, website                      |
| Administrative           | Office supplies, legal, accounting, telephone            |
| Turnover/Make-Ready      | Unit turns, carpet, paint, appliance replacement        |
| Capital Reserves         | Replacement reserves, CapEx reserves                    |

- Total each category across 12 months
- Identify any months with missing data

### Step 2: Calculate Per-Unit and Per-Sqft Metrics

For each expense category:
- `per_unit_annual = category_total / total_units`
- `per_sqft_annual = category_total / total_rentable_sqft`
- `pct_of_egi = category_total / effective_gross_income * 100`

Aggregate metrics:
- `total_opex_per_unit = total_expenses / total_units`
- `total_opex_per_sqft = total_expenses / total_rentable_sqft`
- `expense_ratio = total_expenses / effective_gross_income * 100`

### Step 3: Benchmark Against Standards

Compare each category to benchmarks from the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md):

| Category              | Benchmark Range (per unit/year) | Variance Threshold |
|-----------------------|---------------------------------|--------------------|
| Property Taxes        | Market-specific                 | +/- 15%            |
| Insurance             | $400 - $1,200                   | +/- 20%            |
| Utilities             | $800 - $2,400                   | +/- 20%            |
| Repairs & Maintenance | $600 - $1,500                   | +/- 25%            |
| Contract Services     | $200 - $600                     | +/- 25%            |
| Payroll               | $800 - $2,500                   | +/- 20%            |
| Management Fee        | 3% - 8% of EGI                 | Must be >= 3%      |
| Marketing             | $100 - $500                     | +/- 30%            |
| Administrative         | $200 - $600                     | +/- 25%            |
| Turnover              | $300 - $1,000                   | +/- 25%            |
| Capital Reserves      | $250 - $500                     | Must exist         |

Flag categories outside benchmark ranges with direction (ABOVE/BELOW).

### Step 4: Identify Anomalies

| Anomaly Type                | Detection Rule                                           | Severity |
|-----------------------------|----------------------------------------------------------|----------|
| Missing category            | Standard category has $0 or is absent                    | HIGH     |
| Understated management fee  | Management fee < 3% of EGI                               | HIGH     |
| No replacement reserves     | Reserves = $0 or absent                                  | HIGH     |
| No turnover budget          | Turnover/make-ready = $0                                 | HIGH     |
| Expense spike               | Any month >2x the trailing average for that category     | MEDIUM   |
| Expense cliff               | Any month <50% the trailing average for a category       | MEDIUM   |
| Suspiciously low taxes      | Per unit below county average by >25%                    | HIGH     |
| One-time charges            | Large non-recurring expenses inflating categories        | MEDIUM   |
| Owner-managed discount      | Owner-managed with no imputed management fee             | HIGH     |
| Missing insurance lines     | No flood, no liability, or no umbrella in flood zone     | MEDIUM   |

### Step 5: Research Local Cost Factors

Via web research:
- **Property Taxes**: Search `"{county}" property tax rate {year}` and `"{property address}" tax assessment`
  - Verify current assessment vs expected reassessment at purchase price
  - Calculate potential tax increase: `new_tax = purchase_price * local_mill_rate`
- **Insurance**: Search `"multifamily insurance cost" {state} {year}` and check for catastrophe zone premiums
- **Utilities**: Search `"{utility provider}" {city} rates` for electric, gas, water/sewer
  - Determine if owner-paid or tenant-paid for each utility
  - Estimate RUBS recovery potential

### Step 6: Flag Understated Expenses

Common understated items to check:

| Item                     | Check                                                      |
|--------------------------|-------------------------------------------------------------|
| Management fee           | Impute at market rate (typically 5-7%) if owner-managed     |
| Property taxes           | Recalculate at expected reassessed value                    |
| Insurance                | Verify adequate coverage; check for rate increases          |
| Payroll                  | Verify staffing levels match property size                  |
| Capital reserves         | Impute $250-$500/unit/year if missing                       |
| Turnover costs           | Impute based on historical turnover rate                    |
| Marketing                | Impute if property relies on word-of-mouth only             |
| Legal/eviction costs     | Impute if tenant quality suggests eviction needs            |

### Step 7: Produce Adjusted Expense Schedule

Build two schedules:
1. **Seller's T-12** (as reported)
2. **Adjusted T-12** (buyer's underwriting)

For each line item in the adjusted schedule, provide:
- Adjusted amount
- Adjustment direction (UP/DOWN/NONE)
- Adjustment amount ($)
- Justification (one sentence)

Calculate:
- **NOI Impact**: Seller's NOI vs Adjusted NOI
- **Expense Ratio**: Adjusted total expenses / EGI
- **OpEx per unit**: Adjusted total / unit count

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "t12_summary": {
    "period": "MM/YYYY - MM/YYYY",
    "total_revenue": 0,
    "total_expenses": 0,
    "noi_as_reported": 0,
    "expense_ratio_pct": 0,
    "opex_per_unit": 0,
    "opex_per_sqft": 0
  },

  "expense_categories": [
    {
      "category": "Property Taxes",
      "t12_actual": 0,
      "per_unit": 0,
      "per_sqft": 0,
      "pct_of_egi": 0,
      "benchmark_low": 0,
      "benchmark_high": 0,
      "benchmark_status": "WITHIN | ABOVE | BELOW",
      "variance_pct": 0,
      "monthly_trend": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
  ],

  "anomalies": [
    {
      "category": "",
      "type": "",
      "severity": "HIGH | MEDIUM | LOW",
      "description": "",
      "financial_impact": 0,
      "recommendation": ""
    }
  ],

  "local_research": {
    "property_tax_rate": 0,
    "current_assessment": 0,
    "projected_reassessment": 0,
    "tax_increase_estimate": 0,
    "insurance_market_rate": 0,
    "utility_rates": {
      "electric_kwh": 0,
      "gas_therm": 0,
      "water_1000gal": 0,
      "sewer_1000gal": 0,
      "trash_per_unit": 0
    },
    "sources": []
  },

  "adjusted_schedule": [
    {
      "category": "",
      "seller_amount": 0,
      "adjusted_amount": 0,
      "adjustment_direction": "UP | DOWN | NONE",
      "adjustment_delta": 0,
      "justification": ""
    }
  ],

  "adjusted_totals": {
    "total_adjusted_expenses": 0,
    "adjusted_noi": 0,
    "adjusted_expense_ratio_pct": 0,
    "adjusted_opex_per_unit": 0,
    "noi_delta_from_seller": 0,
    "noi_delta_pct": 0
  },

  "optimization_opportunities": [
    {
      "category": "",
      "opportunity": "",
      "estimated_annual_savings": 0,
      "implementation_effort": "LOW | MEDIUM | HIGH"
    }
  ],

  "risk_flags": [],
  "recommendations": [],
  "confidence_level": "HIGH | MEDIUM | LOW",
  "data_quality_notes": [],
  "uncertainty_flags": [
    {
      "field_name": "",
      "reason": "estimated | assumed | unverified | stale_data | interpolated",
      "impact": "Description of what downstream analysis this affects"
    }
  ]
}
```

---

## Quality Checks

Before finalizing output, run all of the following checks:

**Schema and Math**
- Verify all required output fields are present, non-null, and correctly typed
- Sum of monthly values must equal reported annual for each category (T-12 math check)
- Revenue - Adjusted Expenses = Adjusted NOI (within $100)
- All 11 standard categories must be addressed

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| totalOpEx | > 0 | Zero or negative |
| opExPerUnit | $2,000 - $12,000/year | Outside range |
| opExRatio | 0.20 - 0.80 | Outside range |
| taxes + insurance + utilities + ... | Must sum to totalOpEx | Sum mismatch > 1% |
| adjustedExpenses vs rawExpenses | Difference must be explainable by one-time items | Unexplained difference |

**Threshold Assessment**

| Output Metric | Excellent | Good | Acceptable | Concern |
|--------------|-----------|------|------------|---------|
| Expense Ratio (opExRatio) | ≤ 0.40 | ≤ 0.45 | ≤ 0.50 | > 0.55 |

Additional validation:
- Total expense ratio should be 35–65% for typical multifamily
- Management fee floor: adjusted management fee must be at least 3% of EGI
- Reserve requirement: capital reserves included at minimum $250/unit/year
- Tax verification: reported taxes within 20% of calculated taxes from mill rate

**Completeness**
- Every strategy step has produced output or a documented data gap
- All adjustment decisions have justifications

**Confidence Scoring**
- Set confidence_level based on data completeness
- Populate uncertainty_flags for any estimated or assumed values

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| DSCR below 0.80 without clear value-add thesis | If adjusted expense levels make in-place DSCR < 0.80, flag immediately as CRITICAL |
| Uninsurable property condition | If insurance costs are impossibly high or coverage is unavailable, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if any dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If T-12 data is incomplete (missing months):**
- Attempt to annualize from available months (e.g., 9 months → multiply by 12/9)
- Flag the annualization in `uncertainty_flags`
- Reduce confidence to MEDIUM

**If a standard expense category is absent:**
- Treat as $0 for the reported schedule
- Impute a market-rate estimate for the adjusted schedule
- Document the imputation with source and rationale in `data_quality_notes`

**If local tax or utility research yields no results:**
- Use the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md) as a regional fallback
- Note the assumption and reduce affected confidence factors

For any assumed or estimated value:
- Add to `uncertainty_flags`: `{ "field": "{name}", "reason": "Data unavailable - using {method}", "confidence": "LOW" }`
- Continue analysis; do not halt for non-critical data gaps

---

## Confidence Scoring

Rate the overall confidence of your analysis using this rubric:

| Level | Criteria | When to Assign |
|-------|----------|---------------|
| **HIGH** | All primary data sources available, no significant assumptions, cross-references validate | Complete data, no workarounds needed |
| **MEDIUM** | Most data available, 1-2 assumptions made with reasonable basis, minor cross-reference gaps | Some estimates used, benchmarks substituted for actuals |
| **LOW** | Significant data gaps, multiple assumptions, limited ability to cross-reference | Major data unavailable, heavy reliance on estimates |

Include in output:
```json
{
  "confidence": "HIGH|MEDIUM|LOW",
  "confidenceFactors": [
    { "factor": "{description}", "impact": "positive|negative", "detail": "{explanation}" }
  ]
}
```

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Underwriting Calculations](knowledge/underwriting-calc.md) for NOI calculations and expense ratio benchmarks
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) for per-unit expense ranges by category, class, and region
- Downstream: [Annual Operating Budget Builder](../asset-management/annual-operating-budget-builder.md), [NOI Improvement Analyst](../asset-management/noi-improvement-analyst.md)
