# AI Civic MVP — AI Company Demo

AI agents that form a company and run tasks autonomously.

## Architecture

```
LLM (GPT API)
    ↓
Agent (role, goal, tools, memory)
    ↓
Role (CEO, Engineer, Marketing, Sales)
    ↓
Company (Organization)
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env: add your OPENAI_API_KEY
```

## Run

```bash
python main.py
```

## Output

```
=== Creating company: AI SaaS Builder ===

[CEO] defining strategy...
[CEO] Our strategy is to build...

=== Executing tasks ===

[Engineer] working on: Build FastAPI backend...
[Engineer] Here is a FastAPI backend...

[Marketing] working on: Create landing page...
[Marketing] Landing page copy...

[Sales] working on: Write outreach emails...
[Sales] Outreach email template...

=== AI Company workflow complete ===
```

## Structure

```
company/     → Company, Organization, roles, planner
agents/      → Agent (think, memory, shared_memory)
tasks/       → TaskManager (add_task, run)
environment/ → Memory (task history)
policy.py    → Policy (heuristic / OpenClaw-RL API when configured)
console.py   → Formatted output
llm.py       → GPT API integration
```

## Versions

| Tag        | Description                    |
|------------|--------------------------------|
| `v0.1-mvp` | Initial MVP — agents, roles, task manager, organization |
| `v0.2`     | CEO plan → auto task breakdown, Memory, Policy, console formatting |
| `v0.2.1`   | Policy integrated into workflow (default tasks + CEO role reassign) |
| `v0.3`     | OpenClaw-RL compatible Policy (OPENCLAW_API_BASE for role selection) |
| `v0.3.1`   | Smoke test script (`scripts/check.py`) |
| `v0.4`     | Agent.think() uses OpenClaw when OPENCLAW_API_BASE set; fallback to OpenAI |

Checkout a previous version:
```bash
git checkout v0.1-mvp   # v0.1
git checkout v0.2      # v0.2
git checkout v0.2.1    # v0.2.1
git checkout v0.3      # v0.3
git checkout v0.3.1    # v0.3.1
git checkout v0.4      # v0.4
```

### Smoke tests (no API)

```bash
python scripts/check.py
# or
python -m scripts.check
```

### OpenClaw-RL integration

When running [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) (serves OpenAI-compatible API on port 30000):

```bash
OPENCLAW_API_BASE=http://localhost:30000/v1 python main.py
```

- **Agent.think()** (CEO, Engineer, Marketing, Sales) → OpenClaw; falls back to OpenAI on failure
- **Policy** (task→role) → OpenClaw; falls back to heuristic if API unavailable

## Extensions

- **Memory**: `environment/memory.py` — task history
- **Policy**: `policy.py` — heuristic by default; uses OpenClaw-RL API when `OPENCLAW_API_BASE` is set
- **Multiple companies** → markets → economy → AI civilization
