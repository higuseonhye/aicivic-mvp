"""LLM integration - GPT API with cost tracking."""
from openai import OpenAI
from config import OPENAI_API_KEY

_cost_tracker = None


def set_cost_tracker(tracker):
    global _cost_tracker
    _cost_tracker = tracker


def llm(prompt: str, model: str = "gpt-4o-mini", role: str = "", task: str = "") -> str:
    """Call GPT API. Tracks tokens/cost when CostTracker is set."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.choices[0].message.content or ""

    if _cost_tracker and response.usage:
        _cost_tracker.add(
            role=role,
            task=task,
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
        )

    return text
