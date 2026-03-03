---
schema: enterprise-context/v1/company
company: "Protector Insurance Group"
industry: "General Insurance"
updated: "2025-03-01"
owner: "strategy@protectorinsurance.com"
---

# Company Context

## Company & Industry

- **Company**: Protector Insurance Group
- **Industry**: General Insurance (Property & Casualty)
- **Business Units**: Personal Lines, Commercial Lines, Claims, Underwriting, Distribution
- **Company Size**: 8,500 employees, $6.8B GWP (Gross Written Premium), 4.2M policies
- **Geographic Presence**: National with regional claims centres in all major cities

---

## Strategic Priorities

- **Current Strategy (FY25)**: Customer-centric claims experience, underwriting automation, digital distribution, combined ratio improvement

- **Company OKRs**:
  - Objective: Transform claims experience
    - KR1: Reduce average claim cycle time from 21 days to 7 days
    - KR2: Increase claims NPS from +12 to +45
    - KR3: Achieve 60% straight-through processing for simple claims
  - Objective: Improve underwriting profitability
    - KR1: Reduce combined ratio from 98% to 94%
    - KR2: Implement ML-based pricing for 80% of personal lines
    - KR3: Reduce quote turnaround time by 50%

- **Investment Themes**: Claims automation, Digital self-service, Telematics & IoT, Advanced analytics, Partner API ecosystem

- **Strategic Constraints**: Regulatory scrutiny on claims handling, no new product lines in FY25, focus on profitability over growth, maintain AM Best A rating

---

## Business Capabilities

| Capability | Maturity | Investment Priority | Description |
|------------|----------|---------------------|-------------|
| Claims Lodgement | mature | optimize | Multi-channel claim intake |
| Claims Assessment | emerging | build | AI-assisted damage assessment |
| Policy Administration | mature | maintain | Core policy lifecycle management |
| Underwriting | emerging | grow | Risk assessment and pricing |
| Digital Quote & Bind | emerging | grow | Online self-service for simple products |
| Fraud Detection | nascent | build | ML-based fraud identification |
| Customer Self-Service | emerging | grow | Policy and claims self-service portal |
| Partner Integration | nascent | build | APIs for brokers and partners |

---

## Technology Landscape

- **Core Systems**: Guidewire (ClaimCenter, PolicyCenter, BillingCenter), Duck Creek (legacy, sunset 2026)
- **Cloud & Infrastructure**: AWS (primary), Azure (M365, analytics), on-prem data centre for legacy
- **Key Platforms**: Okta (identity), Snowflake (analytics), ServiceNow (ITSM), Salesforce (CRM for commercial)
- **Integration Approach**: API-first via AWS API Gateway, MuleSoft for legacy integrations, event-driven for real-time notifications
- **Technical Constraints**: Must maintain Guidewire compatibility, no custom core system modifications, all customer data must be encrypted at rest
- **Technical Debt**: Duck Creek migration in progress, legacy mainframe batch processes, paper-based workflows in commercial underwriting

---

## Data Architecture

- **Golden Sources**:

| Data Domain | System of Record |
|-------------|------------------|
| Policy | Guidewire PolicyCenter |
| Claim | Guidewire ClaimCenter |
| Customer | Salesforce (Commercial), PolicyCenter (Personal) |
| Billing | Guidewire BillingCenter |
| Analytics | Snowflake |

- **Data Domains**: Policy, Claim, Customer, Vehicle, Property, Finance, Risk, Fraud
- **Data Governance**: Federated — domain stewards with central standards team
- **Data Platform**: Snowflake (analytics), AWS S3 (data lake), Databricks (ML)
- **Data Quality Standards**: Claims data SLA <1 hour freshness, daily reconciliation with core systems, automated anomaly detection

---

## Regulatory & Compliance

- **Primary Regulators**: Insurance Regulatory Authority, Financial Services Commission, Data Protection Authority
- **Key Frameworks**: SOC 2 Type II, ISO 27001, General Insurance Code of Practice, Privacy Act compliance
- **Compliance Stance**: Moderate — balanced approach, engage regulators on novel AI use cases, strong documentation
- **Data Sensitivity**: PII (policyholder details), medical information (injury claims), financial data (payment details), vehicle/property data
- **Data Residency**: Local data centres for policyholder data, cloud processing permitted with appropriate controls

