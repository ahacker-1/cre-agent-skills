# CRE Concentration and Stress Testing Research

## Purpose

- Supports `knowledge/cre-concentration-and-stress-testing.md`
- Supports the Lender / Credit v1 pack skills that read portfolio-level exposure, in particular `skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md` and `skills/lender-credit/annual-loan-review-and-risk-rating.md`
- Intended users: credit analysts, portfolio managers, credit officers, loan review, and CRE risk staff at banks, credit unions, and other regulated CRE lenders

## U.S.-Only Assumptions

- Geography: United States
- Institution type: U.S. federally insured depository institutions and their holding companies. Non-depository CRE lenders (debt funds, life companies, CMBS originators) are not subject to this supervisory framework but often borrow its vocabulary for internal limits.
- Deal type: income-producing CRE and construction / land development exposure held on balance sheet
- Regulatory assumptions: the OCC, Federal Reserve, and FDIC interagency framework governs. Credit unions follow NCUA rules, which are not covered here.
- Accounting assumptions: ASC 326 (CECL) is the operative credit loss standard for the institutions covered.
- This is educational decision support, not legal, accounting, regulatory, investment, or financing advice.

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| Concentrations in Commercial Real Estate Lending, Sound Risk Management Practices (attachment to SR 07-01) | Board of Governors of the Federal Reserve System / OCC / FDIC | https://www.federalreserve.gov/boarddocs/srletters/2007/SR0701a2.pdf | 2006-12-12 | 2026-09-01 | Primary regulator guidance | Full text of the 2006 interagency guidance: scope, stratification, seven risk management elements, the two supervisory criteria, capital assessment |
| Interagency Guidance on CRE Concentration Risk Management (Bulletin 2006-46) | OCC | https://www.occ.gov/news-issuances/bulletins/2006/bulletin-2006-46.html | 2006-12-06 | 2026-09-01 | Primary regulator guidance | OCC transmittal of the 2006 guidance; confirms the guidance sets no lending limit |
| Real Estate Lending: Interagency Statement on Prudent Risk Management for CRE Lending (Bulletin 2015-51) | OCC | https://www.occ.gov/news-issuances/bulletins/2015/bulletin-2015-51.html | 2015-12-18 | 2026-09-01 | Primary regulator guidance | Agencies' observations on easing underwriting and rising concentrations; reinforces 2006 framework |
| Credit Concentrations: Joint Statement on Adjustment to the Calculation for Credit Concentration Ratios (Bulletin 2020-29) | OCC | https://www.occ.gov/news-issuances/bulletins/2020/bulletin-2020-29.html | 2020-03-30 | 2026-09-01 | Primary regulator guidance | Denominator for supervisory concentration ratios changed to tier 1 capital plus ACL / ALLL effective 2020-03-31 |
| Advisory: Managing Commercial Real Estate Concentrations in a Challenging Economic Environment (FIL-64-2023) | FDIC | https://www.fdic.gov/news/financial-institution-letters/2023/fil23064.html | 2023-12-18 | 2026-09-01 | Primary regulator guidance | Six risk-management actions: capital, ACL, portfolio management, current financial information, workout infrastructure, liquidity |
| Risk Management Manual of Examination Policies, Concentrations in Commercial Real Estate Lending examination module (10/25) | FDIC | https://www.fdic.gov/risk-management-manual-examination-policies/concentrations-commercial-real-estate-lending.pdf | 2025-10 | 2026-09-01 | Primary examiner procedures | Examiner procedures 26-40: MIS content, segment monitoring, stress test sample selection, shock variables, independent validation, use of results |
| Community Bank Stress Testing: Supervisory Guidance (Bulletin 2012-33) | OCC | https://www.occ.gov/news-issuances/bulletins/2012/bulletin-2012-33.html | 2012-10-18 | 2026-09-01 | Primary regulator guidance | Transaction vs portfolio level, top-down vs bottom-up, sensitivity vs scenario analysis, at least annual frequency, links to capital and ALLL |
| Comptroller's Handbook: Concentrations of Credit, Version 2.0 | OCC | https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/concentrations-of-credit/pub-ch-concentrations.pdf | 2020-10 | 2026-09-01 | Primary examiner handbook | Concentration definition, ratio construction, segmentation dimensions, board limits and sublimits, links to capital and ACL |
| Current Expected Credit Losses: Interagency Policy Statement on Allowances for Credit Losses, revised April 2023 (Bulletin 2023-11) | OCC | https://www.occ.treas.gov/news-issuances/bulletins/2023/bulletin-2023-11.html | 2023-04-21 | 2026-09-01 | Primary regulator guidance | ASC 326 measurement, estimation process design and validation, board and management responsibilities, TDR references removed |
| Federal Reserve Board's annual bank stress test results (press release) | Board of Governors of the Federal Reserve System | https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260624a.htm | 2026-06-24 | 2026-09-01 | Primary regulator publication | 2026 severely adverse scenario: 39% CRE price decline, 30% house price decline, 10% unemployment peak; ~$75B CRE loan losses; aggregate CET1 decline 1.6 percentage points across 32 banks |
| Quarterly Banking Profile, Second Quarter 2026 | FDIC | https://www.fdic.gov/quarterly-banking-profile/quarterly-banking-profile-second-quarter-2026.pdf | 2026-08-25 | 2026-09-01 | Primary regulator data | Industry past-due and nonaccrual rate 1.44%; nonfarm nonresidential CRE PD/NA 1.52%, down 14 bps; industry net charge-off rate 0.57%; community bank nonfarm nonresidential CRE balances up 6.6% year over year |
| 17 Percent of Commercial and Multifamily Mortgage Balances to Mature in 2026 | Mortgage Bankers Association | https://www.mba.org/news-and-research/newsroom/news/2026/02/09/17-percent-of-commercial-and-multifamily-mortgage-balances-to-mature-in-2026 | 2026-02-09 | 2026-09-01 | Quasi-primary association survey | $875B of $5.0T maturing in 2026 (17%); depositories $396B (21% of their holdings); office 17%, hotel 30%, industrial 23%, multifamily 13% |
| 2026 CMBS Delinquency Rates (Trepp data) | Commercial Property Executive / CommercialSearch, reporting Trepp | https://www.commercialsearch.com/news/cmbs-delinquency-rates/ | 2026-07-27 | 2026-09-01 | Institutional market data via trade press | June 2026 overall CMBS delinquency 7.35%; office 11.57%, multifamily 7.23%, retail 6.91%, lodging 5.22%, industrial 1.20%; 65% of newly delinquent balances were non-performing matured balloons |

