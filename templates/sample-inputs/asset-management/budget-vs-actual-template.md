# Budget vs Actual Variance Template

Use this template to supply monthly variance-reporting data to the AM-pack Budget-vs-Actual Variance Reviewer skill. One row per line item (match the AM OpEx taxonomy labels exactly so downstream mapping is automatic). The skill will classify each material variance into **Timing / Permanent / One-Time** per the decision rules in `research/asset-management/_taxonomy-seed.md` §3; you may pre-classify in the Classification column or leave blank for the skill to assign.

**Conventions.**
- MTD Variance $ = MTD Actual − Original Budget (for the reporting month). Positive = favorable for revenue, unfavorable for expense. The skill normalizes sign; just be consistent per row.
- YTD Variance $ = YTD Actual − YTD Budget.
- Annual Forecast = reforecast as-of reporting month (not the original budget).
- Annual Variance from Original = Annual Forecast − Original Annual Budget.
- Materiality floor (pack default): only classify variances exceeding the lesser of 10% of budgeted line item OR $25,000 in absolute terms.
- Classification values: `Timing`, `Permanent`, `One-Time`, or `Timing + Permanent` (mixed — split in commentary).

---

## Property Identifier

- **Property Name:**
- **Reporting Month:**
- **Fiscal Year:**
- **Months Elapsed in FY:**

## Variance Table

| Line Item | Original Budget (Annual) | Current-Month Actual | MTD Variance $ | MTD Variance % | YTD Budget | YTD Actual | YTD Variance $ | YTD Variance % | Annual Forecast | Annual Variance from Original | Classification (Timing / Permanent / One-Time) | Commentary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross Potential Rent | 1,826,000 | 152,500 | +500 | +0.3% | 760,000 | 763,000 | +3,000 | +0.4% | 1,830,000 | +4,000 | Timing | Trend holds — small favorable. |
| Vacancy Loss | 100,000 | 9,000 | +(1,400) | +15% | 41,600 | 45,200 | +(3,600) | +8.7% | 104,000 | +(4,000) | Permanent | Occupancy drift in submarket; re-baseline. |
| Concessions | 19,500 | 1,500 | 0 | 0% | 8,000 | 7,800 | −200 | −2.5% | 19,200 | −300 | Timing | Within materiality. |
| Property Taxes | 165,000 | 0 | +13,750 | +100% | 57,750 | 0 | +57,750 | +100% | 165,000 | 0 | Timing | County bills annually in Nov; full-year on budget. |
| Insurance | 85,000 | 0 | +7,083 | +100% | 29,750 | 0 | +29,750 | +100% | 92,000 | +7,000 | Timing + Permanent | Annual renewal not yet posted (timing); renewed premium up 8% (permanent residual). |
| Utilities — Water/Sewer | | | | | | | | | | | | |
| Utilities — Trash | | | | | | | | | | | | |
| Utilities — Gas | | | | | | | | | | | | |
| Utilities — Electric | | | | | | | | | | | | |
| Repairs & Maintenance | 110,000 | 12,500 | +(3,333) | +36% | 45,833 | 58,200 | +(12,367) | +27% | 130,000 | +(20,000) | Permanent | HVAC failures tracking 2x plan; reforecast up $20k. |
| Turnover / Make-Ready | | | | | | | | | | | | |
| Contract Services | | | | | | | | | | | | |
| Management Fee | | | | | | | | | | | | |
| Payroll | | | | | | | | | | | | |
| Administrative | | | | | | | | | | | | |
| Marketing | 18,000 | 1,400 | +100 | +6.7% | 7,500 | 7,620 | +(120) | +1.6% | 18,100 | +(100) | Timing | Within materiality floor; no action. |
| Professional Fees | | | | | | | | | | | | |
| Communications | | | | | | | | | | | | |
| **Total OpEx** | | | | | | | | | | | | |
| **NOI** | | | | | | | | | | | | |

---

## Notes / Commentary

Free-text area for portfolio-level commentary, market-condition notes, or context the row-level Commentary column cannot fit. The variance reviewer skill will read this block as supplementary context.
