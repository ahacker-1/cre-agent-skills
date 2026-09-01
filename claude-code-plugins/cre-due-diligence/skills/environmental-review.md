---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Environmental Review

Assesses environmental risks for a multifamily property — reviewing Phase I ESA scope, identifying recognized environmental conditions (RECs), evaluating hazardous materials risks, and recommending additional testing or insurance to protect the buyer from unknown liabilities.

---

## When to Use This Skill

Use this skill when you need to identify environmental liabilities before acquiring a multifamily property. It is most valuable during due diligence when you want to understand what hazardous conditions may exist (asbestos, lead paint, contaminated soil, flood exposure), estimate remediation costs, and determine whether a Phase II environmental study is warranted.

---

## What You'll Need to Provide

- **Property details** — full address, year built, unit count, and building type
- **Prior use information** (if known) — any notes on what occupied the site before the current building (industrial, agricultural, gas station, etc.)
- **Phase I ESA report** (if already obtained) — paste or attach the findings; if not yet ordered, this skill will conduct preliminary desktop research to inform whether one is needed
- **Property class and building age** — used to flag age-specific hazardous materials (lead, asbestos)

---

## Mission

Assess environmental risks for the property. Review Phase I ESA scope, identify recognized environmental conditions (RECs), evaluate hazardous materials risks, and recommend additional testing or insurance. Produce a comprehensive environmental risk assessment that protects the buyer from unknown liabilities.

---

## Strategy

### Step 1: Research Property History and Prior Uses

- Search: `"{property address}" history prior use`
- Search: `"{property address}" Sanborn map historical`
- Search: `"{city}" land use history {parcel_area}`
- Investigate:

| Research Area          | Questions to Answer                                    |
|------------------------|--------------------------------------------------------|
| Current use            | Residential multifamily — confirm                     |
| Prior use (most recent)| What was on this site before the current building?     |
| Historical use         | Any industrial, manufacturing, or gas station use?     |
| Adjacent use           | What are neighboring properties used for?              |
| Redevelopment          | Was this a brownfield redevelopment?                   |
| Agricultural           | Was this previously farmland (pesticide concerns)?     |

- Flag any prior use involving:
  - Gas stations, dry cleaners, auto repair, manufacturing
  - Chemical storage, petroleum products, heavy metals
  - Agricultural operations (pesticides, herbicides)
  - Military installations, munitions

### Step 2: Search Environmental Databases

Search federal, state, and local environmental databases:

| Database                    | Search Method                                         | What to Find                      |
|-----------------------------|-------------------------------------------------------|-----------------------------------|
| EPA Superfund/CERCLIS       | Search: `"EPA" "Superfund" near "{property address}"` | NPL sites within 1 mile          |
| EPA RCRA                    | Search: `"EPA" "RCRA" "{city}" hazardous waste`      | RCRA generators/TSD facilities    |
| EPA Envirofacts             | Navigate EPA Envirofacts portal for address           | Facility environmental records    |
| State DEQ/ADEQ             | Search: `"{state}" DEQ contaminated sites "{city}"`  | State cleanup sites               |
| Brownfields                 | Search: `"brownfield" "{property address}" OR "{city}"` | Brownfield inventory            |
| UST Registry                | Search: `"underground storage tank" "{property address}" {state}` | UST records          |
| LUST (Leaking UST)         | Search: `"leaking underground storage tank" "{city}" {state}` | Known leaks nearby        |
| Toxic Release Inventory    | Search: `"TRI" "{zip code}" toxic release`           | Toxic releases nearby             |
| State spill database       | Search: `"{state}" spill report "{city}"`            | Known spills in area              |

For each database hit:
- Record distance from subject property
- Classify: ON-SITE, ADJACENT (<0.25 mi), NEARBY (0.25-1 mi), DISTANT (>1 mi)
- Assess potential impact on subject property (groundwater flow direction matters)

### Step 3: Check Flood Zone Status

- Search: `"FEMA flood zone" "{property address}"`
- Search: `"FEMA flood map" "{city}" "{zip code}"`
- Determine:

