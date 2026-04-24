# Annual Operating Budget Builder

Build a defensible next-fiscal-year operating budget for a conventional stabilized multifamily property from T-12 actuals, the current rent roll, and cited market assumptions — line by line, with every OpEx category traced to a benchmark and every revenue assumption traced to a rent-roll input or comp.

---

## When to Use This Skill

Use this skill when the budget season is active (typically late summer through fall for the following calendar year) and you have T-12 actuals, a current rent roll, and enough market context to build a line-item operating budget for a conventional stabilized multifamily property (5+ units, market-rate, U.S.). This is the right starting point when ownership, LPs, or a lender requires an approved annual operating budget that becomes the baseline against which monthly variance packages and quarterly QARs are measured for the coming fiscal year.

Do NOT use this skill for:

- Lease-up or pre-stabilization properties (defer to a lease-up budget workflow).
- Affordable / LIHTC properties (out of AM pack v1.3.0 scope).
- Multi-year forecasts beyond the next fiscal year.
- CapEx / value-add program planning (that is a separate capital budget — reserves are touched here at the agency-minimum level only).

---

## What You'll Need to Provide

- **T-12 operating statement** (trailing 12 months ending as close to the budget date as possible — institutional convention is ≤90 days stale).
- **T-3 operating statement** (most recent trailing 3 months, for run-rate stress on T-12).
- **Current rent roll** (unit, floor plan, face rent, in-place rent, lease start/end, concessions outstanding, move-in date, delinquency).
- **Property metadata:** total units, unit mix, year built, last major renovation, building class (A/B/C), region, submarket, COL tier.
- **Market rent context:** comp-set averaging or a third-party (CoStar, Yardi Matrix, ALN, RealPage) rent comp set as-of today.
- **Contract schedule:** property tax assessor notice or prior-year bill; insurance broker renewal quote (or prior-year policy and renewal date); service-contract schedule (trash, landscaping, pest, pool, elevator, bulk internet/cable, laundry rev-share).
- **Payroll schedule:** on-site staffing plan with wage grid and expected merit/COLA increases.
- **Known one-time T-12 events** (storm deductibles, litigation, roof replacement, tax refund) — will be excluded from run-rate.
- **Acquisition status:** is this the first post-acquisition budget year? (Triggers property-tax reassessment stress test.)
- **Operator materiality override (optional):** if the operator uses a non-pack dual-threshold (% / $ floor), provide it; otherwise pack defaults apply.

---

## Mission

Construct a line-by-line operating budget for the next fiscal year that separates contractually-known escalators (taxes, insurance, contracts, payroll grid) from benchmark-calibrated run-rate assumptions (R&M, turnover, marketing, admin), allocates every dollar to a taxonomy-canonical line item, applies a seasonality curve so monthly budgets sum to the annual, and outputs NOI and NCF under the AM-pack convention with Replacement Reserves below NOI.

---

## Strategy

### Step 1: Normalize T-12 Actuals (Run-Rate Baseline)

Rebuild the T-12 into a normalized run-rate by:

1. **Mapping every GL line** to the canonical OpEx taxonomy in `research/asset-management/_taxonomy-seed.md` §1. Flag mis-classifications (e.g., trash booked to Contract Services should move to Utilities per IREM; payroll embedded in R&M should move to Payroll per the NAA standalone-line convention).
2. **Excluding one-time events** per `_taxonomy-seed.md` §3 Variance Classification Buckets (One-Time rule): named-storm deductibles, litigation settlements, one-off refunds, uninsured events. State each exclusion with $ amount and rationale.
3. **Adjusting for timing distortions** where an annual invoice (e.g., insurance premium) hit T-12 but is not representative on a run-rate basis — apply the Timing bucket's convergence logic.
4. **Comparing T-3 annualized to T-12** (`T-3 Annualized = sum of last 3 months × 4` per `_taxonomy-seed.md` §2). If T-3 diverges from T-12 by more than the materiality floor (10% OR $25K per `knowledge/asset-management-benchmarks.md` §1), document whether the delta is Permanent (re-baseline) or Timing (retain T-12 base).

