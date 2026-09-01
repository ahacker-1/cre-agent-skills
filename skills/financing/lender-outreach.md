---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Lender Outreach

Research and evaluate potential lenders across all categories (Agency, CMBS, Bank, Bridge), qualify a deal for each type, and produce a ranked lender package with indicative terms and requirements.

---

## When to Use This Skill

Use this skill when you have a CRE acquisition under contract or in active diligence and need to identify and compare financing sources. It is the right starting point any time you are moving from underwriting into the financing phase and need to understand which lender categories the deal qualifies for, which specific lenders to approach, and what terms to expect.

---

## What You'll Need to Provide

- **Property details**: address, property type, unit count, construction type, condition
- **Purchase price** and target LTV
- **Current financials**: NOI, effective gross income, operating expenses
- **Current occupancy** percentage
- **Value-add component**: whether there is a renovation budget, and if so, the amount and scope
- **Financial model outputs** (if available): DSCR, cap rate, projected returns
- **Sponsor information**: recourse tolerance, geographic market, hold period
- **Market**: city and state where the property is located

---

## Mission

Research and evaluate potential lenders across all categories (Agency, CMBS, Bank, Bridge). Qualify the deal for each lender type, identify specific lender sources, research current terms, and produce a ranked lender package with indicative terms and requirements.

---

## Strategy

### Step 1: Load Lender Criteria

Use the Lender Criteria knowledge base and the table below to understand qualification requirements for each lender category:

| Category | Key Criteria |
|----------|-------------|
| **Agency (Fannie/Freddie)** | Stabilized property, >90% occupancy, 5+ units, standard construction, no major deferred maintenance |
| **CMBS** | Minimum debt yield (typically 8-10%), loan size $2M+, stabilized or near-stabilized, diverse tenant base |
| **Bank/Credit Union** | Relationship opportunity, local/regional market presence, lower leverage tolerance, recourse acceptable |
| **Bridge/Debt Fund** | Value-add play, renovation component, transitional asset, higher leverage available, shorter term |

### Step 2: Qualify Deal for Each Category

Using the property details, financial model, and deal parameters provided:

```
FOR each lender_category:
  Check all qualification criteria against deal metrics:

  Agency Qualification:
    - Property type = multifamily? YES/NO
    - Occupancy > 90%? YES/NO
    - Unit count >= 5? YES/NO
    - Standard construction? YES/NO
    - Deferred maintenance < $X/unit? YES/NO
    - NOI supports 1.25x DSCR at agency terms? YES/NO
    → QUALIFIED / DISQUALIFIED (with reasons)

  CMBS Qualification:
    - Debt yield > 8%? YES/NO
    - Loan amount > $2M? YES/NO
    - Stabilized or near-stabilized? YES/NO
    - Single-asset or portfolio eligible? YES/NO
    → QUALIFIED / DISQUALIFIED (with reasons)

  Bank Qualification:
    - Loan size in bank range ($500K-$10M typical)? YES/NO
    - Sponsor recourse acceptable? YES/NO
    - Local market with bank presence? YES/NO
    → QUALIFIED / DISQUALIFIED (with reasons)

  Bridge Qualification:
    - Value-add component? YES/NO
    - Renovation budget defined? YES/NO
    - Clear stabilization path? YES/NO
    - Exit to permanent financing feasible? YES/NO
    → QUALIFIED / DISQUALIFIED (with reasons)
```

### Step 3: Identify Specific Lender Sources

For each qualified category, identify 2-3 specific lender sources using current market research:

```
FOR each qualified_category:
  Research: "best {category} multifamily lenders {year} {market}"
  Research: "{category} multifamily loan rates current"

  Select top 2-3 lenders based on:
    - Market presence in deal's geography
    - Loan size fit
    - Program availability
    - Reputation and execution certainty
```

Target lender sources by category:

| Category | Example Sources |
|----------|----------------|
| Agency | Fannie Mae DUS lenders (Walker & Dunlop, Berkadia, CBRE), Freddie Mac Optigo lenders |
| CMBS | Goldman Sachs, JP Morgan, Deutsche Bank, Ladder Capital |
| Bank | Local/regional banks with CRE lending desks, credit unions |
| Bridge | Arbor Realty, Ready Capital, Mesa West, Benefit Street Partners |

### Step 4: Research Each Lender Source

For each identified lender (up to 12 total across all qualified categories), research and report the following:

1. Current rate benchmarks for this property type and size
   - Fixed rate options (5, 7, 10 year)
   - Floating rate options (if available)
2. Maximum LTV offered
3. Minimum DSCR requirement
4. Debt yield minimum (if applicable)
5. Origination fees and closing costs
6. Typical closing timeline
7. Prepayment terms (yield maintenance, defeasance, step-down, open)
8. Interest-only period availability
9. Special programs (green financing, affordable housing, small balance)
10. Recourse requirements
11. Reserve requirements (tax, insurance, CapEx, replacement)
12. Any unique advantages or drawbacks

Use current market data from lender websites, broker rate sheets, and industry sources. Note the date of all rate information.

### Step 5: Preliminary Ranking

Score each lender option on key criteria:

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| All-in Rate | 30% | Lower = better, scale 1-10 |
| Leverage (LTV) | 20% | Higher = better for equity returns |
| Execution Certainty | 15% | Track record, timeline predictability |
| Flexibility | 15% | Prepayment, IO period, assumability |
| Timeline | 10% | Faster closing = better |
| Fees | 10% | Lower total costs = better |

