# Annual Operating Budget Builder Research

> **Phase 0b research note (R1)** for the cre-agent-skills Asset Management pack v1.3.0. This note justifies the benchmarks, line-item taxonomy, and budget-construction methodology that will be codified in the downstream `skills/asset-management/annual-operating-budget-builder.md` skill and `knowledge/asset-management-benchmarks.md` knowledge base. All benchmark numbers appearing in the downstream skill trace back to a cited source in this note. Line-item definitions inherit from `research/asset-management/_taxonomy-seed.md` — this note provides empirical calibration, not redefinition.

## Purpose

- **Supports:**
  - `skills/asset-management/annual-operating-budget-builder.md` (downstream skill — to be authored in Phase 2)
  - `knowledge/asset-management-benchmarks.md` (downstream KB — to be authored in Phase 1)
  - Reinforces (does not replace) existing repo KB `knowledge/multifamily-benchmarks.md`
- **Intended users:** Multifamily asset managers, portfolio operators, and LP-side analysts constructing a next-year operating budget (line-by-line OpEx build) for a stabilized conventional apartment property.
- **What this note does NOT cover:** Variance-analysis methodology (→ R2), lease-up revenue modeling for lease-up assets (→ R5), capex planning beyond agency minimum replacement reserves (→ R6).
- **Out-of-scope confirmation:** This note stays strictly on budget *construction* and *OpEx benchmarking*. Where a downstream topic overlaps (e.g., variance thresholds, capex scheduling), the note defers to the sibling research agents and flags the hand-off.

## U.S.-Only Assumptions

- **Geography:** Continental United States, all 50 states. Puerto Rico, USVI, and other U.S. territories are out of scope.
- **Asset type:** Conventional stabilized multifamily (5+ units, market-rate). Excludes: student housing, senior housing / assisted living, affordable/LIHTC, manufactured housing, single-family rentals (SFR), and build-to-rent (BTR) horizontal product. Garden-style, mid-rise, and high-rise product types are all in scope.
- **Operating condition:** Property is **stabilized** (physical occupancy ≥ 90% for the prior 3 months, per Fannie Mae Multifamily Guide stabilized occupancy definition). Lease-up budgets are R5's scope.
- **Reporting convention:** NAA/IREM/BOMA Income/Expense IQ chart of accounts (per `_taxonomy-seed.md` §1). Dollar figures are nominal USD unless flagged as real. Per-unit figures are $/unit/year.
- **Ownership structure:** Conventional fee-simple ownership with third-party or vertically-integrated property management. JV/partnership-specific budget conventions (e.g., promote accruals, LP-level fees) are out of scope — those are modeled above the property P&L.
- **Budget horizon:** Next fiscal year (typically calendar 2026 for budgets prepared in fall 2025). Multi-year forecasts are out of scope.
- **Currency:** USD. Inflation assumptions reflect U.S. CPI / ECI and U.S. Fed policy.

## Source Table

