---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Rent Roll Analyst

Validates a property's rent roll — analyzing in-place rents vs. market, loss-to-lease opportunity, unit mix, economic vs. physical occupancy, tenant concentration risks, and revenue anomalies.

---

## When to Use This Skill

Use this skill when you have a property's rent roll and need to verify revenue quality before making an acquisition decision. It is most valuable during due diligence when you want to understand how in-place rents compare to the market, identify red flags in the tenant roster, and project stabilized revenue.

---

## What You'll Need to Provide

- **Rent roll data** — unit number, tenant name, lease start date, lease end date, monthly rent, security deposit, and unit status (occupied/vacant/NTV/down) for every unit
- **Property details** — property name, address, submarket, total unit count, and unit mix (studio/1BR/2BR/3BR counts)
- **Asking rents** (if available) — the seller's quoted rents by unit type
- **Market rent data** (optional) — if you have already gathered comparable rents, provide them; otherwise this analysis will research them

---

## Mission

Validate the property rent roll. Analyze in-place rents vs market, identify loss-to-lease opportunity, verify unit mix, calculate economic vs physical occupancy, identify tenant concentration risks, and flag anomalies (same-day leases, below-market rents, related-party tenants).

---

## Strategy

### Step 1: Parse Rent Roll from Deal Inputs

- Use the property details provided to extract the address, unit count, unit mix, and asking rents
- Read rent roll data (CSV, JSON, or structured text)
- Build internal data model: array of unit records with all fields
- Validate completeness: every unit accounted for, no missing fields

### Step 2: Research Market Rents via Web Search

- Search for market rents in the submarket by unit type
- Query pattern: `"{city} {submarket} average rent {unit_type} {current_year}"`
- Cross-reference at least 3 sources (Apartments.com, Zillow, RentCafe, local MLS data)
- Build market rent table: unit type, market low, market median, market high
- If market rent data has already been provided, use it directly and skip external research

### Step 3: Compare In-Place to Market (Loss-to-Lease)

- For each unit type, calculate:
  - `loss_to_lease_per_unit = market_median_rent - in_place_rent`
  - `loss_to_lease_pct = (market_median - in_place) / market_median * 100`
- Aggregate total loss-to-lease across all occupied units
- Annualize the loss-to-lease opportunity
- Classify: SIGNIFICANT (>10%), MODERATE (5-10%), MINIMAL (<5%)

### Step 4: Calculate Weighted Average Rent and Occupancy

- **Weighted Average Rent**: Sum of all in-place rents / number of occupied units
- **Physical Occupancy**: Occupied units / total units * 100
- **Economic Occupancy**: Actual collected rent / gross potential rent * 100
  - Account for: vacancies, concessions, bad debt, loss-to-lease, model/employee units
- **Gross Potential Rent (GPR)**: Total units * market rent (by unit type)
- **Effective Gross Income (EGI)**: GPR - vacancy loss - concessions - bad debt + other income

### Step 5: Identify Tenant Concentration Risks

- Calculate each tenant's share of total rental revenue
- Flag any tenant contributing >10% of total revenue (CRITICAL for commercial/mixed-use)
- Identify related-party tenants (same last name, same employer, same move-in date patterns)
- Analyze lease expiration clustering:
  - Group leases by expiration month
  - Flag any month with >20% of leases expiring
  - Flag any quarter with >40% of leases expiring
- Calculate tenant diversity index

### Step 6: Flag Anomalies

Run anomaly detection across the rent roll:

| Anomaly Type              | Threshold / Pattern                              | Severity |
|---------------------------|--------------------------------------------------|----------|
| Below-market rent         | >15% below market median for unit type           | HIGH     |
| Above-market rent         | >15% above market median (sustainability risk)   | MEDIUM   |
| Long-term vacancy         | Vacant >90 days                                  | HIGH     |
| Same-day leases           | 3+ leases with identical start dates             | MEDIUM   |
| Month-to-month leases     | >15% of tenants on MTM                           | MEDIUM   |
| No security deposit       | Deposit = $0 or missing                          | LOW      |
| Related-party indicators  | Same last name, same employer, same move-in      | HIGH     |
| Lease term anomalies      | Lease term <6 months or >24 months               | LOW      |
| Rent concessions          | Active concessions >5% of face rent              | MEDIUM   |
| Recent bulk move-ins      | >10% of tenants moved in within last 60 days     | HIGH     |

### Step 7: Calculate Other Income

- Identify and quantify all non-rental income streams:
  - Laundry revenue (per unit per month estimate)
  - Parking fees (reserved spaces, garages)
  - Pet fees (pet rent, pet deposits)
  - RUBS (Ratio Utility Billing System) recovery
  - Late fees and NSF charges
  - Application fees
  - Storage units
  - Vending machines
  - Cable/internet commissions
