# LangChain Integration

> **Coming Soon** — This integration is planned but not yet implemented. Track progress in [Issue #1](https://github.com/enterprise-context/enterprise-context-spec/issues/1).

This document describes the planned LangChain integration for loading Enterprise Context Spec files as LangChain documents.

## Planned Features

When implemented, this integration will provide:

- **EnterpriseContextLoader** — Load context files as LangChain documents
- **EnterpriseContextRetriever** — Custom retriever for context-aware RAG
- **Inheritance merging** — Automatic company → division → team merging
- **Section-based splitting** — Split contexts by section for better retrieval

## Current Alternative

Until the LangChain integration is implemented, you can use the core package:

```python
from enterprise_context import load_context, merge_contexts

# Load context files
company = load_context("company-context.md")
division = load_context("division-context.md")
team = load_context("team-context.md")

# Merge with inheritance
context = merge_contexts(company, division, team)

# Use in your LangChain pipeline
from langchain.schema import Document

doc = Document(
    page_content=str(context),
    metadata={"source": "enterprise-context", "schema": "merged"}
)
```

## Planned Usage

```python
# This will work when the integration is implemented
from enterprise_context.langchain import EnterpriseContextLoader

loader = EnterpriseContextLoader([
    "company-context.md",
    "division-context.md",
    "team-context.md"
])

docs = loader.load()
```

## Contributing

Want to help implement this integration? See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Enterprise Context Spec](../../README.md)
- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)

## License

MIT License
