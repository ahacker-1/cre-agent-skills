# Monthly Variance Analyst Research

## Purpose

- Supports the planned `skills/asset-management/monthly-variance-analyst.md` skill (Asset Management pack v1.3.0)
- Intended users: multifamily asset managers, portfolio controllers, and LP-reporting analysts producing monthly and year-to-date (MTD/YTD) budget-vs-actual variance packages for owners, joint-venture partners, and limited partners
- Covers materiality thresholds, the Timing / Permanent / One-Time classification framework (inherited verbatim from `_taxonomy-seed.md` §3), reforecast triggers, and institutional norms for variance-commentary narrative
- Out of scope: budget construction methodology (→ R1), lease-up reforecasting beyond basic variance classification (→ R5), and quarterly asset-report (QAR) / LP-report structure at the quarterly level (→ R9)

## U.S.-Only Assumptions

- Geography: United States only; U.S. GAAP accrual accounting for institutional multifamily; REIT and private-fund reporting conventions
- Asset type: conventional stabilized multifamily (5+ units). Affordable / LIHTC variance analysis has regulatory-reporting overlays not covered here
- Fiscal year: assumed calendar year (Jan–Dec) consistent with Fannie Mae Form 4660 and the major REITs quoted (AVB, CPT, EQR, ESS, MAA, UDR)
- Reporting cadence: monthly variance package with YTD roll-forward is the institutional norm; full reforecast produced quarterly with an ad-hoc update when a material permanent variance is identified mid-quarter
- Currency: USD
- Storm / catastrophe references (Hurricane Ian 2022, Idalia 2023, Helene 2024, Milton 2024) are used as representative U.S. named-storm examples of one-time variances and align with the `multifamily-benchmarks.md` coastal/cat cost overlay

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|--------|-----------|-----|--------------|-------------|-------------|-------|
| IREM Income/Expense IQ — National Summary (Chart of Accounts) | IREM | https://www.irem.org/file%20library/globalnavigation/learning/tools/irem-income-expense-iq-national-summary-23-final.pdf | 2024 (2023 data) | 2026-04-24 | Tier 1 primary industry standards body | Line-item definitions inherited from taxonomy seed; variance-analysis training (ODCFASS-0224HQ03) is part of IREM's CPM curriculum |
| IREM Variance Analysis Tools (On-Demand) | IREM | https://www.irem.org/online-course/id-odcfass-0224hq03/variance_analysis_tools_skills_ondemand | 2024 | 2026-04-24 | Tier 1 primary industry body training | Training materials acknowledge dual threshold (% + $) approach; no single prescriptive threshold published outside course content |
| AvalonBay Communities Q3 2024 10-Q (period ended 9/30/2024, filed 11/12/2024) | AvalonBay (SEC) | https://investors.avalonbay.com/sec-filings | 2024-11-12 | 2026-04-24 | Tier 1 primary filing (public REIT MD&A) | Same-store opex variance commentary; property-tax reassessment and NYC abatement-expiry narrative |
| Camden Property Trust Q1–Q3 2024 Earnings Calls / Press Releases | Camden Property Trust (CPT) | https://investors.camdenliving.com/investors/financials/quarterly-results/default.aspx | 2024-05 / 2024-08 / 2024-11 | 2026-04-24 | Tier 1 primary (public REIT commentary) | Best-documented example of mid-year reforecast driven by permanent variance in insurance (+18% initial → −3% revised → −10% final) and property taxes (+3% → +1.5% → flat) |
| Equity Residential Q1–Q4 2024 Results Press Releases | Equity Residential (EQR) | https://investors.equityapartments.com/news-events/press-releases-news | 2024-04 / 2024-07 / 2024-10 / 2025-02 | 2026-04-24 | Tier 1 primary (public REIT commentary) | Quarterly same-store expense sequencing (+1.3% Q1 → +2.7% Q2 → +3.2% Q3 → +2.9% FY) illustrates timing-vs-permanent interplay across the year |
| MAA Press Release — Minor Damage from Hurricanes Helene and Milton (Oct 14, 2024) + Q3 2024 10-Q | Mid-America Apartment Communities (MAA) | https://ir.maac.com/news-events/press-releases/news-details/2024/MAA-Announces-Minor-Damage-from-Hurricanes-Helene-and-Milton/default.aspx | 2024-10-14 / 2024-10-31 | 2026-04-24 | Tier 1 primary (public REIT commentary) | MAA Q3 2024 call: CFO Clay Holder disclosed full-year storm cost of "$9M–$10M" AND that MAA does NOT add-back storm costs to Core FFO — unusual vs peers and relevant to variance-normalization policy |
| UDR Q1 2025 Commentary on 2024 Variance Drivers | UDR, Inc. | https://ir.udr.com/financials-sec-filings/sec-filings/default.aspx | 2025-04 | 2026-04-24 | Tier 1 primary (public REIT commentary) | COO Mike Lacy: "YoY same-store expense growth of 2.3% in Q1 beat expectations driven by favorable real estate taxes, insurance savings and constrained repair and maintenance expenses" — model variance narrative |
| University of Cambridge Finance Division — Types of Variances | University of Cambridge | https://www.finance.admin.cam.ac.uk/policy-and-procedures/financial-procedures/chapter-2-budgetary-planning-control/monitoring/types | 2024 | 2026-04-24 | Tier 1 institutional (standards body) | Formal timing-vs-permanent variance taxonomy (four causes: Cost, Timing, Change in Planned Activity, Error/Omission) |
| RealPage — 4 Areas to Focus On to Better Understand Financial Budget Variances | RealPage | https://www.realpage.com/blog/4-areas-to-focus-on-to-better-understand-financial-budget-variances/ | 2024 | 2026-04-24 | Tier 2 institutional (platform with operator install base) | Permanent vs timing distinction applied directly to multifamily GL; validates that reforecast is triggered by permanent variances only |
| RealPage — Budget Breakdowns: Understanding and Reporting on Multifamily Budget Variances | RealPage | https://www.realpage.com/blog/budget-breakdowns-understanding-and-reporting-on-multifamily-budget-variances/ | 2024 | 2026-04-24 | Tier 2 institutional | Standard column layout for multifamily variance reports (Current Month Actual/Budget/Var$/Var%, YTD, Reforecast, Original Budget) |
| REBA — Beyond Budget Season: The Power of Forecasting (and Reforecasting) | Real Estate Budgeting Advisors (REBA) | https://www.getreba.com/blog/beyond-budget-season-the-power-of-forecasting-reforecasting | 2024 | 2026-04-24 | Tier 2 practitioner | Best-in-class cadence: quarterly minimum reforecast, best-in-class teams maintain "live budget"; original budget baseline must be preserved, not overwritten |
| Rioo — Budget vs Actual Variance Reporting for Real Estate Finance Teams | Rioo App | https://riooapp.com/blog/budget-vs-actual-variance-reporting-real-estate | 2024 | 2026-04-24 | Tier 3 practitioner | Investor/board variance reports must be presented separately from internal reports; property-level reforecast must precede portfolio consolidation |
| NOAA National Centers for Environmental Information — U.S. Billion-Dollar Weather and Climate Disasters (Helene = $78.7B, Milton = $34.3B) | NOAA NCEI | https://www.ncei.noaa.gov/access/billions/ | 2024-12 | 2026-04-24 | Tier 1 primary (U.S. government) | Source for named-storm cost quantification; anchors one-time variance classification for 2024 Southeast multifamily |
| Fannie Mae Multifamily Guide — Replacement Reserve and NCF convention (Form 4660) | Fannie Mae | https://mfguide.fanniemae.com/node/4101 | Updated 2025-08-29 | 2026-04-24 | Tier 1 primary (agency) | Inherited from taxonomy seed — governs the NOI vs NCF line distinction relevant to how variance reports treat replacement reserves |
| Martus Solutions — How to Perform Budget Variance Analysis | Martus Solutions | https://www.martussolutions.com/blog/budget-variance-analysis | 2024 | 2026-04-24 | Tier 3 practitioner | Corroborates dual-threshold materiality convention (% AND $) and variance-narrative structure |

