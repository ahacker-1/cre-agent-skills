---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial IC Memo Writer

Write an investment-committee-ready memo for a U.S. industrial acquisition using market, lease, physical, underwriting, and financing findings.

---

## When to Use This Skill

Use this skill after market, lease, building, underwriting, and financing work is substantially complete. It is intended for acquisitions teams that need a concise but decision-complete memo explaining whether the industrial thesis is durable enough to proceed.

---

## What You'll Need to Provide

- Property overview and subtype
- Market-study findings
- Lease roster / lease abstract findings
- Tenant-credit findings
- Physical inspection summary
- Underwriting model summary
- Financing-fit summary
- Any sponsor or basis-specific concerns

---

## Mission

Synthesize the industrial diligence package into an IC memo that explains the actual investment thesis, the core risks, and whether the deal is supported by durable cash flow, releasability, and realistic financing.

---

## Strategy

### Step 1: Establish the Core Thesis

Summarize the deal in one sentence:

- durable in-place cash flow
- mark-to-market with releasable space
- infill scarcity
- functional upgrade thesis
- tenant-credit durability

### Step 2: Summarize Market and Building Position

Explain:

- submarket strength
- subtype fit
- functional competitiveness
- major physical constraints

### Step 3: Summarize the Lease Story

Explain:

- WALT
- concentration
- near-term rollover
- reimbursement quality
- release risk

### Step 4: Summarize the Capital Story

Explain:

- base-case underwriting
- major CapEx
- downtime / TI / LC assumptions
- financing fit

### Step 5: State the Decision

Recommend:

- proceed
- proceed with mitigations
- proceed only at revised basis
- do not proceed

State exactly why.

---

## Output Format

```markdown
# Industrial IC Memo
## Property:
## Date:
## Recommendation: PROCEED | PROCEED WITH MITIGATIONS | REPRICE | DECLINE

### Executive Summary
- ...

### Asset and Market Position
- ...

### Lease and Tenant Risk
- ...

### Physical and Capital Considerations
- ...

### Financing View
- ...

### Key Risks
1. ...
2. ...
3. ...

### Mitigations
- ...

### Final Recommendation
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The memo states a clear industrial investment thesis
- Market, lease, building, and capital issues are all represented
- The recommendation is basis-aware and not generic
- Industrial-specific risks such as rollover, releasability, and functional obsolescence are explicit

---

## When Data is Missing

- If one diligence stream is incomplete, say so and explain how that changes the recommendation
- If financing feedback is not available, state that the capital conclusion is provisional
- If rollover assumptions are estimated, reflect that in the memo confidence level

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | All core diligence streams complete and consistent |
| MEDIUM | Recommendation is solid but one or two streams remain partially estimated |
| LOW | Material uncertainty remains in lease, physical, or financing conclusions |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)
- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)
- [Industrial Lender Criteria](knowledge/industrial-lender-criteria.md)

## Research Basis

- [Industrial IC Memo Writer Research](research/industrial/industrial-ic-memo-writer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
