# Quarterly Asset Review Writer

Synthesize all prior Asset Management skill outputs into a publication-ready institutional Quarterly Asset Review (QAR) memo for LP, asset committee, and IC pre-read consumption — following the 10-section institutional standard, the mandatory KPI checklist, and the pack's T-12 / T-3 / variance-classification conventions.

---

## When to Use This Skill

Use this skill at end-of-quarter when a stabilized (or value-add / lease-up) U.S. multifamily property needs its single institutional Quarterly Asset Review package prepared for:

- **LP reporting** — the 30-to-60-day-post-quarter deliverable that an institutional limited partner (pension fund, endowment, fund-of-funds, family office) consumes as its primary read on whether the business plan is on track between annual audited financials.
- **Asset committee prep** — internal GP asset-management committee review; the QAR is the canonical artifact that drives "hold / re-baseline / change course" decisions.
- **IC pre-meet** — when the asset is being considered for a hold/sell/refi decision or a major re-baseline, the QAR is the pre-read that anchors the IC conversation.
- **Quarter-end consolidation** — as the capstone deliverable that integrates all the pack's upstream asset-management work (budget, variance, collections, renewals, concessions, CapEx, NOI levers, hold/sell/refi) into one LP-ready narrative.

This skill is **not** a substitute for the monthly flash report (kept to 1–3 pages of headline KPIs) nor for annual audited financials (GAAP statements delivered 90–120 days after fiscal year-end). It is the narrative-plus-tables quarterly document that sits between them per `knowledge/asset-management-reporting-standards.md` §LP Report Cadence.

---

## What You'll Need to Provide

The QAR Writer is a **meta-synthesizer**: its canonical inputs are the Structured Output JSON blocks produced by the eight upstream Asset Management skills. Provide each that applies to the asset's current life-cycle stage; at minimum the variance, rent-collection, renewal, and CapEx outputs are required for any quarter. Missing upstream skills are handled per §When Data is Missing, below.

**Required upstream skill outputs (primary data feeds):**

1. `annual-operating-budget-builder` Structured Output — approved annual budget by line item, seasonality curve, EGI/OpEx/NOI anchor. Feeds Performance Snapshot, KPI Dashboard, Variance Commentary.
2. `monthly-variance-analyst` Structured Output — the variance package for the current quarter and YTD: classified variances (Timing / Permanent / One-Time), mixed-variance splits, commentary, forward-look. Feeds Variance Commentary section directly.
3. `rent-collection-delinquency-manager` Structured Output — total A/R, aging bands, past-due %, bad-debt reserve, chronic delinquent list, write-off recommendations. Feeds KPI Dashboard (bad-debt %) and Risks & Watch Items.
4. `renewal-decision-analyst` Structured Output — expiring-lease count, per-tenant renewal recommendations, retention vs turnover cost totals, portfolio retention strategy. Feeds Leasing & Occupancy, Forward-Look.
5. `lease-up-concessions-analyst` Structured Output — current occupancy, absorption velocity vs plan, face-vs-effective-rent gap, concession drag, stabilization date (original vs reforecast), burn-off phase. Feeds KPI Dashboard (concessions, occupancy), Leasing & Occupancy, Forward-Look. **Required for lease-up / value-add assets; optional for stabilized.**
6. `capex-value-add-execution-tracker` Structured Output — CapEx budget vs spent vs remaining, units renovated vs planned, rent-premium underwritten vs realized, yield on cost, schedule and cost variance, failure modes. Feeds Capital Projects Status directly.
7. `noi-improvement-analyst` Structured Output — baseline NOI, total estimated lift, prioritized lever list with lift / impact / difficulty / time-to-realize, quick wins, regulatory risk levers. Feeds Forward-Look and Risks & Watch Items.
8. `hold-sell-refi-analyst` Structured Output — IRR / EM to date, scenario-level projections (hold, refi-and-hold, sell-now, sell-at-stabilization), recommendation and rationale, disposition handoff package. Feeds Executive Summary (thesis status) and Financial Position / Forward-Look.

**Additional asset-level inputs the writer assembles directly:**

- Property name, unit count, class, market, year built, GP/LP structure, acquisition date and basis
- Original investment thesis (one sentence — value-add, core-plus, stabilized cash flow, merchant build, etc.) as stated at acquisition
- Reporting period (e.g., Q1 2026 quarter-end date)
- Current rent roll (point-in-time end of quarter) — for occupancy and rent snapshot
- T-12 and T-3 NOI (computed from actuals; T-12 always, T-3 only when diagnostic per pack convention)
- Debt schedule — balance, rate, maturity, DSCR, LTV/LTC, debt yield (point-in-time)
- Capital-account activity — capital calls, distributions, pref accrual, promote status, tier reconciliation (per ILPA Quarterly Reporting Standards)
- Submarket data — new supply, competing lease-up, rent trends, local economic indicators (1/2 to 1 page of Market Update only)
- ESG / DEI / resident-retention updates if available (quarterly narrative + YoY trend per `knowledge/asset-management-reporting-standards.md` §ESG/DEI)
- Operator storm-cost add-back policy (independent of variance One-Time classification per R2 resolution)
- Any mid-quarter event requiring a comparability break footnote (tax reassessment, insurance recategorization, major renovation, property-manager change)

