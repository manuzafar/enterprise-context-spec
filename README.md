# Enterprise Context Spec

**An open standard for defining organizational context that AI agents can consume.**

> *"The missing layer between AI agents and enterprise reality."*

---

## Executive Summary

Enterprise Context Spec (ECS) is a structured, schema-validated format for capturing organizational knowledge that AI agents need to operate effectively within large enterprises. Unlike technical protocols that connect AI to tools and data sources, ECS captures the *human* context: strategy, constraints, team structures, decision processes, and domain language.

**Key insight:** AI agents fail in enterprises not because they lack technical connectivity, but because they lack organizational understanding. They don't know your risk appetite, regulatory constraints, team boundaries, or who approves what. ECS solves this.

---

## Why This Matters for Agentic AI

### The Enterprise AI Context Gap

| What AI Agents Know | What They Need to Know |
|---------------------|------------------------|
| Your API schemas | Your strategic priorities |
| Your codebase structure | Your regulatory constraints |
| Your data formats | Your risk appetite |
| Your tool capabilities | Your team boundaries and ownership |
| How to call functions | Who approves decisions and when |

**Without organizational context, AI agents:**
- Suggest solutions that violate constraints
- Ignore regulatory requirements
- Propose changes to systems they don't own
- Use wrong terminology that confuses stakeholders
- Recommend approaches that exceed budget or timeline
- Overload teams that are already at capacity

**With Enterprise Context Spec, AI agents:**
- Respect budget constraints and approval thresholds
- Use correct domain language (ubiquitous language)
- Design within team boundaries (API ownership)
- Consider cognitive load before suggesting new work
- Align with architecture principles and ADRs
- Route decisions to appropriate stakeholders

---

## Novelty: What Makes ECS Different

### Not Another MCP or A2A

**Model Context Protocol (MCP)** by Anthropic connects AI to external tools and data sources. It's about *technical connectivity*.

**Agent-to-Agent (A2A)** by Google enables agents to communicate with each other. It's about *agent collaboration*.

**Enterprise Context Spec** captures organizational knowledge. It's about *human context*.

| Aspect | MCP | A2A | Enterprise Context Spec |
|--------|-----|-----|-------------------------|
| **Focus** | Tool connectivity | Agent collaboration | Organizational knowledge |
| **Content** | API schemas, function calls | Task delegation, status | Strategy, constraints, culture |
| **Answers** | "What can the AI call?" | "How do agents work together?" | "What should the AI consider?" |
| **Owner** | Engineers | Engineers | Product, Strategy, Teams |
| **Updates** | When tools change | When agents change | When organization changes |

**They're complementary, not competing.**
- **MCP** gives AI the *ability* to act (tools, data)
- **A2A** gives AI the *coordination* to collaborate (multi-agent)
- **ECS** gives AI the *wisdom* to act appropriately (context)

ECS includes a built-in [A2A integration](integrations/a2a/) so any A2A-enabled agent can query organizational context.

### Not Just Documentation

| Approach | Limitation | ECS Advantage |
|----------|------------|---------------|
| **System prompts** | Ad-hoc, duplicated across tools, not version-controlled | Standardized, single source of truth, git-tracked |
| **Knowledge bases** | Unstructured, don't capture relationships | Hierarchical, schema-validated, captures dependencies |
| **Config files** | Technical only | Captures business context, strategy, culture |
| **Wiki pages** | Too verbose for AI, quickly outdated | Concise, structured, clear ownership and update cycles |
| **Tribal knowledge** | Not accessible to AI | Codified, shareable, inheritable |

### Framework-Informed Structure

ECS incorporates concepts from four proven enterprise frameworks:

| Framework | Concepts Incorporated | AI Benefit |
|-----------|----------------------|------------|
| **Team Topologies** | Team types, interaction modes, cognitive load | Respects team boundaries, avoids overload |
| **Domain-Driven Design** | Bounded contexts, domain events, ubiquitous language | Uses correct terminology, designs integrations properly |
| **Enterprise Architecture** | Business capabilities, data ownership, architecture principles | Aligns with existing patterns, respects data ownership |
| **Organizational Design** | Risk appetite, funding model, change capacity | Calibrates recommendations appropriately |

---

## Enterprise Benefits

### 1. Consistency at Scale

