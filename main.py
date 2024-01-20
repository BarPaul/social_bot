from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from os import getenv


load_dotenv(find_dotenv())
TOKEN = getenv("TOKEN")
YOUTUBE, VK, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("VK_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")


ABOUT_BOT = """   *Learning Program* - проект по обучению пользователей данного бота в котором вы узнаете основы языков:
*С#*, *Python* и JavaScript, а также самые популярные библиотеки. В будущем будет большее количество языков программирования. 
Если вы нашли баг напиши нам в соцсетях и мы обязательно его исправим.
NorthStartStudio"""


# Приветствие
@bot.message_handler(command = ['start'])
def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for btn in ('🌐 СоцСети', '📈 Курсы', '📃 О боте'):
        markup.add(btn)
    bot.reply_to_message(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=markup)


# Обработка о соцсетях
def social_response(message: types.Message):
    menu = types.InlineKeyboardMarkup()
    menu.add(types.InlineKeyboardButton("YouTube", url=YOUTUBE))
    menu.add(types.InlineKeyboardButton("VK", url=VK))
    menu.add(types.InlineKeyboardButton("TikTok", url=TIKTOK))
    menu.add(types.InlineKeyboardButton("Telegram", url=TG))
    menu.add(types.InlineKeyboardButton("Discord", url=DISCORD))
    menu.add(types.InlineKeyboardButton("◀️ Вернуться"))
    bot.reply_to(message, "Наши соцсети:", reply_markup=menu)


# Обработка о курсах
def course_response(message):
    bot.reply_to(message, "Under constraction")


# Обработка о боте
def about_bot_response(message: types.Message):
    bot.reply_to(message, ABOUT_BOT)


# Обработка кнопок
@bot.message_handler(content_types = ['text'])
def button_handler(message: types.Message):
    if message.text == '📃 О боте':
        about_bot_response(message)
    elif message.text == '📈 Курсы':
        course_response(message)
    elif message.text == '🌐 СоцСети':
        social_response()

bot.infinity_polling()
