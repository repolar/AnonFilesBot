#    Copyright (C) 2021 - Infinity Bots
#    This programme is a part of JEBotZ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import logging
import pyrogram
import asyncio
import requests
from config import Config
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


LOGGER = logging.getLogger(__name__)

DOWNLOAD = "./"

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
     await message.reply("**Anon Files Bot Help**\n\nSend me any telegram media file, I'll upload it to anonfiles.com and give you direct download link\n\n**@JEBotZ**")


@bot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)



@bot.on_message(filters.media & filters.private)
async def upload(client, message):
    m = await message.reply("Downloading File...")
    sed = await bot.download_media(
                message, DOWNLOAD
            )
    try:
        files = {'file': open(sed, 'rb')}
        await m.edit("Uploading To Anon Files...")
        r = requests.post("https://api.anonfiles.com/upload", files=files)
        text = r.json()
        output = f"""
<u>**File Uploaded To Anon Files**</u>

**Status:** `{text['status']}`
**Link:** {text['data']['file']['url']['full']}
**ID:** `{text['data']['file']['metadata']['id']}`
**Name:** `{text['data']['file']['metadata']['name']}`
**Size:** `{text['data']['file']['metadata']['size']['readable']}`

**@JEBotZ**"""
        btn = InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Download 📥", url=f"{text['data']['file']['url']['full']}")]])
        await m.edit(output, reply_markup=btn)
        os.remove(sed)
    except Exception as e:
        print(str(e))
        await m.edit(str(e))
        return


bot.start()
LOGGER.info("Anon Files Bot Is Started!")
idle()
