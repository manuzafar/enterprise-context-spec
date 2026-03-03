---
schema: enterprise-context/v1/team
team: "Customer Portal"
product_area: "Customer-facing self-service portal"
updated: "2025-03-01"
owner: "pm.portal@acmecorp.com"
---

# Customer Portal Team Context

## Team Identity

- **Team**: Customer Portal
- **Product Area**: Customer-facing self-service portal for case submission and tracking
- **Product Manager**: Alex Johnson
- **Tech Lead**: Sam Williams
- **Team Size**: 8 (1 PM, 1 Designer, 5 Developers, 1 QA)
- **Team Type**: Stream-aligned
- **Value Stream**: Customer Journey

---

## Team Interactions

| Team | Mode | Description | Duration | Contact |
|------|------|-------------|----------|---------|
| Operations Platform | x-as-a-service | Consume core banking APIs; they own the platform | Ongoing | tom.brown@acme |
| Design Team | collaboration | Close collaboration on UX; embedded designer on our team | Ongoing | ux-lead@acme |
| Security Team | facilitating | Security reviews and guidance for PII handling; we implement | Temporary (per release) | security@acme |
| Data Team | x-as-a-service | Consume real-time case status feed; they own pipelines | Ongoing | data-lead@acme |
| Identity Team | x-as-a-service | Consume Okta SSO; they handle identity | Ongoing | identity@acme |
| Fraud ML Team | x-as-a-service | Consume fraud scoring API; they own models | Ongoing | fraud-ml@acme |
| Customer Service | collaboration | Joint work on escalation flows and handoffs | Temporary (during MVP) | cs-lead@acme |

---

## API/Service Ownership

### APIs/Services We Own

| Name | Type | Consumers | SLA |
|------|------|-----------|-----|
| portal-api | REST | Mobile app, Web portal, Partner portal | 99.9% uptime, <200ms p95 |
| upload-service | REST | portal-api, operations-tools | 99.5% uptime, 50MB max file |
| portal-ui | UI | End customers, partners | 3s load time on 3G |
| CaseSubmitted event | event | Operations, Fraud, Notifications, Analytics | <5 min delivery |
| DocumentUploaded event | event | Operations, Fraud ML | <5 min delivery |
| SessionAbandoned event | event | Analytics, Marketing | Best effort |

### APIs/Services We Consume

| Name | Provider | Criticality | Fallback |
|------|----------|-------------|----------|
| core-banking-api | Operations Platform | critical | Queue for retry; show "processing" to user |
| account-lookup | Account team | critical | Manual account entry fallback |
| okta-sso | Identity team | critical | None — auth required |
| document-store | Operations Platform | important | Local storage with sync later |
| fraud-score | Fraud ML team | nice-to-have | Skip scoring; flag for manual review |
| address-lookup | External (vendor) | nice-to-have | Manual address entry |

---

## Cognitive Load

- **Current Velocity**: 32 points/sprint (2-week sprints)
- **Services Owned**: 3 (portal-api, upload-service, portal-ui)
- **Tech Debt Allocation**: 20% of capacity (1 story per sprint)
- **On-Call Burden**: 1 person/week rotation, ~2-3 incidents/week (mostly legacy portal)
- **Meeting Load**: Moderate (standups, refinement, retro, stakeholder demos)
- **Spare Capacity**: Low — currently at capacity with modernisation project
- **Domain Complexity**: Moderate — well-understood domain but many edge cases

- **Load Concerns**:
  - On-call burden increasing due to legacy portal stability issues
  - Supporting two portals (legacy and new) during transition period
  - Dependency on Platform team for core API changes slowing delivery
  - Document upload service needs refactoring but no capacity

---

## Current State

### Existing Solution

8-year-old customer portal built on legacy .NET Web Forms stack. Handles approximately 5,000 customer requests per day across all service types. Originally designed for desktop browsers; mobile experience was retrofitted and performs poorly.

The portal collects customer requests through a multi-step wizard with 35 form fields on average. Customers must provide account details, request information, supporting documents, and contact preferences all in one session.

### Known Issues

- **52% mobile abandonment rate** — users start on mobile but give up
- **28% re-submission rate** — requests rejected due to missing or incorrect information
- **15-minute average completion time** — target is under 5 minutes
- **No real-time status updates** — customers call to check status (40% of inbound calls)
- **NPS of +8** for portal experience specifically (below company average)
- **No save & resume** — if session times out, customer loses all progress
- **Poor document upload** — frequent failures on mobile, no guidance on what documents are needed
- **No pre-fill** — customers re-enter information we already know (account, address, contact details)

