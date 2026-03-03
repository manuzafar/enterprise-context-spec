---
schema: enterprise-context/v1/division
division: "[Division Name]"
business_unit: "[Parent Business Unit]"
updated: "YYYY-MM-DD"
owner: "[division-lead@company.com]"
---

# Division Context

This document provides division-level context that extends the company context. It should be updated quarterly or after divisional reorganisations.

---

## Division Identity

- **Division**: [e.g., Claims, Personal Lines, Commercial, Digital]
- **Business Unit**: [e.g., Operations, Customer, Product]
- **Division Head**: [e.g., Sarah Mitchell, Chief Claims Officer]
- **Division Size**: [e.g., 450 employees, 12 teams]
- **Purpose**: [e.g., Deliver fast, fair claims outcomes that build customer trust]

---

## Division Strategy

- **Division OKRs**:
  - Objective: [e.g., Reduce claims processing time]
    - KR1: [e.g., Average claim settlement from 14 days to 8 days]
    - KR2: [e.g., First-touch resolution rate from 45% to 70%]
  - Objective: [e.g., Improve customer satisfaction]
    - KR1: [e.g., Claims NPS from -12 to +20]
    - KR2: [e.g., Reduce complaints by 30%]

- **Current Priorities**:
  - [e.g., Claims portal modernisation]
  - [e.g., Automation of low-complexity claims]
  - [e.g., Fraud detection enhancement]

- **Division Constraints**:
  - [e.g., Must maintain 24-hour SLA for new claims]
  - [e.g., Cannot reduce assessor headcount until automation proven]

---

## Domain Classification

*Classify your domain using Domain-Driven Design principles. This helps AI understand whether to recommend custom solutions or COTS.*

- **Domain Type**: [Core / Supporting / Generic]
  - **Core**: Competitive differentiator — build custom, invest heavily
  - **Supporting**: Necessary but not differentiating — configurable solutions
  - **Generic**: Commodity — buy COTS/SaaS

- **Rationale**: [e.g., Claims handling is our competitive differentiator; speed and fairness drive NPS and retention]

- **Bounded Contexts**:
  - [e.g., Claims Lodgement — receiving and recording new claims]
  - [e.g., Claims Assessment — evaluating and approving claims]
  - [e.g., Claims Payment — processing payouts]
  - [e.g., Fraud Detection — identifying suspicious claims]

- **Subdomain Focus**: [e.g., Claims Lodgement is the priority subdomain for this year]

---

## Context Map

*Document how this division relates to other contexts using DDD patterns. This helps AI understand integration constraints.*

### Upstream Dependencies (We Depend On)

| Context | Relationship | Integration | Owner |
|---------|--------------|-------------|-------|
| [Policy Admin] | [customer-supplier] | [API] | [Personal Lines] |
| [Customer Master] | [conformist] | [events] | [Customer Data Team] |
| [Identity] | [open-host-service] | [API] | [Platform] |

### Downstream Consumers (Depend On Us)

| Context | Relationship | Integration | Consumer |
|---------|--------------|-------------|----------|
| [Finance] | [customer-supplier] | [events] | [Finance Division] |
| [Reinsurance] | [customer-supplier] | [batch] | [Risk Team] |
| [Reporting] | [conformist] | [events] | [Analytics Team] |

- **Shared Kernel**: [e.g., Document Management — shared model for attachments]
- **Partnership**: [e.g., Customer Experience team — joint ownership of journey]

**Relationship Types**:
- **customer-supplier**: We request features, they deliver
- **conformist**: We conform to their model
- **anticorruption-layer**: We translate their model
- **open-host-service**: They expose a standard API
- **published-language**: Shared language/schema

---

## Team Topology

*Map your teams using Team Topologies patterns. This helps AI understand team structures and capabilities.*

### Stream-Aligned Teams

| Team | Focus | Value Stream |
|------|-------|--------------|
| [Claims Lodgement] | [Customer-facing lodgement experience] | [Claims Journey] |
| [Claims Assessment] | [Assessor tools and workflow] | [Claims Journey] |
| [Motor Claims] | [End-to-end motor claims] | [Motor Claims] |
| [Home Claims] | [End-to-end home claims] | [Home Claims] |

### Platform Teams

| Team | Focus | Services Provided |
|------|-------|-------------------|
| [Claims Platform] | [ClaimCenter APIs and integrations] | [ClaimCenter API, Document Storage, Notifications] |

### Enabling Teams

| Team | Focus | Capabilities Enabled |
|------|-------|---------------------|
| [Claims Analytics] | [Data, reporting, ML models] | [Fraud detection models, reporting dashboards, data pipelines] |

### Complicated Subsystem Teams

| Team | Focus | Specialist Domain |
|------|-------|-------------------|
| [Fraud ML] | [Machine learning models for fraud] | [ML/AI, fraud patterns] |

---

## Cognitive Load Budget

*Assess your division's cognitive load. This helps AI avoid recommending work that exceeds capacity.*

- **Total Teams**: [e.g., 12]
- **Total Services Owned**: [e.g., 28]
- **Average Services per Team**: [e.g., 2.3 — target is 2-3]
- **Capacity for New Work**: [None / Limited / Moderate / High]

