from decouple import config
from telethon.sync import TelegramClient, functions, events, types
from logging import INFO, basicConfig, getLogger

APP_ID = config("APP_ID", cast=int)
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger(__name__)
try:
    cbot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()


@cbot.on(events.NewMessage())
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')
    elif 'bye' in event.raw_text:
        await event.reply('Goodbye to you too!')
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = await event.get_sender()
        slenderer = replied.sender
        await event.reply(f"replied username is {slenderer.username}. and your username is {sender.username}")


cbot.run_until_disconnected()
