# Retail v1 Pack

## Highlights

- Added a new **Retail v1** pack for U.S. retail acquisitions, refinancings, and asset reviews across grocery-anchored, power, strip / unanchored, lifestyle, mall, mixed-use retail, pad, and single-tenant net lease (STNL) assets
- Added **4 retail knowledge bases** covering retail benchmarks, lease structures, tenant sales and occupancy cost, and lender criteria
- Added **12 retail companion research notes** documenting source basis, assumptions, formulas, and issue-spotting logic
- Added **`/cre-retail`** as the 12th Claude Code plugin
- Preserved the repo's additive release framing on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, and Capital Markets v1

## Added

- 8 retail skills under `skills/retail/`
- 4 retail knowledge bases under `knowledge/`
- 12 research notes under `research/retail/`
- 1 Claude Code plugin: `claude-code-plugins/cre-retail/`

## Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, ROADMAP, and CHANGELOG for `v1.6.0`
- Updated GitHub issue templates with a Retail department option

## Notes

- Retail v1 is **U.S.-only**
- Retail is lease-driven and sales-driven: tenant sales, occupancy cost, anchor health, co-tenancy, exclusives, and CAM recovery structure control value
- Reported tenant sales are unaudited landlord reporting, not GAAP revenue; issuer-published occupancy cost figures are non-GAAP operating statistics
- Co-tenancy, radius, continuous-operation, and liquidated-damages provisions are state-law specific and belong to counsel
- Retail v1 is designed for educational decision support, not legal, tax, investment, accounting, or financing advice
- Existing multifamily, industrial, brokerage, asset management, office, capital markets, legal, closing, and document-ingestion paths remain unchanged
- Strict validation should pass with `.\scripts\validate-repo.ps1 -Strict` on Windows or `python3 scripts/validate_repo.py --strict` on macOS / Linux

## Suggested Tag / Version

- `v1.6.0`
