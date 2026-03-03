---
schema: enterprise-context/v1/team
team: "[Team Name]"
product_area: "[Product/Domain]"
updated: "YYYY-MM-DD"
owner: "[pm@company.com]"
---

# Team Context

This document provides team-level context that extends the division context. It should be updated as needed when team circumstances change.

---

## Team Identity

- **Team**: [e.g., Claims Lodgement, Motor Quoting, Customer Portal]
- **Product Area**: [e.g., Customer-facing claims lodgement portal]
- **Product Manager**: [Name]
- **Tech Lead**: [Name]
- **Team Size**: [e.g., 8 (2 PM, 1 Design, 4 Dev, 1 QA)]
- **Team Type**: [Stream-aligned / Platform / Enabling / Complicated-subsystem]
- **Value Stream**: [e.g., Claims Journey — for stream-aligned teams]

---

## Team Interactions

*Document how this team interacts with other teams using Team Topologies patterns. This helps AI understand collaboration needs.*

| Team | Mode | Description | Duration | Contact |
|------|------|-------------|----------|---------|
| [Claims Platform] | [x-as-a-service] | [Consume ClaimCenter APIs; they own the platform] | [Ongoing] | [platform-lead@] |
| [Design Team] | [collaboration] | [Close collaboration on UX; embedded designer] | [Ongoing] | [design-lead@] |
| [Security Team] | [facilitating] | [Security reviews and guidance; we implement] | [Temporary] | [security@] |
| [Data Team] | [x-as-a-service] | [Consume data feeds; they own pipelines] | [Ongoing] | [data-lead@] |

**Interaction Modes**:
- **collaboration**: Working closely together; high-bandwidth, temporary
- **x-as-a-service**: Consuming their service/API; low-bandwidth, ongoing
- **facilitating**: They help us adopt new capabilities; temporary

---

## API/Service Ownership

*Document what this team owns vs consumes. Clear boundaries help AI design appropriate integrations.*

### APIs/Services We Own

| Name | Type | Consumers | SLA |
|------|------|-----------|-----|
| [lodgement-api] | [REST] | [Mobile app, Web portal, Broker portal] | [99.9% uptime] |
| [upload-service] | [REST] | [lodgement-api, assessor-tools] | [99.5% uptime] |
| [ClaimLodged event] | [event] | [Claims Assessment, Fraud Detection, Notifications] | [<5 min delay] |

### APIs/Services We Consume

| Name | Provider | Criticality | Fallback |
|------|----------|-------------|----------|
| [claimcenter-api] | [Claims Platform] | [critical] | [Queue for retry; show "processing" to user] |
| [policy-lookup] | [Policy team] | [critical] | [Manual policy entry fallback] |
| [okta-sso] | [Identity team] | [critical] | [None — auth required] |
| [document-store] | [Platform] | [important] | [Local storage with sync later] |
| [fraud-score] | [Fraud team] | [nice-to-have] | [Skip scoring; manual review] |

---

## Cognitive Load

*Assess your team's capacity. This helps AI calibrate recommendations to realistic team bandwidth.*

- **Current Velocity**: [e.g., 32 points/sprint]
- **Services Owned**: [e.g., 3]
- **Tech Debt Allocation**: [e.g., 20% of capacity]
- **On-Call Burden**: [e.g., 1 person/week, ~2 incidents/week average]
- **Meeting Load**: [Low / Moderate / High / Excessive]
- **Spare Capacity**: [None / Low / Moderate / High]
- **Domain Complexity**: [Low / Moderate / High / Very High]

- **Load Concerns**:
  - [e.g., On-call burden increasing due to legacy portal issues]
  - [e.g., Technical debt in upload service causing production issues]
  - [e.g., Team stretched across legacy and new systems]

---

## Current State

### Existing Solution

[Describe the current state of the product/system]

e.g., 8-year-old claims lodgement portal built on legacy .NET stack. Handles ~2,000 claims/day across home and motor.

### Known Issues

- [e.g., 47% mobile abandonment rate]
- [e.g., 23% of claims require re-submission due to missing information]
- [e.g., Average lodgement time of 18 minutes (target: 5 minutes)]
- [e.g., No real-time status updates — customers call to check status]
- [e.g., NPS of -12 for lodgement experience]

### Current Metrics

| Metric | Value |
|--------|-------|
| [Daily claims volume] | [2,000] |
| [Mobile abandonment] | [47%] |
| [Re-submission rate] | [23%] |
| [Average lodgement time] | [18 min] |
| [Lodgement NPS] | [-12] |

### Previous Attempts