**Output of Step 1:** a T-12 normalized run-rate by canonical line item, with explicit exclusions listed.

### Step 2: Build Revenue Assumptions (Top of Budget)

1. **Gross Potential Rent (GPR):** apply the formula from `knowledge/underwriting-calc.md` §Core Income Metrics — `GPR = Unit Count × Average Monthly Market Rent × 12`. Average Monthly Market Rent is set from the comp-set as-of the budget date, not T-12 in-place rents.
2. **Loss-to-Lease (LTL):** apply `_taxonomy-seed.md` §2 LTL formula. Forecast LTL at year-end by projecting rent-roll roll-throughs month-by-month using the rent roll's lease expiration schedule.
3. **Other Income:** forecast per category (RUBS recovery, pet rent, parking, storage, tech package, admin/late fees) using the rent-roll penetration and the portfolio lift ranges in `knowledge/asset-management-benchmarks.md` §9 as a top-down sanity cap. Do NOT stack more than 15% of EGI in ancillary for Class B / 20% for Class A per that KB's aggregate cap rule.
4. **Vacancy Loss:** physical vacancy assumption per `knowledge/multifamily-benchmarks.md` §Physical Occupancy Benchmarks for class and market.
5. **Concessions:** apply `_taxonomy-seed.md` §2 sign convention (concessions REDUCE effective rent — subtractive) and §4 Effective Rent formula. Depth per `knowledge/asset-management-benchmarks.md` §6 by market condition.
6. **Bad Debt:** `Bad Debt = GPI × Bad Debt Rate` per `knowledge/underwriting-calc.md`. Rate by class per `knowledge/asset-management-benchmarks.md` §7 (Class A 0.5–1.0%, Class B 1.0–1.5%, Class C 1.5–2.5%).

Compute EGI using `underwriting-calc.md` §EGI formula: `EGI = GPI − Vacancy − Credit Loss − Concessions`.

### Step 3: Build OpEx by Category (Bottom of Budget) — Contract-Driven First

Order lines from most contract-driven to most judgment-driven. **Never apply a blanket CPI escalator** (per research/asset-management/annual-operating-budget-builder-research.md Red Flag 1 — "the single most common budget error").

