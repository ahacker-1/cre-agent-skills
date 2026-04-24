# Capex Program Tracker Template

Use this template to supply capital-project execution data to the AM-pack Capex Program Tracker skill. One row per scoped line item (not per invoice — aggregate invoices up to the scope level, e.g., "Unit turns Bldg A Q2"). Output feeds the Hold/Sell/Refi analyst's yield-on-cost and value-add progress views.

**Conventions.**
- `Category`: one of `Unit-Turn`, `Common-Area`, `Systems`, `Amenity` (aligns with AM pack capex taxonomy).
- `Status`: one of `On Track`, `At Risk`, `Delayed`, `Complete`. Use `At Risk` when spend pace or schedule slip is >10% but the item is not yet materially delayed; use `Delayed` when target completion has been revised out by more than 30 days.
- `Rent Premium Realized $/unit/mo`: measured premium vs pre-renovation comp, in-place as of the reporting date (not pro forma). Leave blank if premium has not yet been realized (e.g., unit not yet leased post-renovation).
- `Yield on Cost %`: annualized rent premium × 12 × units delivered ÷ total spent-to-date on that line (illustrative formula — the skill will recompute and cross-check).
- Figures in dollars. Dates in YYYY-MM-DD.

---

## Property Identifier

- **Property Name:**
- **Capex Program Vintage:** (e.g., 2024 value-add program, FY25 capital plan)
- **Reporting Date:**
- **Total Program Budget:** $
- **Total Spent to Date:** $

## Tracker Table

| Item / Scope | Category | Budgeted $ | Spent to Date $ | Remaining $ | Budget vs Spent % | Start Date | Target Completion | Actual Completion | Status | Units Renovated | Rent Premium Realized $/unit/mo | Yield on Cost % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Interior unit turns — Bldg A (40 units, LVP + SS appliances + quartz) | Unit-Turn | 400,000 | 285,000 | 115,000 | 71% | 2024-10-01 | 2025-06-30 | — | On Track | 28 | 185 | 21.8% |
| Roof replacement — Bldg B | Systems | 180,000 | 180,000 | 0 | 100% | 2024-11-15 | 2025-02-28 | 2025-02-20 | Complete | — | — | — |
| Clubhouse refresh (paint, furniture, WiFi) | Common-Area | 65,000 | 52,000 | 13,000 | 80% | 2025-01-10 | 2025-03-31 | — | At Risk | — | — | — |
| Pool resurface + deck furniture | Amenity | 45,000 | 8,000 | 37,000 | 18% | 2025-03-01 | 2025-05-15 | — | On Track | — | — | — |
| HVAC replacement — 12 units (end-of-life) | Systems | 72,000 | 30,000 | 42,000 | 42% | 2025-02-01 | 2025-07-31 | — | Delayed | — | — | — |
| Parking lot mill & overlay | Common-Area | 95,000 | 0 | 95,000 | 0% | 2025-05-01 | 2025-06-30 | — | On Track | — | — | — |
| | | | | | | | | | | | | |
| **Program Total** | | | | | | | | | | | | |

---

## Commentary

Free-text area for program-level narrative: vendor issues, scope changes, market-rent adjustments impacting realized premium assumptions, insurance or permit holds, etc. The capex tracker skill will read this block as supplementary context.
