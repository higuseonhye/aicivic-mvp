"""Task Manager - assign and run tasks across agents."""
from agents import Agent
from console import agent_action, agent_result


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent: Agent, task: str):
        self.tasks.append((agent, task))

    def run(self, console_format: bool = True):
        for agent, task in self.tasks:
            if console_format:
                agent_action(agent.role, f"working on: {task[:60]}{'...' if len(task) > 60 else ''}")
            else:
                print(f"[{agent.role}] working on: {task[:50]}...")
            result = agent.think(task)
            if console_format:
                agent_result(agent.role, result, max_len=300)
            else:
                print(f"[{agent.role}] {result[:200]}{'...' if len(result) > 200 else ''}\n")
