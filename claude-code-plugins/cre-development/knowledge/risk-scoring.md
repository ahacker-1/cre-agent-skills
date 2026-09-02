# Risk Scoring - Multifamily Acquisition

> **What this is:** A complete risk scoring framework for multifamily acquisitions, covering 9 risk categories (6 standard CRE + 3 multifamily-specific), with scoring criteria, automatic escalation rules, mitigation strategies, and structured output formats.
> **How to use it:** Load this knowledge base alongside any skill file that references it, or use it as a standalone reference for conducting systematic due diligence risk assessments on multifamily properties.

This document defines the complete risk scoring framework for multifamily acquisition analysis. The framework covers 9 risk categories: 6 standard CRE categories plus 3 multifamily-specific categories.

---

## Scoring System

### Risk Levels

| Level | Score Range | Color | Meaning |
|-------|-----------|-------|---------|
| LOW | 0-25 | Green | Minimal risk, no action required |
| MEDIUM | 26-50 | Yellow | Moderate risk, monitor and document |
| HIGH | 51-75 | Orange | Significant risk, requires mitigation plan |
| CRITICAL | 76-100 | Red | Severe risk, potential dealbreaker |

### Scoring Method

Each risk factor within a category is scored 0-100. The category score is the weighted average of its risk factors. The overall deal risk score is the weighted average of all category scores (see Risk Weighting by Strategy below).

```
Category Score = Sum(Factor Score x Factor Weight) / Sum(Factor Weights)
Overall Risk Score = Sum(Category Score x Category Weight) / Sum(Category Weights)
```

---

## 1. Ownership & Title Risk

Analyzes the property's ownership history, title chain, and any encumbrances that could complicate acquisition.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Ownership changes (5yr) | 0-1 transfers | 2 transfers | 3 transfers | 4+ transfers (flip pattern) |
| Lien status | No liens | Resolved liens in history | Active liens being resolved | Active unresolved liens |
| Title disputes | None | Historical, resolved | Active dispute, likely to resolve | Active dispute, outcome uncertain |
| Entity structure | Simple LLC/individual | Multi-member LLC | Nested entities | Offshore or untraceable |
| Easements/encumbrances | Standard utility | Non-standard but manageable | Restrictive easement | Easement blocks intended use |
| Tax payment history | Current, no delinquency | Prior delinquency, now current | Currently 1 year behind | 2+ years delinquent or tax sale |

### Automatic Escalations
- Active title dispute with uncertain outcome: Minimum CRITICAL (80)
- Property in tax foreclosure: Minimum CRITICAL (90)
- Ownership chain cannot be verified: Minimum HIGH (60)

---

## 2. Legal & Litigation Risk

Identifies pending or historical litigation, code violations, and legal encumbrances that could affect the property or transaction.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Active lawsuits | None | 1 minor claim (<$50K) | Multiple or significant claims | Material litigation (>$500K) |
| Code violations | None | Minor, correctable | Multiple or structural | Condemnation proceedings |
| Tenant lawsuits | None | 1 historical, resolved | Active tenant litigation | Class action or pattern of suits |
| Zoning violations | None | Minor variance needed | Existing non-conforming use | Active enforcement action |
| HOA/Association issues | None or compliant | Minor assessment disputes | Special assessments pending | Litigation with association |
| Permit history | Clean | Minor unpermitted work | Significant unpermitted work | Structural unpermitted modifications |

### Automatic Escalations
- Active condemnation proceedings: Minimum CRITICAL (90)
- Class action tenant lawsuit: Minimum CRITICAL (85)
- Structural work without permits: Minimum HIGH (65)

---

## 3. Environmental Risk

Assesses environmental contamination, hazardous materials, and regulatory compliance that could result in liability or remediation costs.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Phase I ESA | Clean, no RECs | De minimis conditions | Recognized environmental conditions | Multiple RECs, Phase II recommended |
| Proximity to Superfund | >1 mile | 0.5-1 mile | 0.25-0.5 mile | <0.25 mile or on NPL list |
| Asbestos | None or abated | Encapsulated, managed | Present, needs abatement plan | Friable asbestos, immediate hazard |
| Lead paint | Post-1978 or abated | Pre-1978, managed | Pre-1978, not managed | Active exposure risk |
| Underground storage | None on record | Removed, clean closure | Removed, residual contamination | Active USTs, unknown status |
| Flood zone | Zone X (minimal) | Zone B/C (moderate) | Zone A (high risk, insurable) | Zone V or floodway |
| Mold history | None | Historical, remediated | Active, treatable | Systemic, structural moisture |

### Automatic Escalations
- Active EPA enforcement action: Minimum CRITICAL (90)
- Friable asbestos requiring immediate action: Minimum CRITICAL (85)
- Property on Superfund NPL list: Minimum CRITICAL (95)
- Unresolved Phase II contamination: Minimum HIGH (65)

---

## 4. Zoning & Regulatory Risk

