"""CEO plan parsing - extract tasks from plan output."""
import re
from typing import List, Tuple
from agents import Agent


def parse_plan_tasks(plan_text: str) -> List[Tuple[str, str]]:
    """
    Parse CEO plan output for task assignments.
    Expected format: "Role: task description" per line.
    Returns list of (role, task).
    """
    tasks = []
    # Match "Engineer: ..." or "Marketing: ..." etc.
    pattern = r"^(Engineer|Marketing|Sales|CEO)\s*:\s*(.+)$"
    for line in plan_text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            role, task = match.groups()
            task = task.strip()
            if task:
                tasks.append((role.capitalize(), task))
    return tasks


def get_default_tasks(company_name: str) -> List[Tuple[str, str]]:
    """Fallback tasks when parsing fails."""
    return [
        ("Engineer", f"Build FastAPI backend for {company_name}"),
        ("Engineer", "Write API documentation"),
        ("Marketing", "Create landing page copy and value proposition"),
        ("Sales", "Write 3 outreach email templates for cold outreach"),
    ]
