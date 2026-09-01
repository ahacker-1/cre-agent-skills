---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Industrial Market Study

Research and evaluate a U.S. industrial submarket - including demand, supply, competitive inventory, logistics positioning, and subtype-specific fit - for an acquisition decision.

---

## When to Use This Skill

Use this skill when you need to understand whether a U.S. industrial asset is supported by its market. It is most useful during acquisitions or recapitalization screening when you want to know how the subject competes inside its actual submarket and user niche, rather than relying on generic industrial sentiment.

---

## What You'll Need to Provide

- Property name and address
- Industrial subtype if known: bulk distribution, shallow-bay, flex industrial, light industrial, single-tenant, or infill logistics
- Rent roll or current occupancy summary if available
- Building specs if available: square footage, clear height, loading configuration, truck court depth, trailer parking, office finish ratio, power, and year built
- Asking rents or current in-place rents if available
- Hold thesis or acquisition angle if known

---

## Mission

Build a market view for the subject industrial asset. Analyze local supply and demand, identify the real competing set, test whether the building is functionally competitive, and summarize the market risks and advantages relevant to underwriting and lease rollover.

---

## Strategy

### Step 1: Classify the Asset

- Determine the industrial subtype before doing comp work
- Identify whether the asset behaves like:
  - bulk distribution
  - shallow-bay
  - flex industrial
  - light industrial
  - single-tenant net-leased
  - last-mile / infill logistics
- Use subtype to decide what market data matters most

### Step 2: Define the Market and Comp Set

- Identify the primary submarket, not just the MSA
- Build a competitive set of similar industrial inventory by:
  - subtype
  - building quality
  - size band
  - location and logistics access
- Prefer local market reports and real recent listings / leasing activity over national averages

### Step 3: Analyze Demand

Research:

- trailing 12-month net absorption
- leasing activity
- recent large leases
- active tenant categories
- labor and logistics drivers
- cross-border, port, rail, or intermodal relevance where applicable

### Step 4: Analyze Supply

Research:

- vacancy
- construction pipeline
- recent deliveries
- share of competing newer product
- whether the subject is competing against modern space or mostly legacy space

### Step 5: Evaluate Functional Competitiveness

Compare the subject against current competing stock on:

- clear height
- dock and drive-in loading
- truck court depth
- trailer parking
- power
- office finish ratio
- site circulation
- age and apparent obsolescence risk

### Step 6: Market Rent and Release Depth

- Estimate current market rent and effective rent directionally
- Identify whether the submarket supports:
  - straightforward releasing
  - re-tenanting with CapEx
  - only niche / specialized release demand
- State whether the subject appears above, at, or below current competitive positioning

### Step 7: Synthesize the Market View

Conclude:

- market strength
- subtype fit
- subject competitiveness
- release depth
- major risks to underwriting

---

## Output Format

```markdown
# Industrial Market Study: {Property Name}
## Date: {YYYY-MM-DD}
## Status: COMPLETE | PARTIAL | FAILED

### Asset Classification
- Subtype:
- Market Position:
- Competitive Set Summary:

### Market Demand
- Net absorption:
- Leasing activity:
- Active tenant categories:
- Logistics and labor drivers:

### Market Supply
- Vacancy:
- New supply / pipeline:
- Competitive inventory quality:

### Functional Competitiveness
- Clear height:
- Loading:
- Trailer parking and circulation:
- Power:
- Office finish ratio:
- Overall competitiveness:

### Rent and Release Outlook
- Estimated market rent:
- Effective rent direction:
- Release depth:
- Re-tenanting risk:

### Key Risks
- ...

### Market Verdict
STRONG | MIXED | WEAK

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- The asset subtype is explicitly stated
- The comp set matches the subtype and size band
- Market commentary distinguishes the submarket from the broader metro
- Functional competitiveness is compared against likely competing stock, not generic national averages
- The conclusion states whether market strength actually supports the subject building

---

## When Data is Missing

- If local market reports are limited, use multiple institutional sources and explain the gap
- If building specs are incomplete, note which competitiveness conclusions are lower confidence
- If subtype is ambiguous, state the leading classification and the most plausible alternative

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Local market reports, recent comps, and building specs are all available |
| MEDIUM | Market data is solid but building specs or subtype clarity are incomplete |
| LOW | Heavy reliance on high-level metro data or incomplete building information |

---

## Related Knowledge Bases

- [Industrial Benchmarks](knowledge/industrial-benchmarks.md)
- [Industrial Lease Structures](knowledge/industrial-lease-structures.md)

## Research Basis

- [Industrial Market Study Research](research/industrial/industrial-market-study-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
