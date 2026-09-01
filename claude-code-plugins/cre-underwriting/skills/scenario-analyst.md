---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Scenario Analyst

Run 27 scenario permutations on a base case financial model to stress-test returns, identify probability-weighted outcomes, and rank variable sensitivities for a multifamily CRE acquisition.

---

## When to Use This Skill

Use this skill after a base case financial model has been built. It systematically varies rent growth, expense growth, and exit cap rate across three states each — producing 27 full scenario permutations — so you can understand the full return distribution, identify downside risk, and quantify how sensitive the deal is to each key assumption. The output feeds directly into the Investment Committee memo's scenario and sensitivity sections.

---

## What You'll Need to Provide

- **Base case financial model**: The complete 5-year pro forma with Year 1–5 NOI, CapEx schedule, and debt service (output from the Financial Model Builder skill, or equivalent data)
- **Deal terms**: Purchase price, total equity invested, loan amount, interest rate, loan term, amortization period, interest-only period (if any), hold period
- **Base case assumptions**: The rent growth rate, expense growth rate, and exit cap rate used in the base case model
- **Investment thresholds** (optional): Minimum DSCR, IRR, equity multiple, and cash-on-cash targets; if not provided, standard defaults are applied
- **Property name** for output labeling

---

## Mission

Run 27 scenario permutations on the base case financial model across three key variables (rent growth, expense growth, exit cap rate). Identify best/worst cases, calculate probability-weighted returns, perform stress tests, and determine which variables have the greatest impact on deal returns.

---

## Strategy

### Step 1: Define Scenario Matrix

Three variables, three states each:

| Variable | Downside | Base | Upside |
|----------|----------|------|--------|
| **Rent Growth** | -2% per year | +3% per year | +5% per year |
| **Expense Growth** | +5% per year | +3% per year | +2% per year |
| **Exit Cap Rate** | +50bps above base | Flat (base assumption) | -25bps below base |

Total permutations: 3 x 3 x 3 = **27 scenarios**

Scenario naming convention:
```
S-{rent_state}-{expense_state}-{exit_state}
Example: S-DOWN-BASE-UP = Downside rent, Base expense, Upside exit cap
States: DOWN, BASE, UP
```

Note: If the user provides different variable states or ranges (e.g., a market-specific rent growth forecast), use those values instead of the defaults above. Document any substitutions clearly.

### Step 2: Generate All 27 Permutations

```
scenarios = []
FOR rent_state IN [DOWN, BASE, UP]:
  FOR expense_state IN [DOWN, BASE, UP]:
    FOR exit_state IN [DOWN, BASE, UP]:
      scenario = {
        id: "S-{rent_state}-{expense_state}-{exit_state}",
        rent_growth: rent_values[rent_state],
        expense_growth: expense_values[expense_state],
        exit_cap: exit_values[exit_state]
      }
      scenarios.append(scenario)
```

### Step 3: Calculate All 27 Scenarios

For each scenario, recalculate using the base case pro forma as the starting point:

1. **Years 1–5 NOI** — apply scenario rent growth and expense growth rates instead of base case rates
2. **Exit value** — Year 5 NOI / scenario exit cap rate
3. **IRR (5-year)** — with scenario-specific cash flows and exit proceeds
4. **Equity Multiple** — (total cash flow over hold + net sale proceeds) / total equity
5. **Cash-on-Cash** — (NOI - debt service) / equity, for each year
6. **DSCR** — NOI / annual debt service, for each year
7. **Total cash flow** over hold period

Process all 27 scenarios systematically. If working computationally, process in 3 batches of 9 for manageability.

### Step 4: Build Scenario Matrix Table

Organize all 27 results into a readable matrix:

| Scenario ID | Rent Growth | Expense Growth | Exit Cap | Year 1 NOI | Year 5 NOI | IRR | Equity Multiple | Avg CoC | Min DSCR |
|-------------|-------------|----------------|----------|------------|------------|-----|-----------------|---------|----------|
| S-DOWN-DOWN-DOWN | -2% | +5% | +50bps | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| S-UP-UP-UP | +5% | +2% | -25bps | ... | ... | ... | ... | ... | ... |

### Step 5: Identify Key Cases

```
best_case  = scenario with highest IRR
worst_case = scenario with lowest IRR
base_case  = S-BASE-BASE-BASE
median_case = scenario closest to median IRR across all 27

Label each clearly in the output.
```

### Step 6: Calculate Probability-Weighted Returns

