# Hold / Sell / Refi Analyst Research

## Purpose

- Supports `skills/asset-management/hold-sell-refi-analyst.md` (Asset Management pack v1.3.0, Phase 0b, research agent R8)
- Intended for multifamily owner-operators, sponsors, and LP-side asset managers evaluating mid-hold disposition, refinance, or continued-hold decisions
- Owner-perspective analytical framework only; NOT a broker execution workflow (see `research/brokerage/*` for execution-side packs), NOT pre-acquisition underwriting (see `research/industrial/industrial-underwriting-model-builder-research.md` and existing `knowledge/underwriting-calc.md`), NOT NOI-improvement playbook (see R7 Value-Add / Operating Levers research)
- Scope is limited to the decision framework: IRR-to-date measurement, remaining-IRR projection, refinance economics, disposition timing, and capital-markets / tax context necessary to make the call

## U.S.-Only Assumptions

- Geography is the United States; conventional stabilized multifamily (5+ units); Class A/B/C stabilized or post-value-add assets
- The asset has been held at least 12 months (enough realized cash flow for a meaningful IRR-to-date) and is NOT in distress workout (loan mod / receiver / foreclosure workflows are out of scope)
- The owner has a signed or contemplated LP waterfall and debt stack of normal complexity (preferred return + promote tiers, senior agency or bank debt, possibly a subordinate piece)
- Tax framework references U.S. federal code sections (§1031, §1250, §1245); state tax variation flagged but not modeled
- Capital markets context is calibrated to the 2024-2026 rate regime: 10-Year Treasury in the ~3.85%-4.5% range, agency all-in rates low-to-mid 5%, CMBS conduit multifamily spreads ~145-165 bps over the curve [¹][²][³]
- The framework treats the IRR-to-date / IRR-continue / IRR-sell comparison as the **primary** quantitative decision input; qualitative overlays (tax timing, LP liquidity needs, portfolio concentration, sponsor reputation) are treated as secondary modifiers, not primary drivers

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| ILPA Performance Template (v2.0) & Suggested Guidance | Institutional Limited Partners Association (ILPA) | https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub/ilpa-performance-template/ | 2025-01-22 | 2026-04-24 | Primary industry standard (Tier 1) | Net IRR, Gross IRR definitions; granular vs. gross-up methodology; implementation Q1 2026 for new funds |
| NCREIF/PREA Reporting Standards — TWR vs. IRR methodology & NCREIF Academy Performance Measurement | NCREIF | https://ncreif.org/ncreif-academy/course-descriptions/ | 2024-current | 2026-04-24 | Primary industry standard (Tier 1) | Modified Dietz for TWR; SI-IRR (Since-Inception IRR) convention; TWR measures manager skill, IRR measures investor outcome |
| INREV Performance Measurement Guidelines | INREV (European Association for Investors in Non-Listed Real Estate Vehicles) | https://www.inrev.org/guidelines/module/inrev-performance-measurement | 2024 | 2026-04-24 | Primary industry standard (Tier 1) | Aligns with GIPS and NCREIF/PREA; multiples + IRR + TWR used in conjunction for transparency |
| AvalonBay Communities 2024 Annual Report / 10-K | AvalonBay Communities (AVB) | https://investors.avalonbay.com/sec-filings/all-sec-filings/content/0001104659-25-031182/0001104659-25-031182.pdf | 2025-02 | 2026-04-24 | Primary public issuer filing (Tier 1) | $726M of wholly owned dispositions in 2024; capital recycling into expansion regions; no fixed hold-period rule — strategic fit + favorable pricing triggers |
| Essex Property Trust 2024 10-K | Essex Property Trust (ESS) | https://www.stocktitan.net/sec-filings/ESS/10-k-essex-property-trust-inc-files-annual-report-dfcbf5fd339c.html | 2025-02 | 2026-04-24 | Primary public issuer filing (Tier 1) | Hillsdale Garden 697-unit disposition as "strategic plan to own quality real estate in supply-constrained markets"; capital recycled into BEX II JV consolidation |
| Freddie Mac Multifamily Maturity Risk Research | Freddie Mac Multifamily | https://mf.freddiemac.com/docs/multifamily_maturity_risk_report.pdf | 2024-01 | 2026-04-24 | Primary GSE research (Tier 1) | Refinance test: DSCR ≥ 1.40x and LTV ≤ 65% required to exempt a loan; IO loans must pass refi test pre-approval |
| FHFA 2026 Multifamily Loan Purchase Caps | U.S. Federal Housing Finance Agency | https://www.fhfa.gov/news/news-release/u.s.-federal-housing-announces-2026-multifamily-loan-purchase-caps-for-fannie-mae-and-freddie-mac | 2025-11 | 2026-04-24 | Primary government source (Tier 1) | $88B each for Fannie and Freddie in 2026 (+20% vs. 2025); 50% mission-driven allocation; workforce housing excluded from caps |
| MBA 2025 Commercial Real Estate Survey of Loan Maturity Volumes | Mortgage Bankers Association | https://newslink.mba.org/cmf-newslinks/2026/february/mba-commercial-multifamily-newslink-thursday-feb-12-2026/mba-17-of-commercial-and-multifamily-mortgage-balances-to-mature-in-2026/ | 2026-02 | 2026-04-24 | Institutional research (Tier 2) | $875B maturing in 2026 (17% of $5T); only $39B (4%) is agency multifamily — majority of refi wall is bank/CMBS/life-co |
| CREFC Market Metrics & CMBS Loan Performance Report | Commercial Real Estate Finance Council | https://www.crefc.org/common/Uploaded%20files/Learn/CREFCFinanceData/2025%20MarketMetrics/CREFC%20MarketMetrics%20(12-12-25).pdf | 2025-12 | 2026-04-24 | Primary industry council (Tier 1) | Agency CMBS issuance $147.9B YTD through Dec 2025; multifamily conduit spread ~152 bps over Treasuries; multifamily now ~24% of conduit collateral |
| Northmarq — Commercial Mortgage Rates & Spreads (and related research: "Sorting year: Multifamily 2026") | Northmarq | https://www.northmarq.com/insights/rates-spreads | 2026-current | 2026-04-24 | Institutional market-participant research (Tier 2) | All-in agency multifamily rates low-to-mid 5% on base case; 10-Year Treasury at ~4.2% MBA forecast; cap-rate-to-Treasury spread long-run average 314 bps (1991-2025) |
| Trepp CMBS Delinquency + Monthly CMBS Performance Report | Trepp via CREFC | https://www.crefc.org/common/Uploaded%20files/Learn/July%202025%20Monthly%20CMBS%20Loan%20Performance%20Report..pdf | 2025-07 | 2026-04-24 | Primary industry data (Tier 1) | CMBS multifamily delinquencies rose +24 bps driving total CMBS delinquency to 7.23% in July 2025; 2023-vintage multifamily conduit loans disproportionately stressed |
| Adventures in CRE — "Why Your IRR and XIRR Are Different" | Adventures in CRE | https://www.adventuresincre.com/why-your-irr-and-xirr-are-different/ | 2024-06 | 2026-04-24 | Practitioner technical reference (Tier 3) | IRR() = periodic rate, assumes equal spacing; XIRR() = annualized rate using actual dates and 365-day year (annual compounding, not continuous); material spread vs IRR on same cash-flow series (~280 bps in published worked example) |
| Wall Street Prep — XIRR Function | Wall Street Prep | https://www.wallstreetprep.com/knowledge/xirr-function/ | 2024 | 2026-04-24 | Practitioner technical reference (Tier 3) | Independent corroboration of XIRR vs IRR mechanics; confirms XIRR is correct choice for quarterly/irregular distributions |
| IRS §1031 Like-Kind Exchange + §1250/§1245 Depreciation Recapture (Accruit, R.E. Cost Seg primers) | Accruit; R.E. Cost Seg | https://www.accruit.com/blog/how-is-depreciation-recapture-tax-treated-in-a-1031-exchange/ · https://www.recostseg.com/post/bonus-depreciation-recapture-the-hidden-tax-trap-in-1031-exchanges | 2024 | 2026-04-24 | Practitioner tax reference (Tier 3) | §1031 45/180-day timeline; §1250 unrecaptured gain taxed at 25% flat; §1245 bonus-depreciation recapture hidden trap at ordinary-income rates up to 37%; equal-or-greater value + debt replacement required for full deferral |
| Exit Cap Rate Sensitivity — Corecast, Bonfire Capital, PropRise, IPG, AICN | Multiple practitioner sources | https://blog.corecastre.com/corecast-blog/exit-cap-rates-vs-growth-rates-in-terminal-value · https://www.bonfire.capital/blogs/understanding-cap-rates-and-why-sensitivity-analysis-is-critical-in-commercial-real-estate · https://ipgsf.com/entry-and-exit-cap-rates/ | 2024 | 2026-04-24 | Practitioner underwriting references (Tier 3) | Exit cap rule of thumb +25-75 bps over entry; 100 bps exit cap swing ≈ 540 bps IRR swing; exit proceeds 60-80% of total return on typical hold; existence of inversion point where longer hold raises IRR |
| Breneman Capital — "Understanding Sponsor Promotes and Waterfall Structures" | Breneman Capital | https://www.breneman.com/blog/understanding-sponsor-promotes-and-waterfall-structures-as-an-lp | 2024 | 2026-04-24 | Sponsor practitioner reference (Tier 3) | Explicit identification of the incentive-to-sell problem: IRR-based promote tiers can push GPs to sell earlier than optimal for LPs; catch-up structures and cumulative pref as mitigants |
| Adventures in CRE — Deep Dive: The IRR and XIRR | Adventures in CRE | https://www.adventuresincre.com/irr-a-cre-101/ | 2024 | 2026-04-24 | Practitioner technical reference (Tier 3) | IRR reinvestment-fallacy discussion: IRR does not actually assume reinvestment at IRR; MIRR and XIRR as remediation; academic ambiguity acknowledged |
| Trinity Real Estate — "CRE Portfolio Strategy: When to Hold or Sell Assets" | Trinity Real Estate | https://trinityre.com/cre-portfolio-strategy-when-to-hold-or-sell-assets/ | 2024 | 2026-04-24 | Practitioner process guide (Tier 3) | Annual hold/sell review cadence; opportunity-cost framework: compare IRR-continue vs. IRR-sell-and-reinvest; regular review trigger vs. event-driven |
| DS Property Experts — "Refinance vs Sell Apartment Building 2025" + Multifamily.loans "Sell or Refinance" | DS Property Experts; Multifamily.loans | https://dspropertyexperts.com/refinance-vs-sell-apartment-building-2025/ · https://www.multifamily.loans/apartment-finance-blog/should-you-sell-or-refinance-your-multifamily-property/ | 2025 | 2026-04-24 | Practitioner framework (Tier 3) | Refi closing costs 2-4% of loan amount; DSCR floor 1.25x for refis; rate-reset math: 3.5%→6.5% on $2M = +$44k/yr debt service |
| MIT SRE — Seasonality in CRE Transaction Volume and Capital Returns | MIT Center for Real Estate | https://dspace.mit.edu/handle/1721.1/37448 | 2007 (methodology), confirmed recent data 2023-2025 | 2026-04-24 | Primary academic research (Tier 2) | Q4 transaction volume distribution has statistically higher means vs. other quarters; systematic 4-quarter lag in capital returns |
| Altus Group — US CRE Transaction Analysis Q4 2025 | Altus Group | https://www.altusgroup.com/insights/us-cre-transactions/ | 2026-01 | 2026-04-24 | Institutional research (Tier 2) | Q4 2025 total CRE transaction volume $179.9B (+20.7% QoQ); December is largest month of year; Q1 slowdown is structural |
| Nareit — FTSE Nareit U.S. Real Estate Index Series + Property Sector Returns (Apartments subsector) | Nareit | https://www.reit.com/data-research/reit-indexes/historical-reit-returns/performance-property-sector-subsector | 2025-current | 2026-04-24 | Primary industry index (Tier 1) | Apartments subsector (13 REITs) YTD total return ~20% in 2025; long-run REIT returns historically competitive with broad equity; dividend yield 3.5-3.7% on apartment subsector |

