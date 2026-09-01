---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Market Study

Analyzes the submarket including rent comps, sales comps, supply pipeline, demand drivers, demographics, and market cycle position — then positions the subject property within the competitive landscape and assesses market risk.

---

## When to Use This Skill

Use this skill when you need to understand how a target property fits within its local market before committing to an acquisition. It is most valuable during due diligence when you want to validate the seller's rent assumptions against real comp data, assess cap rate trends, identify supply-side risks, and understand the demand drivers sustaining (or threatening) the market.

---

## What You'll Need to Provide

- **Property details** — address, city, state, submarket name, total unit count, unit mix (studio/1BR/2BR/3BR), year built, and property class (A/B/C)
- **In-place rents by unit type** (optional) — if you have rent roll data, provide it; otherwise this analysis will research market rents without an in-place comparison
- **Asking price or target price** — used to calculate the implied cap rate for comparison against market

---

## Mission

Analyze the submarket including rent comps, sales comps, supply pipeline, demand drivers, demographics, and market trends. Position the subject property within the competitive landscape and assess market risk.

---

## Strategy

### Step 1: Research Submarket Rent Data

- Search: `"apartments for rent" "{city}" "{submarket}" {current_year}`
- Search: `"{city}" average apartment rent by bedroom {current_year}`
- Search: `"RentCafe" OR "Apartments.com" "{submarket}" rent report`
- Gather rent comps — target 5+ comparable properties within 3-mile radius

For each comp, collect:
| Field            | Description                                        |
|------------------|-----------------------------------------------------|
| Property name    | Name of comparable property                        |
| Address          | Full address                                       |
| Distance         | Distance from subject property (miles)             |
| Year built       | Construction year                                  |
| Units            | Total unit count                                   |
| Class            | Property class (A/B/C)                             |
| Studio rent      | Average rent for studio (if applicable)            |
| 1BR rent         | Average rent for 1BR                               |
| 2BR rent         | Average rent for 2BR                               |
| 3BR rent         | Average rent for 3BR (if applicable)               |
| Occupancy        | Current occupancy rate                             |
| Amenities        | Key amenities (pool, fitness, W/D, etc.)           |
| Concessions      | Current move-in specials or concessions            |

- Calculate submarket averages by unit type
- Rank subject property rents relative to comps
- If in-place rents have been provided, compare directly to the comp set

### Step 2: Research Recent Multifamily Sales Comps

- Search: `"multifamily sale" "{city}" "{submarket}" {current_year} OR {last_year}`
- Search: `"apartment sale" "{city}" price per unit {current_year}`
- Search: `"{city}" multifamily cap rate {current_year}`
- Gather 3+ sales comps from the past 12-24 months

For each sales comp, collect:
| Field            | Description                                        |
|------------------|-----------------------------------------------------|
| Property name    | Name of sold property                              |
| Address          | Full address                                       |
| Distance         | Distance from subject (miles)                      |
| Sale date        | Date of sale                                       |
| Sale price       | Total sale price                                   |
| Price per unit   | Sale price / total units                           |
| Price per sqft   | Sale price / total sqft                            |
| Cap rate         | Reported or estimated cap rate                     |
| Units            | Total unit count                                   |
| Year built       | Construction year                                  |
| Class            | Property class                                     |
| Occupancy at sale| Occupancy at time of sale                          |
| Buyer type       | Institutional, private, REIT, syndicator           |

### Step 3: Calculate Market Cap Rates

- From sales comps, compute:
  - Median cap rate
  - Average cap rate
  - Cap rate range (low to high)
- Segment by class if enough data points:
  - Class A cap rate range
  - Class B cap rate range
  - Class C cap rate range
- Compare subject property's implied cap rate to market
- Assess cap rate trend (compressing, stable, expanding)

### Step 4: Research Supply Pipeline

- Search: `"new apartment construction" "{city}" {current_year} {next_year}`
- Search: `"multifamily permits" "{city}" OR "{county}" {current_year}`
- Search: `"planned apartment development" "{submarket}"`
- Identify:
  - New developments under construction (name, units, delivery date, class)
  - Planned/permitted developments not yet started
  - Total new supply as percentage of existing inventory
  - Absorption rate (how quickly market absorbs new units)
- Calculate supply risk:
  - New units delivering in next 12 months / existing inventory = supply pressure %
  - Risk: LOW (<3%), MODERATE (3-7%), HIGH (>7%)

### Step 5: Analyze Demand Drivers

- Search: `"{city}" employment growth {current_year}`
- Search: `"{city}" major employers largest companies`
- Search: `"{city}" population growth {current_year}`
- Research:

