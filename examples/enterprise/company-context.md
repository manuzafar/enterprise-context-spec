---
schema: enterprise-context/v1/company
company: "Acme Corporation"
industry: "Financial Services"
updated: "2025-03-01"
owner: "strategy@acmecorp.com"
---

# Company Context

## Company & Industry

- **Company**: Acme Corporation
- **Industry**: Financial Services
- **Business Units**: Retail Banking, Commercial Banking, Operations, Digital, Risk & Compliance
- **Company Size**: 12,000 employees, $4.2B revenue, 3.5M customers
- **Geographic Presence**: National with regional offices across all major cities

---

## Strategic Priorities

- **Current Strategy (FY25)**: Digital-first customer experience, operational automation, platform modernisation, regulatory excellence

- **Company OKRs**:
  - Objective: Transform customer experience
    - KR1: Increase NPS from +18 to +40
    - KR2: Achieve 70% digital self-service adoption
    - KR3: Reduce customer effort score by 30%
  - Objective: Drive operational efficiency
    - KR1: Reduce processing costs by 25%
    - KR2: Automate 60% of routine transactions
    - KR3: Reduce average processing time from 5 days to 1 day

- **Investment Themes**: Self-service portals, AI/ML automation, Core platform modernisation, Data & Analytics, API ecosystem

- **Strategic Constraints**: No major acquisitions in FY25, 12% cost reduction target, headcount freeze in non-growth areas, focus on core business lines

---

## Business Capabilities

| Capability | Maturity | Investment Priority | Description |
|------------|----------|---------------------|-------------|
| Account Management | mature | maintain | Core account lifecycle management |
| Transaction Processing | mature | optimize | End-to-end transaction handling and settlement |
| Digital Onboarding | emerging | grow | Online self-service customer onboarding — current focus |
| Fraud Detection | nascent | build | ML-based fraud identification — new investment |
| Partner Portal | emerging | grow | Digital tools for partner network |
| Customer Self-Service | emerging | grow | Account servicing, transaction tracking |
| Risk Assessment | nascent | build | AI-assisted risk evaluation |
| Data & Analytics | emerging | grow | Cloud-based analytics platform |

---

## Technology Landscape

- **Core Systems**: Core Banking Platform, SAP (Finance), Salesforce (CRM), ServiceNow (Operations)
- **Cloud & Infrastructure**: Azure (primary), AWS (data platform), hybrid with data centre migration in progress
- **Key Platforms**: Okta (identity), Snowflake (data warehouse), ServiceNow (ITSM), Confluence (knowledge management)
- **Integration Approach**: API-first via Azure API Management, event-driven architecture for real-time events, MuleSoft ESB for legacy integrations
- **Technical Constraints**: Must use existing identity provider, no greenfield rebuilds without ARB approval, core system upgrades must align with vendor release cycle
- **Technical Debt**: Legacy customer portal (EOL 2025), mainframe batch processes (being modernised), on-prem Exchange (migrating to O365)

---

## Data Architecture

- **Golden Sources**:

| Data Domain | System of Record |
|-------------|------------------|
| Customer | Salesforce CRM |
| Account | Core Banking Platform |
| Transaction | Core Banking Platform |
| Finance | SAP |
| Analytics | Snowflake |

- **Data Domains**: Customer, Account, Transaction, Finance, Product, Risk, Partner
- **Data Governance**: Hybrid — centralised standards with domain stewards
- **Data Platform**: Snowflake (primary), with Azure Data Factory for ETL
- **Data Quality Standards**: All data must have defined owners, SLAs for freshness (<24h for operational, real-time for customer-facing), automated quality checks in pipelines

---

## Regulatory & Compliance

- **Primary Regulators**: Central Bank, Financial Conduct Authority, Data Protection Authority
- **Key Frameworks**: SOC 2 Type II, ISO 27001, PCI-DSS, GDPR/Privacy regulations, AML/KYC requirements
- **Compliance Stance**: Conservative — we err on the side of caution in regulatory grey areas and engage regulators early on novel approaches
- **Data Sensitivity**: PII (name, address, DOB, national ID), financial data (account numbers, transactions), credit data, authentication credentials
- **Data Residency**: Local data centres only, no offshore processing of PII, cloud vendors must have local regions

---

## Risk Appetite

| Dimension | Appetite | Description |
|-----------|----------|-------------|
| Technology | moderate | Willing to adopt proven emerging tech (e.g., cloud-native, ML) but not bleeding edge |
| Market | conservative | Focus on core markets; cautious about new segments or products |
| Regulatory | very_conservative | Always err on side of caution; engage regulators early on novel approaches |
| Innovation | progressive | Encourage experimentation in non-critical areas; innovation lab active |
| Operational | moderate | Accept some disruption for meaningful improvement; managed change |