### Current Metrics

| Metric | Value |
|--------|-------|
| Daily request volume | 5,000 |
| Mobile traffic share | 65% |
| Mobile abandonment | 52% |
| Desktop abandonment | 22% |
| Re-submission rate | 28% |
| Average completion time | 15 min |
| Portal NPS | +8 |
| "Status check" calls | 1,200/day |

### Previous Attempts

| Initiative | Year | Outcome | Learnings |
|------------|------|---------|-----------|
| Mobile app MVP | 2019 | Paused at MVP | Integration complexity with core platform underestimated; team was pulled to another priority |
| Portal UX refresh | 2021 | Cancelled | Budget cuts; scope was too ambitious (full rebuild) |
| Form field reduction | 2023 | Partial success | Reduced fields from 52 to 35, but UX still fundamentally flawed |
| Document upload fix | 2024 | Deployed | Improved success rate from 68% to 85%, but still fails too often on mobile |

---

## Domain Events

### Events We Produce

| Event | Description | Consumers | Schema |
|-------|-------------|-----------|--------|
| CaseSubmitted | New request submitted and accepted into core system | Operations, Fraud Detection, Notifications, Analytics | /schemas/events/case-submitted.v1.json |
| DocumentUploaded | Document attached to a case | Operations, Fraud ML (document analysis) | /schemas/events/document-uploaded.v1.json |
| SessionAbandoned | User abandoned self-service flow without completing | Analytics, Marketing (follow-up) | /schemas/events/session-abandoned.v1.json |
| SessionStarted | User began self-service flow | Analytics (funnel tracking) | /schemas/events/session-started.v1.json |

### Events We Consume

| Event | Producer | Usage |
|-------|----------|-------|
| AccountVerified | Account team | Confirm account status; auto-populate account details |
| CustomerAuthenticated | Identity team | Start authenticated session; retrieve customer profile |
| FraudScoreCalculated | Fraud team | Display risk indicator to operations staff |
| CaseStatusChanged | Operations team | Update status shown to customer in portal |

---

## Team Constraints

### Technical Constraints

- **Must integrate with core banking platform** — all case data must flow through platform APIs; cannot bypass
- **Must use Okta for authentication** — existing customer identity; no separate login
- **No greenfield rebuild approved** — must enhance/replace incrementally; ARB rejected "build new" proposal
- **Must support current browsers** — Chrome, Safari, Edge, Firefox; can drop IE11 for customer portal (but not internal tools)
- **Document storage in Azure Blob** — existing pattern; 50MB limit per request
- **Mobile-first design** — ADR-003 mandates mobile-first approach

### Timeline Constraints

- **Q3 FY25 target** for MVP release (mobile-first self-service for common requests)
- **Must align with core platform upgrade** scheduled for Q4 — can't make breaking API changes after September
- **Q4 code freeze** (December) for peak transaction season

### Budget Constraints

- **$1.5M approved for FY25** (approved at L2 gate)
- **No additional headcount** — must deliver with existing team + up to 2 contractors
- **Cloud costs capped** at $20k/month incremental

### Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| Core platform API enhancements | Platform Team | In progress | Medium — competing priorities |
| Real-time case status feed | Data Team | Not started | High — no committed date |
| Okta SSO for new portal | Identity Team | Approved | Low — standard config |
| Address verification integration | Vendor | Contract pending | Medium — procurement delays |
| Document AI (auto-extraction) | Innovation Team | POC complete | Low — optional for MVP |

---

## Definition of Done

### Story Level

- [ ] Code complete and peer reviewed (2 approvals required)
- [ ] Unit tests written and passing (>80% coverage for new code)
- [ ] Integration tests passing
- [ ] Accessibility tested (WCAG 2.1 AA compliance)
- [ ] Security scan passed (no critical/high vulnerabilities)
- [ ] Documentation updated (API docs, runbook if applicable)
- [ ] Deployed to staging environment
- [ ] Tested by QA (functional + exploratory)
- [ ] Mobile testing completed (iOS Safari, Android Chrome)

### Feature Level

