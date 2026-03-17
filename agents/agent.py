"""Agent - role, goal, tools, memory."""
from llm import llm


class Agent:
    def __init__(self, role: str, goal: str, tools: list = None, shared_memory=None):
        self.role = role
        self.goal = goal
        self.tools = tools or []
        self.memory = []
        self.shared_memory = shared_memory

    def think(self, task: str) -> str:
        context = ""
        if self.shared_memory:
            recent = self.shared_memory.get_recent(3)
            if recent:
                context = "\nRecent company context:\n"
                for h in recent:
                    context += f"- [{h['agent']}] {h['task'][:50]}... -> done\n"
                context += "\n"

        prompt = f"""
You are a {self.role}.
Your goal: {self.goal}
{context}
Task: {task}

Respond with your output directly. Be concise.
"""
        result = llm(prompt)
        self.memory.append({"task": task, "result": result})
        if self.shared_memory:
            self.shared_memory.add(self.role, task, result)
        return result
