from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from typing import Final
from os import getenv


load_dotenv(find_dotenv())
TOKEN: Final = getenv("TOKEN")
YOUTUBE, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
VERSION, LAST_UPDATE = getenv("VERSION"), getenv("LAST_UPDATE")
bot = TeleBot(TOKEN, parse_mode="markdown")


GLOBAL_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
GLOBAL_MENU.keyboard = [['📈 Курсы', '🌐 СоцСети'], ['🆙 Обновления', '📃 О боте']]

SOCIAL_MENU = types.InlineKeyboardMarkup()
SOCIAL_MENU.add(types.InlineKeyboardButton(text="YouTube", url=YOUTUBE), types.InlineKeyboardButton(text="TikTok", url=TIKTOK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Telegram", url=TG), types.InlineKeyboardButton(text="Discord", url=DISCORD))


LANGUAGES_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGES_MENU.keyboard = [["💻 C#", "💻 C++",], ["💻 Javascript", "💻 Python"], ['💻 PHP'], ["◀️ Вернуться"]]


CSHARP_RESOURCES = types.InlineKeyboardMarkup()
CPP_RESOURCES = types.InlineKeyboardMarkup()
JAVASCRIPT_RESOURCES = types.InlineKeyboardMarkup()
PYTHON_RESOURCES = types.InlineKeyboardMarkup()
PHP_RESOURCES = types.InlineKeyboardMarkup()
CSHARP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("CSHARP_BASIC")), types.InlineKeyboardButton(text=".NET", url=getenv("CSHARP_NET")))
CPP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("CPP_BASIC")))
JAVASCRIPT_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("JAVASCRIPT_BASIC")), types.InlineKeyboardButton(text="TypeScript", url=getenv("JAVASCRIPT_TYPESCRIPT")), types.InlineKeyboardButton(text="React", url=getenv("JAVASCRIPT_REACT")))
PYTHON_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("PYTHON_BASIC")), types.InlineKeyboardButton(text="FastAPI", url=getenv("PYTHON_FASTAPI")), types.InlineKeyboardButton(text="Django", url=getenv("PYTHON_DJANGO")))
PHP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url=getenv("PHP_BASIC")))
LANGUAGES = {
    '💻 C#': CSHARP_RESOURCES,
    '💻 C++': CPP_RESOURCES,
    '💻 Javascript': JAVASCRIPT_RESOURCES, 
    '💻 Python': PYTHON_RESOURCES,
    '💻 PHP': PHP_RESOURCES
}


ABOUT_BOT = """*Learning Program* - проект по обучению пользователей, в котором вы узнаете основы языков:
*С#*, *C++*, *Python*, *JavaScript* и *PHP*, а также самые популярные библиотеки. В будущем наш проект будет пополняться новыми знаниями.
Если вы нашли недочет или есть предложение, напишите нам в соцсетях. Будем рады любому фидбеку :)
©️ *NorthStartStudio*"""
