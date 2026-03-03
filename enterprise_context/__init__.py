"""
Enterprise Context Spec - Organizational context for AI agents.

An open standard for defining organizational context that AI agents can consume.
"""

__version__ = "0.1.0"

from enterprise_context.loader import (
    load_context,
    load_context_file,
    parse_markdown_frontmatter,
)
from enterprise_context.merger import (
    deep_merge,
    merge_contexts,
)
from enterprise_context.validator import (
    validate_context,
    validate_file,
)

__all__ = [
    "__version__",
    # Loader
    "load_context",
    "load_context_file",
    "parse_markdown_frontmatter",
    # Merger
    "deep_merge",
    "merge_contexts",
    # Validator
    "validate_context",
    "validate_file",
]
