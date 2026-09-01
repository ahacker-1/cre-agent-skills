---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Document Classifier

Identify, classify, and organize incoming CRE deal documents - determining what type each document is, extracting key data points from each, and surfacing any missing or conflicting information.

---

## When to Use This Skill

Use this skill at the start of a new deal when you have a collection of documents (rent rolls, financials, offering memos, PSAs, inspection reports, lease materials, etc.) and need to understand what you have, what each document contains, and what is still missing. It is the first step before performing underwriting, due diligence, or financial modeling across multifamily, industrial, and other CRE workflows - getting your documents organized and validated.

---

## What You'll Need to Provide

- One or more deal documents in any of these formats: PDF, Excel/CSV, Word, images (JPG/PNG)
- The documents can include any combination of: rent roll, T-12 financial statement, offering memorandum, pro forma, PSA/purchase contract, survey/site plan, inspection/PCA report, environmental report, title commitment, or lease abstracts
- If you know what document types you have, describe them — if not, describe what you received and this skill will classify them
- Optionally, tell the skill what property address or deal name these documents relate to

---

## Mission

Scan incoming documents, identify document types, extract relevant CRE deal data, validate completeness, and generate a structured summary of what data has been captured and what gaps remain - ready for use in underwriting and due diligence.

---

## Strategy

### Step 1: Inventory All Documents

List every document provided. For each document, record:
- Filename or description
- File type (PDF, Excel, Word, image)
- Approximate length or size

### Step 2: Classify Each Document

For each document, determine its type using filename patterns and content indicators:

| Document Type | Filename Patterns | Key Indicators |
|---------------|-------------------|----------------|
| Rent Roll | `*rent*roll*`, `*unit*mix*`, `*roster*` | Unit numbers, rent amounts, lease dates |
| T12 Financials | `*t12*`, `*trailing*`, `*income*statement*`, `*operating*` | Revenue, expenses, NOI, monthly columns |
| Offering Memo | `*om*`, `*offering*`, `*memorandum*`, `*marketing*` | Property description, asking price, photos |
| Pro Forma | `*pro*forma*`, `*projections*`, `*underwriting*` | Future projections, assumptions |
| PSA | `*psa*`, `*purchase*`, `*contract*`, `*agreement*` | Legal terms, dates, conditions |
| Survey/Site Plan | `*survey*`, `*site*`, `*plat*` | Property boundaries, dimensions |
| Inspection/PCA | `*pca*`, `*inspection*`, `*condition*` | Building systems, deferred maintenance |
| Environmental | `*phase*`, `*environmental*`, `*esa*` | Environmental findings |
| Title | `*title*`, `*commitment*` | Ownership, encumbrances |
| Lease Abstracts | `*abstract*`, `*lease*` | Tenant terms, options |

**Classification process:**
1. Check the filename against patterns above
2. If unclear, read the first page or first rows to identify content
3. Assign a document type and a confidence level (%)
4. Flag any document that cannot be classified for user confirmation

### Step 3: Extract Key Data by Document Type

#### From a Rent Roll
```json
{
  "unitMix": [
    {
      "type": "1BR/1BA",
      "count": 80,
      "avgSqFt": 725,
      "marketRent": 1350,
      "inPlaceRent": 1225
    }
  ],
  "totalUnits": 200,
  "occupiedUnits": 186,
  "occupancy": 0.93,
  "totalSqFt": 180000,
  "avgRentPerSqFt": 1.63
}
```

#### From T12 Financial Statements
```json
{
  "trailingT12Revenue": 3360000,
  "trailingT12Expenses": 1440000,
  "currentNOI": 1920000,
  "expenseRatio": 0.429,
  "revenueBreakdown": {
    "grossPotentialRent": 3600000,
    "vacancy": -180000,
    "concessions": -30000,
    "otherIncome": 120000
  },
  "expenseBreakdown": {
    "taxes": 320000,
    "insurance": 80000,
    "utilities": 180000,
    "repairs": 200000,
    "management": 150000,
    "payroll": 280000,
    "other": 230000
  }
}
```

#### From an Offering Memo
```json
{
  "property": {
    "name": "",
    "address": "",
    "city": "",
    "state": "",
    "zip": "",
    "county": "",
    "propertyType": "multifamily | industrial | office | retail | mixed-use | unknown",
    "yearBuilt": 0,
    "totalUnits": 0,
    "totalSqFt": 0,
    "stories": 0,
    "buildings": 0,
    "parking": {},
    "amenities": []
  },
  "askingPrice": 0,
  "pricePerUnit": 0,
  "seller": {
    "name": "",
    "broker": "",
    "brokerFirm": ""
  }
}
```

### Step 4: Cross-Validate Extracted Data

After extracting data from all documents:

1. Compare the same data points across documents (e.g., unit count from rent roll vs. offering memo)
2. Flag conflicts: e.g., "Unit count: Rent Roll says 200, OM says 198"
3. Flag missing required fields:
   - **Required**: address, totalUnits, askingPrice
   - **Important**: yearBuilt, occupancy, NOI
   - **Optional**: amenities, parking details

### Step 5: Produce Extraction Summary

Generate a structured summary of what was found:

```markdown
## Documents Processed
| File | Type | Confidence | Key Fields Extracted |
|------|------|------------|----------------------|
| rent-roll.xlsx | Rent Roll | 95% | 12 fields |
| t12.xlsx | T12 Financials | 90% | 18 fields |

## Data Completeness
- Required fields: X/8
- Important fields: X/6
- Optional fields: X/15

## Conflicts Detected
- [list any conflicts]

## Data Gaps
- [list missing documents or fields]

## Documents That Could Not Be Classified
- [list any ambiguous files]
```

### Step 6: Note What Is Still Missing

Flag standard CRE documents that were not provided and explain their importance:

| Missing Document | Importance | When Needed |
|-----------------|------------|-------------|
| Phase I ESA | High | Environmental clearance required for financing |
| PCA / Inspection Report | High | Capital reserve and deferred maintenance assessment |
| Survey | Medium | Required for title insurance and legal description |
| Title Commitment | High | Ownership verification and lien search |
| Lease Abstracts | Medium | Individual tenant term verification |
| PSA / Purchase Agreement | High | Contract terms, contingency deadlines |

---

## Output Format

```json
{
  "document_classification_report": {
    "deal_name": "{property name or address}",
    "processed_at": "{date}",
    "documents_provided": [
      {
        "filename": "{name}",
        "file_type": "PDF / Excel / Word / Image",
        "classified_as": "{document type}",
        "classification_confidence": "{X}%",
        "fields_extracted": "{N}",
        "notes": "{any issues or ambiguities}"
      }
    ],
    "extracted_data": {
      "property": { "..." : "..." },
      "financials": { "...": "..." },
      "unitMix": [ "..." ],
      "seller": { "...": "..." },
      "timeline": { "...": "..." }
    },
    "completeness": {
      "required_fields_present": "{N}/8",
      "important_fields_present": "{N}/6",
      "optional_fields_present": "{N}/15"
    },
    "conflicts": [
      {
        "field": "{field name}",
        "conflict": "{Document A says X, Document B says Y}",
        "recommended_resolution": "{which source to trust and why}"
      }
    ],
    "missing_documents": [
      {
        "document_type": "{type}",
        "importance": "required / important / optional",
        "impact": "{what analysis this blocks}"
      }
    ],
    "unclassified_documents": [
      {
        "filename": "{name}",
        "issue": "{why it could not be classified}",
        "action_needed": "User confirmation required"
      }
    ],
    "ready_for_analysis": "YES / NO / PARTIAL",
    "ready_for_analysis_notes": "{what is and is not ready}"
  }
}
```

---

## Quality Checks

Before finalizing output:

1. **Every document accounted for** — Each document provided appears in the output with a classification or an unclassified flag
2. **No conflicting data left unresolved** — Every conflict is flagged with a recommended resolution
3. **Required fields verified** — Confirm address, total units, and asking price are either populated or flagged as missing
4. **Cross-document consistency** — Unit counts, NOI, and occupancy figures are consistent across documents or conflicts are noted
5. **Missing document list complete** — Flag all standard CRE documents not provided, with their importance level

---

## When Data is Missing

- **Unreadable document**: Flag as a data gap, note which fields could not be extracted, continue with other documents
- **Ambiguous document type**: Describe the document's contents to the user and ask for confirmation of document type before extracting
- **Missing critical data** (address, units, price): Flag prominently — note that underwriting cannot proceed without these fields and request manual input
- **Conflicting data**: Do not silently pick one source over another — always surface the conflict and recommend a resolution based on which source is more authoritative (e.g., rent roll is more authoritative than OM for occupancy figures; OM is more authoritative for asking price)

---

## Confidence Scoring

Assign a confidence level to each document's classification and extraction:

| Level | Criteria |
|-------|----------|
| **HIGH (90%+)** | Filename clearly matches, content confirms type, all expected columns/sections present |
| **MEDIUM (70-89%)** | Content confirms type but some expected fields are missing or ambiguous |
| **LOW (<70%)** | Document type inferred from partial content; user confirmation recommended |

---

## Related Knowledge Bases

For deeper analysis, pair this skill with the specialist parsing skills for each document type:
- **Offering Memo Parser** skill — for detailed extraction from marketing materials
- **Rent Roll Parser** skill — for unit-level occupancy and rent data extraction
- **T12 Financials Parser** skill — for revenue, expense, and NOI extraction from operating statements
- **Multifamily Benchmarks** knowledge base — for validating extracted metrics against typical market ranges

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
