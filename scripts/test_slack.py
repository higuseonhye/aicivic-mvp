"""Test Slack connection and channel creation. Run: python scripts/test_slack.py"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
load_dotenv()

def main():
    token = os.getenv("AI_SLACK_BOT_TOKEN", "")
    channel = os.getenv("AI_SLACK_CHANNEL", "")
    if not token:
        print("ERROR: AI_SLACK_BOT_TOKEN not set in .env")
        return 1
    if not channel:
        print("ERROR: AI_SLACK_CHANNEL not set in .env")
        return 1

    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError

    client = WebClient(token=token)
    print("1. Testing auth...")
    try:
        client.auth_test()
        print("   OK")
    except SlackApiError as e:
        print(f"   FAILED: {e.response.get('error', e)}")
        return 1

    print("2. Posting to default channel...")
    try:
        client.chat_postMessage(channel=channel, text="Test from AI Civic MVP")
        print(f"   OK - check {channel}")
    except SlackApiError as e:
        print(f"   FAILED: {e.response.get('error', e)}")
        if e.response.get("error") == "channel_not_found":
            print("   -> Create the channel and invite the bot")
        elif e.response.get("error") == "not_in_channel":
            print("   -> Invite the bot to the channel")
        return 1

    print("3. Testing channel create (ai-test-channel)...")
    try:
        resp = client.conversations_create(name="ai-test-channel", is_private=False)
        print(f"   OK - created #{resp['channel']['name']}")
    except SlackApiError as e:
        err = e.response.get("error", "")
        if err == "name_taken":
            print("   Channel exists, trying to join...")
            try:
                for c in client.conversations_list(types="public_channel", limit=500).get("channels", []):
                    if c.get("name") == "ai-test-channel":
                        client.conversations_join(channel=c["id"])
                        print("   OK - joined")
                        break
                else:
                    print("   Could not find channel in list")
            except SlackApiError as e2:
                print(f"   FAILED: {e2.response.get('error', e2)}")
                print("   -> Add scopes: channels:manage, channels:read, channels:join")
        else:
            print(f"   FAILED: {err}")
            print("   -> Add scopes: channels:manage, channels:read, channels:join")
        return 1

    print("\nAll tests passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