Assign independent probabilities per variable state:

| State | Probability |
|-------|-------------|
| Downside | 25% |
| Base | 50% |
| Upside | 25% |

Joint probability per scenario = P(rent) x P(expense) x P(exit)

```
Example: S-BASE-BASE-BASE = 0.50 x 0.50 x 0.50 = 12.5%
Example: S-DOWN-DOWN-DOWN = 0.25 x 0.25 x 0.25 = 1.5625%

probability_weighted_irr = SUM(scenario_irr x scenario_probability) for all 27
probability_weighted_em  = SUM(scenario_em x scenario_probability) for all 27
probability_weighted_coc = SUM(scenario_avg_coc x scenario_probability) for all 27
```

Verify: all 27 scenario probabilities sum to 100%.

### Step 7: Stress Test

Identify scenarios where critical thresholds are breached:

```
stress_failures = []
FOR each scenario:
  IF min_dscr < 1.0x:
    stress_failures.append({scenario, "DSCR below 1.0x", min_dscr})
  IF any_year_coc < 0%:
    stress_failures.append({scenario, "Negative cash flow", year, coc})
  IF irr < 0%:
    stress_failures.append({scenario, "Negative IRR", irr})
  IF equity_multiple < 1.0x:
    stress_failures.append({scenario, "Loss of principal", em})

Count: X of 27 scenarios fail stress test
Probability: sum of failed scenario probabilities
```

### Step 8: Sensitivity Analysis

Determine which variable has the most impact on returns:

```
FOR each variable (rent, expense, exit_cap):
  Hold other two at BASE
  Calculate IRR spread: IRR(UP) - IRR(DOWN)
  This isolates the impact of each variable

Rank variables by IRR spread (largest = most sensitive)

Also calculate:
  - Rent swing:     hold expense=BASE, exit=BASE → vary rent (3 scenarios)
  - Expense swing:  hold rent=BASE,    exit=BASE → vary expense (3 scenarios)
  - Exit cap swing: hold rent=BASE,    expense=BASE → vary exit (3 scenarios)
```

---

## Output Format

### Required Sections

```markdown
# Scenario Analysis: {Property Name}
## Generated: {date}
## Scenarios Run: 27
## Overall Assessment: {STRONG | ACCEPTABLE | MARGINAL | WEAK}

### Scenario Matrix (27 Permutations)

| # | Scenario ID | Rent | Expense | Exit Cap | Yr1 NOI | Yr5 NOI | IRR | EM | Avg CoC | Min DSCR | Prob |
|---|------------|------|---------|----------|---------|---------|-----|----|---------|----------|------|
| 1 | S-DOWN-DOWN-DOWN | -2% | +5% | +50bps | $X | $X | X% | X.Xx | X% | X.Xx | X% |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 27 | S-UP-UP-UP | +5% | +2% | -25bps | $X | $X | X% | X.Xx | X% | X.Xx | X% |

### Key Case Summary

| Case | Scenario | IRR | EM | CoC | DSCR |
|------|----------|-----|----|-----|------|
| Best Case | S-UP-UP-UP | X% | X.Xx | X% | X.Xx |
| Base Case | S-BASE-BASE-BASE | X% | X.Xx | X% | X.Xx |
| Median Case | S-XXX-XXX-XXX | X% | X.Xx | X% | X.Xx |
| Worst Case | S-DOWN-DOWN-DOWN | X% | X.Xx | X% | X.Xx |

### Probability-Weighted Returns

| Metric | Value |
|--------|-------|
| Probability-Weighted IRR | X% |
| Probability-Weighted Equity Multiple | X.Xx |
| Probability-Weighted Avg Cash-on-Cash | X% |

### Stress Test Results

- Scenarios failing stress test: X of 27
- Probability of stress failure: X%
- Failures:
  | Scenario | Failure Type | Value | Threshold |
  |----------|-------------|-------|-----------:|
  | S-XXX-XXX-XXX | DSCR < 1.0x | X.Xx | 1.0x |
  | ... | ... | ... | ... |

### Sensitivity Analysis

| Variable | IRR (Downside) | IRR (Base) | IRR (Upside) | Spread | Rank |
|----------|---------------|------------|--------------|--------|------|
| Rent Growth | X% | X% | X% | X% | 1 |
| Exit Cap Rate | X% | X% | X% | X% | 2 |
| Expense Growth | X% | X% | X% | X% | 3 |

Most sensitive variable: {variable} ({spread}% IRR spread)

### Scenario Verdict

{Assessment explanation}
- X of 27 scenarios exceed all thresholds
- Probability-weighted returns {meet/do not meet} investment criteria
- Downside is {protected/exposed}: worst case IRR = X%, worst case DSCR = X.Xx
- Key risk driver: {most sensitive variable}
```

