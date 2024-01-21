from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from typing import Final
from database import Database
from os import getenv


load_dotenv(find_dotenv())
TOKEN: Final = getenv("TOKEN")
YOUTUBE, VK, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("VK_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")
db = Database()


VERSIONS = GLOBAL_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
for btn in ('📈 Курсы', '🌐 СоцСети', '📃 О боте'):
    GLOBAL_MENU.add(btn)

SOCIAL_MENU = types.InlineKeyboardMarkup()
SOCIAL_MENU.add(types.InlineKeyboardButton(text="YouTube", url=YOUTUBE))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="VK", url=VK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="TikTok", url=TIKTOK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Telegram", url=TG))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Discord", url=DISCORD))

for btn in ('📒 Полная', '✏️ Пробная', '◀️ Вернуться'):
    VERSIONS.add(btn)

PRICE = getenv("FULL_PRICE")
PAYLOAD_TOKEN = getenv("PAYLOAD_TOKEN")

ABOUT_BOT = """*Learning Program* - проект по обучению пользователей, в котором вы узнаете основы языков:
*С#*, *Python* и *JavaScript*, а также самые популярные библиотеки. В будущем наш проект будет пополняться новыми знаниями.
Если вы нашли недочет или есть предложение, напишите нам в соцсетях. Будем рады любому фидбеку :)
©️ *NorthStartStudio*"""


# Приветствие
@bot.message_handler(commands = ['start'])
def start_command(message: types.Message):    
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=GLOBAL_MENU)


# Обработка о соцсетях
def social_response(message: types.Message):
    bot.reply_to(message, "Наши соцсети:", reply_markup=SOCIAL_MENU)


# Обработка о курсах
def course_response(message):
    bot.reply_to(message, "Какую версию выбираете?\n*Пробная версия* - это доступ только к половине курсов\n*Полная версия* - это полный доступ ко всему курсу", reply_markup=VERSIONS)


# Обработка о боте
def about_bot_response(message: types.Message):
    bot.reply_to(message, ABOUT_BOT)


# Платная версия
def full_version_response(message: types.Message):
    if db.isPurchased(message.from_user.id):
        bot.send_invoice(message.chat.id, title="Оплати подписку", description="Данная подписка дает вам полный доступ к курсам",
                        invoice_payload=f"fullversion_{message.from_user.id}", currency="RUB", provider_token=PAYLOAD_TOKEN,
                        prices=[types.LabeledPrice("Подписка", PRICE * 100)], reply_to_message_id=message.id
        )
    else:
        bot.reply_to(message, "Спасибо за поддержку проекта :)")


# Бесплатная версия
def trial_version_response(message: types.Message):
    bot.reply_to(message, "Under construction")


# Обработки кнопки обратно
def return_response(message: types.Message):
    bot.reply_to(message, "Возращаемся :)", reply_markup=GLOBAL_MENU)


# Обработка кнопок
@bot.message_handler(content_types = ['text'])
def button_handler(message: types.Message):
    if message.text == '📃 О боте':
        about_bot_response(message)
    elif message.text == '📈 Курсы':
        course_response(message)
    elif message.text == '🌐 СоцСети':
        social_response(message) 
    elif message.text == '📒 Полная':
        full_version_response(message)
    elif message.text == '✏️ Пробная':
        trial_version_response(message)
    elif message.text == '◀️ Вернуться':
        return_response(message)


# Обработка успешной оплаты
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message):
    if not db.isPurchased(message.from_user.id):
        db.insertUser(message.from_user.id)


bot.infinity_polling()
