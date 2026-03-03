---
schema: enterprise-context/v1/team
team: "Motor Claims"
product_area: "Motor Claim Lifecycle"
updated: "2025-03-01"
owner: "motor-claims-pm@protectorinsurance.com"
---

# Motor Claims Team Context

## Team Identity

- **Team**: Motor Claims
- **Product Area**: Motor Claim Lifecycle (FNOL to Settlement)
- **PM**: Alex Thompson
- **Tech Lead**: Priya Sharma
- **Team Size**: 8 (2 BE, 2 FE, 1 QA, 1 BA, PM, TL)
- **Team Type**: stream-aligned
- **Value Stream**: Motor claim resolution — from accident to payment

---

## Team Interactions

- **Claims Platform**:
  - Mode: x-as-a-service
  - Description: Consume ClaimCenter APIs, document storage, orchestration services
  - Duration: ongoing
  - Contact: platform-claims@protectorinsurance.com

- **Claims AI**:
  - Mode: collaboration
  - Description: Integrating Tractable damage assessment, working closely on model accuracy
  - Duration: temporary (Q1-Q2 2025)
  - Contact: claims-ai@protectorinsurance.com

- **Integration Hub**:
  - Mode: x-as-a-service
  - Description: Consume repairer network APIs, parts pricing services
  - Duration: ongoing
  - Contact: integration-hub@protectorinsurance.com

- **Customer Comms**:
  - Mode: collaboration
  - Description: Joint ownership of claim status notifications, SMS/email templates
  - Duration: ongoing
  - Contact: customer-comms@protectorinsurance.com

---

## API Ownership

- **Owns**:

| Name | Type | Consumers | SLA |
|------|------|-----------|-----|
| Motor Claim API | REST | Customer Portal, Mobile App, Contact Centre | 99.9% uptime |
| Damage Assessment Orchestrator | REST | Internal only | 99.5% uptime |
| Motor Claim Events | event | Analytics, Finance, Customer Comms | 99.9% delivery |

- **Consumes**:

| Name | Provider | Criticality | Fallback |
|------|----------|-------------|----------|
| ClaimCenter API | Claims Platform | critical | Manual processing in ClaimCenter UI |
| Policy API | Personal Lines | critical | Cached policy data (24h) |
| Tractable API | External (Claims AI managed) | important | Route to human assessor |
| Repairer Network API | Integration Hub | important | Manual repairer selection |
| Parts Pricing API | Integration Hub | nice-to-have | Standard labour rates |

---

## Cognitive Load

- **Current Velocity**: 28 points/sprint (2-week sprints)
- **Services Owned**: 6 (above target of 3)
- **Tech Debt Allocation**: 15% (target 20%, currently catching up)
- **On-Call Burden**: 1 person/week, ~3 incidents/week average
- **Meeting Load**: moderate
- **Spare Capacity**: low — fully committed to Claims Transformation deliverables
- **Domain Complexity**: high — motor claims involve liability, coverage, multiple parties, regulatory requirements

- **Load Concerns**:
  - Owning too many services — needs split into Lodgement and Assessment teams
  - Claims Transformation deliverables consuming all capacity
  - High on-call burden from legacy integrations

---

## Current State

- **Existing Solution**: Guidewire ClaimCenter with custom workflows, manual triage, assessor dispatch via phone/email, basic automation for glass claims only

- **Known Issues**:
  - Manual triage causes 24-48 hour delays
  - Assessor scheduling is phone-based (inefficient)
  - No automated damage assessment
  - Customer portal shows limited claim status
  - 8 manual touchpoints per claim on average

- **Metrics**:

| Metric | Current |
|--------|---------|
| Average cycle time | 21 days |
| STP rate | 15% |
| Customer effort score | 4.2/5 (high effort) |
| First contact resolution | 45% |
| Assessor utilisation | 62% |

- **Previous Attempts**:

| Initiative | Year | Outcome | Learnings |
|------------|------|---------|-----------|
| Claims Portal v1 | 2022 | Partial success | Customers want real-time status, not just documents |
| Automated triage pilot | 2023 | Failed | ML model accuracy too low (68%), retrained with better data |
| Self-service FNOL | 2024 | Success | 40% of motor claims now lodged via digital channels |

---

## Domain Events

- **Produces**:

| Event | Description | Consumers | Schema |
|-------|-------------|-----------|--------|
| ClaimLodged | New motor claim registered | Analytics, Fraud, Customer Comms | claims/motor-claim-lodged/v2 |
| ClaimAssessed | Assessment completed | Finance (reserves), Customer Comms | claims/motor-claim-assessed/v1 |
| ClaimSettled | Claim finalised and paid | Finance, Analytics | claims/motor-claim-settled/v1 |
| FraudFlagRaised | Claim flagged for investigation | Fraud Intelligence, SIU | claims/fraud-flag-raised/v1 |

- **Consumes**:

| Event | Producer | Usage |
|-------|----------|-------|
| PolicyUpdated | Personal Lines | Refresh policy coverage for open claims |
| PaymentProcessed | Finance | Update claim status to settled |
| FraudScoreCalculated | Fraud Intelligence | Route high-risk claims to manual review |

---

## Constraints

- **Technical**:
  - Must use ClaimCenter APIs (no direct DB access)
  - Tractable integration via AWS Lambda (latency <3s)
  - All PII must be encrypted in transit and at rest
  - Must maintain backwards compatibility with mobile app v2.x

- **Timeline**:
  - Q1 2025: Automated triage for simple claims
  - Q2 2025: Tractable integration for damage assessment
  - H2 2025: Repairer network automation

- **Budget**: $1.2M FY25 (part of Claims Transformation program)

- **Dependencies**:
  - Claims AI team for Tractable integration (collaboration)
  - Integration Hub for repairer APIs (Q2 delivery)
  - Claims Platform for new document management APIs (Q1 delivery)

---

## Definition of Done

- **Story Level**:
  - Code reviewed and approved
  - Unit tests passing (>80% coverage for new code)
  - Integration tests passing
  - Accessibility requirements met (WCAG 2.1 AA)
  - No critical/high security vulnerabilities
  - Documentation updated

- **Feature Level**:
  - All stories complete
  - End-to-end tests passing
  - Performance testing passed (<2s response time)
  - Regulatory review completed (if applicable)
  - Customer-facing documentation ready
  - Feature flag ready for gradual rollout

- **Release Level**:
  - All features complete
  - UAT signed off by business
  - Operational runbook updated
  - Monitoring and alerting configured
  - Rollback plan documented
  - Change Advisory Board approved

- **Quality Gates**:
  - SonarQube quality gate passed
  - Security scan (Snyk) passed
  - OWASP dependency check passed
  - Load testing passed (>500 concurrent users)

---

## Stakeholders

- **Immediate**:

| Name | Role | Interest |
|------|------|----------|
| David Chen | Claims Ops Director | Operational efficiency, throughput |
| Maria Santos | Motor Claims Manager | Team capacity, quality |
| Lisa Park | CX Director | Customer satisfaction, NPS |

- **Impacted Teams**:

| Team | Impact | Size |
|------|--------|------|
| Customer Comms | Claim status events trigger notifications | 5 |
| Contact Centre | Reduced call volume from self-service | 200 |
| Assessor Network | Automated dispatch changes workflow | 50 |
| Fraud Intelligence | New fraud scoring integration | 6 |

---

## Success Metrics Ownership

- **Owns**:

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Motor claim cycle time | 21 days | 7 days | ClaimCenter reporting |
| Motor STP rate | 15% | 50% | Automated vs manual settlement ratio |
| Digital FNOL adoption | 40% | 70% | Channel analytics |
| First contact resolution | 45% | 65% | Contact centre data |

- **Influences**:

| Metric | Contribution | Owner |
|--------|--------------|-------|
| Claims NPS | Motor claims are 60% of volume | Claims Division |
| Claims cost ratio | Automation reduces handling cost | Finance |
| Fraud detection rate | Better data improves ML models | Fraud Intelligence |

---

## Users

- **Primary**: Policyholders with motor claims (individual customers)
- **Secondary**:
  - Claims handlers (internal operations)
  - Contact centre agents
  - Assessors (external workforce)
  - Repairers (external partners)

- **Pain Points**:
  - Customers: Lack of real-time status, slow settlement, repeated information requests
  - Claims handlers: Manual data entry, system switching, incomplete information
  - Assessors: Inefficient scheduling, paper-based reporting

- **Sophistication**: Customers range from tech-savvy to digitally challenged; must support both digital and phone channels

---

## Maintenance

- **Review Frequency**: Sprint retrospectives + quarterly deep review
- **Owner**: Alex Thompson, Product Manager
- **Last Updated**: 2025-03-01
