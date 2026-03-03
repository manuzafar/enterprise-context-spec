# Seedcraft Integration

This guide explains how to use Enterprise Context Spec files with [Seedcraft](https://github.com/...), the AI-powered product discovery system.

## Overview

Seedcraft generates comprehensive inception packs for product ideas. With enterprise context, Seedcraft can:

- Align recommendations with your company strategy
- Design for your actual tech stack
- Consider your regulatory requirements
- Reference real stakeholders and decision forums
- Avoid suggesting approaches that failed before

## Usage

### Option 1: File Upload (UI)

1. Navigate to Seedcraft input form
2. Upload your context files:
   - `company-context.md` (required)
   - `division-context.md` (optional)
   - `team-context.md` (optional)
3. Enter your product idea
4. Generate inception pack

### Option 2: API

```python
import requests

response = requests.post(
    "https://api.seedcraft.dev/api/discovery/start",
    json={
        "product_idea": "AI-powered claims triage",
        "context_files": {
            "company": open("company-context.md").read(),
            "division": open("claims-division-context.md").read(),
            "team": open("lodgement-team-context.md").read()
        }
    }
)
```

### Option 3: Python SDK

```python
from seedcraft import DiscoverySession

session = DiscoverySession(
    product_idea="AI-powered claims triage for motor insurance",
    context_files=[
        "company-context.md",
        "claims-division-context.md",
        "lodgement-team-context.md"
    ]
)

pack = await session.generate()
```

## How Context is Used

### Agent: Planner
Uses company strategy and investment themes to assess domain fit.

### Agent: Customer Research
Uses industry, competitors, and market position for research grounding.

### Agent: Business Strategy
Aligns Lean Canvas and value proposition with company OKRs.

### Agent: Technical Architect
Designs for actual tech stack, integration patterns, and constraints.

### Agent: Legal & Regulatory
Uses regulatory frameworks, compliance stance, and data residency requirements.

### Agent: GTM Strategy
Considers competitive differentiators and market position.

### Agent: Stakeholder Views
Generates briefings for actual exec sponsors and decision forums.

### Agent: Critique
Checks strategic alignment against real OKRs and constraints.

## Example

Without context:
> "Consider integrating with a CRM system..."

With context:
> "Integrate with the existing Salesforce CRM via Azure API Management, following the API-first pattern established by the Platform team. Given the conservative compliance stance, ensure APRA CPS 234 requirements are met for any new data flows."

## Best Practices

1. **Start with company context** — Even minimal context improves outputs
2. **Add division for domain-specific work** — Claims initiatives benefit from claims context
3. **Add team for implementation planning** — Constraints and dependencies matter for PRDs
4. **Keep context current** — Outdated OKRs produce misaligned recommendations