### Compliance Program

- **Compliance Officers**:
  - Chief Compliance Officer (CCO) - Sarah Chen
  - Data Protection Officer (DPO) - Michael Torres
  - Claims Compliance Manager - Jennifer Walsh

- **Audit Schedule**:
  - External: Annual SOC 2 Type II, Biennial ISO 27001 recertification
  - Internal: Quarterly compliance reviews, Annual control testing
  - Regulatory: APRA tripartite reviews as scheduled

- **Last External Audit**: 2024-09-15

- **Active Certifications**:
  - ISO 27001:2022 (expires 2026-05-20)
  - SOC 2 Type II (annual attestation)

- **Regulatory Reporting**:
  - Insurance Regulatory Authority quarterly returns
  - Financial Services Commission annual report
  - Breach notification within 72 hours

---

## Risk Management

- **Risk Framework**: COSO ERM with insurance-specific extensions
- **Risk Committee**: Board Risk Committee (quarterly), Executive Risk Committee (monthly)
- **Risk Reporting**: Monthly to ExCo, Quarterly to Board Risk Committee

### Risk Appetite

| Dimension | Appetite | Description |
|-----------|----------|-------------|
| Technology | progressive | Early adopter of proven insurtech solutions, active innovation lab |
| Market | conservative | Focus on existing product lines, cautious about new segments |
| Regulatory | moderate | Proactive engagement, seek clarity before acting in grey areas |
| Innovation | progressive | Strong investment in AI/ML, willing to experiment with claims automation |
| Operational | moderate | Accept measured disruption for efficiency gains, careful change management |

### Enterprise Risks

| Risk ID | Category | Description | Likelihood | Impact | Owner | Treatment |
|---------|----------|-------------|------------|--------|-------|-----------|
| R-001 | operational | Catastrophe claims surge overwhelming capacity | likely | major | Chief Claims Officer | mitigate |
| R-002 | technology | Core Guidewire system outage | unlikely | catastrophic | CTO | mitigate |
| R-003 | compliance | Regulatory breach on claims handling timeframes | possible | major | CCO | mitigate |
| R-004 | financial | Adverse claims development on motor book | possible | moderate | Chief Actuary | accept |
| R-005 | reputational | Social media amplification of claims dispute | possible | moderate | Chief Marketing Officer | mitigate |

---

## Third-Party Risk Management

- **Vendor Policy**: All critical vendors require annual security assessment
- **Assessment Framework**: SIG (Standardized Information Gathering)
- **Vendor Audit Schedule**: Critical: annual, High: biennial, Medium: triennial

### Critical Vendors

| Vendor | Service | Criticality | Data Access | Last Assessment | Contract End |
|--------|---------|-------------|-------------|-----------------|--------------|
| Guidewire | Core insurance platform | critical | All policy and claims data | 2024-06-15 | 2027-12-31 |
| AWS | Cloud infrastructure | critical | All data (encrypted) | 2024-03-01 | 2026-12-31 |
| Verisk | Vehicle estimating | high | Vehicle details, claim data | 2024-08-20 | 2025-12-31 |
| Friss | Fraud detection | high | Claims data | 2024-04-10 | 2026-06-30 |
| Salesforce | Commercial CRM | high | Commercial customer PII | 2024-07-15 | 2025-09-30 |

### Concentration Limits

| Category | Limit | Current |
|----------|-------|---------|
| Single cloud provider | 85% of infrastructure | 82% (AWS) |
| Core system vendor | Acceptable concentration | Guidewire only |

### Exit Requirements

- All critical vendors must have 12-month exit clause
- Data portability required in all contracts
- Escrow for Guidewire customisation code

---

## Funding Model

- **Funding Type**: Product-based funding for ongoing teams, project-based for transformations
- **Budget Cycle**: January-December (calendar year)
- **CapEx vs OpEx Preference**: Shifting to OpEx for cloud; CapEx for Guidewire licensing
- **Reallocation Flexibility**: Moderate — can reallocate up to 20% within division with CTO approval