---

## Mission

Produce a publication-ready institutional QAR memo that (a) states the original investment thesis and grades current progress in the Executive Summary, (b) presents the mandatory KPI dashboard in the LP-standard format (c) packages the variance analyst's classifications in REIT-style commentary per the pack's Timing / Permanent / One-Time taxonomy, (d) threads every upstream AM skill's findings into the appropriate 10-section location, (e) conforms to institutional length norms (8–12 pages stabilized / 15–20 pages value-add), (f) hits the pack's commentary-to-table ratios per section, and (g) enforces the "every body sentence references a specific number, threshold, named source, or named skill output" discipline so the memo reads as LP-grade and not generic.

---

## Strategy

### Step 1: Assemble the Upstream Skill Outputs

Gather each prior AM skill's Structured Output JSON block and load into the writer's working context. For each output, record (i) which section(s) of the QAR it feeds, (ii) whether the skill's confidence_level is HIGH / MEDIUM / LOW, and (iii) any red_flags the upstream skill raised. Red flags from upstream skills flow directly into the QAR's Risks & Watch Items section.

- `annual-operating-budget-builder` → feeds §2 Performance Snapshot (Budget column), §3 KPI Dashboard (OpEx / EGI / NOI anchor), §4 Variance Commentary (denominator for every variance %)
- `monthly-variance-analyst` → feeds §4 Variance Commentary directly (classification, mixed-variance splits, REIT-pattern narrative), contributes to §1 Executive Summary when any variance crosses 25% / $100k per `asset-management-reporting-standards.md` materiality escalation
- `rent-collection-delinquency-manager` → feeds §3 KPI Dashboard (bad-debt %, past-due %), §8 Risks & Watch Items (chronic delinquents, 90+ day concentration)
- `renewal-decision-analyst` → feeds §5 Leasing & Occupancy (retention rate, expiring-lease count, portfolio strategy), §10 Forward-Look (next-quarter renewal targets)
- `lease-up-concessions-analyst` → feeds §3 KPI Dashboard (physical occupancy, concession $ drag), §5 Leasing & Occupancy (absorption velocity vs plan, effective rent, burn-off phase), §10 Forward-Look (stabilization date reforecast)
- `capex-value-add-execution-tracker` → feeds §6 Capital Projects Status directly (budget vs actual, premium realization, yield on cost, schedule variance), §8 Risks & Watch Items (failure modes, cost overrun flags)
- `noi-improvement-analyst` → feeds §10 Forward-Look (prioritized levers, quick wins), §8 Risks & Watch Items (regulatory risk levers)
- `hold-sell-refi-analyst` → feeds §1 Executive Summary / Thesis Status (scenario-level recommendation anchors the thesis grade), §9 Financial Position (IRR to date, EM to date), §10 Forward-Look (recommendation rationale, disposition handoff if triggered)

### Step 2: Set the Ground Rules at the Top of the Memo

Before drafting, fix:

- Asset status: **Stabilized** / **Value-add (in business plan)** / **Lease-up / development**. Determines length target (8–12 pp vs 15–20 pp per `asset-management-reporting-standards.md` §Length Norms) and whether Performance Snapshot must flag the asset is not stabilized.
- Reporting period (e.g., Q1 2026, quarter-end 2026-03-31)
- Reporting lag (target: 30–60 days post-quarter-end per LP cadence convention)
- Materiality floor for variance callouts: inherited from the upstream variance analyst (per `knowledge/asset-management-benchmarks.md` §1 / `_taxonomy-seed.md` §3); restate at top.
- Sign convention (favorable = higher revenue / lower expense), basis (cash vs accrual), T-3 overlay trigger (show only when T-3 annualized diverges from T-12 by >5% per pack convention).

### Step 3: Draft Section 1 — Executive Summary / Thesis Status

Written last; read first. One-half to one page. Per `knowledge/asset-management-reporting-standards.md` §QAR Structure:

- State the original investment thesis in one sentence (quoted from acquisition memo or sponsor IC approval).
- Grade current thesis status — **on-track / ahead / behind / materially off-track** — anchored to the `hold-sell-refi-analyst` recommendation and the variance analyst's permanent-variance total.
- Call out the 3–5 most important quarter-over-quarter changes (NOI growth, occupancy, variance classification shifts, CapEx milestones, refinance progress, concession environment).
- If any upstream variance crosses 25% or $100k OR any red flag from an upstream skill is severity HIGH → surface here per `asset-management-reporting-standards.md` §Materiality Thresholds escalation tier.
- Commentary/table mix: 90% narrative / 10% table (per `asset-management-reporting-standards.md` §Commentary-to-Table Ratio).

### Step 4: Draft Section 2 — Performance Snapshot

One page, tabular. Columns: Q actual | Q budget | Q prior-year actual. Rows: the 6–10 headline KPIs (physical occupancy, economic occupancy, effective rent, NOI, NOI growth YoY, revenue growth YoY, expense growth YoY, bad debt %, operating expense ratio, DSCR). Commentary/table mix: 10% narrative / 90% table.

For value-add or lease-up assets, footnote that the asset is not stabilized and reconcile to the business-plan ramp schedule, not a steady-state budget, per R9 edge-case guidance.

