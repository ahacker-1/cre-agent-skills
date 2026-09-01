---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Assignment Intake Manager

Launch a seller-side investment sales assignment by organizing seller goals, authority, required documents, and process readiness before BOV or marketing work begins.

---

## When to Use This Skill

Use this skill when a seller is considering or beginning a commercial investment sale assignment and you need a disciplined kickoff. It is most valuable before building a BOV, listing proposal, OM, or buyer process.

---

## What You'll Need to Provide

- Property name and address
- Property type and basic size metrics
- Seller entity and known ownership structure
- Known selling goals:
  - pricing
  - timing
  - confidentiality
  - buyer profile
- Available documents:
  - rent roll
  - trailing financials
  - leases
  - surveys
  - environmental / condition reports
  - title materials
- Any known broker-engagement constraints or office-exclusive preferences

---

## Mission

Create a seller-side assignment kickoff package that confirms authority, documents what is missing, clarifies objectives, and recommends the correct sale process before pricing and marketing begin.

---

## Strategy

### Step 1: Confirm Assignment Context

- Identify the seller, entity, and likely signing authority
- Confirm whether this is:
  - a broad marketed process
  - a targeted process
  - a confidential process
  - an office-exclusive scenario

### Step 2: Clarify Seller Objectives

Document:

- target timing
- confidentiality preference
- pricing expectations
- required deal certainty
- preferred buyer profile

### Step 3: Inventory the Data Package

Track what is available and missing across:

- property facts
- financials
- leases / tenancy
- legal / title / survey
- physical and environmental materials

### Step 4: Identify Readiness Gaps

Flag missing items that materially weaken:

- BOV quality
- listing proposal credibility
- OM accuracy
- buyer process quality

### Step 5: Recommend the Next Steps

Conclude with:

- what to gather next
- what can begin now
- what should wait until the intake is complete

---

## Output Format

```markdown
# Assignment Intake Summary
## Property:
## Status: COMPLETE | PARTIAL | BLOCKED

### Seller Objectives
- Timing:
- Confidentiality:
- Buyer Profile:
- Process Preference:

### Authority and Representation
- Seller Entity:
- Signing Authority Status:
- Listing / Marketing Authorization Status:

### Document Inventory
- Available:
- Missing:

### Readiness Gaps
- ...

### Recommended Process
- ...

### Immediate Next Steps
1. ...
2. ...
3. ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Seller goals are captured explicitly
- Signing authority and marketing authorization are not assumed
- Missing materials are organized by workstream
- Process recommendation matches the confidentiality and timing goals

---

## When Data is Missing

- If ownership or signing authority is unclear, flag this as a launch blocker
- If financials or leases are incomplete, lower confidence in any pricing next step
- If the seller's process preference is unclear, recommend a provisional process and label it as an assumption

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Authority, objectives, and core documents are clear |
| MEDIUM | Seller goals are clear but key diligence inputs are incomplete |
| LOW | Authority, objectives, or core documents remain uncertain |

---

## Related Knowledge Bases

- [Brokerage Investment Sales Process](knowledge/brokerage-investment-sales-process.md)

## Research Basis

- [Assignment Intake Manager Research](research/brokerage/assignment-intake-manager-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
