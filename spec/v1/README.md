# Enterprise Context Spec v1

This document defines version 1.0 of the Enterprise Context Specification.

## Overview

The specification defines three context levels:

| Level | File | Required | Owner | Update Frequency |
|-------|------|----------|-------|------------------|
| **Company** | `company-context.md` | Yes | Strategy / Transformation | Annually |
| **Division** | `division-context.md` | No | Division Head / PM Lead | Quarterly |
| **Team** | `team-context.md` | No | Product Manager | As needed |

## Inheritance Model

Lower levels inherit from higher levels:

```
Company Context (base)
    │
    ├── Division Context (extends company)
    │       │
    │       └── Team Context (extends division)
```

### Inheritance Rules

| Field Type | Behavior |
|------------|----------|
| **Scalars** (strings, numbers) | Lower level overrides higher |
| **Lists** (arrays) | Lower level extends higher (concatenation) |
| **Objects** | Deep merge with lower level taking precedence |

### Example

```yaml
# Company
tech_stack: [Guidewire, SAP]
compliance_stance: conservative

# Division
tech_stack: [React, Azure Functions]  # Extends → [Guidewire, SAP, React, Azure Functions]
compliance_stance: moderate            # Overrides → moderate

# Team
tech_stack: [Jest, Playwright]         # Extends → [Guidewire, SAP, React, Azure Functions, Jest, Playwright]
```

## File Format

### Markdown with YAML Frontmatter (Recommended)

```markdown
---
schema: enterprise-context/v1/company
company: Acme Corp
industry: Financial Services
updated: 2025-03-01
owner: strategy-team@acme.com
---

# Company Context

## Strategic Priorities
...
```

### Pure YAML

```yaml
schema: enterprise-context/v1/company
company: Acme Corp
industry: Financial Services
updated: 2025-03-01
owner: strategy-team@acme.com

strategic_priorities:
  current_strategy: Digital transformation
  okrs:
    - Reduce costs by 20%
...
```

## Schema Files

- [company.schema.json](company.schema.json) — Company-level context
- [division.schema.json](division.schema.json) — Division-level context
- [team.schema.json](team.schema.json) — Team-level context

## Field Reference

### Company Context

| Section | Fields | Source Framework | Description |
|---------|--------|------------------|-------------|
| **Identity** | company, industry, business_units, size, geography | — | Who you are |
| **Strategy** | current_strategy, okrs, investment_themes, constraints | — | Where you're going |
| **Business Capabilities** | capability map with maturity and investment priority | Enterprise Architecture | What capabilities exist and their investment focus |
| **Technology** | core_systems, cloud, platforms, integration_approach, tech_debt | — | How you build |
| **Data Architecture** | golden_sources, data_domains, data_governance, data_platform | Enterprise Architecture | Where data lives and who owns it |
| **Regulatory** | regulators, frameworks, compliance_stance, data_sensitivity, data_residency | — | How you comply |
| **Risk Appetite** | technology, market, regulatory, innovation, operational risk levels | Organisational Design | How bold to be in recommendations |
| **Funding Model** | type, budget_cycle, capex_opex, approval_thresholds | Organisational Design | How initiatives get funded |
| **Change Capacity** | initiatives_in_flight, change_fatigue, adoption_support, blackout_periods | Organisational Design | Capacity for change |
| **Organization** | sponsors, product_leadership, delivery_model, decision_forums, gate_approvers | — | How you decide |
| **Architecture Principles** | principles with statements, rationale, implications | Enterprise Architecture | Design principles that guide decisions |
| **Competition** | primary_competitors, disruptors, differentiators, market_position | — | Who you compete with |
| **Ubiquitous Language** | domain terms and definitions | Domain-Driven Design | Consistent terminology |

### Division Context

| Section | Fields | Source Framework | Description |
|---------|--------|------------------|-------------|
| **Identity** | division, business_unit, head, size, purpose | — | Which division |
| **Strategy** | division_okrs, priorities, constraints | — | Division goals |
| **Domain Classification** | type (core/supporting/generic), rationale, bounded_contexts | Domain-Driven Design | Build vs buy guidance |
| **Context Map** | upstream, downstream, shared_kernel, partnership relationships | Domain-Driven Design | Integration relationships |
| **Team Topology** | stream_aligned, platform, enabling, complicated_subsystem teams | Team Topologies | Team structure |
| **Cognitive Load Budget** | total_teams, services_owned, overloaded_teams, capacity | Team Topologies | Division capacity |
| **Technology** | division_systems, integrations, tech_stack | — | Division tech |
| **Data Ownership** | data domains owned vs consumed, stewards, sensitivity | Enterprise Architecture | Data governance |
| **Architecture Decisions** | ADRs with context, decision, consequences | Enterprise Architecture | Key decisions that constrain work |
| **Regulatory** | additional_frameworks, data_sensitivity, compliance_requirements | — | Division compliance |
| **Stakeholders** | executive_sponsor, decision_forum, gate_approver, key_stakeholders | — | Division governance |
| **Metrics** | division KPIs with current and target values | — | Division performance |

