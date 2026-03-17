"""Market - multiple companies running in a shared context."""
from .company import Company
from console import section


class Market:
    """Holds multiple companies. Run all sequentially."""

    def __init__(self):
        self.companies = []

    def add_company(self, name: str) -> Company:
        """Create and register a company. Returns it for optional config."""
        company = Company()
        self.companies.append((name, company))
        return company

    def run_all(self):
        """Run all registered companies."""
        section(f"Market: {len(self.companies)} companies")
        for name, company in self.companies:
            company.run(name)
        section("Market complete")