| Flood Zone | Description                           | Impact                              |
|------------|---------------------------------------|--------------------------------------|
| Zone X     | Minimal flood hazard                  | No flood insurance required         |
| Zone X500  | 0.2% annual chance (500-year flood)   | Low risk, insurance recommended     |
| Zone A/AE  | 1% annual chance (100-year flood)     | Flood insurance REQUIRED by lenders |
| Zone V/VE  | Coastal high hazard area              | Flood insurance REQUIRED, high cost |

- If in flood zone: estimate annual flood insurance premium
- Check for recent flood history at or near the property
- Check community's NFIP participation status

### Step 4: Assess Hazardous Materials by Property Age

| Age Trigger    | Hazard                    | Requirement / Action                              |
|----------------|---------------------------|---------------------------------------------------|
| Pre-1978       | Lead-based paint (LBP)    | Federal disclosure required (42 USC 4852d)        |
|                |                           | Testing recommended, abatement/encapsulation cost |
| Pre-1981       | Asbestos-containing       | ACM likely in: floor tiles, pipe insulation,      |
|                | materials (ACM)           | popcorn ceilings, roofing, siding                 |
|                |                           | Survey required before renovation                  |
| Any age        | Mold                      | Check for moisture intrusion, HVAC condition       |
|                |                           | Common complaint in resident reviews               |
| Any age        | Radon                     | Check EPA radon zone map for the county            |
|                |                           | Zone 1 = highest risk (>4 pCi/L predicted)        |
| Pre-2010       | Chinese drywall           | Florida/Gulf Coast properties 2001-2009 vintage    |
| Any age        | Underground storage tanks | Check UST registry, look for fill pipes, vents    |
| Near highways  | Air quality               | Properties within 500ft of major highways          |
| Near airports  | Noise/air quality         | Airport noise contours, fuel contamination         |

For each hazard identified:
- Classify risk: CONFIRMED, LIKELY, POSSIBLE, UNLIKELY
- Estimate testing cost
- Estimate remediation cost range (if applicable)

### Step 5: Research Nearby Environmental Hazards

Map environmental hazards within a 1/4 mile radius:

| Hazard Type           | Search Strategy                                       | Risk Impact |
|-----------------------|-------------------------------------------------------|-------------|
| Gas stations          | Search: `gas station near "{property address}"`       | UST leaks, benzene |
| Dry cleaners          | Search: `dry cleaner near "{property address}"`       | PCE/TCE contamination |
| Auto repair shops     | Search: `auto repair near "{property address}"`       | Oil, solvents, metals |
| Industrial sites      | Search: `industrial "{submarket}" manufacturing`      | Various chemicals |
| Landfills             | Search: `landfill near "{property address}"`          | Methane, leachate |
| Rail lines            | Search: `railroad near "{property address}"`          | Diesel, creosote |
| Agricultural land     | Search: `farmland near "{property address}"`          | Pesticides, nitrates |
| High-voltage lines    | Visual/satellite review                               | EMF concerns |

For each nearby hazard:
- Distance from subject property
- Direction relative to groundwater flow (if known)
- Current status (active, closed, remediated)
- Potential impact on subject

### Step 6: Evaluate Wetlands and Protected Areas

- Search: `"wetlands" near "{property address}" {state}`
- Search: `"National Wetland Inventory" "{property address}"`
- Search: `"endangered species" habitat "{city}" {state}`
- Check for:
  - Jurisdictional wetlands on or adjacent to property
  - Protected species habitats
  - Riparian buffers or setbacks
  - Conservation easements (cross-reference with title review if available)
- Impact: development restrictions, stormwater management requirements, mitigation costs

### Step 7: Assess Need for Phase II ESA

Based on all findings, recommend Phase II testing if:

| Trigger                                    | Phase II Component Recommended        | Est. Cost    |
|--------------------------------------------|---------------------------------------|-------------|
| Former gas station on-site or adjacent     | Soil borings, groundwater monitoring  | $10K - $30K |
| Former dry cleaner on-site or adjacent     | Soil gas survey, groundwater sampling | $8K - $25K  |
| USTs found or suspected                    | Geophysical survey, soil borings      | $5K - $20K  |
| Database hits within 1/4 mile (upgradient) | Groundwater monitoring wells          | $10K - $25K |
| Mold complaints or moisture issues         | Mold testing, moisture survey         | $2K - $5K   |
| Pre-1978 with renovation planned           | Lead-based paint survey               | $3K - $8K   |
| Pre-1981 with renovation planned           | Asbestos survey (AHERA)              | $3K - $10K  |
| Radon Zone 1                               | Radon testing (multiple units)        | $1K - $3K   |

