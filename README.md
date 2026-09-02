# CRE Agent Skills — AI-Powered Commercial Real Estate Analysis

**90 CRE skills. No orchestrator required.**

Most CRE operators don't need another AI platform.

They need one sharp tool for the thing on their desk right now. The rent roll they're cleaning tonight. The IC memo due Thursday. The lender comparison they've been avoiding for a week. The quarterly LP report due Friday.

So I took my own orchestrator apart and gave it to them.

A while back I shipped a full multi-agent [CRE Acquisition Orchestrator](https://github.com/ahacker-1/cre-acquisition-orchestrator) — 31 skills wired together across due diligence, underwriting, financing, legal, closing, and document ingestion. Some operators loved it. They wanted the full stack running like a junior analyst team that never sleeps.

But most people I talked to didn't want that.

Not yet.

They had a specific piece of work already in front of them. They didn't want to adopt a whole system. They wanted one good tool for the one thing they were doing right now.

The all-in-one AI platform pitch is a bad fit for how CRE work actually moves. Deals don't wait for you to adopt a pipeline. They land on your desk in pieces.

So I pulled every skill out.

Made each one a clean, standalone file you drop into your own setup — Claude Code, Claude Projects, ChatGPT, Cursor, or any LLM-powered tool.

Then I kept going.

Added a full **Industrial** pack.

Added a **Brokerage Investment Sales** pack.

Added an **Asset Management** pack for post-acquisition operations — budgets, variance, renewals, capex execution, NOI improvement, hold/sell/refi decisions, and quarterly LP reviews.

Added an **Office** pack for lease-driven office analysis - flight-to-quality, stacking plans, lease abstracts, rollover exposure, TI/LC-heavy underwriting, tenant credit, financing fit, and IC memo writing.

Added a **Capital Markets** pack for the messy refinance and maturity work everyone is dealing with now - debt maturity diagnostics, proceeds gaps, extensions, workouts, rescue capital, CMBS special servicing readiness, lender updates, and recap IC memos.

Added a **Retail** pack, because retail is lease-driven and sales-driven at the same time - trade area demand, tenant sales and occupancy cost, anchor health, co-tenancy and exclusives, CAM recovery structure, lease-by-lease underwriting, financing fit, and IC memos.

Added a **Lender / Credit** pack. Every other pack in this repo sits on the borrower, owner, or seller side of the table. This one sits on the other side - screening and sizing loan requests, analyzing sponsors and guarantors, reviewing appraisals, writing credit memos, monitoring covenants and watchlists, running annual reviews and risk ratings, working out problem loans, and stress-testing a CRE book.

Added a **Development and Construction** pack for ground-up and heavy redevelopment - site and entitlement screening, budgets and yield on cost, construction loan sizing and structure, draw and cost-to-complete review, GC contracts and change orders, schedule and delivery risk, lease-up and stabilization pro formas, and development IC memos.

Built knowledge bases — real references, not placeholders. Every benchmark traces to a cited source.

Grab it. Apache 2.0. No API keys. No signup. Clone, star, come back.

Here's where I want to land.

I want this to be the most helpful AI resource in commercial real estate. Period. Not a product I sell. A growing set of building blocks you pick from. Scaffolding for the work you're already trying to think through.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-90-green.svg)](#skill-index)
[![Knowledge Bases](https://img.shields.io/badge/Knowledge_Bases-35-blue.svg)](#knowledge-bases)
[![Research Notes](https://img.shields.io/badge/Research_Notes-93-orange.svg)](#new-in-v160)
[![Claude Code Plugins](https://img.shields.io/badge/Claude_Code_Plugins-14-purple.svg)](#claude-code-plugins-recommended)
[![No API Keys](https://img.shields.io/badge/API_Keys-None_Required-brightgreen.svg)](#quick-start)

---

| | | | |
|---|---|---|---|
| **90** AI Skills | **35** Knowledge Bases | **14** Claude Code Plugins | **0** Dependencies |
| **8** Retail v1 | **8** Lender / Credit v1 | **8** Development and Construction v1 | **8** Capital Markets v1 |
| **8** Office v1 | **9** Asset Management v1 | **8** Brokerage v1 | **8** Industrial v1 |

---

> **No API keys. No installation. No dependencies.** Each `.md` file works on its own.

> **Disclaimer:** These skill files are educational and informational resources, not production software for making investment decisions. The financial calculations, legal checklists, underwriting models, and analysis outputs are for reference and learning purposes only. Nothing in this repository constitutes financial, legal, investment, or tax advice. The authors and contributors are not liable for any decisions made based on information produced using these skills. Always consult qualified professionals — licensed attorneys, CPAs, commercial real estate brokers, and financial advisors — before making real estate investment decisions. These materials are provided "as is" without warranty of any kind. See [LICENSE](LICENSE) for full terms.

---

## New in v1.6.0

This release ships three packs at once - a retail sector pack, the repo's first lender-side pack, and a development and construction pack:

- **Retail v1** with 8 new U.S.-focused retail skills - market and trade area study, rent roll and tenant mix, lease abstract review, co-tenancy and anchor risk, CAM reconciliation and recovery, lease-by-lease underwriting, financing fit, and IC memo writing
- **Lender / Credit v1** with 8 new U.S.-focused credit-side skills - loan request screening and sizing, sponsor and guarantor analysis, appraisal and valuation review, credit memo writing, covenant compliance and watchlist monitoring, annual loan review and risk rating, problem loan and modification analysis, and CRE portfolio concentration and stress testing
- **Development and Construction v1** with 8 new U.S.-focused development skills - site and entitlement screening, development budget and yield on cost, construction loan sizing and structure, construction draw and cost-to-complete review, GC contract and change order review, schedule and delivery risk tracking, lease-up and stabilization pro forma, and development IC memo writing
- **12 new knowledge bases** - 4 retail, 4 lender / credit, and 4 development and construction
- **36 new companion research notes** under `research/retail/`, `research/lender-credit/`, and `research/development/`
- **3 new Claude Code plugins** - `/cre-retail`, `/cre-lender-credit`, and `/cre-development`
- **Cross-platform validation** with `scripts/validate_repo.py --strict`, a Python port of the existing PowerShell validator, plus a second CI job on Ubuntu
- **Additive release framing** on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, and Capital Markets v1

Retail v1 is lease-driven and sales-driven: tenant sales, occupancy cost, anchor health, co-tenancy, exclusives, and CAM recovery structure control value. Lender / Credit v1 is the credit-side mirror of everything else here, written for credit analysts, underwriters, portfolio managers, credit officers, loan review, and special assets. Development and Construction v1 covers U.S. ground-up and heavy redevelopment for developers, development managers, owner representatives, construction lenders, and equity partners.

---

## New in v1.5.0

This release adds a cross-property capital markets pack for the refinance, extension, workout, and recapitalization decisions cutting across every CRE asset type:

- **Capital Markets / Debt Maturity & Recap v1** with 8 new U.S.-focused skills - maturity diagnostics, refinance proceeds gaps, extension/workout strategy, rescue capital comparison, capital stack term sheet comparison, CMBS special servicing readiness, lender update packages, and recap IC memo writing
- **4 capital markets knowledge bases** covering debt sizing, workout structures, rescue capital / preferred equity, and CMBS servicing / default mechanics
- **12 capital markets companion research notes** under `research/capital-markets/`
- **`/cre-capital-markets` Claude Code plugin**
- **Additive release framing** on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, Asset Management v1, and Office v1

Capital Markets v1 is property-type-agnostic. It is designed for owners, brokers, lenders, asset managers, and advisors dealing with maturity walls, refinance gaps, lender updates, special servicing, and rescue-capital decisions.

---

## New in v1.4.0

This release adds a new office acquisition and recapitalization pack, plus validation tooling so the repo can keep scaling without silent drift:

- **Office v1** with 8 new U.S.-focused office skills - flight-to-quality market study, rent roll and stacking plan analysis, lease abstract review, rollover and occupancy-cost analysis, TI/LC underwriting, tenant credit, financing fit, and IC memo writing
- **4 office knowledge bases** covering office benchmarks, lease structures, TI/LC economics, and lender criteria
- **12 office companion research notes** under `research/office/`
- **`/cre-office` Claude Code plugin**
- **PowerShell validation tooling** with `.github/workflows/validate.yml` and `scripts/validate-repo.ps1 -Strict`
- **Additive release framing** on top of the original multifamily core, Industrial v1, Brokerage Investment Sales v1, and Asset Management v1

Office v1 is lease-driven and U.S.-focused. It is designed for acquisitions, refinancings, recapitalizations, lease-up, and hold/sell decisions in a selective office capital environment.

---

## New in v1.3.0

This release adds a new post-acquisition operational pack without changing the existing multifamily, industrial, or brokerage paths:

- **Asset Management v1** with 9 new post-acquisition operational skills — budgeting, variance, collections, renewals, lease-up, capex, NOI improvement, hold/sell/refi decisions, and quarterly asset review memo
- **`/cre-asset-management` Claude Code plugin**
- **Additive release framing** on top of the original multifamily core, Industrial v1, and Brokerage Investment Sales v1

Asset Management v1 is post-closing operational work for owner/operators running stabilized and transitional assets.

---

## New in v1.2.0

This release adds a new role-based pack without changing the existing multifamily or industrial paths:

- **Brokerage Investment Sales v1** with 8 new U.S.-focused seller-side brokerage skills
- **4 brokerage knowledge bases**
- **12 brokerage companion research notes**
- **`/cre-brokerage` Claude Code plugin**
- **Additive release framing** on top of the original multifamily-first repo and the prior Industrial v1 release

Brokerage v1 is seller-side, investment-sales-first, BOV-to-close, and transaction-only. It is designed to support brokers on active assignments, not general prospecting or CRM work.

---

## New in v1.1.0

This release adds to the original multifamily-first library without changing the existing multifamily paths:

- **Industrial v1** with 8 new U.S.-focused industrial acquisition skills
- **3 industrial knowledge bases**
- **11 industrial companion research notes**
- **`/cre-industrial` Claude Code plugin**
- **PowerShell install examples** for Windows-first users
- **Research-backed contribution standards** for future sector packs

The original multifamily core remains intact. Industrial v1 is the first additive sector expansion.

---

## Table of Contents

- [New in v1.6.0](#new-in-v160)
- [New in v1.5.0](#new-in-v150)
- [New in v1.4.0](#new-in-v140)
- [New in v1.3.0](#new-in-v130)
- [New in v1.2.0](#new-in-v120)
- [New in v1.1.0](#new-in-v110)
- [Quick Start](#quick-start)
- [Claude Code Plugins](#claude-code-plugins-recommended)
- [Installation Methods](#installation-methods)
- [Skill Index](#skill-index)
- [Knowledge Bases](#knowledge-bases)
- [How Skills Are Structured](#how-skills-are-structured)
- [Project Structure](#project-structure)
- [Example Usage](#example-usage)
- [Common Workflows](#common-workflows)
- [FAQ](#faq)
- [Want the Full Pipeline?](#want-the-full-pipeline)
- [Author](#author)
- [License](#license)

---

## Quick Start

### Option 1: Claude Code Plugin (Recommended)

If you use Claude Code, install a department plugin in one command:

```bash
# Clone the repo
git clone https://github.com/ahacker-1/cre-agent-skills.git

# Install the due diligence plugin (example)
cp -r cre-agent-skills/claude-code-plugins/cre-due-diligence ~/.claude/skills/

# Now use it in Claude Code
claude
> /cre-due-diligence Analyze the rent roll for 200 Park Avenue, Austin TX
```

See [Claude Code Plugins](#claude-code-plugins-recommended) below for the original department plugins plus the additive Industrial v1, Brokerage v1, Asset Management v1, Office v1, Capital Markets v1, Retail v1, Lender / Credit v1, and Development and Construction v1 packs.

#### Windows / PowerShell

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-industrial "$HOME\.claude\skills\"
```

Brokerage v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-brokerage "$HOME\.claude\skills\"
```

Office v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-office "$HOME\.claude\skills\"
```

Capital Markets v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-capital-markets "$HOME\.claude\skills\"
```

Retail v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-retail "$HOME\.claude\skills\"
```

Lender / Credit v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-lender-credit "$HOME\.claude\skills\"
```

Development and Construction v1 example:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\cre-development "$HOME\.claude\skills\"
```

### Option 2: Copy a Single Skill File

1. Browse the [Skill Index](#skill-index) below
2. Open the `.md` file for the task you need
3. Copy its content into Claude Projects, ChatGPT Custom Instructions, Cursor rules, or any LLM system prompt
4. Provide the inputs listed in "What You'll Need to Provide"
5. Get structured, expert-level analysis back

### Option 3: Point an AI Agent at This Repo

If you're using an AI coding agent (Claude Code, Cursor, Windsurf, etc.), you can point it at this repo and ask it to set things up for you:

```bash
git clone https://github.com/ahacker-1/cre-agent-skills.git
cd cre-agent-skills

# Then tell your AI agent:
# "Read the README.md and set up the CRE skills I need for due diligence and underwriting"
```

The repo is structured so an AI agent can read this README, understand the full skill catalog, and help you install exactly what you need. Every file is plain Markdown — no compilation, no build steps, no configuration files.

---

## Claude Code Plugins (Recommended)

The repo now includes the original six department plugins plus eight additive packs: Industrial v1, Brokerage Investment Sales v1, Asset Management v1, Office v1, Capital Markets v1, Retail v1, Lender / Credit v1, and Development and Construction v1. Each plugin includes a `SKILL.md` entry point that routes to the right specialist skill based on your request, plus all referenced knowledge base files bundled inside.

### Available Plugins

| Plugin | Slash Command | Skills Included | Knowledge Bases Included |
|--------|--------------|-----------------|--------------------------|
| **Due Diligence** | `/cre-due-diligence` | 7 skills (rent roll, OpEx, market, physical, environmental, title, tenant credit) | Underwriting Calc, Multifamily Benchmarks, Risk Scoring |
| **Underwriting** | `/cre-underwriting` | 3 skills (financial model, scenarios, IC memo) | Underwriting Calc, Multifamily Benchmarks |
| **Financing** | `/cre-financing` | 3 skills (lender outreach, quote comparator, term sheet) | Lender Criteria, Underwriting Calc |
| **Legal** | `/cre-legal` | 6 skills (PSA, title/survey, estoppels, loan docs, insurance, transfer docs) | Legal Checklist |
| **Closing** | `/cre-closing` | 2 skills (closing coordinator, funds flow) | Legal Checklist, Underwriting Calc |
| **Asset Management v1** | `/cre-asset-management` | 9 skills (budgeting, variance, collections, renewals, lease-up, capex, NOI improvement, hold/sell/refi, quarterly asset review memo) | Asset Management Benchmarks, Asset Management Reporting Standards, Renewal Economics |
| **Document Ingestion** | `/cre-document-ingestion` | 4 skills (classifier, rent roll parser, financials parser, OM parser) | None (self-contained) |
| **Industrial v1** | `/cre-industrial` | 8 skills (market study, lease roster, lease abstract, tenant credit, physical inspection, underwriting, financing fit, IC memo) | Industrial Benchmarks, Industrial Lease Structures, Industrial Lender Criteria |
| **Brokerage v1** | `/cre-brokerage` | 8 skills (assignment intake, BOV, listing proposal, OM / teaser, buyer process, bid leveling, negotiation brief, PSA-to-close coordination) | Brokerage Investment Sales Process, Broker Opinion of Value Guidance, Marketing Confidentiality and Buyer Process, Offer Negotiation and Closing Playbook |
| **Office v1** | `/cre-office` | 8 skills (market / flight-to-quality, rent roll / stacking plan, lease abstract, rollover / occupancy cost, TI/LC underwriting, tenant credit, financing fit, IC memo) | Office Benchmarks, Office Lease Structures, Office TI/LC Economics, Office Lender Criteria |
| **Capital Markets v1** | `/cre-capital-markets` | 8 skills (maturity diagnostic, refi gap, extension/workout, rescue capital, term sheet comparison, CMBS readiness, lender update, recap IC memo) | Capital Markets Benchmarks, Workout and Extension Structures, Rescue Capital and Preferred Equity, CMBS Servicing and Default Playbook |
| **Retail v1** | `/cre-retail` | 8 skills (market / trade area, rent roll and tenant mix, lease abstract, co-tenancy and anchor risk, CAM reconciliation, underwriting, financing fit, IC memo) | Retail Benchmarks, Retail Lease Structures, Retail Tenant Sales and Occupancy Cost, Retail Lender Criteria |
| **Lender / Credit v1** | `/cre-lender-credit` | 8 skills (loan screening and sizing, sponsor and guarantor, appraisal review, credit memo, covenant and watchlist monitoring, annual review and risk rating, problem loan and modification, portfolio concentration and stress test) | Lender Credit Policy Benchmarks, Regulatory Risk Rating and Classification, Credit Memo and Appraisal Review Standards, CRE Concentration and Stress Testing |
| **Development and Construction v1** | `/cre-development` | 8 skills (site and entitlement screen, budget and yield on cost, construction loan sizing, draw and cost-to-complete, GC contract and change order, schedule and delivery risk, lease-up pro forma, IC memo) | Development Benchmarks, Construction Lending Criteria, Construction Contracts and Draw Controls, Entitlement and Site Risk |

### How to Install

Each plugin is a self-contained directory inside `claude-code-plugins/`. Install the ones you need:

#### Method A: Personal Skills (Available in All Projects)

Copy plugins to your personal Claude Code skills directory:

```bash
# Clone the repo
git clone https://github.com/ahacker-1/cre-agent-skills.git
cd cre-agent-skills

# Install individual plugins
cp -r claude-code-plugins/cre-due-diligence ~/.claude/skills/
cp -r claude-code-plugins/cre-underwriting ~/.claude/skills/
cp -r claude-code-plugins/cre-financing ~/.claude/skills/
cp -r claude-code-plugins/cre-legal ~/.claude/skills/
cp -r claude-code-plugins/cre-closing ~/.claude/skills/
cp -r claude-code-plugins/cre-document-ingestion ~/.claude/skills/

# Or install ALL plugins at once
cp -r claude-code-plugins/* ~/.claude/skills/
```

PowerShell equivalent:

```powershell
git clone https://github.com/ahacker-1/cre-agent-skills.git
Set-Location .\cre-agent-skills

New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse .\claude-code-plugins\* "$HOME\.claude\skills\"
```

After installation, the plugins are available in every Claude Code session. Type `/cre-` and autocomplete will show all installed plugins.

#### Method B: Project-Level Skills (Available in One Project)

If you want skills scoped to a specific deal or project:

```bash
# Inside your project directory
mkdir -p .claude/skills

# Install only the plugins you need for this project
cp -r /path/to/cre-agent-skills/claude-code-plugins/cre-due-diligence .claude/skills/
cp -r /path/to/cre-agent-skills/claude-code-plugins/cre-underwriting .claude/skills/
```

PowerShell equivalent:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-industrial .\.claude\skills\
```

Brokerage v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-brokerage .\.claude\skills\
```

Office v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-office .\.claude\skills\
```

Capital Markets v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-capital-markets .\.claude\skills\
```

Retail v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-retail .\.claude\skills\
```

Lender / Credit v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-lender-credit .\.claude\skills\
```

Development and Construction v1 example:

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item -Recurse C:\path\to\cre-agent-skills\claude-code-plugins\cre-development .\.claude\skills\
```

Project-level skills take priority over personal skills with the same name. You can commit the `.claude/skills/` directory to git so your team shares the same skills.

#### Method C: Using `--add-dir` (No Installation)

Reference the plugins directory directly without copying:

```bash
# Clone once
git clone https://github.com/ahacker-1/cre-agent-skills.git

# Launch Claude Code with the plugins directory
claude --add-dir /path/to/cre-agent-skills/claude-code-plugins/cre-due-diligence
```

This loads the plugin for the current session only. Skills from `--add-dir` directories are detected automatically and support live editing — you can modify skill files during a session without restarting.

### Using the Plugins

Once installed, invoke any plugin with its slash command:

```bash
# Due Diligence
/cre-due-diligence Analyze this rent roll for Parkview Apartments, 200 units, Austin TX
/cre-due-diligence Run an environmental review on the Phase I ESA I just uploaded
/cre-due-diligence Benchmark these T-12 operating expenses against Class B multifamily

# Underwriting
/cre-underwriting Build a 5-year pro forma using the DD outputs we just generated
/cre-underwriting Run 27 scenario stress tests on this financial model
/cre-underwriting Write an IC memo summarizing this deal

# Financing
/cre-financing Which lenders should we approach for a $24M loan on a 200-unit Class B in Austin?
/cre-financing Compare these 4 lender quotes and rank them
/cre-financing Build a term sheet based on the Freddie Mac quote

# Legal
/cre-legal Review this Purchase & Sale Agreement clause by clause
/cre-legal Analyze the title commitment I uploaded
/cre-legal Track estoppel certificate collection — here's the rent roll and returned certificates

# Closing
/cre-closing Build the closing checklist — here's where we stand on all workstreams
/cre-closing Prepare the funds flow memo — here are the deal terms

# Document Ingestion
/cre-document-ingestion Classify these deal documents I just uploaded
/cre-document-ingestion Parse this rent roll into structured data
/cre-document-ingestion Extract the financials from this T-12

# Industrial v1
/cre-industrial Analyze the market for a 240,000 SF distribution asset in Dallas
/cre-industrial Review this industrial lease roster and highlight rollover risk
/cre-industrial Build an underwriting view for this shallow-bay acquisition

# Brokerage v1
/cre-brokerage Build a BOV for this office investment sale listing
/cre-brokerage Draft the OM and teaser for this retail center
/cre-brokerage Level these offers and recommend a seller response

# Office v1
/cre-office Analyze the market and flight-to-quality risk for this CBD tower
/cre-office Review this rent roll and stacking plan for rollover exposure
/cre-office Build a TI/LC-heavy underwriting view for this office recap

# Capital Markets v1
/cre-capital-markets Diagnose the maturity risk for this loan due in October
/cre-capital-markets Calculate the refinance proceeds gap and rescue-capital need
/cre-capital-markets Build the lender update package for an extension request

# Retail v1
/cre-retail Define and test the trade area for this grocery-anchored center
/cre-retail Map the co-tenancy clauses and model the dark-anchor cascade
/cre-retail Rebuild the CAM pool and reconcile recovery income to underwriting

# Lender / Credit v1
/cre-lender-credit Screen and size this $18M loan request against policy
/cre-lender-credit Write the credit approval memo for the loan committee
/cre-lender-credit Run the annual review and confirm or change the risk rating

# Development and Construction v1
/cre-development Screen this site for zoning fit and entitlement risk
/cre-development Test the budget with untrended and trended yield on cost
/cre-development Review this month's draw package and cost to complete
```

Claude reads the `SKILL.md` entry point, identifies which specialist skill to load based on your request, loads the full skill instructions plus relevant knowledge bases, and runs the analysis.

### Plugin Structure (For Reference)

Each plugin follows this pattern:

```
cre-{department}/
├── SKILL.md          # Entry point — YAML frontmatter + routing logic
├── skills/           # Specialist skill files (the actual analysis prompts)
│   ├── skill-one.md
│   ├── skill-two.md
│   └── ...
└── knowledge/        # Domain knowledge reference files (formulas, benchmarks, criteria)
    ├── relevant-knowledge-base-1.md
    └── relevant-knowledge-base-2.md
```

The `SKILL.md` file contains YAML frontmatter that tells Claude Code:
- `name` — the slash command name (e.g., `cre-due-diligence`)
- `description` — when Claude should automatically consider using this skill
- `argument-hint` — what to show in autocomplete

The body of `SKILL.md` routes the user's request to the right specialist skill file, which Claude loads on demand. Knowledge base files provide reference data (formulas, benchmarks, criteria) that the specialist skills draw on.

---

## Installation Methods

Different AI platforms have different ways to load skills. Here's how to use them everywhere:

### Claude Code (Plugins — Recommended)

See [Claude Code Plugins](#claude-code-plugins-recommended) above for the full setup guide. This is the best experience — you get slash commands, automatic routing, and bundled knowledge bases.

### Claude Projects (claude.ai)

1. Open [claude.ai](https://claude.ai) and create a new Project
2. Click "Add knowledge" in the Project settings
3. Upload the `.md` skill file(s) you want to use from the `skills/` directory
4. Optionally upload knowledge base files from `knowledge/` that the skill recommends
5. Start a conversation — Claude automatically references the loaded skills

**Tip:** Name your project by deal (e.g., "Parkview Apartments DD") and load the relevant skill subset.

### ChatGPT (Custom GPTs)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. Paste the full content of a skill file into the "Instructions" field
3. Upload knowledge base files as the GPT's "Knowledge" documents
4. Save and use the GPT for that specific analysis task

### Cursor / Windsurf / AI Code Editors

Copy skill files into your editor's rules directory:

```bash
# Cursor
cp skills/due-diligence/rent-roll-analyst.md .cursor/rules/

# Or reference via --add-dir in Cursor's Claude Code integration
```

### Any LLM (API Usage)

Include skill content in your system prompt:

```python
import anthropic

skill = open("skills/due-diligence/rent-roll-analyst.md").read()
knowledge = open("knowledge/multifamily-benchmarks.md").read()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    system=f"{skill}\n\n---\n\nReference Knowledge:\n{knowledge}",
    messages=[
        {"role": "user", "content": "Analyze this rent roll: [paste data]"}
    ]
)
```

---

## Skill Index

### Due Diligence (7 skills)

| Skill | What It Does |
|-------|-------------|
| [Rent Roll Analyst](skills/due-diligence/rent-roll-analyst.md) | Validates unit mix, in-place rents vs market, loss-to-lease, occupancy metrics, tenant concentration risks, and anomaly detection |
| [OpEx Analyst](skills/due-diligence/opex-analyst.md) | Analyzes T-12 operating expenses, per-unit benchmarking by property class and region, line-item trends, management fee validation, tax reassessment modeling |
| [Market Study](skills/due-diligence/market-study.md) | Researches submarket fundamentals — demographics, employment, supply pipeline, absorption rates, rent comps, competitive set analysis |
| [Physical Inspection](skills/due-diligence/physical-inspection.md) | Assesses property condition from inspection reports, estimates CapEx needs by system, remaining useful life calculations, deferred maintenance quantification |
| [Environmental Review](skills/due-diligence/environmental-review.md) | Evaluates Phase I ESA findings, contamination risk, regulatory compliance, remediation cost estimation, vapor intrusion risk |
| [Legal & Title Review](skills/due-diligence/legal-title-review.md) | Analyzes title commitment, searches for exceptions and encumbrances, easement review, lien detection, deed restriction analysis |
| [Tenant Credit](skills/due-diligence/tenant-credit.md) | Evaluates tenant creditworthiness, income concentration risk, lease rollover exposure, credit scoring, Section 8/subsidized housing analysis |

### Underwriting (3 skills)

| Skill | What It Does |
|-------|-------------|
| [Financial Model Builder](skills/underwriting/financial-model-builder.md) | Builds a complete 5-year pro forma — GPI, vacancy, EGI, OpEx, NOI, debt service, cash flow, reversion, and return metrics (IRR, equity multiple, CoC) |
| [Scenario Analyst](skills/underwriting/scenario-analyst.md) | Runs 27 sensitivity scenarios across rent growth, vacancy, and exit cap rate — stress-tests the deal under adverse conditions |
| [IC Memo Writer](skills/underwriting/ic-memo-writer.md) | Synthesizes all analysis into a structured investment committee memorandum with executive summary, financials, risk factors, and go/no-go recommendation |

### Financing (3 skills)

| Skill | What It Does |
|-------|-------------|
| [Lender Outreach](skills/financing/lender-outreach.md) | Maps deal profile to lender criteria across Agency, CMBS, Life Companies, Banks, and Bridge sources — identifies which lenders to approach and why |
| [Quote Comparator](skills/financing/quote-comparator.md) | Normalizes and scores multiple lender quotes on a common basis using a weighted comparison matrix — identifies the best financing option |
| [Term Sheet Builder](skills/financing/term-sheet-builder.md) | Assembles a complete term sheet, identifies negotiation leverage points, flags non-standard terms, and models rate lock scenarios |

### Legal (6 skills)

| Skill | What It Does |
|-------|-------------|
| [PSA Reviewer](skills/legal/psa-reviewer.md) | Reviews Purchase & Sale Agreement clause by clause — contingencies, representations, earnest money, closing conditions, assignment rights |
| [Title & Survey Reviewer](skills/legal/title-survey-reviewer.md) | Reviews title commitment and ALTA survey — boundary verification, easement impact, encroachment detection, flood zone, zoning compliance |
| [Estoppel Tracker](skills/legal/estoppel-tracker.md) | Manages estoppel certificate collection — tracks sent/received/outstanding, validates tenant-reported terms against rent roll, flags discrepancies |
| [Loan Doc Reviewer](skills/legal/loan-doc-reviewer.md) | Reviews loan documents from the selected lender — note, mortgage, guaranty, environmental indemnity, UCC filings, term sheet compliance |
| [Insurance Coordinator](skills/legal/insurance-coordinator.md) | Verifies insurance requirements from lender and PSA — property, liability, flood, windstorm, umbrella coverage, gap analysis |
| [Transfer Doc Preparer](skills/legal/transfer-doc-preparer.md) | Prepares transfer documentation — deed, bill of sale, assignment of leases, FIRPTA certificate, transfer tax calculations, entity verification |

### Closing (2 skills)

| Skill | What It Does |
|-------|-------------|
| [Closing Coordinator](skills/closing/closing-coordinator.md) | Manages the closing checklist across all workstreams — verifies conditions precedent, tracks outstanding items, performs readiness assessment |
| [Funds Flow Manager](skills/closing/funds-flow-manager.md) | Prepares the funds flow memo — purchase price allocation, prorations, lender disbursement, escrow holdbacks, wire instructions, closing costs |

### Document Ingestion (4 skills)

| Skill | What It Does |
|-------|-------------|
| [Document Classifier](skills/document-ingestion/document-classifier.md) | Classifies incoming deal documents by type (rent roll, T-12, offering memo, etc.) and identifies what data can be extracted from each |
| [Rent Roll Parser](skills/document-ingestion/rent-roll-parser.md) | Extracts structured data from rent roll files — unit numbers, tenant names, lease dates, rents, deposits, status |
| [Financials Parser](skills/document-ingestion/financials-parser.md) | Extracts T-12 operating statements — income line items, expense categories, month-over-month trends |
| [Offering Memo Parser](skills/document-ingestion/offering-memo-parser.md) | Extracts property details, investment highlights, financial projections, and market data from offering memoranda |

### Industrial v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Industrial Market Study](skills/industrial/industrial-market-study.md) | Evaluates a U.S. industrial submarket, competing inventory, logistics positioning, and release depth |
| [Industrial Lease Roster Analyst](skills/industrial/industrial-lease-roster-analyst.md) | Measures WALT, concentration, rollover exposure, reimbursement structure, and release risk from an industrial roster |
| [Industrial Lease Abstract Reviewer](skills/industrial/industrial-lease-abstract-reviewer.md) | Abstracts industrial lease economics, repair obligations, options, transfer rights, estoppel, and SNDA items |
| [Industrial Tenant Credit Analyst](skills/industrial/industrial-tenant-credit-analyst.md) | Evaluates tenant durability, concentration, facility dependence, and release risk |
| [Industrial Physical Inspection](skills/industrial/industrial-physical-inspection.md) | Assesses condition, functionality, power, fire-life-safety, and capital needs for industrial assets |
| [Industrial Underwriting Model Builder](skills/industrial/industrial-underwriting-model-builder.md) | Builds a lease-driven industrial acquisition model that incorporates rollover, downtime, TI, and LC |
| [Industrial Financing Fit](skills/industrial/industrial-financing-fit.md) | Matches industrial deals to bank, life company, CMBS, bridge, or SBA owner-user executions |
| [Industrial IC Memo Writer](skills/industrial/industrial-ic-memo-writer.md) | Synthesizes industrial diligence into an investment-committee-ready recommendation |

### Brokerage Investment Sales v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Assignment Intake Manager](skills/brokerage/assignment-intake-manager.md) | Launches a seller-side assignment by organizing authority, seller goals, missing data, and process readiness |
| [Broker Opinion of Value Builder](skills/brokerage/broker-opinion-of-value-builder.md) | Produces a seller-side pricing opinion with valuation framing, range logic, and broker disclaimer language |
| [Listing Proposal Builder](skills/brokerage/listing-proposal-builder.md) | Drafts a seller-facing listing proposal with positioning, process, timeline, and scope framing |
| [Offering Memorandum and Teaser Writer](skills/brokerage/offering-memorandum-and-teaser-writer.md) | Drafts buyer-facing teaser and OM / CIM structure for a controlled investment sales process |
| [Buyer Process and Data Room Manager](skills/brokerage/buyer-process-and-data-room-manager.md) | Designs confidentiality, buyer qualification, data-room access, tours, and Q&A workflow |
| [Call for Offers and Bid Leveling Analyst](skills/brokerage/call-for-offers-and-bid-leveling-analyst.md) | Compares bids, normalizes certainty, and recommends leveling, BAFO, or backup strategy |
| [Deal Term Negotiation Brief Builder](skills/brokerage/deal-term-negotiation-brief-builder.md) | Organizes seller priorities, give / get issues, and business-term negotiation posture |
| [PSA to Close Transaction Coordinator](skills/brokerage/psa-to-close-transaction-coordinator.md) | Coordinates milestone tracking, open issues, and seller-side execution from signed deal to close |

### Asset Management v1 (9 skills)

| Skill | What It Does |
|-------|-------------|
| [Annual Operating Budget Builder](skills/asset-management/annual-operating-budget-builder.md) | Builds next-year operating budget from T-12 actuals, rent roll, and market assumptions with NOI / NCF split per Fannie Form 4660 convention |
| [Monthly Variance Analyst](skills/asset-management/monthly-variance-analyst.md) | Monthly and YTD variance analysis classifying each line item as Timing, Permanent, or One-Time with LP-ready commentary |
| [Rent Collection & Delinquency Manager](skills/asset-management/rent-collection-delinquency-manager.md) | A/R aging analysis, split-aging decision rule, state-specific eviction timelines, bad-debt reserve, and tenant-level collection actions |
| [Renewal Decision Analyst](skills/asset-management/renewal-decision-analyst.md) | Per-lease retain-vs-replace economics comparing retention cost to turnover cost, with rent-bump elasticity guidance |
| [Lease-Up & Concessions Analyst](skills/asset-management/lease-up-concessions-analyst.md) | Lease-up velocity tracking, concession burn-off mechanics, effective-vs-face rent reconciliation, and stabilization-date reforecasting |
| [CapEx & Value-Add Execution Tracker](skills/asset-management/capex-value-add-execution-tracker.md) | Capex program tracking vs budget, rent-premium realization %, yield-on-cost, and named failure-mode analysis |
| [NOI Improvement Analyst](skills/asset-management/noi-improvement-analyst.md) | Prioritized NOI lever library scored by Impact × Difficulty × Time-to-Realize across ancillary income, OpEx reduction, tax appeal, RUBS, and insurance shopping |
| [Hold/Sell/Refi Analyst](skills/asset-management/hold-sell-refi-analyst.md) | Four-scenario comparison (Hold / Refi+Hold / Sell-Current / Sell-Stabilized) with IRR-to-date, remaining-IRR projection, and disposition handoff to broker |
| [Quarterly Asset Review Writer](skills/asset-management/quarterly-asset-review-writer.md) | Composite flagship skill — synthesizes all eight prior AM skills into a publication-ready QAR memo for IC, LP, or internal asset committee |

### Office v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Office Market and Flight-to-Quality Study](skills/office/office-market-and-flight-to-quality-study.md) | Evaluates office submarket regime, prime-vs-commodity split, competitive set, demand depth, sublease pressure, and conversion risk |
| [Office Rent Roll and Stacking Plan Analyst](skills/office/office-rent-roll-and-stacking-plan-analyst.md) | Reconciles rent roll, occupancy, WALT, rollover, tenant concentration, and floor-by-floor exposure |
| [Office Lease Abstract Reviewer](skills/office/office-lease-abstract-reviewer.md) | Abstracts office lease economics, recovery structures, BOMA area, work letters, options, assignment/sublease, and termination or contraction rights |
| [Office Rollover and Occupancy Cost Analyst](skills/office/office-rollover-and-occupancy-cost-analyst.md) | Measures renewal probability, occupancy-cost pressure, replacement economics, and tenant-by-tenant action priorities |
| [Office TI / LC Underwriting Model Builder](skills/office/office-ti-lc-underwriting-model-builder.md) | Builds office cash flow after downtime, TI, LC, free rent, net effective rent, leasing reserves, and debt stress |
| [Office Tenant Credit and Exposure Analyst](skills/office/office-tenant-credit-and-exposure-analyst.md) | Evaluates tenant durability, guarantor exposure, industry concentration, concentration cliffs, watchlist risk, and downside vacancy |
| [Office Financing Fit](skills/office/office-financing-fit.md) | Matches office deals to bank, life company, CMBS, debt fund, SBA owner-user, private credit, or rescue-capital lanes |
| [Office IC Memo Writer](skills/office/office-ic-memo-writer.md) | Synthesizes office market, lease, tenant, TI/LC, financing, and risk findings into a decision memo |

### Capital Markets v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Debt Maturity Diagnostic](skills/capital-markets/debt-maturity-diagnostic.md) | Classifies maturity urgency, refinanceability, extension risk, and the controlling constraint |
| [Refinance Proceeds Gap Analyzer](skills/capital-markets/refinance-proceeds-gap-analyzer.md) | Calculates supportable refinance proceeds, all-in payoff, reserves, costs, and total gap |
| [Extension / Workout Strategy Builder](skills/capital-markets/extension-workout-strategy-builder.md) | Builds lender-credible extension, modification, forbearance, discounted payoff, or workout strategy |
| [Rescue Capital Comparator](skills/capital-markets/rescue-capital-comparator.md) | Compares preferred equity, mezzanine, JV equity, bridge, note purchase, discounted payoff, and sale alternatives |
| [Capital Stack Term Sheet Comparator](skills/capital-markets/capital-stack-term-sheet-comparator.md) | Normalizes competing debt, mezzanine, preferred equity, and JV equity term sheets |
| [CMBS / Special Servicing Readiness Reviewer](skills/capital-markets/cmbs-special-servicing-readiness-reviewer.md) | Reviews CMBS watchlist, maturity default, transfer, and special-servicing package readiness |
| [Lender Update Package Builder](skills/capital-markets/lender-update-package-builder.md) | Builds lender, servicer, or capital-provider update package with NOI bridge and exhibit checklist |
| [Recap IC Memo Writer](skills/capital-markets/recap-ic-memo-writer.md) | Synthesizes refinance, extension, workout, rescue capital, sale, or hold alternatives into an IC memo |

### Retail v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Retail Market and Trade Area Study](skills/retail/retail-market-and-trade-area-study.md) | Defines and tests the trade area behind a retail asset - demand, void and leakage, competitive supply, anchor draw, access, and category resilience |
| [Retail Rent Roll and Tenant Mix Analyst](skills/retail/retail-rent-roll-and-tenant-mix-analyst.md) | Turns a retail rent roll into a reconciled read on space mix, tenant productivity, rollover, concentration, credit, and mark-to-market |
| [Retail Lease Abstract Reviewer](skills/retail/retail-lease-abstract-reviewer.md) | Abstracts retail leases into economic, recovery, and control-right summaries and flags the investor, lender, and rent-roll conflicts that change value |
| [Retail Co-Tenancy and Anchor Risk Analyst](skills/retail/retail-co-tenancy-and-anchor-risk-analyst.md) | Maps anchors and co-tenancy clauses, models the dark-anchor cascade, tests the REA, and rates anchor risk with a mitigation plan |
| [Retail CAM Reconciliation and Recovery Analyst](skills/retail/retail-cam-reconciliation-and-recovery-analyst.md) | Rebuilds the recoverable expense pool lease by lease, tests prior CAM reconciliations, and ties recovery income back to underwriting |
| [Retail Underwriting Model Builder](skills/retail/retail-underwriting-model-builder.md) | Builds a lease-by-lease retail cash flow with percentage rent, capped recoveries, sales-driven renewals, anchor reserve, co-tenancy downside, and lender sizing |
| [Retail Financing Fit](skills/retail/retail-financing-fit.md) | Maps a retail asset to the lender lanes that will actually quote it, finds the test that controls proceeds, and specifies required structure |
| [Retail IC Memo Writer](skills/retail/retail-ic-memo-writer.md) | Synthesizes trade area, rent roll, lease, co-tenancy, recovery, underwriting, and financing work into one IC memo with a decision table and named conditions |

### Lender / Credit v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Loan Request Screening and Sizing](skills/lender-credit/loan-request-screening-and-sizing.md) | Screens an incoming loan request for product and policy fit, sizes it under every applicable test, names the controlling test, and returns a pursue / structure / decline verdict |
| [Sponsor and Guarantor Analyst](skills/lender-credit/sponsor-and-guarantor-analyst.md) | Analyzes sponsor and guarantor financials, verified liquidity and net worth, contingent liabilities and REO, global cash flow and global DSCR, track record, and guaranty structure |
| [Appraisal and Valuation Reviewer](skills/lender-credit/appraisal-and-valuation-reviewer.md) | Reviews an appraisal or evaluation for regulatory compliance and analytical reasonableness, reconciles it to underwriting, and issues accept, condition, or reject |
| [Credit Memo Writer](skills/lender-credit/credit-memo-writer.md) | Drafts a CRE credit approval memorandum that an approval authority, loan review, and an examiner can all read in the same order |
| [Covenant Compliance and Watchlist Monitor](skills/lender-credit/covenant-compliance-and-watchlist-monitor.md) | Tests a closed loan against covenants, reporting obligations, and structural triggers, then recommends watchlist placement, retention, or removal with an action plan |
| [Annual Loan Review and Risk Rating](skills/lender-credit/annual-loan-review-and-risk-rating.md) | Refreshes NOI, DSCR, debt yield, LTV, appraisal age, rollover, sponsor condition, and exceptions, then confirms or changes the classification and internal grade |
| [Problem Loan and Modification Analyst](skills/lender-credit/problem-loan-and-modification-analyst.md) | Classifies a deteriorating loan, names the source of impairment, compares resolution paths on recovery, timing, cost, and accounting, and sets an action plan |
| [CRE Portfolio Concentration and Stress Tester](skills/lender-credit/cre-portfolio-concentration-and-stress-tester.md) | Segments a CRE book against the supervisory concentration criteria, stresses it, estimates rating migration and reserve pressure, and produces a board or ALCO-ready report |

### Development and Construction v1 (8 skills)

| Skill | What It Does |
|-------|-------------|
| [Site and Entitlement Screen](skills/development/site-and-entitlement-screen.md) | Screens a development site for zoning fit, entitlement path, fees and exactions, environmental and physical constraints, and political risk |
| [Development Budget and Yield on Cost Analyst](skills/development/development-budget-and-yield-on-cost-analyst.md) | Builds or audits a development budget, ties it to sources and uses, and tests untrended and trended yield on cost, spread, residual land value, and overrun sensitivity |
| [Construction Loan Sizing and Structure](skills/development/construction-loan-sizing-and-structure.md) | Sizes a construction loan against every controlling test and structures cash equity, interest reserve, guaranties, draw controls, and takeout |
| [Construction Draw and Cost-to-Complete Reviewer](skills/development/construction-draw-and-cost-to-complete-reviewer.md) | Reviews a monthly draw package end to end - pay application, retainage, lien waivers, change orders, cost to complete, in-balance test - and recommends fund, partial-fund, or hold |
| [GC Contract and Change Order Reviewer](skills/development/gc-contract-and-change-order-reviewer.md) | Reviews a GC or CM agreement and its change orders for price, time, payment, and risk transfer, and produces an issues list with negotiation positions |
| [Schedule and Delivery Risk Tracker](skills/development/schedule-and-delivery-risk-tracker.md) | Tracks the schedule from entitlement through certificate of occupancy, tests delivery against the loan and lease-up plan, prices delay, and rates each milestone |
| [Lease-Up and Stabilization Pro Forma](skills/development/lease-up-and-stabilization-pro-forma.md) | Models absorption, pre-leasing, concession burn-off, operating shortfall and carry, breakeven and stabilization dates, and whether the takeout repays the construction loan |
| [Development IC Memo Writer](skills/development/development-ic-memo-writer.md) | Synthesizes site and entitlement, budget and yield on cost, capital stack, contract, schedule, and lease-up work into a development IC memo with a go / no-go recommendation |

---

## Knowledge Bases

Thirty-five reference files containing formulas, benchmarks, criteria, and checklists. Five belong to the original multifamily-first release, three extend the repo for Industrial v1, four extend it for Brokerage Investment Sales v1, three extend it for Asset Management v1, four extend it for Office v1, four extend it for Capital Markets v1, four extend it for Retail v1, four extend it for Lender / Credit v1, and four extend it again for Development and Construction v1.

| Knowledge Base | What It Contains | Used By |
|---------------|-----------------|---------|
| [Underwriting Calculations](knowledge/underwriting-calc.md) | Every CRE financial formula — GPI, EGI, NOI, DSCR, LTV, Cap Rate, IRR, Equity Multiple, Cash-on-Cash, Debt Yield, loan amortization, and more | Financial Model Builder, Scenario Analyst, Quote Comparator, Rent Roll Analyst |
| [Risk Scoring Framework](knowledge/risk-scoring.md) | 9-category risk scoring system (0-100 scale) covering ownership, physical, environmental, market, financial, tenant, legal, capital markets, and operational risk | All Due Diligence skills, IC Memo Writer |
| [Multifamily Benchmarks](knowledge/multifamily-benchmarks.md) | Institutional-quality benchmarks — operating expenses by property class (A/B/C) and region, occupancy standards, rent growth, CapEx reserves, management fees, turnover costs | OpEx Analyst, Financial Model Builder, Market Study, Rent Roll Analyst |
| [Lender Criteria](knowledge/lender-criteria.md) | Full spectrum of multifamily lending sources — Agency (Fannie/Freddie), CMBS, Life Companies, Banks, Bridge/Mezzanine — with eligibility, loan parameters, rate structures, and prepayment terms | Lender Outreach, Quote Comparator, Term Sheet Builder |
| [Legal Checklist](knowledge/legal-checklist.md) | Legal compliance requirements across the acquisition lifecycle — PSA review items, title requirements, survey standards, environmental compliance, entity formation, transfer documentation | All Legal skills, Closing Coordinator |
| [Industrial Benchmarks](knowledge/industrial-benchmarks.md) | U.S. industrial market, building-function, lease-risk, and underwriting guardrails by subtype | Industrial Market Study, Physical Inspection, Underwriting, IC Memo |
| [Industrial Lease Structures](knowledge/industrial-lease-structures.md) | U.S. industrial lease structures, reimbursements, repairs, assignment, estoppel, and SNDA issue spotting | Industrial Lease Roster, Lease Abstract, Underwriting |
| [Industrial Lender Criteria](knowledge/industrial-lender-criteria.md) | U.S. lender-fit guidance for industrial deals across banks, life companies, CMBS, bridge, and SBA owner-user cases | Industrial Financing Fit, Underwriting, IC Memo |
| [Brokerage Investment Sales Process](knowledge/brokerage-investment-sales-process.md) | Seller-side sequence from assignment intake through close | Assignment Intake, Listing Proposal, Closing Coordination |
| [Broker Opinion of Value Guidance](knowledge/broker-opinion-of-value-guidance.md) | BOV boundaries, method selection, disclaimer logic, and state-law caution | BOV Builder, Listing Proposal |
| [Marketing Confidentiality and Buyer Process](knowledge/marketing-confidentiality-and-buyer-process.md) | Teaser / OM release, confidentiality, registration, vetting, data room, tours, and Q&A | OM / Teaser Writer, Buyer Process Manager |
| [Offer Negotiation and Closing Playbook](knowledge/offer-negotiation-and-closing-playbook.md) | Bid comparison, BAFO logic, seller-side negotiation framing, and PSA-to-close coordination | Bid Leveling, Negotiation Brief, PSA-to-Close |
| [Asset Management Benchmarks](knowledge/asset-management-benchmarks.md) | Operational benchmarks for variance materiality, A/R reserves, turnover costs, unit-turn capex, concession norms by market, bad-debt, absorption, ancillary income lift, and rent-premium realization | Budget Builder, Variance Analyst, Collections Manager, Lease-Up Analyst, CapEx Tracker, NOI Improvement |
| [Renewal Economics](knowledge/renewal-economics.md) | Retain-vs-replace framework, turnover cost components, rent-bump elasticity curve, tenant A/B/C tiering, hold-period analytics, refinance DSCR/LTV gates, and four-scenario disposition framework | Renewal Analyst, CapEx Tracker, Hold/Sell/Refi Analyst |
| [Asset Management Reporting Standards](knowledge/asset-management-reporting-standards.md) | 10-section QAR template, LP report cadence, 12-KPI mandatory dashboard, T-3 vs T-12 bridging conventions, variance-classification taxonomy, and commentary-to-table ratios | Variance Analyst, Quarterly Asset Review Writer |
| [Office Benchmarks](knowledge/office-benchmarks.md) | Office market, quality-tier, vacancy, leasing, operating, sublease, and flight-to-quality guardrails | Office Market Study, Rent Roll / Stacking Plan, TI/LC Underwriting, Office IC Memo |
| [Office Lease Structures](knowledge/office-lease-structures.md) | Full-service, modified gross, base-year, expense-stop, NNN, BOMA area, work letter, option, assignment, sublease, contraction, and termination issue spotting | Office Lease Abstract, Rent Roll / Stacking Plan, Rollover Analyst |
| [Office TI/LC Economics](knowledge/office-ti-lc-economics.md) | TI, LC, free rent, downtime, net effective rent, leasing-cost reserve, renewal-vs-new-lease, and capital stack stress modeling | TI/LC Underwriting, Rollover Analyst, Financing Fit |
| [Office Lender Criteria](knowledge/office-lender-criteria.md) | Office lender lanes, sizing tests, DSCR / debt-yield pressure, leasing reserves, recourse posture, and financing red flags | Office Financing Fit, TI/LC Underwriting, Office IC Memo |
| [Capital Markets Benchmarks](knowledge/capital-markets-benchmarks.md) | Debt sizing, refinance gap, DSCR, debt yield, LTV, LTC, debt constant, and capital-stack screening logic | Debt Maturity Diagnostic, Refinance Gap Analyzer, Term Sheet Comparator, Recap IC Memo |
| [Workout and Extension Structures](knowledge/workout-and-extension-structures.md) | Extensions, modifications, forbearance, A/B notes, discounted payoff, deed-in-lieu, lender give/get, and package requirements | Extension / Workout Strategy, Lender Update Package, Recap IC Memo |
| [Rescue Capital and Preferred Equity](knowledge/rescue-capital-and-pref-equity.md) | Preferred equity, mezzanine, JV equity, bridge, note purchase, discounted payoff, dilution, governance, and exit analysis | Rescue Capital Comparator, Refinance Gap Analyzer, Term Sheet Comparator |
| [CMBS Servicing and Default Playbook](knowledge/cmbs-servicing-and-default-playbook.md) | CMBS parties, transfer triggers, special-servicer package readiness, borrower strategy, and watchlist/default signals | CMBS Readiness Reviewer, Extension / Workout Strategy, Lender Update Package |
| [Retail Benchmarks](knowledge/retail-benchmarks.md) | Retail format definitions, occupancy and leasing reference points, leasing capital, occupancy cost and sales PSF, recovery load, and e-commerce exposure | Retail Market and Trade Area Study, Rent Roll and Tenant Mix, Retail Underwriting, Retail IC Memo |
| [Retail Lease Structures](knowledge/retail-lease-structures.md) | Retail lease forms, base and percentage rent, CAM / tax / insurance recovery, tenant control rights, REA / OEA and pads, assignment, estoppel, and SNDA issue spotting | Retail Lease Abstract Reviewer, Co-Tenancy and Anchor Risk, CAM Reconciliation |
| [Retail Tenant Sales and Occupancy Cost](knowledge/retail-tenant-sales-and-occupancy-cost.md) | Sales and occupancy-cost definitions, category frames, tenant credit tiers, distress and store-closure signals, renewal and backfill economics, and STNL frameworks | Rent Roll and Tenant Mix, Retail Underwriting, Retail IC Memo |
| [Retail Lender Criteria](knowledge/retail-lender-criteria.md) | Retail lender lanes, core sizing tests, how lenders read retail deterioration, reserves, holdbacks, and recourse posture | Retail Financing Fit, Retail Underwriting, Retail IC Memo |
| [Lender Credit Policy Benchmarks](knowledge/lender-credit-policy-benchmarks.md) | What examiners expect in a CRE credit policy, supervisory leverage ceilings and the exception basket, sizing and structure frames by lender and property type, and pricing and reserve frames | Loan Request Screening and Sizing, Credit Memo Writer, Annual Loan Review |
| [Regulatory Risk Rating and Classification](knowledge/regulatory-risk-rating-and-classification.md) | Supervisory classification definitions, criticized / classified / watchlist mapping, dual risk rating scales, nonaccrual, modification treatment, and rating migration reporting | Annual Loan Review and Risk Rating, Covenant Compliance and Watchlist Monitor, Problem Loan Analyst |
| [Credit Memo and Appraisal Review Standards](knowledge/credit-memo-and-appraisal-review-standards.md) | Credit approval memo structure, documentation and covenant checklists, policy exceptions and supervisory LTV limits, appraisal-versus-evaluation tests, and appraisal review standards | Credit Memo Writer, Appraisal and Valuation Reviewer |
| [CRE Concentration and Stress Testing](knowledge/cre-concentration-and-stress-testing.md) | Supervisory concentration screening criteria, book segmentation, stress-test design, and how results feed capital, ACL, and policy limits | CRE Portfolio Concentration and Stress Tester, Annual Loan Review |
| [Development Benchmarks](knowledge/development-benchmarks.md) | Development budget taxonomy, contingency and escalation, dated cost frames, yield on cost and development spread, residual land value, and schedule and lease-up durations | Development Budget and Yield on Cost Analyst, Lease-Up and Stabilization Pro Forma, Development IC Memo |
| [Construction Lending Criteria](knowledge/construction-lending-criteria.md) | Construction sizing tests, equity and HVCRE treatment, interest reserve and carry, guaranty posture, in-balance and draw controls, and extension / mini-perm / takeout paths | Construction Loan Sizing and Structure, Draw and Cost-to-Complete Reviewer, Development IC Memo |
| [Construction Contracts and Draw Controls](knowledge/construction-contracts-and-draw-controls.md) | Contract families and risk allocation, money mechanics, change orders versus construction change directives, completion and retainage, draw packages, lien waivers, bonds, and insurance | GC Contract and Change Order Reviewer, Draw and Cost-to-Complete Reviewer |
| [Entitlement and Site Risk](knowledge/entitlement-and-site-risk.md) | Approval pathways and what each costs, exactions and impact fees, environmental site review, utilities and geotechnical obligations, and historic, design, and state environmental review | Site and Entitlement Screen, Schedule and Delivery Risk Tracker |

**How to use knowledge bases:** Load the knowledge base alongside the skill you're using. For example, when using the Financial Model Builder skill, also load Underwriting Calculations for formula definitions and Multifamily Benchmarks for expense assumptions. The Claude Code plugins bundle relevant knowledge bases automatically.

### Companion Research Notes

Industrial v1 includes 11 research notes under `research/industrial/` plus [research/industrial/INDEX.md](research/industrial/INDEX.md). Brokerage Investment Sales v1 adds 12 more research notes under `research/brokerage/` plus [research/brokerage/INDEX.md](research/brokerage/INDEX.md). Asset Management v1 adds 10 more research files under `research/asset-management/` - 1 shared taxonomy seed, 9 skill-backing notes with 168+ cited sources, and [research/asset-management/INDEX.md](research/asset-management/INDEX.md). Office v1 adds 12 more research notes under `research/office/` plus [research/office/INDEX.md](research/office/INDEX.md). Capital Markets v1 adds 12 more research notes under `research/capital-markets/` plus [research/capital-markets/INDEX.md](research/capital-markets/INDEX.md). Retail v1 adds 12 more research notes under `research/retail/` plus [research/retail/INDEX.md](research/retail/INDEX.md). Lender / Credit v1 adds 12 more research notes under `research/lender-credit/` plus [research/lender-credit/INDEX.md](research/lender-credit/INDEX.md). Development and Construction v1 adds 12 more research notes under `research/development/` plus [research/development/INDEX.md](research/development/INDEX.md), bringing the repo to 93 companion research notes.

---

## How Skills Are Structured

Every skill follows the same format:

| Section | What It Contains |
|---------|-----------------|
| **When to Use This Skill** | Practical triggers — when should you reach for this? |
| **What You'll Need to Provide** | Plain-English list of required inputs |
| **Mission** | What the skill does in one paragraph |
| **Strategy** | Step-by-step analysis process with all formulas, thresholds, and domain logic |
| **Output Format** | Structured output template (JSON or Markdown) |
| **Quality Checks** | Self-validation rules — numeric sanity, cross-references, threshold comparisons |
| **Red Flags & Dealbreakers** | What to immediately escalate |
| **When Data is Missing** | How to handle gaps — use benchmarks, note assumptions, continue |
| **Confidence Scoring** | How to rate the reliability of the analysis |
| **Related Knowledge Bases** | Which companion files enhance this skill |

New sector and role-based packs may also include companion research notes that document the source basis for new benchmarks, process guidance, and assumptions.

---

## Project Structure

```
cre-agent-skills/
|-- README.md                              # This file
|-- LICENSE                                # Apache 2.0
|-- NOTICE                                 # Attribution notice
|
|-- skills/                                # 90 standalone skill files
|   |-- due-diligence/                     # 7 property analysis skills
|   |-- underwriting/                      # 3 financial modeling skills
|   |-- financing/                         # 3 debt sourcing skills
|   |-- legal/                             # 6 legal review skills
|   |-- closing/                           # 2 transaction completion skills
|   |-- document-ingestion/                # 4 document parsing skills
|   |-- industrial/                        # 8 industrial v1 skills
|   |-- brokerage/                         # 8 brokerage investment sales v1 skills
|   |-- asset-management/                  # 9 post-acquisition operations skills
|   |-- office/                            # 8 office v1 skills
|   |-- capital-markets/                   # 8 capital markets v1 skills
|   |-- retail/                            # 8 retail v1 skills
|   |-- lender-credit/                     # 8 lender / credit v1 skills
|   `-- development/                       # 8 development and construction v1 skills
|
|-- knowledge/                             # 35 domain knowledge reference files
|   |-- underwriting-calc.md
|   |-- risk-scoring.md
|   |-- multifamily-benchmarks.md
|   |-- lender-criteria.md
|   |-- legal-checklist.md
|   |-- industrial-benchmarks.md
|   |-- industrial-lease-structures.md
|   |-- industrial-lender-criteria.md
|   |-- brokerage-investment-sales-process.md
|   |-- broker-opinion-of-value-guidance.md
|   |-- marketing-confidentiality-and-buyer-process.md
|   |-- offer-negotiation-and-closing-playbook.md
|   |-- asset-management-benchmarks.md
|   |-- renewal-economics.md
|   |-- asset-management-reporting-standards.md
|   |-- office-benchmarks.md
|   |-- office-lease-structures.md
|   |-- office-ti-lc-economics.md
|   |-- office-lender-criteria.md
|   |-- capital-markets-benchmarks.md
|   |-- workout-and-extension-structures.md
|   |-- rescue-capital-and-pref-equity.md
|   |-- cmbs-servicing-and-default-playbook.md
|   |-- retail-benchmarks.md
|   |-- retail-lease-structures.md
|   |-- retail-tenant-sales-and-occupancy-cost.md
|   |-- retail-lender-criteria.md
|   |-- lender-credit-policy-benchmarks.md
|   |-- regulatory-risk-rating-and-classification.md
|   |-- credit-memo-and-appraisal-review-standards.md
|   |-- cre-concentration-and-stress-testing.md
|   |-- development-benchmarks.md
|   |-- construction-lending-criteria.md
|   |-- construction-contracts-and-draw-controls.md
|   `-- entitlement-and-site-risk.md
|
|-- research/                              # 93 companion research notes
|   |-- industrial/
|   |-- brokerage/
|   |-- asset-management/
|   |-- office/
|   |-- capital-markets/
|   |-- retail/
|   |-- lender-credit/
|   `-- development/
|
|-- claude-code-plugins/                   # 14 ready-to-install Claude Code plugins
|   |-- cre-due-diligence/
|   |-- cre-underwriting/
|   |-- cre-financing/
|   |-- cre-legal/
|   |-- cre-closing/
|   |-- cre-document-ingestion/
|   |-- cre-industrial/
|   |-- cre-brokerage/
|   |-- cre-asset-management/
|   |-- cre-office/
|   |-- cre-capital-markets/
|   |-- cre-retail/
|   |-- cre-lender-credit/
|   `-- cre-development/
|
|-- scripts/
|   |-- validate-repo.ps1                  # strict repo consistency checks (Windows)
|   `-- validate_repo.py                   # same checks, cross-platform (macOS / Linux)
|
|-- .github/
|   `-- workflows/validate.yml             # CI validation workflow
|
|-- templates/
|   `-- sample-inputs/                     # example input data for testing
|
`-- docs/
    |-- HOW-TO-USE.md                      # platform-specific setup instructions
    |-- SKILL-INDEX.md                     # quick reference with recommended combos
    `-- releases/                          # release notes and PR summaries
```

---

## Example Usage

### Example: Rent Roll Analysis

**Step 1:** Load `skills/due-diligence/rent-roll-analyst.md` into your AI tool (or use `/cre-due-diligence` in Claude Code)

**Step 2:** Optionally also load `knowledge/multifamily-benchmarks.md` for market benchmarks

**Step 3:** Provide your inputs:

> Analyze this rent roll for Parkview Apartments, a 200-unit Class B multifamily at 1200 Park Avenue, Austin TX 78701.
>
> [paste rent roll data — unit numbers, tenant names, lease dates, monthly rents, deposits, status]
>
> Asking rents: Studio $1,050, 1BR $1,250, 2BR $1,550, 3BR $1,850

**Step 4:** Get back structured analysis — unit summary, occupancy metrics, loss-to-lease calculation, tenant concentration risks, anomalies, revenue projections, and confidence scoring.

### Example: Full Deal Package Processing

```
/cre-document-ingestion I just received the deal package for Riverside Gardens.
Here are the files: [upload rent roll, T-12, offering memo]

# After classification and parsing:
/cre-due-diligence Analyze the rent roll data we just extracted
/cre-due-diligence Benchmark the T-12 expenses against Class B multifamily
/cre-underwriting Build a 5-year pro forma from the DD results
/cre-financing Which lenders should we approach for this deal?
```

### Example: Industrial v1 Workflow

```
/cre-document-ingestion Classify this industrial deal package
/cre-industrial Analyze the market for this 180,000 SF shallow-bay asset
/cre-industrial Review the lease roster and rollover risk
/cre-industrial Build the underwriting view
/cre-industrial Write the IC memo
```

### Example: Brokerage Investment Sales v1 Workflow

```
/cre-brokerage Run assignment intake for this suburban office listing
/cre-brokerage Build a broker opinion of value for this property
/cre-brokerage Draft the listing proposal and OM structure
/cre-brokerage Coordinate the buyer process and data room
/cre-brokerage Level the bids and recommend the next step
```

### Example: Asset Management v1 Workflow

```
/cre-asset-management Build the 2027 operating budget from this T-12 and rent roll
/cre-asset-management Analyze the March YTD variance and classify each line
/cre-asset-management Run aging analysis on this rent roll and recommend collection actions
/cre-asset-management Which expiring leases should we push on renewal vs let walk
/cre-asset-management Track this month's value-add capex execution vs plan
/cre-asset-management Give me the prioritized NOI improvement lever list
/cre-asset-management Compare hold vs refi vs sell for this asset at year 3
/cre-asset-management Draft the Q1 Asset Review memo for the LP
```

### Example: Office v1 Workflow

```
/cre-office Run a market and flight-to-quality study for this downtown office asset
/cre-office Reconcile the rent roll to the stacking plan and flag rollover exposure
/cre-office Abstract the major tenant leases and work-letter obligations
/cre-office Build the TI/LC underwriting model with downtime and free rent
/cre-office Test financing fit for a refinance at today's office lender standards
/cre-office Write the IC memo for the acquisition committee
```

### Example: Capital Markets v1 Workflow

```
/cre-capital-markets Diagnose the maturity risk for this loan due in October
/cre-capital-markets Calculate the refinance proceeds gap at current lender sizing
/cre-capital-markets Compare sponsor equity, preferred equity, mezzanine, and sale alternatives
/cre-capital-markets Build the lender update package for an extension request
/cre-capital-markets Write the recap IC memo with refinance, workout, rescue capital, and sale options
```

### Example: Retail v1 Workflow

```
/cre-retail Define and test the trade area for this grocery-anchored center
/cre-retail Reconcile the rent roll and score the tenant mix, rollover, and concentration
/cre-retail Abstract the anchor and inline leases, including exclusives and use restrictions
/cre-retail Map the co-tenancy clauses and model the dark-anchor cascade
/cre-retail Rebuild the CAM pool and test the last two reconciliations
/cre-retail Build the lease-by-lease underwriting model with percentage rent and capped recoveries
/cre-retail Test financing fit and identify the controlling sizing test
/cre-retail Write the IC memo for the acquisition committee
```

### Example: Lender / Credit v1 Workflow

```
/cre-lender-credit Screen and size this $18M loan request against our policy
/cre-lender-credit Analyze the sponsor and guarantor, including global cash flow and global DSCR
/cre-lender-credit Review the appraisal and reconcile it to our underwriting
/cre-lender-credit Draft the credit approval memo for loan committee
/cre-lender-credit Test covenant compliance and recommend watchlist treatment
/cre-lender-credit Run the annual review and confirm or change the risk rating
/cre-lender-credit Compare resolution paths on this deteriorating loan
/cre-lender-credit Stress the CRE book against the supervisory concentration criteria
```

### Example: Development and Construction v1 Workflow

```
/cre-development Screen this site for zoning fit, entitlement path, and political risk
/cre-development Build the development budget and test untrended and trended yield on cost
/cre-development Size the construction loan and structure the interest reserve and guaranties
/cre-development Review the GC contract and the pending change orders
/cre-development Review this month's draw package and the cost to complete
/cre-development Track the schedule against the loan completion date and price the delay
/cre-development Model lease-up, concession burn-off, and the stabilization date
/cre-development Write the development IC memo
```

---

## Common Workflows

### "I just got a new deal package"
1. **Document Classifier** → identify what's in the package
2. **Rent Roll Parser** + **Financials Parser** + **Offering Memo Parser** → extract structured data
3. **Rent Roll Analyst** + **OpEx Analyst** → validate the numbers
4. **Financial Model Builder** → build the pro forma

### "I need to underwrite this deal fast"
1. **Rent Roll Analyst** → revenue quality
2. **OpEx Analyst** → expense validation
3. **Financial Model Builder** → pro forma and returns
4. **Scenario Analyst** → stress test

### "We're ready to present to the investment committee"
1. **IC Memo Writer** → synthesize everything into a structured memo (load all prior analysis outputs as context)

### "We need to source debt"
1. **Lender Outreach** → identify lenders
2. **Quote Comparator** → compare received quotes
3. **Term Sheet Builder** → finalize terms

### "We're heading into closing"
1. **PSA Reviewer** → review the purchase agreement
2. **Title & Survey Reviewer** → clear title issues

### "I'm building next year's budget"
1. **Annual Operating Budget Builder** → line-by-line budget from T-12 + rent roll + market benchmarks
2. **Monthly Variance Analyst** → once actuals arrive, classify each variance as Timing / Permanent / One-Time

### "I need to write a quarterly LP report"
1. Run the upstream skills first (Budget Builder / Variance Analyst / Collections Manager / CapEx Tracker / NOI Improvement as needed)
2. **Quarterly Asset Review Writer** → synthesize everything into the 10-section QAR memo with the mandatory KPI dashboard

### "Should I hold, refinance, or sell?"
1. **Hold/Sell/Refi Analyst** → IRR-to-date, remaining-IRR projection, and a four-scenario comparison (Hold / Refi+Hold / Sell-Current / Sell-Stabilized)
2. If sell wins, pass the `disposition_handoff` block into the **Broker Opinion of Value Builder** in the Brokerage pack
3. **Estoppel Tracker** → manage tenant estoppels
4. **Loan Doc Reviewer** → review loan docs
5. **Insurance Coordinator** → verify coverage
6. **Transfer Doc Preparer** → prepare transfer docs
7. **Closing Coordinator** → manage the checklist
8. **Funds Flow Manager** → prepare settlement statement

### "I need a U.S. industrial acquisition workflow"
1. **Document Classifier** → inventory incoming files
2. **Industrial Market Study** → evaluate the submarket and building fit
3. **Industrial Lease Roster Analyst** → measure WALT, concentration, and rollover
4. **Industrial Lease Abstract Reviewer** → abstract reimbursements, repairs, options, and transfer rights
5. **Industrial Physical Inspection** → assess condition and competitiveness
6. **Industrial Underwriting Model Builder** → build the lease-driven base case
7. **Industrial Financing Fit** → identify likely lender lanes
8. **Industrial IC Memo Writer** → summarize the investment case

### "I need a seller-side investment sales workflow"
1. **Assignment Intake Manager** → organize authority, seller goals, and missing data
2. **Broker Opinion of Value Builder** → build the pricing recommendation
3. **Listing Proposal Builder** → prepare the seller-facing proposal
4. **Offering Memorandum and Teaser Writer** → create the buyer-facing marketing package
5. **Buyer Process and Data Room Manager** → control confidentiality, buyer vetting, tours, and Q&A
6. **Call for Offers and Bid Leveling Analyst** → compare bids and recommend leveling or BAFO
7. **Deal Term Negotiation Brief Builder** → frame the seller-side negotiation posture
8. **PSA to Close Transaction Coordinator** → coordinate the deal through closing

### "I need a U.S. office acquisition or refinance workflow"
1. **Office Market and Flight-to-Quality Study** → evaluate the submarket, quality tier, tenant demand, and competitive set
2. **Office Rent Roll and Stacking Plan Analyst** → reconcile occupancy, WALT, rollover, and floor-by-floor exposure
3. **Office Lease Abstract Reviewer** → abstract recoveries, options, work letters, contraction, termination, and sublease rights
4. **Office Rollover and Occupancy Cost Analyst** → score renewal probability and replacement economics
5. **Office TI / LC Underwriting Model Builder** → model downtime, TI, LC, free rent, net effective rent, and leasing reserves
6. **Office Tenant Credit and Exposure Analyst** → assess tenant durability, guarantor support, industry concentration, and downside vacancy
7. **Office Financing Fit** → identify likely lender lanes and sizing constraints
8. **Office IC Memo Writer** → summarize the investment or refinance case

### "My loan is maturing and the refinance may not cover the payoff"
1. **Debt Maturity Diagnostic** → classify urgency, current loan facts, refinanceability, and controlling constraint
2. **Refinance Proceeds Gap Analyzer** → quantify all-in payoff, supportable proceeds, reserves, costs, and gap
3. **Rescue Capital Comparator** → compare sponsor equity, preferred equity, mezzanine, JV equity, bridge debt, note purchase, DPO, and sale
4. **Capital Stack Term Sheet Comparator** → normalize term sheets and identify hidden cost, control, and consent issues
5. **Lender Update Package Builder** → prepare the lender or servicer package
6. **Recap IC Memo Writer** → make the final recommendation

### "I need an extension or workout strategy"
1. **Debt Maturity Diagnostic** → establish default risk, maturity window, and lender path
2. **Extension / Workout Strategy Builder** → select extension, modification, forbearance, A/B note, DPO, deed-in-lieu, or sale-process standstill
3. **CMBS / Special Servicing Readiness Reviewer** → use if the loan is securitized or may transfer to special servicing
4. **Lender Update Package Builder** → assemble ask, NOI bridge, business plan, exhibits, and lender protections
5. **Recap IC Memo Writer** → document decision, alternatives, risks, and approval conditions

### "I need a U.S. retail acquisition or asset review workflow"
1. **Retail Market and Trade Area Study** → test trade-area demand, void and leakage, competitive supply, and anchor draw
2. **Retail Rent Roll and Tenant Mix Analyst** → reconcile space mix, productivity, rollover, concentration, and mark-to-market
3. **Retail Lease Abstract Reviewer** → abstract economics, recovery structure, exclusives, use restrictions, and control rights
4. **Retail Co-Tenancy and Anchor Risk Analyst** → model the dark-anchor cascade and test the REA for re-tenanting restrictions
5. **Retail CAM Reconciliation and Recovery Analyst** → rebuild the recoverable pool and tie recovery income to underwriting
6. **Retail Underwriting Model Builder** → build the lease-by-lease cash flow with percentage rent, capped recoveries, and an anchor reserve
7. **Retail Financing Fit** → identify the lender lanes and the controlling sizing test
8. **Retail IC Memo Writer** → summarize the investment case with a decision table and named conditions

### "I am the lender on this deal, not the borrower"
1. **Loan Request Screening and Sizing** → test product and policy fit, size under every test, and name the controlling test
2. **Sponsor and Guarantor Analyst** → verify liquidity, net worth, contingent liabilities, global cash flow, and global DSCR
3. **Appraisal and Valuation Reviewer** → review the appraisal for compliance and reasonableness and reconcile it to underwriting
4. **Credit Memo Writer** → draft the approval memo for the approval authority, loan review, and the examiner
5. **Covenant Compliance and Watchlist Monitor** → test covenants and triggers after closing and set watchlist treatment
6. **Annual Loan Review and Risk Rating** → refresh the metrics, confirm or change the classification, and set the next review date
7. **Problem Loan and Modification Analyst** → compare resolution paths when the credit deteriorates
8. **CRE Portfolio Concentration and Stress Tester** → segment and stress the book for the board or ALCO

### "I am building this from the ground up"
1. **Site and Entitlement Screen** → test zoning fit, entitlement path, fees and exactions, and political risk
2. **Development Budget and Yield on Cost Analyst** → build the budget and test yield on cost, spread, and overrun sensitivity
3. **Construction Loan Sizing and Structure** → size the loan, quantify cash equity, and structure reserve, guaranty, and takeout
4. **GC Contract and Change Order Reviewer** → review price, time, payment, and risk transfer before signing
5. **Construction Draw and Cost-to-Complete Reviewer** → run the monthly draw, in-balance test, and cost to complete
6. **Schedule and Delivery Risk Tracker** → test delivery against the loan and the lease-up plan and price the delay
7. **Lease-Up and Stabilization Pro Forma** → model absorption, concessions, carry, breakeven, and takeout coverage
8. **Development IC Memo Writer** → summarize the development case with a go / no-go recommendation

---

## FAQ

### Do I need API keys to use these skills?

No. These are plain Markdown files. You load them into whatever AI tool you already use. There are no API calls, no external services, no dependencies.

### Can I use just one skill without installing everything?

Yes. Every skill file in the `skills/` directory is completely self-contained. Open the file, copy the content, paste it into your AI tool. You don't need the full repo.

### What's the difference between `skills/` and `claude-code-plugins/`?

The `skills/` directory contains individual `.md` files — one per analysis task. Use these when you want a single skill in any AI platform.

The `claude-code-plugins/` directory packages those same skills into department-level bundles for Claude Code, with a `SKILL.md` entry point that adds slash command support, automatic routing, and bundled knowledge bases. Use these if you're working in Claude Code and want the full department toolkit.

### How do the Claude Code plugins know which skill to use?

Each plugin's `SKILL.md` file contains a routing table. When you invoke `/cre-due-diligence Analyze this rent roll`, Claude reads the routing table, identifies that rent roll analysis maps to `skills/rent-roll-analyst.md`, loads that file, and follows its instructions. You don't need to know the individual skill file names.

### Can I modify the skills?

Yes. Apache 2.0 license — you can modify, extend, and redistribute. Fork the repo, adapt the skills to your firm's specific investment criteria, thresholds, or analysis standards. Just keep the attribution.

### How do these relate to the CRE Acquisition Orchestrator?

The [CRE Acquisition Orchestrator](https://github.com/ahacker-1/cre-acquisition-orchestrator) is the full multi-agent pipeline — 31 agents with orchestration logic, phase dependencies, checkpoint/resume, JSON schema data contracts, and a real-time dashboard. It's the "enterprise system" that runs all these skills together in an automated pipeline.

This repo extracts those same agents into standalone skills you can use individually. All orchestration-specific code (checkpoints, logging protocols, pipeline data contracts) has been stripped. All domain expertise (formulas, thresholds, analysis logic, benchmarks) has been preserved.

### Can I use these for property types other than multifamily?

Yes. The original repo was optimized for multifamily acquisitions, and those skills remain intact. As of v1.1.0, the repo also includes **Industrial v1** for U.S. industrial acquisitions. As of v1.2.0, it includes **Brokerage Investment Sales v1** for U.S. seller-side commercial investment sales process work. As of v1.4.0, it includes **Office v1** for U.S. office acquisitions, refinancings, recapitalizations, lease-up, tenant credit, TI/LC underwriting, and IC memo writing. As of v1.5.0, it includes **Capital Markets v1** for debt maturities, refinance gaps, workouts, rescue capital, special servicing, and recap decisions across property types. As of v1.6.0, it includes **Retail v1** for grocery-anchored, power, strip, lifestyle, mall, mixed-use, pad, and single-tenant net lease assets, **Lender / Credit v1** for the credit side of CRE lending, and **Development and Construction v1** for U.S. ground-up and heavy redevelopment. Self-storage, and affordable and workforce housing overlays, are still planned, though many shared, brokerage, capital-markets, and lender-side workflows transfer.

---

## Want the Full Pipeline?

These skills are extracted from the [CRE Acquisition Orchestrator](https://github.com/ahacker-1/cre-acquisition-orchestrator) — a 31-agent multi-agent system that runs all of these skills together with:

- **Hierarchical orchestration** — master → phase → specialist agents
- **Phase dependencies and parallel execution** — Legal starts at DD 80%
- **JSON Schema data contracts** — every handoff validated at runtime
- **3-tier checkpoint/resume** — nothing lost on interruption
- **Real-time 9-tab React dashboard** — live pipeline visualization
- **Deterministic simulation engine** — no API keys needed to demo
- **Investment committee memo generation** — automated go/no-go verdict

If you want individual tools, you're in the right place. If you want the full automated pipeline, check out the orchestrator.

---

## Who Is This For?

- **CRE analysts and associates** who want AI-assisted due diligence, underwriting, or legal review for specific tasks
- **Acquisition teams** that want to enhance specific parts of their workflow without adopting a full system
- **Proptech developers** looking for domain-specific prompt engineering patterns for CRE
- **AI engineers** who want to see how deep domain expertise translates into structured AI skill files
- **Anyone learning CRE** — these skills encode institutional-quality analysis frameworks that serve as educational references

---

## Author

**Avi Hacker, J.D.** — AI Consulting for Commercial Real Estate

I work with CRE firms to build AI systems that transform their acquisition and underwriting workflows. These skills encode the same domain expertise I use with clients, open-sourced so the whole industry can build on them.

- [Website — The AI Consulting Network](https://www.theaiconsultingnetwork.com)
- [Newsletter — AI Tactical Toolbox](https://avihacker.substack.com)
- [LinkedIn](https://linkedin.com/in/avi-hacker)

If you're building something in this space or want to talk about how AI can transform CRE workflows, reach out.

---

## License

[Apache 2.0](LICENSE) — Use freely, attribution required. See [NOTICE](NOTICE) for details.

Every skill file carries its own attribution notice in the frontmatter and in an **Attribution** footer. Apache 2.0 requires that notice to travel with the file, so keep it in place when you copy, adapt, or redistribute a skill.