**Source-tier tally.** 15 total sources. Tier 1 = 10 (IREM I/E IQ, IREM Variance Analysis course, AvalonBay 10-Q, Camden CPT commentary, Equity Residential EQR, MAA, UDR, Cambridge, NOAA, Fannie Mae — counting REIT primary filings/press releases each as one Tier 1 source). Tier 2 = 3 (RealPage ×2, REBA). Tier 3 = 2 (Rioo, Martus). **Tier 1+2 = 13, well above the ≥6 minimum.** Total = 15, above the ≥10 minimum.

## Key Findings

### 1. Materiality thresholds — the institutional dual-threshold convention

There is no single universal materiality number, but there is strong institutional convergence on a **dual threshold: percentage OR absolute dollar, whichever is lower** (i.e., investigate if EITHER bar is crossed). The specific numbers cluster as follows:

- **Percentage band: 5%–10% of the budgeted line item.** 10% is the most widely cited anchor (Martus, RealPage, general finance practice). Some conservative institutional operators use 5% for large line items such as property taxes and payroll where a 5% swing on a $300k annual line is meaningful ($15k). IREM's Variance Analysis Tools course teaches the dual-threshold approach without prescribing a fixed number, deferring to operator judgment.
- **Absolute floor: $5,000 to $25,000.** The floor exists to suppress noise on small GL lines (Communications, Professional Fees) where a 10% variance is a trivial dollar figure. Pack convention from `_taxonomy-seed.md` §3 sets the default at the lesser of **10% OR $25,000**; downstream skills may accept operator overrides.
- **Scale-sensitivity.** A $25k floor is appropriate for a stabilized 200-unit asset with ~$3M OpEx; a 50-unit garden-style property's variance package should drop the floor closer to $5k, and a large multi-property portfolio might lift it to $50k. The principle is constant: thresholds should trigger investigation of genuinely consequential variances, not generate busy-work on rounding.

