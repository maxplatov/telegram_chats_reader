import asyncio

from telethon import TelegramClient, events

from config import API_ID, API_HASH, SESSION_NAME, FORWARD_CHAT_ID, CHANNELS


async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start()

    for channel in CHANNELS:
        chat_id = channel["chat_id"]
        link = channel["link"]
        allowed_words = channel["allowed_words"]

        @client.on(events.NewMessage(chats=chat_id))
        async def handler(event, _link=link, _words=allowed_words):
            try:
                msg = event.message.message.lower()
                if any(word in msg for word in _words):
                    await client.send_message(
                        FORWARD_CHAT_ID, _link + f"/{event.message.id}"
                    )
            except Exception:
                pass

    await client.run_until_disconnected()


asyncio.run(main())
