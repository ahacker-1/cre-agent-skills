---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Quote Comparator

Normalize and compare multiple lender quotes on a common basis, build a weighted scoring matrix, and identify the top 3 financing options with risk assessments for each.

---

## When to Use This Skill

Use this skill after you have collected indicative quotes or term indications from multiple lenders and need to evaluate them side-by-side on a true apples-to-apples basis. It is the right tool any time you have 2 or more lender quotes with different rate structures, fees, leverage levels, and prepayment terms, and need to determine which option is actually cheapest, most flexible, or best suited to your deal strategy.

---

## What You'll Need to Provide

- **Lender quotes**: rate (fixed or floating with index + spread), LTV, term, amortization, IO period, origination fees, prepayment structure, closing timeline, recourse terms, and reserve requirements for each lender
- **NOI projections**: at minimum Year 1 NOI; ideally a 5-year pro forma
- **Purchase price** and equity structure (down payment, closing costs, reserves)
- **Target hold period** (typically 5 years) — used for total cost of capital calculation
- **Deal strategy context**: stabilized vs. value-add, exit via sale vs. refinance
- **Financial model outputs** (if available): base case IRR, equity multiple, cash-on-cash — used to calculate financing impact on returns

---

## Mission

Normalize and compare all lender quotes on a common basis. Build a weighted comparison matrix that scores each option across rate, leverage, flexibility, execution certainty, prepayment terms, and timeline. Identify the top 3 financing options with risk assessments for each.

---

## Strategy

### Step 1: Normalize All Quotes to Common Basis

Every lender quotes differently. Normalize all quotes to enable apples-to-apples comparison:

#### 1a. All-In Rate
```
For each lender:
  IF fixed rate:
    all_in_rate = stated_rate
  IF floating rate:
    all_in_rate = index_rate + spread
    (Use current index: SOFR, T-bill, etc.)

  Normalize to: annual percentage rate (APR equivalent)
```

#### 1b. Effective Rate (Including Fees)
```
For each lender:
  total_upfront_fees = origination + legal + appraisal + other
  fee_amortized_annual = total_upfront_fees / expected_hold_years
  effective_annual_cost = (annual_interest + fee_amortized_annual) / loan_amount

  This gives the true cost of capital over the hold period
```

#### 1c. Total Cost of Capital Over Hold Period
```
For each lender:
  total_interest = sum of interest payments over hold period
  total_fees = all upfront and ongoing fees
  prepayment_cost = estimated prepayment penalty at exit year
  total_cost = total_interest + total_fees + prepayment_cost
```

#### 1d. Monthly and Annual Debt Service
```
For each lender:
  loan_amount = purchase_price x lender_ltv

  IF amortizing:
    monthly_payment = loan_amount x [r(1+r)^n] / [(1+r)^n - 1]
    where r = monthly rate, n = amortization months

  IF IO period:
    monthly_payment_io = loan_amount x annual_rate / 12
    monthly_payment_amort = (calculated above for amort period)

  annual_debt_service = monthly_payment x 12 (for each year)
```

#### 1e. DSCR at Quoted Terms
```
For each lender:
  dscr_year1 = year_1_noi / annual_debt_service_year1
  dscr_by_year = [noi_yearN / debt_service_yearN for N in 1..5]
```

#### 1f. Cash-on-Cash at Quoted Terms
```
For each lender:
  equity_required = purchase_price - loan_amount + closing_costs + reserves
  coc_year1 = (year_1_noi - debt_service_year1) / equity_required
  coc_by_year = [(noi_yearN - ds_yearN) / equity_required for N in 1..5]
```

### Step 2: Build Comparison Matrix

Construct a comprehensive comparison table with all lenders as rows and normalized metrics as columns:

```
Rows = Lenders (all quoted options)
Columns = Normalized metrics:
  - Lender Name
  - Category (Agency/CMBS/Bank/Bridge)
  - Loan Amount
  - LTV
  - All-In Rate
  - Effective Rate (with fees)
  - IO Period
  - Term / Amortization
  - Annual Debt Service (Year 1)
  - Year 1 DSCR
  - Year 1 Cash-on-Cash
  - Total Cost of Capital (hold period)
  - Prepayment Terms
  - Estimated Prepayment Cost at Exit
  - Closing Timeline (weeks)
  - Recourse
  - Reserves Required
```

### Step 3: Score Each Option

Apply weighted scoring methodology:

| Criterion | Weight | Scoring Method |
|-----------|--------|----------------|
| **Rate** | 30% | Lowest effective rate = 10, scale linearly to highest = 1 |
| **Leverage** | 20% | Highest LTV = 10, scale linearly to lowest = 1 |
| **Flexibility** | 15% | Score 1-10 based on: IO period, assumability, supplemental loan option, rate lock flexibility |
| **Execution Certainty** | 15% | Score 1-10 based on: lender track record, program stability, underwriting predictability |
| **Prepayment Terms** | 10% | Open/step-down = 10, defeasance = 5, yield maintenance = 3, lockout = 1 |
| **Timeline** | 10% | Fastest closing = 10, scale linearly to slowest = 1 |

```
FOR each lender:
  rate_score = normalize(effective_rate, min_rate, max_rate, inverse=true) x 10
  leverage_score = normalize(ltv, min_ltv, max_ltv) x 10
  flexibility_score = assess_flexibility(io_period, assumability, supplemental, rate_lock)
  execution_score = assess_execution(lender_category, track_record)
  prepayment_score = score_prepayment(prepayment_type)
  timeline_score = normalize(weeks_to_close, min_weeks, max_weeks, inverse=true) x 10

  weighted_total = (
    rate_score x 0.30 +
    leverage_score x 0.20 +
    flexibility_score x 0.15 +
    execution_score x 0.15 +
    prepayment_score x 0.10 +
    timeline_score x 0.10
  )
```

### Step 4: Identify Top 3 Options

```
ranked_lenders = sort(lenders, by=weighted_total, descending=true)
top_3 = ranked_lenders[0:3]

For each top option, provide:
  - Why it ranks highly
  - Best suited for which deal strategy
  - Key advantages over alternatives
  - Key trade-offs to consider
```

### Step 5: Risk Assessment Per Option

For each lender option (focus on top 3, assess all):

```
Execution Risk:
  - How likely is this lender to close as quoted?
  - History of retrading or last-minute changes?
  - Underwriting stringency vs initial indication?
  Score: Low / Medium / High

Rate Lock Risk:
  - Is rate locked at application, commitment, or closing?
  - Float-down provision available?
  - Duration of rate lock?
  Score: Low / Medium / High

Retrading Risk:
  - How likely to change terms after application?
  - Does this lender have reputation for retrading?
  - Appraisal risk (will their appraiser hit value)?
  Score: Low / Medium / High

Structural Risk:
  - Recourse exposure
  - Reserve requirements impact on cash flow
  - Covenant breach probability (from stress test data if available)
  Score: Low / Medium / High
```

---

## Output Format

Produce a quote comparison report with the following sections:

```markdown
# Quote Comparison: {Property Name}
## Date: {date}
## Quotes Compared: {count}
## Recommended Option: {lender name} ({category})

### Normalized Comparison Matrix

| Metric | {Lender 1} | {Lender 2} | {Lender 3} | ... |
|--------|-----------|-----------|-----------|-----|
| Category | Agency | CMBS | Bank | ... |
| Loan Amount | $X | $X | $X | ... |
| LTV | X% | X% | X% | ... |
| All-In Rate | X% | X% | X% | ... |
| Effective Rate (w/ fees) | X% | X% | X% | ... |
| IO Period | X yrs | X yrs | X yrs | ... |
| Term / Amort | X/Xx | X/Xx | X/Xx | ... |
| Year 1 Debt Service | $X | $X | $X | ... |
| Year 1 DSCR | X.Xx | X.Xx | X.Xx | ... |
| Year 1 Cash-on-Cash | X% | X% | X% | ... |
| Total Cost of Capital | $X | $X | $X | ... |
| Prepayment | {type} | {type} | {type} | ... |
| Est. Prepay Cost at Exit | $X | $X | $X | ... |
| Timeline | X wks | X wks | X wks | ... |
| Recourse | {type} | {type} | {type} | ... |

### Scoring Methodology

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Rate | 30% | Effective rate including amortized fees |
| Leverage | 20% | LTV offered |
| Flexibility | 15% | IO period, assumability, supplemental, rate lock |
| Execution Certainty | 15% | Lender track record, program stability |
| Prepayment Terms | 10% | Flexibility to exit or refinance |
| Timeline | 10% | Speed to close |

### Scoring Results

| Lender | Rate | Leverage | Flex | Execution | Prepay | Timeline | Total | Rank |
|--------|------|----------|------|-----------|--------|----------|-------|------|
| {L1} | X.X | X.X | X.X | X.X | X.X | X.X | X.X | 1 |
| {L2} | X.X | X.X | X.X | X.X | X.X | X.X | X.X | 2 |
| {L3} | X.X | X.X | X.X | X.X | X.X | X.X | X.X | 3 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Top 3 Recommendations

#### #1: {Lender Name} ({Category}) - Score: X.X/10
- **Why**: {rationale}
- **Best for**: {deal strategy alignment}
- **Key advantage**: {primary differentiator}
- **Key trade-off**: {main drawback}

#### #2: {Lender Name} ({Category}) - Score: X.X/10
[same structure]

#### #3: {Lender Name} ({Category}) - Score: X.X/10
[same structure]

### Risk Analysis

| Lender | Execution Risk | Rate Lock Risk | Retrade Risk | Structural Risk | Overall |
|--------|---------------|----------------|--------------|-----------------|---------|
| {L1} | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High |
| {L2} | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High |
| {L3} | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High | Low/Med/High |

### Total Cost of Capital Comparison

| Lender | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|--------|--------|--------|--------|--------|--------|-------|
| {L1} | $X | $X | $X | $X | $X | $X |
| {L2} | $X | $X | $X | $X | $X | $X |
| {L3} | $X | $X | $X | $X | $X | $X |

### Impact on Deal Returns

| Metric | {Top Lender} | Base Case Model | Delta |
|--------|-------------|-----------------|-------|
| Cash-on-Cash (Yr 1) | X% | X% | +/-X% |
| IRR (5-Year) | X% | X% | +/-X% |
| Equity Multiple | X.Xx | X.Xx | +/-X.Xx |
| DSCR (Yr 1) | X.Xx | X.Xx | +/-X.Xx |

### Recommendation
{Summary of why the top option is recommended, including risk/return trade-off analysis}
```

