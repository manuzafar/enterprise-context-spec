"""
Schema validation utilities.

Validates context files against Enterprise Context Spec JSON schemas.
"""

from pathlib import Path
from typing import Any

import jsonschema

from enterprise_context.loader import load_context_file
from enterprise_context.schemas import load_schema


def detect_schema_type(context: dict) -> str:
    """
    Detect the schema type from the context.

    Args:
        context: Parsed context dictionary

    Returns:
        Schema type: "company", "division", or "team"

    Raises:
        ValueError: If schema type cannot be detected
    """
    schema = context.get("schema", "")

    if "company" in schema:
        return "company"
    elif "division" in schema:
        return "division"
    elif "team" in schema:
        return "team"

    # Try to guess from content
    if "company" in context:
        return "company"
    elif "division" in context:
        return "division"
    elif "team" in context:
        return "team"

    raise ValueError("Could not detect schema type. Add 'schema' field to frontmatter.")


def validate_context(context: dict, schema_type: str) -> list[str]:
    """
    Validate a context dictionary against its schema.

    Args:
        context: Parsed context dictionary
        schema_type: One of "company", "division", "team"

    Returns:
        List of validation errors (empty if valid)

    Example:
        >>> context = {"company": "Acme", "industry": "Tech"}
        >>> errors = validate_context(context, "company")
        >>> len(errors)
        0
    """
    schema = load_schema(schema_type)
    validator = jsonschema.Draft202012Validator(schema)

    errors = []
    for error in validator.iter_errors(context):
        path = ".".join(str(p) for p in error.path) if error.path else "(root)"
        errors.append(f"  {path}: {error.message}")

    return errors


def validate_file(
    file_path: Path | str,
    schema_type: str | None = None
) -> tuple[bool, list[str]]:
    """
    Validate a single context file.

    Args:
        file_path: Path to the context file
        schema_type: Schema type (auto-detected if not specified)

    Returns:
        Tuple of (is_valid, error_messages)

    Example:
        >>> is_valid, errors = validate_file("company-context.md")
        >>> if not is_valid:
        ...     for error in errors:
        ...         print(error)
    """
    try:
        context = load_context_file(file_path)
    except Exception as e:
        return False, [f"  Failed to parse file: {e}"]

    if schema_type is None:
        try:
            schema_type = detect_schema_type(context)
        except ValueError as e:
            return False, [f"  {e}"]

    errors = validate_context(context, schema_type)
    return len(errors) == 0, errors