| Demand Driver          | Metrics to Collect                                    |
|------------------------|-------------------------------------------------------|
| Employment             | Job growth rate, unemployment rate, YoY change        |
| Major employers        | Top 10 employers, industry diversification            |
| Population             | Population growth rate, net migration                  |
| Income                 | Median household income, income growth rate            |
| Housing affordability  | Median home price, rent-to-own cost comparison         |
| Education              | Universities, student population                       |
| Military               | Nearby bases, personnel count                          |
| Healthcare             | Major hospital systems, medical centers                |
| Transportation         | Transit access, highway proximity, commute times       |

- Assess demand driver strength: STRONG, MODERATE, WEAK

### Step 6: Research Demographic Trends

- Search: `"{city}" demographics census data {current_year}`
- Search: `"{zip code}" demographics median income`
- Collect:

| Metric                      | Value        | Trend (5yr)           |
|-----------------------------|--------------|------------------------|
| Population (MSA)            |              | Growing / Stable / Declining |
| Population (submarket)      |              |                        |
| Median household income     |              |                        |
| Median age                  |              |                        |
| Renter percentage           |              |                        |
| Rent-to-income ratio        |              | Must be <33% for healthy market |
| Poverty rate                |              |                        |
| College educated %          |              |                        |
| Household growth rate       |              |                        |

- Calculate rent-to-income ratio: `(avg_market_rent * 12) / median_household_income`
- Flag if ratio exceeds 33% (rent burden risk)

### Step 7: Assess Market Cycle Position

Based on all collected data, classify the market:

| Cycle Phase    | Indicators                                                 |
|----------------|-------------------------------------------------------------|
| Recovery       | Declining vacancy, no new construction, below-peak rents   |
| Expansion      | Decreasing vacancy, moderate new construction, rising rents |
| Hyper-supply   | Increasing vacancy, high new construction, rent growth slowing |
| Recession      | Rising vacancy, construction halting, declining rents       |

Determine:
- Current cycle phase
- Direction of movement
- Estimated time to next phase transition
- Risk implications for the subject acquisition

### Step 8: Position Subject Property Against Comps

Build a competitive positioning analysis:

| Factor              | Subject   | Comp Avg   | Advantage/Disadvantage |
|---------------------|-----------|------------|------------------------|
| Rent (by type)      |           |            |                        |
| Age                 |           |            |                        |
| Occupancy           |           |            |                        |
| Class               |           |            |                        |
| Amenities           |           |            |                        |
| Location            |           |            |                        |
| Condition           |           |            |                        |
| Unit size (sqft)    |           |            |                        |
| Concessions         |           |            |                        |