- [ ] All stories complete
- [ ] End-to-end tests passing
- [ ] Performance testing complete (3s on 3G target)
- [ ] Security review passed (if PII handling changed)
- [ ] Accessibility audit passed
- [ ] Analytics tracking verified
- [ ] Product owner acceptance

### Release Level

- [ ] All features complete
- [ ] Regression testing passed
- [ ] Load testing passed (2x expected peak load)
- [ ] Penetration testing passed (annual or major release)
- [ ] Runbook updated
- [ ] Monitoring and alerting configured
- [ ] Rollback plan documented and tested
- [ ] Customer Service briefed
- [ ] Release notes published

### Quality Gates

- All PRs require 2 approvals (1 must be senior dev)
- No critical/high security vulnerabilities
- No accessibility violations (WCAG 2.1 AA)
- Performance regression tests must pass
- Architecture review for new APIs or services
- Privacy impact assessment for new PII collection

---

## Team Stakeholders

### Immediate Stakeholders

| Name | Role | Interest | Engagement |
|------|------|----------|------------|
| James Wong | Head of Operations | Reduce calls, improve efficiency, SLA compliance | Weekly check-in |
| Emma Smith | Operations Team Lead | Quality submissions, less rework, complete information | Fortnightly feedback session |
| Tom Brown | Platform Architect | API design, integration patterns, scalability | As needed (tech design) |
| Rachel Green | Compliance | Regulatory adherence, PII handling, audit trail | Gate reviews |
| David Lee | Head of Customer Service | Call deflection, escalation process | Monthly metrics review |

### Impacted Teams

| Team | Impact | Size | Engagement Approach |
|------|--------|------|---------------------|
| Operations Staff | Better quality submissions, less back-and-forth with customers | 150 FTE | Demo at team meeting, feedback Slack channel |
| Customer Service | Fewer "status check" calls, new escalation process for portal issues | 60 FTE | Training sessions, updated runbooks |
| Platform Team | API changes, increased load on core platform | 10 FTE | Technical design reviews, capacity planning |
| Data Team | New event streams, analytics requirements | 8 FTE | Requirements handoff, schema reviews |

---

## Success Metrics Ownership

### Metrics We Own

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Mobile abandonment rate | 52% | 20% | Analytics — sessions started vs completed on mobile |
| Average completion time | 15 min | 5 min | Analytics — time from start to successful submit |
| Re-submission rate | 28% | 8% | Core platform — rejected submissions / total submissions |
| Portal NPS | +8 | +40 | Post-submission survey (sampled) |
| Document upload success rate | 85% | 98% | Upload service — successful uploads / attempts |
| Form completion rate | 48% | 80% | Analytics — users reaching submit / users starting |

### Metrics We Influence

| Metric | Contribution | Owner |
|--------|--------------|-------|
| Operations NPS (overall) | Portal is first touchpoint; drives initial impression | Operations Division |
| Cost per case | Better quality submissions reduce staff rework costs | Operations |
| Call volume | Self-service status reduces "status check" calls | Customer Service |
| First-touch resolution | Complete, accurate information enables faster processing | Operations Team |
| Average case resolution time | Quality submissions reduce back-and-forth, faster to process | Operations Division |

---

## Target Users

- **Primary Users**: Customers submitting service requests (B2C)
  - Mix of request types (account changes, disputes, general enquiries)
  - 65% access via mobile
  - Mix of demographics — 18-80 years old

- **Secondary Users**:
  - Partners submitting on behalf of customers (12% of volume)
  - Customer service agents completing requests by phone (18% of volume)

- **User Sophistication**: Mixed
  - Digital natives who expect mobile-first, instant experience
  - Elderly customers with low digital literacy who prefer phone
  - Customers in stressful situations needing urgent assistance

### Known Pain Points (from user research)

1. **"It feels like doing my tax return"** — too many fields, too much detail required upfront
2. **"Why do I have to tell you my account number? You should know who I am"** — no pre-fill of known data
3. **"I started on my phone but gave up"** — mobile experience is frustrating
4. **"I don't know what documents you need"** — no guidance, then rejection for missing documents
5. **"I have no idea what's happening with my request"** — no status visibility
6. **"I already told the call centre this"** — channel switching loses context
7. **"The page timed out and I lost everything"** — no save & resume

---

## Maintenance

- **Review Frequency**: As needed (typically monthly or after major changes)
- **Owner**: Alex Johnson, Product Manager
- **Last Updated**: 2025-03-01
