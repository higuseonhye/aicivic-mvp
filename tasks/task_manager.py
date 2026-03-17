"""Task Manager - assign and run tasks across agents."""
from agents import Agent


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent: Agent, task: str):
        self.tasks.append((agent, task))

    def run(self):
        for agent, task in self.tasks:
            print(f"[{agent.role}] working on: {task[:50]}...")
            result = agent.think(task)
            print(f"[{agent.role}] {result[:200]}{'...' if len(result) > 200 else ''}\n")
