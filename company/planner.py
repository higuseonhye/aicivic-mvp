"""CEO plan parsing - extract tasks from plan output."""
import re
from typing import List, Tuple


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
    """Fallback tasks when parsing fails. Returns (role, task) - role from Policy."""
    from policy import Policy
    policy = Policy()
    tasks_raw = [
        f"Build FastAPI backend for {company_name}",
        "Write API documentation",
        "Create landing page copy and value proposition",
        "Write 3 outreach email templates for cold outreach",
    ]
    return [(policy.choose_role_for_task(t), t) for t in tasks_raw]
