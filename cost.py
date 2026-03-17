"""Cost tracking - tokens and spend per LLM call."""
from dataclasses import dataclass, field
from typing import Dict, List

# gpt-4o-mini pricing (per 1M tokens)
INPUT_PRICE = 0.15
OUTPUT_PRICE = 0.60


@dataclass
class CallRecord:
    company: str
    role: str
    task: str
    input_tokens: int
    output_tokens: int
    cost_usd: float


class CostTracker:
    def __init__(self):
        self.records: List[CallRecord] = []
        self._company = ""

    def set_company(self, name: str):
        self._company = name

    def add(self, role: str, task: str, input_tokens: int, output_tokens: int):
        cost = (input_tokens * INPUT_PRICE + output_tokens * OUTPUT_PRICE) / 1_000_000
        self.records.append(CallRecord(
            company=self._company,
            role=role,
            task=task[:50],
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost,
        ))

    @property
    def total_tokens(self) -> int:
        return sum(r.input_tokens + r.output_tokens for r in self.records)

    @property
    def total_cost_usd(self) -> float:
        return sum(r.cost_usd for r in self.records)

    def by_company(self) -> Dict[str, float]:
        d = {}
        for r in self.records:
            d[r.company] = d.get(r.company, 0) + r.cost_usd
        return d
