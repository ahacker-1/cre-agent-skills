---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Broker Opinion of Value Builder

Build a seller-side commercial investment sales pricing opinion that frames valuation, recommended pricing, and process strategy without presenting the output as an appraisal.

---

## When to Use This Skill

Use this skill when you need to prepare a broker pricing opinion for a seller who is considering a sale or deciding how to launch an assignment. It is most useful after assignment intake but before the listing proposal is finalized.

---

## What You'll Need to Provide

- Property name and address
- Property type and basic characteristics
- Available operating data, lease data, or land data
- Comparable sales and listing evidence if available
- Known market context
- Seller timing or process preferences
- State or jurisdiction if known

---

## Mission

Produce a broker opinion of value that explains the basis for the pricing recommendation, frames the recommended marketing range, and includes the correct brokerage disclaimers and limitations.

---

## Strategy

### Step 1: Define the Purpose

- Identify the intended user
- State the purpose of the pricing opinion
- Note any current or contemplated brokerage interest

### Step 2: Select the Valuation Lenses

Use one or more of:

- sales comparison
- income / cap-rate framing
- cost / land / replacement logic

### Step 3: Build the Evidence Set

Summarize:

- relevant comps
- market positioning
- financial support where applicable
- assumptions and limitations

### Step 4: Produce a Pricing Recommendation

State:

- value or pricing range
- recommended ask or guidance strategy
- why the process choice supports the pricing goal

### Step 5: Include Boundary Language

Explicitly state:

- not an appraisal
- limiting conditions
- confidence drivers
- any state-specific caution on terminology or scope

---

## Output Format

```markdown
# Broker Opinion of Value
## Property:
## Date:
## Status: COMPLETE | PARTIAL | FAILED

### Purpose and Intended User
- ...

### Property Summary
- ...

### Valuation Approaches Used
- ...

### Market Evidence
- ...

### Recommended Pricing View
- Value / Pricing Range:
- Recommended Ask / Guidance:
- Process Recommendation:

### Limiting Conditions
- ...

### Disclaimer
- This is not an appraisal.

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Purpose, intended user, and contemplated interest are stated
- The output is clearly not positioned as an appraisal
- Method selection matches the property type and available data
- Pricing recommendation is tied to both evidence and process

---

## When Data is Missing

- If comps are weak, widen the range and state lower confidence
- If operating data is incomplete, avoid a narrow income-based conclusion
- If state-specific terminology risk is unclear, add a stronger boundary note and recommend brokerage compliance review

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Strong comps, appropriate methods, and good property data |
| MEDIUM | Good directional evidence but meaningful assumptions remain |
| LOW | Thin comp set, weak property data, or major state-law caution issues |

---

## Related Knowledge Bases

- [Broker Opinion of Value Guidance](knowledge/broker-opinion-of-value-guidance.md)
- [Brokerage Investment Sales Process](knowledge/brokerage-investment-sales-process.md)

## Research Basis

- [Broker Opinion of Value Builder Research](research/brokerage/broker-opinion-of-value-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
