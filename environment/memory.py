"""Memory - agent memory and task history (Day 3)."""
from typing import List, Dict, Any


class Memory:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def add(self, agent_role: str, task: str, result: str):
        self.history.append({
            "agent": agent_role,
            "task": task,
            "result": result,
        })

    def get_recent(self, n: int = 5) -> List[Dict[str, Any]]:
        return self.history[-n:]
