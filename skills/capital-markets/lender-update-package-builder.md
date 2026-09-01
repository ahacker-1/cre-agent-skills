---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Lender Update Package Builder

Build a lender-facing update package for refinance, extension, modification, workout, or rescue-capital discussions.

---

## When to Use This Skill

Use this skill when an owner needs to communicate with an existing lender, prospective refinance lender, servicer, special servicer, preferred-equity investor, or rescue-capital provider.

---

## What You'll Need to Provide

- Property overview and current business plan
- Existing loan terms, maturity, payoff, and lender ask
- T-12, budget, rent roll, occupancy, leasing pipeline, and capex plan
- NOI bridge from underwriting or prior lender update to today
- Sponsor contribution and liquidity
- Requested relief, refinance, or capital structure
- Timeline and decision deadline

---

## Mission

Produce a concise, credible package that answers lender questions before they are asked and supports a specific decision.

---

## Strategy

### Step 1: Define Audience and Ask

Classify audience:

- existing relationship bank
- life company
- agency lender
- CMBS master or special servicer
- debt fund
- preferred-equity / rescue-capital investor

State exact ask:

- refinance quote
- extension
- modification
- forbearance
- consent to subordinate capital
- discounted payoff
- note purchase discussion

### Step 2: Build Current Asset Story

Include:

- what changed since underwriting
- current performance
- leasing and occupancy
- capex execution
- market context
- sponsor actions already taken

### Step 3: Build the Numbers Package

Include:

- T-12
- current rent roll
- budget
- NOI bridge
- debt sizing
- capital need
- reserves
- sensitivity

### Step 4: Build Lender Protections

Propose:

- paydown
- reserves
- reporting
- covenants
- milestones
- cash management
- sponsor contribution

### Step 5: Produce Package Outline and Executive Summary

Deliver a lender-ready structure and list missing exhibits.

---

## Output Format

```markdown
# Lender Update Package
## Property:
## Audience:
## Requested Decision:

### Executive Summary
- ...

### Current Loan and Maturity
| Item | Detail |
|---|---|

### Asset Performance Update
- ...

### NOI Bridge
| Item | Prior / Underwritten | Current | Variance | Explanation |
|---|---:|---:|---:|---|

### Business Plan and Milestones
| Milestone | Date | Evidence |
|---|---|---|

### Proposed Lender Protections
- ...

### Exhibit Checklist
- [ ] T-12
- [ ] Rent roll
- [ ] Budget
- [ ] Leasing pipeline
- [ ] Capex plan
- [ ] Valuation support
- [ ] Sponsor financials

### Open Questions
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- States one clear ask
- Includes lender-facing facts, not just owner narrative
- Reconciles NOI movement
- Includes exhibits checklist
- Identifies lender protections
- Separates known facts from assumptions

---

## Red Flags & Dealbreakers

- Package asks for relief but offers no contribution or protection
- Financials are stale or inconsistent
- NOI bridge does not reconcile
- Maturity deadline is hidden
- Sponsor liquidity is omitted when lender will require it
- Requested decision requires consent from an unidentified party

---

## When Data is Missing

- If financials are missing, create a package skeleton and list required exhibits
- If audience is unclear, produce variants by lender type
- If the ask is unclear, recommend the most lender-credible ask and alternatives
- If sponsor financials are unavailable, flag as likely lender request

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Current financials, rent roll, loan data, business plan, sponsor data, and requested decision are available |
| MEDIUM | Core property and loan data are available, but exhibits or sponsor support are incomplete |
| LOW | Narrative only; no reliable financial package |

---

## Related Knowledge Bases

- [Workout and Extension Structures](knowledge/workout-and-extension-structures.md)
- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)
- [CMBS Servicing and Default Playbook](knowledge/cmbs-servicing-and-default-playbook.md)

## Research Basis

- [Lender Update Package Builder Research](research/capital-markets/lender-update-package-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