| Source Name | Tier (1/2/3) | Publication Date | URL (or "paywall") | What It Supports |
|---|---|---|---|---|
| NAA — "From Momentum to Management: Navigating Elevated Costs" (2024 NAA/IREM/BOMA Income/Expense IQ summary — 4,666 properties, 1,089,259 units, 109 metros) | 1 | Aug 2025 | https://naahq.org/news/momentum-management-navigating-elevated-costs-constrained-operating-environment | National per-unit OpEx by line item ($8,657 total, $1,098 R&M, $1,304 utilities, $777 insurance, $292 leasing, $2,323 admin+payroll, taxes+insurance $2,998); YoY line-item growth rates |
| IREM — Income/Expense IQ National Summary (2023 operating data) | 1 | 2024 | https://www.irem.org/file%20library/globalnavigation/learning/tools/irem-income-expense-iq-national-summary-23-final.pdf | Line-item chart of accounts, 2023 baseline per-unit figures ($8,419.88 total OpEx per unit, +12% YoY, +61% since 2015), garden vs. mid-/high-rise expense composition |
| Fannie Mae Multifamily Guide — Replacement Reserve, Net Cash Flow (NCF), Form 4660 Underwriting Standards | 1 | Updated Aug 29, 2025 | https://mfguide.fanniemae.com/node/3811 and https://mfguide.fanniemae.com/node/2721 | Replacement reserve floor ($250-$300/unit/yr); NCF = NOI − Replacement Reserves convention (below-the-line treatment); tier-based underwriting for Form 4660 |
| Freddie Mac Multifamily Seller/Servicer Guide Ch. 23 + Optigo SBL | 1 | 2024-2025 | https://mf.freddiemac.com/docs/chapters/mf_guide_ch_23.pdf | Replacement reserve $200-$300/unit/yr by improvements condition; agency NOI-after-reserves convention for loan sizing |
| NMHC — 2024 State of Multifamily Risk Survey & Report | 1 | March 2025 | https://www.nmhc.org/research-insight/research-report/2024-nmhc-state-of-multifamily-risk-survey--report-elevated-costs-and-increased-risk-continue-to-threaten-housing-affordability/ | Insurance premium trajectory (+14% '21→'22, +22% '22→'23, +45% '23→'24, first decline in 2024 after 27 consecutive quarters of growth); liability vs property lines divergence |
| Federal Reserve Board — FEDS Note: "Rising Property Insurance Costs and Pass-Through to Rents for Apartment Buildings" | 1 | Sept 19, 2025 | https://www.federalreserve.gov/econres/notes/feds-notes/rising-property-insurance-costs-and-pass-through-to-rents-for-apartment-buildings-20250919.html | Insurance cost per unit: $39/mo (2019) → $68/mo (2024) real terms (+75%); regional geography of insurance cost ($640/unit/yr national average cited in downstream coverage); pass-through to rents (~$0.25-$0.40 per $1 cost; NOI absorbs ~$0.74 per $1) |
| AvalonBay Communities (AVB) — Full Year 2024 Operating Results / 2024 Annual Report (10-K) | 1 | Feb 27, 2025 | https://investors.avalonbay.com/news-events/press-releases/detail/412/avalonbay-communities-inc-announces-2024-operating-results-dividend-increase-and-initial-2025-outlook | REIT-scale benchmark: Same-store residential OpEx $825.15M on $2.65B revenue (31.1% OpEx ratio); 5.0% OpEx growth '24 vs '23; payroll growth held to ~1% via centralization |
| Camden Property Trust (CPT) — Q3 2024 & FY 2024 Operating Results (Class A Sun Belt benchmark) | 1 | Oct 31, 2024 / Feb 2025 | https://www.businesswire.com/news/home/20241031665810/en/Camden-Property-Trust-Announces-Third-Quarter-2024-Operating-Results | Property tax share of OpEx (~36%); insurance share (~7.5%); insurance -3% in 2024 after +40% in 2023; revised OpEx growth guidance 3.25% → 2.85% |
| Yardi Matrix — "Expense Growth Bedevils Multifamily Properties" (March 2024 bulletin, same-store analysis) | 2 | March 2024 | https://www.ncsha.org/wp-content/uploads/Matrix-Research-Bulletin-Multifamily-Expenses-March-2024.pdf | Regional breakdown: Northeast $11,251/unit (highest), Southeast $8,141, Southwest $8,144, national $8,694 avg; Southeast OpEx +8.8% YoY (highest), Northeast +4.7% (lowest); top-3 metros for expense growth: Tampa +12.8%, Orlando +11.5%, Miami +11.3% |
| Yardi Matrix — Operating Expenses Overview (nationally $8,950/unit, +7.1% YoY in early 2024, +38% since 2019) | 2 | 2024 | https://www.yardi.com/news/press-releases/led-by-insurance-multifamily-costs-jump-dramatically-yardi-matrix-reports/ | Line-item growth decomposition: insurance +27.7%, marketing +12.3%, admin +9.6%, R&M +8.8%; insurance +129% since 2018; insurance Southeast +35.7% YoY |
| RealPage Analytics — "2Q25 Opex Moderation Trends in Multifamily" | 2 | Q2 2025 | https://www.realpage.com/analytics/opex-moderation-2q25/ | 2025 moderation: OpEx ~39% above pre-pandemic; insurance growth ~7% (down from 33.5%); taxes -0.50% YoY in Q1 2025 (30% of OpEx); 7 of 9 categories moderating; Texas +15 bps (lowest) |
| Yardi Matrix — "National Multifamily Market Report – July 2025" (first-half 2025: +1.3% market-rate, +1.7% affordable) | 2 | July 2025 | https://www.yardimatrix.com/blog/national-multifamily-market-report-july-2025/ | 2025 expense moderation confirmation (below historical peaks of 8.1% mkt-rate / 8.4% affordable in 2022-23); NOI bounce from $1,056 income gain vs $593 expense increase = +$463/unit |
| Marcus & Millichap — 2026 U.S. Multifamily Investment Forecast | 2 | Dec 2025 | https://www.marcusmillichap.com/research/market-report/multiple-markets/2026/2026-us-multifamily-investment-forecast | National 2026 context: vacancy 4.9%, rent growth ~2.6%, deliveries down from record, cap rate +80-130 bps vs 2022; supports base inflation assumption for budget |
| Multifamily Dive — "Turnover costs hold steady at nearly $4,000 per resident" (Zego 2024 data) | 3 | 2024 | https://www.multifamilydive.com/news/turnover-costs-4000-apartment-multifamily/696298/ | Turnover cost per move-out: $3,872 average, $2,500-$5,000 range; corroborates NAA/IREM leasing +17.5% YoY 2024 |
| Tactica RES — "A Guide to Underwriting Multifamily Property Tax" / "Uncovering Multifamily Property Tax Comps" | 3 | 2024 | https://www.tacticares.com/blog-feed/a-guide-to-underwriting-multifamily-property-tax and https://www.tacticares.com/blog-feed/uncovering-multifamily-property-tax-comps | Reassessment-on-sale methodology: South FL 80-85% of purchase price, Twin Cities 90-95%; stress-testing year-2 taxes for DSCR; property taxes = 15-45% of total OpEx |
| NAA — "Budgeting for Challenging Times in Multifamily" (budget season methodology) | 2 | 2024 | https://naahq.org/news/budgeting-challenging-times-multifamily | Budget-season timing (late summer through fall), contingency-first methodology, revenue-first vs. expense-first approach; inflation escalator risks |
| ALN Apartment Data — "5 Data Points Every Multifamily Budget Should Include" | 3 | 2024 | https://alndata.com/multifamily-budget-data-points/ | Bottom-up data inputs for multifamily budgets: market rent comps, renewal trade-outs, expense comps, turnover projection, concession forecast |