Evaluates whether current use is legal, whether intended use is permitted, and what regulatory hurdles exist.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Current use conformity | Fully conforming | Legal non-conforming (grandfathered) | Non-conforming, variance needed | Non-conforming, no variance path |
| Intended use allowed | By right | Conditional use (likely) | Conditional use (uncertain) | Not permitted, rezone required |
| Density compliance | Under maximum | At maximum | Over maximum (grandfathered) | Over maximum (not grandfathered) |
| Parking compliance | Meets code | Minor shortfall | Significant shortfall | Major shortfall, no waiver path |
| Building code compliance | Current code | Minor updates needed | Significant updates on renovation | Full code compliance required |
| Entitlements (if needed) | Not needed | Approved/in process | Application stage | Not yet applied, uncertain |

### Automatic Escalations
- Intended use not permitted and rezone required: Minimum HIGH (70)
- Non-conforming use without grandfathering: Minimum CRITICAL (80)
- Active zoning enforcement: Minimum HIGH (65)

---

## 5. Financial Risk

Analyzes the financial viability of the acquisition based on income quality, expense levels, debt structure, and return projections.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| NOI trend | Growing >3%/yr | Stable (0-3%) | Declining 0-5% | Declining >5% |
| Occupancy | >95% | 90-95% | 80-90% | <80% |
| Rent vs market | At or below market | 5-10% above market | 10-20% above market | >20% above market |
| OpEx ratio | <40% | 40-50% | 50-60% | >60% |
| DSCR | >1.40x | 1.25-1.40x | 1.10-1.25x | <1.10x |
| Debt yield | >11% | 9-11% | 7-9% | <7% |
| Cap rate spread | >250 bps | 150-250 bps | 100-150 bps | <100 bps |
| Seller financials | Audited/verified | Unaudited but consistent | Inconsistencies noted | Material discrepancies |

### Automatic Escalations
- DSCR < 1.00x: Minimum CRITICAL (90) -- debt service not covered
- Occupancy < 70% without lease-up plan: Minimum CRITICAL (85)
- Material financial discrepancies: Minimum HIGH (70)

---

## 6. Market Risk

Evaluates the strength and trajectory of the local market, including supply/demand dynamics, economic fundamentals, and comparable transactions.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Population growth | >1.5%/yr | 0.5-1.5%/yr | 0-0.5%/yr | Declining |
| Employment growth | >2%/yr | 1-2%/yr | 0-1%/yr | Declining |
| Rent growth trend | >3%/yr | 1-3%/yr | 0-1%/yr | Declining |
| New supply pipeline | <2% of stock | 2-4% of stock | 4-6% of stock | >6% of stock |
| Market vacancy | <5% | 5-7% | 7-10% | >10% |
| Employer concentration | Diversified | Top 3 = 20-30% | Top 3 = 30-50% | Top 3 > 50% |
| Comparable sales volume | Active (>10/yr in submarket) | Moderate (5-10/yr) | Limited (2-5/yr) | Very limited (<2/yr) |
| Submarket trend | Improving | Stable | Mixed signals | Declining |

### Automatic Escalations
- Population decline + employment decline: Minimum HIGH (65)
- New supply > 8% of existing stock: Minimum HIGH (60)
- Single employer > 40% of local jobs: Minimum HIGH (65)

---

## 7. Tenant Concentration Risk

*Multifamily-specific.* Evaluates risks related to tenant mix, income source concentration, lease expiration patterns, and dependency on specific tenant types or programs.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Single tenant revenue share | No tenant >5% of revenue | Largest tenant 5-10% | Largest tenant 10-20% | Largest tenant >20% |
| Government/Section 8 concentration | <20% of units | 20-40% of units | 40-60% of units | >60% of units |
| Lease expiration clustering | Spread evenly | 20-30% expire same quarter | 30-50% expire same quarter | >50% expire same quarter |
| Master lease dependency | No master lease | Master lease with strong guarantor | Master lease with adequate guarantor | Master lease with weak/no guarantor |
| Corporate housing share | <10% of units | 10-25% of units | 25-40% of units | >40% of units |
| Student housing share (non-purpose-built) | <10% of units | 10-25% of units | 25-50% of units | >50% of units |
| Average tenant tenure | >3 years | 2-3 years | 1-2 years | <1 year |
| Income verification quality | All verified | >80% verified | 50-80% verified | <50% verified |

### Key Metrics to Calculate

```
Tenant Concentration Index = Revenue from top 5 tenants / Total Revenue
Lease Rollover Risk = % of leases expiring in next 6 months
Government Program Dependency = Section 8/VASH/Other program units / Total units
Tenant Diversity Score = 100 - (Concentration Index x 100)
```

### Automatic Escalations
- Single tenant > 30% of revenue (non-master-lease): Minimum HIGH (65)
- > 70% government program concentration: Minimum HIGH (60) -- funding/policy change risk
- > 60% lease expirations in single quarter: Minimum HIGH (65)
- Master lease with guarantor in financial distress: Minimum CRITICAL (80)

---

## 8. Physical Condition Risk