- Benchmark other income per unit against the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md)
- Project stabilized other income

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "unit_summary": {
    "total_units": 0,
    "occupied_units": 0,
    "vacant_units": 0,
    "down_units": 0,
    "model_units": 0,
    "unit_mix": [
      {
        "type": "1BR/1BA",
        "count": 0,
        "avg_sqft": 0,
        "avg_in_place_rent": 0,
        "market_rent": 0,
        "loss_to_lease_pct": 0
      }
    ]
  },

  "occupancy": {
    "physical_occupancy_pct": 0,
    "economic_occupancy_pct": 0,
    "gross_potential_rent_monthly": 0,
    "effective_gross_income_monthly": 0,
    "vacancy_loss_monthly": 0,
    "concessions_monthly": 0,
    "bad_debt_monthly": 0
  },

  "rent_analysis": {
    "weighted_avg_rent": 0,
    "total_loss_to_lease_monthly": 0,
    "total_loss_to_lease_annual": 0,
    "loss_to_lease_pct": 0,
    "loss_to_lease_classification": "SIGNIFICANT | MODERATE | MINIMAL",
    "market_rent_sources": ["source1", "source2", "source3"]
  },

  "concentration_risk": {
    "top_tenant_revenue_share_pct": 0,
    "tenants_above_10pct_threshold": [],
    "related_party_flags": [],
    "lease_expiration_clustering": {
      "peak_month": "YYYY-MM",
      "peak_month_pct": 0,
      "peak_quarter": "YYYY-Q#",
      "peak_quarter_pct": 0
    },
    "month_to_month_pct": 0,
    "tenant_diversity_index": 0
  },

  "anomalies": [
    {
      "unit": "",
      "type": "",
      "severity": "HIGH | MEDIUM | LOW",
      "description": "",
      "recommendation": ""
    }
  ],

  "other_income": {
    "total_monthly": 0,
    "total_annual": 0,
    "per_unit_monthly": 0,
    "breakdown": {
      "laundry": 0,
      "parking": 0,
      "pet_fees": 0,
      "rubs": 0,
      "late_fees": 0,
      "application_fees": 0,
      "storage": 0,
      "other": 0
    },
    "benchmark_comparison": "ABOVE | AT | BELOW market"
  },

  "revenue_projection": {
    "in_place_annual": 0,
    "stabilized_annual": 0,
    "upside_annual": 0,
    "assumptions": []
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
- Sum of unit rents must equal reported total rent
- Lease expiration schedule sum must equal total units
- Physical occupancy must equal 1 - vacancy rate

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| occupancy | 0.0 - 1.0 | Outside range |
| avgRent | $200 - $10,000/mo | Outside range |
| lossToLeasePercent | 0.0 - 0.30 | Above 30% |
| totalUnits | Must match provided unit count | Mismatch |
| vacancyRate | 0.0 - 1.0, must equal 1 - occupancy | Inconsistent |
| concessionValue | >= 0 | Negative |

**Cross-Reference Validation**
- Unit count in rent roll must match the property details provided
- No in-place rent should exceed 2x market median

**Threshold Assessment**

| Output Metric | Pass | Conditional | Concern | Distressed |
|--------------|------|-------------|---------|------------|
| Occupancy | ≥ 95% | 90–94% | 85–89% | < 80% |
| Rent-to-market ratio | < 0.90 (upside) | 0.90–1.0 (at market) | 1.0–1.05 | > 1.10 (overpriced) |

**Completeness**
- Every strategy step has produced output or a documented data gap
- Market rents have at least 2 independent sources
- Every unit in the unit mix has at least one rent comp
- If >30% of units are flagged as anomalies, escalate with a prominent warning

**Confidence Scoring**
- Set confidence_level based on data completeness
- Populate uncertainty_flags for any estimated or assumed values

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| DSCR below 0.80 without clear value-add thesis | If calculated in-place DSCR < 0.80, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if any dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If rent roll data is incomplete or unavailable:**
- Attempt to parse any partial data provided
- Note which units are missing data and estimate from similar units in the roster
- Mark affected fields in `uncertainty_flags`

**If market rents cannot be researched:**
- Use the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md) as a fallback
- Note the assumption and source in `data_quality_notes`
- Reduce confidence to MEDIUM or LOW accordingly

**If any required input is missing:**
- Note the gap in `data_quality_notes` with a description of what is missing
- Use industry benchmarks or related data as proxies where possible
- Do not halt analysis for non-critical gaps — continue and aggregate all gaps in the final output

For any assumed or estimated value:
- Add to `uncertainty_flags`: `{ "field": "{name}", "reason": "Data unavailable - using {method}", "confidence": "LOW" }`
- Add to `data_quality_notes`: description of the gap and its impact on the analysis

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
- [Underwriting Calculations](knowledge/underwriting-calc.md) for NOI calculations, cap rate, and revenue projections
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) for market standards on rents, occupancy, and other income per unit
- Downstream: [Annual Operating Budget Builder](../asset-management/annual-operating-budget-builder.md), [Rent Collection & Delinquency Manager](../asset-management/rent-collection-delinquency-manager.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
