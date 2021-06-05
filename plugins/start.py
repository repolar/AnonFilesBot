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


from bot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, InputTextMessageContent


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
