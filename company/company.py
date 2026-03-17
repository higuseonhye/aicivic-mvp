"""Company - runs AI company workflow."""
from tasks import TaskManager
from environment import Memory
from policy import Policy
from console import section, agent_action, agent_result
from .organization import Organization
from .planner import parse_plan_tasks, get_default_tasks


class Company:
    def __init__(self):
        self.memory = Memory()
        self.policy = Policy()
        self.org = Organization(shared_memory=self.memory)

    def run(self, company_name: str = "AI SaaS Builder"):
        section(f"Creating company: {company_name}")

        # 1. CEO creates plan
        agent_action("CEO", "defining strategy...")
        plan_prompt = (
            f"We need to build an AI SaaS product called '{company_name}'. "
            "Create a concise execution plan. "
            "Then list tasks in this format (one per line):\n"
            "Engineer: <task>\n"
            "Marketing: <task>\n"
            "Sales: <task>\n"
            "Example:\n"
            "Engineer: Build FastAPI backend\n"
            "Marketing: Create landing page copy"
        )
        plan = self.org.ceo.think(plan_prompt)
        agent_result("CEO", plan, max_len=400)

        # 2. Parse plan → tasks (fallback: Policy assigns roles)
        tasks = parse_plan_tasks(plan)
        if not tasks:
            tasks = get_default_tasks(company_name)
        else:
            # Use Policy for tasks with unclear role (e.g. "CEO" parsed → reassign)
            tasks = [
                (role if role != "CEO" else self.policy.choose_role_for_task(task), task)
                for role, task in tasks
            ]

        # 3. Assign tasks to agents
        tm = TaskManager()
        for role, task in tasks:
            agent = self.org.get_agent_by_role(role)
            tm.add_task(agent, task)

        # 4. Execute
        section("Executing tasks")
        tm.run(console_format=True)

        section("AI Company workflow complete")
