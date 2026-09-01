---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Capital Stack Term Sheet Comparator

Normalize and compare senior debt, bridge debt, mezzanine debt, preferred equity, and JV equity term sheets.

---

## When to Use This Skill

Use this skill when comparing two or more capital proposals for an acquisition, refinance, recapitalization, rescue-capital raise, or loan workout.

---

## What You'll Need to Provide

- Term sheets or summaries from each capital source
- Property NOI, value, basis, and business plan
- Existing debt and maturity status, if recapitalizing
- Sponsor objectives: proceeds, certainty, control, cost, speed, or flexibility
- Required consents and closing deadline

---

## Mission

Convert non-comparable proposals into a normalized decision matrix that shows all-in cost, proceeds, control burden, execution risk, and best fit.

---

## Strategy

### Step 1: Normalize Each Proposal

Extract:

- capital type
- proceeds
- rate or return
- fees
- amortization or current pay
- term and extensions
- reserves
- covenants
- recourse
- prepayment / lockout / yield maintenance
- control rights
- required consents
- closing conditions

### Step 2: Calculate All-In Economics

Compare:

- net proceeds after fees and reserves
- annual cash-pay burden
- accrued return
- exit cost
- total cost at expected exit
- sponsor dilution or promote impact

### Step 3: Score Strategic Fit

Score 1-5:

- proceeds
- cost
- certainty
- speed
- flexibility
- control preservation
- downside protection
- exit compatibility

### Step 4: Identify Hidden Terms

Flag:

- springing recourse
- cash sweep
- low DSCR or debt-yield trigger
- mandatory paydown
- approval rights
- transfer restrictions
- drag or forced sale rights
- punitive extension fees
- capex or leasing reserve shortfalls

### Step 5: Recommend Negotiation Moves

List:

- must-fix terms
- tradeable terms
- terms to accept
- questions for lender, investor, or counsel

---

## Output Format

```markdown
# Capital Stack Term Sheet Comparator
## Property:
## Decision Objective:

### Normalized Terms
| Term | Proposal A | Proposal B | Proposal C |
|---|---|---|---|
| Capital type | | | |
| Gross proceeds | | | |
| Net proceeds | | | |
| Rate / return | | | |
| Fees | | | |
| Term / extensions | | | |
| Reserves | | | |
| Recourse | | | |
| Control rights | | | |
| Exit cost | | | |

### Scorecard
| Criterion | Weight | A | B | C |
|---|---:|---:|---:|---:|

### Hidden Issues
- ...

### Recommendation
- Winner:
- Why:
- Negotiation asks:
- Counsel review:

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Compares net proceeds, not just gross proceeds
- Includes current-pay and accrued obligations
- Flags control and consent rights
- Scores against the sponsor's stated objective
- Identifies missing term-sheet items
- Does not rank by lowest rate alone

---

## Red Flags & Dealbreakers

- Highest proceeds also creates unpayable debt service
- Preferred equity has control rights equivalent to a forced-sale mechanism
- Mezzanine proposal lacks senior-lender consent path
- Bridge loan requires takeout assumptions unsupported by stabilized NOI
- Fee and reserve deductions make net proceeds insufficient

---

## When Data is Missing

- If proposals omit fees, reserves, or recourse, list as open items
- If property financials are missing, compare terms only and avoid proceeds verdict
- If sponsor priorities are missing, provide multiple rankings by objective
- If exit assumptions are missing, stress at multiple exit dates

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Full term sheets and property data are available |
| MEDIUM | Major terms available, but legal terms, reserves, or exit economics are incomplete |
| LOW | Summary proposals only; no full term sheets |

---

## Related Knowledge Bases

- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)
- [Rescue Capital and Preferred Equity](knowledge/rescue-capital-and-pref-equity.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Capital Stack Term Sheet Comparator Research](research/capital-markets/capital-stack-term-sheet-comparator-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