*Multifamily-specific.* Evaluates the physical condition of the building systems, structural elements, and common areas. Poor physical condition drives unexpected capital costs and affects resident satisfaction and retention.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Roof age/condition | <10 years, good condition | 10-15 years, fair | 15-20 years, needs attention | >20 years or active leaks |
| HVAC systems | <10 years | 10-15 years | 15-20 years | >20 years or failing |
| Plumbing type | Copper/PEX | PVC (appropriate use) | Cast iron (aging) | Galvanized or polybutylene |
| Electrical capacity | Meets current needs | Minor upgrades needed | Panel upgrades needed | Knob-and-tube or major rewiring |
| Foundation | No issues | Hairline cracks, cosmetic | Settlement cracks, monitored | Active structural movement |
| Pest/mold history | None | Historical, treated | Recurring issues | Active infestation/systemic mold |
| ADA compliance | Fully compliant | Minor gaps, easily addressed | Significant gaps, costly to fix | Major non-compliance, enforcement risk |
| Elevator condition (if applicable) | <10 years or modernized | 10-20 years, maintained | 20-30 years, needs modernization | >30 years or failed inspection |
| Parking lot/structure | Good condition | Fair, seal coat needed | Poor, resurfacing needed | Structural issues (if garage) |
| Building envelope | Tight, well-maintained | Minor issues (caulking, etc.) | Moderate water intrusion | Systemic water intrusion |

### Immediate CapEx Estimating

When physical issues are identified, estimate immediate capital needs:

| System | Typical Replacement Cost | Per-Unit Approximation |
|--------|-------------------------|----------------------|
| Roof (flat) | $5-10/SF | $1,500-4,000/unit |
| Roof (pitched) | $3-7/SF | $1,000-3,000/unit |
| HVAC (individual units) | $4,000-8,000/system | $4,000-8,000/unit |
| HVAC (central/boiler) | $50,000-200,000/system | $500-2,000/unit |
| Plumbing repipe | $3,000-7,000/unit | $3,000-7,000/unit |
| Electrical panel upgrade | $1,500-3,000/panel | $1,500-3,000/unit |
| Elevator modernization | $100,000-250,000/cab | Varies by building |
| Parking lot resurface | $3-6/SF | $500-1,500/unit |
| Foundation repair | $10,000-50,000+ | Varies widely |

### Automatic Escalations
- Galvanized or polybutylene plumbing: Minimum HIGH (65) -- known failure-prone materials
- Active structural foundation issues: Minimum CRITICAL (80)
- Knob-and-tube wiring: Minimum HIGH (70) -- fire risk, insurance issues
- Failed elevator inspection: Minimum HIGH (65) -- life safety, code enforcement
- Systemic mold with structural moisture: Minimum HIGH (70) -- health liability
- Active roof leaks with interior damage: Minimum HIGH (60)

---

## 9. Regulatory Risk (Multifamily)

*Multifamily-specific.* Evaluates jurisdiction-specific regulations that uniquely affect multifamily operations, including rent control, tenant protections, and affordable housing mandates.

### Risk Factors

| Factor | LOW (0-25) | MEDIUM (26-50) | HIGH (51-75) | CRITICAL (76-100) |
|--------|-----------|---------------|-------------|-------------------|
| Rent control/stabilization | Not applicable | Proposed/under consideration | In effect, moderate limits | Strict caps (e.g., <3% annual) |
| Just-cause eviction | Not required | Required with standard exceptions | Required with limited exceptions | Required with very narrow exceptions |
| Tenant right of first refusal | Not applicable | Voluntary/informal | Required by ordinance | Required with below-market terms |
| TOPA (Tenant Opportunity to Purchase) | Not applicable | Proposed/under consideration | In effect, standard terms | In effect with aggressive timelines |
| Affordable housing set-asides | None required | <10% set-aside | 10-20% set-aside | >20% set-aside |
| Rent registration/reporting | Not required | Annual registration only | Registration + rent increase approval | Pre-approval required for increases |
| Relocation assistance requirements | None | Moderate (1-2 months rent) | Significant (3-6 months rent) | Substantial (6+ months rent) |
| Habitability/inspection regime | Standard code | Enhanced inspection program | Proactive inspection with penalties | REAP or similar receivership program |
| Short-term rental restrictions | None relevant | Restrictions exist | Strict limits affect flexibility | Complete prohibition |
| Condo conversion restrictions | No restrictions | Standard notice period | Tenant approval required | Moratorium or prohibition |

### Jurisdiction Classification

Classify the jurisdiction's overall regulatory environment:

| Classification | Description | Score Modifier |
|---------------|-------------|----------------|
| **Landlord-Friendly** | Minimal regulation, standard landlord-tenant law | -10 from category score |
| **Balanced** | Standard regulations, reasonable compliance burden | No modifier |
| **Tenant-Friendly** | Significant tenant protections, higher compliance costs | +10 to category score |
| **Highly Regulated** | Extensive rent control, tenant protections, and mandates | +20 to category score |

**Known Highly Regulated Markets (not exhaustive):**
- New York City (rent stabilization, TOPA proposed)
- San Francisco (rent control, just-cause, relocation assistance)
- Los Angeles (RSO, SCEP, relocation assistance)
- Washington DC (rent control, TOPA)
- Portland OR (statewide rent control, relocation assistance)
- Seattle (just-cause, inspection requirements)
- Boston (ended rent control but new regulations emerging)
- Minneapolis/St. Paul (rent caps in St. Paul)