1. **Property Taxes** — use the assessor's notice for the next tax year if received. If not, apply the jurisdiction's 5-year historical growth rate. If this is the first post-acquisition budget year, apply the reassessment stress test from `research/asset-management/annual-operating-budget-builder-research.md` §Property Tax Reassessment Stress Test (South FL 80–85% of purchase price; Twin Cities 90–95%; aggressive TX counties 95–100%; CA Prop 13 100% in year 1 with 2% cap after; default 90%). Cross-ref `knowledge/multifamily-benchmarks.md` §Property Taxes by State for effective rate. Range check: $750–$4,200/unit/yr market-dependent per `_taxonomy-seed.md` §1.
2. **Insurance** — use the broker renewal quote. If unavailable, apply +5% from prior-year policy per 2025–2026 moderation trend; carry a 5–10% contingency until quote is in hand. For cat-exposed properties (hurricane FL/TX/SE coast, wildfire CA/OR/WA/CO, earthquake CA/PNW), default to the +25% Stress Case 1 from the research note's Year-1 Insurance Renewal Stress Test. Range check: $400–$1,500/unit base; $800–$1,500+ coastal/cat per `knowledge/multifamily-benchmarks.md` §Insurance Deep Dive.
3. **Service Contracts** (trash/refuse under Utilities per IREM; landscaping, pest, security, pool, elevator under Contract Services) — apply known CPI escalators in existing contracts; for contracts expiring in the budget year, prompt for re-bid assumptions and flag accordingly.
4. **Payroll** — build from the staffing plan × wage grid + 3.5–4.0% merit/COLA increase (BLS ECI-aligned; NAA 2024 reported +3.6% payroll) per research note Finding 5. Include payroll taxes, benefits, workers' comp, bonuses, leasing commissions, and employee-apartment allowance value per `_taxonomy-seed.md` §1 Payroll definition (use NAA standalone-line convention). Range check: $500–$2,500/unit/yr.
5. **Utilities** — sub-line inflation, NOT blanket: water/sewer +5%, gas/fuel flat to −3%, electric +2–3% (per NAA 2024 sub-component data). Trash stays under Utilities per IREM. Range check: $800–$2,000/unit/yr climate/class dependent per `knowledge/multifamily-benchmarks.md`.
6. **R&M** — T-12 normalized run-rate × 2.5–3.5% inflation, PLUS turnover spillover (see Step 4). Range check: $800–$1,400/unit/yr per `_taxonomy-seed.md` §1; NAA 2024 benchmark $1,098/unit.
7. **Turnover / Make-Ready** — explicit bottoms-up: assume turnover rate (pack default 47.5% per `knowledge/asset-management-benchmarks.md` §4 Turnover Rate Benchmarks) × per-turn direct cost from `knowledge/multifamily-benchmarks.md` ($1,500–$3,000/turn direct). Wide-definition cost ($3,500–$4,500 blended, Class B baseline per §4 of AM benchmarks KB) is used for sanity-checking the aggregate turnover economic impact but the BUDGET line uses direct cost only; the vacancy/marketing/concession components of the wide definition flow to the appropriate other lines per §4's Budget Allocation Rule.
8. **Marketing / Advertising** — T-12 × 2.5–3.5% unless a specific ILS, signage, or digital campaign is planned. Range check: $100–$500/unit/yr per `_taxonomy-seed.md` §1.
9. **Administrative + Professional Fees + Communications** — T-12 × 2.5–3.5%. Range check: Admin $200–$600/unit; Professional $50–$200; Communications $30–$120 per `_taxonomy-seed.md` §1.
10. **Management Fee** — % of EGI per the management contract. Per `knowledge/underwriting-calc.md` §Management Fee and `_taxonomy-seed.md` §1: typical 4–8% of EGI; 3% institutional floor (500+ units); flag any rate below 3% or above 8% as a misalignment with the IREM benchmark.
11. **Contingency** — add a 2–3% contingency reserve on total OpEx for unforecasted items, per research note methodology Step 5. Separate from Replacement Reserves.

### Step 4: Apply Seasonality Curve (Monthly Allocation)

Convert each annual line to monthly buckets. Defaults (override with property-specific T-12 monthly actuals if available):

- **Straight-line (1/12 per month):** Management Fee (as % of EGI — but EGI varies monthly, so the management fee will vary too), most Admin, Professional Fees, Communications.
- **Lump-sum cadence:** Insurance premium (one or two invoices/yr depending on policy); Property Taxes (per jurisdiction — often two installments; CA semi-annual Nov/Apr; TX single payment Jan).
- **Weather-indexed:** Utilities — Gas/Heating peaks Dec–Feb; Electric peaks Jul–Aug in cooling-load climates; Water/Sewer roughly flat with a summer lift in irrigation regions.
- **Turnover-indexed:** Turnover, R&M turn-component, Marketing, Leasing — cluster May–Sep (peak leasing season) per industry convention.
- **Payroll:** straight-line with bonus accrual in Dec (or Mar if fiscal-year-aligned).

**Quality check from `_taxonomy-seed.md` §3 Timing rule:** the sum of monthly values must equal the annual line total for every line item.

### Step 5: Compute NOI and NCF (AM-Pack Convention)

Per `research/asset-management/_taxonomy-seed.md` §1 (intentional divergence from `knowledge/underwriting-calc.md` on Replacement Reserves placement):

```
NOI = EGI − Total Operating Expenses      (Total OpEx EXCLUDES Replacement Reserves)
NCF = NOI − Replacement Reserves          (Fannie/Freddie Form 4660 convention)
```

