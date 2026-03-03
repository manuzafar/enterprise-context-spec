#!/usr/bin/env python3
"""
Enterprise Context Validator

Validates context files against the Enterprise Context Spec schemas.

Usage:
    python validate.py company-context.md
    python validate.py --schema division division-context.md
    python validate.py --all examples/general-insurance/
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

# Try to import jsonschema, provide helpful message if not installed
try:
    import jsonschema
except ImportError:
    print("Error: jsonschema package required. Install with: pip install jsonschema")
    sys.exit(1)


def load_schema(schema_type: str) -> dict:
    """Load a JSON schema from the spec directory."""
    spec_dir = Path(__file__).parent.parent / "spec" / "v1"
    schema_file = spec_dir / f"{schema_type}.schema.json"

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema not found: {schema_file}")

    with open(schema_file) as f:
        return json.load(f)


def parse_markdown_frontmatter(content: str) -> tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter dict, remaining content)
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
    """
    # For now, just return empty dict
    # Full implementation would parse ## sections
    return {}


def load_context_file(file_path: Path) -> dict:
    """
    Load a context file (markdown or YAML).

    Returns:
        Parsed context dictionary
    """
    content = file_path.read_text()

    if file_path.suffix in [".yaml", ".yml"]:
        return yaml.safe_load(content)

    elif file_path.suffix == ".md":
        frontmatter, body = parse_markdown_frontmatter(content)
        # Merge frontmatter with any parsed body content
        body_data = parse_markdown_sections(body)
        return {**frontmatter, **body_data}

    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")


def detect_schema_type(context: dict) -> str:
    """Detect the schema type from the context."""
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

    Returns:
        List of validation errors (empty if valid)
    """
    schema = load_schema(schema_type)
    validator = jsonschema.Draft202012Validator(schema)

    errors = []
    for error in validator.iter_errors(context):
        path = ".".join(str(p) for p in error.path) if error.path else "(root)"
        errors.append(f"  {path}: {error.message}")

    return errors


def validate_file(file_path: Path, schema_type: str | None = None) -> tuple[bool, list[str]]:
    """
    Validate a single context file.

    Returns:
        Tuple of (is_valid, error_messages)
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


def main():
    parser = argparse.ArgumentParser(
        description="Validate Enterprise Context files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate.py company-context.md
    python validate.py --schema division division-context.md
    python validate.py --all examples/
        """
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Context files or directories to validate"
    )
    parser.add_argument(
        "--schema",
        choices=["company", "division", "team"],
        help="Schema type (auto-detected if not specified)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all .md and .yaml files in directories"
    )

    args = parser.parse_args()

    files_to_validate = []

    for path_str in args.files:
        path = Path(path_str)
        if path.is_dir():
            if args.all:
                files_to_validate.extend(path.glob("**/*.md"))
                files_to_validate.extend(path.glob("**/*.yaml"))
                files_to_validate.extend(path.glob("**/*.yml"))
            else:
                print(f"Warning: {path} is a directory. Use --all to validate all files.")
        elif path.is_file():
            files_to_validate.append(path)
        else:
            print(f"Error: {path} not found")
            sys.exit(1)

    if not files_to_validate:
        print("No files to validate")
        sys.exit(1)

    all_valid = True

    for file_path in files_to_validate:
        # Skip non-context files
        if file_path.name in ["README.md", "CONTRIBUTING.md"]:
            continue

        is_valid, errors = validate_file(file_path, args.schema)

        if is_valid:
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            for error in errors:
                print(error)
            all_valid = False

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
