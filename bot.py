# Infinity Bots <https://t.me/Infinity_Bots)
# ImJanindu

import os
import sys
import logging
import pyrogram
import asyncio
from config import Config
from plugins import *
from pyrogram import Client, filters, idle

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

# vars
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

    
bot = Client(
    "AnonFilesBot",
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)


bot.start()
LOGGER.info("Anon Files Bot Is Started!")
idle()
