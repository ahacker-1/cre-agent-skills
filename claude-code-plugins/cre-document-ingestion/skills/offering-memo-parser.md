---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Offering Memo Parser

Extract property characteristics, deal terms, financial highlights, and seller information from an Offering Memorandum (OM), marketing brochure, or property flyer.

---

## When to Use This Skill

Use this skill when you have an offering memorandum, marketing package, or property flyer for a commercial real estate deal and need to extract structured data from it. It handles PDF marketing documents, PowerPoint decks, Word documents, and property flyers (images). Use it at the beginning of deal evaluation to get the key facts out of the OM before underwriting across multifamily, industrial, and other CRE sectors.

---

## What You'll Need to Provide

- The offering memorandum, marketing brochure, or property flyer — as a PDF, PowerPoint, Word document, or image
- If the document is an image or scanned PDF, note that OCR quality will affect confidence
- Optionally, tell the parser if there is specific data you need prioritized (e.g., "I especially need the unit mix and asking price")

---

## Mission

Parse Offering Memorandums (OMs), marketing brochures, and property flyers to extract property characteristics, asking price, and seller information.

---

## Input Formats

- PDF marketing documents
- PowerPoint presentations
- Word documents
- Property flyers (images)

---

## Strategy

### Step 1: Identify Document Structure

Scan the document for standard OM section headers:
- Investment Summary / Executive Summary
- Property Overview / Property Description
- Location Overview / Market Overview
- Financial Summary / Financial Highlights
- Unit Mix / Floor Plans
- Offering Terms / Pricing Guidance
- Contact Information / Broker Information

### Step 2: Extract Property Identification

```json
{
  "property": {
    "name": "Parkview Apartments",
    "address": "4200 Parkview Drive",
    "city": "Austin",
    "state": "TX",
    "zip": "78745",
    "county": "Travis",
    "submarket": "South Austin",
    "msa": "Austin-Round Rock-San Marcos"
  }
}
```

### Step 3: Extract Physical Characteristics

```json
{
  "physical": {
    "propertyType": "multifamily | industrial | office | retail | mixed-use | unknown",
    "propertyClass": "B",
    "totalUnits": 200,
    "totalSqFt": 180000,
    "avgUnitSqFt": 900,
    "yearBuilt": 1998,
    "yearRenovated": null,
    "stories": 3,
    "buildings": 8,
    "construction": "wood-frame",
    "roofType": "composition shingle",
    "hvac": "individual PTAC",
    "parking": {
      "type": "surface",
      "spaces": 320,
      "ratio": 1.6,
      "covered": 80,
      "garages": 0
    },
    "lotSize": {
      "acres": 12.5,
      "sqft": 544500
    }
  }
}
```

### Step 4: Extract Amenities

```json
{
  "amenities": {
    "community": [
      "swimming pool",
      "fitness center",
      "clubhouse",
      "business center",
      "dog park",
      "playground",
      "laundry facility",
      "package lockers",
      "BBQ/picnic area"
    ],
    "unit": [
      "washer/dryer connections",
      "ceiling fans",
      "walk-in closets",
      "patio/balcony",
      "dishwasher",
      "disposal"
    ]
  }
}
```

### Step 5: Extract Unit Mix

```json
{
  "unitMix": [
    {
      "type": "1BR/1BA",
      "count": 80,
      "avgSqFt": 725,
      "rentRange": "$1,200 - $1,400"
    },
    {
      "type": "2BR/1BA",
      "count": 40,
      "avgSqFt": 900,
      "rentRange": "$1,400 - $1,650"
    },
    {
      "type": "2BR/2BA",
      "count": 60,
      "avgSqFt": 1050,
      "rentRange": "$1,600 - $1,850"
    },
    {
      "type": "3BR/2BA",
      "count": 20,
      "avgSqFt": 1200,
      "rentRange": "$1,900 - $2,200"
    }
  ]
}
```

### Step 6: Extract Financial Highlights

```json
{
  "financials": {
    "askingPrice": 32000000,
    "pricePerUnit": 160000,
    "pricePerSqFt": 178,
    "currentNOI": 1920000,
    "proFormaNOI": 2240000,
    "goingInCapRate": 0.06,
    "proFormaCapRate": 0.07,
    "currentOccupancy": 0.93,
    "marketOccupancy": 0.95,
    "avgInPlaceRent": 1465,
    "avgMarketRent": 1610,
    "lossToLease": 0.09
  }
}
```

### Step 7: Extract Investment Thesis

```json
{
  "investmentHighlights": [
    "Value-add opportunity with below-market rents",
    "Strong submarket fundamentals",
    "Units not renovated since 2010",
    "Rent premium potential of $200-300/unit"
  ],
  "valueAddOpportunity": {
    "renovationScope": "interior upgrades",
    "estimatedCost": 2000000,
    "costPerUnit": 10000,
    "expectedRentPremium": 250,
    "components": [
      "flooring",
      "countertops",
      "fixtures",
      "appliances",
      "lighting"
    ]
  }
}
```

