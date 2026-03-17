"""LLM integration - OpenAI or OpenClaw (OpenAI-compatible API)."""
from openai import OpenAI
from config import OPENAI_API_KEY, OPENCLAW_API_BASE


def llm(prompt: str, model: str = None) -> str:
    """Call LLM. Uses OpenClaw when OPENCLAW_API_BASE is set, else OpenAI."""
    if OPENCLAW_API_BASE:
        result = _call_openclaw(prompt, model or "openclaw")
        if result is not None:
            return result
        # Fallback to OpenAI if OpenClaw fails
    return _call_openai(prompt, model or "gpt-4o-mini")


def _call_openai(prompt: str, model: str) -> str:
    """OpenAI API."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""


def _call_openclaw(prompt: str, model: str):
    """OpenClaw-RL API (OpenAI-compatible). Returns None on failure."""
    try:
        client = OpenAI(base_url=OPENCLAW_API_BASE, api_key="openclaw", timeout=5)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content or ""
    except Exception:
        return None
