---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# CapEx & Value-Add Execution Tracker

Track post-close multifamily value-add execution against underwriting: unit-turn cost vs budget, rent-premium realization vs pro-forma, schedule adherence, yield-on-cost, and the failure modes that convert a good deal into a capital-stack problem.

---

## When to Use This Skill

Use this skill when an asset manager, owner-operator GP, LP reporting team, or construction manager needs a monthly/quarterly read on how a value-add capital plan is performing against the acquisition underwriting. It is the right starting point any time the deal thesis depends on renovation-driven rent lift and the question is no longer "will we close?" but "are we delivering what we underwrote?"

Typical triggers:

- Monthly asset-management report or LP quarterly supplemental
- Bridge-to-perm loan decision point where the take-out lender needs realized NOI
- Mid-program re-baseline when actuals have diverged from plan
- Hold / sell / refi analysis requiring durable post-renovation NOI
- Supplemental / green-rewards loan sizing against projected post-renovation rents

This skill is **not** the right tool for pre-acquisition capex underwriting (see Due Diligence pack), replacement-reserve accrual modeling (see R1 / renewal-economics KB), or routine non-renovated turnover economics (see R4). Hand off to those skills where those questions dominate.

---

## What You'll Need to Provide

Required:

- **CapEx program budget** — interior-renovation total budget, common-area / amenity budget, major-systems budget (kept separate), and the contingency line. Per-unit budget by scope tier (Light / Medium / Heavy).
- **Actual spend to date** — $ spent cumulatively and month-to-date, split by interior unit renovations, common area, and major systems. Contingency committed and contingency remaining.
- **Units renovated** — cumulative count, month-over-month completions, unit-type mix (studio / 1BR / 2BR / 3BR), and the scope tier per unit (Light / Medium / Heavy).
- **Renovated-vs-classic rent premium achieved** — achieved face rent on renovated units, matched classic (non-renovated) rent at the same property, and the underwritten premium target. Both new-lease trade-outs and renewal trade-outs.
- **Schedule vs plan** — original program start / completion dates, current milestone status (kickoff / GC selected / 10% / 25% / 50% / 75% / 100%), and forecast completion.

Strongly recommended:

- Concessions on renovated units (free months, reduced rent, move-in incentives) so face premium can be converted to effective premium
- Renovation-complete-to-lease-commencement vacancy days (absorption signal)
- Comp-set rent growth and submarket supply deliveries over the program window
- Reassessment / insurance / utility-cost impacts post-renovation
- Rent-control / LIHTC / affordable overlay status if any

Optional but valuable:

- First-cohort vs steady-state premium split (units 1–20 vs units after month 4)
- Trade-out detail by unit type and bedroom count
- GC / construction-manager change-order log

---

## Mission

Produce a defensible execution read that reconciles actual capex spend, actual units delivered, and actual rent premium against the underwriting, computes yield-on-cost and premium-realization %, flags cost overruns and schedule slippage, and names the specific failure modes that are eroding premium capture. The output must be usable both as an internal asset-management dashboard and as an LP-reporting variance narrative.

---

## Strategy

### Step 1: Anchor to the Underwritten Plan

Before touching actuals, restate the underwriting as it was originally approved:

- Per-unit renovation budget and scope tier
- Total units planned, phasing / cadence
- Underwritten rent premium ($/mo and % lift over classic)
- Underwritten yield-on-cost
- Underwritten program duration and completion date
- Common-area and major-systems budgets (kept separate)

Do not silently overwrite the UW baseline with a later re-forecast. If the plan has been re-baselined, carry both original UW and current-approved forecast through the tracker.

### Step 2: Reconcile Units and Dollars

For each reporting period:

- Cumulative units renovated ÷ units planned = program % complete
- Cumulative $ spent ÷ total budget = budget % consumed
- Cost per renovated unit (actual) vs budget per unit
- Decompose actual cost by unit type — 3BR/townhome cost creep is a common blind spot
- Contingency committed ÷ total contingency = contingency burn %

Apply the pack red-flag rule: **contingency burn % > program-complete %** is an early-warning signal of a 15–25% program-level overrun at completion. Re-baseline rather than absorb.

### Step 3: Measure Rent-Premium Realization

The central execution KPI. Compute:

- Achieved face premium = renovated-unit face rent − matched classic face rent
- Achieved effective premium = achieved face premium − annualized concession drag
- Premium realization % = achieved effective premium ÷ underwritten premium × 100
- Split new-lease trade-out vs renewal trade-out (renewal premiums are typically 30–60% of new-lease premiums)
- Report first-cohort vs steady-state: units 1–20 capture novelty premium; project the steady-state from the 4th–8th month of leasing

