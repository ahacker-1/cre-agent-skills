# CRE Asset Management Plugin

Claude Code plugin bundling 9 specialist skills for post-acquisition multifamily asset management — the operational counterpart to the due-diligence and underwriting packs. Covers the full AM lifecycle from annual budget build through monthly variance, rent collection, renewal decisions, lease-up tracking, capex execution, NOI improvement, hold/sell/refi scenarios, and the composite Quarterly Asset Review memo.

## What's Included

9 skills (`skills/*.md`):

1. **annual-operating-budget-builder** — Build next-year operating budget from T-12 + rent roll, with contract-driven escalators and benchmark-calibrated run-rate assumptions.
2. **monthly-variance-analyst** — Classify every GL line variance as Timing / Permanent / One-Time with reforecast triggers.
3. **rent-collection-delinquency-manager** — A/R aging, delinquency classification, bad-debt reserve sizing, tenant action list.
4. **renewal-decision-analyst** — Per-lease retain-vs-replace economics using elasticity, tenant tier, turnover-cost math.
5. **lease-up-concessions-analyst** — Absorption velocity, concession burn-off, stabilization reforecast.
6. **capex-value-add-execution-tracker** — Capex execution, rent-premium realization, yield-on-cost, schedule variance.
7. **noi-improvement-analyst** — NOI lever prioritization on Impact × Difficulty.
8. **hold-sell-refi-analyst** — Hold / refi / disposition scenario comparison with IRR and equity multiple.
9. **quarterly-asset-review-writer** — Composite QAR memo integrating upstream skill outputs into the 10-section LP-facing narrative.

5 knowledge bases (`knowledge/*.md`):

- `asset-management-benchmarks.md` — variance thresholds, A/R aging reserves, turnover decomposition, ancillary lifts, OpEx-KPI thresholds
- `renewal-economics.md` — Retain-vs-Replace framework, rent-bump elasticity, hold/sell/refi decision frameworks
- `asset-management-reporting-standards.md` — QAR structure, KPI checklist, reporting-layer variance conventions
- `underwriting-calc.md` — canonical CRE formulas (NOI, EGI, GPI, cap rate, DSCR, IRR, equity multiple)
- `multifamily-benchmarks.md` — benchmarks by class, region, vintage, COL tier; property tax by state; insurance cat-zone adjustments

## Install

Copy the `cre-asset-management/` directory into your Claude Code plugins directory, or install via the plugin manager pointed at this path.

## Quick Usage

```
/cre-asset-management build next-year budget for {property} using attached T-12 and rent roll
/cre-asset-management variance analysis for March 2026 actuals vs budget
/cre-asset-management write Q1 2026 QAR for {property}
```

The dispatcher (`SKILL.md`) routes the request to the appropriate specialist skill based on what you describe. Specialist skills load the relevant knowledge bases on demand.

## Scope

Conventional stabilized multifamily (5+ units, market-rate, U.S.). Lease-up / pre-stabilization is supported by the lease-up skill only. Affordable / LIHTC is out of scope for this pack.
