"""
Schema loading utilities.

Provides access to bundled JSON schemas for validation.
"""

import json
from pathlib import Path
from functools import lru_cache


SCHEMA_DIR = Path(__file__).parent


@lru_cache(maxsize=3)
def load_schema(schema_type: str) -> dict:
    """
    Load a JSON schema from the bundled schemas.

    Args:
        schema_type: One of "company", "division", "team"

    Returns:
        Parsed JSON schema dictionary

    Raises:
        FileNotFoundError: If schema file doesn't exist
        ValueError: If schema_type is invalid
    """
    if schema_type not in ("company", "division", "team"):
        raise ValueError(f"Invalid schema type: {schema_type}. Must be one of: company, division, team")

    schema_file = SCHEMA_DIR / f"{schema_type}.schema.json"

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema not found: {schema_file}")

    with open(schema_file) as f:
        return json.load(f)


def get_schema_path(schema_type: str) -> Path:
    """
    Get the path to a schema file.

    Args:
        schema_type: One of "company", "division", "team"

    Returns:
        Path to the schema file
    """
    return SCHEMA_DIR / f"{schema_type}.schema.json"


def list_schemas() -> list[str]:
    """
    List available schema types.

    Returns:
        List of schema type names
    """
    return ["company", "division", "team"]
