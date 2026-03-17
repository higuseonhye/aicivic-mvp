"""Organization - company structure with agents."""
from agents import Agent
from .roles import create_agent


class Organization:
    """Company with CEO, Engineers, Marketing, Sales."""

    def __init__(self, shared_memory=None):
        self.shared_memory = shared_memory
        self._engineer_idx = 0
        self.ceo = create_agent("CEO", shared_memory)
        self.engineers = [create_agent("Engineer", shared_memory), create_agent("Engineer", shared_memory)]
        self.marketing = create_agent("Marketing", shared_memory)
        self.sales = create_agent("Sales", shared_memory)

    def get_agent_by_role(self, role: str) -> Agent:
        if role == "Engineer":
            agent = self.engineers[self._engineer_idx % len(self.engineers)]
            self._engineer_idx += 1
            return agent
        return {"Marketing": self.marketing, "Sales": self.sales}.get(role, self.engineers[0])
