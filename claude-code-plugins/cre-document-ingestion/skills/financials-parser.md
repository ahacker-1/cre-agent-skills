# T12 Financials Parser

Parse a trailing 12-month (T12) operating statement and extract structured revenue, expense, NOI, and per-unit metrics for underwriting analysis.

---

## When to Use This Skill

Use this skill when you have a T12 income statement, operating expense report, or trailing financial summary for a multifamily or commercial property and need to extract clean, standardized financial data from it. It handles monthly-column format, annual summary format, and budget-comparison format. Use it at the start of underwriting to establish a reliable baseline of current property performance.

---

## What You'll Need to Provide

- The T12 financial statement — as an Excel spreadsheet, CSV, or PDF
- The number of units in the property (for per-unit metric calculations)
- If the statement is a partial year (YTD) or covers a non-standard period, note that and specify the period covered
- If the document mixes actual and budgeted figures, note that so the parser can separate them

---

## Mission

Parse T12 financial statements, income/expense reports, and operating statements to extract revenue, expenses, and NOI data for underwriting.

---

## Strategy

The following sections detail the input formats recognized, header patterns used for column identification, and the step-by-step extraction logic applied to each document.

---

## Input Formats

### Common T12 Structures

**Format A: Monthly Columns**
```
                Jan    Feb    Mar    ...    Dec    Total
Revenue
 Gross Rent    280K   282K   285K   ...    295K   3.4M
 Vacancy       (14K)  (12K)  (15K)  ...    (10K)  (170K)
...
```

**Format B: Annual Summary**
```
                     T12        Per Unit    % of Revenue
Revenue
 Gross Potential    3,600,000   18,000      100%
 Vacancy             (180,000)    (900)      (5%)
...
```

**Format C: Budget Comparison**
```
                     Actual     Budget     Variance
Revenue
 Gross Rent        3,420,000  3,500,000   (80,000)
...
```

---

## Column Header Recognition

| Category | Possible Headers |
|----------|------------------|
| Revenue | Revenue, Income, Gross Potential, GPR |
| Vacancy | Vacancy, Loss, Vacancy Loss |
| Concessions | Concessions, Free Rent, Specials |
| Bad Debt | Bad Debt, Write-off, Collections |
| Other Income | Other, Other Income, Misc, Fee Income |
| Total Revenue | Total Revenue, Effective Gross, EGI, Net Rental Income |
| Expenses | Expenses, Operating Expenses, OpEx |
| Taxes | Taxes, Real Estate Taxes, Property Tax |
| Insurance | Insurance, Property Insurance |
| Utilities | Utilities, Electric, Gas, Water, Sewer |
| Repairs | Repairs, R&M, Maintenance, Repairs & Maintenance |
| Management | Management, Management Fee, Property Management |
| Payroll | Payroll, Personnel, Salaries, Wages |
| Admin | Admin, Administrative, G&A, Office |
| Marketing | Marketing, Advertising, Leasing |
| Contract | Contract Services, Vendors |
| Total Expenses | Total Expenses, Total OpEx, Operating Expenses |
| NOI | NOI, Net Operating Income, Operating Income |

---

## Extraction Logic

### Step 1: Identify Statement Structure
Determine which format by scanning:
- Monthly columns (12+ numeric columns) → Format A
- Annual summary with 1–3 numeric columns → Format B
- Columns labeled "Actual", "Budget", "Variance" → Format C

Look for "T12", "Trailing", "Annual", "YTD" indicators to confirm the period covered.

### Step 2: Find Key Sections
Locate section headers:
1. Revenue / Income section
2. Expense / Operating Expense section
3. NOI / Net Operating Income line

### Step 3: Extract Revenue Items
```json
{
  "revenue": {
    "grossPotentialRent": 3600000,
    "vacancy": -180000,
    "vacancyPercent": 0.05,
    "lossToLease": -84000,
    "concessions": -30000,
    "badDebt": -12000,
    "otherIncome": {
      "petFees": 24000,
      "parkingIncome": 36000,
      "laundryIncome": 18000,
      "lateFees": 12000,
      "applicationFees": 8000,
      "otherMisc": 22000,
      "total": 120000
    },
    "effectiveGrossIncome": 3414000
  }
}
```

### Step 4: Extract Expense Items
```json
{
  "expenses": {
    "realEstateTaxes": 320000,
    "insurance": 80000,
    "utilities": {
      "electric": 72000,
      "gas": 36000,
      "water": 48000,
      "trash": 24000,
      "total": 180000
    },
    "repairsAndMaintenance": {
      "general": 120000,
      "turnover": 60000,
      "hvac": 20000,
      "total": 200000
    },
    "managementFee": 150000,
    "managementFeePercent": 0.044,
    "payroll": {
      "salaries": 200000,
      "benefits": 50000,
      "payrollTaxes": 30000,
      "total": 280000
    },
    "administrative": 45000,
    "marketing": 35000,
    "contractServices": {
      "landscaping": 36000,
      "pest": 12000,
      "security": 24000,
      "pool": 18000,
      "total": 90000
    },
    "reserves": 60000,
    "totalOperatingExpenses": 1440000
  }
}
```

