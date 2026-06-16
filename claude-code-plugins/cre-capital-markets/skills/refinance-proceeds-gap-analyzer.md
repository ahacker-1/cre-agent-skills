# Refinance Proceeds Gap Analyzer

Quantify the gap between existing payoff and supportable refinance proceeds.

---

## When to Use This Skill

Use this skill when an owner needs to know how much equity, rescue capital, sale proceeds, or lender concession is required to refinance or pay off an existing CRE loan.

---

## What You'll Need to Provide

- Existing loan payoff or current balance
- Maturity date, default interest, prepayment premium, exit fees, and lender legal costs if known
- Current and stabilized NOI
- Proposed refinance terms or market terms
- Current valuation, cap rate, appraisal, or BOV
- Required reserves and closing costs
- Sponsor contribution and available capital sources

---

## Mission

Calculate supportable new proceeds under DSCR, debt yield, LTV, and reserve constraints, then reconcile the proceeds gap to realistic funding sources.

---

## Strategy

### Step 1: Build the All-In Payoff

Include:

- principal balance
- accrued interest
- default interest, if applicable
- exit fees
- prepayment or yield maintenance
- lender legal and servicer costs
- required escrow or reserve replenishment

### Step 2: Calculate Supportable New Loan Proceeds

Estimate proceeds from:

- DSCR
- debt yield
- LTV
- LTC, if new capital plan is part of the refinance
- lender maximum loan size
- property-type and tenant-risk overlay

### Step 3: Calculate Total Gap

Use:

`total_gap = all_in_payoff + required_reserves + closing_costs - supportable_new_loan`

If the result is negative, identify excess proceeds only after reserves and costs are funded.

### Step 4: Map Funding Sources

Compare:

- sponsor equity
- new common JV equity
- preferred equity
- mezzanine debt
- bridge / stretch senior debt
- asset sale proceeds
- discounted payoff or note purchase

### Step 5: Stress the Gap

Show sensitivity to:

- NOI down 5% and 10%
- interest rate up 50 bps and 100 bps
- cap rate up 25 bps and 50 bps
- required reserve increase

---

## Output Format

```markdown
# Refinance Proceeds Gap Analyzer
## Property:
## Existing Loan:
## Proposed Refinance:

### All-In Payoff
| Component | Amount |
|---|---:|
| Principal | |
| Accrued / default interest | |
| Fees / premium | |
| Legal / servicer costs | |
| Reserve replenishment | |
| Total payoff | |

### Supportable Proceeds
| Test | Max Loan | Constraint |
|---|---:|---|
| DSCR | | |
| Debt yield | | |
| LTV | | |
| LTC / budget | | |
| Recommended supportable proceeds | | |

### Gap
| Item | Amount |
|---|---:|
| All-in payoff | |
| Closing costs and reserves | |
| Supportable proceeds | |
| Total gap | |

### Funding Source Options
| Source | Amount | Pros | Risks |
|---|---:|---|---|

### Sensitivity
| Scenario | Supportable Proceeds | Gap |
|---|---:|---:|

### Recommendation
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Shows all-in payoff rather than principal only
- Uses lowest credible proceeds test
- Separates paydown gap from reserve/cost gap
- Includes sensitivity
- Does not call a gap solved unless source, amount, consent, and timing are identified

---

## Red Flags & Dealbreakers

- Payoff exceeds supportable loan by more than available sponsor capital
- Required reserves are excluded from the funding plan
- Preferred equity or mezzanine is assumed without senior-lender consent
- Stabilized NOI is used before stabilization is funded
- Sensitivity turns a "solved" gap back into an unsolved gap

---

## When Data is Missing

- If payoff is missing, show principal-only and estimated all-in ranges
- If rate terms are missing, test at multiple debt constants
- If value is missing, show DSCR and debt-yield proceeds and mark LTV incomplete
- If capital-source terms are missing, show a source matrix rather than a recommendation

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Payoff, NOI, value, proposed debt terms, costs, reserves, and funding sources are available |
| MEDIUM | Core debt and NOI data are available, but payoff details or funding-source terms are incomplete |
| LOW | Only rough balance, maturity, and property income are available |

---

## Related Knowledge Bases

- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)
- [Rescue Capital and Preferred Equity](knowledge/rescue-capital-and-pref-equity.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Refinance Proceeds Gap Analyzer Research](research/capital-markets/refinance-proceeds-gap-analyzer-research.md)
