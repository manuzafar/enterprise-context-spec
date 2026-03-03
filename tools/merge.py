#!/usr/bin/env python3
"""
Enterprise Context Merger

Merges company, division, and team context files with proper inheritance.

Usage:
    python merge.py company.md division.md team.md -o merged.json
    python merge.py company.md -o context.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml


def parse_markdown_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content

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


def load_context_file(file_path: Path) -> dict:
    """Load a context file (markdown or YAML)."""
    content = file_path.read_text()

    if file_path.suffix in [".yaml", ".yml"]:
        return yaml.safe_load(content)
    elif file_path.suffix == ".md":
        frontmatter, _ = parse_markdown_frontmatter(content)
        return frontmatter
    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")


def deep_merge(base: dict, override: dict) -> dict:
    """
    Deep merge two dictionaries.

    Rules:
    - Lists are concatenated (lower level extends higher)
    - Dicts are recursively merged
    - Scalars are overridden (lower level wins)
    """
    result = base.copy()

    for key, value in override.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge dicts
                result[key] = deep_merge(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                # Concatenate lists (extend)
                result[key] = result[key] + value
            else:
                # Override scalar
                result[key] = value
        else:
            result[key] = value

    return result


def merge_contexts(
    company: dict | None = None,
    division: dict | None = None,
    team: dict | None = None
) -> dict:
    """
    Merge context files with inheritance.

    Inheritance: company <- division <- team
    """
    result = {}

    # Track sources for debugging
    result["_sources"] = []

    if company:
        result = deep_merge(result, company)
        result["_sources"].append("company")

    if division:
        result = deep_merge(result, division)
        result["_sources"].append("division")

    if team:
        result = deep_merge(result, team)
        result["_sources"].append("team")

    # Add merged schema identifier
    result["schema"] = "enterprise-context/v1/merged"

    return result


def detect_context_level(context: dict) -> str:
    """Detect whether a context is company, division, or team level."""
    schema = context.get("schema", "")

    if "company" in schema or "company" in context:
        return "company"
    elif "division" in schema or "division" in context:
        return "division"
    elif "team" in schema or "team" in context:
        return "team"

    return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Merge Enterprise Context files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python merge.py company.md division.md team.md -o merged.json
    python merge.py company.md division.md -o context.json
    python merge.py company.md -o context.yaml
        """
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Context files to merge (order: company, division, team)"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output file (supports .json and .yaml)"
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print output (default: true)"
    )

    args = parser.parse_args()

    # Load and categorize files
    contexts = {"company": None, "division": None, "team": None}

    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"Error: {path} not found")
            sys.exit(1)

        try:
            context = load_context_file(path)
        except Exception as e:
            print(f"Error loading {path}: {e}")
            sys.exit(1)

        level = detect_context_level(context)
        if level == "unknown":
            print(f"Warning: Could not detect level for {path}, skipping")
            continue

        if contexts[level] is not None:
            print(f"Warning: Multiple {level} contexts provided, using last one")

        contexts[level] = context
        print(f"Loaded {level} context from {path}")

    # Merge
    merged = merge_contexts(
        company=contexts["company"],
        division=contexts["division"],
        team=contexts["team"]
    )

    # Output
    output_path = Path(args.output)

    if output_path.suffix == ".json":
        output_content = json.dumps(merged, indent=2 if args.pretty else None)
    elif output_path.suffix in [".yaml", ".yml"]:
        output_content = yaml.dump(merged, default_flow_style=False, sort_keys=False)
    else:
        print(f"Error: Unsupported output format: {output_path.suffix}")
        sys.exit(1)

    output_path.write_text(output_content)
    print(f"\nMerged context written to {output_path}")
    print(f"Sources: {', '.join(merged['_sources'])}")


if __name__ == "__main__":
    main()
