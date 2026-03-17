"""Tool base - execute external actions."""
from abc import ABC, abstractmethod
from typing import Optional


class Tool(ABC):
    """Base class for tools that perform real-world actions."""

    @abstractmethod
    def execute(self, company: str, role: str, task: str, result: str) -> bool:
        """Run the tool. Returns True if successful."""
        pass
