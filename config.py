import os

import yaml


_STD_CONFIG_PATH = "config.yml"

if os.getenv("APP_CONFIG_PATH"):
    _STD_CONFIG_PATH = os.getenv("APP_CONFIG_PATH")

with open(_STD_CONFIG_PATH, "r") as config_file:
    CONFIG = yaml.safe_load(config_file)

API_ID = CONFIG["telegram_client"].get("api_id")
API_HASH = CONFIG["telegram_client"].get("api_hash")
SESSION_NAME = CONFIG["telegram_client"].get("session_name")

FORWARD_CHAT_ID = CONFIG.get("forward_chat_id")

CHANNELS = [
    {
        "chat_id": ch.get("chat_id"),
        "link": ch.get("link"),
        "allowed_words": set(ch.get("allowed_words", [])),
    }
    for ch in CONFIG.get("channels", [])
]