Decision framework:
- If 0 triggers: Phase II NOT recommended
- If 1-2 LOW triggers: Phase II OPTIONAL, targeted testing
- If any HIGH trigger: Phase II RECOMMENDED
- If multiple HIGH triggers: Phase II REQUIRED

### Step 8: Estimate Environmental Insurance Needs

- **Pollution Legal Liability (PLL) insurance**: Recommended if any RECs identified
  - Typical premium: $2,000 - $10,000/year depending on risk profile
  - Covers: cleanup costs, third-party claims, business interruption
- **Flood insurance**: Required if in Zone A/AE/V/VE
  - NFIP rates or private flood insurance
  - Estimate annual premium based on zone and building type
- **Mold insurance**: Consider if moisture issues identified
  - Often excluded from standard property policies

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "property_profile": {
    "address": "",
    "year_built": 0,
    "property_age": 0,
    "building_type": "",
    "prior_uses": [],
    "current_use": "Multifamily Residential"
  },

  "historical_use_summary": {
    "prior_use_timeline": [
      {
        "period": "",
        "use": "",
        "environmental_concern": "YES | NO",
        "details": ""
      }
    ],
    "historical_risk_level": "HIGH | MEDIUM | LOW"
  },

  "database_search_results": {
    "total_hits": 0,
    "on_site_hits": [],
    "adjacent_hits": [],
    "nearby_hits": [],
    "databases_searched": [
      {
        "database": "",
        "searched": true,
        "hits": 0,
        "relevant_findings": []
      }
    ]
  },

  "recognized_environmental_conditions": [
    {
      "rec_type": "REC | CREC | HREC | DE MINIMIS",
      "description": "",
      "source": "",
      "distance_from_property": "",
      "risk_level": "HIGH | MEDIUM | LOW",
      "recommended_action": ""
    }
  ],

  "flood_zone": {
    "fema_zone": "",
    "zone_description": "",
    "flood_insurance_required": true,
    "estimated_annual_premium": 0,
    "recent_flood_history": "",
    "nfip_community_status": ""
  },

  "hazardous_materials": {
    "lead_based_paint": {
      "risk": "CONFIRMED | LIKELY | POSSIBLE | UNLIKELY | N/A",
      "basis": "",
      "testing_cost_estimate": 0,
      "remediation_cost_estimate": { "low": 0, "high": 0 },
      "disclosure_required": true
    },
    "asbestos": {
      "risk": "CONFIRMED | LIKELY | POSSIBLE | UNLIKELY | N/A",
      "basis": "",
      "likely_locations": [],
      "testing_cost_estimate": 0,
      "abatement_cost_estimate": { "low": 0, "high": 0 }
    },
    "mold": {
      "risk": "CONFIRMED | LIKELY | POSSIBLE | UNLIKELY",
      "basis": "",
      "testing_cost_estimate": 0,
      "remediation_cost_estimate": { "low": 0, "high": 0 }
    },
    "radon": {
      "epa_zone": "",
      "risk": "HIGH | MODERATE | LOW",
      "testing_cost_estimate": 0,
      "mitigation_cost_estimate": { "low": 0, "high": 0 }
    },
    "usts": {
      "found": false,
      "details": "",
      "removal_cost_estimate": 0
    },
    "other_hazards": []
  },

  "nearby_hazards": [
    {
      "type": "",
      "name_or_description": "",
      "distance_ft": 0,
      "direction": "",
      "status": "ACTIVE | CLOSED | REMEDIATED",
      "potential_impact": "HIGH | MEDIUM | LOW",
      "contaminants_of_concern": []
    }
  ],

  "wetlands_protected_areas": {
    "wetlands_present": false,
    "wetlands_details": "",
    "protected_species_habitat": false,
    "conservation_easements": false,
    "development_restrictions": ""
  },

  "phase_ii_recommendation": {
    "recommended": true,
    "urgency": "REQUIRED | RECOMMENDED | OPTIONAL | NOT NEEDED",
    "scope": [
      {
        "test_type": "",
        "trigger": "",
        "estimated_cost": { "low": 0, "high": 0 },
        "estimated_timeline_days": 0
      }
    ],
    "total_phase_ii_cost_estimate": { "low": 0, "high": 0 }
  },

  "insurance_recommendations": {
    "pollution_legal_liability": {
      "recommended": true,
      "basis": "",
      "estimated_annual_premium": { "low": 0, "high": 0 }
    },
    "flood_insurance": {
      "required": false,
      "estimated_annual_premium": 0
    },
    "mold_insurance": {
      "recommended": false,
      "estimated_annual_premium": 0
    },
    "total_environmental_insurance_annual": 0
  },

  "environmental_risk_score": {
    "total_score": 0,
    "rating": "LOW | MODERATE | ELEVATED | HIGH | CRITICAL",
    "component_scores": {
      "historical_use": 0,
      "database_hits": 0,
      "hazardous_materials": 0,
      "flood_risk": 0,
      "nearby_hazards": 0,
      "wetlands_protected": 0
    }
  },

  "remediation_cost_summary": {
    "immediate_costs": 0,
    "testing_costs": 0,
    "potential_remediation_low": 0,
    "potential_remediation_high": 0,
    "insurance_costs_annual": 0,
    "total_environmental_budget_low": 0,
    "total_environmental_budget_high": 0
  },

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
- All cost estimates have both low and high range values

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| environmental_risk_score.total_score | 0 - 100 | Outside range |
| component_scores.* | 0 - 100 each | Any outside range |
| estimatedRemediationCost | >= 0 | Negative |
| phase_ii_recommendation.urgency | REQUIRED, RECOMMENDED, OPTIONAL, NOT NEEDED | Invalid enum |
| flood_zone.fema_zone | Known FEMA zone codes | Unknown zone |
| hazardous_materials.*.risk | CONFIRMED, LIKELY, POSSIBLE, UNLIKELY, N/A | Invalid enum |

