# Asset Management v1.3.0 Research Map

This directory contains the supporting Phase 0b research notes for the first Asset Management expansion of `cre-agent-skills`.

## Purpose

- Provide source-backed support for the nine planned Asset Management skills and their shared knowledge bases
- Keep benchmarks, assumptions, formulas, and decision rules traceable to named, dated institutional sources
- Separate research detail from the prompt layer so skills stay concise while staying defensible

## Asset Management v1.3.0 Scope

- Geography: United States only
- Workflow scope: post-acquisition asset management lifecycle (budget through disposition)
- Property focus: conventional stabilized multifamily (5+ units, market-rate); excludes LIHTC/HUD-affordable, student, senior, manufactured, SFR, and BTR horizontal product
- Authority: where a term is defined in `knowledge/underwriting-calc.md` or `knowledge/multifamily-benchmarks.md`, the repo file is primary; external sources corroborate

## Shared Vocabulary

- [Asset Management Taxonomy Seed (Phase 0a)](_taxonomy-seed.md) — Canonical shared vocabulary, OpEx line-item taxonomy, rent/concession definitions, variance classification, A/R aging bands, and KPI formulas inherited by all downstream AM skills and research notes. **Feeds: all nine skills and KBs.**

## Research Notes for Skills

1. [Annual Operating Budget Builder Research](annual-operating-budget-builder-research.md) — Justifies the OpEx benchmarks, line-item chart of accounts, and build methodology for a next-year stabilized-property operating budget. **Feeds: Budget Builder skill.**
2. [Monthly Variance Analyst Research](monthly-variance-analyst-research.md) — Defines materiality thresholds, the Timing / Permanent / One-Time classification framework, reforecast triggers, and institutional variance-commentary norms for monthly and YTD budget-vs-actual packages. **Feeds: Variance Analyst skill.**
3. [Rent Collection & Delinquency Manager Research](rent-collection-delinquency-manager-research.md) — Establishes A/R aging triage, bad-debt reserve methodology, state-by-state eviction sequencing, and hardship-program frameworks for stabilized properties. **Feeds: Collections Manager skill.**
4. [Renewal Decision Analyst Research](renewal-decision-analyst-research.md) — Provides the retention-vs-turn economic framework, rent-bump elasticity benchmarks, and all-in turnover cost inputs that drive renewal-offer decisions. **Feeds: Renewal Analyst skill.**
5. [Lease-Up & Concessions Analyst Research](lease-up-concessions-analyst-research.md) — Supplies absorption benchmarks by market tier, concession norms and burn-off mechanics, face-vs-effective rent reconciliation, and reforecast triggers for stabilization-date slippage. **Feeds: Lease-Up Analyst skill.**
6. [CapEx / Value-Add Execution Tracker Research](capex-value-add-execution-tracker-research.md) — Backs the execution-vs-underwriting tracking framework for unit-turn scope and cost, rent-premium realization, major-systems capex, and schedule/cost-overrun diagnostics. **Feeds: CapEx Tracker skill.**
7. [NOI Improvement Analyst Research](noi-improvement-analyst-research.md) — Catalogs NOI-improvement levers (ancillary income, OpEx reduction, property-tax appeals, utility recovery, insurance, technology) prioritized by impact × difficulty × time-to-realize at a stabilized non-renovation, non-refi property. **Feeds: NOI Improvement skill.**
8. [Hold / Sell / Refi Analyst Research](hold-sell-refi-analyst-research.md) — Frames the IRR-to-date vs. IRR-continue vs. IRR-sell decision math, refinance economics, disposition timing, and tax/capital-markets context for mid-hold owner decisions. **Feeds: Hold/Sell/Refi skill.**
9. [Quarterly Asset Review Writer Research](quarterly-asset-review-writer-research.md) — Documents the institutional reporting standards, KPI checklist, cadence rules, and format norms used to package quarterly operating results for institutional LPs. **Feeds: QAR Writer skill.**

## Cross-Note Standards

Each research note includes:

- Purpose and supported skill/KB
- U.S.-only assumptions
- Dated source table (publisher, URL, publish date, access date, source type/tier)
- Key findings with benchmarks and formula decisions
- Conflicting-source resolution
- Edge cases and red flags
- Open questions

Definitions, formulas, and classification rules route back to `_taxonomy-seed.md` rather than being redefined per note. Where the repo already defines a term in `knowledge/underwriting-calc.md` or `knowledge/multifamily-benchmarks.md`, notes defer to that file as primary authority.

## Current Source Themes

The Asset Management v1.3.0 research set draws primarily from:

- IREM / NAA / BOMA Income/Expense IQ chart of accounts and operating benchmarks
- Fannie Mae Multifamily Guide and Freddie Mac Seller/Servicer Guide (Form 4660, stabilized occupancy, replacement reserves)
- Public multifamily REIT 10-Ks and supplementals (AvalonBay, Equity Residential, Camden, MAA, Essex, UDR)
- NMHC, NAREIT, NCREIF, PREA, and ILPA institutional reporting and benchmarking standards
- Broker/market-data research from CBRE, Cushman & Wakefield, Yardi Matrix, RealPage, ALN, John Burns, and Marcus & Millichap
- State landlord-tenant statutes (TX, FL, CA, NY, GA, AZ, NV, NC) and federal CFPB / FDCPA / FASB ASC 326 frameworks
- Federal Reserve, BLS, and NOAA NCEI primary data for insurance, construction inputs, and catastrophe cost context