### Step 5: Draft Section 3 — KPI Dashboard

One to two pages, deeper tabular. Same KPIs as snapshot plus:

- **T-12 NOI** — always shown (per pack convention, "T-12 always")
- **T-3 NOI annualized** — shown only when T-3 diverges from T-12 by >5% per `asset-management-reporting-standards.md` §T-3 vs T-12 Bridging
- **YTD view** for each KPI
- Occupancy, rent, and NOI broken out by unit type if meaningful

**Mandatory KPIs that must appear** (per `asset-management-reporting-standards.md` §Mandatory KPI Checklist):

1. Physical Occupancy (point-in-time + quarterly average)
2. Economic Occupancy (quarterly average)
3. NOI (Q / YTD / TTM — three columns: actual vs budget vs prior-year)
4. NOI Growth YoY
5. Revenue Growth YoY
6. Expense Growth YoY
7. Effective Rent Growth / Blended Lease Trade-Out (new-lease change %, renewal change %, blended change %)
8. Retention Rate
9. Turnover Rate (annualized + TTM)
10. Bad Debt % of GPR (quarterly + TTM)
11. Operating Expense Ratio (quarterly + TTM)
12. Concessions ($ or % of GPR)

**If levered, also:**

- DSCR (point-in-time + TTM)
- LTV (point-in-time)
- LTC (point-in-time)
- Debt Yield (point-in-time + TTM)

All KPI formulas are by-reference to `_taxonomy-seed.md §2` and `knowledge/underwriting-calc.md` — **do not redefine in the memo**. Commentary/table mix: 20% narrative / 80% table.

### Step 6: Draft Section 4 — Variance Commentary

One to three pages for a healthy quarter; four to six pages for a variance-heavy quarter. Anything over six pages is throat-clearing per `asset-management-reporting-standards.md` §Commentary Section Length Convention — tighten.

Consume the `monthly-variance-analyst` Structured Output directly. For each material variance (variance that crossed the materiality gate in the variance analyst):

- Present in the pack's standard column set: Line Item | Budget | Actual | Variance ($) | Variance (%) | Classification (Timing/Permanent/One-Time) | Driver
- Write REIT-pattern narrative: **topic → driver → quantification ($ and %) → classification → forward-look**
- For mixed variances, split into Timing and Permanent components per `_taxonomy-seed.md` §3 Mixed-Variance Rule

**Normalized NOI footnote.** Present both GAAP / cash NOI and a "normalized" NOI that removes One-Time items. Bridge table shows: As-Reported NOI → less One-Time items (storm costs, settlements, refunds) → Normalized NOI. This is the private-GP equivalent of the public REIT core-FFO bridge (do not import "FFO" into the QAR — AVB/EQR/Camden FFO conventions are a *format* exemplar, not content per R9 resolution). Commentary/table mix: 70% narrative / 30% table.

### Step 7: Draft Section 5 — Leasing & Occupancy Performance

One to two pages. Consume the `renewal-decision-analyst` + `lease-up-concessions-analyst` outputs.

- **New-lease change %, renewal change %, blended lease trade-out %** (the EQR five-way same-store decomposition adapted to single-asset scale per R9)
- **Retention rate** with driver narrative (price, service, community programming per R9 ESG/resident-retention convention)
- **Turnover rate** (annualized)
- **Days-to-lease and traffic counts** where available
- **Concessions environment** — effective vs face rent gap, concession $ drag, burn-off phase (heavy / tapering / normal from lease-up analyst)
- **For lease-up / value-add:** absorption velocity (units/month), velocity vs plan, stabilization date reforecast from `lease-up-concessions-analyst`

Commentary/table mix: 50% narrative / 50% table.

### Step 8: Draft Section 6 — Capital Projects Status

One-half to two pages. Consume the `capex-value-add-execution-tracker` Structured Output directly.

- Per-project table: project name | budget | spent-to-date | remaining | % complete | schedule variance (days) | cost variance (%) | units renovated | units planned | rent premium underwritten | rent premium realized | premium-realization %
- Aggregate yield-on-cost for the CapEx program
- Schedule-to-complete narrative per active project
- Surface any failure modes flagged by the CapEx tracker (cost overrun, schedule slip, premium-realization gap) → also feed to §8 Risks

Commentary/table mix: 30% narrative / 70% table.

### Step 9: Draft Section 7 — Market Update

One-half to one page. This is **not** a market study; it is an operating-context update. Coverage:

- Submarket new supply delivered and in lease-up (competing product)
- Submarket rent trend (YoY change from Yardi Matrix / CoStar / ALN if available)
- Local economic indicators relevant to the asset (employment, major employer moves, transit)
- Reference the `lease-up-concessions-analyst` output's submarket concession read if available

Commentary/table mix: 90% narrative / 10% table.

### Step 10: Draft Section 8 — Risks & Watch Items

One-half to one page. Bulleted narrative. Sources:

