"""LLM integration - GPT API."""
from openai import OpenAI
from config import OPENAI_API_KEY


def llm(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Call GPT API with prompt. Returns response text."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""
