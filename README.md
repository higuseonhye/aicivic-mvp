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
company/     → Company, Organization, roles
agents/      → Agent (think, memory)
tasks/       → TaskManager (add_task, run)
environment/ → Memory (task history)
policy.py    → Policy stub (→ OpenClaw RL later)
llm.py       → GPT API integration
```

## Extensions

- **Memory**: `environment/memory.py` — task history
- **Policy**: `policy.py` — replace with OpenClaw RL for action selection
- **Multiple companies** → markets → economy → AI civilization