- Upstream skill red_flags arrays — every HIGH-severity red flag from any of the 8 input skills surfaces here
- Chronic delinquent concentration from `rent-collection-delinquency-manager` (90+ day concentration, tenant concentration risk)
- CapEx failure modes from `capex-value-add-execution-tracker`
- Regulatory risk levers from `noi-improvement-analyst` (rent-control exposure, tax-abatement expiration, insurance market hardening)
- Debt-maturity stress if loan matures within 12 months OR DSCR <1.15x on a covenant-limited loan OR lockbox triggered — must also appear in §1 Executive Summary and §9 Financial Position per R9 edge-case guidance
- Insurance renewal or tax reassessment mid-quarter, flagged even if financial impact lands later
- Property-manager change or replacement in-quarter (transition cost, continuity plan, data-integrity gaps)
- ESG / climate catastrophe exposure updates

Commentary/table mix: 95% narrative / 5% table.

### Step 11: Draft Section 9 — Financial Position

One page, tabular. Per ILPA Quarterly Reporting Standards.

- **Debt summary:** balance, rate (fixed/floating + spread), maturity date, DSCR (point-in-time + TTM), LTV, LTC, debt yield
- **Cash position** — operating cash, reserves balance (replacement reserve, tax escrow, insurance escrow)
- **Capital-call activity in the quarter** — date, amount, purpose (per ILPA standardized capital-call notice template)
- **Distributions in the quarter** — date, amount, source (per ILPA standardized distribution notice template)
- **Waterfall transparency** — pref accrual balance (per tranche if multiple), catch-up status, promote status, clawback exposure (footnote if applicable), tier-by-tier distribution reconciliation
- **Since-inception** — paid-in capital, DPI, RVPI, TVPI, Net IRR, Gross IRR (per ANREV/INREV/NCREIF global definition)

Pull IRR / EM to date from `hold-sell-refi-analyst` Structured Output. Commentary/table mix: 20% narrative / 80% table.

### Step 12: Draft Section 10 — Forward-Look / Next Quarter Plan

One-half page. Narrative only (0% table / 100% narrative).

- Next-quarter leasing targets (from `renewal-decision-analyst` portfolio strategy + `lease-up-concessions-analyst` reforecast)
- CapEx milestones expected (from `capex-value-add-execution-tracker`)
- NOI-lever execution plan — quick wins from `noi-improvement-analyst` targeted for the next quarter
- Decision points — refi trigger, hold/sell review, thesis re-baseline (anchor to `hold-sell-refi-analyst` recommendation and rationale)
- Expected distribution activity
- Stabilization date update if lease-up / value-add

### Step 13: Enforce Commentary-to-Table Ratios and Length

Measure the finished draft against `asset-management-reporting-standards.md` §Commentary-to-Table Ratio (section-by-section target table) and §Length Norms. If the draft exceeds 12 pages (stabilized) or 20 pages (value-add / lease-up), tighten. If shorter than 6 pages (stabilized) or 12 pages (value-add), the memo is under-disclosed.

### Step 14: Enforce the "Every Body Sentence" Rule

Per R9 institutional norm and the pack's LP-grade standard: **every body-paragraph sentence in the memo must reference a specific number, threshold, named source, or named upstream skill output.** Target ≥90% adherence. Generic sentences ("the property is performing well", "market conditions are supportive") are failure modes and must be rewritten with a number or a named source. Introductions and section headers are exempt.

### Step 15: Enforce the T-3 / T-12 / T-1 Convention

Per pack convention ("T-12 always, T-3 when diagnostic, T-1 never"). The KPI Dashboard shows T-12 always. T-3 overlay shows only when T-3 annualized NOI diverges from T-12 by >5% or in value-add / lease-up situations where T-12 still reflects pre-business-plan performance. T-1 (single-month annualized) must never appear at the QAR level — it is properly confined to the monthly flash report.

### Step 16: Final Self-Review Pass

Apply the §Quality Checks list below and run the R9 reviewer-checklist discipline. Specifically: confirm every mandatory KPI is present, every variance classification label conforms to the taxonomy, every upstream skill's red flags have been either surfaced in §8 Risks or explicitly marked as below the reporting materiality floor.

---

## Output Format

