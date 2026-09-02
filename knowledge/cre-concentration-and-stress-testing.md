# CRE Concentration and Stress Testing

Last updated: 2026-09-01

Scope: U.S. regulated depository CRE lending. This is an educational credit-risk reference for credit analysts, portfolio managers, credit officers, and loan review, not legal, accounting, regulatory, investment, or financing advice. Supervisory expectations come from your primary federal regulator and your board-approved policy; confirm current thresholds, denominators, and scenario assumptions with your risk, finance, and regulatory reporting teams. Non-depository lenders (debt funds, life companies, CMBS originators) are not subject to this framework. Market data below is time-sensitive and directional.

---

## Current Context

- The 2006 interagency screening criteria are unchanged: construction, land development and other land loans at 100 percent or more of capital, or total CRE at 300 percent or more of capital combined with 50 percent or more CRE growth over the prior 36 months (Concentrations in Commercial Real Estate Lending, Sound Risk Management Practices, December 12, 2006). Since March 31, 2020 the supervisory denominator has been tier 1 capital plus the allowance for credit losses attributed to loans and leases, not total risk-based capital (OCC Bulletin 2020-29 / SR 20-8, March 30, 2020).
- MBA reported on February 9, 2026 that $875 billion, or 17 percent, of the $5.0 trillion of outstanding commercial and multifamily mortgages matures during 2026, with depositories holding $396 billion of it (21 percent of their holdings). Maturity, not term default, is the live exposure.
- Trepp data reported July 27, 2026 put June 2026 CMBS delinquency at 7.35 percent overall and 11.57 percent for office, with 65 percent of newly delinquent balances being non-performing matured balloon loans. FDIC's Quarterly Banking Profile for Q2 2026 (released August 25, 2026) put nonfarm nonresidential CRE past-due and nonaccrual at 1.52 percent against an industry rate of 1.44 percent. The two populations and definitions are not comparable.
- The Federal Reserve's June 24, 2026 stress test used a 39 percent CRE price decline in the severely adverse scenario and projected roughly $75 billion of CRE loan losses across 32 large banks. That is a CCAR / DFAST scenario for large firms and a directional reference only, not a required assumption for a smaller institution's internal test.

---

## The Supervisory Screening Criteria

| Criterion | Numerator | Threshold |
|---|---|---|
| Construction concentration | Construction, land development and other land loans | 100 percent or more of capital (no growth condition) |
| Total CRE concentration | Total non-owner-occupied CRE loans as defined by the guidance | 300 percent or more of capital **and** 50 percent or more growth over the prior 36 months |
| Denominator, both tests | Tier 1 capital plus ACL attributed to loans and leases | ALLL for institutions that have not adopted ASC 326 |

```
Construction Ratio = Construction, Land Development and Other Land Loans / (Tier 1 Capital + ACL)
Total CRE Ratio    = Total Non-Owner-Occupied CRE Loans / (Tier 1 Capital + ACL)
36-Month Growth    = (Current CRE Balance / CRE Balance 36 Months Prior) - 1
```

Four points the guidance states plainly and that are routinely misread:

- These are screening indicators for further supervisory analysis, not lending limits. The guidance sets no CRE concentration limit that applies to all institutions.
- They are not a safe harbor. An institution below both criteria can still be criticized when other risk indicators are present.
- Stratification must be reasonable and supportable, and the portfolio must not be sliced into segments simply to avoid the appearance of concentration.
- CRE here means loans where cash flow from the real estate is the primary repayment source, plus construction and land. Owner-occupied nonfarm nonresidential loans repaid by the occupying business are excluded from the ratio, though not from portfolio risk analysis. Loans to REITs and unsecured loans to developers are included when their performance tracks CRE markets.

---

## Segmenting the Book

| Dimension | Named in the 2006 guidance | Why a credit officer cares |
|---|---|---|
| Property type | Yes | Correlated demand shocks; office and ADC behave nothing like stabilized multifamily |
| Geographic market | Yes | Single-MSA employment and supply shocks |
| Tenant and tenant-industry concentration; developer / sponsor concentration | Yes | One employer, industry, or sponsor driving many buildings' NOI |
| Risk rating | Yes | Feeds migration analysis and ACL segmentation |
| Loan structure (fixed vs adjustable) and purpose (construction, short-term, permanent) | Yes | Sizes rate-shock exposure; construction and ADC carry the heaviest stress expectations |
| LTV and DSC bands | Yes | Identifies the thin-coverage tail before it migrates |
| Policy exceptions on new credits, and affiliated loans such as loans to tenants | Yes | Underwriting drift, and hidden correlation between borrower and rent roll |
| Maturity ladder (12 / 24 / 36 months) and IO-to-amortizing conversion | Implied by MIS and examiner procedures | The live 2026 exposure; drives the refinance test and coverage at conversion |

Cross-tab the maturity ladder against risk rating and property type. A book that looks diversified by property type can still be concentrated in a single quarter of maturities.

---

## Designing the Stress Test

Scale the method to the portfolio. The guidance is explicit that a sophisticated portfolio model is not required and that testing may be as simple as applying stressed loss rates to the CRE portfolio, capital, and earnings, and that well-margined seasoned multifamily normally needs less robust testing than most acquisition, development, and construction lending.