### Automatic Escalations
- Strict rent control with <3% caps: Minimum HIGH (65) -- limits value-add upside
- TOPA with aggressive timelines: Minimum HIGH (60) -- complicates disposition
- >20% affordable set-aside requirement: Minimum MEDIUM (45) -- impacts revenue projections
- Active REAP or receivership program on property: Minimum CRITICAL (85)

---

## Risk Weighting by Strategy

Different acquisition strategies weight risk categories differently. Apply the appropriate weights based on the deal's investment thesis.

### Core / Stabilized Acquisition

| Category | Weight |
|----------|--------|
| 1. Ownership & Title | 10% |
| 2. Legal & Litigation | 10% |
| 3. Environmental | 10% |
| 4. Zoning & Regulatory | 5% |
| 5. Financial | 25% |
| 6. Market | 15% |
| 7. Tenant Concentration | 10% |
| 8. Physical Condition | 5% |
| 9. Regulatory (Multifamily) | 10% |

### Value-Add Acquisition

| Category | Weight |
|----------|--------|
| 1. Ownership & Title | 8% |
| 2. Legal & Litigation | 8% |
| 3. Environmental | 8% |
| 4. Zoning & Regulatory | 8% |
| 5. Financial | 18% |
| 6. Market | 12% |
| 7. Tenant Concentration | 10% |
| 8. Physical Condition | 15% |
| 9. Regulatory (Multifamily) | 13% |

### Opportunistic / Deep Value-Add

| Category | Weight |
|----------|--------|
| 1. Ownership & Title | 10% |
| 2. Legal & Litigation | 10% |
| 3. Environmental | 10% |
| 4. Zoning & Regulatory | 10% |
| 5. Financial | 12% |
| 6. Market | 10% |
| 7. Tenant Concentration | 8% |
| 8. Physical Condition | 18% |
| 9. Regulatory (Multifamily) | 12% |

---

## Dealbreaker Checklist

Certain findings are automatic dealbreakers regardless of the overall risk score. If ANY of the following are present, flag the deal as **DEALBREAKER** and escalate immediately for review.

### Hard Dealbreakers (Automatic Rejection)

| # | Condition | Reason |
|---|-----------|--------|
| 1 | Active Superfund / NPL listing | Unlimited environmental liability |
| 2 | Unresolvable title dispute | Cannot acquire clean title |
| 3 | Active condemnation proceedings | Property may be seized |
| 4 | Structural failure / condemned | Unsafe, potentially uninsurable |
| 5 | DSCR < 0.90x (no viable restructure) | Cannot service debt |
| 6 | Active criminal investigation involving property | Legal exposure |
| 7 | Fraud detected in seller financials | Cannot underwrite reliably |
| 8 | Property in active receivership (REAP or similar) | Operational control restricted |

### Soft Dealbreakers (Require Mitigation Plan to Proceed)

| # | Condition | Required Mitigation |
|---|-----------|-------------------|
| 1 | Environmental contamination (Phase II) | Remediation cost estimate + insurance |
| 2 | Galvanized/polybutylene plumbing throughout | Full repipe budget in underwriting |
| 3 | Strict rent control jurisdiction | Adjusted return expectations + compliance plan |
| 4 | >50% lease expiration in 90 days | Lease-up plan + carry cost budget |
| 5 | Occupancy <75% | Market study + lease-up timeline + bridge financing |
| 6 | Single tenant >30% of revenue | Diversification plan + tenant credit analysis |
| 7 | Non-conforming use without grandfathering | Legal opinion on pathway to conformity |
| 8 | DSCR 0.90-1.10x | Debt restructure or additional equity plan |

---

## Mitigation Strategies

For each risk category, standard mitigations are available. Agents should recommend appropriate mitigations when risks are identified.

### Ownership & Title Mitigations
- Title insurance (extended coverage)
- Quiet title action (if feasible within timeline)
- Seller indemnification agreement
- Escrow holdback for unresolved liens

### Legal & Litigation Mitigations
- Seller indemnification for pre-closing claims
- Insurance (E&O, general liability)
- Code violation cure credit at closing
- Permit retroactive approval process

### Environmental Mitigations
- Phase II Environmental Site Assessment
- Environmental insurance (pollution legal liability)
- Remediation cost estimates from licensed professionals
- Seller remediation requirement pre-closing
- Escrow holdback for remediation

### Zoning & Regulatory Mitigations
- Zoning attorney opinion letter
- Pre-application conference with planning department
- Variance application timeline + cost estimate
- Alternative use planning (if primary use not achievable)

### Financial Mitigations
- Conservative underwriting (increase vacancy, decrease rent growth)
- Additional equity reserve
- Interest rate lock / cap
- Debt restructure (different leverage, amortization)
- Operating expense audit

### Market Mitigations
- Diversified tenant base targeting
- Amenity differentiation strategy
- Below-market positioning for occupancy stability
- Longer lease terms in uncertain markets
- Market study from independent third party

### Tenant Concentration Mitigations
- Lease staggering plan (spread expirations)
- Tenant diversification marketing
- Government program contract review (term, renewal certainty)
- Master lease guarantor credit analysis
- Tenant retention programs

