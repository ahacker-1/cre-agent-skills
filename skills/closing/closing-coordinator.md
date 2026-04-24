# Closing Coordinator

Manage a real estate closing checklist, verify all conditions are met, and produce a definitive GO / NOT READY / CONDITIONAL readiness verdict with a day-by-day closing timeline.

---

## When to Use This Skill

Use this skill when you are approaching the closing date on a commercial real estate acquisition and need to track every outstanding condition across title, financing, legal, insurance, estoppels, and prorations in one place. It is especially useful when coordinating multiple parties (buyer, seller, lender, title company, counsel) and you need a clear status report and action-item list for each party.

---

## What You'll Need to Provide

- **Property details**: Name, address, purchase price, and scheduled closing date
- **PSA summary**: Contingencies, earnest money amount, any amendments or extensions, key deadlines
- **Financing status**: Loan commitment status, lender conditions outstanding, whether loan documents have been executed
- **Title and survey status**: Status of title commitment, any exceptions or curative items, endorsements ordered
- **Environmental and inspection status**: Phase I/II completion status, any findings or remediation requirements
- **Estoppel status**: How many estoppels collected, whether the PSA threshold is met
- **Insurance status**: Whether property and liability insurance has been bound, lender endorsements issued
- **Legal/transfer documents status**: Deed, bill of sale, assignment of leases, entity documents (good standing, resolutions)
- **Proration and settlement statement status**: Whether prorations have been agreed and the settlement statement has been circulated

---

## Mission

Manage the closing checklist and verify all conditions are met for closing. Coordinate between buyer, seller, lender, title company, and other parties. Produce a definitive GO / NOT READY / CONDITIONAL readiness verdict and manage the closing timeline to ensure a smooth, on-time closing.

---

## Strategy

### Step 1: Build Master Closing Checklist

Synthesize all conditions into a single master checklist organized by category:

**Category A: PSA Conditions**
- All contingencies satisfied or waived
- Earnest money deposit confirmed
- Hard money deadlines passed/met
- Seller deliverables received
- Buyer deliverables prepared
- No default by either party
- All PSA amendments/extensions executed

**Category B: Title and Survey**
- Title commitment received and reviewed
- All objectionable exceptions cured or waived
- Survey accepted
- Title endorsements ordered
- Owner's title policy to be issued at closing
- Lender's title policy to be issued at closing
- Gap search ordered (date-down endorsement)

**Category C: Environmental**
- Phase I ESA completed and accepted
- Phase II (if required) completed and accepted
- Environmental insurance (if required) bound
- Remediation plan (if required) in place
- No new environmental conditions discovered

**Category D: Financing**
- Loan commitment received
- All commitment conditions satisfied
- Loan documents executed
- Lender closing conditions met:
  - Appraisal accepted
  - Insurance bound per lender requirements
  - Title per lender requirements
  - Survey per lender requirements
  - Entity documents delivered to lender
  - Legal opinion delivered (if required)
  - Environmental report delivered
  - Property condition report delivered
  - Estoppel threshold met
  - Rent roll certified
  - Operating statement certified
  - DSCR / Debt Yield test passed
- Lender funding authorized
- Wire instructions confirmed