---

## Funding Model

- **Funding Type**: Hybrid — project-based for large initiatives, product funding for ongoing teams
- **Budget Cycle**: January-December (calendar year)
- **CapEx vs OpEx Preference**: Shifting to OpEx for cloud and SaaS; CapEx for platform investments
- **Reallocation Flexibility**: Limited — can reallocate up to 15% within division with GM approval

- **Approval Thresholds**:

| Role | Threshold |
|------|-----------|
| Team Lead | $50k |
| Product Director | $100k |
| GM / Division Head | $500k |
| Investment Committee | $2M |
| Executive / Board | $10M+ |

---

## Change Capacity

- **Major Initiatives in Flight**: 5 (Cloud Migration, Digital CX, Core Modernisation, Regulatory Program, Partner Portal)
- **Change Fatigue Level**: High — multiple large programs competing for attention and resources
- **Adoption Support Available**: Limited — small change management team, shared across programs

- **Transformation Programs**:
  - Cloud Migration (ends Q4 2025) — moving from on-prem to Azure
  - Digital Customer Experience (ongoing) — self-service portals
  - Core Platform Modernisation (FY25-27) — replacing legacy systems
  - Regulatory Compliance Program (ongoing) — new regulatory requirements

- **Change Blackout Periods**:
  - End of year freeze (December) — peak transaction period
  - End of financial year (March) — regulatory reporting period
  - Major release windows (quarterly) — controlled deployment periods

---

## Organisational Structure

- **Executive Sponsors**: Chief Digital Officer (product initiatives), Chief Operating Officer (operations initiatives), CTO (platform initiatives), CFO (finance transformation)
- **Product Leadership**: CPO with 4 domain Product Directors (Retail, Commercial, Operations, Digital), each with 3-5 PMs
- **Delivery Model**: Agile (Scrum) for product teams, SAFe for large cross-functional programs, Waterfall for regulatory/compliance projects
- **Key Decision Forums**:
  - Executive Committee (weekly) — strategic decisions
  - Investment Committee (monthly) — funding decisions >$500k
  - Product Council (fortnightly) — product prioritisation
  - Architecture Review Board (weekly) — technical decisions
- **Gate Approvers**:
  - L0-L1: Product Director
  - L2: Investment Committee
  - L3+: Executive Sponsor + CFO (for >$1M)

---

## Architecture Principles

| Principle | Statement | Implications |
|-----------|-----------|--------------|
| API-First | All capabilities must be exposed via APIs before UIs are built | Build APIs first, no direct DB access between systems, invest in API management |
| Cloud-Native | New systems should be designed for cloud deployment | Use managed services, design for horizontal scale, 12-factor app principles |
| Buy Before Build | Prefer COTS/SaaS for non-differentiating capabilities | Only custom-build for competitive advantage; evaluate total cost of ownership |
| Security by Design | Security is not an afterthought | Threat modelling required for new services, security review gates, zero-trust approach |
| Data as Product | Treat data as a first-class product with owners and SLAs | Data domains have stewards, quality standards, documentation requirements |
| Event-Driven | Use events for system integration where real-time is needed | Publish domain events, avoid tight coupling, accept eventual consistency |

---

## Competitor Landscape

- **Primary Competitors**: Major national banks, regional financial institutions, large fintech players
- **Emerging Disruptors**: Neobanks, fintech startups, big tech financial services, embedded finance providers
- **Competitive Differentiators**: Strong branch network, relationship banking, enterprise capabilities, regulatory trust, product breadth
- **Market Position**: Top 5 nationally, #2 in commercial segment, strong regional presence

---

## Ubiquitous Language

| Term | Definition |
|------|------------|
| Customer | An individual or organisation with an active relationship with Acme |
| Account | A product instance held by a customer (e.g., deposit account, loan, credit facility) |
| Transaction | A financial operation on an account (debit, credit, transfer, payment) |
| Onboarding | The process of setting up a new customer and their initial accounts |
| KYC | Know Your Customer — identity verification and due diligence process |
| AML | Anti-Money Laundering — transaction monitoring and suspicious activity reporting |
| STP | Straight-Through Processing — automated transaction completion without manual intervention |
| NPS | Net Promoter Score — measure of customer loyalty and satisfaction |
| Case | A unit of work requiring human review or action (e.g., dispute, request, exception) |
| Fulfilment | The process of completing a customer request or transaction |

---

## Maintenance

- **Review Frequency**: Annually (January) or after major strategic shifts
- **Owner**: Strategy & Transformation Team
- **Last Updated**: 2025-03-01
