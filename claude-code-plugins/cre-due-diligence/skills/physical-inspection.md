---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Physical Inspection Analyst

Evaluates a property's physical condition from available data, estimates deferred maintenance costs and CapEx requirements, and produces a comprehensive condition assessment that informs the buyer's capital plan and risk analysis.

---

## When to Use This Skill

Use this skill when you need to assess the physical condition of a multifamily property and estimate the capital investment required — whether for deferred maintenance, planned system replacements, or a value-add renovation. It is most valuable during due diligence when you need to translate property age, building vintage, and observable condition into a defensible CapEx budget.

---

## What You'll Need to Provide

- **Property details** — address, year built, unit count, total square footage, building type (garden/mid-rise/high-rise), number of stories, property class (A/B/C/D), and parking type
- **Construction details** (if available) — construction type (wood frame, steel, concrete), roof type, HVAC type, utility metering configuration, and amenities list
- **Listing or offering data** (if available) — photos, seller-provided condition notes, and descriptions of any recent renovations
- **Value-add intent** — indicate if this is a value-add acquisition (affects renovation budget analysis)

---

## Mission

Evaluate property physical condition from available data. Estimate deferred maintenance costs, CapEx requirements, and renovation budget. Provide a comprehensive condition assessment that informs the buyer's capital plan and risk analysis.

---

## Strategy

### Step 1: Research Property Age and Lifecycle Issues

- Calculate property age: `current_year - year_built`
- Determine building vintage category:
  - Pre-1970: Cast iron plumbing, potential asbestos, aluminum wiring risk
  - 1970-1985: Polybutylene plumbing risk, original HVAC likely past life
  - 1985-2000: Potential EIFS issues, original roofs at end of life
  - 2000-2010: Generally sound, check for construction defect era issues
  - 2010+: Relatively new, focus on warranty status and builder quality
- Identify era-specific construction risks

### Step 2: Research Property Photos, Reviews, and Inspection Data

- Search for the property on Google Maps (satellite + street view clues)
- Search listing sites (Apartments.com, Google Reviews) for:
  - Resident complaints indicating maintenance issues
  - Photos showing condition of common areas, units, exterior
- Search for any public inspection reports or code violation records
- Search for building permits (recent work done, scope of past renovations)
- Document all findings with sources

### Step 3: Evaluate Major Building Systems

Assess each system against expected useful life:

| System              | Expected Life (years) | Replacement Cost Range (per unit) | Key Indicators                          |
|---------------------|----------------------|------------------------------------|------------------------------------------|
| Roof (flat/TPO)     | 20-25                | $2,000 - $5,000                    | Age, patches, ponding, leaks reported   |
| Roof (shingle)      | 20-30                | $1,500 - $3,500                    | Curling, missing shingles, granule loss |
| HVAC (central)      | 15-20                | $3,000 - $8,000                    | Age, R-22 refrigerant, efficiency       |
| HVAC (PTAC/window)  | 7-12                 | $800 - $2,000                      | Age, noise complaints, cooling capacity |
| Plumbing (supply)   | 40-50                | $3,000 - $8,000                    | Pipe material, leak history, water pressure |
| Plumbing (drain)    | 50-75                | $2,000 - $6,000                    | Material, backups, camera scope needed  |
| Electrical          | 30-40                | $1,500 - $4,000                    | Panel capacity, wiring type, code compliance |
| Windows             | 20-30                | $300 - $800 per window             | Single vs double pane, seals, operability |
| Siding/facade       | 20-40                | $2,000 - $5,000                    | Material type, condition, moisture intrusion |
| Foundation          | 50-100               | $5,000 - $20,000                   | Cracks, settling, drainage              |
| Parking surface     | 15-25                | $2 - $5 per sqft                   | Cracking, striping, drainage            |
| Elevators           | 20-25 (modernize)    | $75,000 - $200,000 each            | Age, compliance, service records        |
| Fire/Life Safety    | 10-20                | $500 - $2,000                      | Sprinklers, alarms, extinguishers       |
| Hot Water (central) | 10-15                | $5,000 - $15,000                   | Type, age, capacity, efficiency         |
| Hot Water (individual) | 8-12              | $800 - $1,500                      | Type, age                               |

For each system:
- Calculate remaining useful life: `expected_life - (current_year - install_year)`
- If install year unknown, assume original to building unless evidence otherwise
- Classify: GOOD (>50% life remaining), FAIR (25-50%), POOR (<25%), CRITICAL (past life)

### Step 4: Estimate Deferred Maintenance

- Sum all systems rated POOR or CRITICAL for immediate deferred maintenance
- Apply condition multiplier:
  - Class A property: 0.8x (better maintained)
  - Class B property: 1.0x (baseline)
  - Class C property: 1.3x (typically more deferred)
  - Class D property: 1.6x (significant deferred likely)
- Calculate total deferred maintenance estimate (low/mid/high range)
- Categorize: IMMEDIATE (year 1), SHORT-TERM (years 1-2), MEDIUM-TERM (years 3-5)

### Step 5: ADA Compliance Considerations

- Properties built before 1991: May not meet current ADA standards
- Check for common ADA deficiencies:
  - Accessible parking spaces and signage
  - Accessible path of travel to building entrance
  - Accessible common area restrooms
  - Accessible leasing office
  - Fair Housing Act requirements for ground-floor units (post-1991)
- Estimate ADA remediation costs if applicable

### Step 6: CapEx Reserve Estimation

Build a 5-year CapEx schedule:
- Year 1: Immediate/critical items + deferred maintenance
- Years 2-3: Short-term replacement items
- Years 4-5: Planned lifecycle replacements
- Annual reserve per unit: $250 - $500 (class dependent)

Calculate:
- Total 5-year CapEx budget
- Average annual CapEx per unit
- CapEx as percentage of revenue

