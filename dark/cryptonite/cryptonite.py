import logging
import os

from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Logging Criteria
logging.basicConfig(level=logging.DEBUG)

# Setup & Handlers
BOT_NAME = "Cryptonite"

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
api_token = os.environ['SLACK_BOT_TOKEN']

client = WebClient(token=api_token)

try:
    response = client.chat_postMessage(
        channel="cream",
        text="Cryptonite is online."
    )
except SlackApiError as e:
    assert e.response["error"]