### 2. Timing, Permanent, One-Time — the three buckets inherited from the taxonomy seed

The Timing / Permanent / One-Time three-bucket framework is adopted **verbatim** from `_taxonomy-seed.md` §3 for this skill and is not re-derived here. Key operational rules:

- **Order of application (strict):** Evaluate Timing first. If no fit, evaluate One-Time. Classify as Permanent by residual.
- **Mixed-variance rule:** Where a variance is genuinely mixed (e.g., an insurance renewal that was both late-billed AND set a new permanent run-rate), split the variance into its Timing and Permanent components in the commentary. Do not force a mixed variance into a single bucket.
- **Seasonal/weather rule:** Weather effects within the normal range are Timing. Weather events that are named (hurricane, wildfire, declared freeze) and non-recurring within the fiscal year are One-Time. A persistently hot summer driving annual cooling load materially above budget becomes Permanent.

### 3. Timing variance — canonical examples

- **Property taxes.** Budgeted straight-line at 1/12 per month but actually paid on a semi-annual or annual cadence per the local taxing jurisdiction's schedule. YTD variance will be large until the payment month, then converge. RealPage Budget Breakdowns explicitly flags this as the #1 timing variance in multifamily operating statements.
- **Insurance premiums.** Budgeted straight-line but paid as an annual lump on renewal. Through the first 11 months, YTD cash basis will show a large favorable variance; in renewal month, it reverses. AvalonBay and Camden both disclosed May/mid-year renewal cycles in their 2024 commentary.
- **Utilities (seasonal).** Summer cooling load in the Sun Belt and winter heating load in the Northeast create predictable monthly swings against a straight-line budget. Seasonal normalization (HDD/CDD-weighted budgets) reduces but does not eliminate this timing noise.
- **Contract services.** Landscape contracts billed quarterly, pest control billed semi-annually, elevator contracts billed annually — each creates predictable timing gaps against straight-line budgets.

### 4. Permanent variance — canonical examples

- **Insurance renewals at a new run-rate.** Camden Property Trust's 2024 sequence is the textbook example of a permanent variance in reverse (favorable): the company initially projected 2024 insurance +18%, revised to −3% in Q2, and ultimately reported roughly −10% for the full year. Each revision was a permanent re-baselining of the forward forecast based on the actual renewal outcome, not a timing artifact.
- **Property-tax reassessment.** AvalonBay's 2024 10-Q commentary attributed same-store property-tax growth (+4.9% in 2023) to "increased assessments across the portfolio, successful appeals in the prior year, and the expiration of property tax incentive programs primarily at certain properties in New York City." Abatement-expiration is a clean permanent variance — it changes the run-rate from the date of expiration forward and never reverses.
- **Labor inflation / payroll step-ups.** When on-site payroll resets because of minimum-wage changes, union renewals, or a competitive labor-market step-up, the new rate persists for the remainder of the year. Equity Residential's 2024 expense trajectory (+1.3% Q1 → +3.2% Q3) reflects the natural return of turnover-related R&M and payroll to normal levels after an unusually low-turnover Q1 — a progression that separates Timing (Q1's low-turnover tailwind) from Permanent (labor step-ups baked in from leasing-season hiring).
- **Management-fee changes.** A percentage-of-EGI management-fee contract re-negotiated mid-year, or a flat fee changed by side-letter, produces a permanent variance from the renegotiation date forward.

