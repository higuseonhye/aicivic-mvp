"""Notion tool - create/update pages for company tracking."""
from typing import Optional
from .base import Tool


class NotionTool(Tool):
    """Post agent output to Notion. Requires NOTION_API_KEY and NOTION_DATABASE_ID in .env."""

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
            return False
        try:
            client = Client(auth=self.api_key)
            client.pages.create(
                parent={"database_id": self.database_id},
                properties={
                    "Company": {"title": [{"text": {"content": company}}]},
                    "Role": {"rich_text": [{"text": {"content": role}}]},
                    "Task": {"rich_text": [{"text": {"content": task[:200]}}]},
                },
                children=[{
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"text": {"content": result[:2000]}}]},
                }],
            )
            return True
        except Exception:
            return False
