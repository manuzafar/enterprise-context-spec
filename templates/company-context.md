---
schema: enterprise-context/v1/company
company: "[Your Company Name]"
industry: "[Your Industry]"
updated: "YYYY-MM-DD"
owner: "[strategy-team@company.com]"
---

# Company Context

This document provides company-wide context for AI agents. It should be updated annually or after major strategic changes.

---

## Company & Industry

- **Company**: [Your company name]
- **Industry**: [e.g., Financial Services, Healthcare, Technology, Manufacturing]
- **Business Units**: [e.g., Personal Lines, Commercial, Claims, Digital]
- **Company Size**: [e.g., 3,500 employees, $2.1B revenue, 1.2M customers]
- **Geographic Presence**: [e.g., National, Global, APAC, North America]

---

## Strategic Priorities

- **Current Strategy**: [e.g., FY25: Digital-first customer experience, operational efficiency, claims automation]

- **Company OKRs**:
  - Objective: [e.g., Improve customer experience]
    - KR1: [e.g., Increase NPS from +12 to +30]
    - KR2: [e.g., Reduce customer effort score by 25%]
  - Objective: [e.g., Drive operational efficiency]
    - KR1: [e.g., Reduce processing costs by 20%]
    - KR2: [e.g., Automate 50% of routine tasks]

- **Investment Themes**: [e.g., Self-service, AI/ML, Platform modernisation, Data & Analytics]

- **Strategic Constraints**: [e.g., No major acquisitions, 10% cost reduction target, headcount freeze in non-growth areas]

---

## Business Capabilities

*Map your business capabilities with their maturity and investment priority. This helps AI understand where to focus recommendations.*

| Capability | Maturity | Investment Priority | Description |
|------------|----------|---------------------|-------------|
| [e.g., Claims Processing] | [mature] | [optimize] | [Core claims handling workflow] |
| [e.g., Digital Lodgement] | [emerging] | [grow] | [Online self-service claims submission] |
| [e.g., Fraud Detection] | [nascent] | [build] | [ML-based fraud identification] |
| [e.g., Policy Admin] | [mature] | [maintain] | [Policy lifecycle management] |

**Maturity Levels**: nascent → emerging → mature → declining
**Investment Priorities**: build (new), grow (expand), optimize (improve efficiency), maintain (keep running), sunset (phase out)

---

## Technology Landscape

- **Core Systems**: [e.g., Guidewire (Policy/Claims/Billing), SAP (Finance), Salesforce (CRM)]
- **Cloud & Infrastructure**: [e.g., Azure (primary), AWS (data platform), Hybrid]
- **Key Platforms**: [e.g., Okta (identity), Snowflake (data warehouse), ServiceNow (ITSM)]
- **Integration Approach**: [e.g., API-first via Azure API Management, event-driven for real-time]
- **Technical Constraints**: [e.g., Must use existing identity provider, no greenfield rebuilds without ARB approval]
- **Technical Debt**: [e.g., Legacy .NET claims portal (EOL 2025), on-prem data centre migration in progress]

---

## Data Architecture

*Define your golden sources and data governance model. This helps AI understand where data lives and who owns it.*

- **Golden Sources**:

| Data Domain | System of Record |
|-------------|------------------|
| [Customer] | [Salesforce] |
| [Policy] | [Guidewire PolicyCenter] |
| [Claims] | [Guidewire ClaimCenter] |
| [Financials] | [SAP] |
| [Analytics] | [Snowflake] |

- **Data Domains**: [e.g., Customer, Policy, Claims, Finance, Product, Risk]
- **Data Governance**: [Centralised / Federated / Hybrid]
- **Data Platform**: [e.g., Snowflake, Databricks, BigQuery]
- **Data Quality Standards**: [e.g., Data must have defined owners, SLAs for freshness, automated quality checks]

---

## Regulatory & Compliance

- **Primary Regulators**: [e.g., APRA, ASIC, Privacy Commissioner]
- **Key Frameworks**: [e.g., APRA CPS 234 (InfoSec), Privacy Act 1988, SOC 2 Type II, ISO 27001]
- **Compliance Stance**: [Conservative / Moderate / Progressive — how does the organisation approach regulatory grey areas?]
- **Data Sensitivity**: [e.g., PII (name, address, DOB), financial data, medical records, claims history]
- **Data Residency**: [e.g., Australian data centres only, no offshore processing of PII]

### Compliance Program

