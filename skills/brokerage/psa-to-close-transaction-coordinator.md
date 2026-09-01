---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# PSA to Close Transaction Coordinator

Coordinate the seller-side transaction process from signed deal through closing with a milestone timeline, open-issues tracker, and responsibility matrix.

---

## When to Use This Skill

Use this skill once the seller has selected a buyer and the deal is under contract or otherwise in binding execution. It is most valuable when multiple diligence and closing workstreams need to stay aligned.

---

## What You'll Need to Provide

- Signed terms or PSA summary
- key dates and deadlines
- deposit and hard-money milestones
- diligence workstreams
- title / survey / legal status
- buyer request log if available
- seller-side team members and outside parties

---

## Mission

Keep the deal organized from signing to closing by tracking dates, ownership, open issues, and escalation items while staying inside the brokerage coordination role.

---

## Strategy

### Step 1: Build the Milestone Calendar

Track:

- execution date
- deposit dates
- diligence deadlines
- title and survey dates
- financing or evidence deadlines where relevant
- closing date

### Step 2: Build the Responsibility Matrix

Assign owners across:

- seller
- broker
- counsel
- title / escrow
- buyer
- lender-related parties where relevant

### Step 3: Build the Open-Issues Tracker

Track:

- issue
- owner
- deadline
- current status
- escalation path

### Step 4: Flag Process Risk

Identify:

- slipping deadlines
- repeated buyer requests
- deposit hardening risk
- unresolved diligence bottlenecks
- legal issues needing counsel decision

---

## Output Format

```markdown
# PSA to Close Coordination
## Property:
## Status: COMPLETE | PARTIAL | FAILED

### Milestone Calendar
- ...

### Responsibility Matrix
- ...

### Open Issues
- ...

### Key Process Risks
- ...

### Immediate Next Actions
1. ...
2. ...
3. ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- All key dates are listed
- Every issue has an owner
- Broker coordination items are distinct from counsel or title items
- Deposit and contingency milestones are not omitted

---

## When Data is Missing

- If the PSA summary is incomplete, build a provisional tracker and clearly label the gaps
- If responsibility is ambiguous, assign a temporary owner and flag for confirmation
- If a legal issue is unclear, elevate it instead of guessing

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full milestone and issue data available |
| MEDIUM | Most critical dates and issues are known but some ownership or legal detail is incomplete |
| LOW | Major dates, responsibilities, or issues are still unclear |

---

## Related Knowledge Bases

- [Offer Negotiation and Closing Playbook](knowledge/offer-negotiation-and-closing-playbook.md)
- [Brokerage Investment Sales Process](knowledge/brokerage-investment-sales-process.md)

## Research Basis

- [PSA to Close Transaction Coordinator Research](research/brokerage/psa-to-close-transaction-coordinator-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