Replacement Reserves floor: $250–$300/unit/yr for newer/well-maintained; $300–$500/unit/yr for older or PCA-flagged properties, per research note Finding 6 and `research/asset-management/annual-operating-budget-builder-research.md` §Conflict 3.

Because the existing repo KB `knowledge/underwriting-calc.md` places reserves INSIDE OpEx, agents should **report both figures** in the Structured Output when the downstream consumer may expect the UW convention: primary NOI is AM-convention (reserves below line); secondary NOI (UW convention, reserves inside OpEx) is a footnoted reconciliation.

### Step 6: Benchmark Sanity Check (Top-Down)

Compare every OpEx line and the total to national/regional/class benchmarks:

- National anchor: **$8,657/unit/yr total OpEx** (NAA/IREM 2024 — the authoritative same-store figure per research note Finding 1).
- Class bands per `knowledge/multifamily-benchmarks.md`: A $7,500–$11,000; B $6,000–$9,500; C $5,000–$8,000.
- Regional multipliers per `research/asset-management/annual-operating-budget-builder-research.md` §Regional Multipliers: Northeast 1.25–1.35x; Midwest 0.85–0.95x; Southeast 0.95–1.05x (insurance 1.40–2.00x coastal FL); Southwest 0.95–1.00x (insurance 1.20–1.60x Gulf TX); West 1.10–1.30x; Mountain West 0.95–1.10x.
- Any line more than ±25% off the benchmark range must be flagged with a rationale in the output.

### Step 7: Stress Tests and Open Questions

1. **Insurance stress:** compute +25% (Stress 1 — single cat-event repricing) and +50% (Stress 2 — market-hardening + loss-history spike) deltas vs base case. Default to base + 5% contingency unless cat-exposed, in which case Stress 1 is default.
2. **Property tax stress:** if post-acquisition or cyclical-reassessment-year, compute the "tax cliff" delta and display it as a separate visible line.
3. **Turnover stress:** recalculate total OpEx under turnover rate +10 pp (e.g., if base is 47.5%, run 57.5%).
4. **Interest-rate stress:** N/A at the OpEx level (this is a debt-service / NCF-after-DS sensitivity — out of scope here).
5. Document open questions for the user where data is missing or assumptions are soft.

---

## Output Format

The skill produces a human-readable Markdown report followed by the Structured Output JSON block. Template:

```markdown
# Annual Operating Budget — {Property Name}
## Budget Year: {YYYY}
## Status: COMPLETE | PARTIAL | FAILED
## Confidence: HIGH | MEDIUM | LOW

## 1. Revenue Assumptions

| Line | Budget {YYYY} | T-12 Actual | YoY % | Source/Basis |
|---|---|---|---|---|
| Gross Potential Rent (GPR) | $ | $ | % | Market rent × units × 12 (comp-set as-of {date}) |
| Loss-to-Lease | ($) | ($) | % | Projected from rent-roll roll-through |
| Concessions | ($) | ($) | % | Market condition: {balanced/competitive/oversupplied} → {months free} |
| Other Income | $ | $ | % | Ancillary lever detail |
| **Gross Potential Income (GPI)** | **$** | **$** | **%** | |
| Vacancy Loss | ($) | ($) | % | Physical vacancy assumption {%} |
| Bad Debt | ($) | ($) | % | Class {A/B/C} rate × GPI |
| **Effective Gross Income (EGI)** | **$** | **$** | **%** | per `underwriting-calc.md` §EGI |

## 2. OpEx Build by Category

| Line Item | Budget {YYYY} | T-12 Actual | $/unit/yr | YoY % | Basis / Escalator | Benchmark Range |
|---|---|---|---|---|---|---|
| Property Taxes | $ | $ | $ | % | Assessor notice / 5-yr avg / reassessment stress | {$/unit — cite KB} |
| Insurance | $ | $ | $ | % | Broker quote / +5% trend / cat stress | $400–$1,500 base per `_taxonomy-seed.md` §1 |
| Utilities — Water/Sewer | $ | $ | $ | % | +5% sub-line | $200–$500 per `_taxonomy-seed.md` §1 |
| Utilities — Gas | $ | $ | $ | % | Flat to −3% | $100–$600 per `_taxonomy-seed.md` §1 |
| Utilities — Electric | $ | $ | $ | % | +2–3% | $200–$800 per `_taxonomy-seed.md` §1 |
| Utilities — Trash | $ | $ | $ | % | Contract CPI | $80–$200 per `_taxonomy-seed.md` §1 |
| R&M | $ | $ | $ | % | T-12 × 2.5–3.5% + turnover spillover | $800–$1,400 per `_taxonomy-seed.md` §1 |
| Turnover / Make-Ready | $ | $ | $ | % | {rate}% × ${per-turn direct} × units | Direct $1,500–$3,000/turn per `multifamily-benchmarks.md` |
| Contract Services | $ | $ | $ | % | Contract schedule | $200–$600 per `_taxonomy-seed.md` §1 |
| Management Fee | $ | $ | $ | % | {%} of EGI | 4–8% per `underwriting-calc.md` |
| Payroll | $ | $ | $ | % | Staffing × grid + 3.5–4.0% | $500–$2,500 per `_taxonomy-seed.md` §1 |
| Administrative | $ | $ | $ | % | T-12 × 2.5–3.5% | $200–$600 per `_taxonomy-seed.md` §1 |
| Marketing | $ | $ | $ | % | T-12 × 2.5–3.5% | $100–$500 per `_taxonomy-seed.md` §1 |
| Professional Fees | $ | $ | $ | % | T-12 × 2.5–3.5% | $50–$200 per `_taxonomy-seed.md` §1 |
| Communications | $ | $ | $ | % | Contract CPI | $30–$120 per `_taxonomy-seed.md` §1 |
| Contingency (2–3%) | $ | — | $ | — | 2–3% of Total OpEx | research note methodology |
| **Total OpEx** | **$** | **$** | **$** | **%** | | National benchmark $8,657/unit NAA 2024 |

## 3. Seasonality Curve (Monthly Allocation)

| Line | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Annual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

(Verify: sum of monthly = annual for every line. Any line that fails this check is a build error.)

## 4. NOI Summary

| | $ | $/unit/yr | % of EGI |
|---|---|---|---|
| EGI | | | 100% |
| Total OpEx (excl. Replacement Reserves) | ($) | ($) | {OER}% |
| **NOI (AM convention)** | **$** | **$** | **%** |
| Replacement Reserves | ($) | ($) | |
| **NCF (Fannie/Freddie Form 4660)** | **$** | **$** | |

*Footnote reconciliation: NOI under `underwriting-calc.md` convention (reserves inside OpEx) = $**{alt}** — shown for interop with acquisition UW tooling.*

## 5. Assumptions & Sensitivities

- **Base case:** stated above.
- **Insurance +25% (single cat-event stress):** NOI impact $(X), OER impact (Y) pp.
- **Insurance +50% (market-hardening stress):** NOI impact $(X), OER impact (Y) pp.
- **Property tax reassessment stress:** (only if applicable) — reassessed value $, new tax line $, NOI delta $.
- **Turnover rate +10 pp:** Total OpEx impact $, NOI impact $.

## 6. Open Questions & Uncertainty

- (bulleted list of user-decision points and assumption-risk flags)
```

---

## Quality Checks

Before declaring the budget COMPLETE, verify ALL of the following:

- **Monthly sums reconcile:** Sum of monthly budgets = annual budget for every line item (enforced by the seasonality curve in Step 4).
- **EGI reconciles:** Budget EGI = Budget GPI − Budget Vacancy − Budget Credit Loss − Budget Concessions, per `knowledge/underwriting-calc.md` §Core Income Metrics.
- **NOI reconciles (AM convention):** Budget NOI = Budget EGI − Budget OpEx, where OpEx **excludes** Replacement Reserves per `research/asset-management/_taxonomy-seed.md` §1.
- **NCF reconciles:** Budget NCF = Budget NOI − Replacement Reserves, reported as a separate line (Fannie Mae Form 4660 / Freddie Ch. 23 convention).
- **OpEx sums to total:** Sum of all OpEx lines equals the Total OpEx figure, and every line has a cross-reference to `knowledge/asset-management-benchmarks.md` or `knowledge/multifamily-benchmarks.md` for a sanity-check range.
- **No blanket escalator applied:** No single inflation factor applied uniformly across lines (would violate research note Red Flag 1). Each line has its own escalator basis documented.
- **Concession sign convention honored:** Concessions REDUCE effective rent; any computed Effective Rent > Face Rent is a build error per `_taxonomy-seed.md` §4 adversarial check.
- **Management fee percentage check:** Management fee ÷ EGI is between 3% and 8% inclusive; otherwise flag per `_taxonomy-seed.md` §1 IREM benchmark.

---

## Red Flags & Dealbreakers

Each flag is specific, thresholded, and cites the source. The skill MUST surface these in the output `red_flags` array of the Structured Output and in Section 6 of the report.

- **Insurance under $400/unit/yr in T-12** — stale policy, imminent renewal shock. Below the lower-bound base range in `_taxonomy-seed.md` §1 ($400–$1,500). Action: obtain broker renewal quote before finalizing budget; assume +25% if quote lagging.
- **T-12 property taxes < market-cap reassessment estimate for a recently-acquired asset** — imminent reassessment shock. Applies if this is the first budget year post-acquisition AND prior-year tax / (purchase price × reassessment % × local mill rate) < 0.80. Action: apply the Property Tax Reassessment Stress Test from `research/asset-management/annual-operating-budget-builder-research.md`.
- **Management fee < 3% of EGI or > 8% of EGI** — misalignment with IREM benchmark per `_taxonomy-seed.md` §1. Below 3% signals related-party mis-pricing, unsustainable institutional concession, or self-management leakage into Payroll. Above 8% signals small-property / specialized-service premium — acceptable only with explicit justification.
- **Total OpEx budget > $11,000/unit/yr for non-Gateway, non-coastal Class B property** — management-inefficiency or aged-property signal per `knowledge/multifamily-benchmarks.md` §Red Flags and research note Red Flag 2. Review operating model.
- **Total OpEx budget < $4,500/unit/yr for any conventional stabilized property** — under-budgeting; signals deferred maintenance, owner neglect, or expense misclassification per research note Red Flag 3. Reconcile against benchmark floor.
- **Insurance increase > 15% YoY without cat-event or material property change** — claims history, loss-control failure, or insured-specific market hardening per research note Red Flag 4. Trigger broker-market check before accepting.
- **Blanket CPI escalator applied across all lines** — the single most common budget error per NAA 2024 guidance and research note Red Flag 1. Reject the budget and rebuild line-by-line.
- **Bad-debt rate set below class baseline** (e.g., < 0.5% Class A; < 1.0% Class B; < 1.5% Class C) — optimistic by historical class baseline per `knowledge/asset-management-benchmarks.md` §7. Justify or reset to class typical.

---

## When Data is Missing

- **No broker insurance renewal quote:** apply +5% to prior-year policy and carry a 5–10% contingency; note the open question and downgrade confidence to MEDIUM for the Insurance line specifically. If the property is cat-exposed and no quote is in hand, apply Stress Case 1 (+25%) per research note §Year-1 Insurance Renewal Stress Test and downgrade confidence to LOW for Insurance.
- **No assessor notice for next tax year:** apply the jurisdiction's 5-year historical growth rate to the prior-year bill. If post-acquisition, apply the reassessment stress test explicitly regardless of prior-year. Document the fallback basis in the output.
- **Incomplete rent roll (missing concession schedule, missing lease-end dates, or missing move-in dates):** fall back to T-12 collected rent as the revenue anchor, note the limitation, and flag LTL and concession forecasts as LOW confidence. Do NOT fabricate a rent-roll roll-through without source data.
- **No T-3 (only T-12 provided):** proceed on T-12 alone, but flag that the most-recent-trend stress cannot be applied; downgrade overall confidence by one level.
- **No staffing plan / wage grid:** apply T-12 payroll × BLS ECI (3.5–4.0%) with the caveat that structural staffing changes will not be captured. Flag MEDIUM confidence on the Payroll line.
- **No service-contract schedule:** apply T-12 contract line × 3% blended CPI and flag re-bid assumptions as an open question. Any contract expiring in the budget year without replacement terms is LOW confidence on that line.

