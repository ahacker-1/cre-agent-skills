# Asset Management Sample-Input Templates

This directory contains standardized input templates for the Asset Management (AM) skill pack (v1.3.0). Each template captures the shape of data that a specific AM skill expects; fill in the fields / rows relevant to your engagement, then paste (or attach) the completed template when invoking the skill.

All templates are additive — they do not replace the shared `deal-summary-template.md` in the parent directory, which remains the canonical property-level metadata carrier. Pair a completed AM template with a completed deal-summary for richest results.

## Index

| # | Template | One-Line Description | Primary AM Skill Consumer |
|---|---|---|---|
| 1 | `t12-actuals-template.md` | Monthly T-12 line-item actuals (income + OpEx), column per month plus T-12 total, rows per the AM OpEx taxonomy. | T-12 / Run-Rate Normalization skill; upstream input to Variance and Hold/Sell/Refi skills. |
| 2 | `budget-vs-actual-template.md` | Variance reporting input: MTD and YTD actual vs budget per line item with forecast, variance classification, and commentary. | Budget-vs-Actual Variance Reviewer skill. |
| 3 | `capex-program-tracker-template.md` | Capex program execution tracker with scope, budget, spend-to-date, schedule, status, and yield-on-cost per item. | Capex Program Tracker skill; feeds Hold/Sell/Refi analyst. |
| 4 | `rent-roll-with-ar-template.md` | Unit-level rent roll extended with 5-band A/R aging columns, effective rent, and payment-plan flag. | Collections / A/R Aging skill and Rent-Roll Normalizer skill. |
| 5 | `README.md` | This index. | — |

## How to use

1. Copy the template file into your working folder.
2. Fill in rows/columns with property data. Leave cells blank if not applicable — do not enter zero where the true value is unknown.
3. Follow the column / row taxonomy as written; downstream skills map line items by exact label match against the taxonomy in `research/asset-management/_taxonomy-seed.md`.
4. Pair with a completed `deal-summary-template.md` when invoking any AM skill that needs property metadata (unit count, class, vintage, submarket).

## Taxonomy alignment

All OpEx line items, KPI formulas, variance buckets, rent definitions, and A/R aging bands used in these templates follow the AM pack taxonomy seed at `research/asset-management/_taxonomy-seed.md`. If a template appears to conflict with the taxonomy seed, the taxonomy seed wins — flag the template for correction.
