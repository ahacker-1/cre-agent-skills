---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Tenant Credit Analyst

Evaluates tenant creditworthiness and lease quality across a multifamily property, assessing tenant mix, concentration risks, lease expiration schedule, renewal probability, and producing a portfolio-level tenant quality score that informs underwriting risk assumptions.

---

## When to Use This Skill

Use this skill when you have a property's rent roll and need to assess the quality and stability of the current tenant base before making an acquisition decision. It is most valuable during due diligence when you want to understand how much revenue is at risk from non-renewals, identify problematic concentrations, and set defensible bad-debt and vacancy assumptions for your underwriting model.

---

## What You'll Need to Provide

- **Rent roll data** — unit number, tenant name, lease start date, lease end date, monthly rent, security deposit, unit status (occupied/vacant/NTV/down/model/employee), unit type, and lease type (standard/month-to-month/Section 8/corporate) for every unit
- **Property details** — property name, address, total unit count, property class (A/B/C/D), and target tenant profile
- **Market rent data** (optional) — market rents by unit type for comparison; if not provided, reference the Multifamily Benchmarks knowledge base
- **Payment history summaries** (optional) — if the seller provides delinquency or payment history data, include it
- **Section 8 contract rents** (optional) — if any units are subsidized, provide the HAP contract amounts

---

## Mission

Evaluate tenant creditworthiness and lease quality across the property. For large properties (>50 units), analyze tenants in batches if needed. Produce a portfolio-level tenant quality assessment that informs underwriting risk assumptions.

---

## Strategy

### Step 1: Receive and Validate Tenant Roster

- Read rent roll and extract tenant records
- Build tenant data model:

| Field              | Description                                         |
|--------------------|-----------------------------------------------------|
| unit_number        | Unit identifier                                     |
| tenant_name        | Tenant name or entity                               |
| lease_start        | Lease commencement date                             |
| lease_end          | Lease expiration date                               |
| monthly_rent       | Current monthly rent                                |
| deposit            | Security deposit amount                             |
| status             | Occupied, Vacant, NTV, Down, Model, Employee        |
| unit_type          | Studio, 1BR, 2BR, 3BR, etc.                        |
| lease_type         | Standard, Month-to-Month, Section 8, Corporate      |
| move_in_date       | Original move-in date                               |

- Validate: total unit count matches the property details provided, no duplicate unit numbers
- Count: total tenants, occupied, vacant, NTV, down, model/employee

### Step 2: Batch Processing Decision

For properties with more than 50 units, process tenants in batches of up to 50 units at a time. For each batch:

1. Calculate lease term remaining for each unit
2. Classify lease status: Active, Expiring Soon (<90 days), Month-to-Month, Expired
3. Assess rent-to-deposit ratio (deposit should be >= 1 month rent)
4. Identify Section 8 or subsidized tenants
5. Estimate payment risk based on:
   - Lease term remaining (shorter = higher risk)
   - Deposit coverage (low deposit = higher risk)
   - Rent level vs market (below market = lower risk, above = higher)
6. Score each tenant: LOW RISK, MODERATE RISK, HIGH RISK
7. Estimate renewal probability: HIGH (>70%), MODERATE (40-70%), LOW (<40%)

Aggregate all batch results into the master tenant analysis after processing.

For properties ≤50 units, analyze all tenants directly using Steps 3-7.

### Step 3: Assess Tenant Mix

Categorize the tenant base:

| Mix Category              | Metric                                             |
|---------------------------|-----------------------------------------------------|
| Residential vs Commercial | % of units/revenue from each (if mixed-use)        |
| Individual vs Corporate   | % of leases held by individuals vs entities         |
| Market Rate vs Subsidized | % of units at market vs Section 8/LIHTC/other       |
| Lease Type               | % Standard, Month-to-Month, Short-term              |
| Tenant Tenure             | % < 1 year, 1-3 years, 3-5 years, 5+ years         |

Ideal mix varies by class:
- Class A: Primarily individual, market rate, standard leases
- Class B: Mixed individual/some corporate, mostly market, some Section 8
- Class C: Higher Section 8 percentage acceptable, more month-to-month expected
- Class D: Significant subsidized component expected

### Step 4: Identify Concentration Risks