---

## Confidence Scoring

| Level | Explicit Trigger Conditions |
|---|---|
| **HIGH** | ALL of: (a) T-12 and T-3 provided and reconciled; (b) broker insurance renewal quote received; (c) assessor notice received OR jurisdiction tax trajectory documented with ≥5-yr history; (d) current rent roll complete with concessions, lease-end dates, and move-in dates; (e) staffing plan and wage grid provided; (f) no line-item variance >25% vs benchmark range without documented rationale. |
| **MEDIUM** | T-12 provided and base assumptions documented, BUT at least one of: (a) insurance quote not yet received (trend-based fallback); (b) one or more OpEx lines rely on benchmark-range defaults rather than property-specific actuals; (c) T-3 not provided; (d) service-contract schedule partial. Budget is usable for directional planning but requires refinement when missing inputs arrive. |
| **LOW** | Any ONE of: (a) T-12 is > 90 days stale OR has major scope changes (ownership change, major renovation) that break run-rate comparability; (b) rent roll is absent or materially incomplete; (c) this is post-acquisition Year 1 and no reassessment stress test could be applied; (d) cat-exposed property with neither broker quote nor stress test applied; (e) benchmarks in `multifamily-benchmarks.md` / `asset-management-benchmarks.md` were substituted wholesale in lieu of property data on >30% of lines. |

---

## Related Knowledge Bases

- [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) — variance materiality, aging reserves, turnover decomposition, ancillary lifts, OpEx-KPI thresholds specific to AM post-acquisition operations.
- [Asset Management Reporting Standards](knowledge/asset-management-reporting-standards.md) — QAR/monthly-flash cadence, KPI checklist, report structure conventions (informs how the budget will be consumed against monthly variance packages).
- [Underwriting Calc](knowledge/underwriting-calc.md) — canonical formulas for GPR, GPI, EGI, NOI, LTL, Bad Debt, Management Fee, Occupancy. Cross-referenced; never redefined in this skill.
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — per-unit OpEx ranges by class, regional/vintage/COL/catastrophe multipliers, property tax by state, insurance cat-zone adjustments, occupancy benchmarks, rent-growth tiers.

---

## Research Basis

- [Annual Operating Budget Builder Research](research/asset-management/annual-operating-budget-builder-research.md) — empirical calibration: NAA/IREM 2024 $8,657/unit anchor, regional multipliers, insurance & property-tax stress-test methodology, turnover wide-definition economics, 2025–2026 moderation-not-inflation finding, budget-construction methodology decisions.
- [Asset Management Taxonomy Seed](research/asset-management/_taxonomy-seed.md) — canonical OpEx line-item taxonomy, KPI formulas, variance classification rules, rent definitions, AR aging — inherited verbatim by this skill.

---

## Structured Output

```json
{
  "skill": "annual-operating-budget-builder",
  "property": "{property_name}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "budget_year": 0,
    "budget_by_category": {},
    "total_opex": 0,
    "total_egi": 0,
    "total_noi": 0,
    "seasonality_curve": {},
    "assumptions": {}
  },
  "uncertainty_flags": [
    { "field_name": "", "reason": "estimated | assumed | missing_source | conflicting_sources", "impact": "" }
  ],
  "red_flags": [
    { "severity": "HIGH | MEDIUM | LOW", "description": "", "recommended_action": "" }
  ]
}
```