```markdown
# Quarterly Asset Review — {Property Name}
## Period: {e.g. Q1 2026, quarter-end YYYY-MM-DD}
## Report Date: {YYYY-MM-DD}
## Asset Status: Stabilized | Value-Add (in business plan) | Lease-up / Development
## Thesis Grade: ON TRACK | AHEAD | BEHIND | MATERIALLY OFF TRACK

---

### 1. Executive Summary / Thesis Status

**Original investment thesis (as-of acquisition):** "{one-sentence thesis — e.g., `Value-add garden-style asset in {market} with underwritten 24-month renovation program and 28% rent premium thesis supported by comp-set mark-to-market`}"

**Current grade:** {grade} — {one-line justification anchored to `hold-sell-refi-analyst` recommendation}

**Top 3–5 quarter-over-quarter changes:**
- {change 1 — quantified in $ and %, referencing upstream skill output}
- {change 2 — quantified}
- {change 3 — quantified}

**Material escalations (variance > 25% or > $100k, or HIGH-severity upstream red flag):**
- {escalation or "None this quarter"}

---

### 2. Performance Snapshot

| KPI | Q Actual | Q Budget | Q Prior-Year | Δ vs Budget | Δ vs Prior Year |
|---|---|---|---|---|---|
| Physical Occupancy | | | | | |
| Economic Occupancy | | | | | |
| Effective Rent ($/unit/mo) | | | | | |
| NOI ($) | | | | | |
| NOI Growth YoY (%) | | | | | |
| Revenue Growth YoY (%) | | | | | |
| Expense Growth YoY (%) | | | | | |
| Bad Debt % of GPR | | | | | |
| Operating Expense Ratio | | | | | |
| DSCR (if levered) | | | | | |

*Footnote if asset is not stabilized: business-plan ramp schedule referenced, not steady-state budget.*

---

### 3. KPI Dashboard

| KPI | Q Actual | Q Budget | YTD Actual | YTD Budget | T-12 | T-3 (if diagnostic) | Source |
|---|---|---|---|---|---|---|---|
| Physical Occupancy | | | | | | | `_taxonomy-seed.md` §2 |
| Economic Occupancy | | | | | | | `_taxonomy-seed.md` §2 |
| NOI | | | | | | | `_taxonomy-seed.md` §2 |
| NOI Growth YoY | | | | | | | REIT supplementals |
| Revenue Growth YoY | | | | | | | REIT supplementals |
| Expense Growth YoY | | | | | | | REIT supplementals |
| New-Lease Change % | | | | | | | `_taxonomy-seed.md` §4 |
| Renewal Change % | | | | | | | `_taxonomy-seed.md` §4 |
| Blended Change % | | | | | | | `_taxonomy-seed.md` §4 |
| Retention Rate | | | | | | | `multifamily-benchmarks.md` |
| Turnover Rate (annualized) | | | | | | | `multifamily-benchmarks.md` |
| Bad Debt % of GPR | | | | | | | `_taxonomy-seed.md` §2 |
| Operating Expense Ratio | | | | | | | `multifamily-benchmarks.md` |
| Concessions ($ or % of GPR) | | | | | | | `_taxonomy-seed.md` §2 |
| DSCR (if levered) | | | | | | | `underwriting-calc.md` |
| LTV (if levered) | | | | | | | `multifamily-benchmarks.md` |
| Debt Yield (if levered) | | | | | | | `underwriting-calc.md` |

*T-3 column populated only when T-3 annualized NOI diverges from T-12 by >5% per pack "T-12 always, T-3 diagnostic, T-1 never" convention.*

---

### 4. Variance Commentary

**Reporting basis:** {cash / accrual}. **Sign convention:** favorable = higher revenue or lower expense than budget. **Materiality floor:** lesser of 10% of budgeted line item OR $25,000 absolute (per `_taxonomy-seed.md` §3; upstream variance analyst materiality inherited).

| Line Item | Budget | Actual | Variance ($) | Variance (%) | Classification | Driver |
|---|---|---|---|---|---|---|
| {line} | | | | | Timing / Permanent / One-Time | {3–8 word cause} |
| ... | | | | | | |

**Material variance narrative (topic → driver → quantification → classification → forward-look):**

- **{Line Item 1}:** {narrative in REIT pattern}
- **{Line Item 2}:** {narrative}
- ...

**Mixed-variance splits (if any):**
- **{Line Item}:** Total variance ${}; Timing component ${} ({reason}); Permanent component ${} ({reason}).

**Normalized NOI bridge:**

| Item | $ |
|---|---|
| As-reported NOI | |
| Less: One-Time items (storm costs, settlements, refunds) | |
| **Normalized NOI** | |

---

### 5. Leasing & Occupancy Performance

| Metric | Quarter | Trend vs Prior Quarter |
|---|---|---|
| New-lease change % | | |
| Renewal change % | | |
| Blended change % | | |
| Retention rate | | |
| Turnover rate (annualized) | | |
| Days-to-lease (avg) | | |
| Traffic count (quarterly) | | |
| Concession $ drag (monthly) | | |
| Effective rent vs face rent gap | | |

**Retention driver narrative:** {price / service / community programming — per `renewal-decision-analyst` portfolio strategy}

**Lease-up commentary (if applicable):** absorption velocity {units/month}, velocity vs plan {%}, burn-off phase {heavy/tapering/normal}, stabilization date reforecast {date} vs original {date} — per `lease-up-concessions-analyst`.

---

### 6. Capital Projects Status

| Project | Budget | Spent YTD | Remaining | % Complete | Schedule Var (days) | Cost Var (%) | Units Renovated | Rent Prem Underwritten | Rent Prem Realized | Realization % |
|---|---|---|---|---|---|---|---|---|---|---|
| {project} | | | | | | | | | | |
| ... | | | | | | | | | | |

**Aggregate yield on cost:** {%}

**Schedule-to-complete narrative:** {per-project status anchored to `capex-value-add-execution-tracker` output}

**Failure modes flagged:** {cost overrun / schedule slip / premium-realization gap — surfaces to §8 Risks}

---

### 7. Market Update

{1/2 to 1 page narrative — submarket new supply, competing lease-up, rent trend, local economic indicators. Short — not a market study.}

---

### 8. Risks & Watch Items

- {Risk 1 — surfaced from upstream skill red_flags array, chronic delinquent concentration, CapEx failure mode, regulatory lever, etc.}
- {Risk 2}
- {Risk 3}

**Debt-maturity stress (if applicable):** {surface here AND in §1 Executive Summary AND in §9 Financial Position if maturity <12 months OR DSCR <1.15x OR lockbox triggered}

---

### 9. Financial Position

| Item | Value |
|---|---|
| Loan balance | |
| Interest rate | |
| Maturity date | |
| DSCR (point-in-time) | |
| DSCR (TTM) | |
| LTV | |
| LTC | |
| Debt yield | |
| Operating cash | |
| Replacement reserve balance | |
| Tax / insurance escrow | |
| IRR to date (from `hold-sell-refi-analyst`) | |
| Equity multiple to date | |

**Capital-call activity this quarter:**
- {date, amount, purpose} — per ILPA standardized notice template

**Distributions this quarter:**
- {date, amount, source} — per ILPA standardized notice template

**Waterfall transparency:**
- Pref accrual: ${} ({% of LP capital})
- Catch-up status: {triggered / not triggered}; paid: ${}
- Promote status: cumulative ${}; current quarter tier hit: {tier}
- Clawback exposure: {footnote if applicable}
- Tier-by-tier distribution reconciliation: {one row per distribution}

**Since-inception (per ANREV/INREV/NCREIF global definition):**
- Paid-in capital: ${}
- DPI: {x}
- RVPI: {x}
- TVPI: {x}
- Net IRR: {%}
- Gross IRR: {%}

---

### 10. Forward-Look / Next Quarter Plan

{1/2 page narrative — next-quarter leasing targets, CapEx milestones, NOI-lever execution plan, decision points (refi trigger / hold-sell review / re-baseline), expected distribution activity, stabilization date update if lease-up.}

---

### Confidence Level

HIGH | MEDIUM | LOW

### Consumed Upstream Skill Outputs

- `annual-operating-budget-builder` — {status / confidence}
- `monthly-variance-analyst` — {status / confidence}
- `rent-collection-delinquency-manager` — {status / confidence}
- `renewal-decision-analyst` — {status / confidence}
- `lease-up-concessions-analyst` — {status / confidence / or "not applicable — stabilized asset"}
- `capex-value-add-execution-tracker` — {status / confidence}
- `noi-improvement-analyst` — {status / confidence}
- `hold-sell-refi-analyst` — {status / confidence}
```

