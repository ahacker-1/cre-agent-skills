---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Legal & Title Review

Reviews title commitment, survey, and legal encumbrances to identify title defects, liens, easements, and encroachments that could affect the acquisition — and verifies zoning compliance, code status, and pending litigation.

---

## When to Use This Skill

Use this skill when you need to assess the legal and title risks of a multifamily acquisition before committing to close. It is most valuable during due diligence when you want to surface title clouds, lien exposure, zoning non-conformance, open code violations, or litigation that could delay or derail closing — and to determine what curative action is needed.

---

## What You'll Need to Provide

- **Property identification** — full address, county, state, and APN/parcel number(s)
- **Current owner information** — the name and entity type of the selling entity (LLC, LP, Trust, etc.)
- **Title commitment or preliminary title report** (if already obtained) — paste or attach the exceptions list; if not yet ordered, this skill will conduct public records research
- **Survey** (if available) — ALTA survey findings, if provided
- **Zoning district** (if known) — from the offering memorandum or prior market research

---

## Mission

Review title commitment, survey, and existing legal encumbrances. Identify title defects, liens, easements, and encroachments that could affect the acquisition. Verify zoning compliance and code status. Produce a comprehensive legal risk assessment for the property.

---

## Strategy

### Step 1: Research County Assessor Records and Property Tax Records

- Search: `"{county}" county assessor property search {state}`
- Search: `"{property address}" property records`
- Extract and verify:
  - Legal description of the property
  - APN/parcel number(s) — confirm all parcels are included
  - Current assessed value (land + improvements)
  - Tax rate and annual tax amount
  - Tax payment status (current, delinquent, in arrears)
  - Special assessments (improvement districts, HOA liens)
  - Homestead or other exemptions that will be removed at sale

### Step 2: Research Property Ownership History

- Search: `"{property address}" deed transfer history`
- Search: `"{current owner entity}" property records {county} {state}`
- Document ownership chain:
  - Current owner entity name and type (LLC, LP, Trust, Individual)
  - Date of last transfer
  - Last recorded sale price (if disclosed)
  - Number of transfers in past 10 years
  - Any related-party transfers (same principals, affiliated entities)
- Flag: Frequent transfers (>3 in 5 years), entity name changes, quitclaim deeds

### Step 3: Identify Recorded Liens

Search for liens against the property and owner:

| Lien Type              | Search Method                                          | Impact    |
|------------------------|--------------------------------------------------------|-----------|
| Property tax liens     | County treasurer records                               | CRITICAL  |
| Federal tax liens      | County recorder + IRS lien search                      | CRITICAL  |
| State tax liens        | Secretary of state UCC search                          | HIGH      |
| Mechanic's liens       | County recorder                                        | HIGH      |
| Judgment liens         | Court records (county + federal)                       | HIGH      |
| HOA/assessment liens   | Property records, HOA filings                          | MEDIUM    |
| Mortgage/deed of trust | County recorder — existing financing                   | LOW (expected) |
| UCC filings            | Secretary of state — personal property security        | MEDIUM    |

- All liens must be resolved or insured over at closing
- Estimate payoff amounts for existing financing

### Step 4: Research Easements and Encumbrances

- Search: `"{property address}" easement records {county}`
- Types to identify:

| Encumbrance Type       | Common Examples                                        | Impact    |
|------------------------|--------------------------------------------------------|-----------|
| Utility easements      | Electric, gas, water, sewer, telecom right-of-way      | LOW       |
| Access easements       | Shared driveways, ingress/egress rights                | MEDIUM    |
| Drainage easements     | Stormwater management, creek setbacks                  | MEDIUM    |
| Conservation easements | Protected areas, no-build zones                        | HIGH      |
| CC&Rs/deed restrictions| Use restrictions, building height limits, design standards | HIGH  |
| Right of first refusal | Existing tenant or entity ROFR                         | CRITICAL  |
| Leasehold interests    | Ground lease, existing tenant leases                   | HIGH      |

