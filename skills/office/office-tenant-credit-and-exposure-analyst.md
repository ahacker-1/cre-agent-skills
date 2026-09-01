---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Office Tenant Credit and Exposure Analyst

Assess tenant durability, industry exposure, concentration, space dependence, and downside risk in an office rent roll.

---

## When to Use This Skill

Use this skill when tenant credit, industry concentration, or tenant behavior could drive value. It is especially useful for buildings with a few large tenants, single-tenant office assets, coworking exposure, government tenancy, tech concentration, or near-term rollover.

---

## What You'll Need to Provide

- Tenant roster with RSF, rent, lease expiration, and options
- Tenant parent companies and guarantors if known
- Public company tickers or financials if available
- Tenant industry and space use
- Security deposits, letters of credit, or guarantees
- Recent tenant news, layoffs, expansion, contraction, or sublease activity
- Building dependency: headquarters, regional office, back office, medical, government, lab/office, call center, etc.

---

## Mission

Identify which tenants create durable income and which tenants create credit, concentration, rollover, or downsizing risk.

---

## Strategy

### Step 1: Normalize Tenant Exposure

Calculate:

- tenant RSF
- tenant annual rent
- percent of leased RSF
- percent of annual base rent
- years to expiration
- parent/guarantor exposure
- industry exposure

### Step 2: Classify Credit

Classify tenants:

- INVESTMENT-GRADE / PUBLIC: public financials or rated parent support
- STRONG PRIVATE: durable business, long operating history, clear local need
- NORMAL PRIVATE: ordinary credit, no obvious distress
- WATCHLIST: layoffs, shrinking footprint, weak financials, sublease activity, or adverse industry trend
- HIGH RISK: default, nonpayment, bankruptcy, going-concern concern, or tenant not occupying

### Step 3: Assess Space Dependence

Evaluate:

- headquarters vs satellite
- customer-facing or employee-support role
- specialized build-out
- data/security needs
- proximity to talent, courts, hospitals, government, clients, or transport
- relocation friction
- ability to remote/hybrid downsize

### Step 4: Assess Lease Protection

Review:

- security deposit or letter of credit
- parent guaranty
- termination/contraction rights
- renewal options
- assignment/sublease rights
- remaining lease term
- above/below-market rent

### Step 5: Build Tenant Watchlist

Rank tenants by downside impact:

```text
Tenant Exposure Score = Rent Share x Credit Risk x Rollover Risk x Replacement Difficulty
```

Use qualitative scoring when numeric data is incomplete.

### Step 6: Recommend Diligence and Underwriting Treatment

For each material tenant:

- keep as durable
- mark for renewal outreach
- require credit diligence
- model downside vacancy
- require reserve
- reduce exit liquidity assumption

---

## Output Format

```markdown
# Office Tenant Credit and Exposure Analysis
## Property:
## As-of Date:

### Exposure Summary
| Tenant | Industry | RSF | % Rent | Expiration | Credit Tier | Exposure Risk |
|---|---|---:|---:|---|---|---|

### Industry Concentration
| Industry | RSF | % Rent | Risk Notes |
|---|---:|---:|---|

### Watchlist
| Tenant | Concern | Evidence | Underwriting Treatment | Follow-Up |
|---|---|---|---|---|

### Durable Income
- Tenants with strong retention logic:
- Tenant protections:

### Downside Case
- Tenants assumed lost:
- Vacancy created:
- Replacement difficulty:
- Capital required:

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Tenant exposure is measured by both RSF and rent
- Parent and guarantor support are separated from operating tenant name
- Industry concentration is shown
- Lease protections are checked before calling income durable
- Space dependence is considered, not only credit rating
- Watchlist tenants receive specific underwriting treatment

---

## Red Flags & Dealbreakers

- One tenant controls more than 25% of rent with weak credit or near-term expiration
- Coworking or flexible office tenant has high rent share and limited credit support
- Tenant has listed space for sublease but is counted as stable occupancy
- Tenant is above market and likely to reset downward
- Parent guaranty is missing or limited despite underwriting relying on parent credit

---

## When Data is Missing

- If tenant financials are unavailable, classify credit based on public information and mark as qualitative
- If guaranty details are unavailable, do not assume parent support
- If tenant industry is unknown, use tenant name only if clearly identifiable and flag as inferred
- If sublease data is missing, ask for broker confirmation before finalizing major tenant risk

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Tenant identities, parent/guarantor data, lease terms, and current business context are available |
| MEDIUM | Tenant list and expirations available, but credit support or business context is partial |
| LOW | Tenant names or parent support unclear; exposure mostly inferred |

---

## Related Knowledge Bases

- [Office Benchmarks](knowledge/office-benchmarks.md)
- [Office Lease Structures](knowledge/office-lease-structures.md)
- [Office Lender Criteria](knowledge/office-lender-criteria.md)

## Research Basis

- [Office Tenant Credit and Exposure Analyst Research](research/office/office-tenant-credit-and-exposure-analyst-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
