# Development and Construction v1 Pack

## Highlights

- Added a new **Development and Construction v1** pack for U.S. ground-up development and heavy redevelopment across multifamily, industrial, retail, office, and mixed-use
- Added **4 development knowledge bases** covering development benchmarks, construction lending criteria, construction contracts and draw controls, and entitlement and site risk
- Added **12 development companion research notes** documenting source basis, cost frames, lending thresholds, contract mechanics, and land use procedure
- Added **`/cre-development`** as the 14th Claude Code plugin
- Preserved the repo's additive release framing on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, and Capital Markets v1

## Added

- 8 development skills under `skills/development/`
- 4 development knowledge bases under `knowledge/`
- 12 research notes under `research/development/`
- 1 Claude Code plugin: `claude-code-plugins/cre-development/`

## Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, ROADMAP, and CHANGELOG for `v1.6.0`
- Updated GitHub issue templates with a Development and Construction department option

## Notes

- Development and Construction v1 is **U.S.-only**
- Users are developers, development managers, owner representatives, construction lenders, and equity partners
- The pack covers the interval from site control through stabilization; stabilized-operations assumptions belong to the multifamily, industrial, office, retail, and asset management packs
- Land use is governed locally under state enabling statutes, and lien law, retainage caps, prompt-payment rules, and bond requirements are state-specific. Confirm with local land use counsel, the current municipal code, and licensed environmental and geotechnical professionals
- Every cost level, cap rate, escalation figure, and absorption assumption is directional as of its stated date and must be re-validated against current local pricing and lender feedback
- Development and Construction v1 is designed for educational decision support, not legal, tax, investment, accounting, engineering, or financing advice
- Existing multifamily, industrial, brokerage, asset management, office, capital markets, retail, legal, closing, and document-ingestion paths remain unchanged
- Strict validation should pass with `.\scripts\validate-repo.ps1 -Strict` on Windows or `python3 scripts/validate_repo.py --strict` on macOS / Linux

## Suggested Tag / Version

- `v1.6.0`
