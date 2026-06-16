# Office Rent Roll and Stacking Plan Analyst

Analyze an office rent roll and stacking plan to identify occupancy, WALT, rollover, floor-by-floor exposure, vacancy quality, and leasing risk.

---

## When to Use This Skill

Use this skill when you have an office rent roll, lease roster, stacking plan, or leasing summary and need to understand the building's true occupancy risk. It is especially useful when reported occupancy hides signed-not-commenced leases, shadow vacancy, sublease space, or concentrated rollover.

---

## What You'll Need to Provide

- Rent roll or lease roster with tenant, suite, floor, RSF, rent, term, and expiration
- Stacking plan if available
- Occupancy summary: leased, occupied, vacant, signed-not-commenced, sublease, spec suite
- Asking rents and market rents by floor or suite type if available
- Tenant industry and credit notes if available
- Any renewal, contraction, expansion, termination, or must-take rights

---

## Mission

Convert the rent roll and stacking plan into a decision-ready view of tenant exposure, vacancy quality, rollover timing, floor-level fragmentation, and lease-up difficulty.

---

## Strategy

### Step 1: Normalize the Rent Roll

Create a clean table with:

- tenant
- suite / floor
- rentable square feet
- current rent
- rent steps
- lease start
- lease expiration
- renewal options
- termination or contraction rights
- status: occupied, vacant, signed-not-commenced, sublease, spec suite, owner-occupied, storage, amenity

### Step 2: Reconcile Area

Compare:

- rent roll RSF
- stacking plan RSF
- building rentable area
- occupied RSF
- leased RSF
- physically occupied RSF

Flag gaps caused by measurement, signed-not-commenced leases, vacancy, sublease space, or non-office areas.

### Step 3: Calculate WALT and Rollover

Calculate:

```text
WALT = Sum(Tenant RSF x Years to Expiration) / Total Occupied or Leased RSF
Tenant Concentration = Tenant RSF / Total Leased RSF
Annual Rollover % = Expiring RSF in Year / Total Leased RSF
```

Show rollover by year and by floor.

### Step 4: Analyze Stacking Plan

Evaluate:

- contiguous vacancy
- fragmented vacancy
- large-block availability
- floor-by-floor tenant mix
- elevator bank or lobby segmentation
- spec suite strategy
- expansion path for key tenants
- whether vacant suites are truly marketable

### Step 5: Identify Tenant and Industry Concentration

Group rent and RSF by:

- tenant
- parent company
- industry
- floor / vertical stack
- expiration year

Flag industry exposure such as technology, coworking, government, legal, finance, health care, education, or distressed sectors.

### Step 6: Create Rollover Risk Tiers

Classify each tenant or suite:

- LOW: durable tenant, market rent, no near-term option risk
- MEDIUM: renewal uncertain, rent gap, or modest space reduction risk
- HIGH: near-term expiration, above-market rent, weak credit, contraction risk, or direct sublease alternative

---

## Output Format

```markdown
# Office Rent Roll and Stacking Plan Analysis
## Property:
## Rentable Area:
## As-of Date:

### Occupancy Reconciliation
| Metric | RSF | % of Building | Notes |
|---|---:|---:|---|
| Leased | | | |
| Physically occupied | | | |
| Signed not commenced | | | |
| Direct vacant | | | |
| Sublease available | | | |

### Tenant Concentration
| Tenant | RSF | % Leased RSF | Expiration | Rent vs Market | Risk |
|---|---:|---:|---|---|---|

### Rollover Schedule
| Year | Expiring RSF | % Leased RSF | Major tenants | Risk notes |
|---|---:|---:|---|---|

### Stacking Plan Findings
- Large blocks:
- Fragmented vacancy:
- Expansion paths:
- Floors with leasing friction:

### Watchlist
| Tenant / suite | Issue | Potential impact | Next diligence item |
|---|---|---|---|

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- Leased RSF plus vacant RSF reconciles to building rentable area or explains the difference
- WALT calculation uses RSF weighting
- Signed-not-commenced space is separated from occupied space
- Sublease space is not treated as direct landlord vacancy unless economics require it
- All tenants over 10% of leased RSF are individually discussed
- Rollover is shown by year, not only as an average

---

## Red Flags & Dealbreakers

- One tenant controls more than 25% of rent or RSF with near-term expiration
- More than 35% of leased RSF rolls within 24 months
- Large contiguous vacancy exists in a market with weak large-block demand
- Reported occupancy includes material signed-not-commenced or shadow-vacant space
- Stacking plan shows stranded partial-floor vacancy that cannot be efficiently leased

---

## When Data is Missing

- If suite-level rent is missing, calculate exposure by RSF and mark rent risk as unknown
- If lease expirations are missing, classify WALT and rollover confidence as LOW
- If no stacking plan is provided, produce a rent-roll-only view and request floor/suite data
- If tenant parent or industry is missing, infer only when obvious and flag as unverified

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Suite-level rent roll, stacking plan, expirations, options, and occupancy status are all available |
| MEDIUM | Rent roll and expirations available, but stacking plan or option detail incomplete |
| LOW | Summary-only occupancy or missing lease expiration data |

---

## Related Knowledge Bases

- [Office Benchmarks](knowledge/office-benchmarks.md)
- [Office Lease Structures](knowledge/office-lease-structures.md)
- [Office TI / LC Economics](knowledge/office-ti-lc-economics.md)

## Research Basis

- [Office Rent Roll and Stacking Plan Analyst Research](research/office/office-rent-roll-and-stacking-plan-analyst-research.md)