| Initiative | Year | Outcome | Learnings |
|------------|------|---------|-----------|
| [Mobile app MVP] | [2019] | [Paused at MVP] | [Integration complexity with ClaimCenter underestimated] |
| [Portal refresh] | [2021] | [Cancelled] | [Budget cuts; scope was too large] |
| [Form optimisation] | [2023] | [Partial success] | [Reduced fields from 67 to 47, but UX still poor] |

---

## Domain Events

*Document domain events this team produces and consumes. Essential for event-driven architecture.*

### Events We Produce

| Event | Description | Consumers | Schema |
|-------|-------------|-----------|--------|
| [ClaimLodged] | [New claim submitted and accepted] | [Assessment, Fraud, Notifications, Analytics] | [/schemas/claim-lodged.json] |
| [PhotoUploaded] | [Photo attached to claim] | [Assessment, Fraud ML] | [/schemas/photo-uploaded.json] |
| [DocumentAttached] | [Document added to claim] | [Assessment, Compliance] | [/schemas/document-attached.json] |
| [LodgementAbandoned] | [User abandoned lodgement flow] | [Analytics, Marketing] | [/schemas/lodgement-abandoned.json] |

### Events We Consume

| Event | Producer | Usage |
|-------|----------|-------|
| [PolicyVerified] | [Policy team] | [Confirm coverage before accepting claim] |
| [CustomerAuthenticated] | [Identity team] | [Start authenticated session] |
| [FraudScoreCalculated] | [Fraud team] | [Show risk indicator to assessors] |

---

## Team Constraints

### Technical Constraints

- [e.g., Must integrate with existing Guidewire ClaimCenter instance]
- [e.g., Must use existing Okta identity provider]
- [e.g., No greenfield rebuild approved — must enhance existing platform]
- [e.g., Must support IE11 for internal assessor tools]

### Timeline Constraints

- [e.g., Q3 FY25 deadline for initial release]
- [e.g., Must align with ClaimCenter upgrade in Q4]

### Budget Constraints

- [e.g., $1.2M approved for FY25]
- [e.g., No additional headcount — must use existing team + contractors]

### Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| [ClaimCenter API enhancements] | [Platform Team] | [In progress] | [Medium] |
| [Real-time claim status feed] | [Data Team] | [Not started] | [High] |
| [Okta SSO for new portal] | [Identity Team] | [Approved] | [Low] |

---

## Definition of Done

*Define what "done" means for this team. This affects how AI writes stories and acceptance criteria.*

### Story Level

- [ ] Code complete and peer reviewed
- [ ] Unit tests written and passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Deployed to staging environment
- [ ] Tested by QA

### Feature Level

- [ ] All stories complete
- [ ] End-to-end tests passing
- [ ] Performance testing complete
- [ ] Security review passed
- [ ] Accessibility audit passed (WCAG 2.1 AA)
- [ ] Product owner acceptance

### Release Level

- [ ] All features complete
- [ ] Regression testing passed
- [ ] Load testing passed
- [ ] Runbook updated
- [ ] Monitoring and alerting configured
- [ ] Rollback plan documented

### Quality Gates

- [e.g., All PRs require 2 approvals]
- [e.g., No critical/high security vulnerabilities]
- [e.g., Performance regression tests must pass]
- [e.g., Architecture review for new services]

---

## Team Stakeholders

### Immediate Stakeholders

| Name | Role | Interest | Engagement |
|------|------|----------|------------|
| [James Wong] | [Head of Claims Ops] | [Reduce calls, improve efficiency] | [Weekly check-in] |
| [Emma Smith] | [Claims Assessor Lead] | [Quality submissions, less rework] | [Fortnightly feedback] |
| [Tom Brown] | [Platform Architect] | [API design, integration patterns] | [As needed] |
| [Rachel Green] | [Compliance] | [Regulatory adherence] | [Gate reviews] |

### Impacted Teams

| Team | Impact | Size | Engagement Approach |
|------|--------|------|---------------------|
| [Claims Assessors] | [Better quality submissions, less back-and-forth] | [120 FTE] | [Demo at team meeting, feedback channel] |
| [Customer Service] | [Fewer status calls, new escalation process] | [45 FTE] | [Training, runbook update] |
| [Platform Team] | [API changes, increased load] | [8 FTE] | [Technical design reviews] |

---

## Success Metrics Ownership

*Clarify which metrics this team owns vs influences. This helps AI write appropriate success criteria.*

