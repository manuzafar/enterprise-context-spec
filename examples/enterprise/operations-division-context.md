---
schema: enterprise-context/v1/division
division: "Operations"
business_unit: "Customer Operations"
updated: "2025-03-01"
owner: "james.wong@acmecorp.com"
---

# Operations Division Context

## Division Identity

- **Division**: Operations
- **Business Unit**: Customer Operations
- **Division Head**: Sarah Mitchell, Chief Operating Officer
- **Division Size**: 650 employees, 15 teams
- **Purpose**: Deliver fast, accurate customer service and transaction processing that builds trust and drives efficiency

---

## Division Strategy

- **Division OKRs**:
  - Objective: Reduce case processing time
    - KR1: Average case resolution from 5 days to 1 day
    - KR2: First-touch resolution rate from 45% to 70%
    - KR3: Straight-through processing for routine cases to 60%
  - Objective: Improve customer satisfaction
    - KR1: Operations NPS from +15 to +45
    - KR2: Reduce complaints by 40%
    - KR3: Real-time status updates for 100% of cases
  - Objective: Reduce operational costs
    - KR1: Cost per case from $85 to $50
    - KR2: Fraud detection rate from 2% to 4%

- **Current Priorities**:
  1. Customer portal modernisation (self-service)
  2. Automation of routine transactions
  3. Fraud detection enhancement (ML models)
  4. Case worker mobile app
  5. Real-time case status notifications

- **Division Constraints**:
  - Must maintain 24-hour SLA for acknowledging new cases
  - Cannot reduce operations headcount until automation proves stable
  - Must integrate with existing core banking platform (no platform change)
  - End of year code freeze (December peak)

---

## Domain Classification

- **Domain Type**: Core
- **Rationale**: Operations handling is our competitive differentiator. Speed and accuracy of case resolution directly drive NPS, retention, and brand reputation. Customers choose providers based on service experience. This must be custom-built and continuously improved.

- **Bounded Contexts**:
  - **Case Intake**: Receiving and recording new cases from all channels (web, mobile, phone, branch)
  - **Case Processing**: Evaluating case validity and completing required actions
  - **Payment Processing**: Processing payments, transfers, and settlements
  - **Fraud Detection**: Identifying suspicious transactions using rules and ML
  - **Partner Management**: Managing relationships with third-party service providers

- **Subdomain Focus**: Case Intake and Self-Service is the priority subdomain for FY25 — this is where we lose customers

---

## Context Map

### Upstream Dependencies (We Depend On)

| Context | Relationship | Integration | Owner |
|---------|--------------|-------------|-------|
| Account Management (Core Banking) | customer-supplier | API | Retail Banking |
| Customer Master (Salesforce) | conformist | events | Customer Data Team |
| Identity (Okta) | open-host-service | API | Platform |
| Document Management (SharePoint) | open-host-service | API | Platform |

### Downstream Consumers (Depend On Us)

| Context | Relationship | Integration | Consumer |
|---------|--------------|-------------|----------|
| Finance (SAP) | customer-supplier | events | Finance Division |
| Risk & Compliance | customer-supplier | batch | Risk Team |
| Analytics (Snowflake) | conformist | events | Data Team |
| Customer Service | conformist | events | Contact Centre |
| Partner Portal | customer-supplier | API | Digital Division |

- **Shared Kernel**: Document Management — shared model for attachments and correspondence
- **Partnership**: Customer Experience team — joint ownership of customer journey

---

## Team Topology

### Stream-Aligned Teams

| Team | Focus | Value Stream |
|------|-------|--------------|
| Customer Portal | Customer-facing self-service experience | Customer Journey |
| Case Management | Case worker tools and workflow | Operations Journey |
| Payments | End-to-end payment processing | Payment Journey |
| Disputes | Dispute and complaint handling | Dispute Journey |
| Partner Services | Partner network and integrations | Partner Journey |

### Platform Teams

| Team | Focus | Services Provided |
|------|-------|-------------------|
| Operations Platform | Core banking APIs and integrations | Core APIs, Document Storage, Notifications, Event Bus |

### Enabling Teams

| Team | Focus | Capabilities Enabled |
|------|-------|---------------------|
| Operations Analytics | Data, reporting, ML models | Fraud detection models, reporting dashboards, data pipelines |

### Complicated Subsystem Teams

| Team | Focus | Specialist Domain |
|------|-------|-------------------|
| Fraud ML | Machine learning models for fraud | ML/AI, fraud patterns, model training |

---

## Cognitive Load Budget

- **Total Teams**: 15
- **Total Services Owned**: 35
- **Average Services per Team**: 2.3 (within target of 2-3)
- **Capacity for New Work**: Limited — most teams at capacity

- **Overloaded Teams**:
  - Operations Platform — owns 7 services, high on-call burden, single point of failure for core banking expertise
  - Payments — supporting legacy and new systems simultaneously, context switching overhead

- **Load Reduction Initiatives**:
  - Platform investment to reduce stream-aligned team burden (FY25)
  - Splitting Operations Platform into Core and Integration teams (planned Q3)
  - Decommissioning legacy portal after new self-service goes live

---

## Division Technology

- **Core Systems**:
  - Core Banking Platform (case and transaction management)
  - Pega (workflow automation)
  - NICE (contact centre)
  - Actimize (fraud detection)