### Team Context

| Section | Fields | Source Framework | Description |
|---------|--------|------------------|-------------|
| **Identity** | team, product_area, pm, tech_lead, type, value_stream | Team Topologies | Which team |
| **Team Interactions** | interaction mode per team (collaboration, x-as-a-service, facilitating) | Team Topologies | How team interacts with others |
| **API/Service Ownership** | APIs/services owned and consumed, SLAs, fallbacks | Team Topologies | Clear boundaries |
| **Cognitive Load** | velocity, services_owned, tech_debt, on_call, spare_capacity | Team Topologies | Team bandwidth |
| **Current State** | existing_solution, known_issues, metrics, previous_attempts | — | Where you are |
| **Domain Events** | events produced and consumed, schemas, consumers | Domain-Driven Design | Event-driven design |
| **Constraints** | technical, timeline, budget, dependencies | — | What limits you |
| **Definition of Done** | story, feature, release level criteria, quality gates | Organisational Design | What "done" means |
| **Stakeholders** | immediate_stakeholders, impacted_teams | — | Who's involved |
| **Success Metrics Ownership** | metrics owned vs influenced, measurement | Organisational Design | Accountability |
| **Users** | primary, secondary users, sophistication, pain_points | — | Who you serve |

## Framework Sources

This specification incorporates concepts from four key frameworks:

### Team Topologies (Skelton & Pais)

- **Team Types**: stream-aligned, platform, enabling, complicated-subsystem
- **Interaction Modes**: collaboration, x-as-a-service, facilitating
- **Cognitive Load**: capacity management and team boundaries

### Domain-Driven Design (Evans)

- **Domain Classification**: core (competitive advantage), supporting, generic (COTS)
- **Context Map**: upstream/downstream relationships, integration patterns
- **Bounded Contexts**: clear domain boundaries
- **Domain Events**: events produced and consumed
- **Ubiquitous Language**: consistent domain terminology

### Enterprise Architecture

- **Business Capabilities**: maturity and investment priority
- **Data Architecture**: golden sources, ownership, governance
- **Architecture Principles**: design guidelines
- **Architecture Decision Records**: documented decisions

### Organisational Design

- **Risk Appetite**: how bold to be across dimensions
- **Funding Model**: how initiatives get funded
- **Change Capacity**: ability to absorb change
- **Definition of Done**: quality criteria
- **Success Metrics Ownership**: accountability for metrics

## Validation

Use the CLI to validate context files:

```bash
ec validate company-context.md
ec validate --schema division division-context.md
```

## Versioning

The spec follows semantic versioning:

- **Major** (v2.0) — Breaking changes to schema
- **Minor** (v1.1) — New optional fields
- **Patch** (v1.0.1) — Documentation fixes

Files should declare their schema version in frontmatter:

```yaml
schema: enterprise-context/v1/company
```

## Why These Sections Matter for AI Agents

Each new section provides context that improves AI agent outputs:

| Section | AI Benefit |
|---------|------------|
| **Business Capabilities** | Prevents suggesting capabilities that already exist; focuses on gaps |
| **Data Architecture** | Designs integrations that respect data ownership and sources |
| **Risk Appetite** | Calibrates recommendations (conservative vs aggressive) |
| **Funding Model** | Understands budget constraints and approval processes |
| **Change Capacity** | Avoids recommending too much change at once |
| **Architecture Principles** | Ensures recommendations align with established patterns |
| **Ubiquitous Language** | Uses correct domain terminology consistently |
| **Domain Classification** | Recommends build vs buy appropriately |
| **Context Map** | Designs integrations that respect relationships |
| **Team Topology** | Understands team capabilities and types |
| **Cognitive Load Budget** | Avoids overloading teams |
| **Team Interactions** | Understands collaboration needs |
| **API Ownership** | Designs within team boundaries |
| **Domain Events** | Supports event-driven architecture |
| **Definition of Done** | Writes appropriate acceptance criteria |
| **Success Metrics Ownership** | Writes metrics teams can actually own |