## Key Findings

### The 2006 guidance defines scope, not a limit

- The guidance covers CRE loans "for which the cash flow from the real estate is the primary source of repayment," and expressly excludes owner-occupied nonfarm nonresidential loans where repayment comes from the operating business. Loans to REITs and unsecured loans to developers are in scope when performance is closely linked to CRE markets.
- Two supervisory screening criteria: (1) construction, land development, and other land loans at 100 percent or more of total capital; or (2) total CRE loans at 300 percent or more of total capital **and** CRE portfolio growth of 50 percent or more during the prior 36 months.
- The guidance states the criteria "do not constitute limits on an institution's lending activity but rather serve as high-level indicators," and are not a safe harbor when other risk indicators are present. It "does not establish a CRE concentration limit that applies to all institutions."
- Since 2020-03-31 the supervisory denominator is tier 1 capital plus the allowance (ACL under ASC 326, ALLL otherwise), not the total risk-based capital originally referenced in the 2006 footnotes.

### Segmentation is prescribed, and gaming it is called out

- Institutions are "encouraged to stratify the CRE portfolio by property type, geographic market, tenant concentrations, tenant industries, developer concentrations, and risk rating."
- Other named stratifications: loan structure (fixed or adjustable), loan purpose (construction, short-term, or permanent), loan-to-value limits, debt service coverage, policy exceptions on newly underwritten credit facilities, and affiliated loans such as loans to tenants.
- Stratification "should be reasonable and supportable" and the portfolio "should not be divided into multiple segments simply to avoid the appearance of concentration risk."
- MIS reporting should show changes in the portfolio's risk profile "including risk-rating migrations," which is the guidance hook for migration analysis.

### Stress testing expectations scale with the book