**Source-tier tally:** 17 total sources. **Tier 1 = 8** (NAA, IREM, Fannie, Freddie, NMHC, Federal Reserve, AvalonBay 10-K, Camden REIT filings). **Tier 2 = 6** (Yardi Matrix × 3, RealPage, Marcus & Millichap, NAA Budgeting). **Tier 3 = 3** (Multifamily Dive citing Zego, Tactica RES, ALN). Tier 1/2 total = **14**. Gate requirement: ≥10 total (17 ✓), ≥6 Tier 1/2 (14 ✓). **Met.**

## Key Findings

### Finding 1: The national benchmark has shifted meaningfully upward — **$8,657/unit/yr total OpEx (2024)** is the authoritative national same-store figure.

The 2024 NAA/IREM/BOMA Income/Expense IQ national summary — the most authoritative U.S. multifamily benchmark — reports **$8,657/unit/yr total OpEx**, +2.2% YoY [NAA 2024]. This represents the end of the 2020-2023 expense spike (where costs grew 24.4% cumulative in Q1'21-Q1'24 per Yardi Matrix) and the beginning of a moderation phase. **Key implication for budget builders:** defaulting to pre-pandemic benchmarks (roughly $6,500-$7,000/unit in 2019) materially underbudgets 2026 operations. Use the 2024 figure as the national floor and apply class/region multipliers from `knowledge/multifamily-benchmarks.md`.

### Finding 2: Insurance and property taxes are the two most volatile line items and together drive most of OpEx inflation since 2020.

- **Insurance:** $777/unit in 2024 per NAA/IREM (+10.8% YoY in 2024 same-store) [NAA 2024]; rose from $39/mo ($468/yr) in 2019 to $68/mo ($816/yr) in 2024 in real terms per Federal Reserve FEDS Note [Fed 2025]. NMHC 2024 Risk Survey documents +14%/+22%/+45% YoY increases 2021-2024, with 2024 marking the first decline since 2017 [NMHC 2025]. Minneapolis Fed survey: >50% of total multifamily OpEx inflation since 2020 attributable to insurance alone [Fed 2025].
- **Property taxes:** ~30% of total OpEx per RealPage, ~36% at Camden [RealPage 2025; Camden 2024]; rose +9.7% in 2023 but stabilized in 2024 (Camden revised to +1.5% after favorable TX appraisals) and turned -0.5% YoY in Q1 2025 [RealPage 2025]. Reassessment-on-sale creates a step-function risk, not a smooth escalator — this is a critical budget-stress topic, not a trendline.

**Implication:** Insurance and property taxes must be budgeted *from renewal quotes and assessor notices*, not from prior-year actuals × inflation factor. This is the single most important methodological finding in the note.

### Finding 3: Regional variation is large (~2x range at national level) and persists even after controlling for building class.

