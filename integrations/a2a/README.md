# A2A (Agent-to-Agent) Integration

This integration enables AI agents to discover and query enterprise context using Google's [Agent2Agent (A2A) Protocol](https://a2a-protocol.org).

## Overview

The A2A protocol enables agents to communicate with each other, exchange information, and coordinate actions. This integration exposes Enterprise Context Spec as an A2A-compliant service, allowing any A2A-enabled agent to:

- **Discover** enterprise context capabilities via Agent Cards
- **Query** company, division, and team context
- **Receive** merged context with proper inheritance
- **Understand** organizational constraints before taking actions

## How A2A Complements MCP and ECS

| Protocol | Purpose | Focus |
|----------|---------|-------|
| **MCP** (Anthropic) | Connect AI to tools and data sources | Technical connectivity |
| **A2A** (Google) | Enable agent-to-agent communication | Agent collaboration |
| **ECS** (This spec) | Define organizational knowledge | Human/business context |

Together: An agent uses **MCP** to access tools, **A2A** to collaborate with other agents, and **ECS** to understand organizational context.

## Installation

```bash
pip install a2a-sdk enterprise-context
```

## Quick Start

### 1. Start the Enterprise Context A2A Server

```bash
python server.py --context-dir /path/to/context/files --port 8080
```

### 2. Discover the Agent

Other A2A agents can discover this service via the Agent Card:

```bash
curl http://localhost:8080/.well-known/agent.json
```

### 3. Query Context

```python
from a2a_sdk import A2AClient

client = A2AClient("http://localhost:8080")

# Get merged context
response = await client.send_task({
    "skill": "get_context",
    "input": {
        "level": "team",
        "team": "Customer Portal"
    }
})

context = response.result
print(context["constraints"])  # Team constraints
print(context["risk_appetite"])  # Inherited from company
```

## Agent Card

The server exposes an Agent Card at `/.well-known/agent.json`:

```json
{
  "name": "Enterprise Context Agent",
  "description": "Provides organizational context (strategy, constraints, team structures) for AI agents operating in enterprise environments",
  "version": "1.0.0",
  "protocol": "a2a/1.0",
  "capabilities": {
    "streaming": false,
    "pushNotifications": false
  },
  "skills": [
    {
      "id": "get_context",
      "name": "Get Enterprise Context",
      "description": "Retrieve merged enterprise context with inheritance (company → division → team)",
      "input": {
        "type": "object",
        "properties": {
          "level": {
            "type": "string",
            "enum": ["company", "division", "team"],
            "description": "Context level to retrieve"
          },
          "division": {
            "type": "string",
            "description": "Division name (required if level is division or team)"
          },
          "team": {
            "type": "string",
            "description": "Team name (required if level is team)"
          }
        }
      },
      "output": {
        "type": "object",
        "description": "Merged enterprise context following ECS schema"
      }
    },
    {
      "id": "check_constraints",
      "name": "Check Constraints",
      "description": "Validate a proposed action against enterprise constraints",
      "input": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "description": "Description of proposed action"
          },
          "team": {
            "type": "string",
            "description": "Team context to check against"
          }
        }
      },
      "output": {
        "type": "object",
        "properties": {
          "allowed": { "type": "boolean" },
          "concerns": { "type": "array", "items": { "type": "string" } },
          "relevant_constraints": { "type": "array" }
        }
      }
    },
    {
      "id": "get_stakeholders",
      "name": "Get Stakeholders",
      "description": "Identify relevant stakeholders for a given initiative",
      "input": {
        "type": "object",
        "properties": {
          "initiative_type": {
            "type": "string",
            "enum": ["technical", "product", "regulatory", "budget"],
            "description": "Type of initiative"
          },
          "estimated_cost": {
            "type": "number",
            "description": "Estimated cost in dollars"
          }
        }
      },
      "output": {
        "type": "object",
        "properties": {
          "approvers": { "type": "array" },
          "stakeholders": { "type": "array" },
          "decision_forum": { "type": "string" }
        }
      }
    }
  ],
  "security": {
    "schemes": ["bearer", "apiKey"]
  }
}
```

## Skills Reference

### `get_context`

Retrieves merged enterprise context with proper inheritance.

**Input:**
- `level` (required): `"company"`, `"division"`, or `"team"`
- `division` (optional): Division name for division/team level
- `team` (optional): Team name for team level

**Output:** Merged ECS context object

**Example:**
```python
# Get company-level context only
response = await client.send_task({
    "skill": "get_context",
    "input": {"level": "company"}
})

# Get team context with full inheritance
response = await client.send_task({
    "skill": "get_context",
    "input": {
        "level": "team",
        "division": "Operations",
        "team": "Customer Portal"
    }
})
```

