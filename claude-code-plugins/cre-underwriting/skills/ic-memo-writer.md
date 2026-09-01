---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# IC Memo Writer

Compile a professional Investment Committee memorandum that synthesizes all due diligence and underwriting analysis into a single definitive document with a clear investment recommendation.

---

## When to Use This Skill

Use this skill when you have completed due diligence and financial underwriting on a multifamily CRE acquisition and need to present findings to an Investment Committee. It takes all DD and underwriting outputs — rent roll analysis, OpEx analysis, physical inspection, market study, title review, tenant analysis, environmental review, base case financial model, and scenario analysis — and weaves them into a professional memo thorough enough for IC members to make an informed PASS/FAIL decision without reading the underlying reports.

---

## What You'll Need to Provide

- **Base case financial model**: Pro forma tables, returns summary, model assumptions, and base case verdict (output from the Financial Model Builder skill, or equivalent data)
- **Scenario analysis**: The 27-scenario matrix, key case summary (best/worst/base/median), probability-weighted returns, stress test results, and sensitivity ranking (output from the Scenario Analyst skill, or equivalent data)
- **Rent roll findings**: Key findings, risk flags, occupancy data, unit mix, loss-to-lease, and the DD verdict
- **OpEx analysis findings**: Adjusted expense line items, variance from seller's stated expenses, and any anomalies
- **Physical inspection findings**: Property condition summary, CapEx schedule, deferred maintenance items, major systems useful life
- **Market study findings**: Submarket overview, rent comps, supply/demand dynamics, vacancy trends, employment context
- **Tenant/lease analysis** (if available): Tenant profile, lease term distribution, rollover risk schedule
- **Title review findings**: Title status, encumbrances, zoning compliance, any pending legal matters
- **Environmental review findings** (if available): Phase I/II findings, any recognized environmental conditions
- **Deal terms**: Property name, address, unit count, purchase price, price per unit, financing structure, hold period, exit strategy
- **Investment thresholds**: Minimum return criteria being applied to this deal (or use standard defaults)
- **Overall risk tolerance / portfolio context** (optional): Helps frame the recommendation

---

## Mission

Compile the Investment Committee memorandum from all underwriting outputs and due diligence findings. The IC memo is the definitive document that synthesizes every analysis into a single, professional narrative with a clear investment recommendation. It must be thorough enough for IC members to make an informed PASS/FAIL decision without reading underlying reports.

---

## Strategy

### Step 1: Gather and Review All Inputs

Before writing, read every source provided and extract:
- Key findings (positive and negative)
- Risk flags (with severity)
- Quantitative data points needed for the memo
- DD/UW verdict for each analysis area (PASS / FAIL / CONDITIONAL)

Sources to extract from:
- Rent roll analysis
- OpEx analysis
- Physical inspection
- Title review
- Market study
- Tenant analysis (if available)
- Environmental review (if available)
- Base case financial model
- Scenario analysis

### Step 2: Apply Risk Scoring Methodology

Using the Risk Scoring Framework knowledge base (or consistent internal methodology):
- Score each risk factor identified across all DD and UW sources
- Aggregate into an overall risk profile
- Categorize risks: Low / Moderate / Elevated / High
- Identify mitigants for each key risk
- Categorize by type: Market, Physical, Financial, Legal, Environmental, Operational

### Step 3: Compile IC Memo Sections

Write each section following the document structure below:

#### Section: Executive Summary
- **Deal Thesis**: Why this property, what is the value creation opportunity
- **Key Investment Merits** (top 3–5 strengths):
  - Below-market rents with capture opportunity
  - Strong market fundamentals
  - Value-add potential
  - Favorable financing available
  - Defensible location/submarket
- **Key Risks** (top 3–5 risks):
  - Pulled from all DD analysis flags
  - Ranked by severity using the risk scoring methodology
- **Recommendation**: PASS / FAIL / CONDITIONAL (with conditions if applicable)
- **Key Metrics Snapshot**: Price, price/unit, cap rate, IRR, equity multiple

#### Section: Property Overview
- Physical description (from physical inspection)
- Unit mix and configuration (from rent roll analysis)
- Location and access (from market study)
- Current occupancy and rent levels (from rent roll)
- Property condition summary (from physical inspection)
- Age, construction type, amenities

#### Section: Market Analysis
- Submarket overview (from market study)
- Supply/demand dynamics
- Rent comps and positioning
- Vacancy trends
- Employment and population growth
- Competitive landscape
- Market rent growth projections

