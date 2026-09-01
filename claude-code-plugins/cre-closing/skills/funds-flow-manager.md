---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Funds Flow Manager

Calculate all closing prorations, credits, adjustments, and disbursements, and produce a settlement statement where total sources equal total uses — to the penny.

---

## When to Use This Skill

Use this skill when you need to prepare a closing settlement statement for a commercial real estate acquisition. It calculates buyer equity required, seller net proceeds, all proration splits, lender wire amounts, and disbursement schedules. Use it when you have finalized purchase price, loan terms, and a confirmed closing date and need to know exactly how much money moves where and when.

---

## What You'll Need to Provide

- **Purchase price** and **scheduled closing date**
- **Loan terms**: Loan amount, interest rate, origination fee (%), underwriting fee, tax/insurance/CapEx reserve months, any upfront reserve amounts, and whether origination fee is withheld from proceeds or paid at closing
- **Earnest money**: Amount already deposited
- **PSA credits and concessions**: Repair credits, seller concessions, any agreed price adjustments
- **Property tax information**: Current or prior-year annual tax bill amount; whether taxes are paid current or in arrears
- **Rent roll**: Current gross monthly rent collected (for rent proration calculation)
- **Security deposits**: Total tenant security deposits held by seller
- **Insurance**: Whether buyer is placing a new policy (no proration) or assuming existing (annual premium for proration)
- **Existing seller debt**: Outstanding principal balance, per-diem interest rate, any prepayment penalty, release fee
- **Closing costs** (to the extent known): Title insurance premium quotes, survey cost, environmental report cost, property condition report cost, recording fee rates, transfer tax rate and which party bears it, broker commission rate, attorney fee estimates
- **Proration methodology**: Specify whether the PSA uses a 365-day or 360-day year

---

## Mission

Manage the closing funds flow and produce the settlement statement. Calculate all prorations, credits, adjustments, and disbursements. Ensure total sources equal total uses, all amounts are accurate to the penny, and every party knows exactly how much money moves where and when.

---

## Strategy

### Step 1: Calculate Purchase Price Adjustments

**Prorations** (split between buyer and seller based on closing date):

Proration methodology: Determine if PSA specifies calendar year (365 days) or 360-day year.

```
daily_rate = annual_amount / days_in_year
seller_share = daily_rate * days_from_jan1_to_closing (or period start to closing)
buyer_share = daily_rate * days_from_closing_to_dec31 (or closing to period end)
```

- **Property Taxes**:
  - Current year tax amount (actual if billed, estimated if not yet billed)
  - Proration: seller responsible through day before closing, buyer from closing forward
  - If taxes not yet billed: use prior year as estimate, true-up post-closing
  - Note any special assessments and their proration treatment

- **Prepaid Rents**:
  - Rents collected for the month of closing
  - Seller retains rent through day before closing
  - Buyer credited for rent from closing day through end of month
  - Calculate: `buyer_credit = monthly_rent * (days_remaining_in_month / days_in_month)`

- **Utility Deposits**:
  - Deposits held by utility companies in seller's name
  - Transfer to buyer or credit at closing

- **Insurance Premium** (if policy is being assumed):
  - Prorate unexpired premium: seller credited for unused portion
  - If new policy: no proration needed

**Credits:**
- **Security Deposits**: All tenant security deposits credited to buyer (buyer assumes obligation to tenants)
- **Repair Credits**: Per PSA or due diligence negotiations (deferred maintenance, capital items)
- **Earnest Money**: Applied to purchase price as credit to buyer

**Adjustments:**
- **Seller Concessions**: Price reductions, closing cost contributions per PSA
- **Post-Closing Holdbacks**: Escrow for unresolved items (repair escrows, tenant improvement completions, proration true-ups)

### Step 2: Calculate Buyer's Closing Costs

**Loan Costs:**
- Loan origination fee: `{loan_amount} * {origination_rate}`
- Underwriting fee: `{flat amount}`
- Appraisal fee: `{flat amount}`
- Rate lock fee (if applicable): `{amount}`
- Lender legal fees: `{amount}`
- Loan application fee: `{amount}`

