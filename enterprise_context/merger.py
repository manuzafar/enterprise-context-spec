"""
Context merging utilities.

Implements hierarchical inheritance: company <- division <- team.
"""

from typing import Any


def deep_merge(base: dict, override: dict) -> dict:
    """
    Deep merge two dictionaries.

    Inheritance rules:
    - Lists are concatenated (lower level extends higher)
    - Dicts are recursively merged
    - Scalars are overridden (lower level wins)

    Args:
        base: Base dictionary (higher level context)
        override: Override dictionary (lower level context)

    Returns:
        Merged dictionary

    Example:
        >>> base = {"tech": ["AWS"], "strategy": {"focus": "growth"}}
        >>> override = {"tech": ["Azure"], "strategy": {"budget": "10M"}}
        >>> result = deep_merge(base, override)
        >>> result["tech"]
        ['AWS', 'Azure']
        >>> result["strategy"]
        {'focus': 'growth', 'budget': '10M'}
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

    Inheritance chain: company <- division <- team

    Each level extends lists from higher levels and can override
    scalar values. This produces a single merged context that
    represents the full organizational context for a specific team.

    Args:
        company: Company-level context (base)
        division: Division-level context (extends company)
        team: Team-level context (extends division)

    Returns:
        Merged context dictionary with:
        - All inherited values
        - "_sources" field tracking which levels contributed
        - "schema" field set to "enterprise-context/v1/merged"

    Example:
        >>> company = {"company": "Acme", "tech": ["AWS"]}
        >>> division = {"division": "Ops", "tech": ["Azure"]}
        >>> merged = merge_contexts(company=company, division=division)
        >>> merged["tech"]
        ['AWS', 'Azure']
        >>> merged["_sources"]
        ['company', 'division']
    """
    result: dict[str, Any] = {}

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