#### Section: Tenant & Lease Analysis
- Tenant profile summary (from tenant analysis)
- Lease term distribution
- Renewal probability assessment
- Rollover risk schedule
- Tenant quality indicators

#### Section: Physical Condition & CapEx
- Property condition assessment (from physical inspection)
- Deferred maintenance items
- CapEx budget summary (by year)
- Major systems remaining useful life
- Environmental findings (from environmental review)

#### Section: Title & Legal
- Title status (from title review)
- Encumbrances and exceptions
- Zoning compliance
- Any legal issues or pending matters

#### Section: Financial Analysis
- Year 1 income and expense summary (from financial model)
- 5-year pro forma summary table (from financial model)
- Returns analysis table (from financial model)
- Value creation bridge (current NOI to stabilized NOI)
- Comparison to acquisition basis

#### Section: Scenario & Sensitivity Analysis
- Key cases summary: best, base, worst, median (from scenario analysis)
- Probability-weighted returns (from scenario analysis)
- Stress test results (from scenario analysis)
- Sensitivity ranking by variable (from scenario analysis)
- Downside protection assessment

#### Section: Risk Assessment
- Aggregate all risks from all DD and UW analyses
- Categorize into: Market, Physical, Financial, Legal, Environmental, Operational
- Rate each risk: Low / Moderate / Elevated / High
- Identify mitigants for each key risk
- State overall risk rating: Low / Moderate / Elevated / High

#### Section: Investment Thesis
- Value creation plan (rent growth, expense reduction, CapEx ROI)
- Competitive advantages of this property
- Why now (market timing, seller motivation)
- Exit strategy and target buyer profile
- Alignment with portfolio strategy

#### Section: Recommendation
- Final verdict: PASS / FAIL / CONDITIONAL
- If CONDITIONAL: list specific conditions that must be met before proceeding
- If PASS: summarize why the deal meets investment criteria
- If FAIL: summarize which criteria are not met and why
- Suggested next steps

### Step 4: Apply Professional Formatting

- Use consistent heading hierarchy throughout
- Include all key tables from underlying analyses (reformatted for memo context)
- Bold key figures and critical findings
- Use bullet points for readability
- Ensure every claim is traceable to a DD source
- Add source citations inline (e.g., "per rent roll analysis", "per market study", "per physical inspection")
- No placeholder text or TBD markers in the final document

---

## Output Format

### Required Document Structure

```markdown
# Investment Committee Memorandum
## {Property Name} | {City, State}
## {Unit Count} Units | ${Purchase Price}
## Date: {date}
## Prepared by: {preparer}

---

### RECOMMENDATION: {PASS | FAIL | CONDITIONAL}
{One paragraph summary of recommendation and rationale}

---

## 1. Executive Summary
{Deal thesis, key merits, key risks, metrics snapshot}

## 2. Property Overview
{Physical description, unit mix, location, condition}

## 3. Market Analysis
{Submarket, supply/demand, comps, trends}

## 4. Tenant & Lease Analysis
{Tenant profile, lease terms, rollover risk}

## 5. Physical Condition & Capital Expenditures
{Condition, CapEx schedule, environmental}

## 6. Title & Legal
{Title status, encumbrances, zoning}

## 7. Financial Analysis
{Pro forma summary, returns, value creation bridge}

## 8. Scenario & Sensitivity Analysis
{Key cases, probability-weighted returns, stress test}

## 9. Risk Assessment
{Categorized risks, severity, mitigants, overall rating}

## 10. Investment Thesis & Value Creation Plan
{Why this deal, competitive advantages, exit strategy}

## 11. Recommendation & Next Steps
{Final verdict, conditions if applicable, next steps}

---

### Appendix A: DD Source Coverage & Verdicts
| Source | Coverage | Verdict |
|--------|----------|---------|
| Rent Roll Analysis | {summary} | PASS/FAIL/CONDITIONAL |
| OpEx Analysis | {summary} | PASS/FAIL/CONDITIONAL |
| Physical Inspection | {summary} | PASS/FAIL/CONDITIONAL |
| Market Study | {summary} | PASS/FAIL/CONDITIONAL |
| Tenant Analysis | {summary} | PASS/FAIL/CONDITIONAL |
| Title Review | {summary} | PASS/FAIL/CONDITIONAL |
| Environmental Review | {summary} | PASS/FAIL/CONDITIONAL |

### Appendix B: Key Assumptions
{All assumptions used in financial model and scenario analysis}

### Appendix C: Glossary
{Key terms and definitions for IC members}
```

