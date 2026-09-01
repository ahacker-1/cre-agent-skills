---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Term Sheet Builder

Assemble a complete draft term sheet and financing recommendation from a selected lender quote, calculating final deal metrics, reserve requirements, closing costs, and conditions precedent.

---

## When to Use This Skill

Use this skill once you have selected a preferred lender and want to formalize the financing structure into a draft term sheet and full financing recommendation. It is the right tool when moving from quote comparison into active lender engagement — producing a structured document that captures every loan term, calculates final returns at those exact terms, and identifies conditions and risks that must be managed through closing. It also prepares the handoff package for legal review.

---

## What You'll Need to Provide

- **Selected lender quote**: the specific lender and all quoted terms (rate, LTV, term, amortization, IO period, prepayment structure, fees, recourse, reserves)
- **Fallback option**: the #2 lender quote (used if the primary has material gaps or risks)
- **Purchase price** and equity structure
- **NOI projections**: 5-year pro forma (Year 1 minimum)
- **Exit cap rate assumption** for exit value calculation
- **Hold period** (typically 5 years)
- **Property details**: name, address, unit count, entity name (if known)
- **Closing cost estimates**: appraisal, environmental, title, legal, and other third-party costs if known
- **Stress test / scenario analysis results** (if available) — used to assess covenant breach probability

---

## Mission

Assemble the recommended term sheet based on the best financing option. Document all key loan terms, calculate final deal metrics at the recommended financing, identify conditions and risks, and produce structured output that supports legal document review.

---

## Strategy

### Step 1: Select Recommended Lender and Structure

From the quote comparison output or the lender terms provided, extract the top recommended lender and all associated terms:

```
recommended = top_ranked lender with complete terms

Verify:
  - Lender name and category
  - All quoted terms are complete (no gaps)
  - Terms are consistent with deal requirements
  - If any terms are missing, flag for manual input
```

If the top recommendation has material gaps or risks, document a fallback to option #2.

### Step 2: Build Complete Term Sheet

Assemble every key term into a formal term sheet document:

#### Loan Amount and Structure
```
Loan Amount: $X (Purchase Price x LTV)
  OR: $X (specific amount from lender quote)
Loan-to-Value: X%
Loan-to-Cost: X% (if CapEx included in basis)
Equity Required: Purchase Price + Closing Costs + Reserves - Loan Amount
```

#### Interest Rate Terms
```
Interest Rate: X.XX% (fixed / floating)
  IF floating: Index + Spread (e.g., SOFR + 250bps)
  Rate type: Fixed / Floating / Hybrid
  Rate lock: At application / commitment / closing
  Rate lock period: X days
  Float-down provision: Yes / No
```

#### Loan Term and Amortization
```
Loan Term: X years
Amortization: X years (or interest-only)
Interest-Only Period: X years (if applicable)
Maturity Date: {calculated from expected closing}
Extension Options: X x X-year extensions (if available)
  Extension conditions: {list}
```

#### Debt Service Coverage
```
DSCR Covenant: X.Xx minimum
  Measured: Quarterly / Annually
  Consequence of breach: Cash sweep / lockbox / default
Debt Yield Minimum: X% (if applicable)
```

#### Prepayment Terms
```
Prepayment Structure: Yield maintenance / Defeasance / Step-down / Open
  IF yield maintenance: Based on {treasury rate + spread}
  IF defeasance: Estimated cost at exit year: $X
  IF step-down: Schedule (e.g., 5/4/3/2/1)
  IF open: Open period starts {date/year}
Estimated Prepayment Cost at Year {hold_period}: $X
```

#### Reserve Requirements
```
Tax Reserves: $X/month (1/12 of annual taxes)
Insurance Reserves: $X/month (1/12 of annual premium)
Capital Expenditure Reserves: $X/unit/year OR $X/month
Replacement Reserves: $X/unit/year (if separate from CapEx)
TI/LC Reserves: $X (if applicable)
Operating Reserve: $X (if required)
Total Monthly Reserves: $X
Total Initial Reserve Deposit: $X
```

