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
policy.py    → Policy (choose_role_for_task, → OpenClaw RL)
console.py   → Formatted output
llm.py       → GPT API integration
```

## Versions

| Tag        | Description                    |
|------------|--------------------------------|
| `v0.1-mvp` | Initial MVP — agents, roles, task manager, organization |
| `v0.2`     | CEO plan → auto task breakdown, Memory, Policy, console formatting |

이전 버전으로 되돌리기:
```bash
git checkout v0.1-mvp   # v0.1
git checkout v0.2      # v0.2
```

## Extensions

- **Memory**: `environment/memory.py` — task history
- **Policy**: `policy.py` — replace with OpenClaw RL for action selection
- **Multiple companies** → markets → economy → AI civilization
