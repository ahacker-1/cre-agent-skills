---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Monthly Variance Analyst

Produce an LP-ready monthly or YTD variance analysis that compares actuals to budget, classifies every material variance as Timing / Permanent / One-Time per the pack taxonomy, and delivers institutional-grade commentary with a forward-look.

---

## When to Use This Skill

Use this skill when you have a stabilized U.S. multifamily property's operating actuals (month and/or YTD) alongside an approved budget, and you need to produce the variance package that accompanies a monthly flash report, a quarterly asset review (QAR), or an ad-hoc LP update. It is the right starting point whenever the question is "what actually happened vs plan, why, and what does it mean for the rest of the year" — not for building the budget (see Annual Operating Budget Builder) and not for writing the full QAR narrative (see Quarterly Asset Review Writer).

---

## What You'll Need to Provide

- Property name, unit count, class, and market
- Reporting period (month and/or YTD through the cutoff date)
- Actuals by line item — current month and YTD — on a stated basis (cash or accrual)
- Approved original annual budget by line item (never overwritten)
- Current full-year reforecast, if one has been produced, as a separate column
- Line-item basis for each actual (cash vs accrual) where it diverges from budget
- Materiality override, if the operator uses something other than the lesser of 10% OR $25,000
- Operator storm-cost add-back policy (add back to normalized NOI or not — MAA-style no-add-back is a peer-disagreement worth confirming)
- Named catastrophe, litigation, tax-refund, or other one-off events in the period
- Sign convention the operator uses for expense variances (Actual − Budget or Budget − Actual)

---

## Mission

Produce a defensible monthly / YTD variance package that (a) isolates which line items crossed the pack materiality floor, (b) classifies each material variance as Timing, Permanent, or One-Time by mechanically applying `_taxonomy-seed.md` §3 decision rules in order, (c) reports mixed variances as two components when appropriate, (d) delivers plain-English commentary in the institutional REIT narrative pattern, and (e) states the forward-period reforecast implication for every Permanent variance.

---

## Strategy

### Step 1: State the Ground Rules at the Top of the Package

Fix the following before any classification work:

- Reporting period (month and YTD cutoff)
- Sign convention: favorable variance = higher revenue or lower expense than budget. `Variance $ = Actual − Budget` is the institutional default. State explicitly.
- Basis: cash or accrual. Flag any line where the budget basis diverges from the actuals basis (property tax and insurance are the usual offenders).
- Materiality floor in force: default is the lesser of 10% of the budgeted line item OR $25,000 absolute (per `_taxonomy-seed.md` §3). Apply the line-item-specific adjustments from `knowledge/asset-management-benchmarks.md` §1 (property taxes / insurance / payroll tighten to 5%; marketing / professional fees / communications drop the absolute floor to $5,000).
- Property-scale floor: use the size-calibrated floor from `knowledge/asset-management-benchmarks.md` §1 (25–75 units → $5k; 75–200 → $10–15k; 200–500 → $25k; 500+ or multi-property → $50k).

### Step 2: Build the Line-Item Variance Table

Per `knowledge/asset-management-reporting-standards.md` (Tabular Presentation Convention) and the R2 column convention, compute for every GL line:

- Current Month Actual, Current Month Budget, Current Month Variance $, Current Month Variance %
- YTD Actual, YTD Budget, YTD Variance $, YTD Variance %
- Full-Year Reforecast (if maintained) and Original Annual Budget (frozen — never overwritten)

Suppress the % column when the budget denominator is near zero; rely on the absolute dollar floor instead.

### Step 3: Apply the Materiality Gate

Only classify variances that cross the materiality floor set in Step 1. Below-floor line items remain in the table but require no commentary and no classification work.

### Step 4: Classify Each Material Variance (Apply §3 Verbatim, In Order)

From `_taxonomy-seed.md` §3 — **order of application is strict. Evaluate Timing first. If no fit, evaluate One-Time. Classify as Permanent by residual.**

**Timing decision rule.** Year-to-date variance exists, but (a) annual budget total is unchanged (or changes by less than the materiality floor), AND (b) the variance is expected to reverse / converge by fiscal year end (either (i) the charge accrues on a different cadence than budgeted, OR (ii) an invoice hit early/late, OR (iii) a seasonal/weather pattern whose full-year run-rate remains within materiality). Signal: reversing sign in subsequent months OR annual projection still within materiality of original budget.

Common Timing patterns (per R2 research):
- Property taxes budgeted straight-line but paid on a semi-annual or annual jurisdiction cadence.
- Insurance premiums budgeted straight-line but paid as an annual lump on renewal.
- Utilities with seasonal swings against a straight-line budget (summer cooling Sun Belt; winter heating Northeast).
- Contract services billed quarterly / semi-annually / annually (landscape, pest, elevator).

