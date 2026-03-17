"""Notion tool - create/update pages for company tracking.

Required database schema:
- Company: Title
- Role: Text (or Rich text)
- Task: Text (or Rich text)
"""
import logging
from .base import Tool

log = logging.getLogger(__name__)


class NotionTool(Tool):
    """Post agent output to Notion. Requires AI_NOTION_API_KEY, AI_NOTION_DATABASE_ID."""

    def __init__(self, api_key: str = "", database_id: str = ""):
        self.api_key = api_key
        self.database_id = database_id
        self._enabled = bool(api_key and database_id)

    def execute(self, company: str, role: str, task: str, result: str) -> bool:
        if not self._enabled:
            return False
        try:
            from notion_client import Client
        except ImportError:
            log.warning("notion-client not installed. pip install notion-client")
            return False
        try:
            client = Client(auth=self.api_key)
            chunk_size = 2000
            children = []
            for i in range(0, len(result), chunk_size):
                chunk = result[i : i + chunk_size]
                children.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"text": {"content": chunk}}]},
                })
            if not children:
                children = [{"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "(empty)"}}]}}]
            client.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    "Company": {"title": [{"text": {"content": company[:2000]}}]},
                    "Role": {"rich_text": [{"text": {"content": role[:2000]}}]},
                    "Task": {"rich_text": [{"text": {"content": task[:2000]}}]},
                },
                children=children,
            )
            return True
        except Exception as e:
            log.error("Notion create failed: %s. Check DB schema: Company (Title), Role (Text), Task (Text)", e)
            return False
