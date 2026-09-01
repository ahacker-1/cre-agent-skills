---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Lease Abstract Reviewer

Review and abstract industrial leases for economic terms, operating obligations, transfer rights, and transaction-critical provisions.

---

## When to Use This Skill

Use this skill when you have one or more industrial leases and need a consistent abstract for acquisitions, financing, or lease-risk analysis. It is most valuable when reimbursement mechanics, repair obligations, options, or transfer rights could materially affect cash flow or execution.

---

## What You'll Need to Provide

- Lease document(s) and amendments
- Property address and subtype if known
- Tenant name and leased square footage
- Any estoppel or SNDA forms already circulating
- Any lender or acquisition diligence issues already identified

---

## Mission

Abstract the lease with emphasis on industrial economics and obligations. Surface reimbursement mechanics, repairs, options, transfer rights, and lender-sale diligence items that matter to underwriting and transaction certainty.

---

## Strategy

### Step 1: Capture Core Economic Terms

- Premises and square footage
- Lease term and dates
- Base rent schedule
- Rent steps
- Free rent or abatement

### Step 2: Abstract Reimbursements

Identify:

- taxes
- insurance
- CAM or operating expenses
- gross-up rules
- caps or exclusions
- capital improvement recovery language

### Step 3: Abstract Repair and Replacement Allocation

Identify who is responsible for:

- roof
- structure
- slab
- HVAC
- loading doors and dock equipment
- parking lot / truck court
- sprinklers and fire-life-safety systems

### Step 4: Abstract Rights and Restrictions

Review:

- assignment and subletting
- affiliate transfer rights
- recapture rights
- expansion / contraction / termination options
- purchase or renewal options

### Step 5: Abstract Transaction-Critical Items

Review:

- estoppel timing and form requirements
- SNDA requirements
- lender-consent or notice mechanics
- casualty and condemnation
- restoration obligations

### Step 6: Flag Underwriting-Significant Provisions

Flag:

- unusually weak recovery language
- tenant-favorable transfer rights
- landlord-unfriendly repair allocations
- abatements that suspend more than base rent
- options that materially alter release risk or value

---

## Output Format

```markdown
# Industrial Lease Abstract
## Tenant:
## Property:
## Status: COMPLETE | PARTIAL | FAILED

### Core Terms
- Premises:
- Square Feet:
- Lease Term:
- Base Rent:
- Rent Steps:
- Free Rent / Abatement:

### Reimbursements
- Taxes:
- Insurance:
- CAM / Operating Expenses:
- Exclusions / Caps:
- Capital Recovery:

### Repairs and Replacements
- Roof:
- Structure:
- Slab:
- HVAC:
- Loading / Dock Equipment:
- Parking / Truck Court:

### Rights and Options
- Assignment / Subletting:
- Affiliate Transfers:
- Expansion / Contraction / Termination:
- Renewal / Purchase:

### Transaction-Critical Items
- Estoppel:
- SNDA:
- Casualty / Condemnation:
- Default / Cure:

### Key Red Flags
- ...

### Underwriting Impact
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Reimbursement structure is abstracted in detail, not just labeled NNN or gross
- Repair obligations are separated by system and component
- Transfer rights and options are clearly summarized
- Estoppel and SNDA items are not omitted
- The abstract states which issues matter to underwriting or sale / financing execution

---

## When Data is Missing

- If amendments are missing, flag the abstract as incomplete
- If exhibits or legal descriptions are missing, note the effect on confidence
- If reimbursement language is ambiguous, mark it as unresolved instead of choosing a favorable interpretation

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full lease, amendments, and key exhibits available |
| MEDIUM | Core lease available but exhibits or amendments incomplete |
| LOW | Partial lease text or summarized terms only |

---

## Related Knowledge Bases

- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)
- [Industrial Lender Criteria](knowledge/industrial-lender-criteria.md)

## Research Basis

- [Industrial Lease Abstract Reviewer Research](research/industrial/industrial-lease-abstract-reviewer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
