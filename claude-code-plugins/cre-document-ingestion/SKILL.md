---
name: cre-document-ingestion
description: "CRE Document Ingestion suite — 4 specialist skills for classifying and extracting structured data from deal documents including rent rolls, T-12 financials, and offering memoranda."
argument-hint: "[document-or-task-description]"
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# CRE Document Ingestion Suite

You have access to 4 specialist document processing skills for commercial real estate deal packages.

## Available Skills

| Skill | File | Use When |
|-------|------|----------|
| Document Classifier | `skills/document-classifier.md` | User provides one or more deal documents and needs them identified by type (rent roll, T-12, offering memo, lease, survey, etc.) |
| Rent Roll Parser | `skills/rent-roll-parser.md` | User provides a rent roll file and needs structured data extracted — unit numbers, tenants, lease dates, rents, deposits, status |
| Financials Parser | `skills/financials-parser.md` | User provides a T-12 or operating statement and needs structured extraction — income lines, expense categories, monthly trends |
| Offering Memo Parser | `skills/offering-memo-parser.md` | User provides an offering memorandum and needs key data extracted — property details, financial projections, market data, investment highlights |

## How to Use

1. If the user provides documents without specifying what they are, start with the Document Classifier
2. Once document types are identified, load the appropriate parser skill
3. Follow the Strategy steps in the loaded skill exactly
4. Produce structured output in the format specified by the skill
5. Run Quality Checks before delivering results

**Recommended workflow for a full deal package:**
1. `Read skills/document-classifier.md` → classify all documents
2. For each rent roll: `Read skills/rent-roll-parser.md` → extract
3. For each T-12/financial: `Read skills/financials-parser.md` → extract
4. For each offering memo: `Read skills/offering-memo-parser.md` → extract

If the user says "$ARGUMENTS", use that to determine which skill to load.

## Quick Reference

**Document Classifier** — Identifies: rent rolls, T-12/T-3 operating statements, offering memoranda, leases, title commitments, surveys, Phase I ESAs, appraisals, insurance certificates, tax returns, entity documents. Outputs: document type, confidence level, extractable data fields.

**Rent Roll Parser** — Extracts: unit number, unit type, square footage, tenant name, lease start/end, monthly rent, security deposit, unit status, move-in date, concessions. Validates: unit count completeness, rent reasonableness, date consistency.

**Financials Parser** — Extracts: income line items (rental income, vacancy loss, other income), expense categories (taxes, insurance, utilities, R&M, management, payroll, turnover, admin), monthly and annual totals. Calculates: per-unit metrics, expense ratios, year-over-year trends.

**Offering Memo Parser** — Extracts: property name/address, unit count/mix, year built, lot size, asking price, in-place NOI, pro forma NOI, cap rate, occupancy, market highlights, seller's financial projections, comparable sales, rent comps.

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
