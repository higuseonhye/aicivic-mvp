"""Slack tool - post agent output. Auto-create channels, invite bot."""
import logging
import re
from .base import Tool

log = logging.getLogger(__name__)


def _company_to_channel(company: str) -> str:
    """AI SaaS Builder -> #ai-saas-builder"""
    slug = re.sub(r"[^a-z0-9]+", "-", company.lower()).strip("-")
    return f"#ai-{slug}" if slug else "#ai-agents"


def _channel_name_from_display(display: str) -> str:
    """#ai-saas-builder -> ai-saas-builder (no #)"""
    return display.lstrip("#")


class SlackTool(Tool):
    """Post agent output to Slack. Auto-creates company channels and joins."""

    def __init__(self, token: str = "", channel: str = "", use_company_channels: bool = False):
        self.token = token
        self.channel = channel
        self.use_company_channels = use_company_channels
        self._enabled = bool(token and channel)
        self._ensured_channels = set()

    def _ensure_channel(self, client, channel_display: str) -> bool:
        """Create channel if not exists, join if exists. Requires channels:manage, channels:read, channels:join."""
        from slack_sdk.errors import SlackApiError

        name = _channel_name_from_display(channel_display)
        if len(name) > 80:
            name = name[:80]
        if name in self._ensured_channels:
            return True
        try:
            client.conversations_create(name=name, is_private=False)
            self._ensured_channels.add(name)
            log.info("Created channel #%s", name)
            return True
        except SlackApiError as e:
            err = e.response.get("error", str(e)).lower()
            if "name_taken" in err or "already_exists" in err:
                try:
                    resp = client.conversations_list(types="public_channel", limit=500, exclude_archived=True)
                    for c in resp.get("channels", []):
                        if c.get("name") == name:
                            client.conversations_join(channel=c["id"])
                            self._ensured_channels.add(name)
                            log.info("Joined channel #%s", name)
                            return True
                    log.warning("Channel #%s exists but not found in list (archived?)", name)
                except SlackApiError as e2:
                    log.warning("Could not join #%s: %s", name, e2.response.get("error", e2))
            else:
                log.warning("Could not create #%s: %s", name, err)
            return False
        except Exception as e:
            log.warning("Could not create #%s: %s", name, e)
            return False

    def execute(self, company: str, role: str, task: str, result: str) -> bool:
        if not self._enabled:
            return False
        try:
            from slack_sdk import WebClient
        except ImportError:
            return False

        channel = _company_to_channel(company) if self.use_company_channels else self.channel
        # Format: company + role (bold)
        header = f"*[{company}] {role}*\nTask: {task}\n\n"
        max_body = 40000 - len(header) - 100
        parts = [result[i : i + max_body] for i in range(0, len(result), max_body)]

        try:
            client = WebClient(token=self.token)
            if self.use_company_channels and channel != self.channel:
                self._ensure_channel(client, channel)
            for i, part in enumerate(parts):
                text = (header if i == 0 else "") + part
                client.chat_postMessage(channel=channel, text=text)
            return True
        except Exception as e:
            log.error("Slack post failed to %s: %s", channel, e)
            if self.use_company_channels and channel != self.channel:
                try:
                    client = WebClient(token=self.token)
                    text = f"*[{company}] {role}*\nTask: {task}\n\n{result[:39000]}"
                    client.chat_postMessage(channel=self.channel, text=text)
                    return True
                except Exception:
                    pass
            return False