| Risk Type                    | Threshold                         | Severity |
|------------------------------|-----------------------------------|----------|
| Single tenant >10% revenue   | Any tenant/entity >10% of GPI     | HIGH     |
| Single employer >20% tenants | >20% tenants share same employer   | HIGH     |
| Section 8 >50%              | >50% of units are subsidized       | MEDIUM   |
| Month-to-month >25%         | >25% of tenants on MTM            | MEDIUM   |
| Corporate tenant >15%       | Single corporate tenant >15% units | HIGH     |
| Related-party tenants        | Tenants sharing last name/employer/move-in | MEDIUM |
| Single unit type >70%       | Over-reliance on one unit type     | LOW      |

For each concentration risk identified:
- Calculate the exposure (% of revenue or units)
- Assess the impact if that concentration fails
- Recommend mitigation strategies

### Step 5: Analyze Lease Expiration Schedule

Build a month-by-month expiration calendar for the next 24 months:

For each month:
- Count leases expiring
- Sum rent at risk
- Calculate % of total rent expiring

Flag:
- Any single month with >15% of leases expiring → HIGH risk
- Any quarter with >30% of leases expiring → HIGH risk
- More than 40% of leases expiring in next 12 months → MEDIUM risk
- Significant clustering around any single date → investigate cause

### Step 6: Assess Renewal Probability

For each tenant, estimate renewal probability based on:

| Factor                      | Weight | HIGH renewal indicators           | LOW renewal indicators            |
|-----------------------------|--------|-----------------------------------|-----------------------------------|
| Lease term remaining        | 25%    | >6 months remaining               | <3 months or MTM                  |
| Tenure (time at property)   | 20%    | >2 years at property              | <6 months at property             |
| Rent vs market              | 20%    | At or below market                | >10% above market                 |
| Deposit coverage            | 15%    | Deposit >= 1 month rent           | No deposit or < 0.5x rent        |
| Section 8 status            | 10%    | Section 8 (stable voucher)        | N/A                               |
| Property class trend        | 10%    | Improving property                | Declining property                |

Calculate:
- Portfolio weighted renewal probability
- Revenue at risk from non-renewals (rent * (1 - renewal_probability))
- Projected turnover rate

### Step 7: Calculate Portfolio Tenant Quality Score

Aggregate all analysis into a single portfolio quality score (0-100):

| Component                   | Weight | Score Basis                                       |
|-----------------------------|--------|---------------------------------------------------|
| Occupancy stability         | 20%    | Physical occupancy rate                           |
| Lease quality               | 20%    | % on standard leases vs MTM                      |
| Tenant tenure               | 15%    | Average tenant tenure length                      |
| Concentration risk          | 15%    | Inverse of concentration (lower = better)         |
| Expiration distribution     | 15%    | Evenness of expiration schedule                   |
| Renewal probability         | 15%    | Portfolio weighted renewal probability            |