---

## Quality Checks

- **Every body sentence references a specific number, threshold, named source, or named skill output.** Target ≥90% adherence per KB3 convention. Generic sentences ("performance was solid", "market remains supportive") must be rewritten with a quantified anchor or removed. Headers and section intros exempt.
- **All 12 mandatory KPIs from `asset-management-reporting-standards.md` §Mandatory KPI Checklist appear in the KPI Dashboard.** Levered assets additionally show DSCR, LTV, LTC, Debt Yield. Missing any mandatory KPI = memo fails institutional floor.
- **Variance classifications use only the three `_taxonomy-seed.md` §3 buckets** (Timing / Permanent / One-Time). Other labels ("favorable / unfavorable only", "controllable / non-controllable", "above / below the line") are not substitutes and must not appear in the Classification column.
- **T-12 NOI always shown; T-3 overlay shown only when T-3 and T-12 diverge >5% or asset is value-add / lease-up; T-1 never appears at the QAR level** per the pack "T-12 always, T-3 diagnostic, T-1 never" convention (R9 / `asset-management-reporting-standards.md` §T-3 vs T-12 Bridging).
- **Every upstream skill output consumed is credited in the "Consumed Upstream Skill Outputs" list at the end of the memo.** Skills whose outputs were not available must be listed with "not provided — see When Data is Missing" flag.
- **Commentary-to-table ratios per section conform to `asset-management-reporting-standards.md` §Commentary-to-Table Ratio** (Executive Summary 90/10 narrative/table; Performance Snapshot 10/90; KPI Dashboard 20/80; Variance Commentary 70/30; Leasing 50/50; Capital Projects 30/70; Market Update 90/10; Risks 95/5; Financial Position 20/80; Forward-Look 100/0). Document overall ~50/50.
- **Length conforms to §Length Norms:** 8–12 pages stabilized; 15–20 pages value-add / lease-up. <6 pp = under-disclosure; >25 pp = over-disclosure (often burying the lede).
- **Every material variance in the variance table has a classification label, a 3–8 word plain-English driver, and narrative commentary in the REIT pattern (topic → driver → quantification $ and % → classification → forward-look).**
- **Normalized NOI bridge present when any One-Time variance exists** in the variance package — strips One-Time items from the reported NOI figure. Storm-cost add-back policy stated; classification as One-Time is independent of the operator's FFO/NOI add-back policy per R2 resolution.
- **Upstream red_flags surfaced to §8 Risks & Watch Items.** Every HIGH-severity red flag from any of the 8 consumed skill outputs appears in §8 (or is explicitly reclassified as sub-materiality with justification). MEDIUM red flags appear in §8 when they would materially affect the LP's view of the forward quarter.
- **Capital-call and distribution activity uses ILPA standardized notice formats** (date, amount, purpose / source) per ILPA Quarterly Reporting Standards — even when the narrative is custom.
- **ESG / DEI / resident-retention disclosure present** at quarterly narrative level (full metric refresh reserved for Q4 / annual per R9) — omission entirely is out of step with 2026 institutional norms per ILPA Diversity in Action and PRI Real Estate Module.

