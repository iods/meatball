#!/usr/bin/env python3
#
# Project:   python-meatball
# Copyright: (c) 2021, Rye Miller
#
"""Retrieves various data sets from the Gemini coin exchange

Cryptonite's bot uses the Gemini public API to access up-to-data
cryptocurrency pricing and trading information.
"""

import logging
import os
import requests

from dotenv import load_dotenv
from pathlib import Path
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.webhook import WebhookClient

# Logging Criteria
logging.basicConfig(level=logging.DEBUG)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Setup and Handlers
GEMINI_API_URL = os.environ["GEMINI_API_URL"]
SLACK_BOT_NAME = "Cryptonite"
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_WEBHOOK_CRYPTONITE = os.environ["SLACK_WEBHOOK_CRYPTONITE"]


def get_details():
    """Retrieve the extra details on supported symbols from the Gemini Public API"""

    SYMBOL = 'btcusd'
    CHANNEL = os.environ["SLACK_CHANNEL_ID"]
    URL = os.environ["GEMINI_API_URL"]
    FIAT = 'USD'

    update = ''

    res = requests.get(GEMINI_API_URL  + "/v1/pubticker/" + SYMBOL)
    assert res.status_code == 200

    data = res.json()
    quantity = data['volume']['BTC']
    price = data['volume'][FIAT]

    update += f'Trade volumes for {SYMBOL} after 24 hrs:\nTotal (quantity): {quantity}\nTotal (price): {price}'
    return update


if __name__ == '__main__':
    print(f"{SLACK_BOT_NAME} now online.")
    get_details()


client = WebClient(token=SLACK_BOT_TOKEN)

try:
    response = client.chat_postMessage(
        channel="cream",
        text=get_details()
    )
except SlackApiError as e:
    assert e.response["error"]



