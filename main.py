from constants import *
from logger import logger


@bot.message_handler(commands = ['start'])
def start_command(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) использует команду /start")
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=GLOBAL_MENU)


@bot.message_handler(func=lambda message: message.text == '🌐 СоцСети')
def social_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) смотрит наши соцсети")
    bot.reply_to(message, "Наши соцсети:", reply_markup=SOCIAL_MENU)


@bot.message_handler(func=lambda message: message.text == '🆙 Обновления')
def update_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) смотрит обновления бота")
    bot.reply_to(message, f"Обновления v{VERSION}:\n{LAST_UPDATE}")


@bot.message_handler(func=lambda message: message.text == '📃 О боте')
def about_bot_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) смотрит информацию о боте")
    bot.reply_to(message, ABOUT_BOT)


@bot.message_handler(func=lambda message: message.text in LANGUAGES.keys())
def language_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) смотрит информацию о {message.text}")
    bot.reply_to(message, "Держи полезные источники курса", reply_markup=LANGUAGES[message.text])


@bot.message_handler(func=lambda message: message.text == '📈 Курсы')
def course_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) смотрит информацию о курсах")
    bot.reply_to(message, "Выбери язык программирования:", reply_markup=LANGUAGES_MENU)


@bot.message_handler(func=lambda message: message.text == '◀️ Вернуться')
def return_response(message: types.Message):
    logger.info(f"{message.from_user.full_name} ({message.from_user.id}) возращается в главное меню")
    bot.reply_to(message, "Возращаемся в главное меню...", reply_markup=GLOBAL_MENU)


if __name__ == '__main__':
    bot.infinity_polling(timeout=0)