---

## Quality Checks

Before finalizing the comparison report, verify:

**Schema and Completeness**
- All lender quotes from the provided package are included — flag any missing quotes
- Every quote in the comparison matrix has the same set of columns — flag any missing data points
- No duplicate ranks in the scoring results

**Numeric Sanity**
- Effective rate >= all-in rate for every lender (fees add cost, never subtract) — recalculate if not true
- Higher leverage options generally show lower DSCR — flag inversions for review
- Weighted scores sum correctly per lender

**Threshold Cross-Check**

Compare the best quote against these thresholds and flag any breach with severity HIGH:

| Output Metric | Threshold | Pass | Fail |
|--------------|-----------|------|------|
| Best quote LTV | Max 75% | <= 75% | > 75% |
| Best quote DSCR | Min 1.25x | >= 1.25 | < 1.25 |
| Best quote interest rate | Max 8% | <= 8% | > 8% |
| Best quote origination fee | Max 2% | <= 2% | > 2% |
| Best quote loan term | Min 5 years | >= 5 | < 5 |
| Total quotes compared | Min 3 | >= 3 | < 3 |

**Logic Checks**
- #1 ranked lender has the highest weighted score — fix ranking if not
- Higher leverage options have higher structural risk in the risk table — flag mismatches
- Total cost of capital includes interest + fees + prepayment — add missing components if any
- Top option explains its impact on deal returns — calculate if missing

**Confidence and Uncertainty**
- All estimated or assumed values noted in uncertainty_flags
- Overall confidence level (HIGH/MEDIUM/LOW) assigned before delivery

---

## When Data is Missing

**If a lender quote is incomplete** (missing rate, LTV, fees, or timeline): Flag the specific gaps prominently. Do not exclude the lender — include them in the matrix with gaps noted. Score only on available criteria and reduce the weight of missing criteria proportionally.

**If NOI projections are unavailable for future years**: Use Year 1 NOI with an assumed annual growth rate of 2-3% (note the assumption). Calculate DSCR and CoC for Year 1 only, and note that multi-year projections are estimated.

**If the financial model base case is unavailable**: Omit the "Impact on Deal Returns" section or calculate it from scratch using the provided purchase price, NOI, and equity structure.

**If a lender's prepayment type is unspecified**: Default to yield maintenance in the scoring (score = 3) and note the assumption. Request clarification before submitting a loan application.

**For all data gaps**:
1. Note the specific field and what is missing
2. Use conservative estimates that bias toward higher cost, not lower
3. Flag the assumption in uncertainty_flags with confidence level LOW
4. Reduce the overall confidence score for the analysis
5. Continue — do not halt analysis due to a single data gap

---

## Confidence Scoring

Assign an overall confidence level to the comparison output:

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

Every estimated, assumed, or unverified value must have a corresponding entry in `uncertainty_flags`. These flags are especially important when this comparison feeds into term sheet assembly.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Underwriting Calculations](knowledge/underwriting-calc.md) — formulas for DSCR, cash-on-cash, IRR, equity multiple, and debt service calculations used throughout the normalization and scoring steps
- [Lender Criteria](knowledge/lender-criteria.md) — qualification standards by lender category, useful for contextualizing why certain lenders offer better terms for specific deal profiles
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — market benchmarks for rates, leverage, and prepayment terms to sanity-check quoted terms against current market conditions

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
