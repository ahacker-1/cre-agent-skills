---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Rent Roll Parser

Parse a rent roll document (Excel, CSV, or PDF) and extract structured unit mix, occupancy, rent, and lease expiration data for underwriting analysis.

---

## When to Use This Skill

Use this skill when you have a rent roll file and need to extract clean, structured data from it. It handles inconsistent column headers, varied unit type naming conventions, multiple rent columns, and mixed occupancy status values. Use it at the start of underwriting to get reliable unit-level and aggregate rent data before building a financial model.

---

## What You'll Need to Provide

- The rent roll file — as an Excel spreadsheet, CSV file, or PDF
- If the file has an unusual structure (e.g., multiple property tabs, summary-only without unit detail, or combined with other reports), describe it
- Optionally, provide the total unit count so the parser can verify its extraction matches

---

## Mission

Parse rent roll documents (Excel, CSV, PDF) and extract structured unit mix, occupancy, and rent data for underwriting analysis.

---

## Strategy

The following sections describe the input formats recognized and the step-by-step extraction logic applied to parse rent roll data.

---

## Input Formats

### Excel/CSV Rent Rolls
Common column headers to look for:

| Category | Possible Headers |
|----------|------------------|
| Unit ID | Unit, Unit #, Unit No, Apt, Apartment |
| Unit Type | Type, Floorplan, Floor Plan, Bed/Bath, BR/BA |
| Bedrooms | BR, Beds, Bedrooms |
| Bathrooms | BA, Baths, Bathrooms |
| Sq Ft | SF, SqFt, Sq Ft, Square Feet, Size |
| Market Rent | Market, Market Rent, Asking Rent, Quoted Rent |
| Actual Rent | Rent, Current Rent, Contract Rent, In-Place Rent, Actual |
| Status | Status, Occupancy, Occupied |
| Tenant | Tenant, Resident, Name |
| Lease Start | Start, Move In, Move-In, Lease Start |
| Lease End | End, Lease End, Expiration, Expires |
| Move Out | Move Out, Notice, NTV |

### PDF Rent Rolls
- Look for tabular data
- Extract using structure recognition
- Handle multi-page documents

---

## Extraction Logic

### Step 1: Identify Header Row
```
Scan first 10 rows for a row containing multiple rent roll indicators:
- Contains "Unit" or "Apt"
- Contains "Rent" or "$"
- Contains "SF" or "SqFt"
```

### Step 2: Map Columns
```python
column_mapping = {
    "unit_id": find_column(["Unit", "Apt", "Unit #"]),
    "unit_type": find_column(["Type", "Floorplan", "BR/BA"]),
    "sqft": find_column(["SF", "SqFt", "Square Feet"]),
    "market_rent": find_column(["Market", "Market Rent", "Asking"]),
    "actual_rent": find_column(["Rent", "Current Rent", "Actual"]),
    "status": find_column(["Status", "Occupied"]),
    "lease_end": find_column(["Lease End", "Expiration"])
}
```

### Step 3: Parse Each Unit Row
For each data row:
1. Extract unit identifier
2. Parse unit type (convert "2x2" → "2BR/2BA"; normalize all variants to standard format)
3. Extract square footage (remove commas, convert to integer)
4. Extract rents (remove $, commas, convert to float)
5. Determine occupancy status
6. Parse lease dates

**Unit type normalization rules:**
- "2BR", "2x2", "2Bed/2Bath", "B2" → "2BR/2BA"
- "Studio", "Eff", "Efficiency" → "Studio" or "0BR/1BA"
- "1/1", "1BR1BA" → "1BR/1BA"

**Occupancy status mapping:**
- "Occupied", "Leased", "Yes" → `occupied`
- "Vacant", "Empty", "No" → `vacant`
- "Notice", "NTV", "MTM" (month-to-month as implied notice) → `notice`
- "Model", "Down", "Offline", "Maintenance" → `non-revenue`

### Step 4: Aggregate Unit Mix
Group units by type and calculate:
```json
{
  "unitMix": [
    {
      "type": "1BR/1BA",
      "count": 80,
      "avgSqFt": 725,
      "minSqFt": 700,
      "maxSqFt": 750,
      "marketRent": 1350,
      "avgInPlaceRent": 1225,
      "minRent": 1150,
      "maxRent": 1300,
      "occupiedCount": 75,
      "vacantCount": 5
    }
  ]
}
```

### Step 5: Calculate Portfolio Aggregates
```json
{
  "totalUnits": 200,
  "occupiedUnits": 186,
  "vacantUnits": 14,
  "occupancyRate": 0.93,
  "totalSqFt": 180000,
  "avgUnitSqFt": 900,
  "grossPotentialRent": {
    "annual": 3864000,
    "monthly": 322000
  },
  "inPlaceRent": {
    "annual": 3516000,
    "monthly": 293000
  },
  "lossToLease": {
    "annual": 348000,
    "percent": 0.09
  },
  "avgMarketRentPerUnit": 1610,
  "avgInPlaceRentPerUnit": 1465,
  "avgRentPerSqFt": 1.63
}
```