```
FOR each lender:
  weighted_score = sum(criterion_score x weight)

Rank by weighted_score descending
```

---

## Output Format

Produce a lender package report with the following sections:

```markdown
# Lender Package: {Property Name}
## Date: {date}
## Qualified Categories: {list}
## Lenders Researched: {count}

### Deal Qualification Summary

| Category | Qualified | Key Reason |
|----------|-----------|------------|
| Agency | YES/NO | {reason} |
| CMBS | YES/NO | {reason} |
| Bank | YES/NO | {reason} |
| Bridge | YES/NO | {reason} |

### Qualified Lender Options

#### {Lender 1 Name} ({Category})
- **Rate**: {rate range}
- **LTV**: up to {X}%
- **DSCR Minimum**: {X.Xx}
- **Term Options**: {5/7/10 year}
- **Amortization**: {X years}
- **IO Period**: {X years available}
- **Fees**: {origination + other}
- **Prepayment**: {terms}
- **Timeline**: {weeks to close}
- **Recourse**: {full/partial/non-recourse}
- **Special Programs**: {if applicable}
- **Score**: {weighted score}/10
- **Pros**: {key advantages}
- **Cons**: {key drawbacks}

[Repeat for each qualified lender]

### Preliminary Ranking

| Rank | Lender | Category | Rate | LTV | Score | Key Advantage |
|------|--------|----------|------|-----|-------|---------------|
| 1 | {name} | {cat} | X% | X% | X.X | {advantage} |
| 2 | {name} | {cat} | X% | X% | X.X | {advantage} |
| ... | ... | ... | ... | ... | ... | ... |

### Disqualified Lenders

| Category | Reason for Disqualification |
|----------|----------------------------|
| {category} | {specific reason} |

### Lender Package Requirements Checklist

Items needed to submit loan packages:
- [ ] Executive summary / deal narrative
- [ ] Trailing 12-month P&L
- [ ] Current rent roll
- [ ] 5-year pro forma
- [ ] Property photos
- [ ] Market overview
- [ ] Sponsor financial statement
- [ ] Sponsor track record / deal history
- [ ] Purchase contract
- [ ] Title report
- [ ] Environmental report (Phase I)
- [ ] Physical inspection report
- [ ] Insurance quote
- [ ] {Category-specific items}

### Next Steps
1. {Recommended actions to advance financing}
```

---

## Quality Checks

Before finalizing the lender package, verify:

**Schema and Completeness**
- All 4 lender categories evaluated (even if disqualified) — evaluate missing categories before output
- Every qualified lender has rate, LTV, DSCR, fees, and timeline populated — flag any gaps
- Package requirements checklist covers all relevant lender types

**Numeric Sanity**
- Interest rates: 2%–15% range — flag anything outside this range
- LTV offered: 0%–90% — flag anything above 90%
- Loan term: 1–40 years — flag outliers
- Origination fee: 0%–5% — flag anything above 5%

**Logical Checks**
- Minimum 3 qualified lender options identified — expand search if fewer
- Rates fall within current market range (verify against recent market data)
- Top-ranked lender has the highest weighted score — verify scoring math
- Top options match the deal's strategy (value-add vs. stabilized) — re-rank if misaligned

**Confidence and Uncertainty**
- All estimated or assumed values noted in uncertainty_flags
- Overall confidence level (HIGH/MEDIUM/LOW) assigned before delivery

---

## Red Flags & Dealbreakers

Monitor for these conditions during analysis:

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Uninsurable property condition | Research or lender feedback indicates the property cannot obtain required insurance coverage |

If a dealbreaker is detected:
1. Set severity to CRITICAL
2. Add to red flags with category "dealbreaker"
3. Note prominently in the output but continue analysis to completion

---

## When Data is Missing

**If financial model data is unavailable**: Use the property details provided directly. Calculate NOI from income and expense data. Note any estimates made and reduce confidence accordingly.

**If market rent data is unavailable**: Research current market rents for comparable properties in the subject market. Use conservative estimates and flag as assumptions.

**If occupancy history is incomplete**: Use the current occupancy as a point-in-time data point. Note the limitation and use conservative underwriting assumptions for lender qualification.

**For all data gaps**:
1. Note the specific field and what is missing
2. Attempt to estimate using industry benchmarks from the Multifamily Benchmarks knowledge base or Underwriting Calculations knowledge base
3. Use conservative estimates that bias toward lower returns (not higher)
4. Flag the assumption in the output with confidence level LOW
5. Reduce the overall confidence score for the analysis
6. Continue — do not halt analysis due to a single data gap

---

## Confidence Scoring

Assign an overall confidence level to the lender package output:

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

Every estimated, assumed, or unverified value must have a corresponding entry in `uncertainty_flags`. These flags are especially important when this analysis feeds into quote comparison or term sheet assembly.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- [Lender Criteria](knowledge/lender-criteria.md) — detailed qualification rules, current program parameters, and lender-specific underwriting standards by category
- [Underwriting Calculations](knowledge/underwriting-calc.md) — formulas for DSCR, debt yield, and return calculations used in lender qualification
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — market benchmarks for rates, leverage, and terms to validate lender quotes against market norms

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
