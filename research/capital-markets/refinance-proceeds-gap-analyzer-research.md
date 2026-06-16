# Refinance Proceeds Gap Analyzer Research

## Purpose

- Supports `skills/capital-markets/refinance-proceeds-gap-analyzer.md`
- Establishes how to calculate all-in payoff, supportable refinance proceeds, and total funding gap

## U.S.-Only Assumptions

- Geography: United States
- Deal type: CRE refinance, recapitalization, or payoff analysis

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| Debt Yield in CRE | Altus Group | https://www.altusgroup.com/insights/how-to-calculate-debt-yield-in-cre/ | 2020 | 2026-06-16 | Practitioner research | DSCR, LTV, and debt-yield formulas |
| Commercial Real Estate Lending Handbook | OCC | https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-real-estate-lending/pub-ch-commercial-real-estate.pdf | 2025 | 2026-06-16 | Primary regulator source | LTV and underwriting standards |
| Annual Commercial/Multifamily Loan Maturity Volumes | MBA | https://www.mba.org/news-and-research/research-and-economics/commercial-multifamily-research/commercial-multifamily-loan-maturity-volumes | n.d. | 2026-06-16 | Industry association | Maturity context |
| April 2026 SLOOS | Federal Reserve | https://www.federalreserve.gov/data/sloos/sloos-202604.htm | 2026-05 | 2026-06-16 | Primary government source | CRE lending terms and demand |
| Financial Stability Report May 2026 | Federal Reserve | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf | 2026-05-08 | 2026-06-16 | Primary government source | Refinancing vulnerability |
| Semiannual Risk Perspective Spring 2026 | OCC | https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/semiannual-risk-perspective-spring-2026.html | 2026 Spring | 2026-06-16 | Primary regulator source | CRE credit and private credit risk |
| Wall of Maturities | Principal Real Estate | https://brandassets.principal.com/m/4f0a2e32cd4949ac/original/Principal-Real-Estate-Wall-of-Maturities.pdf | 2024 | 2026-06-16 | Institutional research | Refinance pressure |
| Capital Markets Benchmarks | Local KB | knowledge/capital-markets-benchmarks.md | 2026-06-16 | 2026-06-16 | Project reference | Gap formula and sizing hierarchy |
| Rescue Capital and Preferred Equity | Federman Steifman | https://www.federmansteifman.com/2026/03/23/rescue-capital-and-the-growing-role-of-preferred-equity-in-real-estate-recapitalizations/ | 2026-03-23 | 2026-06-16 | Law firm guidance | Refinance shortfall use cases |
| Rescue Capital and Preferred Equity for CRE Gaps | Commercial Loan Direct | https://commercialloandirect.com/how-rescue-capital-preferred-equity-bridge-cre-refinance-gaps | 2026 | 2026-06-16 | Practitioner source | Gap capital concepts |

## Key Findings

- A refinance gap should include payoff, costs, reserves, and carry needs.
- Debt-yield and DSCR proceeds can diverge materially when values or rates move.
- Sensitivity is required because small NOI or rate changes can change the gap.

## Benchmark and Formula Decisions

- Use total gap = all-in payoff + reserves + closing costs - supportable proceeds.
- Require DSCR, debt-yield, and LTV supportable proceeds before recommendation.

## Conflicting Source Resolution

- Use lender-provided payoff over model estimates.
- Use current quote terms over benchmark debt constants.

## Edge Cases and Red Flags

- Refinance appears solved when paydown is funded but reserves are not.
- Stabilized NOI is used before stabilization capital is funded.

## Open Questions

- Default interest, yield maintenance, and legal fees often require lender payoff letter.