**Category E: Legal Documents**
- Deed prepared and ready for execution
- Bill of Sale prepared
- Assignment of Leases prepared
- Assignment of Contracts prepared
- Tenant Notification Letters prepared
- FIRPTA Certificate executed by seller
- Transfer Tax Declaration prepared
- Entity documents current and delivered:
  - Buyer Good Standing (buyer's state + property state)
  - Seller Good Standing (seller's state + property state)
  - Authorization Resolutions executed
  - Incumbency Certificates executed

**Category F: Estoppels**
- Minimum threshold met per PSA
- Material discrepancies resolved
- Estoppel-related price adjustments (if any) agreed

**Category G: Insurance**
- Property insurance bound
- Liability insurance bound
- Flood insurance bound (if required)
- All lender endorsements issued
- Evidence of insurance delivered to lender
- Evidence of insurance delivered to title company

**Category H: Prorations and Adjustments**
- Proration calculations agreed by buyer and seller
- Settlement statement approved by all parties
- Closing cost allocation confirmed
- Credits and adjustments finalized

**Category I: Funds**
- Buyer equity wire confirmed (amount and timing)
- Lender funding wire confirmed (amount and timing)
- Title company wire instructions verified
- Seller payoff amounts confirmed

### Step 2: Verify Each Category

For each item on the master checklist:
- Review the status based on information provided
- Classify as: `complete` | `in progress` | `outstanding` | `waived` | `N/A`
- If outstanding: identify responsible party, deadline, and blocking status
- If in progress: assess likelihood of completion by closing

### Step 3: Track Outstanding Items

Build an outstanding items tracker:

| Item | Category | Responsible Party | Deadline | Days Remaining | Blocking | Priority | Notes |
|------|----------|-------------------|----------|----------------|----------|----------|-------|
| {item} | {cat} | {party} | {date} | {N} | yes/no | critical/high/medium/low | {notes} |

Sort by: blocking items first, then by deadline, then by priority.

### Step 4: Assess Closing Readiness

Apply readiness logic:

```
IF all categories complete OR all outstanding items non-blocking:
  verdict = "GO"

ELIF blocking items exist BUT all can be resolved by closing date:
  verdict = "CONDITIONAL"
  conditions = [list of items that must be resolved]

ELIF blocking items exist AND any cannot be resolved by closing date:
  verdict = "NOT READY"
  blockers = [list of items preventing closing]
  recommended_action = "request extension / negotiate resolution / terminate"
```

### Step 5: Prepare Closing Timeline

Build a day-by-day closing timeline:

**T-5 Business Days (or earlier):**
- Final title search / gap search
- Confirm all loan conditions met
- Confirm insurance binding
- Confirm estoppel threshold

**T-3 Business Days:**
- Settlement statement circulated for approval
- Wire instructions confirmed and verified (call-back verification)
- All documents in final form

**T-2 Business Days:**
- Settlement statement approved by all parties
- Pre-signing of documents (if applicable)
- Buyer equity amount confirmed

**T-1 Business Day:**
- Buyer equity wire sent
- Lender funding wire authorized
- Final document review

**Closing Day (T-0):**
- Signing of remaining documents
- Title company confirms receipt of all funds
- Recording of deed and mortgage
- Title company confirms recording
- Disbursement of funds per settlement statement
- Keys / access transferred

**Post-Closing:**
- Recorded documents returned
- Final title policy issued
- Post-closing proration true-ups
- Tenant notification letters sent
- Utility account transfers
- Vendor notification and contract assignments effective

### Step 6: Identify Post-Closing Obligations

Compile all post-closing items:
- Proration true-ups (taxes, when actual bills received)
- Security deposit transfers (if not handled at closing)
- Tenant notification mailing
- Vendor/utility account transfers
- Insurance policy name changes (if assumed)
- Property management transition
- Lender post-closing deliverables (original recorded mortgage, final title policy)
- Any PSA survival obligations (reps, indemnification, holdbacks)

---

## Output Format

```json
{
  "closing_readiness_report": {
    "metadata": {
      "report_date": "{date}",
      "property": "{property name/address}",
      "closing_date": "{date}",
      "days_to_closing": "{N}"
    },
    "readiness_verdict": "GO / NOT READY / CONDITIONAL",
    "verdict_summary": "{1-2 sentence explanation}",
    "master_checklist": {
      "total_items": "{N}",
      "complete": "{N}",
      "in_progress": "{N}",
      "outstanding": "{N}",
      "waived": "{N}",
      "not_applicable": "{N}",
      "completion_rate": "{X}%",
      "categories": [
        {
          "category": "A: PSA Conditions",
          "items_total": "{N}",
          "items_complete": "{N}",
          "items_outstanding": "{N}",
          "status": "clear / issues",
          "items": [
            {
              "item": "{description}",
              "status": "complete / in progress / outstanding / waived / N/A",
              "responsible_party": "{party}",
              "deadline": "{date}",
              "blocking": "yes/no",
              "notes": "{details}"
            }
          ]
        },
        {
          "category": "B: Title and Survey",
          "items_total": "{N}",
          "items_complete": "{N}",
          "items_outstanding": "{N}",
          "status": "clear / issues",
          "items": [
            {
              "item": "{description}",
              "status": "{status}",
              "responsible_party": "{party}",
              "deadline": "{date}",
              "blocking": "yes/no",
              "notes": "{details}"
            }
          ]
        },
        { "category": "C: Environmental", "_comment": "same structure as above" },
        { "category": "D: Financing", "_comment": "same structure as above" },
        { "category": "E: Legal Documents", "_comment": "same structure as above" },
        { "category": "F: Estoppels", "_comment": "same structure as above" },
        { "category": "G: Insurance", "_comment": "same structure as above" },
        { "category": "H: Prorations and Adjustments", "_comment": "same structure as above" },
        { "category": "I: Funds", "_comment": "same structure as above" }
      ]
    },
    "outstanding_items": {
      "blocking": [
        {
          "item": "{description}",
          "category": "{category}",
          "responsible_party": "{party}",
          "deadline": "{date}",
          "days_remaining": "{N}",
          "resolution_plan": "{description}",
          "likelihood_of_resolution": "high / medium / low"
        }
      ],
      "non_blocking": [
        {
          "item": "{description}",
          "category": "{category}",
          "responsible_party": "{party}",
          "deadline": "{date}",
          "notes": "{details}"
        }
      ]
    },
    "conditional_items": [
      {
        "_comment": "Only if verdict is CONDITIONAL",
        "condition": "{description}",
        "must_be_resolved_by": "{date}",
        "responsible_party": "{party}",
        "fallback_action": "{if not resolved}"
      }
    ],
    "closing_timeline": [
      {
        "date": "{date}",
        "days_to_closing": "{T-N}",
        "events": [
          {
            "event": "{description}",
            "responsible_party": "{party}",
            "status": "scheduled / complete / pending",
            "time": "{time if specific}"
          }
        ]
      }
    ],
    "post_closing_obligations": [
      {
        "obligation": "{description}",
        "responsible_party": "{party}",
        "deadline": "{date or ongoing}",
        "category": "proration / notification / transfer / lender / PSA survival",
        "status": "pending / scheduled"
      }
    ],
    "party_action_items": {
      "buyer": [
        {
          "action": "{description}",
          "deadline": "{date}",
          "priority": "critical / high / medium"
        }
      ],
      "seller": [
        {
          "action": "{description}",
          "deadline": "{date}",
          "priority": "critical / high / medium"
        }
      ],
      "lender": [
        {
          "action": "{description}",
          "deadline": "{date}",
          "priority": "critical / high / medium"
        }
      ],
      "title_company": [
        {
          "action": "{description}",
          "deadline": "{date}",
          "priority": "critical / high / medium"
        }
      ],
      "buyer_counsel": [
        {
          "action": "{description}",
          "deadline": "{date}",
          "priority": "critical / high / medium"
        }
      ]
    },
    "risk_flags": [
      {
        "flag": "{description}",
        "severity": "low / medium / high / critical",
        "category": "{checklist category}",
        "recommendation": "{action}"
      }
    ],
    "uncertainty_flags": [
      {
        "field_name": "",
        "reason": "estimated | assumed | unverified | stale_data | interpolated",
        "impact": "Description of what downstream analysis this affects"
      }
    ],
    "stabilization_handoff": {
      "_comment": "(optional, populated if asset will be fed to cre-asset-management pack for post-acquisition operations)",
      "owner_name": "",
      "acquisition_date": "",
      "day1_rent_roll_ref": "",
      "day1_t12_ref": "",
      "business_plan_summary": ""
    }
  }
}
```

---

## Quality Checks

Before finalizing output, run all of these checks:

1. **Schema Compliance** — Verify all required output fields are present, non-null, and correctly typed
2. **Numeric Sanity** — Verify all numeric values fall within CRE-reasonable bounds
3. **Cross-Reference Validation** — Verify unit counts, property address, and party names are consistent throughout the report
4. **Completeness Assessment** — Verify every checklist category has been assessed and produced a status
5. **Confidence Scoring** — Set `confidence_level` and populate `uncertainty_flags` for any finding based on estimated or unverified data

**Self-Validation Checks:**

| Field | Valid Range | Flag If |
|-------|-----------|---------|
| preClosingItems | All 6 required items addressed | Any missing |
| readinessVerdict | GO, NOT_READY, CONDITIONAL | Invalid value |
| outstandingItemCount | If GO, must be 0 blocking items | Blocking items present with GO verdict |
| allPartiesConfirmed | Must include buyer, seller, lender, title company | Any party missing from action items |
| closingDate | Must be future date | Past date entered |

---

## Red Flags & Dealbreakers

Certain conditions must trigger a NOT READY verdict regardless of other status. If any of the following are unresolved, set `readiness_verdict = "NOT READY"` and add to blocking items with category "dealbreaker":

| Dealbreaker | Detection Criteria |
|------------|-------------------|
| Active title dispute or lis pendens | Unresolved title issue reported in title commitment or legal review |
| Property in bankruptcy estate | Identified in title review or legal due diligence |
| Fraud in title chain | Identified in title review |
| Dissolved entity ownership | Identified in entity document review or title review |
| Criminal activity nexus | Identified in estoppel review or tenant background screening |
| Uninsurable property condition | Insurance carrier unable to bind coverage |
| Environmental contamination above acceptable thresholds | Phase I/II findings indicate RECs requiring remediation prior to closing |
| Structural failure or condemnation risk | Property condition assessment identifies imminent structural failure or active condemnation proceeding |

When a dealbreaker is detected:
1. Set `readiness_verdict = "NOT READY"`
2. Add to blocking outstanding items with category "dealbreaker"
3. Include in verdict summary with recommended action (request extension, negotiate resolution, or terminate)

---

## When Data is Missing

When status information for a checklist item is not available:

- **Attempt to gather**: Ask the user for the status of the specific item
- **Note the assumption**: If proceeding without confirmation, mark the item as `outstanding` with a note that status is unconfirmed — do not assume `complete`
- **Mark in output**: Add an entry to `uncertainty_flags` with the field name, reason (unverified), and the impact on the readiness verdict
- **Impact on verdict**: Any unconfirmed item that would be blocking if outstanding should be treated as blocking — do not issue a GO verdict when critical items are unverified
- **Continue analysis**: Complete all other checklist categories and note in the verdict summary which items remain unconfirmed

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
- **Legal Checklist** knowledge base — for detailed document requirements by document type and jurisdiction
- **Lender Criteria** knowledge base — for lender-specific closing condition checklists and common agency/CMBS requirements
- **Underwriting Calculations** knowledge base — for verifying DSCR and Debt Yield tests referenced in lender closing conditions
- Downstream cross-reference: [Annual Operating Budget Builder](../asset-management/annual-operating-budget-builder.md) — consumes `stabilization_handoff` block for next-year budget construction