**Citation tally (AM-pack tier list):** 22 total external sources. Tier 1 = 7 (ILPA, NCREIF, INREV, AvalonBay 10-K, Essex 10-K, Freddie Mac Multifamily, FHFA, CREFC, Trepp via CREFC, Nareit — count de-duplicated = 8 distinct Tier 1 bodies; for safety of count: ILPA, NCREIF, INREV, AvalonBay, Essex, Freddie Mac, FHFA, CREFC, Trepp, Nareit = **10 Tier 1**). Tier 2 = 4 (MBA, Northmarq, MIT SRE, Altus Group). Tier 3 = 8+ (AICRE, WSP, Accruit, R.E. Cost Seg, Corecast/Bonfire/PropRise/IPG, Breneman, Trinity, DS Property Experts, Multifamily.loans). Tier 1+2 total = **14**. Plus internal cross-references to `_taxonomy-seed.md`, `knowledge/underwriting-calc.md`, `knowledge/multifamily-benchmarks.md`. Gate requirement: ≥10 total sources (22 ✓), ≥6 Tier 1/2 (14 ✓). Met with margin.

## Key Findings

### 1. IRR-to-date methodology: three conventions exist and they are not equivalent

**(a) SI-IRR / Since-Inception IRR (ILPA + NCREIF institutional convention).** For a multifamily asset held mid-way through the business plan, the standard institutional practice is to compute a **Since-Inception IRR** that treats (i) original equity contributions as negative cash flows on the actual dates paid, (ii) all LP distributions received to date as positive cash flows on the actual dates received, and (iii) the **current net asset value (NAV) at the measurement date as a simulated terminal proceed**, i.e., what would be received in a hypothetical immediate disposition net of loan payoff and friction costs [ILPA Performance Template v2.0; NCREIF/PREA Reporting Standards].