---

## Quality Checks

Before finalizing results, run all of the following checks:

**Completeness**
- Exactly 27 scenarios in results (flag if any are missing; re-run missing scenarios)
- All metrics calculated for all scenarios (IRR, equity multiple, cash-on-cash per year, DSCR per year)
- All 27 scenario probabilities sum to 100% (recalculate if not)

**Numeric Sanity**

| Field | Valid Range | Flag If |
|-------|-----------|---------:|
| totalScenarios | 27 (3×3×3 matrix) | Not exactly 27 |
| scenariosPassingAll | 0 – 27 | Outside range |
| Each scenario IRR | -0.20 – 1.00 | Outside range |
| Each scenario DSCR | 0.5 – 5.0 | Outside range |

**Logical Consistency**
- S-BASE-BASE-BASE must match the base case financial model output — flag any discrepancy
- Upside scenario metrics must be better than base; downside must be worse (flag inversions)
- Sensitivity analysis: upside > base > downside for each variable individually (flag inversions)
- Monotonicity check: better assumptions should consistently yield better returns

**Threshold Cross-Check** (use user-provided thresholds or apply these standard defaults):

| Metric | Pass | Fail |
|--------|------|------|
| Scenarios passing all criteria | >= 18 of 27 | < 18 of 27 |
| Stress case DSCR | >= 1.25x | < 1.25x |
| Stress case vacancy | <= 15% | > 15% |
| Stress case expense ratio | <= 55% of EGI | > 55% of EGI |

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **HIGH** | Base case model fully verified; all 27 scenarios calculated without gaps |
| **MEDIUM** | Minor base case data gaps; 1-2 scenario assumptions substituted |
| **LOW** | Significant base case gaps; multiple scenario assumptions required |

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

---

## Red Flags & Dealbreakers

| Dealbreaker | Detection Criteria | Threshold |
|------------|-------------------|-----------|
| DSCR critically low in worst case | Worst case scenario DSCR falls below 0.80 and the deal does not include a value-add component | Worst case DSCR < 0.80 |

When a dealbreaker is detected: note it prominently with CRITICAL severity in the output. Continue the full analysis so the IC memo has complete data.

**Overall assessment ratings:**

| Rating | Criteria |
|--------|----------|
| **STRONG** | >= 22 of 27 scenarios pass all thresholds; probability-weighted IRR >= 15%; worst case does not breach DSCR 1.0x |
| **ACCEPTABLE** | >= 18 of 27 scenarios pass; probability-weighted IRR >= 12%; downside scenarios show adequate coverage |
| **MARGINAL** | 12–17 of 27 scenarios pass; probability-weighted returns near threshold; meaningful stress exposure |
| **WEAK** | < 12 of 27 scenarios pass; probability of stress failure > 25%; downside shows loss of principal or negative cash flow |

---

## When Data is Missing

When required data is unavailable:

1. **Note the gap explicitly** — state which scenario inputs or base case data are missing
2. **Attempt a workaround** — use alternate calculation methods from the Underwriting Calculations knowledge base, or use conservative estimates from the Multifamily Benchmarks knowledge base; for scenario analysis, bias estimates toward lower returns
3. **State the assumption clearly** — document what substitute value was used
4. **Mark every estimated value** — add to `uncertainty_flags` with reason and confidence level
5. **Continue the analysis** — use conservative assumptions, reduce confidence score, and flag all gaps

Common fallbacks:
- If base case model is partially complete: use available NOI data and note which years are estimated
- If financing terms are incomplete: use standard market terms (e.g., 65% LTV, 6.5% rate, 30-year amort) and flag as assumed
- If hold period is not specified: default to 5 years

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:

- [Underwriting Calculations](knowledge/underwriting-calc.md) — IRR, equity multiple, and all return metric formulas used across the 27 scenarios
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — market norms for vacancy, expense ratios, and rent growth that inform scenario variable selection
- [Financial Model Builder](skills/underwriting/financial-model-builder.md) — produces the base case model that this skill stress-tests
- [IC Memo Writer](skills/underwriting/ic-memo-writer.md) — consumes this skill's scenario output for the investment committee memorandum

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
