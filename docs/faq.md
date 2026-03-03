# Frequently Asked Questions

## General

### What is Enterprise Context Spec?

An open standard for defining organizational context that AI agents can consume. Write your company's context once, use it with any compatible AI tool.

### Why do I need this?

Every AI agent needs to understand your organization — strategy, tech stack, regulations, constraints. Today, you re-explain this every session. With Enterprise Context Spec, you write it once and reuse it.

### Is this just for large enterprises?

No. The spec scales from startups to large enterprises. Start with a simple company context (name, industry, key constraints) and add detail as needed.

## Files and Format

### Why markdown instead of JSON/YAML?

Markdown with YAML frontmatter gives you the best of both worlds:
- **Human readable** — Anyone can edit it
- **Machine parseable** — AI agents can consume it
- **Version controllable** — Lives in git like code
- **Documentation friendly** — Renders nicely in GitHub, Notion, Confluence

We also support pure YAML for automation use cases.

### Do I need all three levels (company/division/team)?

No. Only company context is required. Division and team are optional and add depth when needed.

### How do I handle sensitive information?

Context files should contain **structural** information, not secrets:

✅ "We use Azure for cloud infrastructure"
✅ "APRA CPS 234 compliance required"
❌ API keys, passwords, or credentials
❌ Specific customer data

For sensitive details, reference them without including them:
"See internal wiki for detailed security architecture"

### Can I have multiple company contexts?

The spec assumes one company context per organization. If you're a holding company with distinct subsidiaries, each can have its own company context.

## Integration

### How do AI agents use these files?

Agents parse the context and use it to:
- Ground their responses in your reality
- Check strategic alignment
- Suggest appropriate technologies
- Consider relevant regulations
- Reference actual stakeholders

### Does this work with ChatGPT/Claude/Gemini?

Yes. You can paste context file contents directly into any LLM. For better experiences, use tools that natively support the spec (like Seedcraft).

### How do I integrate with my own agents?

```python
from enterprise_context import load_context, merge_contexts

# Load files
company = load_context("company-context.md")
division = load_context("division-context.md")

# Merge with inheritance
context = merge_contexts(company, division)

# Use in your agent prompt
prompt = f"""
Given this organizational context:
{json.dumps(context, indent=2)}

Help me with: {user_request}
"""
```

## Maintenance

### How often should I update context files?

| Level | Frequency | Trigger |
|-------|-----------|---------|
| Company | Annually | Strategy refresh, major reorg |
| Division | Quarterly | OKR cycles, divisional changes |
| Team | As needed | Significant constraint changes |

### Who should own each file?

| Level | Owner |
|-------|-------|
| Company | Strategy/Transformation team |
| Division | Division head or PM lead |
| Team | Product Manager |

### What if information conflicts between levels?

Lower levels override higher levels for scalar values. The merge logic is:
- **Scalars**: Team > Division > Company
- **Lists**: Concatenated (all values kept)
- **Objects**: Deep merged

## Troubleshooting

### Validation fails — what do I check?

1. **YAML frontmatter syntax** — Ensure proper `---` delimiters
2. **Required fields** — `company` and `industry` are required for company context
3. **Schema identifier** — Add `schema: enterprise-context/v1/company` to frontmatter

### AI agent ignores my context

1. **Check file is loaded** — Verify the agent confirms context ingestion
2. **Be more specific** — Vague context produces vague outputs
3. **Reduce ambiguity** — If two contexts conflict, agent may guess wrong

### Context feels outdated

Set calendar reminders:
- July: Review company context (FY planning)
- End of each quarter: Review division context
- Start of each initiative: Review team context