**(b) Realized IRR (distributions only, no NAV).** A strictly realized IRR excludes the simulated NAV and uses only cash actually distributed. On a mid-hold asset this number is almost always negative or near zero because original equity has not yet been returned. This number is **only** useful for liquidity / distribution-pacing analysis, not for hold/sell decisions. Downstream skills should not confuse "realized IRR" with "IRR-to-date".

**(c) Time-Weighted Return (TWR, Modified Dietz).** NCREIF-style TWR measures **manager performance** by neutralizing the timing and size of capital flows; it is the standard for open-end fund benchmarking. TWR is NOT the appropriate number for a hold/sell decision on a single asset — it tells you how skillfully management ran the asset, not what the LP actually earned on their capital to date. IRR (investor-weighted) is the correct lens [NCREIF Academy].

**Convention the pack should adopt: SI-IRR with marked-to-market NAV at measurement date.** This is the ILPA-recommended convention for LP quarterly reporting and is the only number that has a mechanical bridge to "what IRR do I lock in if I sell today."

### 2. Interim-distribution handling: use XIRR, not IRR, for quarterly cash flows

Excel's `=IRR()` assumes equally spaced periodic cash flows; it returns the **effective periodic rate** (if cash flows are quarterly, IRR returns a quarterly rate that must be annualized). Excel's `=XIRR()` takes explicit dates for each cash flow and returns the **effective annual rate** using actual day-count and annual compounding (NOT continuous, NOT daily — a common misconception) [Adventures in CRE; Wall Street Prep].