Without ECS:
```
Agent A: "Migrate to AWS for cost savings"
Agent B: "Use Azure since it's your primary cloud"
Agent C: "Consider GCP for ML workloads"
→ Conflicting recommendations, wasted cycles
```

With ECS:
```yaml
technology_landscape:
  cloud: "Azure (primary), AWS (data platform)"
  constraints: "Must use existing identity provider (Okta)"
```
```
All agents: "Recommend Azure-native solutions using Okta SSO"
→ Consistent, aligned recommendations
```

### 2. Governance and Audit Trail

| Governance Need | ECS Solution |
|-----------------|--------------|
| **Version control** | Context files live in git with full history |
| **Clear ownership** | Company (Strategy), Division (PM Lead), Team (PM) |
| **Update cycles** | Company: Annual, Division: Quarterly, Team: As needed |
| **Change approval** | Standard code review process |
| **Compliance** | Schema validation ensures completeness |

### 3. Reduced Hallucination

AI agents hallucinate organizational facts because they lack authoritative sources:

| Without ECS | With ECS |
|-------------|----------|
| "Your budget is probably around $500K" | `budget: "$1.5M approved for FY25"` |
| "You should consider GDPR compliance" | `regulators: ["Central Bank", "FCA", "Data Protection Authority"]` |
| "The team can probably handle this" | `spare_capacity: "low — currently at capacity"` |

### 4. Faster AI Tool Adoption

When you adopt a new AI tool:

| Without ECS | With ECS |
|-------------|----------|
| Re-explain your organization | Load existing context files |
| Re-describe constraints | Constraints inherited automatically |
| Re-define terminology | Ubiquitous language available |

### 5. Cross-Agent Alignment

Multiple AI agents working on the same initiative:

| Agent | Uses ECS For |
|-------|--------------|
| **Research Agent** | Market constraints, competitive landscape, target users |
| **Strategy Agent** | Risk appetite, funding model, change capacity |
| **Architecture Agent** | Tech stack, architecture principles, ADRs |
| **PRD Agent** | Definition of Done, success metrics, team constraints |
| **Review Agent** | Quality gates, stakeholder requirements |

All agents share the same organizational understanding.

---

## Accelerating Agentic AI in Large Enterprises

### The Enterprise AI Adoption Challenge

Large enterprises struggle with AI adoption not because AI isn't capable, but because:

1. **Organizational complexity** — Hundreds of teams, thousands of constraints
2. **Regulatory burden** — Financial services, healthcare, aviation face strict oversight
3. **Change fatigue** — Multiple transformation programs competing for attention
4. **Institutional knowledge** — Critical context exists only in people's heads
5. **Coordination overhead** — AI suggestions must align across divisions

### How ECS Accelerates Adoption

| Challenge | ECS Solution |
|-----------|--------------|
| **Complexity** | Hierarchical context (Company → Division → Team) mirrors organizational structure |
| **Regulatory** | Explicit regulatory section with frameworks, data sensitivity, compliance stance |
| **Change fatigue** | Change capacity section prevents agents from suggesting too much at once |
| **Tribal knowledge** | Codifies institutional knowledge into shareable, version-controlled files |
| **Coordination** | Shared context ensures all AI agents work from same organizational truth |

### Enterprise-Specific Sections

ECS includes sections specifically designed for large enterprise needs:

| Section | Enterprise Need | Example Content |
|---------|-----------------|-----------------|
| **Risk Appetite** | Calibrate AI boldness | `regulatory: very_conservative` |
| **Funding Model** | Understand budget constraints | `approval_thresholds: { executive: $5M+ }` |
| **Change Capacity** | Prevent overload | `change_fatigue: high` |
| **Architecture Principles** | Respect existing patterns | `API-first, Cloud-native, Buy before build` |
| **Context Map** | Understand dependencies | `upstream: Core Banking, downstream: Finance` |
| **Cognitive Load Budget** | Respect team capacity | `overloaded_teams: [Platform, Payments]` |
| **Definition of Done** | Meet quality standards | `security_scan: required, accessibility: WCAG 2.1 AA` |

---

## The Problem

Every AI agent needs to understand your organization — strategy, tech stack, regulations, stakeholders. Today, every tool invents its own format. Context is copy-pasted, duplicated, and quickly outdated.

## The Solution

A simple, open specification for enterprise context files that any AI agent can consume:

```
company-context.md      →  Company-wide context (strategy, tech, regulations)
division-context.md     →  Business unit context (division OKRs, systems)
team-context.md         →  Team-level context (constraints, stakeholders)
```

Write once. Use everywhere.

## Quick Start

### 1. Copy a template

```bash
cp templates/company-context.md my-company-context.md
```

### 2. Fill it in

```markdown
---
schema: enterprise-context/v1/company
company: Acme Corp
industry: Financial Services
updated: 2025-03-01
---

# Company Context

## Strategic Priorities
- FY25 Strategy: Digital transformation, cost reduction
- Investment Themes: AI/ML, Cloud migration, Self-service
...
```

### 3. Use with any AI agent

```python
from enterprise_context import load_context, merge_contexts

# Load and merge your context
context = merge_contexts(
    load_context("company-context.md"),
    load_context("division-context.md")
)

# Include in your agent prompts
```

Works with any AI framework — LangChain, LlamaIndex, custom agents, or raw API calls.

## Why Use This?

| Benefit | Description |
|---------|-------------|
| **Write once** | Same context files work across multiple AI tools |
| **Clear ownership** | Company, Division, Team — different owners, different update cycles |
| **Version controlled** | Context files live in git, not in chat history |
| **Validated** | JSON Schema ensures your context is well-formed |
| **Human readable** | Markdown files anyone can edit |

## Specification

The spec defines three context levels with inheritance:

```
Company Context (required)
    │
    ├── Division Context (optional, extends company)
    │       │
    │       └── Team Context (optional, extends division)
```

Lower levels **extend** lists (OKRs, tech stack) and **override** scalars (compliance stance, primary contact).

See [spec/v1/README.md](spec/v1/README.md) for the full specification.

## File Formats

We support two formats:

| Format | Best For | Extension |
|--------|----------|-----------|
| **Markdown + YAML frontmatter** | Human editing, documentation | `.md` |
| **Pure YAML** | Automation, CI/CD | `.yaml` |

Both are equivalent and convertible via the CLI tools.

## Directory Structure

```
enterprise-context-spec/
├── spec/v1/                    # Schema definitions
│   ├── README.md               # Full specification with field reference
│   ├── company.schema.json     # Company-level schema (7 sections)
│   ├── division.schema.json    # Division-level schema (6 sections)
│   └── team.schema.json        # Team-level schema (6 sections)
├── templates/                  # Ready-to-use templates
│   ├── company-context.md      # Company template with guidance
│   ├── division-context.md     # Division template with guidance
│   └── team-context.md         # Team template with guidance
├── examples/                   # Industry examples
│   ├── enterprise/             # Financial Services (Banking)
│   │   ├── company-context.md
│   │   ├── operations-division-context.md
│   │   └── customer-portal-team-context.md
│   ├── insurance/              # General Insurance (Claims)
│   │   ├── company-context.md
│   │   ├── claims-division-context.md
│   │   └── motor-claims-team-context.md
│   ├── fintech/
│   └── saas/
├── tools/                      # CLI tools
│   ├── validate.py             # Schema validation
│   └── merge.py                # Context merging with inheritance
└── integrations/               # Agent integrations
    ├── a2a/                    # Google A2A protocol server
    │   ├── server.py           # A2A-compliant server
    │   └── agent_card.json     # Agent discovery card
    ├── langchain/              # LangChain document loader
    └── seedcraft/              # Seedcraft integration
```

## Installation

```bash
# Install from PyPI (when published)
pip install enterprise-context

# Or install from source
git clone https://github.com/enterprise-context/enterprise-context-spec.git
cd enterprise-context-spec
pip install -e .
```

Or just copy the templates — no installation required for basic use.

## CLI Usage

```bash
# Validate a context file
ec validate company-context.md

# Merge company + division + team into single context
ec merge company.md division.md team.md -o merged-context.json

# Convert between formats
ec convert company-context.md -o company-context.yaml
```

## Integrations

### Python Package (Core)

```python
from enterprise_context import load_context, merge_contexts

# Load context files
company = load_context("company-context.md")
division = load_context("division-context.md")
team = load_context("team-context.md")

# Merge with inheritance (company <- division <- team)
context = merge_contexts(company, division, team)

# Use context in your agent prompts
```

### Google A2A (Agent-to-Agent)

Expose enterprise context as an A2A-compliant service for multi-agent systems:

```bash
# Start the A2A server
python integrations/a2a/server.py --context-dir ./context --port 8080
```

```python
from a2a_sdk import A2AClient

client = A2AClient("http://localhost:8080")

# Query context from any A2A-enabled agent
response = await client.send_task({
    "skill": "get_context",
    "input": {"level": "team", "team": "Customer Portal"}
})

# Check constraints before taking action
response = await client.send_task({
    "skill": "check_constraints",
    "input": {"action": "Deploy ML model", "team": "Customer Portal"}
})
```

See [integrations/a2a/README.md](integrations/a2a/README.md) for full documentation.

### LangChain (Coming Soon)

> **Note:** Direct LangChain integration is planned. See [integrations/langchain/README.md](integrations/langchain/README.md) for current workarounds.

### Seedcraft (Coming Soon)

> **Note:** Direct Seedcraft SDK integration is planned. See [integrations/seedcraft/README.md](integrations/seedcraft/README.md) for current workarounds.

## Comparison Matrix

| Feature | System Prompts | Wiki/Confluence | ECS |
|---------|----------------|-----------------|-----|
| Structured schema | ❌ | ❌ | ✅ |
| Version controlled | ❌ | ⚠️ | ✅ |
| Clear ownership | ❌ | ⚠️ | ✅ |
| Hierarchical inheritance | ❌ | ❌ | ✅ |
| Machine-parseable | ⚠️ | ❌ | ✅ |
| Human-readable | ✅ | ✅ | ✅ |
| Validation | ❌ | ❌ | ✅ |
| Cross-tool reusability | ❌ | ❌ | ✅ |
| Framework-informed | ❌ | ❌ | ✅ |

---

## Framework Foundations

Enterprise Context Spec incorporates best practices from:

### Team Topologies (Skelton & Pais)
- **Team Types**: stream-aligned, platform, enabling, complicated-subsystem
- **Interaction Modes**: collaboration, x-as-a-service, facilitating
- **Cognitive Load**: capacity management and team boundaries

### Domain-Driven Design (Evans)
- **Domain Classification**: core (build), supporting (configure), generic (buy)
- **Context Map**: upstream/downstream relationships
- **Bounded Contexts**: clear domain boundaries
- **Ubiquitous Language**: consistent terminology

### Enterprise Architecture
- **Business Capabilities**: maturity and investment priority
- **Data Architecture**: golden sources, ownership, governance
- **Architecture Principles**: design guidelines that constrain decisions
- **Architecture Decision Records**: documented decisions with context

### Organizational Design
- **Risk Appetite**: calibration across technology, market, regulatory dimensions
- **Funding Model**: project vs product funding, approval thresholds
- **Change Capacity**: organizational ability to absorb change
- **Definition of Done**: quality criteria at story, feature, release levels

---

## Acknowledgments

### Frameworks and Thought Leaders
- **Team Topologies** — Matthew Skelton and Manuel Pais
- **Domain-Driven Design** — Eric Evans
- **Continuous Discovery Habits** — Teresa Torres
- **Demand-Side Sales** — Bob Moesta
- **Inspired/Empowered** — Marty Cagan
- **Enterprise Architecture** patterns from TOGAF and Zachman

### Development
This specification was developed alongside [Seedcraft](https://github.com/...) — an AI-powered product discovery system that demonstrated the need for structured organizational context.

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to contribute:
- **Industry templates** — Add examples for your industry (banking, healthcare, aviation)
- **Integrations** — Connect to more AI tools (Claude Code, Cursor, Copilot)
- **Schema improvements** — Propose new fields or refinements
- **Documentation** — Improve guides and examples
- **Translations** — Localize templates for different regions

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Get Started

```bash
# Clone the repo
git clone https://github.com/enterprise-context/enterprise-context-spec.git
cd enterprise-context-spec

# Install the package
pip install -e .

# Copy templates to your project
cp templates/*.md ~/your-project/context/

# Fill in your organizational context
# Start with company-context.md, then add division and team as needed

# Validate your context files
ec validate ~/your-project/context/*.md

# Merge contexts for use with AI
ec merge ~/your-project/context/*.md -o merged.json
```

---

**Enterprise Context Spec — The missing layer between AI agents and enterprise reality.**

*Built for banks, insurers, airlines, and any organization where AI agents need to respect the complexity of enterprise operations.*
