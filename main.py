from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from os import getenv


load_dotenv(find_dotenv())
TOKEN = getenv("TOKEN")
YOUTUBE, VK, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("VK_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")


# This command show social network
@bot.message_handler(commands=["start"])
def start_command(message: types.Message):
    menu = types.InlineKeyboardMarkup()
    menu.add(types.InlineKeyboardButton("YouTube", url=YOUTUBE))
    menu.add(types.InlineKeyboardButton("VK", url=VK))
    menu.add(types.InlineKeyboardButton("TikTok", url=TIKTOK))
    menu.add(types.InlineKeyboardButton("Telegram", url=TG))
    menu.add(types.InlineKeyboardButton("Discord", url=DISCORD))
    bot.reply_to_message(message, f"Привет, *{message.from_user.full_name}*! Какую соцсеть вы хотите посетить?", reply_markup=menu)


# Комментиккккккккккккккккккккккккк


bot.infinity_polling()