### 5. One-Time variance — canonical examples

- **Hurricane Ian (Florida, Sep 2022).** Estimated $112B in total damages per NOAA. Southeast multifamily operators reported named-storm-deductible hits (typically 3%–5% of insured value per building) on individual communities. Classified One-Time because the event has a discrete start and end and is excluded from run-rate NOI for forward underwriting.
- **Hurricane Idalia (Florida Gulf Coast, Aug 2023).** A Category 3 landfall with ~$3.6B in estimated damages; relatively contained impact to multifamily but generated one-off deductible and BI-claim entries.
- **Hurricanes Helene and Milton (Southeast US, Sep–Oct 2024).** Helene ~$78.7B and Milton ~$34.3B per NOAA NCEI. MAA disclosed full-year 2024 storm-cost impact of roughly $9M–$10M on the Q3 2024 earnings call (CFO Clay Holder) — notable because MAA does NOT add back storm costs to Core FFO, an explicit policy divergence from most peers. Relevance to variance policy: when an operator has a strict "no add-back" stance, the One-Time variance still appears in the actuals, and the variance report must classify it as One-Time in commentary even if it is not excluded from the FFO line.
- **Litigation settlements, uninsured casualty events, one-off tax refunds, discrete regulatory fines.** Each fits the One-Time bucket because they are discrete, externally triggered, and non-recurring.

### 6. Reforecast trigger rules

Two independent sources — RealPage and REBA — converge on the same institutional policy:

- **Timing variances do NOT trigger a reforecast update.** Because they converge to the annual budget by year-end, the original budget's full-year figure remains the best forward estimate.
- **Permanent variances DO trigger a reforecast update.** Because the economics have structurally shifted, the remaining months' projections must be re-baselined to the new run-rate.
- **One-Time variances generally DO NOT trigger a forward-period reforecast.** They are already-closed discrete events. However, a large One-Time event MAY trigger a ripple (e.g., insurance-premium step-up at next renewal as a knock-on permanent variance).
- **Cadence.** Quarterly full reforecast is the institutional minimum; best-in-class operators run monthly or continuous ("live budget") reforecasts. Ad-hoc reforecasts occur mid-quarter when a permanent variance is identified and crosses the materiality threshold.
- **Baseline preservation (mandatory).** The original approved annual budget must never be overwritten. The variance report must present both "Variance to Original Budget" and "Variance to Current Reforecast" as separate columns so the board / LP can see how performance compares to both the originally-approved plan and management's current expectation.

### 7. Institutional variance-commentary norms — language and structure

Three representative examples from 2024 REIT commentary illustrate the institutional narrative pattern (topic-driver-quantification-forward-look):

- **Camden Property Trust, Q2 2024 (CFO Alex Jessett):** *"Our 55 basis point reduction in full-year expense guidance is driven primarily by the assumption of continued lower-than-anticipated insurance and property taxes."* — Format: (a) identifies line-level drivers, (b) quantifies the revision (55 bps), (c) ties directly to the forward-period reforecast ("full-year expense guidance"). This is the model institutional commentary structure.
- **UDR Q1 2025 on 2024 drivers (COO Mike Lacy):** *"YoY same-store expense growth of 2.3% in Q1 beat expectations driven by favorable real estate taxes, insurance savings and constrained repair and maintenance expenses [due to improved resident retention]."* — Format: (a) names three specific line drivers, (b) explains the root cause for R&M (retention → lower turnover → lower make-ready), (c) connects operational behavior to financial outcome.
- **AvalonBay FY 2023 10-Q commentary:** *"Same Store Residential property taxes increased $13,071,000, or 4.9%, in 2023 compared to the prior year, primarily due to increased assessments across the portfolio, successful appeals in the prior year, and the expiration of property tax incentive programs primarily at certain properties in New York City."* — Format: (a) exact dollar and percentage change, (b) three distinct drivers (assessment increase, prior-period appeals base effect, abatement expiration), (c) geographic specificity (NYC).