- Assess whether each encumbrance affects property value or intended use

### Step 5: Check for Pending Litigation

- Search: `"{current owner entity}" lawsuit {state}`
- Search: `"{property address}" litigation`
- Search county and federal court records for:
  - Active lawsuits naming the property or owner
  - Tenant lawsuits (habitability, discrimination, wrongful eviction)
  - Construction defect claims
  - Environmental claims
  - Code enforcement actions
  - Condemnation proceedings
- Assess litigation risk: monetary exposure, timeline, impact on closing

### Step 6: Verify Zoning Compliance

- Search: `"{city}" zoning code {property address}`
- Search: `"{city}" zoning map` and locate parcel
- Verify:
  - Current zoning designation
  - Permitted uses under current zoning (multifamily residential must be permitted)
  - Density allowance (units per acre) vs actual density
  - Setback requirements
  - Parking requirements vs actual parking spaces
  - Height restrictions
  - Open space requirements
  - Conforming vs legal nonconforming status
- If legal nonconforming: assess expansion limitations, rebuild rights, grandfathering conditions

### Step 7: Check Code Violations, Permits, and Certificates of Occupancy

- Search: `"{city}" building permits {property address}`
- Search: `"{city}" code violations {property address}`
- Research:
  - Open code violations (fire, health, building)
  - Unpermitted work (additions, conversions, structural changes)
  - Certificate of Occupancy status (current, expired, conditional)
  - Recent permit history (work done, inspections passed/failed)
  - Fire inspection status
  - Elevator inspection certificates (if applicable)
- Flag: Any open violations, unpermitted work, or expired certificates

### Step 8: Title Insurance Assessment

Based on all findings, recommend:
- Standard vs extended coverage
- Required endorsements:
  - Survey endorsement
  - Zoning endorsement
  - Access endorsement
  - Environmental protection lien endorsement
  - Contiguity endorsement (multiple parcels)
  - Comprehensive endorsement
- Exception items to negotiate removal
- Curative items required before closing

---

## Output Format

