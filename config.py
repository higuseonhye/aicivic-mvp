"""Configuration - load from env."""
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# OpenClaw-RL (OpenAI-compatible API). When set: Agent.think() and Policy use it; fallback to OpenAI on failure.
OPENCLAW_API_BASE = os.getenv("OPENCLAW_API_BASE", "")  # e.g. http://localhost:30000/v1