### Step 5: Calculate Key Metrics
```json
{
  "metrics": {
    "noi": 1974000,
    "noiMargin": 0.578,
    "expenseRatio": 0.422,
    "expensePerUnit": 7200,
    "revenuePerUnit": 17070,
    "noiPerUnit": 9870,
    "taxesPerUnit": 1600,
    "insurancePerUnit": 400,
    "utilitiesPerUnit": 900,
    "repairsPerUnit": 1000,
    "payrollPerUnit": 1400
  }
}
```

### Step 6: Trend Analysis (if monthly data is available)
```json
{
  "trends": {
    "revenueGrowthYoY": 0.03,
    "expenseGrowthYoY": 0.02,
    "noiGrowthYoY": 0.04,
    "occupancyTrend": "stable",
    "seasonality": {
      "highOccupancy": ["May", "Jun", "Jul"],
      "lowOccupancy": ["Dec", "Jan", "Feb"]
    }
  }
}
```

---

## Output Format

Return structured JSON using this schema:

```json
{
  "source": {
    "file": "t12-financials.xlsx",
    "period": "Jan 2025 - Dec 2025",
    "extractedAt": "2026-02-01T12:00:00Z",
    "confidence": 0.92
  },
  "summary": {
    "effectiveGrossIncome": 3414000,
    "totalExpenses": 1440000,
    "netOperatingIncome": 1974000,
    "expenseRatio": 0.422,
    "noiMargin": 0.578
  },
  "revenue": {
    "grossPotentialRent": 3600000,
    "vacancy": -180000,
    "vacancyPercent": 0.05,
    "concessions": -30000,
    "badDebt": -12000,
    "otherIncome": 120000,
    "effectiveGrossIncome": 3414000
  },
  "expenses": {
    "taxes": 320000,
    "insurance": 80000,
    "utilities": 180000,
    "repairs": 200000,
    "management": 150000,
    "payroll": 280000,
    "admin": 45000,
    "marketing": 35000,
    "contract": 90000,
    "reserves": 60000,
    "total": 1440000
  },
  "perUnit": {
    "units": 200,
    "revenue": 17070,
    "expenses": 7200,
    "noi": 9870,
    "taxes": 1600,
    "insurance": 400
  },
  "warnings": [],
  "dataGaps": []
}
```

---

## Quality Checks

Run these validation checks before finalizing:

1. **Math check**: Revenue − Expenses = NOI (within 1% tolerance)
2. **Expense ratio**: Use property-type context. For multifamily, 35–55% is a useful screening range; for other CRE property types, compare against sector-specific benchmarks instead of treating the multifamily range as universal
3. **Management fee**: Compare against property type and lease structure. For management-intensive assets, 3–5% of EGI is common; for leaner industrial structures it may be lower
4. **Taxes per unit**: Compare to property's known tax bill or market norms; large discrepancies may indicate the T12 is pre-reassessment
5. **Per-unit metrics**: Flag any expense category that is more than 2× or less than 0.5× typical benchmarks
6. **Below-the-line items excluded**: CapEx, debt service, and depreciation must not be included in operating expenses; identify and exclude if present

---

## When Data is Missing

### Missing Expense Categories
Some T12s combine line items differently (e.g., "Administrative & Marketing" as one line):
- Map to the closest standard category
- Note the mapping assumption in `warnings`

### Below-the-Line Items Included
CapEx, debt service, and depreciation should be excluded from operating expenses:
- Identify these items (look for "Capital Expenditures", "Depreciation", "Debt Service", "Mortgage")
- Exclude from total operating expenses
- Note in `warnings` that they were excluded and state the amount

### Partial Year Data
YTD instead of full T12:
- If more than 6 months of data: annualize by dividing total by months elapsed and multiplying by 12
- If fewer than 6 months: flag as insufficient for reliable T12 analysis
- Note the annualization basis in `warnings`

### Pro Forma Mixed In
Some statements mix actual and projected figures:
- Extract actuals only for the T12 output
- Flag any line item that appears to be a projection rather than actual (look for round numbers, footnotes about "stabilized", or budget-vs-actual formatting)
- Store pro forma items separately and note them in `warnings`

---

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **HIGH (0.90+)** | Full 12-month actual data, all major line items present, math validates |
| **MEDIUM (0.70–0.89)** | Some line items combined or missing, minor annualization needed, or one anomalous month |
| **LOW (<0.70)** | Partial year data, heavy combining of categories, pro forma mixed with actuals, or PDF extraction with ambiguous table structure |

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- **Multifamily Benchmarks** knowledge base — to validate expense ratios, per-unit metrics, and NOI margins against market norms for the property class and geography
- **Underwriting Calculations** knowledge base — for building a forward-looking financial model from T12 baseline data
- **Rent Roll Parser** skill — to cross-validate gross potential rent and occupancy against the rent roll
- **Offering Memo Parser** skill — to cross-validate the T12 NOI against the financial highlights in the OM