### Metrics We Own

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| [Mobile abandonment rate] | [47%] | [20%] | [Analytics — sessions started vs completed] |
| [Average lodgement time] | [18 min] | [5 min] | [Analytics — time from start to submit] |
| [Re-submission rate] | [23%] | [5%] | [ClaimCenter — rejected submissions / total] |
| [Lodgement NPS] | [-12] | [+30] | [Post-lodgement survey] |

### Metrics We Influence

| Metric | Contribution | Owner |
|--------|--------------|-------|
| [Claims NPS (overall)] | [Lodgement is first touchpoint; drives initial impression] | [Claims Division] |
| [Cost per claim] | [Better quality submissions reduce rework costs] | [Claims Ops] |
| [Call volume] | [Self-service reduces "where's my claim" calls] | [Customer Service] |
| [First-touch resolution] | [Complete information enables faster assessment] | [Assessment Team] |

---

## Team Compliance

*Document compliance requirements that apply to this team's work. This helps AI ensure recommendations are compliant.*

- **Compliance Checklist**:
  - [e.g., PCI-DSS for payment handling]
  - [e.g., WCAG 2.1 AA for accessibility]
  - [e.g., Privacy by design for new features]
  - [e.g., Claims handling code for customer communications]

- **Last Compliance Review**: [e.g., 2024-09-15]

### Open Findings Assigned to Team

| Finding ID | Description | Due Date | Status |
|------------|-------------|----------|--------|
| [AF-2024-012] | [Incomplete audit trail for claim decisions] | [2025-02-28] | [in_progress] |

- **Evidence Requirements**:
  - [e.g., Access logs retained for 2 years]
  - [e.g., Change records for all production deployments]
  - [e.g., User consent records for data processing]

---

## Team Risk Exposure

*Document risks related to services this team owns. This helps AI understand operational risk context.*

### Service Risks

| Service | Risk | Impact | Mitigations |
|---------|------|--------|-------------|
| [lodgement-api] | [High traffic causing timeouts] | [major] | [Auto-scaling, circuit breaker, fallback queue] |
| [upload-service] | [Storage quota exceeded] | [moderate] | [Monitoring alerts, automated cleanup] |

### SLA Exposure

- **SLA Target**: [e.g., 99.9% uptime]
- **Current Performance**: [e.g., 99.7%]
- **Recent Breaches**: [e.g., 2024-11-15: 4-hour outage due to upstream dependency]
- **Financial Exposure**: [e.g., $50k penalty per 0.1% below target]

### Known Vulnerabilities

| System | Vulnerability | Severity | Remediation Plan |
|--------|---------------|----------|------------------|
| [Legacy upload service] | [Outdated dependencies (CVE-2024-xxxx)] | [high] | [Scheduled for Q1 2025 upgrade] |

---

## Third-Party Dependencies

*Document vendors this team depends on. This helps AI understand external dependencies and fallback options.*

### Team Vendor Dependencies

| Vendor | Service | Criticality | SLA | Support Contact |
|--------|---------|-------------|-----|-----------------|
| [Verisk] | [Repair estimating API] | [critical] | [99.5% uptime] | [support@verisk.com] |
| [Twilio] | [SMS notifications] | [medium] | [99.95% uptime] | [support@twilio.com] |

### Fallback Options

| Vendor | Fallback Approach |
|--------|-------------------|
| [Verisk] | [Manual estimation by assessors; 2-hour delay expected] |
| [Twilio] | [Email fallback; customer preference required] |

---

## Target Users

- **Primary Users**: [e.g., Policyholders lodging home and motor claims (B2C)]
- **Secondary Users**: [e.g., Brokers lodging on behalf of clients, internal assessors]
- **User Sophistication**: [e.g., Mixed — ranges from digital natives to elderly customers with low digital literacy]

### Known Pain Points

- [e.g., Too many form fields — feels like a tax return]
- [e.g., Unclear what information is needed upfront]
- [e.g., No visibility into claim progress after submission]
- [e.g., Poor mobile experience — can't lodge from accident scene]
- [e.g., Have to re-enter policy details they think we should already know]

---

## How to Maintain This Document

- **Review Frequency**: Update when team circumstances change significantly
- **Owner**: [Product Manager]
- **Last Updated**: [Date]

### Tips for Quality Context

1. **Know your boundaries** — Clear API ownership prevents scope creep and ownership confusion
2. **Track cognitive load** — Overloaded teams deliver less and have higher turnover
3. **Define done clearly** — Ambiguous "done" leads to incomplete work
4. **Own your metrics** — If you don't own a metric, you can't be accountable for it
5. **Document your events** — Event-driven systems need clear contracts