Benchmark per R6 and `knowledge/asset-management-benchmarks.md`:

| Realization % | Verdict |
|---|---|
| 85%+ | Strong |
| 70–85% | Acceptable |
| 50–70% | Underperforming |
| <50% | Failing — re-baseline required |

### Step 4: Compute Yield-on-Cost

Yield-on-cost = (achieved effective premium × 12) ÷ actual renovation cost per unit × 100

Benchmarks (Medium scope, interior):

- 18–22% — institutional target, REIT disclosure range (MAA, Camden, UDR)
- 12–15% — minimum acceptable
- <10% — failing; scope or pricing is wrong

Heavy-scope / re-amenitization programs benchmark lower (7–10%, AvalonBay re-development band) — do not mis-apply the Medium target.

### Step 5: Reconcile Schedule

- Original planned completion vs current forecast completion (days variance)
- Unit-turn cadence actual vs 10–20 units/month planning norm
- Common-area milestones: front-loaded (months 1–9) or back-loaded? Back-loaded common-area delivery erodes first-12-month premium capture by 10–20%.
- Renovated-unit downtime (completion → lease commencement). >30 days signals mispricing; >14 days on a steady-state unit is a yellow flag.

### Step 6: Classify Cost Overruns

Compute overrun % = (actual − original budget) ÷ original budget × 100 (standardize to original-budget denominator per R6 conflicting-source resolution).

| Overrun | Verdict |
|---|---|
| 0–10% | Within tolerance, 2024–2025 plateau norm |
| 10–20% | Elevated; identify driver (materials / labor / scope creep / discovered conditions) |
| 20%+ | Material; LP re-baseline trigger |

Attribute overruns to the four canonical drivers from R6:

1. Discovered conditions at unit turn (hidden damage, subfloor, plumbing)
2. Scope creep on amenities / finish upgrades mid-execution
3. Change orders from finish-package substitutions / supply lead times
4. Schedule slippage causing carrying-cost overruns (interest, taxes on vacant units)

### Step 7: Name the Premium-Realization Failure Modes

Per R6, when realization % is underperforming or failing, name which of these failure modes applies. Do not report a low realization % without a named failure mode.

- **FM-1: Comp-set rent growth below UW assumption** — base rent growth of 0–2% actual vs 4–6% underwritten (2021–2022 vintage problem per W&D). Detection: pull comp-set growth over the program window and compare to UW base growth.
- **FM-2: Oversupply compressing premiums** — new deliveries in submarket exceed absorption, concessions re-emerge, renovated premium gets competed away. Per M&M, specific metros running 40–65% of UW premium in 2024 (Austin, Phoenix, Nashville, Raleigh, Charlotte, Salt Lake City). Detection: submarket pipeline + concession prevalence.
- **FM-3: Amenity-tier saturation** — renovated unit no longer stands out because new supply ships with the same finish package at entry pricing. Detection: comp-shop finish parity vs new supply.
- **FM-4: Demographic shift away from renovation tier** — the renter cohort that pays for Class A finishes is leaving the submarket (e.g., remote-work coastal exodus 2020–2022). Detection: demographic trend + move-in application quality.
- **FM-5: Scope mis-fit for submarket WTP** — lipstick scope applied where renters only pay for full kitchen refresh (per John Burns WTP research), or heavy scope applied where premium ceiling is $75/mo. Detection: scope tier vs premium ceiling for market.
- **FM-6: Renovated-unit concessions masking face premium** — 1+ month free on renovated units means effective premium is materially below face premium. Detection: compute effective premium net of concession drag.
- **FM-7: First-cohort novelty premium not durable** — first 20 units leased at higher-than-steady-state premium; steady-state is 70–85% of first-cohort rate. Detection: project from month 4–8, not month 1–2.
- **FM-8: Renewal trade-out drag** — existing tenants on renewal accept renovated-unit status but at 30–60% of the new-lease premium. Detection: separate renewal vs new-lease trade-out reporting.

### Step 8: Compute Post-Renovation NOI Drag

Gross premium capture is not net NOI. Subtract:

- Property-tax reassessment impact ($300–$800/unit/yr in reassessment-on-transfer states)
- Insurance premium uplift (10–25% on post-renovation replacement cost)
- Utility / common-area-operating uplift from new amenities (fitness, pool, smart-home tech)

Report both gross and net premium capture. The Hold/Sell/Refi analyst skill and LP reporting should consume net.

### Step 9: State the Verdict

