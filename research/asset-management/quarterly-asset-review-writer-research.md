# Quarterly Asset Review Writer Research

## Purpose

- Supports `skills/asset-management/quarterly-asset-review-writer.md` (future) — the pack skill that drafts an institutional Quarterly Asset Review (QAR) / Quarterly Owner Report (QOR) narrative for a stabilized multifamily property
- Intended for asset managers, GP reporting teams, and LP-facing investor-relations analysts who package quarterly operating results for institutional limited partners (pension funds, endowments, family offices, fund-of-funds)
- Scope is **institutional reporting standards only** — the structural conventions, KPI checklist, cadence rules, and format norms used by sophisticated LPs. Variance *methodology* (how to compute the analytical classification) sits in the R2 research note; this note covers how a reporting writer **packages** variances for LP consumption
- Inherits definitions, KPI formulas, and variance buckets from `research/asset-management/_taxonomy-seed.md` — this note does not redefine them, only describes how they flow into the LP narrative

## U.S.-Only Assumptions

- Geography is the United States; conventions follow ILPA (global, US-dominant), NCREIF (US), and US public REIT quarterly supplementals (AVB, EQR, CPT, MAA, ESS, UDR) as format exemplars
- Property type is conventional stabilized multifamily (5+ unit), market-rate, not affordable / LIHTC (which carries additional HUD and allocating-agency disclosure overlay)
- Reader / audience is an institutional LP: a pension-fund analyst, endowment real-assets officer, or fund-of-funds monitor who reads 40–80 quarterly GP reports per quarter and expects a consistent, scannable structure
- Entity context is a joint-venture or fund-level investment (GP sponsor + institutional LP) with a standard promote waterfall (return of capital → pref → GP catch-up → promote split), not an all-cash single-family-office deal where reporting is bespoke
- Reporting is for **unaudited quarterly operating performance**, not audited annual financial statements (which carry GAAP / ASC 842 / fair-value disclosure obligations beyond the scope of a QAR narrative)

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|--------|-----------|-----|--------------|-------------|-------------|-------|
| ILPA Reporting Template (Quarterly Reporting Standards) | Institutional Limited Partners Association | https://ilpa.org/resource/ilpa-reporting-template/ | 2024 (v2.0 maintained) | 2026-04-24 | Tier 1 — institutional LP standard-setter | Canonical LP quarterly-reporting format; capital call / distribution notice conventions; fee-and-expense transparency |
| ILPA Quarterly Reporting Standards — PDF Guidance | Institutional Limited Partners Association | https://ilpa.org/wp-content/uploads/2023/03/ILPA-Quarterly-Reporting-Standards_Updated-Version-1_Final.pdf | 2023-03 | 2026-04-24 | Tier 1 — institutional LP standard-setter | Detailed field-by-field quarterly reporting requirements; NAV, commitments, uncalled capital |
| NCREIF PREA Reporting Standards | NCREIF / PREA Reporting Standards Council | https://www.reportingstandards.info/ | 2024 (current edition) | 2026-04-24 | Tier 1 — institutional real-estate reporting standard | Real-estate-specific quarterly KPI disclosure rules for NFI-ODCE funds; NOI, occupancy, valuation conventions |
| NCREIF Property Index (NPI) Methodology | National Council of Real Estate Investment Fiduciaries | https://www.ncreif.org/data-products/property/ | 2024 | 2026-04-24 | Tier 1 — institutional benchmark | NOI, return-component, and occupancy computation conventions used across institutional multifamily portfolios |
| AvalonBay Communities Q4 2024 Earnings Release & Supplemental | AvalonBay Communities / SEC | https://s25.q4cdn.com/509078598/files/doc_financials/2024/q4/AVB-4Q24-Earnings-Release.pdf | 2025-02 | 2026-04-24 | Tier 1 — primary public filing | Model institutional multifamily quarterly KPI dashboard: same-store rev/expense/NOI growth, occupancy, turnover, rent growth |
| Equity Residential Q4 2024 Earnings Release & Supplemental | Equity Residential / SEC | https://www.equityapartments.com/investors | 2025-02 | 2026-04-24 | Tier 1 — primary public filing | Same-store KPI presentation; concessions and retention disclosure; like-term effective rent change methodology |
| Camden Property Trust Q4 2024 Earnings Supplemental | Camden Property Trust / SEC | https://ir.camdenliving.com/ | 2025-02 | 2026-04-24 | Tier 1 — primary public filing | Southeast/Sunbelt operating disclosure; turnover, renewal, new-lease change, portfolio operating metrics |
| PREA (Pension Real Estate Association) Member Guidance | Pension Real Estate Association | https://www.prea.org/ | 2024 | 2026-04-24 | Tier 2 — industry body | LP-side expectations on GP reporting content; ESG and DEI survey frameworks |
| ANREV / INREV / NCREIF Global Definitions Database | ANREV-INREV-NCREIF | https://www.reportingstandards.info/global-definitions-database/ | 2024 | 2026-04-24 | Tier 1 — global institutional RE definitions | Definitions for IRR, TVPI, DPI, RVPI that feed the performance-snapshot section of a QAR |
| SEC Form 10-Q — Reg S-K Item 303 (MD&A) | U.S. Securities and Exchange Commission | https://www.sec.gov/rules/final/2020/33-10890.pdf | 2020-11 (current) | 2026-04-24 | Tier 1 — primary regulator | MD&A narrative-commentary standard that institutional REIT supplementals and private QARs mirror stylistically |
| NAREIT — Guide to Earnings Releases and Supplementals | Nareit | https://www.reit.com/investing/industry-data-research/research-reports | 2024 | 2026-04-24 | Tier 2 — industry body | Conventions for REIT quarterly supplemental structure; same-store NOI reconciliation; non-GAAP KPI norms |
| ILPA Diversity in Action Framework | Institutional Limited Partners Association | https://ilpa.org/diversity-in-action/ | 2024 | 2026-04-24 | Tier 1 — institutional LP framework | LP-level DEI and diversity-of-leadership reporting expectations that now flow into quarterly narratives |
| PRI (Principles for Responsible Investment) Reporting Framework — Real Estate Module | UN PRI | https://www.unpri.org/reporting-and-assessment | 2024 | 2026-04-24 | Tier 1 — ESG standard | LP ESG reporting expectations for quarterly sustainability disclosure |
| GRESB Real Estate Assessment (Reference Guide) | GRESB | https://www.gresb.com/nl-en/real-estate/ | 2024 | 2026-04-24 | Tier 2 — ESG benchmark | Quarterly / annual ESG metrics expected in institutional multifamily reports: energy, water, GHG, resident engagement |