### Physical Condition Mitigations
- Property Condition Assessment (PCA) from licensed engineer
- Capital expenditure reserve increase
- Insurance coverage review and upgrade
- Deferred maintenance budget at closing
- Phase-specific renovation planning
- Specialist inspections (structural, MEP, elevator)

### Regulatory (Multifamily) Mitigations
- Local counsel specializing in landlord-tenant law
- Rent control compliance audit
- Relocation cost budgeting
- Affordable housing consultant
- Political/regulatory trend monitoring
- TOPA timeline planning and legal counsel

---

## Output Template

Risk assessments should be structured in the following JSON format:

```json
{
  "dealId": "deal-2025-001",
  "scoringDate": "2025-01-15T14:45:00Z",
  "investmentStrategy": "value-add",
  "overallRiskScore": 42,
  "overallRiskLevel": "MEDIUM",
  "dealbreakers": [],
  "softDealbreakers": [
    {
      "condition": "Galvanized plumbing in Building B",
      "category": "Physical Condition",
      "requiredMitigation": "Full repipe budget ($4,500/unit x 24 units = $108,000) included in renovation scope"
    }
  ],
  "categories": {
    "ownershipTitle": {
      "score": 15,
      "level": "LOW",
      "factors": [
        {"name": "Ownership changes (5yr)", "score": 10, "detail": "1 transfer in 2023"},
        {"name": "Lien status", "score": 5, "detail": "No active liens"},
        {"name": "Title disputes", "score": 0, "detail": "None found"},
        {"name": "Entity structure", "score": 20, "detail": "Multi-member LLC, identifiable"},
        {"name": "Easements", "score": 10, "detail": "Standard utility easement only"},
        {"name": "Tax payment history", "score": 0, "detail": "Current, no delinquency"}
      ],
      "findings": ["Clean title with single transfer to current LLC in 2023"],
      "mitigations": [],
      "dataGaps": []
    },
    "legalLitigation": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "environmental": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "zoningRegulatory": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "financial": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "market": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "tenantConcentration": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    },
    "physicalCondition": {
      "score": 55,
      "level": "HIGH",
      "factors": [
        {"name": "Plumbing type", "score": 75, "detail": "Galvanized plumbing in Building B (24 units)"},
        {"name": "Roof age", "score": 45, "detail": "Roof is 17 years old, fair condition"},
        {"name": "HVAC systems", "score": 35, "detail": "Individual units, 12 years average age"}
      ],
      "findings": [
        "Building B has galvanized plumbing (24 of 48 total units) -- known failure-prone material",
        "Roof approaching end of useful life, budget replacement within 3-5 years"
      ],
      "mitigations": [
        "Include full repipe of Building B in renovation budget: $108,000",
        "Roof reserve: $75,000 for replacement in Year 3-5"
      ],
      "dataGaps": []
    },
    "regulatoryMultifamily": {
      "score": 0,
      "level": "LOW",
      "factors": [],
      "findings": [],
      "mitigations": [],
      "dataGaps": []
    }
  },
  "topRisks": [
    {
      "rank": 1,
      "category": "Physical Condition",
      "factor": "Galvanized plumbing",
      "score": 75,
      "impact": "Potential pipe failures, water damage, tenant displacement",
      "mitigation": "Full repipe budgeted in renovation scope"
    },
    {
      "rank": 2,
      "category": "Physical Condition",
      "factor": "Roof age",
      "score": 45,
      "impact": "Replacement needed within 3-5 years, $75K cost",
      "mitigation": "Capital reserve allocation"
    }
  ],
  "dataGapsSummary": [],
  "recommendation": "PROCEED_WITH_MITIGATIONS",
  "recommendationDetail": "Overall risk is MEDIUM (42/100). One soft dealbreaker identified (galvanized plumbing) with viable mitigation (repipe budgeted). No hard dealbreakers. Recommend proceeding with renovation plan that includes Building B repipe and roof reserve."
}
```

### Recommendation Values

| Value | When to Use |
|-------|-------------|
| `PROCEED` | Overall score < 30, no dealbreakers, no soft dealbreakers |
| `PROCEED_WITH_MITIGATIONS` | Overall score < 60, no hard dealbreakers, soft dealbreakers have viable mitigations |
| `PROCEED_WITH_CAUTION` | Overall score 60-75, significant risks but manageable |
| `FURTHER_DILIGENCE` | Data gaps prevent accurate scoring, need more information |
| `REJECT` | Hard dealbreaker present, OR overall score > 75, OR soft dealbreakers without viable mitigations |

---

## Edge Cases & Special Scenarios

The standard scoring framework handles the majority of deals. The following edge cases require specialized handling to avoid incorrect scoring, missed risks, or premature deal rejection.

---

### 1. Multiple Dealbreakers

**Description**: More than one hard or soft dealbreaker is present in the same deal. This is not simply "two problems" -- the combination may compound risk in ways that exceed the sum of individual issues.

**Why It Matters**: A deal with galvanized plumbing AND environmental contamination AND sub-80% occupancy faces overlapping capital demands, extended timelines, and compounding execution risk. Each dealbreaker individually might be manageable, but together they strain the capital budget, management bandwidth, and lender appetite simultaneously.