Synthesis of the norm: a good variance narrative (a) identifies the specific GL line, (b) quantifies in both dollars and percent, (c) gives the operational or market driver, (d) classifies as Timing / Permanent / One-Time (or its industry equivalent), and (e) states the forward-period implication.

### 8. Standard column structure for a multifamily variance report

Cross-referencing RealPage, Rioo, and REBA, the institutional-grade column set is:

| # | Column | Purpose |
|---|--------|---------|
| 1 | GL Account / Line Item | Canonical chart of accounts (aligned with taxonomy seed §1) |
| 2 | Current Month Actual | Reported cash or accrual basis actual |
| 3 | Current Month Budget | Approved month budget |
| 4 | Current Month Variance ($) | (2) − (3); favorable/unfavorable sign convention |
| 5 | Current Month Variance (%) | (4) / (3); suppressed when denominator near zero |
| 6 | YTD Actual | Cumulative actual through report month |
| 7 | YTD Budget | Cumulative budget through report month |
| 8 | YTD Variance ($) | (6) − (7) |
| 9 | YTD Variance (%) | (8) / (7) |
| 10 | Full-Year Reforecast | Current best estimate (updated each quarter) |
| 11 | Original Annual Budget | Approved at start of year — never overwritten |
| 12 | Reforecast vs. Original Budget | (10) − (11) |
| 13 | Variance Bucket | Timing / Permanent / One-Time (per taxonomy seed §3) |
| 14 | Commentary | Narrative per §7 above |

Aggregation levels: line item → revenue/expense category → property → portfolio (for multi-asset packages). Property-level reforecast must be updated BEFORE portfolio consolidation (per REBA).

## Benchmark and Formula Decisions

- **Materiality default for the variance-analyst skill: lesser of 10% of line-item budget OR $25,000 absolute** (inherited from `_taxonomy-seed.md` §3; matches dual-threshold convention). Downstream skill accepts operator overrides.
- **Classification rules: apply `_taxonomy-seed.md` §3 verbatim.** Do not redefine buckets within the skill.
- **Reforecast trigger: Permanent variance crossing materiality → reforecast update.** Timing and One-Time variances do NOT trigger reforecast of forward months (though One-Time events may produce knock-on permanent effects that then trigger an update).
- **Cadence default: monthly variance package, quarterly full reforecast, ad-hoc reforecast when a material permanent variance is identified mid-quarter.**
- **Sign convention: favorable variance = higher revenue or lower expense than budget (positive NOI impact).** Variance $ = Actual − Budget is the institutional default; some operators flip the sign for expenses. The skill should state the convention explicitly at the top of every variance package.
- **Baseline preservation: original approved annual budget must be carried as a frozen column in every variance report** — never overwritten by reforecast updates.
- **Commentary content floor:** For every variance exceeding materiality, commentary must include (a) root cause / driver, (b) classification bucket, (c) forward-period implication (or "no forward impact — timing only").
- **Non-default / operator-specific items:** Materiality threshold, reforecast cadence beyond quarterly, whether storm/casualty costs are added back to a normalized NOI — these are operator-policy decisions and must be confirmed at engagement onboarding, not hard-coded.

## Conflicting Source Resolution

- **Materiality threshold specifics.** Sources diverge on the exact numbers: 10% + $5k (Martus), 10% + $10k (Datarails), 10% + $25k (pack default per taxonomy seed). No single authoritative number exists in IREM's publicly available materials. Resolution: adopt the pack default (10% OR $25k) with explicit permission for operator override. This aligns with the taxonomy seed and is scale-appropriate for stabilized 100–300 unit multifamily.
- **Storm-cost normalization (add-back or not).** Most multifamily REITs add back named-storm costs when computing "Core FFO" (normalized FFO). MAA's CFO explicitly stated on the Q3 2024 call that MAA does NOT add back storm costs — a peer-disagreement on policy. Resolution: variance classification (One-Time) is independent of FFO add-back policy. The variance report must flag the storm cost as One-Time regardless of whether the operator excludes it from normalized NOI / Core FFO.
- **Reforecast cadence.** RealPage implies monthly reforecasting; REBA calls quarterly the "standard," monthly "best-in-class," and live/continuous "elite." Resolution: default to quarterly reforecast + ad-hoc for material permanent variances; treat monthly reforecast as an operator-choice uplift, not a skill default.
- **Timing-vs-permanent edge cases on weather.** RealPage implicitly treats all weather as timing. Cambridge's taxonomy allows for "Change in planned activity" as a separate cause. Resolution: apply the taxonomy seed's seasonal/weather rule — within-normal-range = Timing; named/extreme = One-Time; persistent full-year divergence = Permanent.
- **Inclusion of replacement reserves in variance reports.** Taxonomy seed §1 intentionally places Replacement Reserves below NOI (Fannie NCF convention) rather than inside Total OpEx. Some operators' T-12 statements put reserves inside OpEx. Resolution: the variance report should follow the operator's reporting convention for input but reconcile output to the NOI-vs-NCF split described in `_taxonomy-seed.md`.

