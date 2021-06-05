# Infinity Bots <https://t.me/Infinity_Bots)
# ImJanindu

import os
import sys
import logging
import pyrogram
import asyncio
from config import Config
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


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


@bot.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start(client, message):
    await message.reply("Heya, I'm **Anon Files** Bot 👨‍💻 \n\nClick on help to find out how to use me \n\n**@JEBotZ**",
                         reply_markup=InlineKeyboardMarkup(
                                [
                                   [InlineKeyboardButton(
                                        "Help", callback_data="help")],
                                   [InlineKeyboardButton(
                                        "Channel", url="https://t.me/Infinity_BOTs"),
                                    InlineKeyboardButton(
                                        "Source", url="https://github.com/ImJanindu/AnonFilesBot")]]))      


async def help(client, message):
     await message.reply("**Help**\n\nSend me any telegram media file, I'll upload it to anonfiles.com and give direct download link\n\n**@JEBotZ**")


@bot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)


bot.start()
LOGGER.info("Anon Files Bot Is Started!")
idle()
