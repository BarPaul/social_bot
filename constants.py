from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from typing import Final
from os import getenv


load_dotenv(find_dotenv())
TOKEN: Final = getenv("TOKEN")
YOUTUBE, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")


GLOBAL_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
GLOBAL_MENU.keyboard = [['📈 Курсы', '🌐 СоцСети'], ['📃 О боте']]

SOCIAL_MENU = types.InlineKeyboardMarkup()
SOCIAL_MENU.add(types.InlineKeyboardButton(text="YouTube", url=YOUTUBE), types.InlineKeyboardButton(text="TikTok", url=TIKTOK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Telegram", url=TG), types.InlineKeyboardButton(text="Discord", url=DISCORD))


LANGUAGES_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGES_MENU.keyboard = [["💻 C#", "💻 Javascript", "💻 Python"], ["◀️ Вернуться"]]


CSHARP_RESOURCES = types.InlineKeyboardMarkup()
JAVASCRIPT_RESOURCES = types.InlineKeyboardMarkup()
PYTHON_RESOURCES = types.InlineKeyboardMarkup()
CSHARP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text=".NET", url="https://example.com"))
JAVASCRIPT_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text="TypeScript", url="https://example.com"), types.InlineKeyboardButton(text="React", url="https://example.com"))
PYTHON_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text="FastAPI", url="https://example.com"), types.InlineKeyboardButton(text="Django", url="https://example.com"))
LANGUAGES = {'💻 C#': CSHARP_RESOURCES, '💻 Javascript': JAVASCRIPT_RESOURCES, '💻 Python': PYTHON_RESOURCES}


ABOUT_BOT = """*Learning Program* - проект по обучению пользователей, в котором вы узнаете основы языков:
*С#*, *Python* и *JavaScript*, а также самые популярные библиотеки. В будущем наш проект будет пополняться новыми знаниями.
Если вы нашли недочет или есть предложение, напишите нам в соцсетях. Будем рады любому фидбеку :)
©️ *NorthStartStudio*"""
