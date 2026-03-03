# Getting Started with Enterprise Context Spec

This guide will help you create your first enterprise context files.

## Overview

Enterprise Context Spec defines a standard way to capture organizational context that AI agents can consume. Instead of re-explaining your company, strategy, and constraints to every AI tool, you write it once and use it everywhere.

## Quick Start (5 minutes)

### Step 1: Copy the Template

```bash
# Clone the repo
git clone https://github.com/YOUR_ORG/enterprise-context-spec.git
cd enterprise-context-spec

# Copy the company template
cp templates/company-context.md my-company-context.md
```

### Step 2: Fill in the Basics

Open `my-company-context.md` and fill in the essentials:

```markdown
---
schema: enterprise-context/v1/company
company: "Acme Corp"
industry: "Financial Services"
updated: "2025-03-01"
---

# Company Context

## Company & Industry
- **Company**: Acme Corp
- **Industry**: Financial Services
- **Business Units**: Retail Banking, Commercial, Wealth
- **Company Size**: 5,000 employees, $2B revenue

## Strategic Priorities
- **Current Strategy**: Digital transformation, cost efficiency
- **Investment Themes**: AI/ML, Cloud migration, Self-service
```

You don't need to fill everything — start with what you know. AI agents will work with partial context and ask for what's missing.

### Step 3: Validate

```bash
python tools/validate.py my-company-context.md
```

### Step 4: Use with an AI Agent

```python
# Example with Seedcraft
from seedcraft import DiscoverySession

session = DiscoverySession(
    product_idea="AI-powered expense management",
    context_files=["my-company-context.md"]
)
```

## The Three Levels

### Company Context (Required)

Company-wide context that applies to all initiatives:

- Company identity and size
- Strategic priorities and OKRs
- Technology landscape
- Regulatory posture
- Organizational structure
- Competitive landscape

**Owner**: Strategy or Transformation team
**Update frequency**: Annually

### Division Context (Optional)

Business unit or division-specific context:

- Division strategy and OKRs
- Division-specific systems
- Additional regulations
- Key stakeholders

**Owner**: Division head or PM lead
**Update frequency**: Quarterly

### Team Context (Optional)

Team-level context for specific initiatives:

- Current state and known issues
- Team constraints
- Dependencies
- Target users

**Owner**: Product Manager
**Update frequency**: As needed

## Inheritance

Lower levels inherit from and extend higher levels:

```
Company: core_systems = [SAP, Salesforce]
Division: core_systems = [Guidewire]
→ Merged: core_systems = [SAP, Salesforce, Guidewire]

Company: compliance_stance = "conservative"
Division: compliance_stance = "moderate"
→ Merged: compliance_stance = "moderate" (overridden)
```

## Tips for Good Context

### 1. Be Specific

❌ "Reduce costs"
✅ "Reduce claims handling cost from $847 to $600 per claim"

### 2. Include Numbers

❌ "Large customer base"
✅ "1.2M active customers, 15% growth YoY"

### 3. Name Your Constraints

AI can't navigate constraints it doesn't know about:

✅ "Must integrate with existing Guidewire instance — no platform change approved"
✅ "Australian data residency required — no offshore processing"

### 4. Document Previous Attempts

This prevents AI from suggesting things that have already failed:

```markdown
### Previous Attempts
| Initiative | Year | Outcome | Learnings |
|------------|------|---------|-----------|
| Mobile app | 2019 | Cancelled | Integration too complex |
```

### 5. Keep It Current

Outdated strategy or OKRs produce misaligned outputs. Review:
- Company context: Annually
- Division context: Quarterly
- Team context: As circumstances change

## Next Steps

1. **Start simple** — Create company context first
2. **Add depth gradually** — Add division and team as needed
3. **Validate often** — Use the CLI to check your files
4. **Share with your team** — Context files work best when maintained by the right owners

## Need Help?

- [Full Schema Reference](schema-reference.md)
- [Examples](../examples/)
- [FAQ](faq.md)
