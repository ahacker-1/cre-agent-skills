---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Lease Roster Analyst

Analyze an industrial rent roll or lease roster to evaluate WALT, rollover concentration, concentration risk, reimbursement structure, and release risk.

---

## When to Use This Skill

Use this skill when you have an industrial rent roll, tenant schedule, or lease roster and need to understand the durability of income. It is most valuable when evaluating a multi-tenant or single-tenant industrial asset where lease structure and rollover drive the underwriting outcome.

---

## What You'll Need to Provide

- Tenant roster or rent roll with:
  - tenant names
  - leased square feet
  - annual or monthly rent
  - lease start and expiration
  - free-rent or abatement information if known
  - reimbursement structure if known
- Property subtype and address
- Current occupancy summary
- Market rent information if available
- Any known tenant options, early termination rights, expansion rights, or contraction rights

---

## Mission

Evaluate the lease roster as an industrial income stream. Measure WALT, rollover concentration, rent concentration, lease-structure variability, and likely release risk at expiration.

---

## Strategy

### Step 1: Normalize the Roster

- Standardize tenant names and rentable square footage
- Convert rent to a common basis
- Separate base rent from reimbursements when possible
- Identify missing or estimated fields

### Step 2: Measure Income Concentration

Calculate:

- top tenant share of rent
- top 3 tenants share of rent
- top 5 tenants share of rent
- top tenant share of occupied square footage

### Step 3: Measure Lease Duration

Calculate:

- WALT by annual base rent
- WALT by leased square footage
- near-term rollover in the next 12, 24, and 36 months
- annual rollover by both rent and square footage

### Step 4: Review Lease Structure

For each tenant, identify whether the lease appears:

- triple net
- modified gross
- hybrid / unclear

Flag where reimbursements are missing, inconsistent, or lower confidence.

### Step 5: Review Cash Flow Friction

Flag:

- free rent / abatements
- below-market or above-market in-place rents
- large rent steps
- termination or contraction rights
- renewal options that may affect market-rent capture

### Step 6: Release Risk Assessment

For each major tenant or major rollover year, assess:

- subtype fit
- building dependence
- likely downtime
- likely TI / LC burden
- depth of replacement demand

### Step 7: Portfolio-Level Verdict

Conclude whether the roster is:

- durable
- acceptable but lumpy
- concentrated
- transitional / release-driven

---

## Output Format

```json
{
  "property": "",
  "status": "COMPLETE | PARTIAL | FAILED",
  "walt": {
    "by_rent_years": 0,
    "by_square_feet_years": 0
  },
  "concentration": {
    "top_tenant_rent_share_pct": 0,
    "top_3_rent_share_pct": 0,
    "top_5_rent_share_pct": 0
  },
  "rollover": {
    "next_12_months_rent_pct": 0,
    "next_24_months_rent_pct": 0,
    "next_36_months_rent_pct": 0
  },
  "lease_structure_summary": [],
  "major_risks": [],
  "release_risk_summary": [],
  "verdict": "DURABLE | MIXED | CONCENTRATED | TRANSITIONAL",
  "confidence_level": "HIGH | MEDIUM | LOW"
}
```

---

## Quality Checks

- WALT is calculated by rent and square footage
- Rollover is measured by both rent and square footage
- Concentration findings are not limited to tenant count
- Lease-structure uncertainty is called out instead of ignored
- Release risk is assessed for major tenants and major rollover years

---

## When Data is Missing

- If reimbursements are missing, state that effective NOI durability is lower confidence
- If options are missing, assume no exercise only if clearly labeled as a conservative simplification
- If market rent is unavailable, focus on rollover concentration and release burden rather than hard rent mark-to-market

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full tenant roster, reimbursement structure, and option data available |
| MEDIUM | Core rent and term data available, but some options or reimbursement fields missing |
| LOW | Partial roster or heavy assumptions required |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)
- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)

## Research Basis

- [Industrial Lease Roster Analyst Research](research/industrial/industrial-lease-roster-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
