# Contributing to Enterprise Context Spec

Thank you for your interest in contributing! This document provides guidelines for contributing to the Enterprise Context Spec.

## Ways to Contribute

### 1. Industry Templates

Add context templates for your industry:

```
examples/
├── healthcare/
│   ├── company-context.md
│   ├── clinical-division-context.md
│   └── nursing-team-context.md
```

**Guidelines:**
- Use realistic but fictional company names
- Include industry-specific regulations
- Add relevant tech stack examples
- Include common stakeholder roles

### 2. Schema Improvements

Propose changes to the JSON Schema:

1. Open an issue describing the proposed change
2. Discuss with maintainers
3. Submit a PR with schema changes + updated templates

**Guidelines:**
- Backwards compatibility is important
- New fields should be optional unless critical
- Include examples of how the field would be used

### 3. Integrations

Add integrations for AI tools:

```
integrations/
├── your-tool/
│   ├── README.md
│   ├── loader.py
│   └── examples/
```

### 4. Documentation

Improve docs, fix typos, add examples.

## Development Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_ORG/enterprise-context-spec.git
cd enterprise-context-spec

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Validate all examples
python tools/validate.py examples/**/*.md
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Run validation (`python tools/validate.py`)
5. Commit with clear messages
6. Push and open a PR

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn

## Questions?

Open an issue or start a discussion. We're happy to help!