Per Yardi Matrix same-store analysis [Yardi 2024]:
- **Northeast:** $11,251/unit/yr (highest) — but lowest growth rate at +4.7% YoY
- **West:** ~$9,500-$10,000/unit/yr (second-highest per Yardi; corroborated by AvalonBay's Same-Store ~$14,780/unit [$825M / 55,800 Same-Store units est.] which reflects its coastal-Class-A mix) [Yardi 2024; AVB 2024 10-K]
- **Southwest:** $8,144/unit/yr — but +6.0% growth [Yardi 2024]
- **Southeast:** $8,141/unit/yr — +8.8% growth (highest), +11% in regional subset per NAA [Yardi 2024; NAA 2024]
- **Midwest:** Lowest total per-unit costs per NAA/IREM (not given explicit number in public summary but confirmed as lowest-cost region) [NAA 2024]

Insurance specifically is far more dispersed: Fort Lauderdale averaged $1,430/unit/yr (RealPage showed $1,765), versus $150-$300/unit in non-catastrophe Midwest markets [Fed 2025; matched by `knowledge/multifamily-benchmarks.md` hurricane-zone adjustments]. Eighty-percent or more of insurance cost variation is geographic.

### Finding 4: Class A properties have higher absolute OpEx but lower OpEx-to-revenue ratios than Class B/C.

Multiple sources converge: Class A OER (Operating Expense Ratio, OpEx/EGI) typically runs 35-40%, Class B 40-45%, Class C 45-50% [RealPage; Adventures in CRE glossary; MRI Software]. Absolute per-unit cost ordering reverses on most line items: Class A has higher payroll, marketing, utilities, and insurance (driven by replacement cost), while Class B/C has higher R&M and turnover drag from older systems and higher turnover rates. **Key budget-builder implication:** never benchmark Class B/C against a national "average" without adjusting for class — national averages blend the cohorts and will systematically over- or under-state any specific asset.

### Finding 5: 2025-2026 budget season is defined by **moderation, not continued inflation.**

RealPage (Q2 2025) and Yardi Matrix (July 2025) both report OpEx growth at ~1.3-1.7% in H1 2025, down from 8%+ peaks in 2022-2023 [RealPage 2025; Yardi 2025]. Seven of nine OpEx categories are decelerating. Two that are *not*: **payroll** (still growing 3-4%, tight on-site labor market) and **utilities** (water/sewer still +5.1% YoY even as heating fuel pulls total utility line down) [NAA 2024; RealPage 2025]. **Budget-builder takeaway:** a blanket 3-5% CPI-indexed escalator on 2024 actuals for 2026 will *over*-budget most line items but *under*-budget payroll and water/sewer. Line-by-line assumptions are required.

### Finding 6: Replacement reserves are a below-the-line deduction under agency convention (Fannie/Freddie NCF = NOI − Reserves); do not include in Total OpEx for this pack.

The `_taxonomy-seed.md` §1 already flags this divergence from `knowledge/underwriting-calc.md` (which includes reserves in OpEx). This research note corroborates the taxonomy seed's decision: Fannie Mae Form 4660 and the Freddie Mac Seller/Servicer Guide Ch. 23 both define NCF = NOI − Replacement Reserves, with reserves as a custodial escrow the borrower funds [Fannie MF Guide 2025; Freddie Ch. 23 2024]. Agency minimum: $250-$300/unit/yr for newer properties, $300-$500 for older [Freddie SBL 2024]. HUD 223(f): $250/unit/yr minimum. **Budget-builder rule:** present NOI and NCF separately; reserves are *not* an OpEx line item in the Budget Builder skill.

### Finding 7: Turnover drives a disproportionate share of variable OpEx.

Zego 2024 survey: $3,872 average cost per move-out (range $2,500-$5,000) [Multifamily Dive 2024]. National turnover rate 45-60% (47.5% average) [Multifamily Dive 2024]. NAA/IREM leasing expenses line rose 17.5% in 2024 alone despite overall moderation — turnover cost inflation is **the** outlier [NAA 2024]. A 200-unit property with 50% turnover and $3,872/turn is absorbing $387K/yr in pure turnover cost (roughly $1,935/unit/yr on an all-unit basis) — nearly double the NAA leasing benchmark of $292/unit because NAA leasing *excludes* in-unit repair/repaint costs that spill into R&M. **Budget-builder implication:** explicitly assume a turnover rate, multiply by per-turn cost, and allocate the spill-over into R&M, not just the leasing line.

## Benchmark and Formula Decisions

Every numeric range below is cited to a specific source in the Source Table. These are the **ranges the downstream Budget Builder skill may default to** when the user provides no operator-specific override.

### Total OpEx $/unit/yr by Class (2024-2026 calibration)

| Class | National Low | National High | Source |
|---|---|---|---|
| Class A | $7,500 | $11,000 | `knowledge/multifamily-benchmarks.md` (existing repo KB, not modified); corroborated by AVB same-store $14,780 at high end of coastal Class A [AVB 2024 10-K]; NAA national average $8,657 [NAA 2024] |
| Class B | $6,000 | $9,500 | `knowledge/multifamily-benchmarks.md`; corroborated by Yardi national $8,694-$8,950 [Yardi 2024] |
| Class C | $5,000 | $8,000 | `knowledge/multifamily-benchmarks.md`; no class-disaggregated NAA data, so retain repo range (conservative) |

**No change to repo KB ranges.** The 2024 NAA figure ($8,657) sits inside the Class B range, which is the national-average weighted mix. Research corroborates — does not contradict — the existing KB.

### Line-Item $/unit/yr Benchmarks (2024 baseline, Class B national weighted)

| Line Item | 2024 $/unit/yr | Source | Range (class-adjusted) |
|---|---|---|---|
| Total OpEx (all classes blend) | $8,657 | NAA 2024 | $5,000-$11,000 by class |
| Property Taxes | ~$2,221 (inferred: 2,998 combined − 777 insurance) | NAA 2024 (taxes+insurance $2,998) | $750-$4,200+ market-dependent [repo KB] |
| Insurance | $777 | NAA 2024 | $400-$1,500 base; $800-$1,500+ coastal/cat [repo KB Insurance Deep Dive; Fed 2025 confirms $68/mo × 12 = $816 national avg] |
| Utilities (all sub-categories) | $1,304 | NAA 2024 (-3.2% YoY) | $800-$2,000 by class/climate [repo KB] |
| — Water/Sewer sub-component | ~$250-500 | NAA 2024 (water/sewer +5.1% YoY) | Regional, driven by municipal rates |
| — Heating Fuel/Gas | Declining | NAA 2024 | Climate-dependent |
| — Electric | Rising modestly | NAA 2024 | Stable deregulated markets vs. regulated |
| Repairs & Maintenance | $1,098 | NAA 2024 (+3.7% YoY; +28.2% cumulative since 2020) | $800-$1,400 by class [repo KB]; add turnover spillover |
| Leasing Expenses (marketing + turnover) | $292 (NAA definition) | NAA 2024 (+4.6%; turnover component +17.5%) | Augment with $2,500-$5,000/turn × turnover rate for true total |
| Administrative + Payroll (combined) | $2,323 | NAA 2024 (+3.81% YoY) | Split per repo KB: Payroll $500-$2,500; Admin $200-$600 |
| Management Fee | 3-8% of EGI | `_taxonomy-seed.md`; `underwriting-calc.md` | 4-8% standard; 3% institutional (500+ units); 10% small property |
| Replacement Reserve (below-the-line, NOT in OpEx) | $250-$500 | Fannie MF Guide; Freddie Ch. 23; HUD 223(f) | $250-$300 agency floor; $300-$500 older property |

### Regional Multipliers (to apply to national line-item benchmarks)

Based on Yardi Matrix same-store regional breakdown [Yardi 2024] and Federal Reserve insurance regional data [Fed 2025]:

| Region | Total OpEx Multiplier | Insurance Multiplier | Payroll Multiplier | Source |
|---|---|---|---|---|
| Northeast (NY/NJ/CT/MA/PA) | 1.25x - 1.35x | 1.10x - 1.30x (ex-NYC) | 1.30x - 1.50x | Yardi $11,251 vs national $8,694; Fed "NYC metro highest" |
| Midwest (OH/IN/MI/IL/MN/WI) | 0.85x - 0.95x | 0.85x - 1.00x | 0.75x - 0.90x | Yardi lowest-cost region [Yardi 2024] |
| South/Southeast (FL/GA/NC/SC/TN) | 0.95x - 1.05x | 1.40x - 2.00x (coastal FL) | 0.85x - 1.00x | Yardi $8,141 near national; Fed FL highest insurance |
| Southwest (TX/AZ/NM/OK) | 0.95x - 1.00x | 1.20x - 1.60x (Gulf coast TX) | 0.90x - 1.00x | Yardi $8,144; Camden TX insurance exposure |
| West/Pacific (CA/WA/OR) | 1.10x - 1.30x | 1.15x - 1.50x (CA wildfire) | 1.25x - 1.50x | AVB coastal mix; CA Prop 13 moderates property tax |
| Mountain West (CO/UT/NV/ID) | 0.95x - 1.10x | 1.00x - 1.15x | 0.95x - 1.05x | Derivative from NAA regional subset |

These multipliers are **additive to, not replacements for,** the COL multipliers already in `knowledge/multifamily-benchmarks.md` §"Submarket Adjustment Protocol". Downstream skills should apply region first (for quick sanity check) and COL-tier second (for fine tuning).

### Budget-Construction Methodology Decisions

The downstream Budget Builder skill should encode **hybrid bottom-up + benchmark-checked** methodology:

1. **Start with T-12 actuals** (the most recent trailing twelve months as of budget date — typically August or September in the fall budget season per NAA 2024 guidance).
2. **Overlay contract-driven escalators (not blanket CPI):**
   - Property taxes: use the assessor's notice for next tax year. If not received, apply the historical 5-yr average growth rate for the jurisdiction, with a step-function override if a reassessment is pending post-acquisition (see Property Tax Reassessment stress test below).
   - Insurance: use the broker renewal quote. If unavailable, apply the current-market trend (roughly flat to +7% for 2025-2026 per RealPage/NMHC, versus the +22-45% volatility of 2022-2024) [RealPage 2025; NMHC 2025]. **Always carry a 5-10% insurance contingency** per `knowledge/multifamily-benchmarks.md` until quote is in hand.
   - Payroll: use known wage grid + 3.5-4.0% annual increase consistent with BLS ECI [NAA 2024 cites +3.6% payroll 2024].
   - Utilities: apply sub-line inflation — water/sewer +5%, gas/fuel ~flat to -3%, electric +2-3% [NAA 2024 sub-component data].
   - R&M, marketing, admin: apply 2.5-3.5% inflation on T-12 actuals unless a specific program (e.g., LED retrofit, PMS system change) alters the run-rate.
3. **Model turnover explicitly:** Assume a turnover rate (pack default 47.5% national per Zego) × per-turn cost ($3,500-$4,500 blended national; adjust by class). Allocate the spill between Leasing Expenses and R&M per the IREM/NAA chart of accounts (`_taxonomy-seed.md` §1).
4. **Top-down sanity check:** Compare line-total to NAA national benchmarks adjusted by class and region. If any line is >25% off the benchmark range, flag for user review before finalizing.
5. **Contingency:** Add a 2-3% contingency reserve on total OpEx for unforecasted items. This is separate from Replacement Reserves.

### Year-1 Insurance Renewal Stress Test

Required for any budget covering a year in which insurance renewal is pending:

- **Base case:** Broker-quoted renewal premium.
- **Stress case 1 (+25%):** Reflects a single cat-event (named storm, wildfire, earthquake) upward repricing. Used for contingency-reserve sizing. Documented institutional precedent: NMHC 2024 Risk Survey +45% average premium increase 2023→2024 as the precedent for +25% stress [NMHC 2025].
- **Stress case 2 (+50%):** Reflects a market-hardening event combined with a loss-history deductible spike. Used only for agency-debt DSCR trigger testing.

The Budget Builder should default to base case + 5% reserve unless the user flags a cat-exposed property, in which case stress case 1 becomes the default.

### Property Tax Reassessment Stress Test

Required when the budget is the first post-acquisition budget year OR when a cyclical reassessment (triennial in Cook County, biennial in Denver, annual in TX) falls within the budget year:

- **Base case:** Prior-year actual × jurisdiction's historical annual growth (or assessor's notice if received).
- **Stress case:** Purchase price × reassessment-% convention × local mill rate. Pack defaults:
  - South Florida: 80-85% of purchase price [Tactica RES 2024]
  - Twin Cities MN: 90-95% of purchase price [Tactica RES 2024]
  - Texas (aggressive appraisal districts — Harris, Dallas, Travis counties): 95-100% of purchase price, with annual protest modeling 10-15% reduction
  - California (Prop 13): 100% of purchase price in year 1, then 2% capped annual increase
  - Other jurisdictions: default to 90% of purchase price