Score interpretation:
- 80-100: EXCELLENT — Low risk, stable tenant base
- 60-79: GOOD — Manageable risk, some areas to watch
- 40-59: FAIR — Moderate risk, active management needed
- 20-39: POOR — High risk, significant tenant issues
- 0-19: CRITICAL — Severe tenant quality issues

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "processing_method": "DIRECT | BATCHED",
  "batch_count": 0,

  "tenant_roster_summary": {
    "total_units": 0,
    "occupied_units": 0,
    "vacant_units": 0,
    "ntv_units": 0,
    "down_units": 0,
    "model_employee_units": 0,
    "total_tenants": 0
  },

  "tenant_mix": {
    "residential_pct": 0,
    "commercial_pct": 0,
    "individual_pct": 0,
    "corporate_pct": 0,
    "market_rate_pct": 0,
    "section_8_pct": 0,
    "other_subsidized_pct": 0,
    "standard_lease_pct": 0,
    "month_to_month_pct": 0,
    "short_term_pct": 0,
    "tenure_distribution": {
      "less_than_1yr": 0,
      "one_to_3yr": 0,
      "three_to_5yr": 0,
      "over_5yr": 0
    },
    "avg_tenant_tenure_months": 0
  },

  "concentration_risks": [
    {
      "risk_type": "",
      "entity_or_group": "",
      "exposure_pct": 0,
      "revenue_at_risk": 0,
      "severity": "HIGH | MEDIUM | LOW",
      "mitigation": ""
    }
  ],

  "lease_expiration_schedule": {
    "next_12_months": {
      "total_expiring": 0,
      "pct_of_total": 0,
      "rent_at_risk": 0,
      "monthly_detail": [
        {
          "month": "YYYY-MM",
          "count_expiring": 0,
          "rent_expiring": 0,
          "pct_of_total": 0,
          "risk_flag": false
        }
      ]
    },
    "next_13_to_24_months": {
      "total_expiring": 0,
      "pct_of_total": 0,
      "rent_at_risk": 0
    },
    "peak_expiration_month": "",
    "peak_expiration_pct": 0,
    "clustering_flags": []
  },

  "renewal_analysis": {
    "portfolio_renewal_probability_pct": 0,
    "projected_turnover_rate_pct": 0,
    "revenue_at_risk_from_nonrenewal": 0,
    "renewal_by_category": {
      "high_probability": { "count": 0, "pct": 0 },
      "moderate_probability": { "count": 0, "pct": 0 },
      "low_probability": { "count": 0, "pct": 0 }
    }
  },

  "payment_risk_assessment": {
    "low_risk_tenants": { "count": 0, "pct": 0 },
    "moderate_risk_tenants": { "count": 0, "pct": 0 },
    "high_risk_tenants": { "count": 0, "pct": 0 },
    "estimated_annual_bad_debt_pct": 0,
    "estimated_annual_bad_debt_amount": 0
  },

  "portfolio_quality_score": {
    "total_score": 0,
    "rating": "EXCELLENT | GOOD | FAIR | POOR | CRITICAL",
    "component_scores": {
      "occupancy_stability": 0,
      "lease_quality": 0,
      "tenant_tenure": 0,
      "concentration_risk": 0,
      "expiration_distribution": 0,
      "renewal_probability": 0
    }
  },

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
- All strategy steps have produced output or a documented data gap
- All lease expiration counts sum to the total occupied unit count
- All mix percentages sum to approximately 100%

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| avgCreditScore | 300 - 850 | Outside range |
| concentrationRisk | LOW, MEDIUM, HIGH | Invalid enum |
| topTenantExposure | 0.0 - 1.0 | Outside range |
| delinquencyRate | 0.0 - 1.0 | Outside range or > 0.30 (warning) |
| tenantRetentionRate | 0.0 - 1.0 | Outside range |
| leaseExpirations sum | Must equal totalUnits | Sum mismatch |

**Roster Validation**
- Tenant roster count matches the unit count provided
- All lease start dates are before lease end dates
- No rent is negative or exceeds 3x market median for unit type
- Portfolio quality score is between 0 and 100
- All occupied units have an expiration date or MTM designation

**Confidence Scoring**
- Set confidence_level based on data completeness
- Populate uncertainty_flags for any estimated or assumed values

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Criminal activity nexus | If tenant analysis reveals evidence of illegal activity operating on or from the property, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if this dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If lease type (standard/MTM/Section 8) is not provided:**
- Classify leases without an end date or with very short remaining terms as month-to-month
- Note the classification assumption in `data_quality_notes`
- If Section 8 tenants cannot be identified, note this as a data gap and recommend verification with the seller

**If market rent data is not provided:**
- Reference the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md) for typical rent ranges by unit type and property class
- Note the substitution in `uncertainty_flags`

**If payment history is not available:**
- Estimate bad debt based on property class benchmarks from the Multifamily Benchmarks knowledge base:
  - Class A: 0.5-1.0% of GPI
  - Class B: 1.0-2.0% of GPI
  - Class C: 2.0-4.0% of GPI
  - Class D: 4.0-8.0% of GPI
- Flag as an estimate in `uncertainty_flags`

**If employer information for employer concentration analysis is not provided:**
- Research the top recurring employer names from the tenant roster
- Note any employers with 3+ units as potential concentration risks requiring verification

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
- [Underwriting Calculations](knowledge/underwriting-calc.md) for bad debt assumptions and vacancy projections
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) for tenant quality standards by class and typical turnover rates
- [Risk Scoring Framework](knowledge/risk-scoring.md) for tenant concentration risk scoring methodology

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