---

## Red Flags & Dealbreakers

- **Any mandatory KPI from the §Mandatory KPI Checklist missing → memo fails institutional LP floor.** Do not ship. Either populate the KPI or state the data gap explicitly with expected remediation date; never silently omit.
- **Upstream variance analyst reports a Permanent variance > 10% of an annual line item → ad-hoc reforecast trigger AND Executive Summary mention required** (per `knowledge/asset-management-benchmarks.md` §1 Reforecast Trigger Table). The QAR that buries a reforecast trigger inside §4 only is a reporting failure.
- **Any upstream skill raises a HIGH-severity red flag → must appear in §8 Risks & Watch Items and, if affecting forward guidance or thesis, also in §1 Executive Summary.** Omission = material reporting failure per R9 edge-case guidance.
- **Variance > 25% or > $100k on any line item → Executive Summary escalation required** per `asset-management-reporting-standards.md` §Materiality Thresholds in Reports. Bury-in-commentary-only = failure.
- **DSCR stress (< 1.15x on a covenant-limited loan) OR loan maturity within 12 months OR lockbox / cash-management sweep triggered → must surface in §1 Executive Summary, §8 Risks, AND §9 Financial Position.** Institutional LPs treat silent burial of maturity or covenant stress as a material reporting failure per R9 edge-case guidance.
- **Sponsor-affiliated service provider fees (management, construction management, leasing commissions) buried inside generic OpEx lines** rather than separately disclosed → ILPA fee-transparency red flag; triggers LPAC-level follow-up. Must be broken out in §9 Financial Position or a dedicated affiliated-fees footnote.
- **One-size-fits-all template commentary repeated across multiple assets in a portfolio** → institutional LPs read across; boilerplate commentary erodes credibility and re-up probability. Narrative must be asset-specific.
- **Over-length driven by underperformance** — when a quarter underperforms, expanding the Executive Summary signals burying the lede. Correct response: tighten structure, state underperformance cleanly in §1, work through cause and response in §4 and §8.
- **ESG / DEI / resident-retention completely omitted** → out of step with 2026 institutional norms (ILPA Diversity in Action, PRI Real Estate Module). Flag and request operator input; do not ship with section silently empty.
- **Refi or disposition activity in-quarter buried inside regular §9 Financial Position** rather than broken out as a separate "Capital Transactions" subsection → material reporting failure per R9.

---

## When Data is Missing

- **`monthly-variance-analyst` output missing.** Variance Commentary is the load-bearing narrative section of a QAR; its absence is material. Pull raw variance from T-12 actuals + original annual budget and classify Timing / Permanent / One-Time at the reporting layer per `_taxonomy-seed.md` §3 and `asset-management-reporting-standards.md` §Variance Classification. Label the variance commentary "produced at QAR writer layer — variance analyst pre-read not available." Confidence drops to MEDIUM.
- **`annual-operating-budget-builder` output missing.** Performance Snapshot and KPI Dashboard require a Budget column. If prior-year actuals are available, substitute "Prior-Year Actual" as the comparison column and clearly re-label; if not, report actuals-only and mark the memo "pre-budget approval — indicative only." Confidence drops to LOW.
- **`rent-collection-delinquency-manager` output missing.** Bad debt % and past-due % still populate from raw A/R and GPI in the property accounting system. Chronic delinquent and write-off commentary absent from §8 Risks — note the gap explicitly. Confidence: MEDIUM on Risks section.
- **`renewal-decision-analyst` output missing.** Retention rate still populates from lease expirations ÷ renewals. Portfolio retention-strategy narrative replaced with a single-line "renewal strategy pending" flag in §5 Leasing & Occupancy and §10 Forward-Look. Confidence: MEDIUM on those sections.
- **`lease-up-concessions-analyst` output missing AND asset is stabilized.** No action — this skill is conditional on lease-up / value-add status. Confidence unchanged.
- **`lease-up-concessions-analyst` output missing AND asset is lease-up / value-add.** Critical gap — lease-up KPIs (absorption velocity, stabilization reforecast, concession $ drag, burn-off phase) cannot be populated. Substitute raw rent-roll-derived physical occupancy and lease-signing count; mark stabilization reforecast as "pending lease-up analyst refresh." Confidence: LOW on §5 Leasing & §10 Forward-Look.
- **`capex-value-add-execution-tracker` output missing AND active CapEx program.** §6 Capital Projects Status narrative-only; populate a simplified project table from the property accounting system (budget, spent-to-date, remaining) without premium-realization metrics. Flag as "CapEx tracker pre-read not available." Confidence: LOW on §6.
- **`noi-improvement-analyst` output missing.** §10 Forward-Look loses the prioritized-lever list. Substitute sponsor-provided next-quarter objectives narrative; flag the absence. Confidence: MEDIUM on §10.
- **`hold-sell-refi-analyst` output missing.** §1 Executive Summary thesis-grade anchor lost. Substitute sponsor-stated thesis grade (on-track / ahead / behind / materially off-track) with explicit "analyst pre-read not available." IRR / EM to-date in §9 Financial Position pulled directly from fund accounting. Confidence: MEDIUM on §1.
- **Submarket / market-update data not provided.** Run §7 Market Update as a one-paragraph "submarket conditions pending refresh" stub rather than fabricating. Flag as data gap. Confidence: MEDIUM on §7.
- **ESG / DEI / resident-retention data not provided.** Populate what is available (retention rate from renewal analyst; concessions from lease-up analyst) and flag full ESG refresh as scheduled for Q4 / annual per pack convention. Confidence unchanged if stabilized; flagged if lease-up/value-add where ESG is more consumed.
- **Capital-account activity not provided.** Cannot publish §9 waterfall and capital-call/distribution sections without fund-accounting data. Hold the memo until data arrives, or ship a partial memo labeled "operating-only — capital-account section to follow under separate cover" per ILPA guidance.

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | All 8 upstream AM skill outputs provided with HIGH or MEDIUM confidence; variance analyst output HIGH; all mandatory KPIs populated; T-12 anchored to audited or reviewed actuals; capital-account activity complete; no upstream HIGH-severity red flags unmitigated. |
| MEDIUM | 1–2 upstream skill outputs missing OR at LOW confidence; one or more data gaps flagged in §When Data is Missing; one HIGH-severity upstream red flag surfaced and addressed in §8; variance classifications defensible but one or more material variances still awaiting 2-month trailing confirmation. |
| LOW | 3+ upstream skill outputs missing OR variance analyst missing entirely; budget not provided (pre-budget-approval indicative memo); multiple data gaps flagged; material comparability break (tax reassessment, renovation, property-manager change) mid-quarter not yet reconciled; or insufficient fund-accounting data to populate ILPA-standard §9. Memo labeled "indicative — final QAR to follow" where appropriate. |