```json
{
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",

  "property_identification": {
    "legal_description": "",
    "apn_parcels": [],
    "assessed_value_land": 0,
    "assessed_value_improvements": 0,
    "assessed_value_total": 0,
    "annual_property_tax": 0,
    "tax_status": "CURRENT | DELINQUENT | IN ARREARS",
    "special_assessments": [],
    "exemptions_to_be_removed": []
  },

  "ownership_chain": {
    "current_owner": "",
    "owner_entity_type": "",
    "date_of_last_transfer": "",
    "last_sale_price": 0,
    "transfers_past_10_years": 0,
    "ownership_history": [
      {
        "entity": "",
        "transfer_date": "",
        "instrument_type": "",
        "recorded_price": 0
      }
    ],
    "flags": []
  },

  "liens": [
    {
      "lien_type": "",
      "lienholder": "",
      "amount": 0,
      "date_recorded": "",
      "status": "ACTIVE | RELEASED | DISPUTED",
      "impact": "CRITICAL | HIGH | MEDIUM | LOW",
      "curative_action": ""
    }
  ],

  "easements_encumbrances": [
    {
      "type": "",
      "description": "",
      "beneficiary": "",
      "impact_on_value": "NONE | MINOR | MODERATE | SIGNIFICANT",
      "impact_on_use": "NONE | MINOR | MODERATE | SIGNIFICANT",
      "recommendation": ""
    }
  ],

  "litigation": {
    "pending_cases": [
      {
        "case_name": "",
        "court": "",
        "type": "",
        "status": "",
        "monetary_exposure": 0,
        "impact_on_closing": "NONE | DELAY | BLOCK"
      }
    ],
    "litigation_risk_level": "HIGH | MEDIUM | LOW | NONE"
  },

  "zoning": {
    "current_designation": "",
    "permitted_uses": [],
    "multifamily_permitted": true,
    "density_allowed": 0,
    "density_actual": 0,
    "parking_required": 0,
    "parking_actual": 0,
    "conforming_status": "CONFORMING | LEGAL NONCONFORMING | NONCONFORMING",
    "variances": [],
    "expansion_limitations": "",
    "rebuild_rights": ""
  },

  "code_compliance": {
    "open_violations": [],
    "unpermitted_work": [],
    "certificate_of_occupancy_status": "CURRENT | EXPIRED | CONDITIONAL | NONE",
    "recent_permits": [],
    "fire_inspection_status": "",
    "elevator_inspection_status": ""
  },

  "title_insurance_recommendations": {
    "coverage_type": "STANDARD | EXTENDED",
    "required_endorsements": [],
    "exceptions_to_negotiate": [],
    "curative_items_required": [
      {
        "item": "",
        "responsible_party": "SELLER | BUYER",
        "estimated_cost": 0,
        "timeline": "",
        "blocking_closing": true
      }
    ]
  },

  "risk_assessment": {
    "overall_risk_rating": "HIGH | MEDIUM | LOW",
    "title_risk": "HIGH | MEDIUM | LOW",
    "zoning_risk": "HIGH | MEDIUM | LOW",
    "litigation_risk": "HIGH | MEDIUM | LOW",
    "compliance_risk": "HIGH | MEDIUM | LOW"
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

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------| 
| exceptionsCount | 0 - 50 | Above 50 (unusual) |
| liensCount | >= 0 | Negative |
| zoningCompliance | CONFORMING, LEGAL NONCONFORMING, NONCONFORMING | Invalid enum |
| encumbrances | Each must have description | Empty description |

**Cross-Reference Validation**
- APN must match the property address provided
- Annual tax = assessed value * published mill rate (within 10%)
- Current owner must match the seller entity provided
- Multifamily use must be explicitly permitted or legally nonconforming

**Curative Item Coverage**
- All CRITICAL liens have identified curative actions
- Certificate of occupancy is current or has a clear path to renewal

**Confidence Scoring**
- Set confidence_level based on depth of records accessed
- Populate uncertainty_flags for anything that could not be confirmed via public records

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Active title dispute or lis pendens | If active litigation affects title or lis pendens is recorded against the property, flag immediately as CRITICAL |
| Fraud in title chain | If evidence of forged documents, fraudulent transfers, or identity theft in ownership chain, flag immediately as CRITICAL |
| Dissolved entity ownership | If current owner entity is dissolved, revoked, or not in good standing, flag immediately as CRITICAL |
| Property in bankruptcy estate | If property or owner is subject to active bankruptcy proceedings, flag immediately as CRITICAL |

Immediately set `severityRating = "CRITICAL"` and add to `risk_flags` with category `"dealbreaker"` if any dealbreaker is triggered. Continue analysis but surface the dealbreaker prominently in findings.

---

## When Data is Missing

**If no title commitment has been obtained:**
- Conduct public records research as a preliminary desktop review
- Clearly note that a formal title commitment from a licensed title company is required before closing and for lender compliance
- Flag any items that require a title search to verify

**If county assessor or recorder records are not accessible online:**
- Note the limitation in `data_quality_notes`
- Recommend engaging a local title company or attorney to pull physical records
- Proceed with the available information and mark affected fields as unverified

**If litigation search returns no usable results:**
- Note the searches attempted and their limitations
- Recommend a formal litigation search by a local attorney if the deal advances

**If zoning information is unavailable:**
- Contact the local planning/zoning department directly (note this as a recommended action)
- Use publicly available GIS or zoning map tools as a secondary source
- Do not assume compliance — flag as unknown and require verification before closing

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
- [Risk Scoring Framework](knowledge/risk-scoring.md) for legal and title risk scoring methodology and risk flag definitions
- [Legal Checklist](knowledge/legal-checklist.md) for a comprehensive due diligence checklist of required legal items

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
