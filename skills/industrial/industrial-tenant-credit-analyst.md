---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Tenant Credit Analyst

Evaluate industrial tenant quality, concentration, release risk, and lease durability for acquisition underwriting.

---

## When to Use This Skill

Use this skill when tenant quality is a major driver of value - especially in single-tenant, low-tenant-count, or concentrated industrial assets. It is also useful in multi-tenant assets where a few tenants drive most of the rent.

---

## What You'll Need to Provide

- Tenant roster or major-tenant summary
- Lease expiration dates and square footage by tenant
- Any available tenant credit information:
  - public filings
  - ratings
  - guaranties
  - parent support
- Property subtype and basic building specs
- Market context if available

---

## Mission

Assess tenant durability and its impact on asset durability. Distinguish tenant credit quality from release risk and explain how concentration, lease term, and building specificity affect downside exposure.

---

## Strategy

### Step 1: Tenant Identification

- Confirm legal tenant names
- Identify parent or guarantor support where visible
- Distinguish public, PE-backed, and private tenants if possible

### Step 2: Credit and Industry Review

Review:

- corporate scale and visibility
- industry cyclicality
- exposure to freight, retail, manufacturing, or specialized end markets
- signs of margin pressure or strategic retrenchment if publicly visible

### Step 3: Lease Durability Review

Measure:

- remaining lease term
- options
- near-term rollover
- concentration by rent and square footage

### Step 4: Building Dependence and Replaceability

Assess:

- how specific the facility is to the tenant's use
- whether the tenant likely needs this exact location
- whether a replacement tenant pool is broad or narrow

### Step 5: Asset-Level Risk View

Score each major tenant and then the overall asset on:

- financial durability
- lease durability
- replacement risk
- concentration

### Step 6: Downside Narrative

Explain what happens if a major tenant leaves:

- likely downtime
- likely TI / LC burden
- need for reconfiguration
- effect on financing or valuation

---

## Output Format

```markdown
# Industrial Tenant Credit Analysis
## Property:
## Status: COMPLETE | PARTIAL | FAILED

### Tenant Summary
| Tenant | SF | Rent Share | Remaining Term | Credit Visibility | Key Risk |
|--------|----|------------|----------------|-------------------|----------|

### Major Findings
- ...

### Tenant-Level Risk Ratings
- Tenant A: LOW | MODERATE | HIGH
- Tenant B: LOW | MODERATE | HIGH

### Asset-Level View
- Concentration:
- Lease Durability:
- Replacement Risk:
- Overall Verdict:

### Downside Case
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Tenant credit and asset release risk are analyzed separately
- Concentration is measured by rent and square footage
- Remaining lease term is considered alongside tenant quality
- Specialized build-out or building dependence is explicitly discussed

---

## When Data is Missing

- If tenant financial visibility is limited, lower confidence and weight release risk more heavily
- If guaranty data is unavailable, state that explicitly
- If building specificity is unclear, avoid overconfident release conclusions

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Public or well-supported tenant information plus strong lease and property context |
| MEDIUM | Good lease and property context but partial tenant credit visibility |
| LOW | Private tenants with limited disclosure and incomplete lease or property context |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)
- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)

## Research Basis

- [Industrial Tenant Credit Analyst Research](research/industrial/industrial-tenant-credit-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
