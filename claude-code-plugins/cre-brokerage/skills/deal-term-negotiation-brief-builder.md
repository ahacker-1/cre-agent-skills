---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Deal Term Negotiation Brief Builder

Prepare a seller-side negotiation brief that frames the key business issues, tradeoffs, and escalation points in an LOI or purchase negotiation.

---

## When to Use This Skill

Use this skill when the seller is negotiating terms with one or more buyers and needs a concise view of what to hold, what to trade, and what needs counsel review.

---

## What You'll Need to Provide

- Current LOI or offer terms
- Seller priorities
- Open issues
- Competing offer context if relevant
- Any counsel guidance already received

---

## Mission

Create a negotiation brief that organizes the commercial terms, identifies give / get opportunities, and separates business decisions from legal review items.

---

## Strategy

### Step 1: Summarize the Current Deal

- capture economics
- capture timing
- capture contingencies
- capture assignment and control requests

### Step 2: Identify Seller Priorities

Organize by:

- must have
- preferred
- tradable
- unacceptable

### Step 3: Build the Give / Get Framework

For each open term, state:

- seller ask
- buyer ask
- possible trade
- risk if accepted without additional consideration

### Step 4: Flag Legal Escalation Items

Mark issues that require counsel instead of broker judgment.

---

## Output Format

```markdown
# Negotiation Brief
## Property:
## Status: COMPLETE | PARTIAL | FAILED

### Current Deal Snapshot
- ...

### Seller Priorities
- Must Have:
- Preferred:
- Tradable:
- Unacceptable:

### Give / Get Opportunities
- ...

### Legal Review Needed
- ...

### Recommended Negotiation Posture
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The brief distinguishes business tradeoffs from legal issues
- Seller priorities are explicit
- Every major open issue has a clear recommended posture
- The brief does not drift into legal drafting

---

## When Data is Missing

- If seller priorities are not explicit, infer a conservative default and state it
- If counsel has already raised issues, do not override them
- If competing offer context is missing, focus on deal quality rather than pure leverage tactics

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Clear seller priorities and full current term set available |
| MEDIUM | Most business terms are clear but some priorities or legal boundaries remain unresolved |
| LOW | Fragmented term set or unclear seller priorities |

---

## Related Knowledge Bases

- [Offer Negotiation and Closing Playbook](knowledge/offer-negotiation-and-closing-playbook.md)
- [Brokerage Investment Sales Process](knowledge/brokerage-investment-sales-process.md)

## Research Basis

- [Deal Term Negotiation Brief Builder Research](research/brokerage/deal-term-negotiation-brief-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