**One-Time decision rule.** Variance caused by a discrete, non-recurring event with a clear start and end and no expectation of repetition in the current or future fiscal years. Signal: (a) single-period hit, AND (b) identifiable external trigger (named storm, litigation settlement, one-off tax refund, uninsured event, seasonal extreme clearly outside the normal range). Exclude from run-rate NOI. Seasonal/weather effects within the normal range → Timing, not One-Time.

Common One-Time patterns: named hurricanes (Ian, Idalia, Helene, Milton), litigation settlements, uninsured casualty events, one-off tax refunds, discrete regulatory fines.

**Permanent decision rule (by residual).** Variance reflects a structural change in the underlying economics that will persist for the remainder of the fiscal year and beyond. Signal: (a) variance persists for **2+ consecutive months** in the same direction at similar magnitude (or, on a single-period line item like annual insurance renewal, the new level is expected to persist), AND (b) no invoice-lag or seasonality explanation fits. Forward projection must be re-baselined.

Common Permanent patterns: insurance renewal at a new run-rate (Camden's 2024 sequence +18% → −3% → −10% is the textbook example), property-tax reassessment or abatement expiration (AvalonBay NYC), labor inflation / payroll step-ups, management-fee re-negotiations.

### Step 5: Apply the Mixed-Variance Rule

Per `_taxonomy-seed.md` §3: "If the full-year annual projection diverges from budget by more than the materiality floor AND the YTD variance also has a clear timing cadence component, **split the variance into two reported components**: one Timing (the cadence-driven portion expected to converge) and one Permanent (the residual annual divergence). Report both in the variance commentary. Do NOT force the whole variance into one bucket when it is materially mixed."

Canonical example: an insurance renewal billed two months late (Timing component) AT a 15% higher rate than budgeted (Permanent component). Report both.

### Step 6: Apply the Seasonal / Weather Rule

Per `_taxonomy-seed.md` §3: "A variance driven by weather or seasonality is Timing if the annual run-rate converges within materiality; Permanent if the full year cumulatively diverges (e.g., a persistently harsh summer pushing annual cooling load materially above budget); One-Time only if the weather event is named or otherwise extreme enough to exclude from run-rate (hurricane, wildfire, named freeze)."

### Step 7: Draft Commentary in the Institutional REIT Pattern

Pattern (per `knowledge/asset-management-reporting-standards.md` and R2 research): **topic → driver → quantification → classification → forward-look.**

Model narrative (per `asset-management-reporting-standards.md` "Model Narrative Format"):

> "Property taxes for the quarter came in $48,000 favorable to budget (−11%), driven by a successful 2024 assessment appeal at the Atlanta asset that reduced the assessed value by $2.1M. This is a permanent variance — the new assessment basis persists for at least the next reassessment cycle. Full-year expense guidance is tightened by 30 bps."

Every material variance commentary must include: (1) the specific GL line, (2) quantification in both $ and %, (3) operational or market driver, (4) classification bucket, (5) forward-period implication (or "no forward impact — timing only").

### Step 8: Trigger Reforecast Updates Only for Permanent Variances

Per `knowledge/asset-management-benchmarks.md` §1 Reforecast Trigger Table and R2 research:

- Timing → NO reforecast update. Full-year figure stands.
- Permanent (above materiality) → YES reforecast update within 30 days of identification.
- One-Time → generally NO reforecast. But flag any knock-on Permanent effect (e.g., post-storm premium step-up at next renewal).
- Mixed Timing + Permanent → reforecast the Permanent component only.

**Baseline preservation rule (mandatory).** Original approved annual budget must never be overwritten. Carry "Variance to Original Budget" and "Variance to Current Reforecast" as separate columns. A reforecast is an updated estimate, NOT a new approved budget.

### Step 9: Reconcile the Variance Totals

Sum check: `Timing $ + Permanent $ + One-Time $ = Total Variance $`. If the identity fails, the splits in Step 5 are wrong or a classification is missing.

---

## Output Format

```markdown
# Monthly Variance Analysis
## Property: {Property Name} — {Unit Count} units, Class {A/B/C}, {Market}
## Period: {YYYY-MM or YYYY-MM YTD}
## Basis: {Cash | Accrual}
## Sign Convention: Actual − Budget; favorable = higher revenue or lower expense
## Materiality Floor in Force: lesser of {X%} OR ${Y}

---

### Period Summary
- Total Revenue Variance: ${} ({}%)  [favorable/unfavorable]
- Total OpEx Variance: ${} ({}%)
- Total NOI Variance: ${} ({}%)
- Classification split (YTD $): Timing ${}, Permanent ${}, One-Time ${}
- Reforecast action: {No change | Permanent variance triggers reforecast of line items X, Y, Z}

### Top 5 Variance Drivers (by absolute $)

1. {Line Item} — ${} ({}%) — {Timing | Permanent | One-Time} — {one-sentence driver}
2. ...
3. ...
4. ...
5. ...

### Line-Item Variance Table (YTD)

| Line Item | Budget | Actual | Variance $ | Variance % | Classification | Commentary |
|---|---|---|---|---|---|---|
| Property Taxes | | | | | | |
| Insurance | | | | | | |
| Utilities — Water/Sewer | | | | | | |
| Utilities — Trash | | | | | | |
| Utilities — Gas | | | | | | |
| Utilities — Electric | | | | | | |
| Repairs & Maintenance | | | | | | |
| Turnover / Make-Ready | | | | | | |
| Contract Services | | | | | | |
| Management Fee | | | | | | |
| Payroll | | | | | | |
| Administrative | | | | | | |
| Marketing / Advertising | | | | | | |
| Professional Fees | | | | | | |
| Communications | | | | | | |
| **Total OpEx** | | | | | | |
| **NOI** | | | | | | |
| Replacement Reserves (below NOI) | | | | | | |
| **NCF** | | | | | | |

(Suppress variance % when budget denominator is near zero; rely on absolute dollar floor. Sub-floor lines may be aggregated or omitted from commentary.)

### Commentary (Material Variances Only)

Each entry follows: topic → driver → quantification ($ and %) → classification → forward-look.

- **{Line Item 1}:** {narrative in REIT pattern}
- **{Line Item 2}:** {narrative in REIT pattern}
- ...

### Mixed-Variance Splits (if any)

- **{Line Item}:** Total variance ${}; Timing component ${} (reason); Permanent component ${} (reason).

### Forward-Look / Reforecast Adjustments

- {Line Item}: original budget ${}, revised reforecast ${}, driver {}, classification Permanent.
- {Line Item}: no reforecast change — Timing variance expected to converge by FY end.
- Knock-on effects: {e.g., insurance renewal step-up expected at next policy renewal as residual impact of hurricane deductible}

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Sum of variance explanations × affected line items = total variance reported (no missing dollars)
- Timing + Permanent + One-Time dollars = total variance (identity must hold at the YTD line)
- Every line item with ≥ 5% deviation from budget has a classification (or is explicitly flagged sub-materiality)
- Classifications follow `_taxonomy-seed.md` §3 decision rules exactly, in the prescribed order (Timing → One-Time → Permanent by residual)
- Materiality floor per `knowledge/asset-management-benchmarks.md` §1 applied before classification; property-scale and line-item-specific adjustments from §1 are reflected
- Sign convention stated at the top and applied consistently across the table
- Cash-vs-accrual basis mismatches reconciled BEFORE reporting a variance (property tax and insurance are flagged, not reported as real variances)
- Original annual budget preserved as a separate frozen column; reforecast carried in its own column — the two are never merged
- Mixed-variance splits sum back to the reported line-item total
- Every Permanent variance above materiality has a forward-period reforecast implication stated
- Every One-Time variance has a named external trigger (storm, litigation, tax refund, etc.); if none, re-evaluate as Permanent
- Variance commentary follows the REIT pattern: topic → driver → quantification ($ and %) → classification → forward-look

---

## Red Flags & Dealbreakers

- **Permanent variance > 10% of annual line item → reforecast trigger.** Issue ad-hoc reforecast within 30 days per `knowledge/asset-management-benchmarks.md` §1 Reforecast Trigger Table. Do not wait for quarter-end.
- **One-Time variance unexplained by named event → reclassify to Permanent (investigate).** If no identifiable external trigger exists, the "One-Time" label is being used to hide a structural issue. Per §3, a One-Time bucket requires a named storm, litigation settlement, one-off tax refund, uninsured event, or seasonal extreme clearly outside normal range.
- **Mixed variance $ > materiality floor → report as two components per taxonomy seed.** Do not force a mixed variance into one bucket; split into Timing and Permanent per `_taxonomy-seed.md` §3 Mixed-Variance Rule.
- **Line-item variance > 10% AND > $25K for 2+ consecutive months same direction → Permanent; reforecast required.** Per `knowledge/asset-management-benchmarks.md` Quick Reference red flag table; supersedes any prior Timing classification.
- **Insurance increase > 15% YoY without cat event → investigate.** Claims history, poor loss-control, or hardening insurance market. Flag in commentary; may require Risks & Watch Items escalation in the QAR.
- **Variance > 25% or > $100,000 on any line → escalate to Executive Summary.** Per `knowledge/asset-management-reporting-standards.md` materiality table, this tier requires Executive Summary and/or Risks & Watch Items disclosure even if classified as Timing or One-Time.
- **Variance > 50% or affecting covenants → immediate LP notification separate from the variance package.** Do not wait for the next scheduled report.
- **Reforecast silently replaces original approved budget → reporting failure.** A reforecast is an estimate, not a new baseline. Both columns must appear in every variance report.
- **Portfolio / consolidated reforecast changes by less than the sum of property-level reforecasts → top-down plug, not bottom-up.** Per REBA guidance cited in R2; require property-level updates first.

---

## When Data is Missing

- **Original annual budget missing or partial.** Variance analysis is not possible without a baseline. Request the approved budget; in its absence, reconstruct from the property's prior T-12 as a proxy baseline and state the substitution explicitly — confidence drops to LOW and the package is labeled "indicative, not variance-to-approved-budget."
- **Reforecast column missing.** Proceed with variance-to-original-budget only. Note in the header that current reforecast is not available. Do not invent a reforecast; that would silently rebase the budget.
- **Line-item basis (cash vs accrual) not stated.** Ask. If unanswered, assume accrual for institutional reporting and flag that property-tax and insurance timing variances may be basis artifacts, not operational. Confidence: MEDIUM.
- **Single-month data only (no YTD).** Run current-month variance only and note that Timing classification requires YTD or trailing-3 data to confirm convergence. Treat single-month results as directional; confidence: MEDIUM at best.
- **Named storm or catastrophe event period but no deductible / recovery detail.** Classify the gross hit as One-Time in the current period, add an explicit "expected insurance recovery pending" footnote with ballpark deductible per building, and flag that the net impact is not yet known. Do not net the recovery before it is booked.
- **Operator storm-cost add-back policy unknown.** Default to "no add-back" and flag. Note explicitly: variance classification (One-Time) is independent of FFO/NOI add-back policy per R2. Confirm at engagement onboarding.
- **Unbudgeted line item (actual hit to a GL line with zero budget).** Treat the full actual as variance. Classification depends on the event: new recurring reserve = Permanent; one-off litigation = One-Time. Do not suppress the line.
- **Prior-month / trailing data unavailable to confirm 2+ consecutive months test.** Default the classification conservatively: if the item would otherwise be Timing but you cannot confirm reversal, hold at Timing with a "pending trailing-3 confirmation" note. Revisit next period. Confidence: MEDIUM.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Original annual budget, current reforecast, and at least YTD actuals on a consistent basis are all available; line-item basis (cash/accrual) stated; named events for any One-Time classification confirmed; 2+ months of trailing data available to validate Timing-vs-Permanent calls. |
| MEDIUM | Core actuals vs budget available but one or more of: basis not stated, reforecast column missing, single-month (no trailing) data, ambiguous classification on a material line, or operator storm add-back policy unconfirmed. Classifications are defensible but flagged for next-period review. |
| LOW | Original approved budget missing or reconstructed from a proxy; material cash-vs-accrual basis mismatch unreconciled; one or more material line items with no clear classification; or insufficient data to apply the 2+ consecutive months test on line items that structurally require it. Package labeled "indicative, not variance-to-approved-budget." |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) — §1 Variance Materiality Thresholds (dual-threshold defaults, line-item adjustments, property-scale floors, Reforecast Trigger Table)
- [Asset Management Reporting Standards](knowledge/asset-management-reporting-standards.md) — Variance Classification at the Reporting Layer, Materiality Thresholds in Reports, Model Narrative Format, LP-facing commentary conventions
- [Underwriting Calculations](knowledge/underwriting-calc.md) — NOI, EGI, GPI, concessions, bad-debt, and replacement-reserve / NCF formulas referenced by the variance table (do not redefine)

---

## Structured Output

```json
{
  "skill": "monthly-variance-analyst",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "period": "{e.g. 2026-03 YTD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "total_variance_pct": 0,
    "total_variance_dollars": 0,
    "variance_by_line_item": [],
    "timing_variance_dollars": 0,
    "permanent_variance_dollars": 0,
    "one_time_variance_dollars": 0,
    "variance_commentary": ""
  },
  "uncertainty_flags": [
    { "field_name": "", "reason": "estimated | assumed | missing_source | conflicting_sources", "impact": "" }
  ],
  "red_flags": [
    { "severity": "HIGH | MEDIUM | LOW", "description": "", "recommended_action": "" }
  ]
}
```

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