*Document your compliance program structure. This helps AI understand governance and escalation paths.*

- **Compliance Officers**:
  - [e.g., Chief Compliance Officer (CCO) - overall compliance program]
  - [e.g., Data Protection Officer (DPO) - privacy compliance]
  - [e.g., Money Laundering Reporting Officer (MLRO) - AML compliance]

- **Audit Schedule**:
  - [e.g., External: Annual SOC 2 Type II, Biennial ISO 27001 recertification]
  - [e.g., Internal: Quarterly compliance reviews, Annual control testing]

- **Last External Audit**: [e.g., 2024-06-15]

- **Active Certifications**:
  - [e.g., ISO 27001:2022 (expires 2026-03-15)]
  - [e.g., SOC 2 Type II (annual)]
  - [e.g., PCI-DSS Level 1 (annual)]

- **Regulatory Reporting**:
  - [e.g., APRA quarterly returns]
  - [e.g., ASIC breach reporting (as required)]
  - [e.g., Privacy breach notification (within 72 hours)]

---

## Risk Management

*Define your enterprise risk management approach. This helps AI understand risk governance and calibrate recommendations.*

- **Risk Framework**: [e.g., COSO, ISO 31000, NIST RMF, Custom]
- **Risk Committee**: [e.g., Board Risk Committee, ERM Steering Committee]
- **Risk Reporting**: [e.g., Monthly to ExCo, Quarterly to Board]

### Risk Appetite

| Dimension | Appetite | Description |
|-----------|----------|-------------|
| Technology | [moderate] | [Willing to adopt proven emerging tech, but not bleeding edge] |
| Market | [conservative] | [Focus on core markets, cautious about new segments] |
| Regulatory | [very_conservative] | [Always err on side of caution, engage regulators early] |
| Innovation | [progressive] | [Encourage experimentation, fail-fast culture] |
| Operational | [moderate] | [Accept some disruption for meaningful improvement] |

**Levels**: very_conservative → conservative → moderate → progressive → aggressive

### Enterprise Risks

*Top risks tracked at board level. This helps AI avoid recommending approaches that increase known risks.*

| Risk ID | Category | Description | Likelihood | Impact | Owner | Treatment |
|---------|----------|-------------|------------|--------|-------|-----------|
| [R-001] | [technology] | [Legacy system failure] | [possible] | [major] | [CTO] | [mitigate] |
| [R-002] | [compliance] | [Regulatory breach] | [unlikely] | [catastrophic] | [CCO] | [mitigate] |
| [R-003] | [operational] | [Vendor concentration] | [likely] | [moderate] | [COO] | [transfer] |

**Categories**: strategic, operational, financial, compliance, technology, reputational
**Likelihood**: rare → unlikely → possible → likely → almost_certain
**Impact**: insignificant → minor → moderate → major → catastrophic
**Treatment**: accept, mitigate, transfer, avoid

---

## Third-Party Risk Management

*Define your vendor/third-party risk management approach. This helps AI understand approved vendors and concentration limits.*

- **Vendor Policy**: [e.g., All vendors must complete SIG questionnaire]
- **Assessment Framework**: [e.g., SIG, CAIQ, VSAQ, Custom]
- **Vendor Audit Schedule**: [e.g., Critical: annual, High: biennial, Medium: triennial]

### Critical Vendors

| Vendor | Service | Criticality | Data Access | Last Assessment | Contract End |
|--------|---------|-------------|-------------|-----------------|--------------|
| [AWS] | [Cloud infrastructure] | [critical] | [All data] | [2024-06-15] | [2026-12-31] |
| [Salesforce] | [CRM] | [critical] | [Customer PII] | [2024-03-01] | [2025-12-31] |
| [Guidewire] | [Core insurance platform] | [critical] | [Policy, claims data] | [2024-09-10] | [2027-06-30] |

### Concentration Limits

| Category | Limit | Current |
|----------|-------|---------|
| [Single cloud provider] | [80% of infrastructure] | [75%] |
| [Single vendor per critical capability] | [Avoid] | [Compliant] |

### Exit Requirements

- [e.g., All critical vendors must have 12-month exit clause]
- [e.g., Data portability required in all contracts]
- [e.g., Escrow for critical source code]

---

## Funding Model

*Explain how initiatives get funded. This helps AI understand budget constraints and approval processes.*

