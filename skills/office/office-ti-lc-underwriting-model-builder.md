---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Office TI / LC Underwriting Model Builder

Build an office cash-flow model that explicitly reflects downtime, tenant improvements, leasing commissions, free rent, renewal costs, and net effective rent.

---

## When to Use This Skill

Use this skill when office underwriting depends on rollover, vacancy lease-up, second-generation leasing, or repositioning capital. It is the right model when NOI alone overstates cash flow because leasing costs are material.

---

## What You'll Need to Provide

- Rent roll with tenant expirations and current rents
- Vacancy schedule and asking rents
- Market rent, TI, LC, free rent, and downtime assumptions
- Lease terms by tenant size and quality tier
- Purchase price, hold period, exit cap, and debt assumptions
- Base-building capital plan if available
- Sponsor strategy: stabilize, reposition, sell, refi, or harvest cash flow

---

## Mission

Produce a defensible office underwriting model that separates GAAP/stabilized NOI from real cash flow after leasing costs and capital requirements.

---

## Strategy

### Step 1: Build In-Place Income

Calculate:

- current base rent
- reimbursements
- parking/storage/other income
- signed-not-commenced rent
- abatements
- vacant suite market rent
- recoverable vs non-recoverable expenses

### Step 2: Build Rollover Schedule

For each tenant or vacant suite:

- expiration date
- probability of renewal
- downtime if vacated
- market rent
- free rent
- TI
- LC
- renewal TI/LC if retained
- new lease term

### Step 3: Model Leasing Costs Below NOI

Calculate:

```text
TI Dollars = RSF x TI PSF
LC Dollars = Gross Lease Value x Commission Rate
Free Rent Dollars = Monthly Rent x Free Rent Months
Net Leasing Cost = TI + LC + Free Rent + Landlord Work
```

Show timing by year. Do not bury leasing costs in operating expenses.

### Step 4: Calculate Net Effective Rent

For each new or renewed lease:

```text
Net Effective Rent = (Contract Rent Value - TI - LC - Free Rent - Other Concessions) / Lease Term Years / RSF
```

Compare NER to market alternatives and required return.

### Step 5: Model Debt and Cash Flow

Show:

- NOI
- leasing costs
- base-building capital
- debt service
- cash flow after debt service
- debt yield
- DSCR
- refinance value
- exit value

### Step 6: Run Sensitivities

At minimum:

- renewal probability
- downtime
- TI/LC
- rent growth
- exit cap
- debt cost
- terminal vacancy

### Step 7: State Verdict

Classify the deal:

- PASS: cash flow survives leasing cost and debt stress
- MARGINAL: return depends on controllable but material leasing execution
- FAIL: leasing cost, downtime, or debt risk overwhelms returns

---

## Output Format

```markdown
# Office TI / LC Underwriting Model
## Property:
## Strategy:
## Verdict: PASS | MARGINAL | FAIL

### Core Assumptions
- Hold period:
- Exit cap:
- Debt:
- Market rent:
- Vacancy / downtime:
- TI / LC:

### In-Place vs Stabilized
| Metric | In-Place | Stabilized | Notes |
|---|---:|---:|---|
| Occupancy | | | |
| NOI | | | |
| Leasing costs | | | |
| Cash flow after leasing costs | | | |

### Rollover / Lease-Up Schedule
| Year | RSF rolling or vacant | Rent assumption | Downtime | TI | LC | Free rent |
|---|---:|---:|---:|---:|---:|---:|

### Returns
- Going-in yield:
- Stabilized yield:
- Average annual leasing cost:
- DSCR:
- Debt yield:
- IRR:
- Equity multiple:

### Sensitivities
| Case | Key Change | IRR | DSCR Low Point | Verdict |
|---|---|---:|---:|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- TI, LC, free rent, and downtime are modeled separately
- Renewal costs are included, not only new-tenant costs
- In-place NOI is separated from stabilized NOI
- Cash flow after leasing costs is shown
- Debt sizing uses current and stressed cash flow, not only stabilized value
- Sensitivities include leasing cost and downtime

---

## Red Flags & Dealbreakers

- Projected returns disappear after realistic TI/LC
- Debt service cannot be covered during lease-up
- Major rollover requires capital the sponsor cannot fund
- Free rent and downtime are omitted from first-year cash flow
- Exit value assumes stabilized occupancy before the market can absorb space

---

## When Data is Missing

- If TI/LC market data is missing, use ranges from Office TI / LC Economics and reduce confidence
- If debt terms are missing, show an unlevered model and a placeholder debt-sizing sensitivity
- If lease terms are missing, model major tenants individually and use conservative assumptions for the rest
- If operating expenses are missing, use current T-12 or a clearly labeled benchmark proxy

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Rent roll, T-12, lease expirations, TI/LC comps, debt terms, and capex plan are available |
| MEDIUM | Core rent roll and T-12 available, but TI/LC, capex, or debt assumptions are partly estimated |
| LOW | Summary data only; leasing costs or rollover timing materially unknown |

---

## Related Knowledge Bases

- [Office TI / LC Economics](knowledge/office-ti-lc-economics.md)
- [Office Benchmarks](knowledge/office-benchmarks.md)
- [Office Lender Criteria](knowledge/office-lender-criteria.md)
- [Underwriting Calculations](knowledge/underwriting-calc.md)

## Research Basis

- [Office TI / LC Underwriting Model Builder Research](research/office/office-ti-lc-underwriting-model-builder-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