- The 2006 guidance requires portfolio-level stress tests or sensitivity analysis to quantify the effect of changing economic conditions on asset quality, earnings, and capital, focused on the more vulnerable segments. It explicitly says a sophisticated portfolio model may not be required and testing "may be as simple as analyzing the potential effect of stressed loss rates on the CRE portfolio, capital, and earnings."
- It also distinguishes risk by product: "well-margined and seasoned performing loans on multifamily housing normally would require significantly less robust stress testing than most acquisition, development, and construction loans."
- The FDIC examination module lists shock variables directly: increases in interest rates, overall changes in property values, changes in property vacancy or absorption rates, declines in NOI, and changes in capitalization or discount rates. It also lists the MIS inputs stress testing needs: stratified portfolios, recent interest and capitalization rates, NOI, average LTV and DSC, and current client / tenant operating incomes.
- The module asks examiners whether the methodology considers volatility in supply and demand for lots, retail and office space, and multifamily units across business cycles, and whether the model or methodology is subject to periodic comprehensive independent validation.
- OCC Bulletin 2012-33 separates transaction-level testing (single borrower under stress) from portfolio-level testing, and portfolio-level into bottom-up (aggregate loan-level results) and top-down (apply stressed loss rates to pools with similar characteristics). It frames scenario analysis as a coherent narrative across multiple variables versus sensitivity analysis as isolated variable moves, and expects at least annual testing.

### Results have to go somewhere

- The FDIC module asks examiners to determine whether stress test results and sensitivity analyses are factored into CRE strategies, policies, staffing and managerial needs, capital planning, funding requirements, underwriting criteria, loan pricing, and risk limits.
- OCC 2012-33 links results to capital planning (whether ratios could fall below adequacy thresholds) and to allowance provisioning.
- FIL-64-2023 pairs capital maintenance and appropriate credit loss allowances with portfolio monitoring, current borrower financial information, workout infrastructure, and liquidity, and points institutions back to both the 2006 guidance and the revised 2023 ACL policy statement.
- The 2023 ACL policy statement governs the estimation process itself under ASC 326: design, documentation, validation, internal controls, and board and management responsibilities. It removed TDR recognition and measurement following ASU 2022-02.
- The 2006 guidance closes with the capital point: an institution with inadequate capital to buffer unexpected losses from a CRE concentration "should develop a plan for reducing its CRE concentrations or for maintaining capital appropriate to the level and nature of its CRE concentration risk."

### Directional market context as of access date

- MBA's February 2026 survey put $875 billion, or 17 percent, of the $5.0 trillion of outstanding commercial and multifamily mortgages as maturing during 2026, down 9 percent from the $957 billion scheduled for 2025. Depositories held $396 billion of that, 21 percent of their holdings.
- Trepp data reported in July 2026 showed overall CMBS delinquency of 7.35 percent for June 2026 with office at 11.57 percent, and 65 percent of newly delinquent balances were non-performing matured balloon loans, which is a maturity-default signal rather than a term-default signal.
- FDIC's Q2 2026 Quarterly Banking Profile reported the industry past-due and nonaccrual rate at 1.44 percent, with nonfarm nonresidential CRE at 1.52 percent (down 14 basis points in the quarter) and the industry net charge-off rate at 0.57 percent. Community bank nonfarm nonresidential CRE balances were up 6.6 percent year over year.
- The Federal Reserve's June 2026 stress test used a 39 percent CRE price decline in the severely adverse scenario and projected roughly $75 billion of CRE loan losses across 32 large banks, with aggregate CET1 falling 1.6 percentage points.

## Benchmark and Formula Decisions

Suitable as repo defaults, because each is stated in a regulator document:

- Construction / land development at 100 percent or more of capital: supervisory screening criterion (2006 guidance).
- Total non-owner-occupied CRE at 300 percent or more of capital combined with 50 percent or more growth in 36 months: supervisory screening criterion (2006 guidance).
- Denominator = tier 1 capital plus ACL (or ALLL for non-CECL filers) for supervisory concentration ratios (OCC 2020-29 / SR 20-8), effective 2020-03-31.
- Segmentation dimensions listed above, taken verbatim from the 2006 guidance.
- Stress variables (interest rate, property value, vacancy / absorption, NOI, cap rate / discount rate) taken from the FDIC examination module.
- Stress testing frequency of at least annual (OCC 2012-33).
- Requirement that stress results feed strategy, policy, staffing, capital planning, funding, underwriting, pricing, and risk limits (FDIC examination module).

Must stay case-by-case, because no regulator publishes a number:

- The size of the shock. Nothing in the guidance sets a required NOI decline, cap-rate expansion, vacancy increase, or rate shock. The Federal Reserve's supervisory scenario (39 percent CRE price decline in 2026) applies to large bank holding companies under CCAR / DFAST and is a directional reference point only. It is not a required assumption for a community or regional bank's internal test, and any institution borrowing it should say so.
- Internal concentration limits and sublimits. The 2006 guidance and the Concentrations of Credit handbook both require board-approved limits but leave the levels to the institution's risk appetite, capital, and management capacity.
- Risk-rating migration thresholds, watchlist triggers, and criticized-asset tolerances.
- Any pass / fail capital ratio after stress. Institutions set their own post-stress capital floors above regulatory minimums.

