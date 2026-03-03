"""
Command-line interface for Enterprise Context Spec.

Provides commands for validating and merging context files.
"""

import json
import sys
from pathlib import Path

import click
import yaml

from enterprise_context.loader import load_context_file, detect_context_level
from enterprise_context.merger import merge_contexts
from enterprise_context.validator import validate_file


@click.group()
@click.version_option()
def main():
    """Enterprise Context Spec CLI.

    Tools for validating and merging organizational context files.
    """
    pass


@main.command()
@click.argument("files", nargs=-1, required=True, type=click.Path(exists=True))
@click.option(
    "--schema",
    type=click.Choice(["company", "division", "team"]),
    help="Schema type (auto-detected if not specified)"
)
@click.option(
    "--all", "validate_all",
    is_flag=True,
    help="Validate all .md and .yaml files in directories"
)
def validate(files: tuple[str, ...], schema: str | None, validate_all: bool):
    """Validate Enterprise Context files against schemas.

    Examples:

        ec validate company-context.md

        ec validate --schema division division-context.md

        ec validate --all examples/
    """
    files_to_validate: list[Path] = []

    for path_str in files:
        path = Path(path_str)
        if path.is_dir():
            if validate_all:
                files_to_validate.extend(path.glob("**/*.md"))
                files_to_validate.extend(path.glob("**/*.yaml"))
                files_to_validate.extend(path.glob("**/*.yml"))
            else:
                click.echo(f"Warning: {path} is a directory. Use --all to validate all files.")
        elif path.is_file():
            files_to_validate.append(path)
        else:
            click.echo(f"Error: {path} not found", err=True)
            sys.exit(1)

    if not files_to_validate:
        click.echo("No files to validate")
        sys.exit(1)

    all_valid = True

    for file_path in files_to_validate:
        # Skip non-context files
        if file_path.name in ["README.md", "CONTRIBUTING.md"]:
            continue

        is_valid, errors = validate_file(file_path, schema)

        if is_valid:
            click.echo(f"✅ {file_path}")
        else:
            click.echo(f"❌ {file_path}")
            for error in errors:
                click.echo(error)
            all_valid = False

    sys.exit(0 if all_valid else 1)


@main.command()
@click.argument("files", nargs=-1, required=True, type=click.Path(exists=True))
@click.option(
    "-o", "--output",
    required=True,
    type=click.Path(),
    help="Output file (supports .json and .yaml)"
)
@click.option(
    "--pretty/--no-pretty",
    default=True,
    help="Pretty-print output (default: true)"
)
def merge(files: tuple[str, ...], output: str, pretty: bool):
    """Merge Enterprise Context files with inheritance.

    Merges company, division, and team context files into a single
    context with proper inheritance (company <- division <- team).

    Examples:

        ec merge company.md division.md team.md -o merged.json

        ec merge company.md division.md -o context.json

        ec merge company.md -o context.yaml
    """
    # Load and categorize files
    contexts = {"company": None, "division": None, "team": None}

    for path_str in files:
        path = Path(path_str)
        if not path.exists():
            click.echo(f"Error: {path} not found", err=True)
            sys.exit(1)

        try:
            context = load_context_file(path)
        except Exception as e:
            click.echo(f"Error loading {path}: {e}", err=True)
            sys.exit(1)

        level = detect_context_level(context)
        if level == "unknown":
            click.echo(f"Warning: Could not detect level for {path}, skipping")
            continue

        if contexts[level] is not None:
            click.echo(f"Warning: Multiple {level} contexts provided, using last one")

        contexts[level] = context
        click.echo(f"Loaded {level} context from {path}")

    # Merge
    merged = merge_contexts(
        company=contexts["company"],
        division=contexts["division"],
        team=contexts["team"]
    )

    # Output
    output_path = Path(output)

    if output_path.suffix == ".json":
        output_content = json.dumps(merged, indent=2 if pretty else None)
    elif output_path.suffix in [".yaml", ".yml"]:
        output_content = yaml.dump(merged, default_flow_style=False, sort_keys=False)
    else:
        click.echo(f"Error: Unsupported output format: {output_path.suffix}", err=True)
        sys.exit(1)

    output_path.write_text(output_content)
    click.echo(f"\nMerged context written to {output_path}")
    click.echo(f"Sources: {', '.join(merged['_sources'])}")


if __name__ == "__main__":
    main()
