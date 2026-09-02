# Lender / Credit v1 Pack

## Highlights

- Added a new **Lender / Credit v1** pack covering the LENDER side of U.S. commercial real estate: banks, credit unions, debt funds, life companies, agency DUS / Optigo lenders, and CMBS originators screening, underwriting, approving, monitoring, reviewing, and working out CRE loans
- Added **4 lender / credit knowledge bases** covering credit policy benchmarks, regulatory risk rating and classification, credit memo and appraisal review standards, and CRE concentration and stress testing
- Added **12 lender / credit companion research notes** documenting source basis, supervisory guidance, assumptions, and issue-spotting logic
- Added **`/cre-lender-credit`** as the 13th Claude Code plugin
- Preserved the repo's additive release framing on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, and Capital Markets v1

## Added

- 8 lender / credit skills under `skills/lender-credit/`
- 4 lender / credit knowledge bases under `knowledge/`
- 12 research notes under `research/lender-credit/`
- 1 Claude Code plugin: `claude-code-plugins/cre-lender-credit/`

## Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, ROADMAP, and CHANGELOG for `v1.6.0`
- Updated GitHub issue templates with a Lender / Credit department option

## Notes

- Lender / Credit v1 is **U.S.-only**
- This is the **first credit-side pack** in the repo. Every existing pack is borrower, owner, or seller side; this one is the mirror
- Users are credit analysts, underwriters, portfolio managers, credit officers, loan review, and special assets
- The supervisory classification, nonaccrual, charge-off, allowance, and regulatory reporting framework applies to U.S. banks, thrifts, and credit unions. Non-bank lenders use internal or rating-agency grades instead
- Classification, nonaccrual, allowance, and regulatory reporting conclusions belong to the institution and its regulator; the pack is educational decision support, not legal, accounting, regulatory, investment, or financing advice
- Existing multifamily, industrial, brokerage, asset management, office, capital markets, retail, legal, closing, and document-ingestion paths remain unchanged
- Strict validation should pass with `.\scripts\validate-repo.ps1 -Strict` on Windows or `python3 scripts/validate_repo.py --strict` on macOS / Linux

## Suggested Tag / Version

- `v1.6.0`
