"""Agent - role, goal, tools, memory."""
from llm import llm


class Agent:
    def __init__(self, role: str, goal: str, tools: list = None):
        self.role = role
        self.goal = goal
        self.tools = tools or []
        self.memory = []

    def think(self, task: str) -> str:
        prompt = f"""
You are a {self.role}.
Your goal: {self.goal}

Task: {task}

Respond with your output directly. Be concise.
"""
        result = llm(prompt)
        self.memory.append({"task": task, "result": result})
        return result