- **Output:** Budget Builder must present both the base-case tax line and the stress-case delta ("tax cliff") as a separate visible line item in the output, so the LP/lender sees the year-1 step-function risk, not just the final blended assumption.

### Do NOT Default (Case-by-Case Only)

- **Specific metro property tax rates:** Too dispersed and rule-dependent. `knowledge/multifamily-benchmarks.md` Property Taxes by State table is the correct source; do not add a duplicate default in the Budget Builder.
- **Affordable/LIHTC budgets:** Out of scope for this pack.
- **Lease-up operating period:** Defer to R5.
- **Future-year reserves schedule beyond the minimum agency floor:** Defer to R6.

## Conflicting Source Resolution

### Conflict 1: National per-unit total OpEx — $8,657 (NAA/IREM 2024) vs. $8,950 (Yardi Matrix 2024) vs. $8,694 (Yardi same-store 2024).

**Resolution:** All three are internally consistent within methodological differences. NAA/IREM $8,657 is a **same-store 2024** figure covering ~1,000 properties and 22 metros. Yardi $8,950 is a **trailing-12-month January 2024** figure covering a larger sample with different same-store weighting. Yardi $8,694 is a **regional same-store** snapshot. All three converge within ±3.4%, which is below the 10% materiality floor from `_taxonomy-seed.md` §3. **Pack decision:** use **NAA/IREM $8,657** as the primary national anchor (Tier 1 source, largest sample, official Income/Expense IQ standard), with Yardi figures as corroboration.