- **Funding Type**: [Project-based / Product-based / Hybrid]
- **Budget Cycle**: [e.g., July-June fiscal year, Calendar year]
- **CapEx vs OpEx Preference**: [CapEx / OpEx / Balanced]
- **Reallocation Flexibility**: [None / Limited / Moderate / High]

- **Approval Thresholds**:

| Role | Threshold |
|------|-----------|
| [Team Lead] | [$50k] |
| [Director] | [$250k] |
| [Investment Committee] | [$1M] |
| [Executive / Board] | [$5M+] |

---

## Change Capacity

*Describe the organisation's capacity to absorb change. This helps AI avoid recommending too much change at once.*

- **Major Initiatives in Flight**: [e.g., 3]
- **Change Fatigue Level**: [Low / Moderate / High / Critical]
- **Adoption Support Available**: [None / Limited / Moderate / Strong]

- **Transformation Programs**:
  - [e.g., Cloud Migration (ends Q4 2025)]
  - [e.g., Digital Customer Experience (ongoing)]
  - [e.g., Core Platform Modernisation (FY26)]

- **Change Blackout Periods**:
  - [e.g., Q4 code freeze (October-December)]
  - [e.g., End of financial year (May-June)]
  - [e.g., Peak trading periods]

---

## Organisational Structure

- **Executive Sponsors**: [e.g., Chief Digital Officer, Chief Claims Officer, CTO — typical sponsors for product initiatives]
- **Product Leadership**: [e.g., CPO with 4 domain PMs, or BU-embedded product managers]
- **Delivery Model**: [e.g., Agile (Scrum), SAFe for large programs, Waterfall for regulatory projects]
- **Key Decision Forums**: [e.g., Investment Committee (monthly), Product Council (fortnightly), Architecture Review Board (weekly)]
- **Gate Approvers**:
  - L0-L1: [e.g., Product Lead]
  - L2: [e.g., Investment Committee]
  - L3+: [e.g., Executive Sponsor + CFO for >$500k]

---

## Architecture Principles

*Document the key architecture principles that guide design decisions. AI will use these to ensure recommendations align with your standards.*

| Principle | Statement | Implications |
|-----------|-----------|--------------|
| [API-First] | [All capabilities must be exposed via APIs before UIs] | [Build APIs first, no direct DB access, invest in API management] |
| [Cloud-Native] | [New systems should be designed for cloud deployment] | [Use managed services, design for horizontal scale, 12-factor apps] |
| [Buy Before Build] | [Prefer COTS/SaaS for non-differentiating capabilities] | [Only custom-build for competitive advantage, evaluate build cost vs buy] |
| [Security by Design] | [Security is not an afterthought] | [Threat modelling required, security review gates, zero-trust approach] |

---

## Competitor Landscape

- **Primary Competitors**: [e.g., IAG, Suncorp, QBE, Allianz]
- **Emerging Disruptors**: [e.g., Insurtechs (Huddle, Upcover), neobanks expanding into insurance, embedded insurance providers]
- **Competitive Differentiators**: [e.g., Broker network strength, claims processing speed, regional presence, brand trust]
- **Market Position**: [e.g., #3 by GWP in personal lines, market leader in commercial motor]

---

## Ubiquitous Language

*Define key domain terms to ensure consistent language across AI outputs. This is critical for domain-driven design.*

| Term | Definition |
|------|------------|
| [Claim] | [A request for indemnity under a policy] |
| [Lodgement] | [The act of submitting a claim for the first time] |
| [Assessment] | [Evaluation of claim validity and determination of quantum] |
| [Settlement] | [Final payment and closure of a claim] |
| [Policy] | [A contract of insurance between insurer and policyholder] |
| [Cover] | [The specific risks insured under a policy] |
| [Premium] | [The amount paid by the customer for insurance coverage] |
| [Excess] | [The amount the policyholder must pay before the insurer pays] |

---

## How to Maintain This Document

- **Review Frequency**: Update at the start of each financial year or after a major strategic shift
- **Owner**: [Name/role responsible for keeping this current]
- **Last Updated**: [Date]

### Tips for Quality Context

1. **Be specific** — "Reduce costs" is weak; "Reduce claims handling cost from $847 to $600 per claim" is strong
2. **Include numbers** — Revenue, customer counts, NPS scores, processing volumes give AI concrete anchors
3. **Name the constraints** — AI cannot navigate constraints it doesn't know about
4. **Keep it current** — Outdated strategy or OKRs produce misaligned outputs
5. **Define your language** — Terms like "customer", "claim", "settlement" mean different things in different contexts