Three dimensions, each PASS / MARGINAL / FAIL:

- Cost adherence
- Schedule adherence
- Premium realization

A program is only PASS overall if all three are PASS or MARGINAL with a named remediation plan.

---

## Output Format

```markdown
# CapEx & Value-Add Execution Tracker
## Property:
## Reporting Period:
## Overall Status: PASS | MARGINAL | FAIL

### Program Snapshot
- Scope Tier: Light | Medium | Heavy
- Units Planned:
- Units Renovated to Date: (% complete)
- Total Budget (Interior / Common / Major Systems / Contingency):
- Total Spent to Date: (% of budget)
- Contingency Burn: % committed at % program complete
- Original Completion Date → Current Forecast Completion:

### Unit-Turn Execution Table
| Unit Type | Units Planned | Units Renovated | $/Unit Budget | $/Unit Actual | Variance % |
|---|---|---|---|---|---|
| Studio | | | | | |
| 1BR | | | | | |
| 2BR/1BA | | | | | |
| 2BR/2BA | | | | | |
| 3BR | | | | | |

### Rent-Premium Realization
- Underwritten Premium: $/mo
- Achieved Face Premium: $/mo
- Concession Drag: $/mo
- Achieved Effective Premium: $/mo
- Premium Realization %: (verdict)
- New-Lease Trade-Out: $/mo / %
- Renewal Trade-Out: $/mo / %
- First-Cohort vs Steady-State: $/mo / $/mo
- Lease-Up Downtime (completion → commencement): days

### Schedule vs Plan
- Program % Complete:
- Units/Month Cadence (actual vs 10–20 planning norm):
- Common-Area Milestone Status (front-loaded / back-loaded):
- Days Variance vs Original Completion:

### Cost-Overrun Analysis
- Overall Overrun %: ((actual − original budget) / original budget)
- Primary Drivers (name 1–4):
  - Discovered conditions
  - Scope creep
  - Change orders / supply lead times
  - Schedule slippage / carrying cost

### Premium-Realization Failure Modes Flagged
- List any of FM-1 through FM-8 that apply, with evidence.

### ROI Summary
- Actual Renovation Cost / Unit:
- Achieved Effective Premium (annualized):
- Yield-on-Cost % (verdict vs 18–22% target):
- Gross vs Net Premium (after reassessment / insurance / utility drag):

### Verdict
- Cost: PASS | MARGINAL | FAIL
- Schedule: PASS | MARGINAL | FAIL
- Premium: PASS | MARGINAL | FAIL
- Overall: PASS | MARGINAL | FAIL

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Original underwriting baseline is preserved alongside any re-baselined forecast. The tracker does not silently adopt a later forecast as "plan."
- Interior, common-area, and major-systems capex are tracked in separate buckets. Combined reporting is only produced for board-level summary, never for ROI computation.
- Yield-on-cost uses effective premium (net of concessions), not face premium.
- Premium realization is reported at both face and effective, and both new-lease and renewal trade-outs are reported separately.
- Cost overruns are denominated as % of **original budget**, not % of final actual cost (pack convention per R6 conflicting-source resolution).
- When realization % is below 85%, at least one named failure mode (FM-1 through FM-8) is cited with evidence.
- Contingency burn is reported against program-complete % (not just as an absolute number).
- First-cohort novelty premium is not projected as steady-state.

---

## Red Flags & Dealbreakers

Structural red flags that change the verdict:

- **Premium realization <50%.** Failing. Re-baseline the UW thesis; the deal may no longer pencil at the UW exit cap. This is the single highest-priority flag.
- **Contingency burn > program-complete %.** Indicates a 15–25% overall overrun at completion is already baked in. LP re-baseline trigger.
- **Yield-on-cost <10% on a Medium scope.** Either overspending or underpricing; the scope-to-market fit is wrong. Do not scale the program further without a re-bid and a comp-shop.
- **Renovated-unit downtime >30 days.** Premium is mispriced vs comps; the market will not absorb at the current asking.
- **Rent-control / LIHTC / affordable overlay present but UW modeled market-rate premiums.** Fundamental error — the skill must redirect to a regulatory-cap calculation. Do not proceed.
- **Tax reassessment triggered but not modeled in net premium.** Gross premium capture may be offsetting to zero on a net basis. Report net NOI impact.
- **Insurance premium uplift not modeled.** 10–25% post-renovation premium lift is routinely overlooked.

Premium-realization failure modes (required naming per R6 when realization underperforms):

1. **FM-1: Comp-set rent growth below UW assumption.** Underwriting assumed 4–6% base growth; actuals are 0–2%. Premium plus base-growth compounding is the miss, not just premium.
2. **FM-2: Oversupply compressing premiums.** Specific Sun Belt submarkets (Austin, Phoenix, Nashville, Raleigh, Charlotte, Salt Lake City) running 40–65% of UW premium per M&M 2025 forecast. Concessions re-emerge and the renovated unit competes against new supply at entry pricing.
3. **FM-3: Amenity-tier saturation.** Renovated finish package no longer differentiates because new deliveries ship with the same package. Common in submarkets with heavy 2023–2025 delivery cohorts.
4. **FM-4: Demographic shift away from the renovation tier.** Class A-paying renter cohort is leaving the submarket; Class B property renovating up toward Class A fails premium capture despite scope execution.
5. **FM-5: Scope mis-fit for submarket willingness-to-pay.** Lipstick scope applied where WTP requires full kitchen; heavy scope applied where premium ceiling is $75/mo. Per John Burns WTP research.
6. **FM-6: Renovated-unit concessions masking face premium.** 1+ month free on renovated units = effective premium is below the UW target even if face premium looks on-plan.
7. **FM-7: First-cohort novelty premium not durable.** First 20 units captured novelty; steady-state lands 70–85% of first-cohort rate.
8. **FM-8: Renewal trade-out drag.** Existing tenants on renewal accept renovated status at 30–60% of new-lease premium; if renewal mix is high, blended realization falls below UW.

---

## When Data is Missing

- **If achieved-rent data is not yet available** (early program months), report premium realization as "Pre-Data" with an explicit note that the first 20-unit cohort will be the first benchmark and the 4th–8th month will establish steady-state. Confidence LOW.
- **If the classic-unit match rent is unclear**, state the assumed classic comparison basis (same floorplan, same property, matched month) and widen the confidence interval. Prefer same-property matched comparison over submarket comp average.
- **If concession data is missing**, report face premium only and flag that the effective premium could be 10–20% lower. Confidence cannot exceed MEDIUM in this case.
- **If renewal vs new-lease trade-out is not split**, report blended trade-out and flag that renewal drag may be masking a premium miss.
- **If reassessment / insurance uplift is not quantified**, report gross premium only and include a line-item placeholder in the output with the pack-default range ($300–$800/unit/yr reassessment; 10–25% insurance uplift) for LP reporting.
- **If first-cohort vs steady-state split is not feasible**, report current realization and explicitly note the projection may drift 15–30% downward when novelty premium decays.
- **If scope-tier classification is ambiguous**, default to the lower tier for benchmarking (e.g., "Medium borderline Heavy" → benchmark against Medium). This prevents overstating yield expectations.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | ≥6 months of post-renovation lease data, ≥30 units renovated and leased, effective premium known (face + concessions), new-lease and renewal trade-outs split, reassessment and insurance uplift quantified, schedule and cost data reconciled monthly |
| MEDIUM | Core cost and units data clean; rent-premium data partial (face only, or new-lease only); reassessment/insurance impacts estimated rather than measured |
| LOW | <3 months of post-renovation data, first-cohort only, concessions unknown, or scope tier ambiguous. Realization % should be flagged as pre-steady-state. |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](../../knowledge/asset-management-benchmarks.md) — unit-turn capex ranges, rent premium realization benchmarks, yield-on-cost thresholds
- [Renewal Economics](../../knowledge/renewal-economics.md) — renewal trade-out dynamics and renewal-vs-new-lease premium split
- [Multifamily Benchmarks](../../knowledge/multifamily-benchmarks.md) — COL cost dispersion multipliers, per-unit expense benchmarks, class-tier context
- [Underwriting Calculations](../../knowledge/underwriting-calc.md) — NOI / NCF conventions, yield and IRR formulas, effective-rent (concession) math

---

## Research Basis

- [CapEx / Value-Add Execution Tracker Research (R6)](../../research/asset-management/capex-value-add-execution-tracker-research.md)

---

## Structured Output

```json
{
  "skill": "capex-value-add-execution-tracker",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "capex_budget_total": 0,
    "capex_spent_to_date": 0,
    "capex_remaining": 0,
    "units_renovated": 0,
    "units_planned": 0,
    "rent_premium_underwritten_per_unit": 0,
    "rent_premium_realized_per_unit": 0,
    "rent_premium_realization_pct": 0,
    "yield_on_cost_pct": 0,
    "cost_overrun_pct": 0,
    "schedule_variance_days": 0,
    "failure_modes_flagged": []
  },
  "uncertainty_flags": [],
  "red_flags": []
}
```

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
