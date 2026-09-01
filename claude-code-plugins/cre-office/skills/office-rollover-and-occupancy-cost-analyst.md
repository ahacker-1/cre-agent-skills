---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Office Rollover and Occupancy Cost Analyst

Analyze office lease expirations, renewal probability, tenant occupancy-cost pressure, downtime, concessions, and re-leasing economics.

---

## When to Use This Skill

Use this skill when a building's value depends on whether tenants renew, downsize, expand, or leave. It is useful for acquisition underwriting, loan sizing, renewal planning, and hold/sell decisions.

---

## What You'll Need to Provide

- Rent roll with expirations, RSF, rent, escalations, options, and tenant status
- Market rent and concessions by tenant size and quality tier
- Tenant credit or business context if available
- Historical renewal, expansion, contraction, and downtime data if available
- TI, LC, free-rent, and downtime assumptions
- Tenant revenue, headcount, or occupancy-cost data if available

---

## Mission

Translate rollover into cash-flow risk by estimating which tenants renew, how much space they retain, what economics are required, and how much downtime and capital are needed if they leave.

---

## Strategy

### Step 1: Build Expiration Ladder

Create annual and quarterly expiration schedules:

- expiring RSF
- expiring rent
- percent of leased RSF
- percent of base rent
- tenant names
- option notice dates

### Step 2: Classify Tenant Renewal Probability

Score each material tenant:

- HIGH: mission-critical build-out, stable or growing business, market rent, strong credit, low relocation incentive
- MEDIUM: normal office user, some space planning uncertainty, rent near market
- LOW: downsizing industry, above-market rent, weak credit, contraction rights, obvious relocation alternative

### Step 3: Test Occupancy-Cost Pressure

Where tenant financial data is available, estimate occupancy cost. If unavailable, use qualitative pressure:

- headcount vs seats
- hybrid utilization
- industry margins
- rent as above/below market
- recent layoffs or growth
- space per employee if known

Do not invent tenant revenue. If not provided, mark as qualitative.

### Step 4: Model Renewal vs Re-let

For each major rollover, model:

- renewal rent
- renewal TI
- renewal LC
- downtime if tenant leaves
- new-tenant rent
- new-tenant TI
- new-tenant LC
- free rent
- probability-weighted cash flow

### Step 5: Identify Building-Level Rollover Clusters

Flag:

- multiple tenants expiring in same year
- same-industry exposure
- floor-level vacancy clustering
- large-block risk
- near-term debt maturity overlap

### Step 6: Recommend Actions

Recommend:

- early renewal
- blend-and-extend
- targeted spec suite
- repositioning capital
- sale before rollover
- lender reserve plan
- tenant watchlist

---

## Output Format

```markdown
# Office Rollover and Occupancy Cost Analysis
## Property:
## As-of Date:

### Rollover Summary
| Year | Expiring RSF | % Leased RSF | Expiring Rent | Major Tenants | Risk |
|---|---:|---:|---:|---|---|

### Tenant Renewal Probability
| Tenant | Expiration | RSF | Rent vs Market | Renewal Probability | Key Driver |
|---|---|---:|---|---|---|

### Renewal vs Re-let Economics
| Tenant / Suite | Renewal NER | Re-let NER | Downtime | TI / LC | Recommended Assumption |
|---|---:|---:|---:|---:|---|

### Occupancy-Cost Pressure
- High-pressure tenants:
- Stable tenants:
- Unknowns:

### Recommended Actions
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Rollover is measured by RSF and rent, not only tenant count
- Option notice dates are checked before recommending action
- Renewal and new-tenant economics include TI, LC, free rent, and downtime
- Tenant occupancy-cost pressure is not invented when tenant financials are unavailable
- Debt maturity overlap is flagged when known

---

## Red Flags & Dealbreakers

- More than 35% of RSF expires before or near loan maturity
- Major tenant has termination or contraction right inside the hold period
- Renewal probability is assumed high solely because tenant is currently occupying
- Re-leasing economics omit TI/LC or free rent
- Existing rent is above market and renewal analysis assumes no reset

---

## When Data is Missing

- If market concessions are missing, use a range and lower confidence
- If tenant financials are missing, score occupancy-cost pressure qualitatively
- If options are unknown, flag every major tenant as requiring lease abstract review
- If downtime history is unavailable, use submarket and suite-size evidence from the market study

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Lease expirations, options, market rents, concessions, and tenant context are available |
| MEDIUM | Expirations and market rent are available, but concessions or tenant context is incomplete |
| LOW | Summary rent roll only or missing option/downtime assumptions |

---

## Related Knowledge Bases

- [Office Benchmarks](knowledge/office-benchmarks.md)
- [Office TI / LC Economics](knowledge/office-ti-lc-economics.md)
- [Office Lease Structures](knowledge/office-lease-structures.md)

## Research Basis

- [Office Rollover and Occupancy Cost Analyst Research](research/office/office-rollover-and-occupancy-cost-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
