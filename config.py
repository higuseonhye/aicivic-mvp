"""Configuration - load from env."""
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# AI workspace only. When human company is added, use AI_* vs HUMAN_* for separation.
AI_NOTION_API_KEY = os.getenv("AI_NOTION_API_KEY", "")
AI_NOTION_DATABASE_ID = os.getenv("AI_NOTION_DATABASE_ID", "")
AI_SLACK_BOT_TOKEN = os.getenv("AI_SLACK_BOT_TOKEN", "")
AI_SLACK_CHANNEL = os.getenv("AI_SLACK_CHANNEL", "")  # default channel, e.g. #ai-agents
AI_SLACK_USE_COMPANY_CHANNELS = os.getenv("AI_SLACK_USE_COMPANY_CHANNELS", "false").lower() == "true"
