"""Organization - company structure with agents."""
from agents import Agent
from .roles import create_agent


class Organization:
    """Company with CEO, Engineers, Marketing, Sales."""

    def __init__(self):
        self.ceo = create_agent("CEO")
        self.engineers = [create_agent("Engineer"), create_agent("Engineer")]
        self.marketing = create_agent("Marketing")
        self.sales = create_agent("Sales")
