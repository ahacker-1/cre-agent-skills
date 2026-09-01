---
license: Apache-2.0
metadata:
  author: "Avi Hacker, J.D."
  organization: "The AI Consulting Network"
  homepage: https://www.theaiconsultingnetwork.com
  source: https://github.com/ahacker-1/cre-agent-skills
  copyright: "Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network"
---

# Recap IC Memo Writer

Write an investment committee memo for refinance, extension, workout, rescue capital, recapitalization, sale, or hold decision.

---

## When to Use This Skill

Use this skill after running the capital markets diagnostics, refinance gap, rescue capital, term sheet, servicing, or lender package skills and needing a decision-ready memo.

---

## What You'll Need to Provide

- Outputs from relevant capital markets skills
- Property overview and current performance
- Existing debt, maturity, payoff, and default status
- Refinance gap and capital alternatives
- Business plan, risks, and exit strategy
- Sponsor objectives and decision deadline

---

## Mission

Synthesize the facts into a clear IC recommendation: refinance, extend, modify, recapitalize, inject equity, sell, pursue discounted payoff, or decline further capital.

---

## Strategy

### Step 1: Define the Decision

State the exact IC question:

- approve refinance
- approve paydown
- approve rescue capital
- approve extension/workout proposal
- approve sale process
- decline additional capital

### Step 2: Summarize Current Position

Cover:

- asset status
- loan status
- maturity timeline
- operating performance
- valuation
- sponsor liquidity
- default or servicing risk

### Step 3: Present Alternatives

Compare:

- refinance
- extension
- workout/modification
- sponsor equity
- preferred equity or mezzanine
- common JV equity
- sale
- note purchase or discounted payoff

### Step 4: Analyze Economics and Risk

Include:

- proceeds gap
- required capital
- expected return or loss avoidance
- control and dilution
- downside case
- timing risk
- legal/tax/counsel issues

### Step 5: Make Recommendation

Give:

- recommended path
- why alternatives were rejected
- required approvals
- next 30/60/90 day actions
- confidence level

---

## Output Format

```markdown
# Recap / Maturity IC Memo
## Property:
## Decision:
## Recommendation: APPROVE | APPROVE WITH CONDITIONS | DEFER | REJECT

### Executive Summary
- ...

### Current Position
| Item | Detail |
|---|---|

### Capital Need and Gap
| Item | Amount |
|---|---:|

### Alternatives Reviewed
| Alternative | Economics | Execution Risk | Control / Dilution | Verdict |
|---|---|---|---|---|

### Recommended Path
- ...

### Key Risks
- ...

### Conditions to Approval
- ...

### 30 / 60 / 90 Day Plan
| Window | Action | Owner |
|---|---|---|

### Data Gaps
- ...

### Confidence Level
HIGH | MEDIUM | LOW
```

---

## Quality Checks

- States the exact IC decision
- Compares alternatives rather than advocating one path blindly
- Quantifies gap and required capital
- Names execution, consent, and control risks
- Includes conditions to approval
- Provides next actions with timing

---

## Red Flags & Dealbreakers

- Recommendation depends on unconfirmed lender consent
- Required capital exceeds value preserved
- Rescue capital structure creates immediate control-loss risk
- Sale is rejected without a refinance or recap path
- Tax, guaranty, or legal risk is material and unreviewed
- Memo hides uncertainty or missing data

---

## When Data is Missing

- If alternatives are incomplete, state what can and cannot be decided
- If economics are missing, write a preliminary screening memo only
- If legal/tax issues are unresolved, make counsel review a condition
- If value is unclear, include valuation sensitivity as a gating item

---

## Confidence Scoring

| Level | Criteria |
|---|---|
| HIGH | Prior skill outputs, financials, loan data, term sheets, value support, and sponsor objectives are available |
| MEDIUM | Main facts are available but one or more alternatives lack full terms |
| LOW | Memo relies on high-level narrative without validated financials or term sheets |

---

## Related Knowledge Bases

- [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md)
- [Workout and Extension Structures](knowledge/workout-and-extension-structures.md)
- [Rescue Capital and Preferred Equity](knowledge/rescue-capital-and-pref-equity.md)
- [CMBS Servicing and Default Playbook](knowledge/cmbs-servicing-and-default-playbook.md)
- [Risk Scoring Framework](knowledge/risk-scoring.md)

## Research Basis

- [Recap IC Memo Writer Research](research/capital-markets/recap-ic-memo-writer-research.md)

---

## Attribution

Built and maintained by [The AI Consulting Network](https://www.theaiconsultingnetwork.com/?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills), the commercial real estate AI consulting practice of Avi Hacker, J.D., and part of [CRE Agent Skills](https://github.com/ahacker-1/cre-agent-skills), an open-source library of AI skills for commercial real estate.

If this skill saved you time and you want systems like it built inside your firm, [reach out](https://www.theaiconsultingnetwork.com/contact?utm_source=github&utm_medium=skill-file&utm_campaign=cre-agent-skills). We would love to work with you.

Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network. Licensed under the [Apache License 2.0](https://github.com/ahacker-1/cre-agent-skills/blob/main/LICENSE). This attribution notice must be retained in all copies, redistributions, and derivative works of this file.