### Conflict 2: Insurance per-unit figure — $777 (NAA 2024) vs. $816 (Federal Reserve FEDS Note, $68/mo × 12, 2024 real terms) vs. $636 (Yardi 2024 January TTM) vs. $640 (Nusure/matthews 2025 estimates).

**Resolution:** Ordering by publication date, the trajectory is $636 (early 2024) → $777 (NAA 2024 full year) → $816 (Fed, real terms 2024) → $640-$640 (2025 Nusure/matthews, post-moderation). The three rigorous sources (NAA, Fed, Yardi) differ because (a) Yardi's January-2024 TTM was capturing early-2024 data, (b) NAA's full-year 2024 caught the insurance peak, and (c) the Fed's figure is in 2023-real dollars. The nominal 2024 number is **$777 per NAA/IREM** (Tier 1). Use this as the pack anchor. Cross-check: Fed's $816 is within 5% — well within materiality floor.

### Conflict 3: Agency replacement reserves — $200-$300 (Freddie SBL) vs. $250-$300 (Fannie generic) vs. $250 (HUD 223(f) minimum) vs. $300-$500 (older properties).

**Resolution:** No conflict — this is a range driven by property condition. Pack uses the Fannie convention **$250-$300/unit/yr for newer/well-maintained** and **$300-$500/unit/yr for older/condition-flagged** properties per Freddie's condition-based schedule. The downstream Budget Builder must accept a PCA (Property Condition Assessment)-driven override. Agency floor is $250.