**Age-Based Hazard Validation**
- If year_built < 1978: lead risk cannot be "N/A" or "UNLIKELY"
- If year_built < 1981: asbestos risk cannot be "N/A" or "UNLIKELY"
- If any HIGH risk REC exists: Phase II must be RECOMMENDED or REQUIRED

**Database Coverage**
- At least 5 environmental databases searched
- FEMA flood zone must be determined
- Property address confirmed in output

**Confidence Scoring**
- Set confidence_level based on data completeness and source quality
- Populate uncertainty_flags for any estimated or assumed values

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Active environmental contamination (unquantified) | If confirmed contamination exists with unknown scope or remediation cost, flag immediately as CRITICAL |
| Demolition order or condemnation (environmental cause) | If environmental condition has triggered demolition order or condemnation, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if any dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If Phase I ESA has not been conducted:**
- This skill performs desktop-level research as a preliminary assessment only
- Clearly note that a formal Phase I ESA (ASTM E1527-21) is required for any serious acquisition and for lender compliance
- Flag all age-based hazards conservatively based on year built

**If environmental database searches return no usable results:**
- Note the limitation and the search queries attempted
- Treat absence of database data as inconclusive (not as confirmation of no contamination)
- Recommend a professional Phase I ESA to cover the gap

**If FEMA flood zone cannot be determined:**
- Note the gap and recommend confirming via FEMA's Flood Map Service Center (msc.fema.gov)
- Assume Zone X (minimal hazard) only if the address is inland and at elevation — otherwise treat as unknown

**If prior use history is unavailable:**
- Research historical Sanborn fire insurance maps and county aerial photograph archives as alternatives
- Default to conservative risk assumptions when history is unknown

For any assumed or estimated value:
- Add to `uncertainty_flags`: `{ "field": "{name}", "reason": "Data unavailable - using {method}", "confidence": "LOW" }`
- Use the Risk Scoring Framework knowledge base (knowledge/risk-scoring.md) for risk classification guidance
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
- [Risk Scoring Framework](knowledge/risk-scoring.md) for environmental risk scoring methodology and REC classification standards

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