### Step 7: Renovation Budget (Value-Add Properties)

If the deal involves value-add repositioning:

| Renovation Scope | Cost per Unit    | Typical Inclusions                                        |
|------------------|------------------|-----------------------------------------------------------|
| Light            | $5,000 - $10,000 | Paint, fixtures, hardware, lighting, minor appliances     |
| Moderate         | $10,000 - $20,000| Countertops, cabinets (reface), flooring, appliances, bath fixtures |
| Heavy            | $20,000 - $40,000| Full kitchen/bath gut, layout changes, windows, HVAC      |

Estimate:
- Per-unit renovation cost by scope
- Total renovation budget
- Exterior/common area improvements budget
- Amenity additions budget (dog park, fitness center, package lockers)
- Renovation timeline (units per month, total months to stabilize)
- Expected rent premium post-renovation

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "property_profile": {
    "year_built": 0,
    "property_age": 0,
    "vintage_category": "",
    "construction_type": "",
    "building_type": "",
    "stories": 0,
    "units": 0,
    "total_sqft": 0,
    "class": ""
  },

  "system_assessments": [
    {
      "system": "Roof",
      "type": "",
      "estimated_install_year": 0,
      "expected_useful_life": 0,
      "remaining_useful_life": 0,
      "condition_rating": "EXCELLENT | GOOD | FAIR | POOR | CRITICAL",
      "replacement_cost_estimate": {
        "low": 0,
        "mid": 0,
        "high": 0
      },
      "notes": "",
      "evidence": []
    }
  ],

  "overall_condition_rating": "EXCELLENT | GOOD | FAIR | POOR",

  "deferred_maintenance": {
    "immediate_items": [],
    "short_term_items": [],
    "medium_term_items": [],
    "total_estimate": {
      "low": 0,
      "mid": 0,
      "high": 0
    },
    "per_unit_estimate": 0,
    "class_multiplier_applied": 0
  },

  "ada_compliance": {
    "building_subject_to_ada": true,
    "deficiencies_identified": [],
    "remediation_cost_estimate": 0,
    "risk_level": "HIGH | MEDIUM | LOW | N/A"
  },

  "capex_schedule": {
    "year_1": 0,
    "year_2": 0,
    "year_3": 0,
    "year_4": 0,
    "year_5": 0,
    "total_5_year": 0,
    "avg_annual_per_unit": 0,
    "capex_as_pct_of_revenue": 0,
    "line_items": [
      {
        "item": "",
        "year": 0,
        "cost_estimate": 0,
        "priority": "CRITICAL | HIGH | MEDIUM | LOW"
      }
    ]
  },

  "renovation_budget": {
    "scope": "LIGHT | MODERATE | HEAVY | N/A",
    "per_unit_cost": {
      "low": 0,
      "mid": 0,
      "high": 0
    },
    "total_interior_budget": 0,
    "exterior_improvements": 0,
    "amenity_additions": 0,
    "total_renovation_budget": 0,
    "units_per_month": 0,
    "total_months_to_complete": 0,
    "expected_rent_premium": 0,
    "expected_rent_premium_pct": 0
  },

  "major_issues": [],
  "risk_flags": [],
  "recommendations": [],
  "confidence_level": "HIGH | MEDIUM | LOW",
  "data_quality_notes": [],
  "photo_evidence_urls": [],
  "review_excerpts": [],
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
- All 15 major building systems have assessments
- All 7 strategy steps have produced output or a documented data gap

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| conditionScore | 0 - 100 | Outside range |
| deferredMaintenance | >= 0 | Negative |
| deferredMaintenancePerUnit | $0 - $50,000 | Above $50K/unit |
| capExTotal5Year | >= sum of individual capExNeeds | Less than sum |
| systemAges.*.age | 0 - 100 years | Impossible age |
| systemAges.*.remainingLife | >= 0 | Negative remaining life |

**Reasonableness Checks**
- Property age matches year_built calculation
- No single system replacement exceeds total property value * 10%
- Annual CapEx per unit between $200-$2,000
- If value-add: rent premium must exceed renovation cost amortized over 5 years
- Overall condition rating aligns with individual system ratings

**Confidence Scoring**
- Set confidence_level based on data completeness and evidence quality
- Populate uncertainty_flags for any estimated or assumed values (especially for systems where install year is assumed)

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Structural failure requiring demolition | If foundation, structural framing, or load-bearing elements are beyond repair, flag immediately as CRITICAL |
| Uninsurable property condition | If property condition makes insurance unavailable or prohibitively expensive, flag immediately as CRITICAL |
| Demolition order or condemnation | If active demolition order or condemnation notice is discovered, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if any dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If year built or construction type is unknown:**
- Estimate vintage category from listing photos, permit records, and architectural style
- Note the estimate and its basis in `uncertainty_flags`
- Use the most conservative lifecycle assumptions for the estimated era

**If system install years are unknown:**
- Assume all systems are original to the building unless there is evidence of replacement
- Apply conservative remaining life estimates
- Flag these as assumptions in `uncertainty_flags`

**If no photos or inspection reports are available:**
- Conduct web research for Google Maps imagery, listing photos, and resident reviews
- Note the data gap and reduce confidence to MEDIUM or LOW
- Apply conservative cost estimates until a physical inspection can confirm

**If CapEx cost data cannot be verified locally:**
- Use the Multifamily Benchmarks knowledge base (knowledge/multifamily-benchmarks.md) for system lifecycle standards and cost per unit benchmarks by class and region
- Note regional cost variation as a factor in confidence scoring

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
- [Underwriting Calculations](knowledge/underwriting-calc.md) for CapEx projections and renovation ROI calculations
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) for system lifecycle standards and cost per unit benchmarks by class and region

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