**How to Handle**:
1. **Do NOT abort on the first dealbreaker found.** Complete the full risk assessment across all 9 categories so the operator has the complete picture.
2. **List all dealbreakers** -- both hard and soft -- in the output, ranked by severity (highest score first).
3. **Assess interaction effects**: Do the dealbreakers share a common root cause (e.g., deferred maintenance causing both plumbing failure and mold)? If so, a single remediation program may address multiple issues. Flag this as a potential efficiency.
4. **Apply the Multiple Dealbreaker Escalation Rule**:
   - 1 hard dealbreaker = `REJECT` (standard rule)
   - 2+ soft dealbreakers without shared mitigation = Minimum overall score of 65 (HIGH), recommendation `PROCEED_WITH_CAUTION` only if each has a viable mitigation
   - 2+ soft dealbreakers with overlapping mitigation = Score normally, but flag the combined capital requirement prominently
   - 1 hard + 1 soft dealbreaker = `REJECT` unless the hard dealbreaker can be reclassified (e.g., environmental contamination with completed Phase II showing remediation cost under $50K)
   - 3+ soft dealbreakers = Minimum overall score of 70 (HIGH), recommendation `FURTHER_DILIGENCE` regardless of individual mitigation viability
5. **Report combined capital exposure**: Sum all mitigation costs across dealbreakers and express as a percentage of purchase price. If combined mitigation exceeds 15% of acquisition price, flag as a compound risk.

**Example**: 200-unit property in Memphis. Soft dealbreakers: (a) galvanized plumbing throughout -- repipe budget $1.4M, (b) 55% of leases expire in Q2 -- lease-up budget $180K, (c) occupancy at 78% -- bridge financing and carry costs $320K. Combined mitigation capital: $1.9M on a $12M acquisition (15.8% of price). These three issues share a common theme of operational distress. Recommendation: `FURTHER_DILIGENCE` -- verify whether the seller's distress creates sufficient price discount to absorb the combined remediation cost and still meet return targets.

**What to Flag**: `MULTIPLE_DEALBREAKERS_DETECTED` with count, combined capital requirement, and whether interaction effects exist.

---

### 2. Mixed Signals

**Description**: Some risk categories score LOW (0-25) while others score HIGH (51-75) or CRITICAL (76-100). The weighted average may produce a MEDIUM overall score that masks the extremes.

**Why It Matters**: A deal scoring 40 overall could have a perfectly clean title, excellent financials, and strong market fundamentals -- but CRITICAL environmental contamination. The 40 looks acceptable; the environmental liability is not. Relying solely on the weighted average can bury category-level dealbreakers or severe risks behind strong performance in other areas.

**How to Handle**:
1. **Always present category-level scores alongside the overall score.** Never present only the overall score.
2. **Calculate the risk dispersion metric**: Standard deviation of the 9 category scores. If the standard deviation exceeds 25 points, flag as `MIXED_SIGNAL_ALERT`.
3. **Apply the Mixed Signal Override Rule**:
   - If ANY single category scores CRITICAL (76-100), the overall recommendation cannot be `PROCEED` regardless of the weighted average. Minimum recommendation is `PROCEED_WITH_CAUTION`.
   - If ANY two categories score HIGH (51-75) or above, the overall recommendation cannot be `PROCEED`. Minimum is `PROCEED_WITH_MITIGATIONS`.
4. **Highlight the outlier categories** in the `topRisks` array. The highest-scoring category should always be the #1 top risk, even if other categories pulled the average down.
5. **Reconciliation narrative**: Include a plain-language explanation of the mixed signals. Example: "Overall risk score of 38 (MEDIUM) masks a CRITICAL environmental score of 82. The strong financial and market scores reduce the weighted average but do not eliminate the environmental liability. This deal's viability depends entirely on the environmental remediation outcome."

**Example**: 150-unit Class B property in Austin. Category scores: Ownership & Title: 10, Legal: 5, Environmental: 82, Zoning: 15, Financial: 20, Market: 12, Tenant Concentration: 25, Physical Condition: 30, Regulatory: 18. Weighted average (value-add weights): 28. The 28 score looks good, but the Environmental score of 82 indicates recognized environmental conditions requiring Phase II investigation. Without the mixed signal override, this deal would get a `PROCEED` recommendation -- dangerously incorrect.

**What to Flag**: `MIXED_SIGNAL_ALERT` with standard deviation value, highest category name and score, and lowest category name and score.

---

### 3. Unable to Score (Insufficient Data)

**Description**: Data available for a risk category is insufficient to produce a reliable score. This could be missing seller financials, no Phase I ESA completed yet, unavailable tenant records, or outdated market data.

**Why It Matters**: An unscorable category is not the same as a LOW risk category. Assigning a 0 or LOW score due to missing data creates a false sense of safety. Conversely, assigning CRITICAL due to missing data may be unnecessarily conservative and kill viable deals.

**How to Handle**:
1. **Use the `UNSCORED` designation.** Do not assign a numeric score. In the JSON output, set the category score to `null` and the level to `"UNSCORED"`.
2. **Minimum data requirements per category**:

