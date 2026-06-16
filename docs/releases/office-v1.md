# Office v1 and Repo Validation

## Highlights

- Added a new **Office v1** sector pack for U.S. office acquisitions, refinancings, recapitalizations, lease-up, tenant credit, TI/LC underwriting, financing fit, and investment committee memo writing
- Added **4 office knowledge bases** for office benchmarks, lease structures, TI/LC economics, and lender criteria
- Added **12 office companion research notes** documenting sources, assumptions, benchmark rationale, and issue-spotting logic
- Added **`/cre-office`** as the 10th Claude Code plugin
- Added strict validation tooling so the repo can catch missing mirrors, stale badges, missing research indexes, and required-heading drift
- Preserved the repo's additive release framing on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, and Asset Management v1

## Added

- 8 office skills under `skills/office/`
- 4 office knowledge bases under `knowledge/`
- 12 research notes under `research/office/`
- 1 Claude Code plugin: `claude-code-plugins/cre-office/`
- `scripts/validate-repo.ps1`
- `.github/workflows/validate.yml`

## Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, ROADMAP, and CHANGELOG for `v1.4.0`
- Updated GitHub issue templates with newer sector and pack options
- Updated the PR template with a strict-validation checkbox
- Normalized legacy heading drift in mirrored document-ingestion and underwriting skills so strict validation passes

## Notes

- Office v1 is **U.S.-only**
- Office v1 is **lease-driven** and emphasizes WALT, rollover, tenant credit, TI/LC drag, net effective rent, lender selectivity, and flight-to-quality
- Existing multifamily, industrial, brokerage, asset management, legal, closing, and document-ingestion paths remain unchanged
- The validation script is PowerShell-first and can be run locally with `.\scripts\validate-repo.ps1 -Strict`

## Suggested Tag / Version

- `v1.4.0`
