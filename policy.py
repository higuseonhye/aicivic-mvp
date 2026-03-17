"""Policy - task assignment. Heuristic by keyword matching."""
from typing import List, Any


class Policy:
    """Task-to-role assignment via keyword heuristic."""

    ROLE_KEYWORDS = {
        "Engineer": ["build", "api", "code", "backend", "frontend", "documentation", "implement"],
        "Marketing": ["landing", "page", "copy", "promote", "content", "brand", "value prop"],
        "Sales": ["outreach", "email", "sell", "pitch", "lead", "cold", "template"],
    }

    def choose_action(self, options: List[Any]) -> Any:
        """Fallback: first option."""
        return options[0] if options else None

    def choose_role_for_task(self, task: str) -> str:
        """Pick best role for task based on keywords."""
        task_lower = task.lower()
        best_role, best_score = "Engineer", 0
        for role, keywords in self.ROLE_KEYWORDS.items():
            score = sum(1 for k in keywords if k in task_lower)
            if score > best_score:
                best_score, best_role = score, role
        return best_role
