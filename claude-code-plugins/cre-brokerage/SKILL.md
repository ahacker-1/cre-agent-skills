---
name: cre-brokerage
description: "CRE Brokerage Investment Sales v1 - 8 specialist skills for U.S. seller-side commercial investment sales brokers, covering assignment intake, broker opinion of value, listing proposal, OM and teaser drafting, buyer process management, bid leveling, negotiation support, and PSA-to-close coordination."
argument-hint: "[task-description]"
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# CRE Brokerage Suite

You have access to 8 specialist brokerage skills for U.S. seller-side investment sales.

## Available Skills

| Skill | File | Use When |
|-------|------|----------|
| Assignment Intake Manager | `skills/assignment-intake-manager.md` | User is beginning a seller-side investment sales assignment and needs a structured kickoff |
| Broker Opinion of Value Builder | `skills/broker-opinion-of-value-builder.md` | User needs a broker pricing opinion or BOV-style listing valuation package |
| Listing Proposal Builder | `skills/listing-proposal-builder.md` | User needs a seller-facing listing proposal or process recommendation |
| Offering Memorandum and Teaser Writer | `skills/offering-memorandum-and-teaser-writer.md` | User needs buyer-facing marketing copy, a teaser, or OM structure |
| Buyer Process and Data Room Manager | `skills/buyer-process-and-data-room-manager.md` | User needs confidentiality, qualification, buyer access, or data-room process control |
| Call for Offers and Bid Leveling Analyst | `skills/call-for-offers-and-bid-leveling-analyst.md` | User needs offer comparison, bid leveling, or BAFO guidance |
| Deal Term Negotiation Brief Builder | `skills/deal-term-negotiation-brief-builder.md` | User needs a seller-side negotiation brief for LOI or purchase terms |
| PSA to Close Transaction Coordinator | `skills/psa-to-close-transaction-coordinator.md` | User needs seller-side transaction coordination from signed deal through closing |

## How to Use

1. Read the user's request to determine which skill is needed
2. Load the full skill file - e.g. `Read skills/broker-opinion-of-value-builder.md`
3. Follow the Strategy steps exactly
4. Produce output in the specified format
5. Run Quality Checks before delivering results

For deeper analysis, load knowledge bases:

- `knowledge/brokerage-investment-sales-process.md` - seller-side process map from assignment intake through closing
- `knowledge/broker-opinion-of-value-guidance.md` - BOV vs appraisal boundaries, methods, and disclaimer logic
- `knowledge/marketing-confidentiality-and-buyer-process.md` - teaser, OM, confidentiality, buyer vetting, and data-room workflow
- `knowledge/offer-negotiation-and-closing-playbook.md` - offer comparison, BAFO, negotiation posture, and PSA-to-close coordination

If the user says "$ARGUMENTS", use that to determine which skill to load.

## Quick Reference

**Assignment Intake Manager** - seller kickoff, authority, missing data, process recommendation.

**Broker Opinion of Value Builder** - pricing opinion, comp synthesis, disclaimer logic, recommended ask and process range.

**Listing Proposal Builder** - seller-facing proposal, positioning, marketing strategy, timeline, and scope framing.

**Offering Memorandum and Teaser Writer** - teaser, OM structure, confidentiality-aware marketing package.

**Buyer Process and Data Room Manager** - buyer registration, qualification, data-room access, tours, and Q&A.

**Call for Offers and Bid Leveling Analyst** - offer matrix, certainty analysis, leveling, BAFO guidance, backup strategy.

**Deal Term Negotiation Brief Builder** - seller priorities, give / get framing, legal-escalation flags, negotiation posture.

**PSA to Close Transaction Coordinator** - milestone calendar, responsibility matrix, open issues, and close readiness.

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
