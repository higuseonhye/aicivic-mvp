"""Role definitions for AI company."""
from agents import Agent

# Role configs: (role_name, goal)
ROLES = {
    "CEO": ("CEO", "build successful AI startup"),
    "Engineer": ("Engineer", "build software"),
    "Marketing": ("Marketing", "promote product"),
    "Sales": ("Sales", "sell product"),
}


def create_agent(role_key: str, shared_memory=None) -> Agent:
    role, goal = ROLES[role_key]
    return Agent(role, goal, [], shared_memory)