| Design choice | Options | Practical guidance |
|---|---|---|
| Level | Transaction-level vs portfolio-level | Do both; transaction-level feeds the bottom-up roll-up |
| Portfolio approach | Bottom-up (aggregate loan-level results) vs top-down (stressed loss rates on similar pools) | Bottom-up where loan-level data exists; top-down for thin-data segments, labeled as such |
| Test type | Sensitivity (one variable moved in isolation) vs scenario (a coherent multi-variable narrative) | Sensitivity to find the breaking variable; scenario to size capital impact |
| Sample | Vulnerable segments: low DSC, high LTV, single geography, property type, or industry | Guidance directs focus to vulnerable segments, not the whole book equally |
| Frequency and validation | At least annual, with periodic independent validation | More often for fast-growing or criticized-heavy segments; examiners ask for validation by name |

Shock variables named in FDIC examination procedures:

| Variable | Test | What it exposes |
|---|---|---|
| Interest rates | Rate shock on floating balances and at repricing or maturity | Coverage failure on adjustable and IO-to-amortizing loans |
| Property values | Value decline on as-is collateral | LTV migration, guarantor reliance, loss given default |
| Capitalization or discount rates | Cap-rate expansion applied to in-place NOI | Value decline independent of NOI; the refinance gap |
| Vacancy and absorption | Occupancy decline, slower lease-up | Construction and lease-up exposure; NOI timing |
| Net operating income | NOI decline, with and without expense relief | Coverage and debt yield compression |

Two composite tests worth running by name:

- **Maturity refinance test.** For each loan maturing inside the horizon, re-size proceeds at a stressed constant and stressed cap rate against stressed NOI, then measure the gap to current balance. Matured-balloon defaults dominating new CMBS delinquency in June 2026 is why this test earns its place.
- **Migration analysis.** Track risk-rating movement by segment and vintage, then project stressed ratings forward. MIS reporting is expected to show changes in the portfolio's risk profile including risk-rating migrations, which is the bridge from stress output to classification and ACL.

Cash-flow math (DSCR, debt yield, LTV, cap rate, NOI) is not restated here. Use [Underwriting Calculations](knowledge/underwriting-calc.md).

Severity is a board decision, not a published benchmark. No regulator sets the required shock size for an individual institution. Anchor it to the institution's own worst historical segment loss experience, current market data by MSA and property type, and the board's post-stress capital floor. A public CCAR / DFAST scenario value may be used as a directional upper bound if it is labeled as borrowed. State the horizon, the variable path, and the source of every assumption; an undocumented shock size is itself the finding.

---

## Feeding Results Into Capital, ACL, and Policy

Examiners ask whether stress results are actually used. FDIC examination procedures list the destinations, and OCC community bank stress testing guidance ties results to capital planning and allowance provisioning.

| Destination | What changes when results are bad |
|---|---|
| CRE strategy and growth targets | Slow or redirect origination in the failing segment |
| Concentration limits and sublimits | Tighten board-approved limits; add a segment sublimit |
| Underwriting and pricing | Raise coverage and debt yield floors, reprice, tighten exception tolerance |
| Capital planning | Test post-stress ratios against the board floor; if breached, plan capital or concentration reduction |
| ACL under ASC 326 | Inform segmentation, qualitative factors, and reasonable-and-supportable forecasts; the estimation process must be designed, documented, validated, and controlled |
| Staffing, workout capacity, and liquidity | Build special assets and appraisal review capacity ahead of the migration, and keep funding diverse, since CRE and funding stress correlate |

The 2006 guidance closes the loop on capital: an institution without capital adequate to buffer unexpected losses from a CRE concentration should plan either to reduce the concentration or to hold capital appropriate to it. FDIC's December 2023 advisory pairs that with appropriate credit loss allowances, current borrower financial information, workout infrastructure, and liquidity.

---

## Questions to Ask Before Signing Off on a Portfolio Review

- Which denominator produced this ratio, and does the CRE numerator capture REIT loans, unsecured developer lines, and participations rather than only collateral-coded real estate?
- Can the system produce current NOI, DSC, LTV, maturity date, rate type, and property type at the loan level, or is the test running on estimates?
- What share of the book matures in 12, 24, and 36 months, and how much of that fails a stressed refinance test today?
- Which single variable breaks the portfolio first, at what level, and where did that severity assumption come from?
- When was the methodology last independently validated, and what changed in policy, limits, pricing, capital, or ACL after the last run?

---

## Red Flags

- Concentration ratio quoted without naming the denominator or the CRE definition behind it.
- The 300 percent criterion treated as a hard cap, or as a safe harbor below which no analysis is required.
- Stress testing performed on aggregate balances because loan-level NOI, DSC, and maturity data are unreliable.
- Scenario severity copied from a public CCAR / DFAST scenario with no statement that it was borrowed and no institution-specific calibration.
- A maturity ladder with no refinance test, in a year when maturities and matured-balloon defaults are the dominant CRE credit event.
- Stress results presented to the board with no resulting change to limits, underwriting, pricing, capital plan, or ACL assumptions, or no independent validation of the stress methodology at all.
- Contingency plans that assume loan sales or securitization in the same stress that would close those markets, or growth in a segment outrunning the ability to underwrite, monitor, and work out loans in it.

---

## Related Research

- [CRE Concentration and Stress Testing Research](research/lender-credit/cre-concentration-and-stress-testing-research.md)