#### Recourse and Guarantor
```
Recourse: Non-recourse / Partial recourse / Full recourse
  IF partial: Burn-off schedule / amount
Bad-boy carve-outs: Standard (fraud, environmental, bankruptcy, etc.)
Guarantor Requirements:
  - Net worth: $X minimum (typically 1x loan amount)
  - Liquidity: $X minimum (typically 10% of loan)
  - Credit score: {minimum}
  - Experience: {units/deals required}
```

#### Rate Lock and Closing
```
Rate Lock: {when locked and for how long}
Application Fee: $X (refundable / non-refundable)
Good Faith Deposit: $X
Estimated Closing Costs:
  - Origination fee: $X (X% of loan)
  - Legal fees (lender): $X
  - Appraisal: $X
  - Environmental: $X
  - Title insurance: $X
  - Survey: $X
  - Recording fees: $X
  - Other: $X
  - Total estimated closing costs: $X
Expected Closing Timeline: X weeks from application
```

#### Conditions Precedent to Closing
```
Standard conditions:
  - Satisfactory appraisal (value >= $X)
  - Satisfactory environmental report (Phase I clean)
  - Satisfactory physical inspection
  - Clear title
  - Insurance binder
  - Entity formation documents
  - Guarantor financial package
  - Property financial statements (trailing 12 months)

Special conditions (lender-specific):
  - {any special requirements from this lender}
```

### Step 3: Calculate Final Deal Metrics at Recommended Terms

Recalculate all deal metrics using the exact recommended financing terms:

```
Equity Investment:
  Down payment: Purchase Price - Loan Amount
  Closing costs: (estimated above)
  Initial reserves: (from reserve requirements)
  Total equity: down payment + closing costs + reserves

Annual Debt Service:
  IF IO period: Year 1-{IO}: Loan Amount x Rate / 12 x 12
  Amortizing years: standard mortgage calculation
    monthly_payment = loan_amount x [r(1+r)^n] / [(1+r)^n - 1]
    where r = monthly rate, n = amortization months

Net Cash Flow by Year:
  Year N: NOI(N) - Debt Service(N) - Reserve Contributions(N)

Returns at Recommended Terms:
  - In-Place Cap Rate: Year 1 NOI / Purchase Price
  - DSCR by year: NOI / Debt Service (each year)
  - Cash-on-Cash by year: Net Cash Flow / Total Equity
  - Debt Yield: NOI / Loan Amount
  - Exit Value: Year 5 NOI / Exit Cap Rate
  - Loan Balance at Exit: Remaining principal after amortization
  - Net Proceeds: Exit Value - Loan Balance - Prepayment Cost - Selling Costs
  - IRR: Solved from equity outflow and annual cash flows + net proceeds
  - Equity Multiple: (Total Cash Flows + Net Proceeds) / Total Equity
```

### Step 4: Identify Conditions and Risks

```
Financing Risks:
  - Rate risk: {is rate locked? for how long?}
  - Execution risk: {lender track record, timeline certainty}
  - Retrading risk: {appraisal risk, underwriting stringency}
  - Covenant risk: {probability of DSCR breach from stress test data}
  - Refinance risk: {if bridge loan, exit to perm feasibility}

Conditions requiring action:
  - {list all conditions that must be satisfied before closing}
  - {flag any that are uncertain or risky}

Deal-breaker scenarios:
  - Appraisal comes in below $X (loan reduction)
  - Environmental Phase I reveals RECs requiring Phase II
  - Rate lock expires before closing
  - Guarantor does not meet requirements
```

---

## Output Format

Produce two outputs:

### Output 1: Draft Term Sheet

