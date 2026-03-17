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
python main.py "My Company"

# Multiple companies (market)
python main.py --market
python main.py --market "Company A" "Company B"

# Web UI
streamlit run app.py
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
tools/       → NotionTool, SlackTool (real actions)
environment/ → Memory (task history)
cost.py      → CostTracker (tokens, spend)
policy.py    → Policy (heuristic task→role)
console.py   → Formatted output
llm.py       → GPT API integration
app.py       → Streamlit frontend
```

### Cost tracking

Each run shows total cost and tokens at the end.

### Tools (optional)

- **Notion**: Create pages per company/role/task. Set `NOTION_API_KEY`, `NOTION_DATABASE_ID`.
- **Slack**: Post agent output to channel. Set `SLACK_BOT_TOKEN`, `SLACK_CHANNEL`.

## Versions

| Tag        | Description                    |
|------------|--------------------------------|
| `v0.1-mvp` | Initial MVP — agents, roles, task manager, organization |
| `v0.2`     | CEO plan → auto task breakdown, Memory, Policy, console formatting |
| `v0.5`     | OpenAI + heuristic only |
| `v0.6`     | Market — multiple companies |
| `v0.7`     | Cost tracking, Tools (Notion/Slack), Streamlit frontend |

Checkout a previous version:
```bash
git checkout v0.1-mvp
git checkout v0.2
git checkout v0.5
git checkout v0.6
git checkout v0.7
```

### Smoke tests (no API)

```bash
python scripts/check.py
# or
python -m scripts.check
```

## Future vision

- **Economy** — companies trading, value exchange