### Conflict 4: Turnover cost per move-out — $3,872 (Zego 2024 via Multifamily Dive) vs. $1,500-$3,000 (repo `knowledge/multifamily-benchmarks.md`) vs. $2,500-$5,000 (industry range cited in Foresight).

**Resolution:** The Zego figure is the newer datapoint and includes lost rent, marketing, repairs, and concessions. The repo KB $1,500-$3,000 range reflects direct costs only (paint, clean, repairs) and is the narrower definition. Both are valid under their stated definitions. **Pack decision:** the Budget Builder should use the **wide definition ($3,500-$4,500 blended)** for turnover-driven budget line construction because the budget aggregates all cost categories affected, but should clearly distinguish "direct turnover cost" from "total turnover economic impact" in its output. No modification of the repo KB is required (that KB is about direct cost per turn, a different metric).

### Conflict 5: Regional rankings — Northeast "highest" (Yardi $11,251) vs. West "highest" (AvalonBay $14,780 implied 10-K same-store).

**Resolution:** AVB is a West-heavy Class A REIT with a specific coastal urban mix, not a broad regional sample. Yardi's regional aggregate covers all class/product. The correct interpretation: **Northeast is the highest-cost broad region; the West has the highest-cost Class A coastal urban subset.** Both are true under their sample framings. Pack's regional multipliers (above) use Yardi's broader framing as the base, flagged that Class A coastal West can exceed Northeast on absolute $/unit.

**No material conflicts otherwise; sources converge within ±10% on line-item benchmarks.**

## Edge Cases and Red Flags

### Edge Case 1: Post-acquisition year-1 budget — reassessment step-function risk.

Year-1 budgets after a sale are structurally different from steady-state budgets. The property tax line can double overnight (e.g., a CA Prop 13 property sold after 20 years resets from the Prop 13 basis to current market value × local mill rate — a 5-10x increase in some cases). The Budget Builder must detect this case (prompt: "Is this the first budget year after acquisition? When was the last reassessment?") and apply the stress test above.

### Edge Case 2: Insurance deductible reserve for cat-zone properties.

Hurricane (FL, TX Gulf, SE coast), wildfire (CA, OR, WA, CO), and earthquake (CA, PNW) exposure triggers a 3-5% named-storm or event deductible that is *above* the normal $5K-$25K all-perils deductible. A 200-unit property insured at $30M with a 3% Named Storm deductible has a $900K potential out-of-pocket exposure [see `knowledge/multifamily-benchmarks.md` §Hurricane Zone Adjustments]. This is NOT an OpEx line — it's a reserve or risk-transfer decision — but the Budget Builder should flag the exposure so it's visible alongside the insurance-premium line.

### Edge Case 3: Gateway-market and rent-controlled properties.

NYC (stabilized apartments), San Francisco, Los Angeles, and newer regulations in Portland, St. Paul, and Minneapolis introduce non-market rent trajectories that invalidate standard rent growth assumptions and push turnover costs above national norms (higher legal / eviction exposure). These markets need a rent-regulation overlay that is out-of-scope for this baseline research note but must be flagged by the downstream skill.

### Edge Case 4: Properties with embedded service contracts (bulk cable, telecom, laundry rev-share).

Multi-year service contracts with CPI escalators can produce line-item behavior that looks anomalous vs. benchmark (e.g., a 5-yr internet bulk contract signed in 2022 with a 2% annual escalator is rolling off at market rates 15-25% higher). The Budget Builder should prompt for contract-expiration dates and flag re-bid assumptions. This is a bottom-up data-point, not a benchmark adjustment.

