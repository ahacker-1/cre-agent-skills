---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Underwriting Model Builder

Build a U.S. industrial acquisition model that reflects lease structure, rollover, downtime, TI, LC, and functional competitiveness.

---

## When to Use This Skill

Use this skill when you have industrial rent roll, lease, market, and building data and need a base-case underwriting model. It is the right starting point for acquisitions where the return profile depends on lease durability, release assumptions, and capital requirements rather than on a simple stabilized rent-roll snapshot.

---

## What You'll Need to Provide

- Current lease roster or rent roll
- Lease structure summary
- Market rent context
- Building subtype and specs
- Purchase price and hold period
- Financing assumptions if available
- CapEx and competitiveness-upgrade view if available
- Any known rollover, release, or re-tenanting thesis

---

## Mission

Build a defensible industrial underwriting model that separates contractual income from market assumptions and explicitly models rollover, downtime, TI, LC, capital needs, and exit risk.

---

## Strategy

### Step 1: Build In-Place Cash Flow

Calculate:

- contractual base rent
- reimbursements
- temporary abatements
- known step-ups
- non-recoverable operating costs

### Step 2: Build Lease Timeline

Map:

- WALT
- annual rollover
- major tenant expirations
- options that may alter rollover

### Step 3: Model Release Assumptions

For each major rollover:

- estimate downtime
- estimate TI
- estimate LC
- estimate market rent vs in-place rent
- state whether space requires spec upgrades or reconfiguration

### Step 4: Model Operating Expenses and Recoveries

Separate:

- reimbursable expenses
- leakage or non-recoverable costs
- management / overhead
- reserves and recurring capital

### Step 5: Model Capital Needs

Include:

- immediate repairs
- near-term replacements
- competitiveness upgrades
- tenant-specific capital tied to rollovers

### Step 6: Build Debt and Exit View

Model:

- financing assumptions
- debt service or interest burden
- exit cap assumption
- expected disposition story:
  - stabilized
  - transitional
  - partially re-tenanted

### Step 7: State Base-Case Verdict

Conclude whether the base case depends primarily on:

- durable in-place income
- market-rent capture
- successful re-tenanting
- CapEx-led repositioning

---

## Output Format

```markdown
# Industrial Underwriting Model
## Property:
## Status: PASS | FAIL | MARGINAL

### Base Assumptions
- Subtype:
- Hold Period:
- Financing:
- Exit Cap:

### In-Place Cash Flow
- Base Rent:
- Reimbursements:
- Non-Recoverable Expenses:
- NOI:

### Lease Risk
- WALT:
- Major Rollover Years:
- Concentration:

### Release Assumptions
- Downtime:
- TI:
- LC:
- Market Rent View:

### Capital Plan
- Immediate Repairs:
- Near-Term Replacements:
- Competitiveness Upgrades:

### Returns Summary
- Going-In Yield:
- Stabilized Yield:
- Base-Case IRR:
- Equity Multiple:

### Key Risks
- ...

### Verdict
PASS | MARGINAL | FAIL

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Contractual revenue is separated from market-rent assumptions
- Rollover is explicitly modeled rather than buried in growth
- TI and LC are not omitted
- Recoveries and leakage are handled explicitly
- CapEx is separated from routine operating costs

---

## When Data is Missing

- If reimbursements are unclear, underwrite conservatively
- If TI / LC market data is missing, state directional assumptions and lower confidence
- If the lease roster is incomplete, identify which tenants or terms create the greatest model sensitivity

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Lease roster, market rent, CapEx, and recovery structure are all clear |
| MEDIUM | Core rent and market data available, but some release-cost assumptions estimated |
| LOW | Significant lease or building-capital uncertainty remains |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)
- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)
- [Industrial Lender Criteria](knowledge/industrial-lender-criteria.md)

## Research Basis

- [Industrial Underwriting Model Builder Research](research/industrial/industrial-underwriting-model-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