- **Approval Thresholds**:

| Role | Threshold |
|------|-----------|
| Team Lead | $75k |
| Product Director | $200k |
| Division Head | $750k |
| Investment Committee | $3M |
| Executive / Board | $15M+ |

---

## Change Capacity

- **Major Initiatives in Flight**: 4 (Claims Transformation, Guidewire Upgrade, Digital Distribution, Data Platform)
- **Change Fatigue Level**: Moderate — Claims team stretched with transformation, other areas manageable
- **Adoption Support Available**: Moderate — dedicated change team for Claims, shared resources elsewhere

- **Transformation Programs**:
  - Claims Transformation (FY24-26) — end-to-end claims digitisation
  - Guidewire Upgrade (FY25) — major version upgrade for all centres
  - Digital Distribution (FY25-26) — online quote & bind for personal lines
  - Data Platform Modernisation (FY25) — Snowflake migration complete

- **Change Blackout Periods**:
  - Catastrophe season (Nov-Feb) — severe weather claims surge
  - End of financial year (June) — regulatory reporting
  - Major renewals (quarterly) — peak underwriting periods

---

## Organisational Structure

- **Executive Sponsors**: Chief Claims Officer (claims initiatives), Chief Digital Officer (digital), CTO (platform), Chief Underwriting Officer (underwriting)
- **Product Leadership**: CPO with domain Product Directors (Claims, Personal Lines, Commercial Lines, Platform), each with 4-6 PMs
- **Delivery Model**: Agile (Scrum) for product teams, SAFe for Claims Transformation, Waterfall for regulatory projects
- **Key Decision Forums**:
  - Executive Committee (weekly) — strategic decisions
  - Technology Steering Committee (fortnightly) — tech investment
  - Product Council (weekly) — product prioritisation
  - Architecture Review Board (fortnightly) — technical decisions
- **Gate Approvers**:
  - L0-L1: Product Director
  - L2: Investment Committee
  - L3+: Executive Sponsor + CFO

---

## Architecture Principles

| Principle | Statement | Implications |
|-----------|-----------|--------------|
| Guidewire-First | Core insurance operations should leverage Guidewire capabilities | Custom development only where Guidewire cannot support, follow Guidewire upgrade path |
| API-First | All capabilities exposed via APIs before UIs | Build APIs first, enable partner integration, invest in API management |
| Cloud-Native | New systems designed for AWS | Use managed services, design for horizontal scale, avoid vendor lock-in |
| Data-Driven Decisions | All significant decisions backed by data | Invest in analytics, ML models require explainability, maintain audit trails |
| Security by Design | Security built into all solutions | Threat modelling required, PII encryption mandatory, zero-trust approach |

---

## Competitor Landscape

- **Primary Competitors**: Major national insurers, regional specialists, direct insurers
- **Emerging Disruptors**: Insurtech startups, embedded insurance providers, big tech financial services
- **Competitive Differentiators**: Claims service reputation, broker relationships, commercial underwriting expertise, regional presence
- **Market Position**: Top 5 nationally, #2 in motor insurance, strong commercial lines presence

---

## Ubiquitous Language

| Term | Definition |
|------|------------|
| Claim | A request for payment under the terms of an insurance policy |
| FNOL | First Notice of Loss — the initial report of a claim |
| Lodgement | The process of registering a new claim in the system |
| Assessment | Evaluation of claim validity, coverage, and quantum |
| Quantum | The amount payable for a claim |
| Reserve | Estimated cost of an outstanding claim |
| STP | Straight-Through Processing — automated claim settlement without human intervention |
| CAT | Catastrophe event — widespread claims from a single event (storm, flood) |
| Excess | The amount the policyholder pays towards a claim (deductible) |
| Underwriting | The process of evaluating and pricing risk |
| GWP | Gross Written Premium — total premium before reinsurance |
| Combined Ratio | Claims + expenses as % of premium (below 100% = profitable) |
| Policy | The contract between insurer and policyholder |
| Endorsement | A modification to an existing policy |

---

## Maintenance

- **Review Frequency**: Annually (January) or after major strategic shifts
- **Owner**: Strategy & Transformation Team
- **Last Updated**: 2025-03-01