- Multifamily LP distributions are typically quarterly, not year-end. Treating them as year-end cash flows (a common modeling error) materially overstates IRR, because later-dated cash is discounted more heavily than in reality.
- Adventures in CRE publishes a worked example where the same cash-flow series yields IRR = 13.45% vs. XIRR = 16.25% — a 280 bps spread driven entirely by timing convention.
- **Downstream skill convention: default to XIRR.** The skill must accept distribution dates (or at minimum quarterly tags) and compute on actual-date basis. Where the user cannot supply dates, fall back to end-of-quarter as a convention and flag the assumption.

**The reinvestment-fallacy caveat.** Both IRR and XIRR mathematically make no assumption about reinvestment rate; the popular claim that "IRR assumes distributions are reinvested at IRR" is a persistent misreading. MIRR (Modified IRR) provides an explicit reinvestment rate input for LP-level analysis when the LP needs to show blended returns assuming a specific re-deployment yield [Adventures in CRE].

### 3. Remaining-IRR projection is where the decision is actually made

The hold/sell/refi comparison collapses to three forward-looking IRRs measured from today through a common terminal date:

- **IRR-sell-today** = IRR from inception through a hypothetical disposition closing ~90 days from the measurement date, net of broker commission (typically 1.0-1.5% institutional / 2.0-3.0% middle-market), closing costs, loan prepayment penalty (if fixed-rate agency loan has yield maintenance or defeasance), and taxes (if not 1031'd).
- **IRR-hold-through-original-plan** = IRR from inception through the originally underwritten exit date, using updated remaining-period cash flows, updated forward NOI, and a revised exit cap rate reflecting current market conditions.
- **IRR-refi-and-hold** = IRR from inception through a later exit date, taking cash-out refi proceeds as an interim distribution at the refi date, with new higher debt service reducing subsequent CFADS, and a revised (typically later) exit.

**The core decision rule.** Sell if IRR-sell-today materially exceeds the *remaining marginal IRR* of IRR-hold-through-original-plan. The marginal IRR is the forward-only return on the capital you would leave in the deal by not selling — i.e., the IRR computed using only (i) today's net sale proceeds (opportunity cost of capital still invested) as the initial negative, (ii) remaining forward cash flows, and (iii) the original-plan terminal exit. If that marginal number is below the LP's alternative-use yield, sell [Trinity Real Estate; corroborated by exit-cap sensitivity analysis below].

**Exit cap rate is the dominant variable.** Practitioner sensitivity work consistently shows that a 100 bps swing in exit cap can move projected IRR by ~540 bps because disposition proceeds typically represent 60-80% of total return over a standard 5-year hold. The rule of thumb is to assume **+25-75 bps expansion over entry cap** (or +5-10 bps per year of hold as a floor) and stress ±50 bps around the base case. Any deal that only pencils at a compressed or flat exit cap is structurally fragile [Corecast; Bonfire Capital; PropRise; IPG].

**Hold-period inversion point.** There is an exit-cap level at which extending the hold period stops reducing IRR and starts *increasing* it, because the lower terminal value has decreasing marginal impact on discounted cash flows the further it sits in the future, while additional interim cash flows compound in. For heavily levered value-add deals the inversion point is typically 6-8 years; for unlevered core it pushes to 10+. This is the quantitative rebuttal to the "held five years — time to sell" heuristic.

### 4. Refinance economics: cash-out refi dominates when three conditions converge

A cash-out refi dominates continued-hold-on-existing-debt when:

1. **Rate/spread environment is friendly.** Agency all-in rates are at or below the existing loan's coupon — in 2025-2026, this is rare for a pre-2022 fixed-rate loan (5-yr Treasury and agency spreads compressed the gap meaningfully in H2 2025 but most pre-2022 paper is still below current market) [Northmarq; CREFC]. More commonly, the refi is *defensive*: extending a maturing loan to lock in duration and avoid distressed refi at the maturity wall.
2. **The after-refi DSCR and LTV clear agency constraints.** Freddie Mac requires DSCR ≥ 1.25x at high leverage (>65% LTV) and ≥ 1.55x at low leverage (≤55% LTV), with a refinance test exempting loans at DSCR ≥ 1.40x and LTV ≤ 65%. Fannie Mae is similar. Violating these forces either a smaller loan size (less cash out) or a life-co / bank alternative with different covenants [Freddie Mac Multifamily; Apartment Loan Store].
3. **The LP needs liquidity AND the tax shield of debt over sale is valuable.** Refi proceeds are **not a taxable event** (it is borrowing, not realization) — capital gains and §1250 unrecaptured-gain are deferred [DS Property Experts]. For a high-basis-differential asset (long held, significant depreciation), refi preserves the step-up-at-death tax planning optionality that a sale forecloses.

**Back-of-envelope test.** Refi cash-out NPV > Sale NPV when:

```
PV(refi proceeds) + PV(remaining levered CFADS at new debt service) + PV(deferred-exit sale proceeds)
      − PV(refi closing costs, 2-4% of new loan)
>
PV(net sale proceeds today, after tax, broker, closing, prepay penalty)
      + PV(reinvestment yield on those proceeds to same terminal date)
```

**Refi closing-cost benchmark.** 2-4% of new loan amount; on a $2M loan that is $40k-$80k. Rate examples from current market: a refi from a 3.5% coupon to a 6.5% coupon on $2M adds ~$44k/yr of debt service — real drag on CFADS that must be offset by NOI growth for the refi to be accretive vs. simply holding the existing loan to maturity [DS Property Experts; Multifamily.loans].

**Incremental DSCR at new debt level.** Downstream skill must compute: `DSCR_post-refi = Trailing 12-month NOI / New Annual Debt Service` and flag any result below 1.25x (agency floor). A DSCR under 1.25x typically forces loan downsize → less cash out → worse refi economics.

### 5. Disposition timing heuristics — strengths and failure modes

| Heuristic | Logic | When it works | When it fails |
|---|---|---|---|
| **Peak-NOI** | Sell when NOI has stabilized at business-plan target and further growth tapers to organic market rate | After value-add execution; clear evidence T-3 and T-12 NOI have converged and the convergence is on plan, not macro-driven | Misleading when the peak is temporary (short-term concession burn-off, one-time tax refund, anomalous expense control that will revert) — requires Timing-vs-Permanent variance classification per `_taxonomy-seed.md` §3 |
| **Cycle-top** | Sell when cap-rate compression has outpaced NOI growth, so that price-per-unit is at or near the historical peak multiple | Works when the owner has a credible view on the cycle AND is willing to hold cash or redeploy into another cycle's trough (most owners cannot do this consistently) | Timing the cycle is notoriously hard; pre-2022 sellers who held into rate-hike cycle gave back gains; post-2023 sellers who exited at the bottom missed the 2024-2025 spread recovery |
| **Value-add-complete** | Sell once the renovation CapEx and lease-up are done, rents are marked-to-market, and the asset has transitioned from value-add to stabilized | Cleanest heuristic analytically — the risk profile of the deal has genuinely changed, and the value-add sponsor's LP base may have different risk tolerance than a core buyer's LP base | Fails when the post-stabilization market cap rate is below expected (so the sale proceeds are strong) or the cost of re-deploying into another value-add deal is prohibitive (fewer opportunities, higher friction) |
| **Held-5-years** | Quasi-default rule driven by typical LP fund life, sponsor waterfall structures, and tax optimization (§1250 is unchanged by holding period past 1 year, so the 5-year convention is **not** tax-driven; it is LP-fund-life-driven) | Aligns with promote tiers and LP liquidity expectations | Mechanical and ignores marginal-IRR analysis; the inversion point above shows that longer holds frequently outperform on IRR |
| **REIT practice: strategic-fit + market-conditions** | AVB and ESS explicitly disclose **no fixed hold-period policy** — dispositions are triggered by (i) asset no longer fitting long-term strategy / target market, OR (ii) market pricing is favorable. Proceeds recycle into expansion-region development or acquisition [AvalonBay 2024 10-K; Essex 2024 10-K]. | REIT-scale portfolio with optionality to redeploy | Small sponsor single-asset LP deals don't have the redeployment infrastructure of a REIT; heuristic must be adapted |

**Pack recommendation: treat heuristics as screening filters, not decision triggers.** A disposition signal (peak NOI reached, 5 years elapsed, value-add complete) should trigger the IRR-sell-today vs. IRR-marginal-hold comparison — it is the comparison, not the heuristic, that decides.

### 6. Capital markets snapshot for the 2024-2026 decision window

- **10-Year Treasury.** MBA forecast ~4.2% average in 2026; long-run average 5.85% since 1990; last two Fed cuts saw the 10Y *rise* immediately, so owners must price refinancing off the long end, not the Fed funds rate [Northmarq; MBA].
- **Agency multifamily all-in rates.** Freddie Mac and Fannie Mae all-in rates in the low-to-mid 5% range for prime collateral at moderate leverage; 10-year fixed around 5.7-6.8% depending on LTV and coverage [Select Commercial; Freddie Mac]. **Workforce housing is excluded from the 2026 agency $88B cap** — so mission-driven assets have larger allocation headroom [FHFA].
- **CMBS multifamily spreads.** Conduit AAA ~78 bps, AA ~145 bps, BBB- ~450 bps; multifamily conduit spread over Treasuries ~152 bps (down from 166 bps mid-2025) — multifamily now leads the market in spread tightness [CREFC; CRED iQ]. CMBS conduit gets most competitive at mid-size ($10-50M) loans; agency usually beats it at smaller sizes.
- **Delinquency.** CMBS total delinquency 7.23% in July 2025 (+10 bps MoM), with multifamily driving +24 bps of that increase — 2023-vintage multifamily conduit loans are disproportionately stressed [Trepp via CREFC]. This informs the *distressed-disposition* overlay: sellers facing loan maturity in a stressed vintage have less negotiating leverage.
- **2026 maturity wall.** $875B of commercial mortgages mature in 2026 (17% of $5T outstanding). Only $39B (4%) is agency multifamily — the majority of the wall is bank ($396B), CMBS/CLO ($200B), and life-co ($76B) [MBA]. Owners holding bank or CMBS paper approaching maturity have sharper refi-vs-sell pressure than owners holding agency paper.
- **Cap-rate-to-Treasury spread.** 1991-2025 long-run average 314 bps; range 58 bps (June 2007) to 495 bps (December 2009). Current multifamily cap rates implying a spread near the long-run average suggest neither froth nor distress at the macro level [Northmarq].

### 7. Tax framework (citation only — NOT tax advice)

Downstream skills must reference but not opine on:

- **§1031 like-kind exchange.** Defers both capital gains and §1250/§1245 depreciation recapture IF: replacement property of equal or greater value + all net equity reinvested + debt replaced (or matched with additional cash). Missing any of the three creates taxable "boot." 45-day identification window, 180-day close window; qualified intermediary required [Accruit; LandsbergBennett].
- **§1250 unrecaptured-gain.** Depreciation previously taken on §1250 real property (buildings) is recaptured at a flat 25% federal rate at sale. This is NOT offset by prior capital losses in the same way ordinary capital gains are. A held-long multifamily with $3M of depreciation taken creates a baseline $750k federal bill before any capital-gains calc.
- **§1245 bonus-depreciation recapture trap.** Cost-segregation-studies that accelerated depreciation into §1245 personal-property buckets (appliances, carpet, parking-lot striping) are recaptured at **ordinary-income rates up to 37%**, not the §1250 flat 25% — and a 1031 that doesn't **replace like-kind §1245 property** can still trigger recapture on those buckets even when the real-property exchange is otherwise perfect [R.E. Cost Seg].
- **Step-up at death.** Holding until death eliminates the deferred tax liability via basis step-up; this is the primary estate-planning argument for refi-over-sell on a highly appreciated asset with deep depreciation history.
- **State taxes.** California, New York, Oregon, and a handful of other high-tax states add 8-13% on the federal capital-gains number; affects the sell vs. hold math materially in those geographies.

**Downstream skill rule.** Cite the framework; require the user / sponsor to engage qualified CPA / tax counsel for the actual calculation. Do not produce a specific tax number.

### 8. Opportunity cost: the reinvestment-yield benchmark

The opportunity-cost lens asks: if I sell and realize $X of net proceeds after tax and friction, what yield can I plausibly earn on $X over the remaining hold period if I don't hold this asset?

- **Pack convention: compare IRR-marginal-hold against a LP-specific alternative-yield benchmark.** The benchmark can be (i) the LP's stated target fund return (typically 12-15% for value-add, 8-10% for core), (ii) a realistic replacement-asset IRR based on current-market acquisition underwriting, or (iii) a long-duration public-market proxy (Nareit apartments subsector 10-year CAGR, currently tracking well into double digits on partial recoveries post-2022).
- If IRR-marginal-hold < alternative-yield benchmark by more than ~200 bps, the opportunity-cost argument favors sell. If within ±200 bps, qualitative factors (tax, concentration, sponsor-LP relationship) decide.
- **The "infinite ROE" trap.** A long-held, self-amortized asset can look like an "infinite return" because the investor has pulled out original basis through refis. This is not a reason to hold — it is a reason to aggressively re-measure opportunity cost on the trapped equity, because the marginal yield on equity not earning any cash-on-cash return looks much lower than the accounting ROE [Real Estate CPA / Adventures in CRE].

### 9. LP-promote structure creates an incentive distortion the skill must flag

The standard multi-tier waterfall pays GP a disproportionate share after each IRR hurdle (e.g., 80/20 to 8%, 70/30 to 12%, 50/50 thereafter). Because IRR is front-loaded — earlier cash flows compound into higher IRR — **a GP can meaningfully increase promote by selling earlier than LP-optimal** [Breneman Capital].

- Where to look: if IRR-sell-today is just above a waterfall hurdle AND IRR-marginal-hold is only ~100-200 bps below IRR-sell-today, the GP has a structural incentive to sell that an LP reviewer should scrutinize.
- Mitigating structures: (i) cumulative + compounding preferred return, (ii) catch-up provisions that smooth GP carry across time rather than incentivizing quick exits, (iii) equity-multiple hurdles alongside IRR hurdles so GP is not rewarded for accelerating exits at cost of LP total dollars returned.
- **Downstream skill requirement: compute both IRR and equity multiple for each scenario.** A deal that raises IRR by selling early but reduces equity multiple is GP-favorable, not LP-favorable.

### 10. Scenario framework: four-case comparison

The pack should standardize on a four-case comparison matrix for every hold/sell/refi analysis:

| Scenario | Definition | Key metrics to compute |
|---|---|---|
| **Hold (base case)** | Continue under current plan through original underwriting exit date, current debt unchanged | IRR-inception-to-projected-exit; Equity Multiple; Average CoC; remaining years; sensitivity to exit cap ±50 bps and ±100 bps |
| **Refi + Hold** | Cash-out refi at current market terms, distribute net refi proceeds, continue to extended exit (typically +3-5 years) | IRR-inception-to-projected-exit (with refi distribution as interim CF); Equity Multiple; DSCR-post-refi; marginal IRR on trapped equity after refi; sensitivity to rate ±50 bps and exit cap ±50 bps |
| **Sell at Current** | Dispose at current-market pricing within 60-120 days; no 1031 (assume taxable event) | IRR-sell-today; after-tax IRR; after-tax Equity Multiple; net proceeds per LP; waterfall-promote calc |
| **Sell at Stabilization** | Execute remaining value-add / lease-up, dispose at projected stabilized pricing 12-24 months forward | IRR-inception-to-stabilized-sale; marginal IRR on remaining capital from today to stabilized sale; sensitivity to lease-up execution risk and exit cap |

**Recommended ranking.** Rank scenarios by LP IRR AND LP equity multiple. If the top scenario by IRR disagrees with the top scenario by equity multiple, flag the disagreement to the decision-maker — the spread is a direct measure of LP vs. GP misalignment.

### 11. Disposition market windows: seasonality is real

- Q4 consistently produces the highest CRE transaction volume of the year; December is the single biggest month. 2024 saw $108.5B in Q4 (+33.6% QoQ); 2025 posted $179.9B (+20.7% QoQ) [Altus Group]. Academic confirmation: statistically significant Q4-volume distribution differences from 1984-2005 MIT panel.
- Q1 is the structural low — pipelines exhausted by year-end closings.
- **Practical implication for hold/sell timing:** launching a marketed process in late Q2 to close in Q4 aligns with peak buyer demand. Launching in Q3 for Q1 close is the worst combination (highest macro-uncertainty period, weakest quarter for close).
- **2026 caveat:** the maturity-wall dynamic plus agency cap expansion ($88B each) suggests Q4 2026 will be disproportionately active — but also disproportionately competitive for sellers, since distressed-hold sellers will also be in-market.

## Benchmark and Formula Decisions

- **Default IRR computation: XIRR with actual distribution dates.** Fall back to end-of-quarter if dates missing; flag assumption explicitly.
- **Default IRR-to-date convention: SI-IRR with marked-to-market NAV at measurement date** (ILPA convention). Compute realized-only IRR as a secondary metric, TWR only if the LP explicitly requests manager-performance analysis.
- **Always report IRR paired with Equity Multiple** for every scenario. Flag any scenario where the two disagree on ranking.
- **Exit cap sensitivity mandatory.** Base case + ±50 bps + ±100 bps, on every scenario. No single-point exit cap output permitted.
- **Sensitivity variables in order of typical impact (for leveraged multifamily, 5-year hold):** exit cap, rent growth rate, achieved rent premium (for value-add), expense growth, hold period, refi rate. Skill should sensitize at least the top three.
- **DSCR floor for refi: 1.25x at agency high-leverage; 1.40x+ to avoid refi test.** Any refi scenario producing post-refi DSCR < 1.25x should be flagged as non-financeable at agency and require a life-co / bank alternative with different covenants.
- **Cross-reference `knowledge/underwriting-calc.md` for core IRR and Equity Multiple formulas.** Do NOT redefine them here — Worked Example 5 (IRR) and Worked Example 6 (Equity Multiple) in underwriting-calc.md are the authoritative pack references. This research document adds the forward-looking / hold-sell-refi *application layer* on top of those formulas.
- **Cross-reference `_taxonomy-seed.md` §3 (Variance Classification) when evaluating whether observed NOI improvement is Timing / Permanent / One-Time** — this is the gating check for the "peak NOI" heuristic.
- **Cross-reference `knowledge/multifamily-benchmarks.md` for cap rate and operating-expense benchmarks** used to derive exit-cap assumptions.

## Conflicting Source Resolution

- **TWR vs. IRR for performance attribution.** NCREIF prefers TWR for manager-skill measurement in open-end funds; ILPA emphasizes IRR for LP outcome in closed-end funds. Multifamily asset management at the individual-asset level is an LP-outcome question, so the pack follows ILPA's IRR-first convention. TWR is computed only on request.
- **"Exit cap rule of thumb" variation.** Corecast / Bonfire suggest +25-75 bps over entry; IPG suggests +5-10 bps per year of hold; others (AICRE) suggest flat-to-entry in strong markets. These are all defensible; the pack convention is to **use +5 bps per year as a floor, +75 bps as a ceiling for 5-year holds, and always present sensitivity rather than a single assumption**.
- **Peak-NOI heuristic strength.** Sponsor literature (every multifamily syndication blog) loves this heuristic; institutional research is more skeptical because "peak" is only knowable retrospectively. Pack convention: use peak-NOI as a screening signal (triggers the four-scenario comparison), not as a standalone decision rule.
- **Promote-driven incentive to sell.** Breneman (sponsor voice) and Colony Hills (sponsor voice) agree this is a real distortion — an unusually consistent acknowledgment. The pack treats it as a baseline requirement to flag, not a controversial claim.
- **1031 exchange deferral vs. step-up-at-death.** Tax-planning literature is consistent: §1031 defers, death eliminates. Pack does not take a position on which is "better" — both are legitimate strategies with different implications for LP liquidity and sponsor longevity.
- **REIT hold-period policies.** AVB and ESS 10-Ks explicitly disavow fixed hold periods and instead cite strategic fit and market conditions. This directly contradicts a common sponsor-marketing claim that institutional owners operate on fixed hold periods. Pack follows the REIT disclosure language over sponsor-marketing convention.

## Edge Cases and Red Flags

- **Distressed refi scenarios.** Where current NOI will not support refi at any rational LTV, refi is mathematically dominated by sell-or-modify. Pack skill should auto-flag when computed DSCR at 75% LTV prevailing-rate debt is < 1.10x — this is a distress signal, not a refi opportunity.
- **Yield maintenance / defeasance on existing agency debt.** Fixed-rate agency loans typically carry significant prepayment penalties; a sale or refi before maturity can produce a 5-15% prepayment penalty on outstanding balance that materially reduces net proceeds. Must be modeled explicitly — ignoring it is a common underwriting error.
- **Assumable-debt value as disposition accelerant.** Where the existing loan is assumable and is priced meaningfully below current market (common on pre-2022 paper), assumable debt can add 100-300 bps to effective sale price by enabling buyer leverage that isn't otherwise available at prevailing rates. Exit cap must be adjusted for this — a lazy skill will miss it.
- **LP fund-life expiration.** If the sponsor's closed-end fund is approaching its stated termination date, the hold-vs-sell decision may be forced by fund mechanics (extension fees, LP consent) regardless of IRR math. Flag early; sometimes a deliberately-earlier sale is the right answer even if IRR-marginal-hold is attractive, because the alternative is a forced sale at a worse time.
- **Concentration-driven sale.** A single asset representing >25% of LP portfolio NAV may trigger sale even when IRR math favors hold, for diversification reasons. Skill should compute portfolio-level NAV contribution and flag if above 25% (or operator-specified) threshold.
- **Tax lock-up from recent §1031.** A property acquired via §1031 within the last 2 years carries forward the original depreciation schedule and basis; selling it non-§1031 triggers both the current sale's gain AND the previously-deferred gain. Deep-history §1031 chains can create 60-70% effective tax rates on non-exchange sales.
- **Bonus-depreciation §1245 recapture from cost-seg studies.** If the owner ran cost segregation and accelerated depreciation into §1245 buckets, a non-§1245-matched 1031 can still trigger ordinary-income recapture up to 37%. Must require disclosure of prior cost-seg work in skill intake.
- **Waterfall-hurdle-just-cleared.** If IRR-sell-today is within 50-100 bps of a promote-tier breakpoint, test whether small changes in exit cap or timing push the deal above or below the tier — GP's economic interest in the crossing may not be transparent to LPs.
- **Floating-rate debt with expiring rate cap.** A meaningfully in-the-money rate cap that expires within the next 12 months is a hidden-time-bomb that fundamentally changes the hold/sell analysis — post-expiration debt service can spike 100-300 bps overnight. Skill must ingest rate-cap expiry and strike, not just current debt terms.
- **Seasonality over-interpretation.** The Q4 seasonal peak is a distribution property, not a forecast — an individual asset marketed in Q2 doesn't under-perform because of seasonality. The correct use is process-timing, not go/no-go.

## Open Questions

- Whether the skill should support **partial-interest disposition** (e.g., recapitalization with new LP, JV partner buy-in/out) as a separate fifth scenario, or treat it as a variant of refinance.
- Whether the skill should support **fund-level roll-up** (aggregate hold/sell decisions across a fund portfolio) or remain strictly single-asset.
- Whether **UPREIT / §721 contribution to REIT OP units** should be a sixth scenario for owners with meaningful appreciated basis; this is increasingly relevant as public REITs re-emerge as buyers in 2026.
- Whether **debt-service-coverage deterioration triggers** should auto-initiate a hold/sell analysis (e.g., DSCR drops below 1.20x for two consecutive quarters) or remain a user-initiated exercise.
- Whether the skill's opportunity-cost benchmark should pull real-time Nareit apartments-subsector returns or be a user-supplied input (automation vs. explainability trade-off).
- Whether the skill should attempt to compute **after-tax IRR at the LP level** (requires knowing LP tax status — taxable, tax-exempt, pension) or present pre-tax only and leave after-tax to the LP's tax advisor.
- Whether **2026 agency cap expansion and mission-driven 50% allocation rule** warrant a dedicated "workforce-housing disposition" overlay — these assets have structurally better refi optionality than market-rate product.
