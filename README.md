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
# Single company
python main.py

# Multiple companies (market)
python main.py --market
python main.py --market "Company A" "Company B"
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
company/     → Company, Organization, Market, roles, planner
agents/      → Agent (think, memory, shared_memory)
tasks/       → TaskManager (add_task, run)
environment/ → Memory (task history)
policy.py    → Policy (heuristic task→role)
console.py   → Formatted output
llm.py       → GPT API integration
```

## Versions

| Tag        | Description                    |
|------------|--------------------------------|
| `v0.1-mvp` | Initial MVP — agents, roles, task manager, organization |
| `v0.2`     | CEO plan → auto task breakdown, Memory, Policy, console formatting |
| `v0.5`     | OpenAI + heuristic only |
| `v0.6`     | Market — multiple companies |

Checkout a previous version:
```bash
git checkout v0.1-mvp
git checkout v0.2
git checkout v0.5
git checkout v0.6
```

### Smoke tests (no API)

```bash
python scripts/check.py
# or
python -m scripts.check
```

## Future vision

- **Economy** — companies trading, value exchange
