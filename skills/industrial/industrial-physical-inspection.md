---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Physical Inspection

Assess industrial building condition and functional competitiveness, then translate findings into CapEx, release risk, and operational fit.

---

## When to Use This Skill

Use this skill during acquisitions or recapitalization diligence when you need to understand whether an industrial building is merely standing or actually competitive. It is most valuable when functional obsolescence, fire protection, loading, or power could affect lease-up, tenant retention, or financing.

---

## What You'll Need to Provide

- Inspection report, engineering report, or property-condition summary
- Basic specs:
  - square footage
  - clear height
  - loading type and dock count
  - truck court depth
  - trailer and auto parking
  - office finish ratio
  - power information if available
  - sprinkler type if available
- Year built and major renovation history
- Industrial subtype

---

## Mission

Evaluate both the physical condition and the leasing competitiveness of the building. Identify immediate repairs, near-term capital needs, and function-driven upgrades required to keep or improve tenantability.

---

## Strategy

### Step 1: Confirm Subtype and Use Case

- Determine whether the building functions as:
  - bulk distribution
  - shallow-bay
  - flex industrial
  - light industrial
  - single-tenant specialized occupancy
- Use the subtype to decide which specs matter most

### Step 2: Review Core Condition

Assess:

- roof age and status
- slab condition
- paving and truck court condition
- exterior walls and structure
- HVAC and make-up air
- electrical and power distribution
- lighting
- dock equipment and doors

### Step 3: Review Fire-Life-Safety and Insurability

Identify:

- sprinkler type
- apparent fit for racking or storage use
- any known limitations
- whether cold storage or specialized uses imply additional complexity

### Step 4: Review Functional Competitiveness

Compare the building to current competing stock on:

- clear height
- loading configuration
- circulation
- trailer storage
- power
- office finish burden
- adaptability to modern users

### Step 5: Separate Capital Needs

Group findings into:

1. Immediate repairs
2. Near-term replacements
3. Competitiveness upgrades

### Step 6: Release and Underwriting Impact

Explain how the physical issues affect:

- leasing depth
- likely downtime
- TI burden
- lender comfort
- probable buyer pool

---

## Output Format

```markdown
# Industrial Physical Inspection Summary
## Property:
## Status: COMPLETE | PARTIAL | FAILED

### Core Condition
- Roof:
- Slab:
- Loading Equipment:
- Paving / Truck Court:
- HVAC:
- Electrical / Power:
- Sprinklers:

### Functional Competitiveness
- Clear Height:
- Loading Configuration:
- Trailer Parking / Circulation:
- Office Finish Ratio:
- Overall Market Competitiveness:

### CapEx Summary
- Immediate Repairs:
- Near-Term Replacements:
- Competitiveness Upgrades:

### Underwriting Impact
- Leasing risk:
- Downtime risk:
- Financing risk:

### Overall Verdict
STRONG | ADEQUATE | WEAK | OBSOLETE-RISK

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The building is analyzed relative to its subtype
- Condition issues are separated from competitiveness issues
- Fire-life-safety is not omitted
- CapEx is separated into repair vs replacement vs competitiveness spend
- The summary states how physical findings affect lease risk and underwriting

---

## When Data is Missing

- If sprinkler or power data is missing, call out the resulting underwriting uncertainty
- If no engineering report exists, treat hidden-condition confidence as lower
- If subtype is unclear, state the leading subtype assumption and its impact on the review

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Detailed report plus clear building-spec data available |
| MEDIUM | Core building information available but some systems or specs incomplete |
| LOW | Limited condition data or marketing-level information only |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)

## Research Basis

- [Industrial Physical Inspection Research](research/industrial/industrial-physical-inspection-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