- **Overloaded Teams**:
  - [e.g., Claims Platform — owns 6 services, on-call burden high]
  - [e.g., Motor Claims — supporting legacy and new systems]

- **Load Reduction Initiatives**:
  - [e.g., Platform investment to reduce stream-aligned team burden]
  - [e.g., Splitting Claims Platform into Core and Integration teams]

---

## Division Technology

- **Core Systems**:
  - [e.g., Guidewire ClaimCenter (claims management)]
  - [e.g., Friss (fraud detection)]
  - [e.g., Verisk (repair estimating)]
  - [e.g., Symbility (property claims)]

- **Key Integrations**:
  - [e.g., Policy Admin System (PolicyCenter) — policy lookup, coverage verification]
  - [e.g., Payment Gateway (Monoova) — claim payouts, EFT]
  - [e.g., Document Management (SharePoint) — claim attachments]
  - [e.g., Identity Provider (Okta) — customer and assessor authentication]

- **Division Tech Stack**: [e.g., React (customer portal), Azure Functions (backend APIs), Azure SQL (operational data), Power BI (reporting)]

---

## Data Ownership

*Clarify which data domains this division owns vs consumes. This helps AI understand data governance.*

### Data We Own

| Domain | System of Record | Data Steward | Sensitivity |
|--------|------------------|--------------|-------------|
| [Claims] | [Guidewire ClaimCenter] | [James Wong] | [Confidential] |
| [Fraud Indicators] | [Friss] | [Fraud Team Lead] | [Restricted] |
| [Repair Estimates] | [Verisk] | [Assessment Lead] | [Internal] |

### Data We Consume

| Domain | Source System | Owner | Refresh Frequency |
|--------|---------------|-------|-------------------|
| [Policy] | [PolicyCenter] | [Personal Lines] | [Real-time] |
| [Customer] | [Salesforce] | [Customer Team] | [Real-time] |
| [Payment Status] | [Monoova] | [Finance] | [Near real-time] |

---

## Architecture Decisions

*Document key Architecture Decision Records (ADRs) that constrain future work.*

### ADR-001: Use ClaimCenter as Claims System of Record

- **Status**: Accepted
- **Date**: 2023-06-15
- **Context**: Needed to consolidate claims data across legacy systems
- **Decision**: All claims data flows through Guidewire ClaimCenter; no direct database writes from other systems
- **Consequences**:
  - All integrations must use ClaimCenter APIs
  - Real-time requirements need event-driven patterns
  - No bypass for "quick" fixes

### ADR-002: Event-Driven Integration for Downstream Consumers

- **Status**: Accepted
- **Date**: 2024-01-10
- **Context**: Finance and Reinsurance need claim data but shouldn't couple to ClaimCenter
- **Decision**: Publish domain events for claim lifecycle changes; consumers subscribe to events
- **Consequences**:
  - Must define and maintain event schemas
  - Eventual consistency accepted
  - Need event replay for new consumers

---

## Division Regulatory

- **Additional Frameworks**:
  - [e.g., General Insurance Code of Practice 2020 (claims handling timeframes)]
  - [e.g., ASIC RG 271 (complaints handling — 45 day resolution)]
  - [e.g., AFCA (external dispute resolution)]

- **Data Sensitivity**:
  - [e.g., Medical records (injury claims)]
  - [e.g., Photos of property damage]
  - [e.g., Financial details (bank accounts for payouts)]
  - [e.g., Witness statements]

- **Compliance Requirements**:
  - [e.g., 10-year claim record retention]
  - [e.g., Audit trail for all claim decisions]
  - [e.g., 45-day complaint resolution requirement]

---

## Division Stakeholders

- **Executive Sponsor**: [e.g., Sarah Mitchell, Chief Claims Officer]
- **Decision Forum**: [e.g., Claims Leadership Team (CLT) — meets weekly Wednesday 9am]
- **Gate Approver**: [e.g., James Wong (Head of Claims Ops) for L0-L2, Sarah Mitchell for L3+]

| Name | Role | Interest |
|------|------|----------|
| [James Wong] | [Head of Claims Ops] | [Operational efficiency, assessor capacity] |
| [Michael Chen] | [CTO] | [Technical feasibility, platform alignment] |
| [Lisa Park] | [CFO] | [Investment justification, ROI] |
| [David Lee] | [Head of Customer Service] | [Call deflection, customer experience] |

---

## Division Metrics

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| [Average claim settlement time] | [14 days] | [8 days] | [↓ improving] |
| [Claims NPS] | [-12] | [+20] | [→ flat] |
| [First-touch resolution] | [45%] | [70%] | [↑ improving] |
| [Cost per claim] | [$847] | [$600] | [→ flat] |
| [Digital lodgement rate] | [34%] | [60%] | [↑ improving] |

---

## How to Maintain This Document

- **Review Frequency**: Update quarterly or after divisional reorg
- **Owner**: [Division PM Lead or Division Head]
- **Last Updated**: [Date]

### Tips for Quality Context

1. **Classify your domain honestly** — Not everything is "core"; generic domains should use COTS
2. **Map your relationships** — Understanding upstream/downstream helps AI design integrations correctly
3. **Know your cognitive load** — Overloaded teams can't take on more work
4. **Document key ADRs** — Past decisions constrain future options