```markdown
# Draft Term Sheet: {Property Name}
## {Lender Name} | {Loan Category}
## Date: {date}

---

### Borrower
{Entity name TBD}

### Property
{Property name, address, units}

### Loan Amount
${X} ({X}% LTV)

### Interest Rate
{X.XX}% {fixed/floating}
{Rate lock details}

### Term / Amortization
{X}-year term / {X}-year amortization
{IO period if applicable}

### Debt Service
Year 1: ${X}/month (${X}/year)
{Note IO vs amortizing schedule}

### DSCR Covenant
Minimum {X.Xx} {quarterly/annual}

### Prepayment
{Type and schedule}
Estimated cost at Year {X}: ${X}

### Reserves
| Reserve | Monthly | Annual | Initial Deposit |
|---------|---------|--------|-----------------|
| Tax | $X | $X | $X |
| Insurance | $X | $X | $X |
| CapEx | $X | $X | $X |
| Replacement | $X | $X | $X |
| Operating | - | - | $X |
| **Total** | **$X** | **$X** | **$X** |

### Recourse
{Non-recourse / Partial / Full}
{Bad-boy carve-outs: standard}

### Guarantor Requirements
- Net Worth: $X minimum
- Liquidity: $X minimum
- Experience: {requirement}

### Estimated Closing Costs
| Item | Amount |
|------|--------|
| Origination Fee | $X |
| Legal (Lender) | $X |
| Appraisal | $X |
| Environmental | $X |
| Title Insurance | $X |
| Survey | $X |
| Recording | $X |
| Other | $X |
| **Total** | **$X** |

### Timeline
Application to closing: {X} weeks

### Conditions Precedent
1. Satisfactory appraisal (value >= $X)
2. Phase I environmental (clean)
3. Clear title and title insurance
4. Insurance binder
5. Entity formation
6. Guarantor financial package
7. {Lender-specific conditions}

---
*This is a draft term sheet for internal use. Final terms subject to lender underwriting and approval.*
```

### Output 2: Financing Recommendation

```markdown
# Financing Recommendation: {Property Name}
## Date: {date}
## Recommended Lender: {name} ({category})

### Final Deal Metrics at Recommended Terms

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Loan Amount | $X | - | - |
| LTV | X% | Max 75% | PASS/FAIL |
| Equity Required | $X | - | - |
| Year 1 DSCR | X.Xx | Min 1.25x | PASS/FAIL |
| Year 1 Cash-on-Cash | X% | Min X% | PASS/FAIL |
| Debt Yield | X% | Min X% | PASS/FAIL |
| 5-Year IRR | X% | Min X% | PASS/FAIL |
| Equity Multiple | X.Xx | Min X.Xx | PASS/FAIL |

### Cash Flow Summary (at Recommended Terms)

| Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|------|--------|--------|--------|--------|--------|
| NOI | $X | $X | $X | $X | $X |
| (-) Debt Service | $X | $X | $X | $X | $X |
| = Net Cash Flow | $X | $X | $X | $X | $X |
| Cash-on-Cash | X% | X% | X% | X% | X% |
| DSCR | X.Xx | X.Xx | X.Xx | X.Xx | X.Xx |

### Exit Analysis
- Exit Value (Yr 5 NOI / Exit Cap): $X
- Loan Balance at Exit: $X
- Prepayment Cost: $X
- Selling Costs (X%): $X
- Net Proceeds: $X

### Total Return
- Total Equity Invested: $X
- Total Cash Distributions (Yrs 1-5): $X
- Net Sale Proceeds: $X
- Total Return: $X
- IRR: X%
- Equity Multiple: X.Xx

### Sources & Uses

| Sources | Amount |
|---------|--------|
| Loan Proceeds | $X |
| Sponsor Equity | $X |
| **Total Sources** | **$X** |

| Uses | Amount |
|------|--------|
| Purchase Price | $X |
| Closing Costs | $X |
| Initial Reserves | $X |
| CapEx Budget (Year 1) | $X |
| **Total Uses** | **$X** |

### Conditions & Risks

**Conditions Requiring Action:**
1. {condition and status}
2. {condition and status}

**Key Risks:**
| Risk | Severity | Mitigation |
|------|----------|------------|
| {risk} | Low/Med/High | {mitigation} |

**Deal-Breaker Scenarios:**
- {scenario and contingency plan}

### Recommendation
{Final recommendation narrative: why this financing option, how it aligns with the investment thesis, key advantages, what must go right}

### Next Steps for Legal Review
- Loan terms for document review: {reference to term sheet above}
- Key terms requiring legal attention: {list}
- Timeline dependencies: {what must happen by when}
```

---

## Quality Checks

Before finalizing both outputs, verify:

**Sources and Uses Balance**
- Total sources must equal total uses exactly — adjust equity to balance if needed

