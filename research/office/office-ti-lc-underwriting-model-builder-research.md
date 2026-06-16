# Office TI / LC Underwriting Model Builder Research

## Purpose

- Supports `skills/office/office-ti-lc-underwriting-model-builder.md`
- Intended users: office acquisition and asset management teams modeling cash flow after leasing costs

## U.S.-Only Assumptions

- Geography: United States
- Deal type: office acquisition, lease-up, renewal, bridge, refinance, and repositioning
- Market assumptions: local broker and contractor inputs control over national ranges

## Source Table

| Source | Publisher | URL | Publish Date | Access Date | Source Type | Notes |
|---|---|---|---|---|---|---|
| U.S. and Canada Office Fit-Out Costs Guide 2026 | JLL | https://www.jll.com/en-us/guides/us-canada-office-fit-out-costs-guide | 2026-05 | 2026-06-16 | Institutional cost guide | U.S.-Canada fit-out ranges |
| Office Fit Out Cost Guide Americas 2026 | Cushman & Wakefield | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-amer-regional-en-content-pds-office | 2026-03-24 | 2026-06-16 | Institutional cost guide | U.S. average costs and escalation |
| Global Office Fit-Out Costs Guide 2026 | JLL | https://www.jll.com/en-us/guides/global-office-fit-out-costs-guide | 2026 | 2026-06-16 | Institutional cost guide | Fit-out cost inflation |
| Tenant Improvement Allowance | Cushman & Wakefield | https://www.cushmanwakefield.com/en/united-states/insights/tenant-improvement-allowance | n.d. | 2026-06-16 | Practitioner market guide | TI definition and exclusions |
| BOMA Green Lease Guide | BOMA International | https://boma.org/wp-content/uploads/2024/11/BOMAgreenLeaseGuide-hr.pdf | 2018 / hosted 2024 | 2026-06-16 | Industry standards body | Work letter disbursement logic |
| Commercial Real Estate Terms and Definitions | NAIOP | https://www.naiop.org/education-and-career/industry-terms-and-definitions | n.d. | 2026-06-16 | Industry association | Concessions |
| Q1 2026 U.S. Office Market Report | CBRE | https://www.cbre.com/insights/figures/q1-2026-us-office-market-report | 2026-04-23 | 2026-06-16 | Institutional market research | Rent and lender context |
| U.S. Office Market Dynamics Q1 2026 | JLL | https://www.jll.com/en-us/insights/market-dynamics/us-office | 2026-Q1 | 2026-06-16 | Institutional market research | Leasing market context |
| vno-20251231 Form 10-K | SEC / Vornado | https://www.sec.gov/Archives/edgar/data/899689/000089968926000009/vno-20251231.htm | 2026-02 | 2026-06-16 | Primary company filing | TI and LC disclosures |
| slg-20251231 Form 10-K | SEC / SL Green | https://www.sec.gov/Archives/edgar/data/1040971/000162828026008669/slg-20251231.htm | 2026-02 | 2026-06-16 | Primary company filing | Leasing and occupancy disclosures |

## Key Findings

- Office underwriting must show cash flow after leasing costs.
- TI/LC, downtime, and free rent can overwhelm the difference between asking and taking rent.
- Renewal costs are not zero and should be modeled separately from new-tenant costs.
- Lenders may reserve for leasing costs when vacancy or rollover is material.

## Benchmark and Formula Decisions

- Include formulas for TI dollars, LC dollars, free rent, and net effective rent.
- Require in-place and stabilized views.
- Require sensitivities for downtime and TI/LC.

## Conflicting Source Resolution

- Cost guides differ, so the model should use ranges and local inputs.
- Rent growth can be positive while net cash flow remains weak due to concessions.

## Edge Cases and Red Flags

- High-finish legal, financial, medical, and lab-office build-outs need special assumptions.
- Base-building upgrades should not be hidden inside tenant TI.
- Tenant delay and rent commencement rules can shift cash timing.

## Open Questions

- Current broker commission structures and tenant-specific construction pricing require local quotes.
