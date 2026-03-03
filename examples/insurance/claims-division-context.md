---
schema: enterprise-context/v1/division
division: "Claims"
business_unit: "Operations"
updated: "2025-03-01"
owner: "claims-product@protectorinsurance.com"
---

# Claims Division Context

## Division Identity

- **Division**: Claims
- **Business Unit**: Operations
- **Division Head**: Sarah Mitchell, Chief Claims Officer
- **Size**: 2,200 employees, 18 product/engineering teams
- **Purpose**: Deliver fast, fair, and empathetic claims experiences that exceed customer expectations while maintaining cost discipline

---

## Strategic Priorities

- **Division OKRs** (extending company OKRs):
  - Objective: Automate simple claims end-to-end
    - KR1: Achieve 70% STP for motor glass claims
    - KR2: Achieve 50% STP for motor single-vehicle claims under $5K
    - KR3: Reduce manual touchpoints per claim from 8 to 3
  - Objective: Improve claims team efficiency
    - KR1: Increase claims per FTE from 120 to 180 per month
    - KR2: Reduce average handling time by 30%
    - KR3: Implement AI-assisted assessment for 80% of motor claims

- **Priorities**:
  - Q1-Q2: Motor claims automation
  - Q3-Q4: Property claims digitisation
  - Ongoing: Fraud detection enhancement

- **Constraints**:
  - Must maintain regulatory compliance for claims handling
  - Cannot reduce headcount until automation proven
  - Must support catastrophe surge capacity

---

## Domain Classification (DDD)

- **Type**: Core
- **Rationale**: Claims experience is our primary differentiator. Fast, fair claims directly impacts retention and NPS. This is where we compete.
- **Bounded Contexts**:
  - Lodgement (FNOL capture, triage)
  - Assessment (liability, quantum, coverage)
  - Settlement (payment, recovery, finalisation)
  - Fraud (detection, investigation)
- **Subdomain Focus**: Motor claims (60% of volume, highest automation potential)

---

## Context Map (DDD)

- **Upstream Dependencies**:

| Context | Relationship | Integration | Owner |
|---------|-------------|-------------|-------|
| Policy | customer-supplier | API | Personal Lines |
| Customer | customer-supplier | API | Digital |
| Underwriting | customer-supplier | events | Underwriting |

- **Downstream Consumers**:

| Context | Relationship | Integration | Consumer |
|---------|-------------|-------------|----------|
| Finance | open-host-service | API | Finance Division |
| Reinsurance | open-host-service | batch | Risk Division |
| Analytics | published-language | events | Data Platform |

- **Shared Kernel**: Risk scoring models (shared with Underwriting)
- **Partnership**: Customer Service (joint ownership of customer communication)

---

## Team Topology

- **Stream-Aligned Teams**:

| Team | Focus | Value Stream |
|------|-------|--------------|
| Motor Claims | Motor claim lifecycle | Motor claim resolution |
| Property Claims | Home/contents claims | Property claim resolution |
| Commercial Claims | Business insurance claims | Commercial claim resolution |
| Customer Comms | Claim notifications & updates | Customer communication |

- **Platform Teams**:

| Team | Focus | Services Provided |
|------|-------|-------------------|
| Claims Platform | Core ClaimCenter services | API gateway, claim orchestration, document management |
| Integration Hub | External integrations | Supplier APIs, assessor networks, repairer networks |

- **Enabling Teams**:

| Team | Focus | Capabilities Enabled |
|------|-------|---------------------|
| Claims AI | ML model development | Fraud detection, damage assessment, triage |

- **Complicated Subsystem Teams**:

| Team | Focus | Specialist Domain |
|------|-------|------------------|
| Fraud Intelligence | Fraud detection & investigation | Fraud analytics, network analysis |

---

## Cognitive Load Budget

- **Total Teams**: 8
- **Total Services Owned**: 24
- **Average Services per Team**: 3.0
- **Overloaded Teams**: Motor Claims (owns 6 services), Claims Platform (owns 5 services)
- **Capacity for New Work**: Limited — Claims Transformation consuming most capacity
- **Load Reduction Initiatives**:
  - Split Motor Claims into Lodgement and Assessment teams (Q2)
  - Migrate legacy services to platform team (ongoing)

---

## Technology

- **Core Systems** (extends company):
  - Guidewire ClaimCenter (claim management)
  - Livegenic (video assessment)
  - Tractable (AI damage assessment)
  - Shift Technology (fraud detection)

- **Integrations**:
  - Repairer network APIs (200+ repairers)
  - Assessor network (mobile workforce)
  - Weather data providers (CAT detection)
  - Glass supplier networks
  - Parts pricing databases

- **Tech Stack** (extends company):
  - Python (ML models, automation)
  - Java (ClaimCenter customisation)
  - React (internal tools)
  - AWS Lambda (integrations)

---

## Data Ownership

- **Owns**:

| Domain | System of Record | Data Steward | Sensitivity |
|--------|-----------------|--------------|-------------|
| Claim | ClaimCenter | Claims Data Team | confidential |
| Assessment | ClaimCenter | Claims Data Team | confidential |
| Fraud Indicators | Shift Technology | Fraud Intelligence | restricted |

- **Consumes**:

| Domain | Source System | Owner | Refresh Frequency |
|--------|--------------|-------|-------------------|
| Policy | PolicyCenter | Personal Lines | real-time |
| Customer | CRM/PolicyCenter | Digital | real-time |
| Vehicle | External APIs | Data Platform | on-demand |
| Weather | External APIs | Data Platform | hourly |

---

## Architecture Decisions (ADRs)

| ID | Title | Status | Date | Decision |
|----|-------|--------|------|----------|
| ADR-001 | Use Tractable for motor damage assessment | accepted | 2024-06 | Integrate Tractable AI for automated photo-based damage assessment to reduce assessor visits |
| ADR-002 | Event-driven claim status updates | accepted | 2024-03 | Publish claim events to Kafka for real-time downstream consumption |
| ADR-003 | Maintain ClaimCenter as SOR | accepted | 2023-12 | All claim data modifications must go through ClaimCenter APIs, no direct database access |
| ADR-004 | Fraud scoring on every claim | accepted | 2024-09 | All claims receive fraud score at lodgement; high-risk claims routed to SIU |

---

## Regulatory & Compliance

- **Additional Frameworks** (extends company):
  - General Insurance Code of Practice — claims handling timeframes
  - Internal Dispute Resolution requirements
  - Privacy Act — medical information handling

- **Data Sensitivity** (extends company):
  - Medical reports and injury details
  - Police reports
  - Financial hardship information

- **Compliance Requirements**:
  - Acknowledge claims within 10 business days
  - Decision within 4 months (standard claims)
  - Monthly reporting to regulator on claims handling

### Compliance Status

- **Next Audit Date**: 2025-06-15
- **Compliance Contacts**: claims-compliance@protectorinsurance.com

**Open Audit Findings**:

| Finding ID | Severity | Description | Due Date | Owner | Status |
|------------|----------|-------------|----------|-------|--------|
| AF-2024-018 | high | Claims decision audit trail incomplete for automated decisions | 2025-03-31 | Claims Platform Lead | in_progress |
| AF-2024-022 | medium | Medical record access logging gaps | 2025-05-15 | Claims Data Team | open |

---

## Risk Management

- **Risk Owner**: David Chen, Claims Operations Director

### Division Risks

| Risk ID | Category | Description | Likelihood | Impact | Owner | Controls |
|---------|----------|-------------|------------|--------|-------|----------|
| DR-001 | operational | CAT event overwhelming claims capacity | likely | major | Operations Director | Surge capacity plan, contractor pool, automation |
| DR-002 | technology | ClaimCenter outage during peak | possible | catastrophic | Claims Platform Lead | Failover, manual backup processes |
| DR-003 | compliance | Breach of claims handling timeframes | possible | major | Compliance Manager | Automated alerts, escalation process |
| DR-004 | financial | Adverse development on motor claims | possible | moderate | Chief Actuary | Reserve monitoring, reinsurance |

### Key Risk Indicators (KRIs)

| Indicator | Threshold | Current | Status |
|-----------|-----------|---------|--------|
| Claims backlog > 10 days | > 500 claims | 285 claims | green |
| Assessor utilisation | > 95% | 82% | green |
| ClaimCenter availability | < 99.5% | 99.8% | green |
| IDR complaint response time | > 30 days avg | 18 days | green |
| CAT claims surge indicator | > 2x normal | 1.1x | green |

---

## Third-Party Risk

### Critical Vendors

| Vendor | Service | Criticality | Contract Owner | Contract End | SLA Performance |
|--------|---------|-------------|----------------|--------------|-----------------|
| Tractable | AI damage assessment | high | Claims AI Lead | 2026-06-30 | 99.7% uptime |
| Shift Technology | Fraud detection | high | Fraud Team Lead | 2026-03-31 | 99.5% uptime |
| Livegenic | Video assessment | medium | Assessment Lead | 2025-12-31 | 98.9% uptime |
| Repairer Network | Motor repairs | critical | Supplier Manager | Various | 92% satisfaction |

### Active Vendor Issues

| Vendor | Issue | Severity | Status |
|--------|-------|----------|--------|
| Livegenic | Video quality degradation on mobile | low | in_progress |

---

## Stakeholders

- **Executive Sponsor**: Sarah Mitchell, Chief Claims Officer
- **Decision Forum**: Claims Leadership Team (weekly)
- **Gate Approver**: Claims Product Director (up to $500k), CCO (above)

- **Key Stakeholders**:

| Name | Role | Interest |
|------|------|----------|
| Sarah Mitchell | CCO | Strategic direction, cost discipline |
| David Chen | Claims Operations Director | Operational efficiency, team capacity |
| Lisa Park | Customer Experience Director | NPS, customer satisfaction |
| James Wong | CFO | Claims cost ratio, reserves |

---

## Metrics

| Metric | Current | Target |
|--------|---------|--------|
| Claims NPS | +12 | +45 |
| Average cycle time (motor) | 21 days | 7 days |
| STP rate (motor simple) | 15% | 50% |
| Claims per FTE | 120/month | 180/month |
| Fraud detection rate | 2.1% | 3.5% |
| Combined ratio (claims element) | 72% | 68% |

---

## Maintenance

- **Review Frequency**: Quarterly
- **Owner**: Claims Product Director
- **Last Updated**: 2025-03-01
