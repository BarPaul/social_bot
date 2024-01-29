from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from typing import Final
from database import Database
from os import getenv


load_dotenv(find_dotenv())
TOKEN: Final = getenv("TOKEN")
YOUTUBE, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")
db = Database()


GLOBAL_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
GLOBAL_MENU.keyboard = [['📈 Курсы', '🌐 СоцСети'], ['📃 О боте']]

SOCIAL_MENU = types.InlineKeyboardMarkup()
SOCIAL_MENU.add(types.InlineKeyboardButton(text="YouTube", url=YOUTUBE), types.InlineKeyboardButton(text="TikTok", url=TIKTOK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Telegram", url=TG), types.InlineKeyboardButton(text="Discord", url=DISCORD))

VERSIONS = types.ReplyKeyboardMarkup(resize_keyboard=True)
VERSIONS.keyboard = [['🪙 Подписка', '✏️ Курс'], ['◀️ Вернуться']]
# VERSIONS.keyboard = [['Полная версия', 'Пробная версия'], ['◀️ Вернуться']]

LANGUAGES_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGES_MENU.keyboard = [["💻 C#", "💻 Javascript", "💻 Python"], ["◀️ Вернуться"]]


PRICE = getenv("FULL_PRICE")
PAYLOAD_TOKEN = getenv("PAYLOAD_TOKEN")


CSHARP_RESOURCES = types.InlineKeyboardMarkup()
JAVASCRIPT_RESOURCES = types.InlineKeyboardMarkup()
PYTHON_RESOURCES = types.InlineKeyboardMarkup()
CSHARP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("CSHARP_BASIC")), types.InlineKeyboardButton(text=".NET", url=getenv("CSHARP_NET")))
JAVASCRIPT_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("JAVASCRIPT_BASIC")), types.InlineKeyboardButton(text="TypeScript", url=getenv("JAVASCRIPT_TYPESCRIPT")), types.InlineKeyboardButton(text="React", url=getenv("JAVASCRIPT_REACT")))
PYTHON_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("PYTHON_BASIC")), types.InlineKeyboardButton(text="FastAPI", url=getenv("PYTHON_FASTAPI")), types.InlineKeyboardButton(text="Django", url=getenv("PYTHON_DJANGO")))
LANGUAGES = {'💻 C#': CSHARP_RESOURCES, '💻 Javascript': JAVASCRIPT_RESOURCES, '💻 Python': PYTHON_RESOURCES}


ABOUT_BOT = """*Learning Program* - проект по обучению пользователей, в котором вы узнаете основы языков:
*С#*, *Python* и *JavaScript*, а также самые популярные библиотеки. В будущем наш проект будет пополняться новыми знаниями.
Если вы нашли недочет или есть предложение, напишите нам в соцсетях. Будем рады любому фидбеку :)
©️ *NorthStartStudio*"""