### Step 6: Lease Expiration Analysis
```json
{
  "leaseExpirations": {
    "month1": 12,
    "month2": 8,
    "month3": 15,
    "monthToMonth": 5,
    "nextQuarter": 35,
    "nextYear": 120
  },
  "avgRemainingLeaseTerm": 6.5
}
```

---

## Output Format

Return structured JSON using this schema:

```json
{
  "source": {
    "file": "rent-roll.xlsx",
    "extractedAt": "2026-02-01T12:00:00Z",
    "confidence": 0.95
  },
  "summary": {
    "totalUnits": 200,
    "occupiedUnits": 186,
    "vacantUnits": 14,
    "occupancyRate": 0.93,
    "totalSqFt": 180000,
    "avgUnitSqFt": 900
  },
  "income": {
    "grossPotentialRentAnnual": 3864000,
    "grossPotentialRentMonthly": 322000,
    "inPlaceRentAnnual": 3516000,
    "inPlaceRentMonthly": 293000,
    "lossToLeaseAnnual": 348000,
    "lossToLeasePercent": 0.09,
    "avgMarketRent": 1610,
    "avgInPlaceRent": 1465,
    "avgRentPerSqFt": 1.63
  },
  "unitMix": [
    {
      "type": "1BR/1BA",
      "count": 80,
      "percentOfTotal": 0.40,
      "avgSqFt": 725,
      "marketRent": 1350,
      "inPlaceRent": 1225,
      "occupiedCount": 75,
      "vacancyRate": 0.0625
    }
  ],
  "leaseExpirations": {
    "next30Days": 12,
    "next60Days": 20,
    "next90Days": 35,
    "monthToMonth": 5
  },
  "units": [
    {
      "unitId": "101",
      "type": "1BR/1BA",
      "sqft": 725,
      "marketRent": 1350,
      "actualRent": 1225,
      "status": "occupied",
      "leaseEnd": "2026-06-30"
    }
  ],
  "warnings": [],
  "dataGaps": []
}
```

---

## Quality Checks

Run these validation checks before finalizing:

1. **Unit count**: Sum of unit mix counts = `totalUnits`
2. **Occupancy math**: `occupiedUnits` + `vacantUnits` + `noticeUnits` + `nonRevenueUnits` = `totalUnits`
3. **Rent outliers**: Flag any unit with rent > 5× the average (likely a data entry error)
4. **Size outliers**: Flag any unit with square footage > 3× the average (likely a data entry error)
5. **Date logic**: Lease end dates should be in the future for currently occupied units; flag past lease end dates as needing confirmation
6. **Loss to lease direction**: Loss to lease should be positive (in-place < market) for most value-add deals; flag if negative (in-place > market) as unusual

---

## When Data is Missing

### Multiple Rent Columns
Some rent rolls have: Base Rent, Additional Rent, Total Rent
- Use "Total Rent" if present, or sum Base + Additional
- Log which column was used in `warnings`

### Mixed Status Values
"Occupied", "Vacant", "Notice", "Model", "Down"
- Map to: `occupied`, `vacant`, `notice`, `non-revenue`
- Calculate separate vacancy rates for economic vacancy (lost rent) vs. physical vacancy (empty units)

### Missing Market Rents
- Flag as a data gap in `dataGaps`
- If the rent roll has vacant units with no asking rent listed, attempt to estimate market rent from comparable occupied units of the same type
- Note any estimated market rents in `warnings` with the basis for the estimate

### Inconsistent Unit Types
"2BR", "2x2", "2Bed/2Bath", "B2" all mean the same thing
- Normalize to standard format: "2BR/2BA"
- Handle studios: "Studio" or "0BR/1BA"
- Log all normalizations applied in `warnings`

---

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **HIGH (0.90+)** | All columns mapped, all units parsed, no outliers, dates clean |
| **MEDIUM (0.70–0.89)** | Most units parsed; some columns missing (e.g., market rent absent) or minor data quality issues |
| **LOW (<0.70)** | Significant missing data (no market rents, no lease dates), heavy manual normalization required, or PDF extraction with unclear table structure |

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- **Multifamily Benchmarks** knowledge base — to validate occupancy rates, loss-to-lease percentages, and rent per square foot against market norms
- **Underwriting Calculations** knowledge base — for building a financial model from the rent roll data (GPR, vacancy assumptions, effective gross income)
- **Offering Memo Parser** skill — to cross-validate unit count and occupancy against the OM
- **T12 Financials Parser** skill — to cross-validate gross potential rent and occupancy against the operating statement

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
