---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Office Lease Abstract Reviewer

Review office lease abstracts or full leases for rent, recoveries, TI, options, assignment, sublease, and transaction-critical obligations.

---

## When to Use This Skill

Use this skill during acquisition diligence, refinancing, asset management, or leasing review when office leases need to be converted into decision-ready economic and legal issue summaries.

---

## What You'll Need to Provide

- Lease, amendment, abstract, or lease summary
- Rent roll and tenant name
- Premises RSF and measurement standard if known
- Any side letters, work letters, guaranties, SNDA, estoppels, or commencement agreements
- Business question: acquisition diligence, lender review, renewal decision, or dispute issue spotting

---

## Mission

Extract the lease terms that affect office cash flow, rollover risk, recoveries, capital obligations, tenant control rights, and lender/investor risk.

---

## Strategy

### Step 1: Identify Document Stack

List reviewed documents:

- original lease
- amendments
- commencement letters
- work letters
- guaranties
- estoppels
- SNDAs
- side letters
- assignments or subleases

State whether any expected document is missing.

### Step 2: Abstract Economics

Extract:

- premises and RSF
- lease term
- commencement and expiration
- base rent schedule
- rent abatements
- escalations
- operating expense structure
- tax, insurance, utility, cleaning, parking, and after-hours charges
- security deposit or letter of credit

### Step 3: Abstract Recoveries

Determine:

- full-service, modified gross, base year, expense stop, or NNN
- base year or stop amount
- tenant pro rata share
- gross-up provisions
- controllable expense caps
- exclusions
- audit rights
- capital expense pass-through treatment

### Step 4: Abstract Work Letter and TI

Extract:

- TI allowance
- eligible and excluded costs
- disbursement mechanics
- tenant contribution
- substantial completion
- tenant delay
- rent commencement
- ownership and removal obligations

### Step 5: Abstract Options and Control Rights

Extract:

- renewal
- expansion
- ROFO / ROFR
- contraction
- termination
- purchase option
- signage
- parking
- assignment and sublease
- recapture
- profit sharing
- affiliate transfer

### Step 6: Identify Investor and Lender Issues

Flag:

- rights that impair sale, financing, or leasing flexibility
- near-term termination or contraction rights
- below-market renewal options
- unrecoverable expense exposure
- unfunded landlord capital obligations
- lease language that conflicts with rent roll assumptions

---

## Output Format

```markdown
# Office Lease Abstract Review
## Tenant:
## Premises:
## Documents Reviewed:
## Verdict: CLEAN | NEEDS FOLLOW-UP | HIGH RISK

### Economic Terms
| Item | Finding | Source / Notes |
|---|---|---|
| Term | | |
| RSF | | |
| Base rent | | |
| Escalations | | |
| Abatement | | |
| Recoveries | | |
| Security | | |

### TI / Work Letter
- Allowance:
- Eligible costs:
- Disbursement:
- Rent commencement:
- Landlord obligations:

### Options and Control Rights
| Right | Tenant Position | Investor Impact |
|---|---|---|

### Diligence Issues
| Issue | Severity | Why It Matters | Next Step |
|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Original lease and all amendments are considered together
- Rent schedule reconciles to the rent roll
- Recovery structure is clearly classified
- TI/work letter obligations are separated from operating expenses
- Options and termination rights are not buried in narrative
- Missing documents are listed explicitly

---

## Red Flags & Dealbreakers

- Tenant has a termination, contraction, or purchase right not reflected in underwriting
- Renewal option is materially below market
- Landlord owes material TI or base-building work with no reserve
- Expense caps or exclusions prevent recovery of rising costs
- Assignment/sublease rights create discounted competing space
- Premises RSF differs from rent roll without explanation

---

## When Data is Missing

- If amendments are missing, treat the abstract as incomplete
- If the work letter is missing, do not assume TI obligations are zero
- If expense provisions are unclear, flag for counsel and model recoveries conservatively
- If RSF conflicts across documents, show each figure and request BOMA or lease measurement support

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full lease stack, amendments, work letter, and rent roll are available and reconciled |
| MEDIUM | Core lease available but one amendment, estoppel, or work letter detail is missing |
| LOW | Abstract-only review or missing economic provisions |

---

## Related Knowledge Bases

- [Office Lease Structures](knowledge/office-lease-structures.md)
- [Office TI / LC Economics](knowledge/office-ti-lc-economics.md)
- [Office Benchmarks](knowledge/office-benchmarks.md)

## Research Basis

- [Office Lease Abstract Reviewer Research](research/office/office-lease-abstract-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