- **Key Integrations**:
  - Core Banking Platform — account lookup, transaction processing
  - Payment Gateway — payment processing, EFT
  - Document Management (SharePoint) — case attachments, correspondence
  - Identity Provider (Okta) — customer and staff authentication
  - SMS Gateway (Twilio) — status notifications
  - Partner Network — third-party service providers

- **Division Tech Stack**: React (customer portal), Azure Functions (backend APIs), Azure SQL (operational data), Power BI (reporting)

---

## Data Ownership

### Data We Own

| Domain | System of Record | Data Steward | Sensitivity |
|--------|------------------|--------------|-------------|
| Cases | Core Banking Platform | James Wong | Confidential |
| Fraud Indicators | Actimize | Fraud Team Lead | Restricted |
| Workflow State | Pega | Operations Lead | Internal |
| Partner Performance | Internal DB | Partner Manager | Internal |

### Data We Consume

| Domain | Source System | Owner | Refresh Frequency |
|--------|---------------|-------|-------------------|
| Account | Core Banking | Retail Banking | Real-time (API) |
| Customer | Salesforce | Customer Team | Real-time (events) |
| Payment Status | Payment Gateway | Finance | Near real-time (webhooks) |
| Credit Data | Bureau | External | On-demand (API) |

---

## Architecture Decisions

### ADR-001: Use Core Banking as System of Record for Cases

- **Status**: Accepted
- **Date**: 2023-06-15
- **Context**: Case data was fragmented across legacy systems, leading to inconsistencies and data quality issues. Needed a single source of truth.
- **Decision**: All case data flows through the core banking platform. No direct database writes from external systems. All integrations use platform APIs.
- **Consequences**:
  - All integrations must use platform APIs (REST or events)
  - Real-time requirements need event-driven patterns
  - No bypass for "quick" fixes — all changes go through the platform
  - Dependency on core platform team for changes

### ADR-002: Event-Driven Integration for Downstream Consumers

- **Status**: Accepted
- **Date**: 2024-01-10
- **Context**: Finance, Risk, and Analytics need case data but shouldn't couple directly to core banking. Need loose coupling and real-time updates.
- **Decision**: Publish domain events for case lifecycle changes (CaseCreated, CaseUpdated, CaseResolved, etc.). Consumers subscribe to events rather than polling APIs.
- **Consequences**:
  - Must define and maintain event schemas (versioned)
  - Eventual consistency is accepted (not immediate)
  - Need event replay capability for new consumers
  - Need dead-letter handling for failed events

### ADR-003: Mobile-First for Customer Self-Service

- **Status**: Accepted
- **Date**: 2024-09-01
- **Context**: 65% of self-service traffic is mobile, but mobile abandonment is 52%. Desktop-first design is failing customers.
- **Decision**: New customer portal will be designed mobile-first with progressive enhancement for desktop. Touch targets, single-column layouts, minimal form fields.
- **Consequences**:
  - Design reviews start with mobile mockups
  - Performance budget of 3 seconds on 3G
  - Document upload optimised for mobile cameras
  - Desktop experience may feel "spacious" but that's acceptable

---

## Division Regulatory

- **Additional Frameworks**:
  - Consumer protection regulations
  - Complaints handling requirements (regulatory timeframes)
  - External dispute resolution requirements
  - Privacy regulations (data handling)

- **Data Sensitivity**:
  - Financial records (account statements, transactions)
  - Identity documents
  - Financial details (account numbers for processing)
  - Correspondence and case notes
  - Voice recordings (service calls)

- **Compliance Requirements**:
  - 7-year case record retention
  - Audit trail for all case decisions
  - Regulatory complaint resolution timeframes
  - Response time SLAs
  - Vulnerable customer identification and support

---

## Division Stakeholders

- **Executive Sponsor**: Sarah Mitchell, Chief Operating Officer
- **Decision Forum**: Operations Leadership Team (OLT) — meets weekly Wednesday 9am
- **Gate Approver**: James Wong (Head of Operations) for L0-L2, Sarah Mitchell for L3+

| Name | Role | Interest |
|------|------|----------|
| James Wong | Head of Operations | Operational efficiency, staff capacity, SLAs |
| Michael Chen | CTO | Technical feasibility, platform alignment, security |
| Lisa Park | CFO | Investment justification, ROI, operational costs |
| David Lee | Head of Customer Service | Call deflection, customer experience, NPS |
| Emma Smith | Operations Team Lead | Quality cases, reduced rework, tools |
| Tom Brown | Platform Architect | Integration patterns, API design, scalability |
| Rachel Green | Compliance Manager | Regulatory adherence, audit readiness |

---

## Division Metrics

| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| Average case resolution time | 5 days | 1 day | ↓ improving |
| Operations NPS | +15 | +45 | → flat |
| First-touch resolution | 45% | 70% | ↑ improving |
| Cost per case | $85 | $50 | → flat |
| Digital self-service rate | 38% | 70% | ↑ improving |
| Straight-through processing | 25% | 60% | → flat |
| Fraud detection rate | 2.1% | 4% | ↑ improving |
| Complaint volumes | 1,800/month | 1,000/month | → flat |

---

## Maintenance

- **Review Frequency**: Quarterly (aligned with OKR cycles)
- **Owner**: James Wong, Head of Operations
- **Last Updated**: 2025-03-01