### `check_constraints`

Validates a proposed action against enterprise constraints (budget, regulatory, technical, timeline).

**Input:**
- `action` (required): Description of proposed action
- `team` (optional): Team context to check against

**Output:**
- `allowed`: Boolean indicating if action is permissible
- `concerns`: List of potential issues
- `relevant_constraints`: Applicable constraints from context

**Example:**
```python
response = await client.send_task({
    "skill": "check_constraints",
    "input": {
        "action": "Deploy new ML model to production",
        "team": "Customer Portal"
    }
})

if not response.result["allowed"]:
    print("Concerns:", response.result["concerns"])
    # ["Code freeze in effect (December)", "Security review required for ML models"]
```

### `get_stakeholders`

Identifies relevant stakeholders and approvers based on initiative type and cost.

**Input:**
- `initiative_type`: `"technical"`, `"product"`, `"regulatory"`, or `"budget"`
- `estimated_cost` (optional): Cost estimate for budget-based routing

**Output:**
- `approvers`: List of required approvers
- `stakeholders`: List of stakeholders to inform
- `decision_forum`: Relevant decision forum

**Example:**
```python
response = await client.send_task({
    "skill": "get_stakeholders",
    "input": {
        "initiative_type": "budget",
        "estimated_cost": 750000
    }
})

# Returns: {"approvers": ["Investment Committee"], "decision_forum": "Monthly IC Meeting"}
```

## Architecture

```
┌─────────────────────┐     A2A Protocol      ┌──────────────────────┐
│                     │  ─────────────────►   │                      │
│   Client Agent      │                       │  Enterprise Context  │
│   (LangGraph,       │  ◄─────────────────   │  A2A Server          │
│    ADK, etc.)       │     JSON-RPC/SSE      │                      │
└─────────────────────┘                       └──────────┬───────────┘
                                                         │
                                                         ▼
                                              ┌──────────────────────┐
                                              │  Context Files       │
                                              │  ├── company.md      │
                                              │  ├── division.md     │
                                              │  └── team.md         │
                                              └──────────────────────┘
```

## Use Cases

### 1. Pre-Action Constraint Checking

Before an agent takes action, it queries enterprise context to ensure compliance:

```python
# Agent about to recommend a technology
context = await context_agent.get_context(team="Customer Portal")

if "Azure" in context["technology"]["cloud"]:
    recommend_azure_solution()
else:
    recommend_cloud_agnostic_solution()
```

### 2. Multi-Agent Collaboration

Multiple agents share organizational understanding:

```python
# Research agent gets company strategy
strategy = await context_agent.get_context(level="company")

# Passes to architecture agent
architecture_agent.set_context(
    investment_themes=strategy["strategic_priorities"]["investment_themes"],
    tech_stack=strategy["technology_landscape"]["core_systems"]
)
```

### 3. Stakeholder Routing

Agent determines who to notify about findings:

```python
stakeholders = await context_agent.get_stakeholders(
    initiative_type="regulatory",
    estimated_cost=50000
)

for approver in stakeholders["approvers"]:
    notify(approver, findings)
```

## Configuration

### Environment Variables

```bash
# Required
CONTEXT_DIR=/path/to/context/files

# Optional
PORT=8080
HOST=0.0.0.0
AUTH_TYPE=bearer  # or apiKey, none
AUTH_SECRET=your-secret-key
LOG_LEVEL=INFO
```

### Docker

```bash
docker run -d \
  -p 8080:8080 \
  -v /path/to/context:/context \
  -e CONTEXT_DIR=/context \
  enterprise-context-a2a:latest
```

## Security

The A2A server supports multiple authentication schemes:

| Scheme | Use Case |
|--------|----------|
| `bearer` | JWT tokens for service-to-service auth |
| `apiKey` | Simple API key authentication |
| `none` | Development/testing only |

For production, always use authentication and HTTPS.

## Comparison: A2A vs Direct File Loading

| Approach | Pros | Cons |
|----------|------|------|
| **A2A Server** | Centralized, real-time, multi-agent | Requires server, network dependency |
| **Direct Loading** | Simple, no server | Each agent loads separately, no caching |

Use A2A when:
- Multiple agents need the same context
- Context is updated frequently
- You want constraint checking as a service
- Enterprise security requirements apply

## Resources

- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [A2A Python SDK](https://pypi.org/project/a2a-sdk/)
- [A2A GitHub Repository](https://github.com/a2aproject/A2A)
- [Enterprise Context Spec](../../README.md)

## License

MIT License