---

## Quality Checks

Before finalizing the memo, run all of the following checks:

**Template Compliance**
- All 11 sections present and substantively filled (no placeholders or TBD markers)
- Appendices A, B, and C included
- Minimum length is substantive (~2,000+ words for the body)

**Source Coverage**
- All DD sources referenced in the memo body
- If a DD source was unavailable, note it explicitly in the relevant section rather than silently omitting it
- Every quantitative claim cites a source (rent roll, market study, financial model, etc.)

**Metric Consistency**
- All financial figures in the IC memo match the financial model output exactly
- Scenario statistics (best/worst/base IRR, stress test count) match scenario analysis output
- No discrepancies between sections citing the same metric

**Risk Completeness**
- All risk flags from DD sources are captured in Section 9
- No DD agent verdicts of FAIL or CONDITIONAL are omitted from the risk assessment
- Each key risk has at least one identified mitigant

**Recommendation Logic**
- The final verdict is consistent with the financial model verdict, scenario assessment, and risk rating
- If any DD source produced a FAIL verdict, the memo addresses it explicitly in the recommendation
- CONDITIONAL verdicts include a clear, actionable list of conditions

**Formatting**
- Consistent heading hierarchy (no skipped levels)
- Tables are formatted cleanly and match surrounding narrative
- Key figures are bolded; no walls of unformatted text

**Self-Validation**

| Field | Valid Range | Flag If |
|-------|-----------|---------:|
| All metrics referenced | Must match source analyses | Mismatch with source |
| Deal recommendation | PASS, CONDITIONAL, FAIL | Any other value |
| Risk factors identified | At least 3 | Fewer than 3 |
| Key assumptions | All must be sourced from DD or UW data | Unsourced assumption |

---

## Red Flags & Dealbreakers

This skill compiles findings from upstream analyses rather than directly detecting dealbreakers. However, if any data encountered during compilation suggests a dealbreaker condition, flag it as CRITICAL in the risk assessment and recommendation sections.

Watch for these patterns across DD sources:
- Any DD source verdict of FAIL that was not addressed in underwriting
- Base case financial model verdict of FAIL on any primary investment criteria
- Scenario stress test showing > 25% probability of DSCR < 1.0x
- Environmental Phase II findings with unresolved contamination
- Title encumbrances that could impair transfer or operations
- Deferred maintenance exceeding the CapEx budget in the financial model

---

## When Data is Missing

When a DD source is unavailable or incomplete:

1. **Note the gap explicitly** — state in the relevant memo section that the analysis was not available or was incomplete, and what the implication is
2. **Attempt a workaround** — use industry benchmarks from the Multifamily Benchmarks knowledge base to approximate missing data points; note the gap in the relevant memo section rather than omitting the section
3. **State assumptions clearly** — document what substitute approach was used and flag it as an assumption
4. **Mark in output** — add to `uncertainty_flags` and note in Appendix B
5. **Continue compilation** — use conservative assumptions; reduce overall confidence rating; aggregate all gaps for the IC's awareness

Common fallbacks:
- Missing tenant analysis: note lease term distribution is not available; describe tenant profile from rent roll data only
- Missing environmental review: note Phase I was not reviewed; flag as a pre-close requirement in Section 11
- Missing title review: note title was not reviewed; flag as a pre-close requirement
- Missing market study: use publicly available market data; note reliance on external sources

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **HIGH** | All DD and UW sources available and complete; no assumptions required; all metrics verified |
| **MEDIUM** | 1–2 DD sources missing or incomplete; minor gaps filled with benchmarks; recommendation supported by available data |
| **LOW** | Multiple DD sources missing; significant assumptions required; recommendation carries meaningful uncertainty |

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

The IC memo should aggregate uncertainty_flags from all upstream analyses and include them in the risk assessment section, so IC members understand the data quality behind the recommendation.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:

- [Risk Scoring Framework](knowledge/risk-scoring.md) — risk categorization methodology for rating and ranking findings from all DD sources
- [Underwriting Calculations](knowledge/underwriting-calc.md) — formulas behind the financial metrics cited in the memo
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — market norms for expense ratios, vacancy, rent growth, and cap rates used to contextualize findings
- [Financial Model Builder](skills/underwriting/financial-model-builder.md) — produces the base case financial model that feeds Sections 7 and 8 of the memo
- [Scenario Analyst](skills/underwriting/scenario-analyst.md) — produces the 27-scenario stress test that feeds Section 8 of the memo

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
