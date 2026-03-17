"""Policy - task assignment. Heuristic by default, OpenClaw-RL when API available."""
from typing import List, Any


class Policy:
    """Task-to-role assignment. Uses OpenClaw API if configured, else heuristic."""

    ROLE_KEYWORDS = {
        "Engineer": ["build", "api", "code", "backend", "frontend", "documentation", "implement"],
        "Marketing": ["landing", "page", "copy", "promote", "content", "brand", "value prop"],
        "Sales": ["outreach", "email", "sell", "pitch", "lead", "cold", "template"],
    }

    VALID_ROLES = ["Engineer", "Marketing", "Sales"]

    def __init__(self):
        from config import OPENCLAW_API_BASE
        self._openclaw_base = OPENCLAW_API_BASE

    def choose_action(self, options: List[Any]) -> Any:
        """Fallback: first option."""
        return options[0] if options else None

    def choose_role_for_task(self, task: str) -> str:
        """Pick role: OpenClaw API if available, else heuristic."""
        if self._openclaw_base:
            return self._choose_via_openclaw(task)
        return self._choose_heuristic(task)

    def _choose_heuristic(self, task: str) -> str:
        """Keyword-based role selection."""
        task_lower = task.lower()
        best_role, best_score = "Engineer", 0
        for role, keywords in self.ROLE_KEYWORDS.items():
            score = sum(1 for k in keywords if k in task_lower)
            if score > best_score:
                best_score, best_role = score, role
        return best_role

    def _choose_via_openclaw(self, task: str) -> str:
        """Call OpenClaw-RL OpenAI-compatible API for role selection."""
        try:
            from openai import OpenAI
            client = OpenAI(base_url=self._openclaw_base, api_key="openclaw", timeout=5)
            resp = client.chat.completions.create(
                model="openclaw",
                messages=[{
                    "role": "user",
                    "content": f"Task: {task}\n\nWhich role should do this? Reply with exactly one word: Engineer, Marketing, or Sales."
                }],
            )
            text = (resp.choices[0].message.content or "").strip()
            for role in self.VALID_ROLES:
                if role.lower() in text.lower():
                    return role
        except Exception:
            pass
        return self._choose_heuristic(task)
