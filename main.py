from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from os import getenv


load_dotenv(find_dotenv())
TOKEN = getenv("TOKEN")
YOUTUBE, VK, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("VK_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")


# This command show social network
TxtF= "   Learning Program - проект по обучению пользователей данного бота в котором вы узнаете основы языков:\nС#, Python и JavaScript, а также самые популярные библиотеки. В будущем будет большее количество языков программирования. \nЕсли вы нашли баг напиши нам в соцсетях и мы обязательно его исправим. \nNorthStartStudio"


@bot.message_handler(command = ['start'])
def start_command(message: types.Message):
    bot.reply_to_message(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=murkup)

    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Соц.Сети')
    btn2 = types.KeyboardButton('Курсы📈')
    btn3 = types.KeyboardButton('О боте📃')

#Обработка соц сетей
@bot.message_handler(content_types = ['text'])
def social_command(message):
    if (message.text == 'Соц.Сети'):
        menu = types.InlineKeyboardMarkup()
        menu.add(types.InlineKeyboardButton("YouTube", url=YOUTUBE))
        menu.add(types.InlineKeyboardButton("VK", url=VK))
        menu.add(types.InlineKeyboardButton("TikTok", url=TIKTOK))
        menu.add(types.InlineKeyboardButton("Telegram", url=TG))
        menu.add(types.InlineKeyboardButton("Discord", url=DISCORD))

#Обратботка курсов
@bot.message_handler(content_types = ['text'])
def course_comand(message):
    if (message.text == 'Курсы📈'):
        pass


#Обработка команды 'О боте📃'
@bot.message_handler(content_types = ['text'])
def info_comand(message):
    if (message.text == 'О боте📃'):
        bot.reply_to_message(message.chat.id, TxtF)

bot.polling(non_stop= True, interval=0 )