| Category | Minimum Data Required to Score |
|----------|-------------------------------|
| Ownership & Title | Title commitment or preliminary title report |
| Legal & Litigation | Court records search or seller litigation disclosure |
| Environmental | Phase I ESA (within 180 days) |
| Zoning & Regulatory | Zoning verification letter or municipal confirmation |
| Financial | Trailing 12-month operating statement + current rent roll |
| Market | Market data from recognized source within 6 months |
| Tenant Concentration | Current rent roll with tenant details and lease dates |
| Physical Condition | Property Condition Assessment or detailed inspection report |
| Regulatory (Multifamily) | Jurisdiction regulatory research (rent control, tenant protections) |

3. **Impact on overall score**: UNSCORED categories are excluded from the weighted average calculation. Redistribute their weights proportionally across scored categories. However, if more than 2 categories are UNSCORED, the overall recommendation must be `FURTHER_DILIGENCE` regardless of scored category results.
4. **Report all UNSCORED categories** in the `dataGapsSummary` array with the specific data needed to score them.
5. **Set a deadline**: Each UNSCORED category should include an estimated timeline to obtain the missing data and a note on whether the due diligence period allows for it.

**Example**: Day 5 of a 45-day due diligence period. Phase I ESA has been ordered but not yet received. Environmental category is UNSCORED. Title commitment received -- Ownership & Title scored at 15 (LOW). Financial T-12 received -- Financial scored at 35 (MEDIUM). Three other categories still awaiting data. Overall score calculated from 4 scored categories only. Recommendation: `FURTHER_DILIGENCE` (more than 2 categories UNSCORED). Expected resolution: Phase I due Day 25, PCA due Day 20, market study due Day 15.

**What to Flag**: `DATA_GAPS_PRESENT` with count of UNSCORED categories, list of missing data items, and estimated resolution dates.

---

### 4. Strategy-Specific Risk Tolerance

**Description**: Different investment strategies have fundamentally different risk appetites. A score that is unacceptable for a core acquisition may be perfectly acceptable for an opportunistic play. The same deal can be a REJECT for one buyer and a PROCEED for another.

**Why It Matters**: Applying a single risk threshold across all strategies leads to either rejecting viable opportunistic deals or approving risky core deals. The scoring framework must calibrate its pass/fail thresholds to the investment strategy.

**How to Handle**:
1. **Apply strategy-specific thresholds for the overall score**:

| Strategy | PROCEED Threshold | PROCEED_WITH_MITIGATIONS | PROCEED_WITH_CAUTION | FURTHER_DILIGENCE | REJECT |
|----------|------------------|--------------------------|---------------------|-------------------|--------|
| Core / Stabilized | < 20 | 20-25 | 25-35 | Data gaps present | > 35 or any dealbreaker |
| Core-Plus | < 25 | 25-35 | 35-45 | Data gaps present | > 45 or any hard dealbreaker |
| Value-Add | < 35 | 35-45 | 45-55 | Data gaps present | > 55 or any hard dealbreaker |
| Opportunistic | < 45 | 45-55 | 55-65 | Data gaps present | > 65 or any hard dealbreaker |
| Distressed / Turnaround | < 55 | 55-65 | 65-75 | Data gaps present | > 75 or any hard dealbreaker |

2. **Hard dealbreakers remain absolute** for Core and Core-Plus strategies. For Value-Add and Opportunistic strategies, some soft dealbreakers may be reclassified as standard HIGH risks if the business plan explicitly addresses them and sufficient capital is budgeted.
3. **Category-level tolerance also varies**: Physical Condition scores of 60+ are expected in opportunistic deals (that is the value-add thesis). But Financial scores of 60+ are concerning regardless of strategy because they indicate current cash flow problems that affect debt service.
4. **Always state the strategy** in the output and note which threshold set was applied.
5. **If strategy is unknown or not specified**, default to Value-Add thresholds and note that thresholds should be adjusted once strategy is confirmed.

**Example**: 300-unit Class C property in Indianapolis. Overall risk score: 52 (HIGH under standard thresholds). Strategy: Opportunistic / Deep Value-Add. Under opportunistic thresholds, 52 falls in the `PROCEED_WITH_MITIGATIONS` range. The high score is driven by Physical Condition (68) and Tenant Concentration (55) -- both of which are the investment thesis (renovate units, diversify tenant base). Recommendation changes from `PROCEED_WITH_CAUTION` (standard) to `PROCEED_WITH_MITIGATIONS` (opportunistic).

**What to Flag**: `STRATEGY_THRESHOLD_APPLIED` with strategy name, threshold set used, and how recommendation would differ under Core thresholds.

---

### 5. Rapidly Changing Market Conditions (Stale Data)

**Description**: Market data used for scoring is outdated -- typically more than 90 days old. In rapidly shifting markets (rising interest rates, sudden supply glut, major employer departure), even 60-day-old data can be materially misleading.

**Why It Matters**: Market Risk (Category 6) relies on employment data, rent growth trends, vacancy rates, supply pipeline, and comparable sales. If this data is 6 months old and the market has deteriorated, the risk score understates reality. Conversely, stale data from a pre-recovery period may overstate risk in a recovering market.

**How to Handle**:
1. **Track data freshness for every market data point.** Record the date of each data source used in the Market Risk scoring.
2. **Apply staleness discounts** based on data age:

| Data Age | Staleness Adjustment | Action |
|----------|---------------------|--------|
| 0-30 days | No adjustment | Data is current |
| 31-60 days | +5 points to Market Risk score | Note staleness, acceptable for most purposes |
| 61-90 days | +10 points to Market Risk score | Recommend refreshing data before final decision |
| 91-180 days | +15 points to Market Risk score | Flag as `STALE_MARKET_DATA`, refresh required before commitment |
| 180+ days | +20 points to Market Risk score | Category approaches UNSCORED territory; strongly recommend new market study |

3. **Identify rapid-change indicators** that amplify staleness risk:
   - Interest rate changes > 100 bps since data collection
   - Major employer announcement (relocation, layoff, expansion) since data collection
   - New supply deliveries exceeding forecast since data collection
   - Natural disaster affecting the market since data collection
   - Any of the above present: double the staleness adjustment
4. **Report the data vintage** in the Market Risk category output: oldest data source date, newest data source date, and weighted average age.
5. **Recommendation impact**: If Market Risk data is >90 days old, the overall recommendation cannot be `PROCEED`. Minimum is `PROCEED_WITH_MITIGATIONS` with a specific mitigation of "Obtain updated market data before waiving due diligence contingency."

**Example**: Evaluating a 120-unit property in Phoenix. Market data sources: CoStar rent comps (45 days old), Census employment data (5 months old), building permit data (3 months old), comparable sales (4 months old). Weighted average data age: 105 days. Staleness adjustment: +15 to Market Risk score. Additionally, since data collection, a major semiconductor manufacturer announced a 2,000-job facility in the submarket -- a rapid-change indicator. Double the adjustment to +30. Original Market Risk score: 22 (LOW). Adjusted score: 52 (HIGH). This materially changes the market risk assessment and warrants fresh data collection.

**What to Flag**: `STALE_MARKET_DATA` with oldest data point age, staleness adjustment applied, and any rapid-change indicators detected.

---

### 6. First-Time Market Entry

**Description**: The buyer has no prior acquisition, ownership, or operational experience in the subject property's market or submarket. This could mean entering a new state, metro area, or even a different submarket within a known metro.

**Why It Matters**: Local market knowledge reduces execution risk across every phase -- from understanding tenant demographics and rent comps to navigating municipal processes, identifying reliable contractors, and building lender relationships. A buyer entering a new market faces higher execution risk than the property's inherent characteristics suggest. Lenders also assess sponsor market experience, which affects financing terms and availability.

**How to Handle**:
1. **Apply a First-Time Market Premium**: Add 5-10 points to the overall risk score when the buyer has no prior experience in the metro area. Add 3-5 points when the buyer has metro experience but not submarket experience.

| Experience Level | Premium | Rationale |
|-----------------|---------|-----------|
| No experience in state | +10 points | Unfamiliar regulations, tax regime, contractor base, lender relationships |
| No experience in metro area | +7 points | Unfamiliar submarket dynamics, tenant base, competition |
| Metro experience but new submarket | +3 points | General market knowledge but unfamiliar micro-dynamics |
| Existing submarket experience | +0 points | No premium needed |

2. **Mitigations that reduce the premium**:

| Mitigation | Premium Reduction | How to Verify |
|-----------|------------------|---------------|
| Hire local property management company with 5+ years in submarket | -3 points | Management agreement or LOI |
| Engage local broker/advisor with 10+ deals in submarket | -2 points | Advisory agreement or track record |
| Partner with local operator as co-GP or JV partner | -5 points | Operating agreement or JV term sheet |
| Complete a market immersion trip (3+ days on-ground research) | -1 point | Trip report documenting findings |
| Retain local legal counsel with multifamily specialization | -1 point | Engagement letter |

3. **Lender impact**: Flag that first-time market entry may affect agency lending (Fannie/Freddie prefer experienced local sponsors) and may require a Key Principal with local experience or a management company with Fannie/Freddie approval in the market.
4. **Increase data requirements**: For first-time market entries, require a third-party market study (not just CoStar or internal analysis) as a minimum data requirement for the Market Risk category.
5. **Regulatory risk amplification**: In highly regulated markets (NYC, SF, LA, Portland), first-time entry without local counsel is particularly dangerous. If the Regulatory (Multifamily) category scores MEDIUM or above AND the buyer is a first-time entrant, escalate the Regulatory score by +10 points.

**Example**: Texas-based operator acquiring their first property in Portland, OR. Base overall risk score: 38 (MEDIUM). First-time market premium: +10 (no Oregon experience). Portland is a highly regulated market (statewide rent control, relocation assistance requirements). Regulatory category base score: 45 (MEDIUM). First-time regulatory amplification: +10, adjusted to 55 (HIGH). Mitigations applied: hired local PM with 8 years Portland experience (-3), retained Portland multifamily attorney (-1). Net premium after mitigations: +6. Adjusted overall score: 44 (MEDIUM, near the upper bound). Recommendation: `PROCEED_WITH_MITIGATIONS` -- specifically, complete market immersion trip and consider partnering with a local co-GP to further reduce execution risk.

**What to Flag**: `FIRST_TIME_MARKET_ENTRY` with experience level, premium applied, mitigations identified, net premium after mitigations, and specific lender/regulatory implications.