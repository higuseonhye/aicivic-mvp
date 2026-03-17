"""Company - runs AI company workflow."""
from tasks import TaskManager
from .organization import Organization


class Company:
    def __init__(self):
        self.org = Organization()

    def run(self, company_name: str = "AI SaaS Builder"):
        print(f"=== Creating company: {company_name} ===\n")

        # 1. CEO creates plan
        print("[CEO] defining strategy...")
        plan = self.org.ceo.think(
            f"We need to build an AI SaaS product called '{company_name}'. "
            "Create a concise execution plan with tasks for engineers, marketing, and sales."
        )
        print(f"[CEO] {plan[:300]}...\n")

        # 2. Task breakdown & assignment
        tm = TaskManager()
        tm.add_task(self.org.engineers[0], "Build FastAPI backend with core API endpoints")
        tm.add_task(self.org.engineers[1], "Write API documentation and code structure")
        tm.add_task(self.org.marketing, "Create landing page copy and value proposition")
        tm.add_task(self.org.sales, "Write 3 outreach email templates for cold outreach")

        print("=== Executing tasks ===\n")
        tm.run()

        print("=== AI Company workflow complete ===")
