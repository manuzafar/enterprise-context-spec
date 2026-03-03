"""
Context file loading utilities.

Handles loading enterprise context from markdown and YAML files.
"""

from pathlib import Path
from typing import Any

import yaml


def parse_markdown_frontmatter(content: str) -> tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content.

    Args:
        content: Raw markdown content with optional YAML frontmatter

    Returns:
        Tuple of (frontmatter dict, remaining body content)

    Example:
        >>> content = '''---
        ... schema: enterprise-context/v1/company
        ... company: Acme Corp
        ... ---
        ... # Company Context
        ... '''
        >>> frontmatter, body = parse_markdown_frontmatter(content)
        >>> frontmatter['company']
        'Acme Corp'
    """
    if not content.startswith("---"):
        return {}, content

    # Find the closing ---
    end_index = content.find("---", 3)
    if end_index == -1:
        return {}, content

    frontmatter_str = content[3:end_index].strip()
    body = content[end_index + 3:].strip()

    try:
        frontmatter = yaml.safe_load(frontmatter_str) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML frontmatter: {e}")

    return frontmatter, body


def parse_markdown_sections(content: str) -> dict[str, Any]:
    """
    Parse markdown sections into a dictionary.

    This is a simplified parser that extracts key information
    from the markdown body to complement the frontmatter.

    Currently returns empty dict - frontmatter is the primary source.
    """
    # For now, just return empty dict
    # Full implementation would parse ## sections
    return {}


def load_context_file(file_path: Path | str) -> dict:
    """
    Load a context file (markdown or YAML).

    Args:
        file_path: Path to the context file (.md, .yaml, or .yml)

    Returns:
        Parsed context dictionary

    Raises:
        ValueError: If file type is unsupported
        FileNotFoundError: If file doesn't exist
    """
    path = Path(file_path)
    content = path.read_text()

    if path.suffix in [".yaml", ".yml"]:
        return yaml.safe_load(content)

    elif path.suffix == ".md":
        frontmatter, body = parse_markdown_frontmatter(content)
        # Merge frontmatter with any parsed body content
        body_data = parse_markdown_sections(body)
        return {**frontmatter, **body_data}

    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")


def load_context(file_path: Path | str) -> dict:
    """
    Load a context file. Alias for load_context_file.

    Args:
        file_path: Path to the context file

    Returns:
        Parsed context dictionary
    """
    return load_context_file(file_path)


def detect_context_level(context: dict) -> str:
    """
    Detect whether a context is company, division, or team level.

    Args:
        context: Parsed context dictionary

    Returns:
        One of "company", "division", "team", or "unknown"
    """
    schema = context.get("schema", "")

    if "company" in schema or "company" in context:
        return "company"
    elif "division" in schema or "division" in context:
        return "division"
    elif "team" in schema or "team" in context:
        return "team"

    return "unknown"
