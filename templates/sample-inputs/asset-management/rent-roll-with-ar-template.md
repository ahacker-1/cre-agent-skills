# Rent Roll with A/R Aging Template

Use this template to supply a unit-level rent roll extended with accounts-receivable aging columns to the AM-pack Collections / A/R Aging skill and the Rent-Roll Normalizer. One row per unit (include vacant units with blank tenant and rent fields). Aging bands follow the canonical 5-bucket schema in `research/asset-management/_taxonomy-seed.md` §5.

**Conventions.**
- `Face Rent`: headline / contract rent from the signed lease, before concession adjustment ($/unit/mo).
- `In-Place Rent`: rent the tenant is currently paying per the signed lease, as of the report date.
- `Effective Rent`: `(Face Rent × Lease Months − Concession Value) / Lease Months`. Concessions SUBTRACT — effective must be ≤ face when concessions are present.
- `Concessions`: total remaining concession value amortizing across the lease term (not monthly), in dollars.
- A/R columns are **days past due** buckets as of the report date:
  - `A/R Current`: billed but not yet past due (0 days).
  - `A/R 1-30`: 1–30 days past due.
  - `A/R 31-60`: 31–60 days past due.
  - `A/R 61-90`: 61–90 days past due.
  - `A/R 90+`: over 90 days past due.
- `Total A/R`: sum of the 5 A/R columns for that tenant (should reconcile to the balance sheet A/R per-tenant).
- `Payment Plan (Y/N)`: `Y` if an active written payment plan is in force; otherwise `N`.
- Dates in YYYY-MM-DD. Dollar amounts to the dollar; rents to the dollar.
- Vacant units: leave Tenant, Lease Start, Lease End, In-Place Rent, Effective Rent, Concessions, and all A/R columns blank. Show Face Rent as the asking rent.

---

## Property Identifier

- **Property Name:**
- **Report Date:**
- **Total Units:**
- **Occupied Units:**
- **Physical Occupancy %:**

## Rent Roll

| Unit | Tenant | Lease Start | Lease End | Face Rent | In-Place Rent | Effective Rent | Concessions | A/R Current | A/R 1-30 | A/R 31-60 | A/R 61-90 | A/R 90+ | Total A/R | Payment Plan (Y/N) | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 101 | J. Rivera | 2024-08-01 | 2025-07-31 | 1,800 | 1,800 | 1,650 | 1,800 | 0 | 0 | 0 | 0 | 0 | 0 | N | 1 month free at signing; fully amortized. |
| 102 | M. Chen | 2024-05-15 | 2025-05-14 | 1,775 | 1,775 | 1,775 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | N | |
| 103 | — | — | — | 1,850 | — | — | — | — | — | — | — | — | — | — | Vacant — asking $1,850. |
| 104 | T. Okafor | 2023-12-01 | 2024-11-30 | 1,725 | 1,725 | 1,725 | 0 | 0 | 1,725 | 0 | 0 | 0 | 1,725 | N | MTM post-expiry; notice to vacate received. |
| 105 | R. Patel | 2024-02-01 | 2025-01-31 | 1,900 | 1,900 | 1,900 | 0 | 0 | 0 | 1,900 | 1,900 | 0 | 3,800 | Y | Payment plan: $500/wk, tracking. |
| 106 | L. Baptiste | 2023-07-01 | 2024-06-30 | 1,750 | 1,750 | 1,750 | 0 | 0 | 0 | 0 | 0 | 5,250 | 5,250 | N | Eviction filed 2025-02-10; vacate pending. |
| 107 | D. Schwartz | 2024-09-01 | 2025-08-31 | 2,050 | 2,050 | 2,050 | 0 | 2,050 | 0 | 0 | 0 | 0 | 2,050 | N | Current billing; within grace period. |
| 108 | S. Nguyen | 2024-11-15 | 2025-11-14 | 1,825 | 1,825 | 1,750 | 900 | 0 | 0 | 0 | 0 | 0 | 0 | N | $100 off × 9 mo promo; amortized. |

---

## Aggregate A/R Summary (auto-computed; fill if you want to cross-check the skill's output)

| Band | Total $ | % of Total A/R |
|---|---|---|
| Current | | |
| 1-30 | | |
| 31-60 | | |
| 61-90 | | |
| 90+ | | |
| **Total** | | 100% |

## Notes / Commentary

Free-text area for property-level A/R or rent-roll commentary: eviction pipeline, seasonal delinquency patterns, skip/abandonment history, or material lease-specific issues not captured in the per-row Notes column.
