"""Configuration - load from env."""
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# OpenClaw-RL serves OpenAI-compatible API. When set, Policy uses it for role selection.
OPENCLAW_API_BASE = os.getenv("OPENCLAW_API_BASE", "")  # e.g. http://localhost:30000/v1