## Edge Cases and Red Flags

- **Line items near zero budget.** Variance % blows up when the budget denominator is small (e.g., a "Miscellaneous Income" line budgeted at $100 with $5,000 actual yields +4,900%). Suppress the percentage and report only dollar variance. Materiality check should rely on the $25k absolute floor in these cases.
- **Re-classification mid-year.** An item initially flagged Timing (e.g., "contractor invoice late") that persists into a second and third month of the same direction should be re-evaluated; it may actually be Permanent. The taxonomy seed's "2+ consecutive months same direction at similar magnitude" rule is the trigger.
- **Mixed Timing + Permanent variances.** Example: an insurance renewal billed two months late (Timing) AT a 15% higher rate than budgeted (Permanent). Split and report both components; do not force one bucket.
- **Unbudgeted line items.** When an actual lands in a GL line with no budget (e.g., a new litigation-reserve account opened mid-year), treat the full actual as variance. Classification depends on the event: a new recurring reserve is Permanent; a one-off litigation hit is One-Time.
- **Cash-vs-accrual timing mismatches.** If the budget is accrual and the T-12 is cash (or vice versa), property tax and insurance premiums will show large apparent variances every single month that are purely basis-difference, not operational. Must be reconciled at report assembly, not reported as a real variance.
- **Storm and catastrophe events with insurance claims.** The gross cost hits the P&L in the month incurred; the insurance recovery may land 6–18 months later. Variance commentary must disclose both sides (gross loss + expected recovery + deductible) to avoid overstating the permanent impact.
- **Reforecast re-baselining without a budget rebase.** A reforecast is an updated estimate, NOT a new approved budget. If an LP / owner asks to "reset the budget," that is a formal amendment to the operating plan — requires a separate governance action and a fresh approved baseline. The variance package must NEVER silently replace the original budget with the reforecast.
- **Small-line-item warnings suppressed by dollar floor.** If a property's Marketing budget is set low ($30k/year) and it runs 50% over ($15k variance), the $25k absolute floor would suppress the flag — but this is a material operational issue. Operators running lean chart-of-accounts should use the smaller $5k floor.
- **Portfolio consolidation without property-level updates.** Red flag: a consolidated reforecast that changes by less than the sum of property-level reforecast changes suggests top-down plugs, not bottom-up. Refuse and require the property-level updates first (REBA guidance).

## Open Questions

- Whether the skill should publish a separate, higher materiality threshold (e.g., $50k) for larger portfolios (>1,000 units or >$25M OpEx) and, if so, what the trigger portfolio size should be.
- Whether the skill should produce a separate "LP-facing" variance narrative that aggregates line items into revenue / controllable opex / non-controllable opex groupings, distinct from the line-by-line operator-facing report. (Noted by Rioo as an institutional best practice; full LP-reporting structure handled by R9.)
- Whether the skill should output a standardized commentary template (fill-in-the-blanks) or only free-form narrative. Current institutional norm is free-form; LLM-driven templating may change this.
- Whether storm-cost add-back policy (MAA no-add-back vs peer add-back) should be a user-prompted configuration item at engagement onboarding or a per-report prompt.
- Whether Timing / Permanent / One-Time labels should appear in owner-facing reports (institutional norm) or only in internal analyst work-papers (some operators find the labels too "inside baseball" for owner consumption).
- Whether monthly cadence is the right default, or whether a "trailing-3-month variance" flag should accompany every variance to flag emerging trends the single-month view misses.

---

**Research note version:** v1.0 • Phase 0b R2 • Asset Management pack v1.3.0 • 2026-04-24
