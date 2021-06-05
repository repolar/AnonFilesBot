# Infinity Bots <https://t.me/Infinity_Bots)
# ImJanindu

import os
import sys
import logging
import pyrogram
import asyncio
from config import Config
from pyrogram import Client, idle, filters

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# vars
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

    
bot = Client(
    "AnonFilesBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)


bot.start()
print("Anon Files Bot Started!\n\nVisit @JEBotZ.")


idle()
bot.stop()
