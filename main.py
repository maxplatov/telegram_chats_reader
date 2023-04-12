import re

from telethon.sync import TelegramClient, events

from config import (
    API_ID,
    API_HASH,
    SESSION_NAME,
    BARAHOLKA_ID,
    BARAHOLKA_ALLOWED_WORDS,
    BARAHOLKA_FORWARD_CHAT_ID,
)


with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
    # for dialog in client.iter_dialogs():
    #     print(dialog.title, dialog.id)

    @client.on(events.NewMessage(chats=(BARAHOLKA_ID)))
    async def handler(event):
        try:
            words = set(re.findall(r'\w+|[^\s\w]+', event.message.to_dict()['message'].lower()))
            if words.intersection(BARAHOLKA_ALLOWED_WORDS):
                await client.forward_messages(BARAHOLKA_FORWARD_CHAT_ID, event.message)
        except Exception:
            pass

    client.run_until_disconnected()
