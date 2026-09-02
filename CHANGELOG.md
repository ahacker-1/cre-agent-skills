# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.6.0] - 2026-09-01

### Added

- Retail Pack v1 release with 8 new U.S.-focused retail skills under `skills/retail/`
  - Retail Market and Trade Area Study
  - Retail Rent Roll and Tenant Mix Analyst
  - Retail Lease Abstract Reviewer
  - Retail Co-Tenancy and Anchor Risk Analyst
  - Retail CAM Reconciliation and Recovery Analyst
  - Retail Underwriting Model Builder
  - Retail Financing Fit
  - Retail IC Memo Writer
- 4 new retail knowledge bases under `knowledge/`
  - `retail-benchmarks.md` - retail format definitions, occupancy and leasing reference points, leasing capital, occupancy cost, recovery load, and e-commerce exposure
  - `retail-lease-structures.md` - retail lease forms, base and percentage rent, CAM / tax / insurance recovery, tenant control rights, REA / OEA and pads, assignment, estoppel, and SNDA
  - `retail-tenant-sales-and-occupancy-cost.md` - sales and occupancy-cost definitions, category frames, tenant credit tiers, distress signals, renewal and backfill economics, and STNL frameworks
  - `retail-lender-criteria.md` - retail lender lanes, core sizing tests, deterioration signals, reserves, holdbacks, and recourse posture
- 12 new companion research notes under `research/retail/` plus `research/retail/INDEX.md`
- New Claude Code plugin: `cre-retail` at `claude-code-plugins/cre-retail/`
- Lender / Credit Pack v1 release with 8 new U.S.-focused credit-side skills under `skills/lender-credit/`
  - Loan Request Screening and Sizing
  - Sponsor and Guarantor Analyst
  - Appraisal and Valuation Reviewer
  - Credit Memo Writer
  - Covenant Compliance and Watchlist Monitor
  - Annual Loan Review and Risk Rating
  - Problem Loan and Modification Analyst
  - CRE Portfolio Concentration and Stress Tester
- 4 new lender / credit knowledge bases under `knowledge/`
  - `lender-credit-policy-benchmarks.md` - CRE credit policy content, supervisory leverage ceilings and the exception basket, sizing frames by lender and property type, and pricing and reserve frames
  - `regulatory-risk-rating-and-classification.md` - supervisory classification definitions, criticized / classified / watchlist mapping, dual risk rating scales, nonaccrual, modification treatment, and rating migration reporting
  - `credit-memo-and-appraisal-review-standards.md` - credit approval memo structure, documentation and covenant checklists, policy exceptions and supervisory LTV limits, and appraisal review standards
  - `cre-concentration-and-stress-testing.md` - supervisory concentration screening criteria, book segmentation, stress-test design, and how results feed capital, ACL, and policy limits
- 12 new companion research notes under `research/lender-credit/` plus `research/lender-credit/INDEX.md`
- New Claude Code plugin: `cre-lender-credit` at `claude-code-plugins/cre-lender-credit/`
- Development and Construction Pack v1 release with 8 new U.S.-focused development skills under `skills/development/`
  - Site and Entitlement Screen
  - Development Budget and Yield on Cost Analyst
  - Construction Loan Sizing and Structure
  - Construction Draw and Cost-to-Complete Reviewer
  - GC Contract and Change Order Reviewer
  - Schedule and Delivery Risk Tracker
  - Lease-Up and Stabilization Pro Forma
  - Development IC Memo Writer
- 4 new development knowledge bases under `knowledge/`
  - `development-benchmarks.md` - development budget taxonomy, contingency and escalation, dated cost frames, yield on cost and development spread, residual land value, and schedule and lease-up durations
  - `construction-lending-criteria.md` - construction sizing tests, equity and HVCRE treatment, interest reserve and carry, guaranty posture, in-balance and draw controls, and extension / mini-perm / takeout paths
  - `construction-contracts-and-draw-controls.md` - contract families and risk allocation, money mechanics, change orders versus construction change directives, completion and retainage, draw packages, lien waivers, bonds, and insurance
  - `entitlement-and-site-risk.md` - approval pathways and their cost, exactions and impact fees, environmental site review, utilities and geotechnical obligations, and historic, design, and state environmental review
- 12 new companion research notes under `research/development/` plus `research/development/INDEX.md`
- New Claude Code plugin: `cre-development` at `claude-code-plugins/cre-development/`
- Cross-platform validation tooling: `scripts/validate_repo.py`, a Python port of `scripts/validate-repo.ps1` that checks the same invariants and runs with `python3 scripts/validate_repo.py --strict`
- Second CI job `validate-python` on `ubuntu-latest` in `.github/workflows/validate.yml`, alongside the unchanged Windows job
- New release notes:
  - `docs/releases/retail-v1.md`
  - `docs/releases/lender-credit-v1.md`
  - `docs/releases/development-v1.md`
  - `docs/releases/v1.6.0-pr-summary.md`

### Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, and ROADMAP to position Retail v1, Lender / Credit v1, and Development and Construction v1 as the sixth, seventh, and eighth additive packs after Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, and Capital Markets v1
- Updated README counts, badges, project structure, knowledge base table, example workflows, common workflows, and FAQ for 90 skills, 35 knowledge bases, 93 research notes, and 14 Claude Code plugins
- Updated `docs/ROADMAP.md` so the Retail / Self-Storage wave reads "Retail shipped in v1.6.0, self-storage deferred", and marked the capital-markets depth items "lender-side credit memo variants" and "construction-loan workouts" as shipped via the new packs
- Updated `.github/ISSUE_TEMPLATE/new-skill-request.yml` with Retail, Lender / Credit, and Development and Construction department options
- Updated `CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md` so macOS / Linux contributors can run the Python validator as the equivalent of the PowerShell one

### New conventions introduced

- First release to ship three packs at once; release notes are written per pack with a single combined PR summary
- First lender-side pack in the repo. Every prior pack is borrower, owner, or seller side; Lender / Credit v1 is the credit-side mirror and states plainly that classification, nonaccrual, allowance, and regulatory reporting conclusions belong to the institution and its regulator
- Validation is now cross-platform: `scripts/validate_repo.py --strict` mirrors `scripts/validate-repo.ps1 -Strict` check for check, so contributors on macOS and Linux can run the same strict gate locally and CI runs both
- Development content covers the interval from site control to stabilization and hands off to the stabilized-operations packs rather than restating them
- Retail content separates reported tenant sales (unaudited landlord reporting) from lease-driven contract rent, and separates issuer-published occupancy cost statistics from underwritten recovery income

### Deferred to future releases

- Self-storage sector pack
- Leasing pack for landlord and tenant representation
- Equity / JV / investor relations pack for waterfalls, promotes, capital calls, and LP reporting
- Affordable and workforce housing overlays
- Hospitality pack
- Capital markets depth for agency-specific refinance overlays and note-sale bidding workflows

## [1.5.0] - 2026-06-16

### Added

- Capital Markets / Debt Maturity & Recap Pack v1 release with 8 new U.S.-focused cross-property capital markets skills under `skills/capital-markets/`
  - Debt Maturity Diagnostic
  - Refinance Proceeds Gap Analyzer
  - Extension / Workout Strategy Builder
  - Rescue Capital Comparator
  - Capital Stack Term Sheet Comparator
  - CMBS / Special Servicing Readiness Reviewer
  - Lender Update Package Builder
  - Recap IC Memo Writer
- 4 new capital markets knowledge bases under `knowledge/`
  - `capital-markets-benchmarks.md` - debt sizing, DSCR, debt yield, LTV, refinance gap, and capital-stack screening
  - `workout-and-extension-structures.md` - extensions, modifications, forbearance, A/B notes, DPOs, deeds-in-lieu, and lender give/get
  - `rescue-capital-and-pref-equity.md` - preferred equity, mezzanine, JV equity, bridge, note purchase, DPO, and rescue-capital comparison
  - `cmbs-servicing-and-default-playbook.md` - CMBS parties, transfer triggers, special-servicer package readiness, and borrower strategy
- 12 new companion research notes under `research/capital-markets/` plus `research/capital-markets/INDEX.md`
- New Claude Code plugin: `cre-capital-markets` at `claude-code-plugins/cre-capital-markets/`
- New release notes:
  - `docs/releases/capital-markets-v1.md`
  - `docs/releases/capital-markets-v1-pr-summary.md`

### Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, and ROADMAP to position Capital Markets v1 as the fifth additive pack after Industrial v1, Brokerage Investment Sales v1, Asset Management v1, and Office v1
- Updated GitHub issue templates to include capital markets skills and knowledge bases

### New conventions introduced

- Cross-property packs can sit beside sector and role packs when the workflow applies across multiple property types
- Refinance and recap workflows should separate asset viability, supportable proceeds, reserve need, sponsor liquidity, lender consent, and exit feasibility
- Capital markets outputs must distinguish educational decision support from legal, tax, investment, or financing advice

### Deferred to future releases

- Retail and self-storage sector packs
- Affordable and workforce housing overlays
- Capital markets depth modules for agency-specific refinances, construction-loan workouts, lender-side credit memos, and note-sale bidding

