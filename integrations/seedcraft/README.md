# Seedcraft Integration

> **Coming Soon** — Direct SDK integration is planned but not yet implemented. Track progress in [Issue #2](https://github.com/enterprise-context/enterprise-context-spec/issues/2).

This document describes how Enterprise Context Spec files work with [Seedcraft](https://github.com/seedcraft-ai/seedcraft), the AI-powered product discovery system.

## Current Status

Seedcraft can consume Enterprise Context files, but the dedicated SDK integration shown in the examples below is not yet available.

## How to Use Today

### Option 1: Manual Context (Recommended)

Copy your context into Seedcraft's "Additional Context" field:

1. Merge your context files using the CLI:
   ```bash
   ec merge company.md division.md team.md -o merged.json
   ```

2. Copy the merged context into Seedcraft's input form

### Option 2: API (Direct JSON)

```python
import requests
from enterprise_context import load_context, merge_contexts

# Load and merge contexts
company = load_context("company-context.md")
division = load_context("division-context.md")
context = merge_contexts(company, division)

# Include in API request
response = requests.post(
    "https://api.seedcraft.dev/api/discovery/start",
    json={
        "product_idea": "AI-powered claims triage",
        "additional_context": context  # Pass merged context
    }
)
```

## How Context Improves Outputs

When Seedcraft has enterprise context, its agents can:

| Agent | Uses Context For |
|-------|------------------|
| **Planner** | Strategy alignment, investment themes |
| **Customer Research** | Industry, competitors, market position |
| **Business Strategy** | OKRs, funding model, risk appetite |
| **Technical Architect** | Tech stack, integration patterns, constraints |
| **Legal & Regulatory** | Compliance frameworks, data residency |
| **GTM Strategy** | Competitive differentiators, market position |
| **Critique** | Strategic alignment validation |

## Example

**Without context:**
> "Consider integrating with a CRM system..."

**With context:**
> "Integrate with the existing Salesforce CRM via Azure API Management, following the API-first pattern. Given the conservative compliance stance, ensure regulatory requirements are met for any new data flows."

## Planned SDK Usage

When the SDK integration is implemented:

```python
# This will work when the SDK is available
from seedcraft import DiscoverySession

session = DiscoverySession(
    product_idea="AI-powered claims triage for motor insurance",
    context_files=[
        "company-context.md",
        "division-context.md",
        "team-context.md"
    ]
)

pack = await session.generate()
```

## Contributing

Want to help implement this integration? See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## License

MIT License
