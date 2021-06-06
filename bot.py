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
import time
import logging
import pyrogram
import aiohttp
import asyncio
import requests
import randit
from progress import progress
from config import Config
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

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
    if Config.UPDATES_CHANNEL is not None:
        try:
            user = await client.get_chat_member(Config.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.chat.id,
                    text="Sorry, You are Banned to use me! Contact my [Support Group](https://t.me/InfinityBots_Support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel To Use Me 🏃‍♂**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{Config.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong! Contact my [Support Group](https://t.me/InfinityBots_Support).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    m = await message.reply("Downloading File...")
    now = time.time()
    sed = await bot.download_media(
                message, DOWNLOAD,
          progress=progress,
          progress_args=(
            "Big Files Will Take More Time, Don't Panic!\n\n**ETA:** ", 
            m,
            now
            )
        )
    try:
        files = {'file': open(sed, 'rb')}
        await m.edit("Uploading To Anon Files...")
        callapi = requests.post("https://api.anonfiles.com/upload", files=files)
        text = callapi.json()
        output = f"""
<u>**File Uploaded To Anon Files**</u>

**📂 File Name:** {text['data']['file']['metadata']['name']}
**File Size:** {text['data']['file']['metadata']['size']['readable']}

**📥 Download Link:** `{text['data']['file']['url']['full']}`

**Join @JEBotZ**"""
        btn = InlineKeyboardMarkup(
                                [[InlineKeyboardButton("Download File", url=f"{text['data']['file']['url']['full']}")]])
        await m.edit(output, reply_markup=btn)
        os.remove(sed)
    except Exception:
        await m.edit("Process Failed, Maybe Time Out Due To Large File Size!")
        return
      
@bot.on_message(filters.regex(pattern="https://") & filters.private & ~filters.edited)
async def url(client, message):
    msg = await message.reply("Checking Url...")
    lenk = message.text
    cap = "@JEBotZ"               
    try:
         await msg.edit("Big Files Will Take More Time, Don't Panic!")
         filename = await download(lenk)
         files = {'file': open(filename, 'rb')}
         await msg.edit("Uploading File To Telegram...")
         await message.reply_document(files, caption=cap)
         await msg.delete()
         os.remove(filename)
    except Exception as e:
        await msg.edit("Process Failed, Maybe Time Out Due To Large File Size!")
        print(e)
        
async def download(url):
    ext = url.split(".")[-1]
    filename = str(randint(1000, 9999)) + "." + ext
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return filename
        
        
bot.start()
print("Anon Files Bot Is Started!")
idle()