**Numeric Sanity**
- Loan amount: must be > 0 and <= purchase price x max LTV (75%) — flag if outside
- Interest rate: must match the selected quote exactly — flag any mismatch
- Loan term: minimum 5 years — flag if below
- DSCR at proposed terms: minimum 1.25x — flag any breach
- Monthly reserves x 12 = annual reserves — recalculate if not equal
- Total closing costs should be within 2–4% of loan amount — flag if outside range
- Equity = down payment + closing costs + reserves — recalculate if not equal

**Threshold Cross-Check**

| Output Metric | Threshold | Pass | Fail |
|--------------|-----------|------|------|
| LTV | Max 75% | <= 75% | > 75% |
| DSCR (Year 1) | Min 1.25x | >= 1.25 | < 1.25 |
| DSCR (all years) | Min 1.0x floor | >= 1.0 | < 1.0 — flag critical risk |
| Loan Term | Min 5 years | >= 5 | < 5 |
| Prepayment Penalty | Within market norms | Reasonable | Flag if excessive |

**Completeness**
- All sections of the term sheet filled — no TBD or placeholder values remaining; flag gaps for manual completion
- Term sheet rate matches the quote comparison rate exactly — correct if different
- Sources & uses structured data included for legal review

**Logic**
- Metric consistency: term sheet metrics and recommendation metrics agree — reconcile if different
- Loan amount = purchase price x LTV — recalculate if not equal
- Rate lock risk noted: flag if rate is not locked or lock expires before expected closing

---

## When Data is Missing

**If the quote is missing specific terms** (e.g., reserve amounts not specified): Use the following defaults and note them as assumptions:
- Tax reserves: 1/12 of estimated annual property taxes
- Insurance reserves: 1/12 of estimated annual premium
- CapEx/replacement reserves: $250–$350/unit/year (use Multifamily Benchmarks knowledge base for market-specific figures)
- Closing costs: 1–2% of loan for origination, plus $15K–$25K for third-party costs; total 2–4% of loan amount

**If NOI projections are unavailable for future years**: Use Year 1 NOI with 2–3% annual growth. Flag as assumption and note that actual returns depend on lease-up performance.

**If exit cap rate is not provided**: Use the acquisition cap rate plus 25–50bps as a conservative exit assumption. Note this explicitly in the output.

**If stress test / scenario data is unavailable**: Describe covenant risk qualitatively based on Year 1 DSCR headroom above the covenant minimum. Flag that quantitative breach probability is not available.

**For all data gaps**:
1. Note the specific field and what is missing
2. Use the conservative estimate listed above or the Multifamily Benchmarks knowledge base
3. Flag the assumption in uncertainty_flags with confidence level LOW
4. Reduce the overall confidence score for the analysis
5. Continue — do not halt analysis due to a single data gap

---

## Confidence Scoring

Assign an overall confidence level to the term sheet and financing recommendation output:

| Level | Criteria |
|-------|----------|
| **HIGH** | All input data available and verified; no assumptions required; all calculations cross-checked |
| **MEDIUM** | Minor data gaps filled with reasonable estimates; 1-2 assumptions made; calculations verified |
| **LOW** | Significant data gaps; multiple assumptions required; limited cross-verification possible |

### Output Format
```json
{
  "confidence_level": "HIGH | MEDIUM | LOW",
  "confidence_score": 0.0-1.0,
  "factors": [
    { "factor": "{description}", "impact": "positive | negative", "weight": 0.0-1.0 }
  ],
  "uncertainty_flags": [
    { "field": "{name}", "reason": "{why}", "confidence": "HIGH | MEDIUM | LOW" }
  ]
}
```

Every estimated, assumed, or unverified value must have a corresponding entry in `uncertainty_flags`. These flags flow into legal review to highlight terms requiring additional scrutiny.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Underwriting Calculations](knowledge/underwriting-calc.md) — formulas for IRR, equity multiple, DSCR, debt service, and exit value calculations used throughout Step 3
- [Lender Criteria](knowledge/lender-criteria.md) — qualification standards and typical reserve and guarantor requirements by lender category, useful for filling gaps when lender has not specified all terms
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — market benchmarks for CapEx reserves, closing cost ranges, and typical covenant levels, used when lender-specific data is missing
- [Legal Checklist](knowledge/legal-checklist.md) — conditions precedent and document requirements that the legal review phase will need once the term sheet is finalized

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
