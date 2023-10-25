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

BARAHOLKA_ID = CONFIG["baraholka"].get("chat_id")
BARAHOLKA_LINK = CONFIG["baraholka"].get("link")
BARAHOLKA_ALLOWED_WORDS = set(CONFIG["baraholka"].get("allowed_words"))
BARAHOLKA_FORWARD_CHAT_ID = CONFIG["baraholka"].get("forward_chat_id")