- Overall positioning: PREMIUM, AT MARKET, DISCOUNT, VALUE-ADD OPPORTUNITY

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "submarket_overview": {
    "submarket_name": "",
    "city": "",
    "state": "",
    "msa": "",
    "submarket_description": ""
  },

  "rent_comps": [
    {
      "property_name": "",
      "address": "",
      "distance_miles": 0,
      "year_built": 0,
      "units": 0,
      "class": "",
      "rents": {
        "studio": 0,
        "one_br": 0,
        "two_br": 0,
        "three_br": 0
      },
      "occupancy_pct": 0,
      "amenities": [],
      "concessions": ""
    }
  ],

  "rent_comp_summary": {
    "submarket_avg_rent_studio": 0,
    "submarket_avg_rent_1br": 0,
    "submarket_avg_rent_2br": 0,
    "submarket_avg_rent_3br": 0,
    "submarket_avg_occupancy": 0,
    "subject_rent_position": "ABOVE | AT | BELOW market"
  },

  "sales_comps": [
    {
      "property_name": "",
      "address": "",
      "distance_miles": 0,
      "sale_date": "",
      "sale_price": 0,
      "price_per_unit": 0,
      "price_per_sqft": 0,
      "cap_rate": 0,
      "units": 0,
      "year_built": 0,
      "class": "",
      "occupancy_at_sale": 0,
      "buyer_type": ""
    }
  ],

  "cap_rate_analysis": {
    "market_cap_rate_median": 0,
    "market_cap_rate_avg": 0,
    "market_cap_rate_low": 0,
    "market_cap_rate_high": 0,
    "cap_rate_by_class": {
      "class_a": 0,
      "class_b": 0,
      "class_c": 0
    },
    "cap_rate_trend": "COMPRESSING | STABLE | EXPANDING",
    "subject_implied_cap_rate": 0,
    "subject_vs_market": "ABOVE | AT | BELOW"
  },

  "supply_pipeline": {
    "under_construction": [
      {
        "project_name": "",
        "units": 0,
        "expected_delivery": "",
        "class": "",
        "distance_miles": 0
      }
    ],
    "planned_not_started": [],
    "total_new_units_12mo": 0,
    "total_new_units_24mo": 0,
    "existing_inventory_estimate": 0,
    "supply_pressure_pct_12mo": 0,
    "absorption_rate_units_per_month": 0,
    "supply_risk": "LOW | MODERATE | HIGH"
  },

  "demand_drivers": {
    "employment": {
      "job_growth_rate_pct": 0,
      "unemployment_rate_pct": 0,
      "major_employers": [],
      "industry_diversification": "HIGH | MODERATE | LOW"
    },
    "population": {
      "msa_population": 0,
      "population_growth_rate_pct": 0,
      "net_migration": "POSITIVE | NEGATIVE"
    },
    "income": {
      "median_household_income": 0,
      "income_growth_rate_pct": 0
    },
    "housing_affordability": {
      "median_home_price": 0,
      "rent_vs_own_ratio": 0,
      "homeownership_rate_pct": 0
    },
    "other_drivers": [],
    "demand_strength": "STRONG | MODERATE | WEAK"
  },

  "demographics": {
    "population_msa": 0,
    "population_submarket": 0,
    "median_household_income": 0,
    "median_age": 0,
    "renter_pct": 0,
    "rent_to_income_ratio": 0,
    "rent_burden_flag": false,
    "poverty_rate_pct": 0,
    "college_educated_pct": 0,
    "household_growth_rate_pct": 0,
    "trends_5yr": {}
  },

  "market_cycle": {
    "current_phase": "RECOVERY | EXPANSION | HYPER-SUPPLY | RECESSION",
    "direction": "IMPROVING | STABLE | DECLINING",
    "supporting_indicators": [],
    "risk_implications": ""
  },

  "competitive_positioning": {
    "overall_position": "PREMIUM | AT MARKET | DISCOUNT | VALUE-ADD OPPORTUNITY",
    "advantages": [],
    "disadvantages": [],
    "positioning_details": [
      {
        "factor": "",
        "subject": "",
        "comp_avg": "",
        "assessment": "ADVANTAGE | NEUTRAL | DISADVANTAGE"
      }
    ]
  },

  "market_risk_rating": "HIGH | MEDIUM | LOW",
  "risk_flags": [],
  "recommendations": [],
  "confidence_level": "HIGH | MEDIUM | LOW",
  "data_quality_notes": [],
  "sources": [],
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
- All 8 strategy steps have produced output or a documented data gap

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| rentGrowthTrailing12 | -0.20 to 0.30 | Outside range |
| rentGrowthProjected | -0.10 to 0.20 | Outside range |
| capRateRange.low | 0.02 to 0.15 | Outside range |
| capRateRange.high | >= capRateRange.low | Low > High |
| employmentGrowth | -0.10 to 0.15 | Outside range |
| populationGrowth | -0.05 to 0.10 | Outside range |
| rentToIncomeRatio | 0.10 to 0.60 | Outside range |
| medianHouseholdIncome | $20,000 to $300,000 | Outside range |

**Comp Coverage**
- At least 5 rent comps gathered
- At least 3 rent comps within 3 miles of subject
- At least 3 sales comps from past 12-24 months
- At least 2 sales comps within past 12 months
- Subject rents within 30% of comp average
- Market cap rate between 3% and 12% (typical multifamily range)
- Data from at least 3 independent sources

**Red Flag Conditions**
- Flag as HIGH severity if market cycle is in recession with accelerating decline
- Flag as HIGH severity if neighborhood has significant documented safety concerns

**Confidence Scoring**
- Set confidence_level based on data completeness and source quality
- Populate uncertainty_flags for any estimated or assumed values

---

## Red Flags & Dealbreakers

This skill does not carry direct dealbreaker authority, but immediately flag as HIGH severity:

| Red Flag | Detection Criteria |
|----------|-------------------|
| Severe market decline | Market cycle is in recession with accelerating decline indicators |
| Rent burden risk | Rent-to-income ratio exceeds 33% |
| Extreme supply pressure | New supply delivering in next 12 months exceeds 7% of existing inventory |

Set `severityRating = "HIGH"` and add to `risk_flags` with detailed description and supporting data for each red flag identified.

---

## When Data is Missing

**If fewer than 5 rent comps are available:**
- Note the shortfall in `data_quality_notes`
- Use the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md) for regional rent ranges as a supplement
- Reduce confidence to MEDIUM

**If sales comp data is scarce (<3 comps):**
- Broaden the search radius and time window (up to 3 miles, 24 months)
- Use regional cap rate data from industry sources as a proxy
- Note the limitation and its impact on cap rate analysis

**If demographic or employment data cannot be found:**
- Use U.S. Census Bureau or Bureau of Labor Statistics national/regional data as a fallback
- Note the approximation in `uncertainty_flags`

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
- [Underwriting Calculations](knowledge/underwriting-calc.md) for cap rate calculations and valuation methodology
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) for market rent ranges and occupancy benchmarks by class and region

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
