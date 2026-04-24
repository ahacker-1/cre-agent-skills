# T-12 Actuals Template

Use this template to supply a **trailing twelve-month** line-item income statement to the AM-pack T-12 / Run-Rate Normalization skill. Each row is a canonical line item from the AM OpEx taxonomy (`research/asset-management/_taxonomy-seed.md` §1); each column is a calendar month, ending with the T-12 total. Populate actual collected income and actual paid expenses for each month of the trailing window (rolling 12 months ending at the report date — not a fiscal year). Leave a cell blank if the true value is unknown; do NOT enter zero as a placeholder.

**Conventions.**
- Figures in dollars, positive for revenue and expense unless otherwise noted.
- Vacancy Loss, Concessions, Bad Debt are shown as **positive numbers** that are subtracted from GPR to arrive at EGI (see formulas at bottom).
- Replacement Reserves are **not** included here — per AM pack convention they sit below NOI as an NCF adjustment, not an operating expense.
- Report month-1 through month-12 in calendar order ending on the T-12 end date. The header row below uses Jan–Dec as placeholders; rename to match your actual trailing window (e.g., Apr-24 through Mar-25).

---

## Property Identifier

- **Property Name:**
- **T-12 Period Ending:**
- **Unit Count:**

## Income

| Line Item | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | T-12 Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross Potential Rent (GPR) | 150,000 | 150,000 | 150,000 | 152,000 | 152,000 | 152,000 | 152,000 | 152,000 | 154,000 | 154,000 | 154,000 | 154,000 | 1,826,000 |
| Other Income | 8,500 | 8,800 | 9,100 | 8,900 | 9,200 | 9,500 | 9,400 | 9,300 | 9,600 | 9,400 | 9,200 | 9,100 | 110,000 |
| Vacancy Loss (subtract) | 7,500 | 7,500 | 7,500 | 7,600 | 7,600 | 7,600 | 9,120 | 9,120 | 9,240 | 9,240 | 9,240 | 9,240 | 100,500 |
| Concessions (subtract) | 2,000 | 2,000 | 2,000 | 1,500 | 1,500 | 1,500 | 1,500 | 1,500 | 1,500 | 1,500 | 1,500 | 1,500 | 19,500 |
| Bad Debt (subtract) | 1,800 | 1,800 | 1,800 | 1,850 | 1,850 | 1,850 | 1,850 | 1,850 | 1,900 | 1,900 | 1,900 | 1,900 | 22,250 |
| **Effective Gross Income (EGI)** | | | | | | | | | | | | | |

## Operating Expenses

| Line Item | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | T-12 Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Property Taxes | | | | | | | | | | | | | |
| Insurance | | | | | | | | | | | | | |
| Utilities — Water/Sewer | | | | | | | | | | | | | |
| Utilities — Trash | | | | | | | | | | | | | |
| Utilities — Gas | | | | | | | | | | | | | |
| Utilities — Electric | | | | | | | | | | | | | |
| Repairs & Maintenance (R&M) | | | | | | | | | | | | | |
| Turnover / Make-Ready | | | | | | | | | | | | | |
| Contract Services | | | | | | | | | | | | | |
| Management Fee | | | | | | | | | | | | | |
| Payroll (Salaries & Personnel) | | | | | | | | | | | | | |
| Administrative (G&A) | | | | | | | | | | | | | |
| Marketing / Advertising | | | | | | | | | | | | | |
| Professional Fees | | | | | | | | | | | | | |
| Communications | | | | | | | | | | | | | |
| **Total Operating Expenses** | | | | | | | | | | | | | |
| **Net Operating Income (NOI)** | | | | | | | | | | | | | |

---

## Formulas (verification aids)

```
EGI = GPR + Other Income − Vacancy Loss − Concessions − Bad Debt
Total OpEx = Property Taxes + Insurance + Utilities (W/S + Trash + Gas + Electric)
           + R&M + Turnover + Contract Services + Management Fee
           + Payroll + Administrative + Marketing + Professional Fees + Communications
NOI = EGI − Total OpEx           (AM-pack convention: excludes Replacement Reserves)
NCF = NOI − Replacement Reserves (report separately if needed downstream)
```
