# How to Use CRE Agent Skills

This guide covers how to load these skill files into different AI platforms.

---

## Claude (Anthropic)

### Claude Projects (Recommended)

1. Open [claude.ai](https://claude.ai) and create a new Project
2. Click "Add knowledge" in the Project settings
3. Upload the `.md` skill file(s) you want to use
4. Optionally upload the recommended knowledge base files listed in the skill's "Related Knowledge Bases" section
5. Start a conversation in the project — Claude will automatically reference the loaded skills

**Tip:** Name your project by deal or task (e.g., "Parkview Apartments DD") and load the relevant subset of skills for that workflow.

### Claude Code (CLI)

If you're using Claude Code, you can reference skill files directly:

```bash
# Load a skill as context
claude "Using the skill in skills/due-diligence/rent-roll-analyst.md, analyze this rent roll: [data]"
```

Or add frequently-used skills to your CLAUDE.md file for automatic loading.

### Claude Code Plugins

The repo still works well with individual skill files, and Claude Code now has additional packaged options on top of the original multifamily department plugins:

- original multifamily department plugins
- plus the new `/cre-industrial` plugin added in v1.1.0
- plus the new `/cre-brokerage` plugin added in v1.2.0

PowerShell example for the new Industrial v1 plugin:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-industrial "$HOME\.claude\skills\"
```

Bash example for the new Industrial v1 plugin:

```bash
git clone https://github.com/ahacker-1/cre-agent-skills.git
cd cre-agent-skills
mkdir -p ~/.claude/skills
cp -r ./claude-code-plugins/cre-industrial ~/.claude/skills/
```

The original multifamily department plugins remain available exactly as before.

Brokerage v1 install example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-brokerage "$HOME\.claude\skills\"
```

---

## ChatGPT (OpenAI)

### Custom GPT

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the "Instructions" field, paste the full content of the skill file
3. For knowledge bases, upload them as files in the GPT's "Knowledge" section
4. Save and use the GPT for that specific analysis task

### Conversation-Level

1. Start a new conversation
2. Paste the skill content as your first message: "Use the following skill instructions for our conversation: [paste skill content]"
3. Follow up with your analysis request and data

---

## Cursor / Windsurf / AI Code Editors

### As Rules Files

1. Copy the `.md` skill file into your project's rules directory (e.g., `.cursor/rules/` or `.windsurfrules/`)
2. The AI assistant will automatically reference the skill when relevant

### As Context Files

1. Open the skill file in your editor
2. Reference it in your prompt: "Following the instructions in rent-roll-analyst.md, analyze this data..."

---

## Any LLM (API Usage)

Include the skill content in your system prompt:

```python
system_prompt = open("skills/due-diligence/rent-roll-analyst.md").read()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    system=system_prompt,
    messages=[
        {"role": "user", "content": "Analyze this rent roll: [data]"}
    ]
)
```

For richer analysis, concatenate the skill with its recommended knowledge bases:

```python
skill = open("skills/due-diligence/rent-roll-analyst.md").read()
knowledge = open("knowledge/multifamily-benchmarks.md").read()

system_prompt = f"{skill}\n\n---\n\nReference Knowledge:\n{knowledge}"
```

---

## Recommended Skill Combinations

Different tasks benefit from loading multiple skills together. Here are common combinations:

### Full Due Diligence Review
Load all 7 due diligence skills + Risk Scoring Framework + Multifamily Benchmarks

### Underwriting Package
- Financial Model Builder + Scenario Analyst + IC Memo Writer
- Knowledge: Underwriting Calculations + Multifamily Benchmarks

### Debt Sourcing
- Lender Outreach + Quote Comparator + Term Sheet Builder
- Knowledge: Lender Criteria + Underwriting Calculations

### Legal Review
- PSA Reviewer + Title & Survey Reviewer + Estoppel Tracker
- Knowledge: Legal Checklist

### Document Processing
- Document Classifier + Rent Roll Parser + Financials Parser + Offering Memo Parser
- These work well as a pipeline: classify first, then parse each document type

### Industrial v1 Acquisitions Core
- Industrial Market Study + Industrial Lease Roster Analyst + Industrial Lease Abstract Reviewer + Industrial Physical Inspection + Industrial Underwriting Model Builder + Industrial Financing Fit + Industrial IC Memo Writer
- Knowledge: Industrial Benchmarks + Industrial Lease Structures + Industrial Lender Criteria
- Research: use `research/industrial/` when you want the model to see the source-backed benchmark rationale behind the new industrial defaults

### Brokerage Investment Sales v1
- Assignment Intake Manager + Broker Opinion of Value Builder + Listing Proposal Builder + Offering Memorandum and Teaser Writer + Buyer Process and Data Room Manager + Call for Offers and Bid Leveling Analyst + Deal Term Negotiation Brief Builder + PSA to Close Transaction Coordinator
- Knowledge: Brokerage Investment Sales Process + Broker Opinion of Value Guidance + Marketing Confidentiality and Buyer Process + Offer Negotiation and Closing Playbook
- Research: use `research/brokerage/` when you want the model to see the source-backed brokerage process and valuation guidance behind the new pack

### Asset Management v1
- Annual Operating Budget Builder + Monthly Variance Analyst + Rent Collection & Delinquency Manager + Renewal Decision Analyst + Lease-Up & Concessions Analyst + CapEx & Value-Add Execution Tracker + NOI Improvement Analyst + Hold/Sell/Refi Analyst + Quarterly Asset Review Writer
- Knowledge: Asset Management Benchmarks + Asset Management Reporting Standards + Renewal Economics + Underwriting Calculations + Multifamily Benchmarks
- Research: use `research/asset-management/` when you want the model to see the source-backed benchmarks, variance-classification rules, A/R aging conventions, and institutional reporting standards behind the pack
- Note: this pack adopts a Fannie Form 4660 NOI / NCF split — NOI excludes Replacement Reserves; NCF = NOI − Replacement Reserves. See `research/asset-management/_taxonomy-seed.md` for full taxonomy.

### Post-Acquisition Budget-to-QAR Combo
- Annual Operating Budget Builder → Monthly Variance Analyst → Quarterly Asset Review Writer
- Knowledge: Asset Management Benchmarks + Asset Management Reporting Standards
- Gets an operator from day-1 stabilization hand-off through monthly operations into a publication-ready quarterly LP memo

### Quick Deal Screening
- Rent Roll Analyst + OpEx Analyst + Financial Model Builder
- Knowledge: Underwriting Calculations + Multifamily Benchmarks
- Gets you to a preliminary NOI and cap rate assessment fast

---

## Tips for Best Results

1. **Provide structured data when possible.** CSV or tabular data produces better analysis than unstructured text.

2. **Include the property address.** Many skills use web research to pull market comps, submarket data, and benchmarks. The more specific the location, the better.

3. **Load knowledge bases for deeper analysis.** Skills work on their own, but pairing them with the recommended knowledge files gives the AI access to formulas, benchmarks, and criteria it can reference during analysis.

4. **Trust the output format.** Each skill defines a structured output (JSON or Markdown). Let the AI follow that format — it makes results consistent and comparable across deals.

5. **Review the confidence scoring.** Every skill rates its own confidence (HIGH/MEDIUM/LOW) and flags data gaps. Pay attention to these — they tell you where the analysis is weakest.

6. **Iterate on data gaps.** If the skill flags missing data, provide additional information and re-run that section. The skills are designed to handle partial data gracefully.

7. **For Industrial v1, pass building specs whenever you can.** Clear height, dock count, truck court depth, trailer parking, office finish, and power materially affect the quality of the output.

8. **Treat research-backed benchmarks as directional, not universal.** The industrial research notes improve traceability, but local market conditions should still control real decisions.

9. **For Brokerage v1, separate business terms from legal terms.** The brokerage pack is designed for seller-side process control and negotiation support, not for replacing counsel.
