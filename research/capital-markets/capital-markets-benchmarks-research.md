# Capital Markets Benchmarks Research

## Purpose

- Supports `knowledge/capital-markets-benchmarks.md`
- Establishes screening logic for debt sizing, refinance gaps, and capital-stack comparisons

## U.S.-Only Assumptions

- Geography: United States
- Deal types: acquisition debt, refinancing, maturity management, recapitalization, and rescue capital
- Use: screening and decision support, not a live quote

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| Annual Commercial/Multifamily Loan Maturity Volumes | Mortgage Bankers Association | https://www.mba.org/news-and-research/research-and-economics/commercial-multifamily-research/commercial-multifamily-loan-maturity-volumes | n.d. | 2026-06-16 | Industry association | Maturity reporting framework by year, investor group, and property type |
| MBA Commercial/Multifamily Research | Mortgage Bankers Association | https://www.mba.org/news-and-research/research-and-economics/commercial-multifamily-research | n.d. | 2026-06-16 | Industry association | Source family for debt outstanding, maturity, origination, and servicing data |
| April 2026 SLOOS | Federal Reserve | https://www.federalreserve.gov/data/sloos/sloos-202604.htm | 2026-05 | 2026-06-16 | Primary government source | Bank standards and demand for CRE loans |
| January 2026 SLOOS | Federal Reserve | https://www.federalreserve.gov/data/sloos/sloos-202601.htm | 2026-02 | 2026-06-16 | Primary government source | CRE demand and standards entering 2026 |
| Financial Stability Report May 2026 | Federal Reserve | https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf | 2026-05-08 | 2026-06-16 | Primary government source | CRE prices stabilizing but refinancing vulnerabilities remain |
| Semiannual Risk Perspective Spring 2026 | OCC | https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/semiannual-risk-perspective-spring-2026.html | 2026 Spring | 2026-06-16 | Primary regulator source | CRE refinancing and private credit risk |
| Commercial Real Estate Lending Comptroller's Handbook | OCC | https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-real-estate-lending/pub-ch-commercial-real-estate.pdf | 2025 | 2026-06-16 | Primary regulator source | LTV, underwriting, administration, and credit-risk guidance |
| Debt Yield in CRE | Altus Group | https://www.altusgroup.com/insights/how-to-calculate-debt-yield-in-cre/ | 2020 | 2026-06-16 | Practitioner research | LTV, DSCR, and debt-yield formulas and sizing discussion |
| Unpacking the Wall of Maturities | Principal Real Estate | https://brandassets.principal.com/m/4f0a2e32cd4949ac/original/Principal-Real-Estate-Wall-of-Maturities.pdf | 2024 | 2026-06-16 | Institutional research | Maturity wall by property type and capital source |
| 2026 CRE Outlook | Deloitte | https://www.deloitte.com/us/en/insights/industry/financial-services/financial-services-industry-outlooks/commercial-real-estate-outlook.html | 2025 | 2026-06-16 | Institutional research | Capital availability and cost of capital as key concerns |

## Key Findings

- Debt sizing should use DSCR, debt yield, LTV, and reserve needs together.
- Refinance gaps require all-in payoff plus reserves and costs, not just principal balance.
- Lender appetite varies by property type, quality, tenancy, and capital source.
- Maturity timing is a separate risk from asset value and NOI support.

## Benchmark and Formula Decisions

- Include DSCR, debt yield, LTV, LTC, debt constant, break-even occupancy, and refinance gap formulas.
- Use directional DSCR, debt-yield, and LTV ranges by property condition and type.
- Require lowest credible proceeds test to control.

## Conflicting Source Resolution

- Live lender quotes override static ranges.
- Regulator guidance is treated as a risk frame; practitioner ranges are treated as screening heuristics.

## Edge Cases and Red Flags

- Stabilized proceeds should not be used before stabilization is funded.
- A maturity may be low leverage but still fail from DSCR or debt-yield pressure.

## Open Questions

- Live spreads, floors, lender reserves, and recourse posture require current quotes.