## [1.4.0] - 2026-06-16

### Added

- Office Pack v1 release with 8 new U.S.-focused office acquisition, refinance, recapitalization, lease-up, tenant credit, TI/LC underwriting, financing-fit, and IC memo skills under `skills/office/`
  - Office Market and Flight-to-Quality Study
  - Office Rent Roll and Stacking Plan Analyst
  - Office Lease Abstract Reviewer
  - Office Rollover and Occupancy Cost Analyst
  - Office TI / LC Underwriting Model Builder
  - Office Tenant Credit and Exposure Analyst
  - Office Financing Fit
  - Office IC Memo Writer
- 4 new office knowledge bases under `knowledge/`
  - `office-benchmarks.md` - office market, quality-tier, vacancy, leasing, operating, and flight-to-quality guardrails
  - `office-lease-structures.md` - full-service, modified gross, base-year, expense-stop, NNN, BOMA, work-letter, option, and transfer-right guidance
  - `office-ti-lc-economics.md` - TI, LC, free rent, downtime, net effective rent, leasing-cost reserve, and renewal-vs-new-lease economics
  - `office-lender-criteria.md` - office lender lanes, sizing tests, reserves, recourse posture, and financing red flags
- 12 new companion research notes under `research/office/` plus `research/office/INDEX.md`
- New Claude Code plugin: `cre-office` at `claude-code-plugins/cre-office/`
- Strict repo validation tooling:
  - `scripts/validate-repo.ps1`
  - `.github/workflows/validate.yml`

### Changed

- Updated README, HOW-TO-USE, SKILL-INDEX, and ROADMAP to position Office v1 as the fourth additive pack after Industrial v1, Brokerage Investment Sales v1, and Asset Management v1
- Updated GitHub issue and PR templates so new sectors and validation are visible in contribution workflows
- Fixed legacy heading drift in document-ingestion and underwriting skill mirrors so root and plugin copies pass strict validation

### New conventions introduced

- README badges are now validated against actual repo counts for skills, knowledge bases, research notes, and Claude Code plugins
- Strict validation checks root/plugin mirror coverage, required skill headings, research indexes, and skill-backed research notes
- Office pack uses an explicit lease-driven framing: market quality, rollover, tenant credit, TI/LC drag, lender selectivity, and IC-level risk synthesis

### Deferred to future releases

- Retail and self-storage sector packs
- Affordable and workforce housing overlays

## [1.3.0] - 2026-04-24

### Added

- Asset Management Pack v1 release with 9 new U.S.-focused post-closing asset management skills under `skills/asset-management/`
  - Annual Operating Budget Builder
  - Monthly Variance Analyst
  - Rent Collection & Delinquency Manager
  - Renewal Decision Analyst
  - Lease-Up & Concessions Analyst
  - CapEx & Value-Add Execution Tracker
  - NOI Improvement Analyst
  - Hold/Sell/Refi Analyst
  - Quarterly Asset Review Writer (composite synthesizer)
- 3 new shared knowledge bases under `knowledge/`
  - `asset-management-benchmarks.md` — operational benchmarks (variance thresholds, A/R reserves, turnover costs, absorption, concession norms)
  - `renewal-economics.md` — retain-vs-replace framework plus hold/sell/refi economics
  - `asset-management-reporting-standards.md` — QAR structure, LP reporting cadence, mandatory KPI checklist
- 10 new research notes under `research/asset-management/` (1 taxonomy seed + 9 skill-backing notes + INDEX), 168+ cited sources, all meeting the >=10 total / >=6 Tier 1/2 thresholds
- 5 new input templates under `templates/sample-inputs/asset-management/`
- New Claude Code plugin: `cre-asset-management` at `claude-code-plugins/cre-asset-management/` (16 files: SKILL.md dispatcher + README + 9 mirrored skills + 5 mirrored KBs for standalone install)

### Changed

- `skills/closing/closing-coordinator.md` — added optional `stabilization_handoff` block to Output Format and downstream cross-reference to Budget Builder (+10 lines)
- `skills/brokerage/broker-opinion-of-value-builder.md` — accepts optional `disposition_handoff` from Hold/Sell/Refi Analyst (+2 lines)
- `skills/due-diligence/rent-roll-analyst.md` — added downstream cross-link (+1 line)
- `skills/due-diligence/opex-analyst.md` — added downstream cross-link (+1 line)
- `skills/underwriting/scenario-analyst.md` — added downstream cross-link (+1 line)
- `skills/underwriting/ic-memo-writer.md` — added downstream cross-link (+1 line)
- `docs/ROADMAP.md` — Wave 1 (Multifamily Depth) marked substantially complete (4 of 5 focus areas shipped); Wave 2 (Office) advanced to "next"

