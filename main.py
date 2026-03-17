"""Run AI company demo. Single company or market (multiple companies)."""
import logging
import sys
from company import Company, Market

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Default companies for market mode
DEFAULT_COMPANIES = ["AI SaaS Builder", "AI Analytics Co", "AI Security Inc"]


def run_single(name=None):
    """Run single company."""
    company = Company()
    company.run(name or "AI SaaS Builder")


def run_market(names=None):
    """Run multiple companies."""
    market = Market()
    for name in names or DEFAULT_COMPANIES:
        market.add_company(name)
    market.run_all()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--market":
        run_market(sys.argv[2:] if len(sys.argv) > 2 else None)
    else:
        name = sys.argv[1] if len(sys.argv) > 1 else None
        run_single(name)