**Title and Recording:**
- Owner's title insurance premium: `{based on purchase price and rate schedule}`
- Lender's title insurance premium: `{based on loan amount and rate schedule}`
- Title endorsement fees: `{sum of endorsement premiums}`
- Title search / exam fee: `{amount}`
- Survey cost: `{amount}`
- Recording fees - deed: `{pages * per_page_rate}`
- Recording fees - mortgage: `{pages * per_page_rate}`
- Transfer taxes (buyer's portion): `{purchase_price * buyer_tax_rate}`

**Due Diligence Costs:**
- Environmental report (Phase I): `{amount}`
- Environmental report (Phase II, if applicable): `{amount}`
- Property condition report: `{amount}`
- Zoning report: `{amount}`

**Legal:**
- Buyer's attorney fees: `{amount}`
- Lender's attorney fees (if buyer-paid): `{amount}`

**Escrow Reserves (Lender Requirements):**
- Tax reserve: `{N months * monthly_tax_amount}`
- Insurance reserve: `{N months * monthly_insurance_premium}`
- CapEx / replacement reserve: `{per_unit * units or upfront amount}`
- Completion / repair reserve (if required): `{amount}`
- Other reserves per loan docs: `{amounts}`

**Prepaid Items:**
- Prepaid interest: `{loan_amount * daily_rate * days_from_closing_to_first_payment}`
- First month's insurance premium (if not escrowed): `{amount}`

### Step 3: Calculate Seller's Closing Costs

- **Broker Commission**: `{purchase_price * commission_rate}`
- **Transfer Taxes (Seller's Portion)**: `{purchase_price * seller_tax_rate}`
- **Payoff of Existing Debt**:
  - Outstanding principal balance
  - Accrued interest through closing date
  - Prepayment penalty (if applicable)
  - Release fee
  - Per diem interest calculation
- **Attorney Fees**: Seller's counsel
- **Prorated Expenses Owed**: Seller's share of expenses through closing
- **Miscellaneous**: UCC termination fees, lien release costs

### Step 4: Build Funds Flow (Sources and Uses)

**Sources of Funds:**
```
sources:
  buyer_equity:         {calculated}
  lender_funding:       {loan_amount - lender_retained_reserves}
  earnest_money_applied: {amount}
  seller_credits:       {if seller contributing to costs}

  total_sources:        {sum}
```

**Uses of Funds:**
```
uses:
  purchase_price:       {amount}
  buyer_closing_costs:  {sum from Step 2}
  lender_reserves:      {sum of escrow reserves}
  prepaid_items:        {sum of prepaids}
  prorations_to_seller: {net prorations favoring seller}

  total_uses:           {sum}
```

**Key Calculations:**
```
buyer_equity_required = purchase_price
                      + buyer_closing_costs
                      + lender_reserves
                      + prepaid_items
                      - loan_proceeds_to_closing
                      - earnest_money
                      - seller_credits
                      - net_proration_credit_to_buyer

lender_wire_to_closing = loan_amount
                       - lender_retained_reserves (taxes, insurance, CapEx held back)

seller_net_proceeds = purchase_price
                    - seller_closing_costs
                    - existing_debt_payoff
                    - prorations_owed_to_buyer
                    + prorations_owed_by_buyer
                    - holdbacks
```

### Step 5: Verify Balance (Total In = Total Out)

```
VERIFY: total_sources == total_uses

total_in  = buyer_equity + lender_wire + earnest_money + any_other_sources
total_out = seller_proceeds + seller_debt_payoff + buyer_costs_paid +
            lender_reserves + broker_commissions + transfer_taxes +
            recording_fees + attorney_fees + title_costs + holdbacks

ASSERT: total_in == total_out (to the penny)

IF imbalance:
  - Identify discrepancy amount
  - Trace through each line item
  - Resolve before finalizing
```

### Step 6: Identify Wire Instructions and Timing

- **Buyer's Equity Wire**:
  - Amount: `{buyer_equity_required}`
  - From: Buyer's bank account
  - To: Title company / escrow agent trust account
  - Timing: T-1 business day (or per title company requirements)
  - Call-back verification required

- **Lender's Funding Wire**:
  - Amount: `{lender_wire_to_closing}`
  - From: Lender
  - To: Title company / escrow agent trust account
  - Timing: Closing day (or T-1 per lender)
  - Conditions: All lender closing conditions must be met

- **Disbursement Wires** (from title company after recording):
  - Seller proceeds: `{amount}` to seller's account
  - Existing lender payoff: `{amount}` to payoff lender
  - Broker commission: `{amount}` to broker
  - Attorney fees: `{amounts}` to respective counsel
  - Transfer taxes: `{amount}` to taxing authority
  - Holdback escrow: `{amount}` to escrow agent

---

## Output Format

```json
{
  "settlement_statement": {
    "metadata": {
      "statement_date": "{date}",
      "property": "{property name/address}",
      "closing_date": "{date}",
      "purchase_price": "{amount}",
      "loan_amount": "{amount}"
    },
    "buyer_statement": {
      "debits": [
        { "item": "Purchase Price", "amount": "{amount}" },
        { "item": "Loan Origination Fee ({rate}%)", "amount": "{amount}" },
        { "item": "Underwriting Fee", "amount": "{amount}" },
        { "item": "Appraisal Fee", "amount": "{amount}" },
        { "item": "Owner's Title Insurance", "amount": "{amount}" },
        { "item": "Lender's Title Insurance", "amount": "{amount}" },
        { "item": "Title Endorsements", "amount": "{amount}" },
        { "item": "Survey", "amount": "{amount}" },
        { "item": "Environmental Report", "amount": "{amount}" },
        { "item": "Property Condition Report", "amount": "{amount}" },
        { "item": "Recording Fees - Deed", "amount": "{amount}" },
        { "item": "Recording Fees - Mortgage", "amount": "{amount}" },
        { "item": "Transfer Tax (Buyer Portion)", "amount": "{amount}" },
        { "item": "Buyer's Attorney", "amount": "{amount}" },
        { "item": "Lender's Attorney", "amount": "{amount}" },
        { "item": "Tax Reserve ({N} months)", "amount": "{amount}" },
        { "item": "Insurance Reserve ({N} months)", "amount": "{amount}" },
        { "item": "CapEx Reserve", "amount": "{amount}" },
        { "item": "Prepaid Interest ({N} days)", "amount": "{amount}" }
      ],
      "credits": [
        { "item": "Loan Proceeds", "amount": "{amount}" },
        { "item": "Earnest Money Deposit", "amount": "{amount}" },
        { "item": "Seller Concession", "amount": "{amount}" },
        { "item": "Proration Credit - Prepaid Rents", "amount": "{amount}" },
        { "item": "Proration Credit - Property Taxes", "amount": "{amount}" },
        { "item": "Security Deposit Credit", "amount": "{amount}" },
        { "item": "Repair Credit", "amount": "{amount}" }
      ],
      "total_debits": "{amount}",
      "total_credits": "{amount}",
      "buyer_equity_required": "{debits - credits}"
    },
    "seller_statement": {
      "credits": [
        { "item": "Purchase Price", "amount": "{amount}" },
        { "item": "Proration Credit - Property Taxes", "amount": "{amount if taxes prepaid by seller}" }
      ],
      "debits": [
        { "item": "Broker Commission ({rate}%)", "amount": "{amount}" },
        { "item": "Transfer Tax (Seller Portion)", "amount": "{amount}" },
        { "item": "Existing Mortgage Payoff", "amount": "{amount}" },
        { "item": "Prepayment Penalty", "amount": "{amount}" },
        { "item": "Seller's Attorney", "amount": "{amount}" },
        { "item": "Proration - Prepaid Rents to Buyer", "amount": "{amount}" },
        { "item": "Proration - Property Taxes Owed", "amount": "{amount}" },
        { "item": "Security Deposits Transferred", "amount": "{amount}" },
        { "item": "Repair Credit to Buyer", "amount": "{amount}" },
        { "item": "Post-Closing Holdback", "amount": "{amount}" }
      ],
      "total_credits": "{amount}",
      "total_debits": "{amount}",
      "seller_net_proceeds": "{credits - debits}"
    },
    "funds_flow_summary": {
      "sources": [
        { "source": "Buyer Equity", "amount": "{amount}" },
        { "source": "Lender Funding", "amount": "{amount}" },
        { "source": "Earnest Money (previously deposited)", "amount": "{amount}" }
      ],
      "total_sources": "{amount}",
      "uses": [
        { "use": "Seller Net Proceeds", "amount": "{amount}" },
        { "use": "Existing Debt Payoff", "amount": "{amount}" },
        { "use": "Broker Commission", "amount": "{amount}" },
        { "use": "Transfer Taxes", "amount": "{amount}" },
        { "use": "Recording Fees", "amount": "{amount}" },
        { "use": "Title Insurance and Endorsements", "amount": "{amount}" },
        { "use": "Attorney Fees (all parties)", "amount": "{amount}" },
        { "use": "Lender Reserves (held by lender)", "amount": "{amount}" },
        { "use": "Prepaid Interest", "amount": "{amount}" },
        { "use": "DD Costs (environmental, PCA, survey)", "amount": "{amount}" },
        { "use": "Post-Closing Holdback", "amount": "{amount}" }
      ],
      "total_uses": "{amount}",
      "balance_check": {
        "total_sources": "{amount}",
        "total_uses": "{amount}",
        "difference": "{should be $0.00}",
        "balanced": "yes / no"
      }
    },
    "wire_schedule": {
      "incoming": [
        {
          "wire": "Buyer Equity",
          "amount": "{amount}",
          "from": "{buyer entity}",
          "to": "{title company trust account}",
          "send_date": "{date}",
          "expected_receipt": "{date}",
          "status": "pending / sent / received"
        },
        {
          "wire": "Lender Funding",
          "amount": "{amount}",
          "from": "{lender}",
          "to": "{title company trust account}",
          "send_date": "{date}",
          "expected_receipt": "{date}",
          "status": "pending / authorized / received"
        }
      ],
      "outgoing": [
        {
          "wire": "Seller Proceeds",
          "amount": "{amount}",
          "to": "{seller entity}",
          "timing": "after recording",
          "status": "pending"
        },
        {
          "wire": "Existing Debt Payoff",
          "amount": "{amount}",
          "to": "{existing lender}",
          "timing": "at closing",
          "status": "pending"
        },
        {
          "wire": "Broker Commission",
          "amount": "{amount}",
          "to": "{broker/firm}",
          "timing": "after recording",
          "status": "pending"
        }
      ]
    },
    "proration_calculations": {
      "methodology": "calendar year (365 days) / 360-day year",
      "closing_date": "{date}",
      "property_taxes": {
        "annual_amount": "{amount}",
        "daily_rate": "{amount}",
        "seller_days": "{N}",
        "seller_share": "{amount}",
        "buyer_days": "{N}",
        "buyer_share": "{amount}",
        "credit_direction": "buyer / seller",
        "credit_amount": "{amount}",
        "based_on": "actual bill / prior year estimate",
        "true_up_required": "yes/no"
      },
      "prepaid_rents": {
        "monthly_gross_rent": "{amount}",
        "daily_rate": "{amount}",
        "seller_days_in_month": "{N}",
        "seller_share": "{amount}",
        "buyer_days_in_month": "{N}",
        "buyer_share": "{amount}",
        "credit_to_buyer": "{amount}"
      },
      "other_prorations": [
        {
          "item": "{description}",
          "annual_amount": "{amount}",
          "daily_rate": "{amount}",
          "seller_share": "{amount}",
          "buyer_share": "{amount}",
          "credit_direction": "buyer / seller",
          "credit_amount": "{amount}"
        }
      ],
      "net_proration_summary": {
        "total_credits_to_buyer": "{amount}",
        "total_credits_to_seller": "{amount}",
        "net_proration": "{amount to buyer / amount to seller}"
      }
    },
    "equity_summary": {
      "purchase_price": "{amount}",
      "total_buyer_closing_costs": "{amount}",
      "total_lender_reserves": "{amount}",
      "total_prepaids": "{amount}",
      "gross_cost": "{sum}",
      "less_loan_proceeds": "{amount}",
      "less_earnest_money": "{amount}",
      "less_seller_credits": "{amount}",
      "less_net_proration_credit": "{amount}",
      "total_equity_required": "{amount}",
      "equity_as_percent_of_price": "{X}%"
    },
    "lender_disbursement": {
      "gross_loan_amount": "{amount}",
      "less_origination_fee": "{amount if withheld}",
      "less_tax_reserve": "{amount}",
      "less_insurance_reserve": "{amount}",
      "less_capex_reserve": "{amount}",
      "less_other_reserves": "{amount}",
      "net_wire_to_closing": "{amount}"
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "recommendation": "{action}"
      }
    ],
    "uncertainty_flags": [
      {
        "field_name": "",
        "reason": "estimated | assumed | unverified | stale_data | interpolated",
        "impact": "Description of what downstream analysis this affects"
      }
    ]
  }
}
```

---

## Quality Checks

Before finalizing the settlement statement, run all of these checks:

1. **Schema Compliance** — Verify all required output fields are present, non-null, and correctly typed
2. **Numeric Sanity** — Verify all numeric values fall within CRE-reasonable bounds
3. **Cross-Reference Validation** — Verify purchase price and loan amount are consistent throughout all sections
4. **Completeness Assessment** — Verify every strategy step produced output or noted a data gap
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any estimated values

**Self-Validation Checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| purchasePrice | > 0, match provided deal terms | Mismatch |
| loanAmount | Match provided financing terms | Mismatch |
| equityRequired | purchasePrice − loanAmount + closingCosts | Arithmetic mismatch |
| totalCredits + totalDebits | Must balance | Imbalanced |
| closingCostVariance | ≤ 5% of estimated total | Exceeds threshold |
| wireInstructions | Must be present for all parties | Missing wire info |
| prorations | Must be calculated as of closing date | Missing or wrong date |

**Detailed Validation:**

| Check | Method |
|-------|--------|
| Prorations mathematically correct | Verify: daily rate × days = share amount |
| Tax proration uses correct basis | Confirm actual bill or prior year estimate |
| Rent proration uses correct rent | Cross-reference with provided rent roll |
| All buyer costs included | Compare against loan docs, title quote, PSA |
| All seller costs included | Compare against PSA, payoff statement, broker agreement |
| Loan proceeds match | Net wire = loan amount − withheld reserves |
| Earnest money applied | Deposit amount credited to buyer |
| Security deposits credited | Full deposit balance credited to buyer |
| Sources = Uses | Total in equals total out to the penny |
| Equity calculation correct | Equity = price + costs − loan − credits |
| Wire amounts sum correctly | All outgoing wires = total uses |
| Proration methodology consistent | Same day-count method used throughout |

---

## When Data is Missing

When required financial data is unavailable:

- **Transfer tax rates**: Look up the applicable state and county transfer tax rates for the property jurisdiction; note the source and date
- **Recording fees**: Use jurisdiction-specific per-page recording fee schedules; estimate page counts if documents not yet finalized
- **Title insurance premiums**: Use the applicable state's rate schedule and filed rates; note as estimate pending final title quote
- **Seller's existing debt**: If payoff statement is not yet available, use known outstanding balance and estimate per-diem interest; flag as estimate requiring confirmation before closing
- **Prior-year tax amount**: If current-year tax bill not yet issued, use prior-year amount as the proration basis and flag for true-up post-closing
- **Mark in output**: Add an entry to `uncertainty_flags` for every estimated or assumed amount, with the reason and the impact on total equity required
- **Do not halt**: Complete all other calculations using available data; clearly identify which line items are estimates vs. confirmed figures

---

## Confidence Scoring

Apply confidence levels to all findings and outputs:

| Level | Criteria |
|-------|----------|
| **HIGH** | Based on verified source documents; no assumptions; data directly observed |
| **MEDIUM** | Based on partially verified data; minor assumptions made; some data interpolated |
| **LOW** | Based on unverified data; significant assumptions; stale or incomplete sources |

Set `confidence_level` in the output and populate `uncertainty_flags` for any finding rated MEDIUM or LOW.

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- **Underwriting Calculations** knowledge base — for loan sizing, reserve requirement formulas, and DSCR/Debt Yield calculations
- **Lender Criteria** knowledge base — for typical reserve requirements, prepaid interest conventions, and origination fee structures by lender type (Agency, CMBS, bank)
- **Legal Checklist** knowledge base — for transfer tax rates and recording fee schedules by state/county

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