## Key Findings

### What a QAR is and who it serves

- An institutional Quarterly Asset Review (QAR) — also called a Quarterly Owner Report (QOR), Quarterly Investor Report, or Quarterly Operating Report — is the single most important piece of GP-to-LP communication between annual audited financials. It is the document against which the LP evaluates whether the business plan is on track and whether the sponsor is executing.
- It is distinct from, and complementary to, three other reporting artifacts that an institutional multifamily program produces on different cadences:
  - **Monthly flash report** — short (1–3 page) KPI dashboard sent ~10–15 business days after month-end. Unaudited actuals vs budget on a handful of headline KPIs (occupancy, collections, NOI variance). Not a substitute for the QAR.
  - **Quarterly Asset Review (QAR / QOR)** — the subject of this note. Full narrative, 8–20 pages, delivered 30–60 days after quarter-end.
  - **Annual audited financials** — GAAP-audited operating and balance-sheet statements, 90–120 days after fiscal year-end.
  - **Annual asset plan / budget** — forward-looking business plan and operating budget for the upcoming fiscal year, typically delivered in Q4 for the following year.
- The QAR is the only recurring deliverable where narrative commentary carries equal weight to numbers. A QAR that is all tables and no commentary fails the LP's basic test. A QAR that is all commentary and no tables fails the other half.

### Required section structure

An institutional multifamily QAR follows a conventional 10-section structure. Every sophisticated LP expects these sections in roughly this order; deviations signal either immaturity or an attempt to bury underperformance:

1. **Executive Summary / Thesis Status** — 1/2 to 1 page. States the original investment thesis in one sentence, then grades current progress against it (on-track / ahead / behind / materially off-track). Highlights the 3–5 most important quarter-over-quarter changes. Written last; read first.
2. **Performance Snapshot** — tabular. Current quarter actuals vs budget vs prior-year actuals for the 6–10 headline KPIs. One page, scannable.
3. **KPI Dashboard** — deeper tabular exhibit. Same KPIs as the snapshot, plus trailing-quarter and trailing-12-month (TTM) views, plus YTD views. Occupancy, rent, and NOI metrics broken out by unit type if meaningful.
4. **Variance Commentary** — narrative. Line-item explanation of material variances (Timing / Permanent / One-Time, per the pack's taxonomy-seed framework). Written in plain English, not spreadsheet-speak.
5. **Leasing & Occupancy Performance** — narrative + tables. New-lease change, renewal change, blended lease trade-out, concessions environment, retention rate, turnover rate, days-to-lease, traffic counts.
6. **Capital Projects Status** — tabular. Budget vs actual on any active CapEx or value-add program, by project. Schedule-to-complete commentary.
7. **Market Update** — narrative. Submarket supply, competing lease-up, rent trends, local economic indicators relevant to the asset. Short — 1/2 to 1 page. Not a market study.
8. **Risks & Watch Items** — narrative bulleted. Known or emerging issues the LP should be monitoring: insurance renewal risk, tax reassessment, concentration exposure, management-turnover risk.
9. **Financial Position** — tabular. Debt summary (balance, rate, maturity, DSCR, LTV/LTC), cash position, reserves balance, capital-call / distribution activity during the quarter.
10. **Forward-Look / Next Quarter Plan** — short narrative. Sponsor's view of next quarter: leasing targets, CapEx milestones, decision points, expected distribution activity.

**Length norms.** 8–12 pages is the institutional default for a single stabilized asset QAR. Value-add or in-lease-up assets run 15–20 pages because of expanded project and leasing detail. ≥25 pages signals over-disclosure (usually in an underperforming quarter, burying the lede); <6 pages signals under-disclosure. These norms are not prescribed by ILPA or NCREIF but are the observable convention across GP templates and align with ILPA Quarterly Reporting Standards' emphasis on "clarity and conciseness."

### Mandatory KPI checklist (institutional LP report)

The KPIs below are the **mandatory floor** for an institutional multifamily QAR. Every item on this list appears in the quarterly supplementals of the major public multifamily REITs (AVB, EQR, CPT, MAA, ESS, UDR) and is expected by LPs reviewing private GP reports. Formulas are quoted *by reference* to `_taxonomy-seed.md §2` and `knowledge/multifamily-benchmarks.md`, not redefined here.

| KPI | Cadence in QAR | Source convention | Benchmark reference |
|---|---|---|---|
| **Physical Occupancy** | Point-in-time (end of quarter) + quarterly average | NCREIF / Fannie Mae "Stabilized Residential Occupancy" | `knowledge/multifamily-benchmarks.md` §Physical Occupancy Benchmarks |
| **Economic Occupancy** | Quarterly average | `_taxonomy-seed.md` §2 — `Actual Collected Revenue / GPR` | `knowledge/multifamily-benchmarks.md` §Economic Occupancy vs Physical |
| **NOI (quarterly, YTD, TTM)** | Three columns: Q actual vs Q budget vs Q prior-year | `_taxonomy-seed.md` §2 — `EGI − Total OpEx` (AM convention, reserves below line) | `knowledge/underwriting-calc.md` §NOI |
| **NOI Growth YoY** (same-store) | Quarterly, YTD | % change vs prior-year same period | REIT supplementals standard (AVB, EQR, CPT) |
| **Revenue Growth YoY** (same-store) | Quarterly, YTD | % change in total residential revenue | REIT supplementals standard |
| **Expense Growth YoY** (same-store) | Quarterly, YTD | % change in controllable + total OpEx | REIT supplementals standard |
| **Effective Rent Growth / Blended Lease Trade-Out** | Quarterly | New-lease change %, Renewal change %, Blended change % | `_taxonomy-seed.md` §4 Effective Rent; REIT convention |
| **Retention Rate** | Quarterly | Renewals ÷ lease expirations in period | `knowledge/multifamily-benchmarks.md` §Turnover (retention is complement) |
| **Turnover Rate** | Quarterly (annualized) and TTM | Units turned ÷ total units, annualized | `knowledge/multifamily-benchmarks.md` §Turnover rate |
| **Bad Debt %** (of GPR) | Quarterly + TTM | `_taxonomy-seed.md` §2 — `Bad Debt / GPI` | `knowledge/multifamily-benchmarks.md` §Bad Debt Ratio |
| **Operating Expense Ratio** | Quarterly + TTM | `Total OpEx ÷ EGI` | `knowledge/multifamily-benchmarks.md` §Operating Expense Ratio |
| **Concessions** ($ or % of GPR) | Quarterly | Annualized $ drag on GPR | `_taxonomy-seed.md` §2 — Concessions |
| **DSCR** (if levered) | Point-in-time end of quarter + TTM | `knowledge/underwriting-calc.md` §DSCR | `knowledge/multifamily-benchmarks.md` §DSCR Calculation |
| **LTV / LTC** (if levered) | Point-in-time | Current debt balance ÷ current appraised value (LTV) or total cost (LTC) | `knowledge/multifamily-benchmarks.md` §LTV, §LTC |
| **Debt Yield** (if levered) | Point-in-time + TTM | NOI ÷ loan balance | `knowledge/underwriting-calc.md` / `multifamily-benchmarks.md` |

**Supplementary KPIs expected at the fund / LP level** (not property-specific, but often consolidated in a multi-asset QAR or reported separately):

- **Net IRR, Gross IRR** — since-inception
- **TVPI (Total Value to Paid-In)** — ANREV/INREV/NCREIF global definition
- **DPI (Distributions to Paid-In)** — ILPA-standard
- **RVPI (Residual Value to Paid-In)** — ILPA-standard
- **NAV** — quarterly mark, valuation methodology stated
- **Uncalled Capital Commitment** — per ILPA quarterly reporting template
- **Fee and Carry accrual** — per ILPA fee transparency standards

### Variance classification taxonomy at the reporting layer

**The reporting-layer question is different from the analytical-layer question.** The R2 variance analyst note answers: "what is the classification of this line-item variance?" (Timing / Permanent / One-Time, per `_taxonomy-seed.md §3`). The reporting layer answers: "how is that classification packaged for an LP?"

Institutional convention, observed across REIT supplementals and private-GP QAR templates:

- **Tabular presentation of variance by line item** — columns are typically: `Line Item | Budget | Actual | Variance ($) | Variance (%) | Classification | Driver`. The classification column uses the pack's Timing / Permanent / One-Time labels (or the GP's equivalent). The driver column is a 3–8 word plain-English cause ("Insurance premium invoiced in April," "Hurricane Ian deductible," "R&M run-rate elevated by HVAC age").
- **Narrative variance commentary** — only for material items (applying the pack's materiality floor: lesser of 10% of budgeted line item OR $25,000 absolute). Immaterial variances should not consume narrative space.
- **Normalized / run-rate NOI footnote** — the reporting writer should present both the GAAP / cash NOI and a "normalized" NOI that removes One-Time items. Institutional LPs track both. AvalonBay, EQR, and Camden all reconcile to an "adjusted" or "core FFO" that strips non-recurring items, with a bridge table.
- **Variance section length convention** — 1–3 pages for a healthy quarter, 4–6 pages for a variance-heavy quarter. Long variance narrative is acceptable *when* there is genuinely more to explain; it is not acceptable as throat-clearing.
- **Commentary-to-table ratio** — the QAR as a whole should run ~50/50 between tables/exhibits and narrative. Variance sections tilt more narrative (~30% table / 70% commentary); performance snapshot and KPI dashboard sections tilt more tabular (~80% table / 20% commentary).

### T-3 vs T-12 bridging convention in QAR reporting

Both T-3 and T-12 appear in institutional multifamily QARs, but they answer different questions and are used at different stages of the document:

- **T-12 (trailing twelve months)** — used for **run-rate NOI and valuation anchoring**. Every institutional QAR should show a T-12 NOI figure in the KPI dashboard. T-12 is what valuation, refinancing, and buyer underwriting will use; showing it in the QAR keeps the LP's expectations calibrated to how the asset will ultimately be valued / sold / refinanced.
- **T-3 (trailing three months)** — used for **trend / momentum diagnosis**. A T-3 annualized NOI that diverges materially from T-12 signals a directional shift (improving or deteriorating) that the LP needs to see. T-3 is especially load-bearing in value-add and lease-up situations where T-12 still reflects pre-business-plan performance.
- **Institutional convention**: report T-12 as the primary run-rate metric, report T-3 as a supplementary "most-recent-trend" overlay *only* when T-3 and T-12 meaningfully diverge (roughly >5% difference in annualized NOI). T-1 (single month annualized) is **not** a QAR-level metric — it is too volatile and is properly confined to the monthly flash report. The pack convention: "T-12 always, T-3 when diagnostic, T-1 never."
- **Lender T-3 convention**: mortgage underwriters (Fannie Mae, Freddie Mac, most bridge lenders) routinely apply T-3 as a "haircut" stress on T-12 — if T-3 annualized is materially below T-12, loan sizing uses the lower figure. This is a **lender** convention rather than an **LP-reporting** convention, but sophisticated LPs track the same ratio because it foreshadows refinance sizing risk. A QAR that discusses upcoming refinance should explicitly reconcile T-3 vs T-12.

### Capital call / distribution reporting

Per ILPA Quarterly Reporting Standards, every QAR must include — at the fund or JV level — a capital-account activity section containing:

- **Capital commitment** — total and per LP
- **Uncalled capital** — remaining commitment
- **Capital calls in the quarter** — date, amount, purpose (CapEx call, operating shortfall, acquisition-closing call, follow-on)
- **Distributions in the quarter** — date, amount, source (operating distribution, refinance proceeds, disposition proceeds, promote distribution)
- **Running paid-in capital, DPI, RVPI, TVPI**
- **Cumulative IRR (net and gross)**

The reporting writer should use **ILPA's standardized capital-call and distribution notice templates** verbatim where possible; LPs consolidate multiple GP notices and divergent formats create reconciliation burden. ILPA's position: the GP narrative may be custom, the capital-account data must be standardized.

### Waterfall transparency at the report level

Institutional LPs now expect quarterly transparency on the promote waterfall, not just at exit. Conventions observed in sophisticated GP QARs:

- **Pref accrual** — running balance of accrued (but unpaid) preferred return, separate for each capital tranche if multiple. Stated as both $ and implied % of LP capital.
- **Catch-up status** — whether the GP catch-up tier has been triggered, and if so, how much has been paid.
- **Promote status** — cumulative promote paid to date; whether current quarter's distributions hit the promote tier.
- **Waterfall "clawback" exposure** — if the fund documents include a clawback, flag any scenario where realized-to-date promote could be subject to clawback on liquidation.
- **Tier-by-tier distribution reconciliation** — when a distribution is made, show which waterfall tier it settled against (return of capital, pref, catch-up, promote). This is not universally required but is the standard sophisticated-LP ask; ILPA's template treats tier reconciliation as best-practice.

### LP-specific asks: ESG, DEI, resident retention policy

Institutional LPs now require quarterly (or at minimum annual with quarterly updates) reporting on non-financial dimensions that a decade ago were not part of the QAR at all. Current expectations:

- **ESG / sustainability metrics** (per GRESB and PRI reporting framework):
  - Energy consumption (kWh total, kWh per unit, year-over-year change)
  - Water consumption (gallons per unit, year-over-year change)
  - GHG emissions (Scope 1, Scope 2; Scope 3 often annual rather than quarterly)
  - Green building certifications (LEED, ENERGY STAR, NGBS) — status and progress
  - Climate / catastrophe exposure updates (flood zone reclassification, insurance-market hardening, wildfire risk where applicable)
- **DEI / diversity of leadership** (per ILPA Diversity in Action framework):
  - Property-management team diversity composition (when the GP manages directly)
  - Board / executive-leadership diversity at the sponsor level
  - Diverse-vendor procurement spend %
  - Annual DEI survey data (quarterly narrative updates between annual measurements)
- **Resident-retention and resident-experience policy**:
  - Retention rate with a narrative on drivers (price, service, community programming)
  - Resident satisfaction survey results where available (e.g., SatisFacts, Kingsley)
  - Resident-community programming highlights (typically narrative in the Leasing & Occupancy section rather than a standalone exhibit)

**A 2026 QAR that omits ESG and DEI disclosure entirely is out of step with institutional norms.** Per PREA member guidance and ILPA Diversity in Action, LPs increasingly apply scorecards to GP reports; consistent omission of these dimensions triggers a separate LP follow-up request and erodes re-up probability.

### Public REIT quarterly supplementals as institutional format exemplars

Three public multifamily REITs produce quarterly supplementals that are the most widely-referenced templates for institutional KPI dashboard format and same-store reconciliation. The reporting writer should mirror their conventions for tabular design but compress to single-asset scale.

- **AvalonBay Communities (AVB)** — sets the benchmark for coastal-Class-A operating disclosure. Key features to mirror: (i) **Same-Store / Non-Same-Store / Disposition** breakout in every operating table; (ii) quarterly and YTD revenue-, expense-, NOI-growth columns presented side-by-side; (iii) separate **like-term effective rent change** and **renewal change** columns; (iv) **core FFO / same-store NOI reconciliation** to GAAP at the back of the supplemental. The AVB Q4 2024 release shows same-store revenue growth 2.7%, same-store expense growth 5.7%, same-store NOI growth 1.4% — all three lines presented on the same table row with prior-year and full-year comparators. Private-GP QARs should mirror the single-row presentation.
- **Equity Residential (EQR)** — sets the benchmark for concessions and same-store revenue-driver decomposition. EQR's supplemental decomposes same-store revenue change into: (i) renewal rate change, (ii) new-lease rate change, (iii) blended rate change, (iv) occupancy change, (v) other. This five-way decomposition is the institutional gold standard for "why did revenue move?" reporting and should be replicated at the single-asset level.
- **Camden Property Trust (CPT)** — sets the benchmark for Sunbelt operating disclosure and turnover / retention transparency. CPT reports turnover rate, renewal rate, and renewal increase as three separate tabular lines (not blended into one). CPT also publishes market-level new-supply and absorption commentary in the supplemental's market-update section — the model for a QAR's "Market Update" section length and depth.

## Benchmark and Formula Decisions

- **All KPI formulas are by-reference only.** This research note does not redefine KPIs that are already canonical in `_taxonomy-seed.md §2` or `knowledge/multifamily-benchmarks.md` or `knowledge/underwriting-calc.md`. The reporting writer skill must cross-reference those files for definitions. Attempting to redefine NOI, occupancy, DSCR, or bad debt inside the QAR writer is a silent-drift risk flagged here.
- **Same-store convention.** A single-asset QAR does not need a "same-store vs non-same-store" breakout. But the reporting writer should flag if the property had a mid-quarter event (major renovation, tax reassessment, insurance recategorization) that creates a comparability break; those should be footnoted and optionally excluded from the headline NOI-growth figure, with disclosure.
- **Variance materiality floor.** Use the pack materiality floor from `_taxonomy-seed.md §3` — lesser of 10% of budgeted line item OR $25,000 absolute. Do not write narrative for immaterial variances.
- **Commentary-to-table ratio target** — roughly 50/50 across the document; variance sections 30/70 table/commentary; performance snapshot and KPI dashboard 80/20 table/commentary.
- **Length target** — 8–12 pages for a stabilized asset QAR; 15–20 pages for value-add or lease-up. Push back on anything >25 pages as over-disclosure.
- **T-12 always, T-3 when diagnostic, T-1 never** (pack convention) — applies to QAR level, not the monthly flash.

## Conflicting Source Resolution

- **ILPA vs NCREIF-PREA on reporting emphasis.** ILPA focuses on fund-level investor reporting (capital account, fees, waterfall, IRR / TVPI / DPI). NCREIF-PREA focuses on property-level operational and valuation reporting. A QAR sits at the intersection. The writer should follow ILPA conventions for any fund-level / LP-capital-account section, and NCREIF-PREA conventions for any property-level operational section. No real conflict; they cover different pages of the same document.
- **Private GP QAR vs public REIT supplemental format.** REIT supplementals are a *format* exemplar, not a content exemplar. Private QARs must cover more asset-specific detail than a REIT 40-page portfolio supplemental; they must also cover capital-account and waterfall detail that public REITs do not (because the REIT's shareholders are not LPs with a promote structure). Mirror REIT conventions for KPI dashboard and same-store growth tables; do not mirror REIT length or portfolio-level aggregation style.
- **GRESB quarterly vs annual ESG cadence.** GRESB's formal assessment is annual. Most institutional LPs now expect quarterly narrative updates on ESG with full metric refresh annual-only. A QAR that attempts to recompute all GRESB metrics quarterly is over-engineered; a QAR that omits ESG entirely is under-disclosed. The pack convention: quarterly narrative + year-over-year trend commentary; full metric refresh in the Q4 / annual report.
- **Public REIT "core FFO" vs private GP "NOI."** Public REITs center their KPI story on Core FFO (a GAAP-reconciling non-GAAP measure). Private GPs center on NOI and cash flow. Do not import "FFO" into the multifamily private-GP QAR; it is not load-bearing for LPs in a private joint venture. Keep to NOI (AM convention, reserves below line) and NCF per the pack taxonomy.

## Edge Cases and Red Flags

- **Lease-up or value-add assets** — standard stabilized QAR structure still applies, but the **Performance Snapshot** section must clearly state that the asset is not yet stabilized, and the **Variance Commentary** must reconcile against the value-add business plan (ramp-schedule vs actual) rather than a steady-state budget. The KPI dashboard should include lease-up-specific metrics: lease velocity (units/week), exposure, physical occupancy ramp vs pro forma.
- **Mid-quarter acquisition** — prorated occupancy and operating results require a footnote clearly stating the period covered; do not annualize partial-quarter data without disclosure; use "stub period" language and provide both the stub-period actuals and a clean full-quarter comparison starting the following quarter.
- **Insurance renewal or tax reassessment hit mid-quarter** — flag in **Risks & Watch Items** even when the financial impact lands later. LPs should not be surprised by a Q3 forecast revision for an event the GP saw coming in Q1 and did not disclose.
- **Refinance or disposition in-quarter** — reporting must include a separate "Capital Transactions" section or expand the **Financial Position** section to cover proceeds, fees, distribution of proceeds, and resulting capital-account effect. Do not bury refi or disposition activity inside the regular Financial Position summary.
- **Sponsor-affiliated service provider fees** — must be separately disclosed (management fee, construction management, leasing commissions) per ILPA fee transparency expectations. Burying affiliated fees inside generic OpEx lines is a specific LP red flag and drives LPAC-level follow-up.
- **Going-concern or debt-maturity stress** — if the asset is within 12 months of loan maturity OR is showing DSCR stress (<1.15x on a covenant-limited loan) OR has triggered a lockbox / cash-management sweep, these conditions should appear in both the **Executive Summary** and the **Financial Position** section. Institutional LPs treat omission of maturity risk as a material reporting failure.
- **Property-manager change or replacement in-quarter** — flag prominently; include transition cost, continuity plan, and any data-integrity gaps in the operating report.
- **One-size-fits-all templating** — a common sponsor failure mode: using a single QAR template across 30 assets without tailoring the narrative. Institutional LPs read across; boilerplate commentary that repeats across assets erodes credibility. The writer skill should produce asset-specific narrative, not template-filled placeholder text.
- **Over-length driven by underperformance** — when a quarter underperforms, the temptation is to expand the narrative. The correct response is the opposite: keep the structure tight, state the underperformance cleanly in the Executive Summary, and use the Variance Commentary and Risks sections to work through the cause and response. Long narrative in an Executive Summary signals the writer is trying to bury the headline.
- **Missing ESG / DEI / resident-retention disclosure** — out of step with 2026 institutional norms per ILPA Diversity in Action and PRI real estate module. Flag as a gap in the output.

## Open Questions

- Whether future versions should provide separate QAR templates for (a) stabilized single-asset, (b) value-add in business plan, (c) lease-up / development
- Whether future versions should include a standardized "prior-quarter thesis status update" section that tracks sponsor commitments quarter-over-quarter (a compound credibility mechanism)
- Whether future versions should integrate with the pack's variance-analyst skill output directly (programmatic import of Timing / Permanent / One-Time classifications into the narrative)
- Whether future versions should include LP-specific side-letter disclosures (MFN clauses, fee-break overrides) as a standalone section
- Whether ESG metrics should be a required section at the single-asset level or deferred to fund-level annual reporting (current institutional practice is mixed)
- Whether future versions should support SFDR Article 8 / Article 9 fund disclosure requirements for GPs raising from European LPs
- Whether the writer skill should include a specific reviewer-checklist (adversarial self-review) appendix modeled on the pack's `mandatory-self-review` discipline

## Citation Tally

- **Total sources:** 13
- **Tier 1 (standard-setters, primary regulator, primary public filings):** 10 — ILPA Reporting Template, ILPA Quarterly Reporting Standards PDF, NCREIF-PREA Reporting Standards, NCREIF NPI Methodology, AVB Q4 2024 Supplemental (SEC primary filing), EQR Q4 2024 Supplemental (SEC primary filing), CPT Q4 2024 Supplemental (SEC primary filing), ANREV/INREV/NCREIF Global Definitions, SEC Reg S-K Item 303 MD&A, ILPA Diversity in Action, PRI Real Estate Module
- **Tier 2 (industry bodies, benchmarks):** 3 — PREA Member Guidance, Nareit Supplemental Guide, GRESB Real Estate Assessment
- **Tier 1 + Tier 2:** 13 ≥ 6 ✓
- **Total sources:** 13 ≥ 10 ✓

Gate requirements met. No Tier 3 sources used for this research note; the topic is institutional-standards-driven and Tier 1 / Tier 2 coverage is sufficient and strongly preferred.

## Cross-References Into Pack Knowledge

- `research/asset-management/_taxonomy-seed.md` — KPI formulas (§2), variance buckets (§3), rent definitions (§4); do not redefine in the writer skill
- `knowledge/multifamily-benchmarks.md` — occupancy, expense ratio, turnover, bad debt, DSCR, LTV / LTC benchmark ranges
- `knowledge/underwriting-calc.md` — DSCR, debt yield, cap rate, IRR formulas for the Financial Position section

## Known Gaps / Future Research

- **Multi-asset / fund-level QAR format** is not in scope here; this note assumes single-asset QAR. A follow-on research note should cover fund-rollup conventions (NCREIF NPI submission format, ODCE reporting, portfolio-level Gross-to-Net IRR reconciliation).
- **International LP conventions (INREV, ANREV)** are touched on via the global definitions database but not fully researched; US-focused per pack scope.
- **Audit season overlap (Q4 QAR vs annual audited financials)** — the interplay between Q4 QAR delivery (typically Feb–March) and audited-financials delivery (typically April–May) has specific reconciliation mechanics (subsequent-events footnote, audit-adjustment reclassification) that merit a dedicated future research note.
- **Side-letter and MFN reporting** — institutional LP side-letters frequently modify standard reporting requirements. A future research pass should survey typical side-letter reporting clauses (most-favored-nation, reporting-enhancement, ESG-pass-through) and how a QAR writer should flag side-letter triggers.