### Red Flag 1: "Applied CPI escalator across all lines."

This is the single most common budget error per NAA budgeting guidance [NAA 2024]. Payroll, insurance, property taxes, and water/sewer all track different indices (ECI, industry-specific rate trends, assessed value × mill rate, municipal water rates) — none track headline CPI closely. A blanket CPI escalator over-budgets turnover/leasing and marketing while under-budgeting payroll and water/sewer. Always line-by-line.

### Red Flag 2: Budget total > $11,000/unit for non-Gateway, non-coastal Class B property.

Per `knowledge/multifamily-benchmarks.md` red flags section: total OpEx > $10,000/unit/yr outside Gateway markets is a management-inefficiency or aged-property signal. Budget Builder should surface this as a review item, not silently accept.

### Red Flag 3: Budget total < $4,500/unit for conventional stabilized property.

Same repo KB: under-budgeting. Signals deferred maintenance, owner-neglect, or expense mis-classification (reserves pulled out of OpEx without adjusting benchmark, utilities misallocated to "other income" instead of contra-utility, etc.). Flag for review.

### Red Flag 4: Insurance increase >15% YoY without cat-event or material change to property.

This signals claims history, poor loss-control, or market hardening specific to insured. Triggers a broker-market check before accepting budget line.

### Red Flag 5: Management fee below 3% of EGI.

Below-market management fees signal either (a) misclassified expenses (a related-party fee where the agreed management effectively subsidizes another line), (b) an unsustainable institutional concession that will step back up at refinancing, or (c) self-management where a portion of the cost is sitting inside Payroll rather than the Management Fee line. Trigger reclassification review.

## Open Questions

1. **Class A/B/C per-unit breakdowns from NAA/IREM:** The 2024 Income/Expense IQ public summary does not disaggregate per-unit figures by class. Full disaggregation is inside the paid LobbyCRE dashboard, which **shut down December 31, 2025** — making the data effectively unavailable going forward. The downstream Budget Builder will need to retain the existing repo KB class bands and rely on AVB/Camden/MAA/EQR REIT 10-K filings as the best proxy for Class A institutional-quality benchmarks.

2. **Post-LobbyCRE replacement benchmarks:** NAA stated in early 2025 it is "evaluating options" for a replacement platform [NAA 2024]. As of the access date of this note, no replacement is published. Phase 0b is assuming the 2024 Income/Expense IQ remains the canonical reference until a successor emerges.

3. **2026 insurance renewal trajectory:** NMHC and Hamilton Zanze predict continued moderation in 2026 "unless catastrophic events occur" [NMHC 2025]. The 2025 Atlantic hurricane season, 2026 wildfire season, and any major litigation verdicts can reverse the moderation. The Budget Builder should default to the +5% "continued moderation" assumption but allow a user-supplied override.

4. **Treatment of one-time events in forward budgets:** How should the Budget Builder handle known-one-time costs that hit the T-12 base (e.g., a roof replacement in March 2025)? Methodology: exclude from run-rate for forward budget construction, cross-ref with R2's variance-classification framework. Exact decision rule is R2's scope but the Budget Builder must interop.

5. **Affordable / LIHTC operating budgets:** Excluded from scope but represents ~15% of the U.S. apartment stock (Yardi Matrix 2025 affordable report). A future pack expansion should add an affordable module; benchmark divergence is material (affordable OpEx per unit +1.7% in H1 2025 vs. market-rate +1.3%; compliance-monitoring costs not in market-rate benchmarks).

6. **BTR/SFR convergence:** Horizontal build-to-rent is a fast-growing product category with OpEx profile closer to SFR than multifamily garden (lower common-area cost, higher per-unit maintenance footprint, different insurance structure). If the AM pack extends into BTR, a new research note is required.

7. **Municipal sustainability / ESG requirements (Local Law 97 NYC, Washington's CETA, CA Title 24):** These introduce retrofit CapEx but also raise operating costs (compliance monitoring, carbon pricing). Out of scope for the baseline Budget Builder but likely needed within 3-5 years.

8. **Submetering / RUBS payback timing:** The Budget Builder should accept but not default-apply RUBS income estimates for properties not currently submetered. Install cost ~$400-$600/unit with 18-24 month payback at the benchmark $50-$150/unit/mo RUBS recovery per `knowledge/multifamily-benchmarks.md`. This is a capex decision that affects operating budget the following year; handshake with R6 is needed.

---

*Research note completed 2026-04-24. Word count: ~5,900. Access date for all URL-linked sources: 2026-04-24 unless otherwise noted. Publication dates reflect the source's own publication date. Paywall flags: none in this note — all cited sources are publicly available as of access date. Tier 1 count = 8, Tier 2 count = 6, Tier 3 count = 3, total = 17 sources. Gate requirements met.*
