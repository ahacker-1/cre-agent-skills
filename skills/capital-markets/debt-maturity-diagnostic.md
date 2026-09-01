---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Debt Maturity Diagnostic

Diagnose a CRE loan maturity, quantify refinance risk, and identify the immediate decision path.

---

## When to Use This Skill

Use this skill when a property loan is inside 24 months of maturity, has an upcoming extension test, may fail refinance sizing, or needs a clear maturity-risk dashboard.

---

## What You'll Need to Provide

- Property type, address, size, occupancy, and business plan
- Existing loan amount, lender type, maturity date, rate, amortization, IO period, reserves, covenants, and extension options
- Current payoff estimate, including fees if available
- T-12, current NOI, budget, rent roll, and leasing/capex plan
- Current valuation, purchase price, basis, or BOV
- Sponsor liquidity and willingness to contribute, if known

---

## Mission

Determine whether the upcoming maturity is likely refinanceable, extendable, recapitalizable, or headed toward sale/workout/default risk. Produce a practical action plan with dates.

---

## Strategy

### Step 1: Classify the Maturity Window

Classify urgency:

- EARLY WATCH: 12-24 months out
- ACTIVE REFI WINDOW: 6-12 months out
- URGENT MATURITY: 90-180 days out
- CRITICAL / DEFAULT RISK: under 90 days, extension failed, or payment default likely

### Step 2: Build the Loan Snapshot

Summarize:

- lender and servicing path
- current debt
- maturity and extension rights
- rate type and reset risk
- amortization and IO status
- current reserves
- default, cash sweep, and lockbox triggers
- guaranty and recourse exposure

### Step 3: Size Refinance Feasibility

Use Capital Markets Benchmarks to test:

- DSCR on current NOI
- DSCR on stabilized NOI
- debt yield on current NOI
- LTV on current value
- loan-per-unit, loan-per-key, or loan-per-SF sanity check
- refinance gap against estimated payoff

### Step 4: Diagnose the Constraint

Name the controlling problem:

- proceeds gap
- maturity timing
- cash-flow coverage
- value impairment
- property-type lender appetite
- tenant rollover
- capex or leasing reserve need
- sponsor liquidity
- consent or servicing constraint

### Step 5: Recommend the Path

Choose one or more:

- refinance now
- refinance after NOI bridge
- extension request
- workout / modification
- rescue capital / preferred equity
- sale
- note purchase / discounted payoff exploration

---

## Output Format

```markdown
# Debt Maturity Diagnostic
## Property:
## Existing Lender / Servicer:
## Maturity Date:
## Risk Rating: LOW | MODERATE | HIGH | CRITICAL

### Loan Snapshot
| Item | Detail |
|---|---|
| Current balance / payoff | |
| Rate / amortization | |
| Maturity / extension options | |
| Current NOI | |
| Current value support | |
| Sponsor liquidity | |

### Refinance Sizing Snapshot
| Test | Result | Pass / Fail | Notes |
|---|---:|---|---|
| DSCR - current NOI | | | |
| DSCR - stabilized NOI | | | |
| Debt yield - current NOI | | | |
| LTV | | | |
| Refinance gap | | | |

### Controlling Constraint
- ...

### Recommended Path
- ...

### 30 / 60 / 90 Day Action Plan
| Date / Window | Action | Owner |
|---|---|---|

### Data Gaps
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Uses maturity date and payoff, not only original loan amount
- Separates current NOI from stabilized NOI
- Names the controlling sizing test or constraint
- Flags extension rights and servicing path
- Gives dated next actions
- Does not treat lower future rates as a plan by itself

---

## Red Flags & Dealbreakers

- Maturity inside 90 days with no package or payoff
- Existing loan balance exceeds supportable proceeds and no paydown source exists
- Extension option depends on tests the asset cannot meet
- Major capex, leasing, tax, or insurance reserve need is not funded
- Borrower is already in monetary default
- Guarantor exposure is unknown

---

## When Data is Missing

- If payoff is missing, estimate from current balance and flag as preliminary
- If value is missing, size against debt yield and DSCR first
- If sponsor liquidity is missing, present path alternatives with and without sponsor contribution
- If loan documents are missing, mark extension and default analysis as incomplete

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Loan terms, payoff, maturity, financials, rent roll, value support, and sponsor liquidity are available |
| MEDIUM | Loan and property data are available, but payoff, value, or sponsor liquidity is incomplete |
| LOW | Summary debt amount and maturity only; no reliable operating or document data |

---

## Related Knowledge Bases

- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)
- [Workout and Extension Structures](knowledge/workout-and-extension-structures.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Debt Maturity Diagnostic Research](research/capital-markets/debt-maturity-diagnostic-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
