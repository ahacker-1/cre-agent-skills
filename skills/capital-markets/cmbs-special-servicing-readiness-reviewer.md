---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# CMBS / Special Servicing Readiness Reviewer

Assess borrower readiness for CMBS watchlist, maturity default, transfer to special servicing, or workout negotiation.

---

## When to Use This Skill

Use this skill when a securitized loan is watchlisted, nearing maturity, in covenant stress, in default, or likely to require a material modification.

---

## What You'll Need to Provide

- Loan documents, servicer correspondence, or remittance/watchlist excerpts
- Loan balance, maturity, rate, amortization, reserves, covenants, and default status
- Master servicer and special servicer contact path if known
- Current rent roll, T-12, budget, valuation support, and business plan
- Borrower request, proposed resolution, and timeline

---

## Mission

Identify what the borrower needs to know, prepare, and decide before engaging a master servicer, special servicer, controlling class, or counsel.

---

## Strategy

### Step 1: Confirm Servicing Status

Classify:

- performing with routine master-servicer request
- watchlisted
- imminent maturity issue
- transfer likely
- specially serviced
- monetary or non-monetary default

### Step 2: Identify Decision Authority

Map:

- master servicer authority
- special servicer authority
- controlling class / directing certificateholder role
- PSA or loan-document constraints
- consent or notice requirements

### Step 3: Build Readiness Checklist

Check whether borrower has:

- current financial package
- current rent roll and lease status
- valuation support
- clear ask
- recovery comparison
- cash-flow forecast
- sponsor contribution
- legal issue list
- tax, insurance, environmental, and life-safety status

### Step 4: Diagnose Transfer and Default Risk

Flag:

- maturity default
- payment default
- covenant default
- borrower statement of inability to pay
- collateral value decline
- unauthorized transfer or subordinate debt
- missing reporting

### Step 5: Recommend Engagement Plan

State:

- who to contact
- what to submit
- what to avoid saying without counsel
- likely servicer questions
- expected fees, reserves, and timeline

---

## Output Format

```markdown
# CMBS / Special Servicing Readiness Review
## Property:
## Loan / Trust:
## Current Status:
## Readiness Rating: READY | PARTIAL | NOT READY

### Servicing Map
| Role | Known Party | Action Needed |
|---|---|---|

### Transfer / Default Risk
| Trigger | Status | Notes |
|---|---|---|

### Package Readiness
| Item | Status | Gap |
|---|---|---|

### Borrower Ask
- ...

### Servicer Questions to Prepare For
- ...

### Recommended Next Steps
- ...

### Counsel / Tax Review Items
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Distinguishes master servicing from special servicing
- Identifies whether the PSA or loan documents must be reviewed
- Frames borrower proposal around recovery and feasibility
- Lists missing package items
- Flags legal, tax, guaranty, and default communication risks

---

## Red Flags & Dealbreakers

- Borrower does not know if the loan is securitized
- Material modification request is sent without current financials
- Borrower admits inability to pay without counsel strategy
- No recovery comparison is prepared
- Taxes, insurance, or life-safety obligations are unresolved
- Guaranty carveout exposure is ignored

---

## When Data is Missing

- If PSA is missing, use general CMBS servicing principles and require document review
- If servicer status is unknown, create questions to confirm it
- If financials are missing, mark package not ready
- If default status is unclear, advise counsel review before borrower communication

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Loan documents, servicer status, current financials, and borrower request are available |
| MEDIUM | Loan and property data are available, but PSA, servicer status, or request details are incomplete |
| LOW | Borrower summary only; no documents or current financial package |

---

## Related Knowledge Bases

- [CMBS Servicing and Default Playbook](knowledge/cmbs-servicing-and-default-playbook.md)
- [Workout and Extension Structures](knowledge/workout-and-extension-structures.md)
- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)

## Research Basis

- [CMBS / Special Servicing Readiness Reviewer Research](research/capital-markets/cmbs-special-servicing-readiness-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