---

## Related Knowledge Bases

- [Asset Management Reporting Standards](knowledge/asset-management-reporting-standards.md) — KB3 — primary source for QAR 10-section structure, mandatory KPI checklist, length norms, commentary-to-table ratios, T-3 vs T-12 bridging rules, variance packaging conventions, capital-call / distribution reporting, waterfall transparency, ESG/DEI/resident-retention reporting, edge cases
- [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) — KB1 — materiality thresholds, reforecast triggers, variance benchmarks used to calibrate Executive Summary escalations
- [Underwriting Calculations](knowledge/underwriting-calc.md) — DSCR, Debt Yield, Cap Rate, IRR, NOI, EGI formulas referenced (by reference only) in the KPI Dashboard and Financial Position sections
- [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) — occupancy, expense ratio, turnover, bad debt, DSCR, LTV / LTC benchmark ranges referenced in KPI Dashboard and Risks & Watch Items

## Research Basis

- [Quarterly Asset Review Writer Research](research/asset-management/quarterly-asset-review-writer-research.md) — R9 — primary research note; sourced from ILPA Reporting Template, ILPA Quarterly Reporting Standards PDF, NCREIF-PREA Reporting Standards, NCREIF NPI Methodology, AvalonBay / Equity Residential / Camden Q4 2024 Earnings Supplementals (SEC primary filings), ANREV/INREV/NCREIF Global Definitions Database, SEC Reg S-K Item 303 MD&A, ILPA Diversity in Action, PRI Real Estate Module, PREA Member Guidance, Nareit Supplemental Guide, GRESB Real Estate Assessment (13 Tier-1/Tier-2 sources)
- [Asset Management Taxonomy Seed](research/asset-management/_taxonomy-seed.md) — §2 KPI formulas (referenced, not redefined); §3 Timing / Permanent / One-Time decision rules and materiality floor inherited at the reporting layer; §4 rent definitions

---

## Structured Output

```json
{
  "skill": "quarterly-asset-review-writer",
  "property": "{property_name}",
  "period": "{e.g. Q1 2026}",
  "analysis_date": "{YYYY-MM-DD}",
  "status": "COMPLETE | PARTIAL | FAILED",
  "confidence_level": "HIGH | MEDIUM | LOW",
  "findings": {
    "thesis_status": "on_track | at_risk | exceeded | re_baselined",
    "executive_summary": "",
    "kpi_dashboard": {
      "physical_occupancy_pct": 0,
      "economic_occupancy_pct": 0,
      "noi": 0,
      "noi_growth_yoy_pct": 0,
      "rent_growth_yoy_pct": 0,
      "bad_debt_pct": 0,
      "turnover_rate_pct": 0,
      "retention_rate_pct": 0,
      "expense_ratio_pct": 0,
      "dscr": 0,
      "ltv_pct": 0
    },
    "top_variance_drivers": [],
    "leasing_occupancy_commentary": "",
    "capital_projects_status": "",
    "market_update": "",
    "risks_and_watch_items": [],
    "financial_position": {},
    "forward_look": "",
    "consumed_skill_outputs": []
  },
  "uncertainty_flags": [
    { "field_name": "", "reason": "estimated | assumed | missing_source | conflicting_sources", "impact": "" }
  ],
  "red_flags": [
    { "severity": "HIGH | MEDIUM | LOW", "description": "", "recommended_action": "" }
  ]
}
```
