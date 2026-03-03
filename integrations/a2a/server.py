#!/usr/bin/env python3
"""
Enterprise Context A2A Server

Exposes Enterprise Context Spec as an A2A-compliant service, enabling
any A2A-enabled agent to query organizational context.

Usage:
    python server.py --context-dir /path/to/context --port 8080

Environment Variables:
    CONTEXT_DIR: Path to context files directory
    PORT: Server port (default: 8080)
    HOST: Server host (default: 0.0.0.0)
    AUTH_TYPE: Authentication type (bearer, apiKey, none)
    AUTH_SECRET: Secret for authentication
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Load agent card
AGENT_CARD_PATH = Path(__file__).parent / "agent_card.json"


# ============================================================================
# Context Loading (reused from tools/merge.py)
# ============================================================================

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
    """Deep merge with list concatenation and scalar override."""
    result = base.copy()

    for key, value in override.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key] = result[key] + value
            else:
                result[key] = value
        else:
            result[key] = value

    return result


# ============================================================================
# Context Manager
# ============================================================================

class ContextManager:
    """Manages enterprise context files and provides query capabilities."""

    def __init__(self, context_dir: Path):
        self.context_dir = context_dir
        self.contexts: dict[str, dict] = {}
        self.load_all_contexts()

    def load_all_contexts(self):
        """Load all context files from directory."""
        self.contexts = {
            "company": None,
            "divisions": {},
            "teams": {}
        }

        for file_path in self.context_dir.glob("**/*.md"):
            if file_path.name in ["README.md", "CONTRIBUTING.md"]:
                continue

            try:
                context = load_context_file(file_path)
                self._categorize_context(context, file_path)
            except Exception as e:
                print(f"Warning: Failed to load {file_path}: {e}")

    def _categorize_context(self, context: dict, file_path: Path):
        """Categorize a loaded context by type."""
        schema = context.get("schema", "")

        if "company" in schema or "company" in context:
            self.contexts["company"] = context
        elif "division" in schema or "division" in context:
            division_name = context.get("division", file_path.stem)
            self.contexts["divisions"][division_name] = context
        elif "team" in schema or "team" in context:
            team_name = context.get("team", file_path.stem)
            self.contexts["teams"][team_name] = context

    def get_context(
        self,
        level: str,
        division: str | None = None,
        team: str | None = None,
        sections: list[str] | None = None
    ) -> dict:
        """Get merged context at specified level."""
        result = {}

        # Always include company context
        if self.contexts["company"]:
            result = deep_merge(result, self.contexts["company"])

        # Add division context if requested
        if level in ["division", "team"] and division:
            if division in self.contexts["divisions"]:
                result = deep_merge(result, self.contexts["divisions"][division])
            else:
                # Try case-insensitive match
                for div_name, div_context in self.contexts["divisions"].items():
                    if div_name.lower() == division.lower():
                        result = deep_merge(result, div_context)
                        break

        # Add team context if requested
        if level == "team" and team:
            if team in self.contexts["teams"]:
                result = deep_merge(result, self.contexts["teams"][team])
            else:
                # Try case-insensitive match
                for team_name, team_context in self.contexts["teams"].items():
                    if team_name.lower() == team.lower():
                        result = deep_merge(result, team_context)
                        break

        # Filter sections if specified
        if sections:
            filtered = {}
            for section in sections:
                if section in result:
                    filtered[section] = result[section]
            result = filtered

        result["_level"] = level
        result["_retrieved_at"] = datetime.utcnow().isoformat()

        return result

    def check_constraints(
        self,
        action: str,
        team: str | None = None,
        action_type: str | None = None,
        estimated_cost: float | None = None,
        target_date: str | None = None
    ) -> dict:
        """Check if an action violates any constraints."""
        context = self.get_context(
            level="team" if team else "company",
            team=team
        )

        concerns = []
        blockers = []
        relevant_constraints = []

        # Check budget constraints
        if estimated_cost and "funding_model" in context:
            thresholds = context["funding_model"].get("approval_thresholds", {})
            for role, threshold in thresholds.items():
                # Parse threshold (e.g., "$500k" -> 500000)
                if isinstance(threshold, str):
                    match = re.search(r'\$?([\d.]+)([kKmM])?', threshold)
                    if match:
                        value = float(match.group(1))
                        multiplier = match.group(2)
                        if multiplier and multiplier.lower() == 'k':
                            value *= 1000
                        elif multiplier and multiplier.lower() == 'm':
                            value *= 1000000

                        if estimated_cost > value:
                            relevant_constraints.append({
                                "type": "budget",
                                "constraint": f"{role} approval required for amounts over {threshold}",
                                "threshold": threshold
                            })

        # Check timeline constraints (blackout periods)
        if target_date and "change_capacity" in context:
            blackouts = context["change_capacity"].get("blackout_periods", [])
            for blackout in blackouts:
                if isinstance(blackout, str) and "december" in blackout.lower():
                    if target_date and target_date.startswith("12") or "-12-" in target_date:
                        blockers.append(f"Target date falls within blackout period: {blackout}")
                        relevant_constraints.append({
                            "type": "timeline",
                            "constraint": blackout
                        })

        # Check regulatory constraints
        if "regulatory" in context:
            compliance_stance = context["regulatory"].get("compliance_stance", "moderate")
            if compliance_stance in ["conservative", "very_conservative"]:
                if action_type == "regulatory" or "compliance" in action.lower():
                    concerns.append(f"Organization has {compliance_stance} compliance stance - extra scrutiny required")

        # Check risk appetite
        if "risk_appetite" in context:
            risk = context["risk_appetite"]
            if action_type == "technical" and risk.get("technology") == "conservative":
                concerns.append("Conservative technology risk appetite - prefer proven solutions")
            if risk.get("regulatory") == "very_conservative":
                concerns.append("Very conservative regulatory stance - engage compliance early")

        # Check team capacity
        if team and "cognitive_load" in context:
            capacity = context["cognitive_load"].get("spare_capacity", "moderate")
            if capacity in ["low", "none"]:
                concerns.append(f"Team has {capacity} spare capacity - may impact delivery")

        # Check change capacity
        if "change_capacity" in context:
            fatigue = context["change_capacity"].get("change_fatigue", "moderate")
            if fatigue == "high":
                concerns.append("Organization experiencing high change fatigue")

        allowed = len(blockers) == 0

        return {
            "allowed": allowed,
            "confidence": 0.8 if relevant_constraints else 0.6,
            "concerns": concerns,
            "blockers": blockers,
            "relevant_constraints": relevant_constraints,
            "recommendations": self._generate_recommendations(concerns, blockers)
        }

    def _generate_recommendations(self, concerns: list, blockers: list) -> list[str]:
        """Generate recommendations based on concerns and blockers."""
        recommendations = []

        if any("blackout" in b.lower() for b in blockers):
            recommendations.append("Consider rescheduling to avoid blackout period")

        if any("capacity" in c.lower() for c in concerns):
            recommendations.append("Discuss with team lead about capacity before committing")

        if any("compliance" in c.lower() or "regulatory" in c.lower() for c in concerns):
            recommendations.append("Engage compliance team early in planning")

        if any("conservative" in c.lower() for c in concerns):
            recommendations.append("Prepare additional justification and risk mitigation")

        return recommendations

    def get_stakeholders(
        self,
        initiative_type: str,
        estimated_cost: float | None = None,
        team: str | None = None,
        division: str | None = None
    ) -> dict:
        """Identify stakeholders for an initiative."""
        context = self.get_context(
            level="team" if team else ("division" if division else "company"),
            division=division,
            team=team
        )

        approvers = []
        stakeholders = []
        decision_forum = None
        gate_level = "L0"

        # Determine gate level based on cost
        if estimated_cost:
            thresholds = context.get("funding_model", {}).get("approval_thresholds", {})
            for role, threshold in thresholds.items():
                if isinstance(threshold, str):
                    match = re.search(r'\$?([\d.]+)([kKmM])?', threshold)
                    if match:
                        value = float(match.group(1))
                        multiplier = match.group(2)
                        if multiplier and multiplier.lower() == 'k':
                            value *= 1000
                        elif multiplier and multiplier.lower() == 'm':
                            value *= 1000000

                        if estimated_cost <= value:
                            approvers.append({
                                "name": role,
                                "role": role,
                                "threshold": threshold
                            })
                            break

        # Add stakeholders from context
        if "stakeholders" in context:
            for stakeholder in context.get("stakeholders", []):
                if isinstance(stakeholder, dict):
                    stakeholders.append(stakeholder)

        # Determine decision forum
        if "organization" in context:
            forums = context["organization"].get("decision_forums", {})
            if initiative_type == "technical":
                decision_forum = forums.get("architecture", "Architecture Review Board")
            elif initiative_type == "product":
                decision_forum = forums.get("product", "Product Council")
            elif initiative_type == "budget":
                decision_forum = forums.get("investment", "Investment Committee")

        return {
            "approvers": approvers,
            "stakeholders": stakeholders,
            "decision_forum": decision_forum,
            "gate_level": gate_level
        }

    def get_ubiquitous_language(
        self,
        terms: list[str] | None = None,
        division: str | None = None
    ) -> dict:
        """Get domain terminology definitions."""
        context = self.get_context(
            level="division" if division else "company",
            division=division
        )

        language = context.get("ubiquitous_language", {})

        if terms:
            return {term: language.get(term, "Term not defined") for term in terms}

        return language

    def check_team_capacity(
        self,
        team: str,
        work_type: str | None = None,
        estimated_effort: str | None = None
    ) -> dict:
        """Check team capacity for additional work."""
        context = self.get_context(level="team", team=team)

        cognitive_load = context.get("cognitive_load", {})

        spare_capacity = cognitive_load.get("spare_capacity", "unknown")
        current_load = "moderate"

        if spare_capacity in ["none", "low"]:
            current_load = "high" if spare_capacity == "low" else "overloaded"
        elif spare_capacity == "high":
            current_load = "low"

        has_capacity = spare_capacity not in ["none", "low"]

        blockers = []
        if "load_concerns" in cognitive_load:
            blockers = cognitive_load["load_concerns"]

        recommendation = "Team has capacity for additional work"
        if not has_capacity:
            recommendation = "Consider deferring or finding alternative team"
        elif current_load == "moderate":
            recommendation = "Proceed with caution, monitor team load"

        return {
            "has_capacity": has_capacity,
            "current_load": current_load,
            "spare_capacity": spare_capacity,
            "blockers": blockers,
            "recommendation": recommendation
        }


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="Enterprise Context A2A Server",
    description="A2A-compliant server exposing Enterprise Context Spec",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global context manager (initialized on startup)
context_manager: ContextManager | None = None


# ============================================================================
# Request/Response Models
# ============================================================================

class JsonRpcRequest(BaseModel):
    jsonrpc: str = "2.0"
    method: str
    params: dict = {}
    id: str | int | None = None


class JsonRpcResponse(BaseModel):
    jsonrpc: str = "2.0"
    result: Any = None
    error: dict | None = None
    id: str | int | None = None


# ============================================================================
# Authentication
# ============================================================================

def verify_auth(
    authorization: str | None = Header(None),
    x_api_key: str | None = Header(None)
) -> bool:
    """Verify authentication based on configured scheme."""
    auth_type = os.environ.get("AUTH_TYPE", "none")
    auth_secret = os.environ.get("AUTH_SECRET", "")

    if auth_type == "none":
        return True

    if auth_type == "bearer" and authorization:
        token = authorization.replace("Bearer ", "")
        return token == auth_secret

    if auth_type == "apiKey" and x_api_key:
        return x_api_key == auth_secret

    return False


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/.well-known/agent.json")
async def get_agent_card():
    """Return the Agent Card for discovery."""
    if AGENT_CARD_PATH.exists():
        with open(AGENT_CARD_PATH) as f:
            return json.load(f)

    return HTTPException(status_code=404, detail="Agent card not found")


@app.post("/rpc")
async def handle_rpc(
    request: JsonRpcRequest,
    authorization: str | None = Header(None),
    x_api_key: str | None = Header(None)
):
    """Handle JSON-RPC requests."""
    if not verify_auth(authorization, x_api_key):
        return JSONResponse(
            status_code=401,
            content={
                "jsonrpc": "2.0",
                "error": {"code": -32000, "message": "Unauthorized"},
                "id": request.id
            }
        )

    if context_manager is None:
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "error": {"code": -32000, "message": "Context manager not initialized"},
                "id": request.id
            }
        )

    try:
        result = dispatch_method(request.method, request.params)
        return {"jsonrpc": "2.0", "result": result, "id": request.id}
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={
                "jsonrpc": "2.0",
                "error": {"code": -32602, "message": str(e)},
                "id": request.id
            }
        )


def dispatch_method(method: str, params: dict) -> Any:
    """Dispatch to appropriate skill handler."""
    handlers = {
        "get_context": lambda p: context_manager.get_context(
            level=p.get("level", "company"),
            division=p.get("division"),
            team=p.get("team"),
            sections=p.get("sections")
        ),
        "check_constraints": lambda p: context_manager.check_constraints(
            action=p.get("action", ""),
            team=p.get("team"),
            action_type=p.get("action_type"),
            estimated_cost=p.get("estimated_cost"),
            target_date=p.get("target_date")
        ),
        "get_stakeholders": lambda p: context_manager.get_stakeholders(
            initiative_type=p.get("initiative_type", "product"),
            estimated_cost=p.get("estimated_cost"),
            team=p.get("team"),
            division=p.get("division")
        ),
        "get_ubiquitous_language": lambda p: context_manager.get_ubiquitous_language(
            terms=p.get("terms"),
            division=p.get("division")
        ),
        "check_team_capacity": lambda p: context_manager.check_team_capacity(
            team=p.get("team", ""),
            work_type=p.get("work_type"),
            estimated_effort=p.get("estimated_effort")
        )
    }

    if method not in handlers:
        raise ValueError(f"Unknown method: {method}")

    return handlers[method](params)


# ============================================================================
# Startup
# ============================================================================

def create_app(context_dir: str | Path) -> FastAPI:
    """Create app with context manager initialized."""
    global context_manager
    context_manager = ContextManager(Path(context_dir))
    return app


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enterprise Context A2A Server"
    )
    parser.add_argument(
        "--context-dir",
        default=os.environ.get("CONTEXT_DIR", "."),
        help="Directory containing context files"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "8080")),
        help="Server port"
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),
        help="Server host"
    )

    args = parser.parse_args()

    # Initialize context manager
    global context_manager
    context_manager = ContextManager(Path(args.context_dir))

    print(f"Loaded contexts from: {args.context_dir}")
    print(f"  Company: {'Yes' if context_manager.contexts['company'] else 'No'}")
    print(f"  Divisions: {list(context_manager.contexts['divisions'].keys())}")
    print(f"  Teams: {list(context_manager.contexts['teams'].keys())}")
    print(f"\nStarting A2A server on {args.host}:{args.port}")
    print(f"Agent card available at: http://{args.host}:{args.port}/.well-known/agent.json")

    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