### New conventions introduced

Documented in `research/asset-management/_taxonomy-seed.md`:

- NOI/NCF split: AM pack computes NOI excluding Replacement Reserves; NCF = NOI − Replacement Reserves per Fannie Form 4660 convention (note: divergence from existing `underwriting-calc.md` treatment — transparent, documented)
- 12-section skill template (AM pack extension): adds `## Research Basis` and `## Structured Output` JSON block with `uncertainty_flags` and `red_flags` arrays
- Variance classification: Timing / Permanent / One-Time buckets with mechanically-applicable decision rules including mixed-variance and seasonal-weather rules
- A/R split-aging rule: apply action for oldest band with balance >= $100
- 8-section research note format with 5-column Source Table schema

### Deferred to v1.4.0+

- Affordable and workforce housing overlays (Wave 1, 5th focus area)

## [1.2.0] - 2026-04-22

### Added

- Brokerage Investment Sales v1 release with 8 new U.S.-focused seller-side brokerage skills
  - assignment intake manager
  - broker opinion of value builder
  - listing proposal builder
  - offering memorandum and teaser writer
  - buyer process and data room manager
  - call for offers and bid leveling analyst
  - deal term negotiation brief builder
  - PSA to close transaction coordinator
- 4 brokerage knowledge bases
  - brokerage investment sales process
  - broker opinion of value guidance
  - marketing confidentiality and buyer process
  - offer negotiation and closing playbook
- 12 brokerage companion research notes under `research/brokerage/`
- New Claude Code plugin: `cre-brokerage`
- New documentation:
  - `docs/releases/brokerage-v1.md`
  - `docs/releases/brokerage-v1-pr-summary.md`

### Changed

- Updated the public docs to position Brokerage Investment Sales v1 as an additive `v1.2.0` release on top of the original multifamily-first repo and the prior Industrial v1 release
- Extended usage and skill-index docs with role-based brokerage workflows
- Updated contributing guidance so role-based packs follow the same research-backed standard as sector packs

## [1.1.0] - 2026-04-22

### Added

- Industrial v1 sector expansion with 8 new U.S.-focused industrial acquisition skills
  - industrial market study
  - industrial lease roster analysis
  - industrial lease abstract review
  - industrial tenant credit analysis
  - industrial physical inspection
  - industrial underwriting model builder
  - industrial financing fit
  - industrial IC memo writer
- 3 industrial knowledge bases
  - industrial benchmarks
  - industrial lease structures
  - industrial lender criteria
- 11 industrial companion research notes under `research/industrial/`
- New Claude Code plugin: `cre-industrial`
- New documentation:
  - `docs/RESEARCH-STANDARDS.md`
  - `docs/ROADMAP.md`
  - `docs/releases/industrial-v1.md`
  - `docs/releases/industrial-v1-pr-summary.md`

### Changed

- Repositioned the repo as a broader U.S. CRE skill library spanning multifamily core, shared CRE workflows, and industrial v1
- Updated `README.md`, `docs/HOW-TO-USE.md`, and `docs/SKILL-INDEX.md` to reflect the new sector structure
- Updated `CONTRIBUTING.md` to require companion research notes for new sector content
- Added PowerShell plugin installation examples alongside existing Claude Code usage guidance
- Lightly broadened shared document-ingestion wording so intake workflows read cleanly for industrial and broader CRE use cases

## [1.0.0] - 2026-03-30

### Added

- 25 standalone CRE analysis skills extracted from [CRE Acquisition Orchestrator](https://github.com/ahacker-1/cre-acquisition-orchestrator)
  - 7 Due Diligence skills (rent roll, OpEx, market, physical, environmental, title, tenant credit)
  - 3 Underwriting skills (financial model, scenario analysis, IC memo)
  - 3 Financing skills (lender outreach, quote comparison, term sheet)
  - 6 Legal skills (PSA, title/survey, estoppels, loan docs, insurance, transfer docs)
  - 2 Closing skills (closing coordinator, funds flow)
  - 4 Document Ingestion skills (classifier, rent roll parser, financials parser, OM parser)
- 5 domain knowledge bases (underwriting calculations, risk scoring, multifamily benchmarks, lender criteria, legal checklist)
- 6 Claude Code plugins — one per department with SKILL.md entry points and bundled knowledge bases
- Sample input templates (rent roll CSV, T-12 CSV, deal summary template)
- Full documentation (README, HOW-TO-USE guide, SKILL-INDEX quick reference)
