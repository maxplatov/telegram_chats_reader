from telethon.sync import TelegramClient, events

from config import (
    API_ID,
    API_HASH,
    SESSION_NAME,
    BARAHOLKA_ID,
    BARAHOLKA_LINK,
    BARAHOLKA_ALLOWED_WORDS,
    BARAHOLKA_FORWARD_CHAT_ID,
)


with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
    # for dialog in client.iter_dialogs():
    #     print(dialog.title, dialog.id)

    @client.on(events.NewMessage(chats=(BARAHOLKA_ID)))
    async def handler(event):
        try:
            msg = event.message.to_dict()['message'].lower()
            if any(word in msg for word in BARAHOLKA_ALLOWED_WORDS):
                await client.send_message(
                    BARAHOLKA_FORWARD_CHAT_ID, BARAHOLKA_LINK + f"/{event.message.id}"
                )
        except Exception:
            pass

    client.run_until_disconnected()
