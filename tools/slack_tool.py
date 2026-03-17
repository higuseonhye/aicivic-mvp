"""Slack tool - post agent output to channel."""
from .base import Tool


class SlackTool(Tool):
    """Post agent output to Slack. Requires SLACK_BOT_TOKEN and SLACK_CHANNEL in .env."""

    def __init__(self, token: str = "", channel: str = ""):
        self.token = token
        self.channel = channel
        self._enabled = bool(token and channel)

    def execute(self, company: str, role: str, task: str, result: str) -> bool:
        if not self._enabled:
            return False
        try:
            from slack_sdk import WebClient
        except ImportError:
            return False
        try:
            client = WebClient(token=self.token)
            text = f"*[{company}] {role}*\nTask: {task[:100]}\n\n{result[:1500]}"
            client.chat_postMessage(channel=self.channel, text=text)
            return True
        except Exception:
            return False