Formulas: this knowledge base does not restate CRE cash flow math. Debt yield, DSCR, LTV, cap rate, and NOI definitions live in [Underwriting Calculations](knowledge/underwriting-calc.md) and should be cited from there rather than duplicated.

Concentration ratio construction used in the knowledge base:

```
Construction Concentration Ratio = Construction, Land Development and Other Land Loans
                                 / (Tier 1 Capital + ACL attributed to loans and leases)

Total CRE Concentration Ratio = Total Non-Owner-Occupied CRE Loans (as defined by the 2006 guidance)
                              / (Tier 1 Capital + ACL attributed to loans and leases)

36-Month Growth Test = (Current CRE Balance / CRE Balance 36 Months Prior) - 1
```

## Conflicting Source Resolution

- **Denominator conflict.** The 2006 guidance's footnotes define "total capital" as total risk-based capital from Call Report schedule RC-R. The 2020 joint statement (OCC 2020-29 / SR 20-8) changed the supervisory calculation to tier 1 capital plus the allowance. The later, more specific interagency statement controls for supervisory ratio purposes; the 2006 text is left as historical context. Institutions frequently still report the legacy total risk-based capital version internally, so any figure should be labeled with its denominator.
- **"Is 300 percent a limit?"** Trade press and vendor commentary routinely describe 300 percent as a cap or a trigger for mandatory action. The guidance itself says the criteria are high-level indicators and not limits, and not a safe harbor. Regulator text controls; the knowledge base states this explicitly because the misreading is common.
- **Stress test severity.** Public CCAR / DFAST scenario values are widely quoted as if they were the standard for all banks. The Federal Reserve applies them to the large firms in its test population; the community bank guidance (OCC 2012-33) instead scales method and severity to portfolio risk and complexity. Both are cited, with the CCAR values labeled directional.
- **Delinquency data.** FDIC Call Report based CRE past-due and nonaccrual (1.52 percent for nonfarm nonresidential in Q2 2026) and Trepp CMBS delinquency (7.35 percent overall, 11.57 percent office in June 2026) measure different populations under different definitions and are not comparable. Both are reported with their population named.

## Edge Cases and Red Flags

- Owner-occupied CRE sits outside the 2006 guidance's CRE definition but still carries real estate collateral risk and often shares sponsors with investor CRE. Excluding it from the supervisory ratio is correct; excluding it from portfolio risk analysis is not.
- Multifamily is inside the supervisory CRE definition even though the guidance names well-structured multifamily finance as historically lower risk. Segments should not be dropped from the ratio because they feel safer.
- Construction loans that convert to permanent, and interest-only loans that convert to amortizing, need forward-looking coverage testing; the FDIC module asks examiners to check exactly this.
- Loans to REITs and unsecured developer lines can be missed by collateral-code-driven MIS but belong in CRE exposure when their performance tracks CRE markets.
- Participations, syndications, and loans to non-depository financial institutions secured indirectly by CRE can create hidden correlation; the guidance asks that management evaluate the degree of correlation between related real estate sectors.
- Contingency plans that rely on selling or securitizing CRE assume secondary market access that may close in the same stress being modeled. The guidance asks management to periodically assess marketability.
- Data quality is the most common failure point in practice: stress testing on a portfolio that cannot produce current NOI, LTV, DSC, maturity date, rate type, and property type at the loan level is estimation, not measurement, and should be labeled that way.
- Non-bank CRE lenders (debt funds, life companies, CMBS originators) are not subject to this framework. Applying bank concentration ratios to them without saying so misstates their constraints.

## Open Questions

- Whether an institution's own internal concentration limits, watchlist triggers, and post-stress capital floors are appropriate is a board and examiner judgment; no published benchmark substitutes for it.
- Credit union CRE concentration treatment under NCUA rules is out of scope here and would need its own research.
- Cap-rate and value assumptions for stress testing vary by market and property type and require current third-party market data at the time of use; nothing in this note fixes them.
- The interaction between CECL model assumptions and stress-scenario assumptions (double counting, or scenario weighting) is an accounting and model-governance question that requires the institution's own auditors and model validators.
- HVCRE capital treatment, appraisal and evaluation requirements, and FIRREA thresholds are covered by sibling files in this pack and are not researched here.