### Step 8: Extract Seller and Broker Information

```json
{
  "seller": {
    "name": "Parkview Holdings LLC",
    "entityType": "Texas LLC",
    "motivation": ["portfolio rebalancing", "capital recycling"],
    "ownershipDuration": "8 years"
  },
  "broker": {
    "name": "Jane Smith",
    "firm": "Apex Capital Markets",
    "phone": "512-555-1234",
    "email": "jane.smith@example.com",
    "coBroker": null
  }
}
```

### Step 9: Extract Offering Timeline

```json
{
  "timeline": {
    "callForOffers": "2026-01-10",
    "bestAndFinal": "2026-01-20",
    "sellerSelection": "2026-01-25",
    "dueDiligencePeriod": 30,
    "closingTarget": "2026-03-31",
    "guidancePrice": "Low $30M range"
  }
}
```

---

## Extraction Techniques

### PDF Text Extraction
1. Extract all text while preserving structure
2. Identify section headers (Investment Summary, Property Overview, etc.)
3. Extract tables as structured data
4. Handle multi-column layouts

### Key Phrase Recognition

| Data Point | Look For |
|------------|----------|
| Asking Price | "Asking Price", "Guidance", "Price", "$XX,XXX,XXX" |
| Units | "XX Units", "XX-Unit", "Total Units" |
| Year Built | "Built in XXXX", "Year Built", "Vintage" |
| Occupancy | "XX% Occupied", "Occupancy", "XX% Leased" |
| Cap Rate | "X.X% Cap", "Going-In Cap", "Cap Rate" |
| Price/Unit | "$XXX,XXX/Unit", "Per Unit", "Per Door" |

### Image Analysis (for property photos)
- Exterior shots: building style, condition, landscaping
- Amenity shots: pool, fitness, clubhouse quality
- Unit photos: finishes, appliances, condition
- Aerial: site layout, parking, surrounding area

---

## Output Format

Return structured JSON using this schema:

```json
{
  "source": {
    "file": "parkview-om.pdf",
    "pages": 45,
    "extractedAt": "2026-02-01T12:00:00Z",
    "confidence": 0.88
  },
  "property": { "...": "..." },
  "physical": { "...": "..." },
  "amenities": { "...": "..." },
  "unitMix": [ "..." ],
  "financials": { "...": "..." },
  "investmentHighlights": [ "..." ],
  "seller": { "...": "..." },
  "broker": { "...": "..." },
  "timeline": { "...": "..." },
  "photos": {
    "exterior": 5,
    "amenities": 8,
    "units": 12,
    "aerial": 2
  },
  "warnings": [],
  "dataGaps": []
}
```

---

## Quality Checks

Run these validation checks on all extracted data before finalizing:

1. **Unit math**: Sum of unit mix counts = total units stated in the OM
2. **Price math**: Price/unit × total units ≈ asking price (within 1-2%)
3. **Cap rate math**: Current NOI ÷ asking price ≈ stated going-in cap rate (within 0.1%)
4. **Occupancy range**: Should be 80–100% for a marketed property; flag if below 80%
5. **Year built**: Should be a plausible year (1900–current year)
6. **Pro forma vs. actual clearly separated**: Never mix current and projected numbers in the same field

---

## When Data is Missing

### Ranges Instead of Specifics
OMs often show "200–210 units" or "$30–32M":
- Use the midpoint as the primary value, or the conservative end for underwriting
- Flag the field as an estimate in `warnings`

### Pro Forma Emphasized Over Actual
OMs emphasize pro forma figures over current performance:
- Extract both clearly, labeled as `current` and `proForma`
- Never use pro forma figures as if they were current actuals
- Flag whenever a stated cap rate or NOI is based on pro forma rather than T12

### Missing Broker Info
- Check the cover page, last page, and contact section
- If not found, leave blank and flag as a data gap

### Missing Financial Details
- If NOI is not stated, note that the OM is marketing-focused and recommend obtaining the T12 separately
- If cap rate is stated but NOI is not, back-calculate: `NOI = cap_rate × asking_price` and flag as derived

---

## Confidence Scoring

| Level | Criteria |
|-------|----------|
| **HIGH (0.85+)** | All key fields extracted directly from document; no ambiguity |
| **MEDIUM (0.70–0.84)** | Most fields extracted; some values inferred or derived from ranges |
| **LOW (<0.70)** | Key fields missing or heavily inferred; recommend obtaining additional documents |

---

## Related Knowledge Bases

For deeper analysis, pair this skill with:
- **Rent Roll Parser** skill — to cross-validate unit mix and occupancy figures against the actual rent roll
- **T12 Financials Parser** skill — to cross-validate OM financial highlights against the actual operating statement
- **Multifamily Benchmarks** knowledge base — to validate whether OM-stated metrics (cap rate, price/unit, expense ratio) are consistent with market norms
- **Underwriting Calculations** knowledge base — for running your own cap rate, NOI, and return calculations independently of the broker's presentation

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
