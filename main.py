from constants import *
from logger import logger


@bot.message_handler(commands = ['start'])
def start_command(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) вводит команду /start")
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=GLOBAL_MENU)


@bot.message_handler(func=lambda message: message.text == '🌐 СоцСети')
def social_response(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) открывает список социальных сетей")
    bot.reply_to(message, "Наши соцсети:", reply_markup=SOCIAL_MENU)


@bot.message_handler(func=lambda message: message.text == '📈 Курсы')
def choose_course_version_response(message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) открывает список курсов")
    bot.reply_to(message, "Напоминаем вам, если вы не покупали подписку, то некоторая часть курса будет для вас закрыта\nПосле покупки подписки вы получите полный доступ курсу + благодарность за поддержку :)", reply_markup=VERSIONS)


@bot.message_handler(func=lambda message: message.text == '📃 О боте')
def about_bot_response(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) открывает информацию о боте")
    bot.reply_to(message, ABOUT_BOT)


@bot.message_handler(func=lambda message: message.text == '🪙 Подписка')
def full_version_response(message: types.Message):
    if not db.isPurchased(message.from_user.id):
        logger.info(f"{message.from_user.full_name} ({message.from_user.id}) намеревает купить подписку")
        bot.send_invoice(message.chat.id, title="Оплатите подписку", description="Данная подписка дает вам полный доступ к курсам",
                        invoice_payload=f"fullversion_{message.from_user.id}", currency="RUB", provider_token=PAYLOAD_TOKEN,
                        prices=[types.LabeledPrice("Подписка", PRICE * 100)], reply_to_message_id=message.id
        )
    else:
        logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) пытался еще раз нас поддержать")
        bot.reply_to(message, "Спасибо за вашу поддержку 💖. У вас уже открыта полная версия")


@bot.message_handler(func=lambda message: message.text in LANGUAGES.keys())
def language_response(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) выбрал язык {message.text} для курса")
    if db.isPurchased(message.from_user.id):
        return bot.reply_to(message, "У вас открыты все ссылки :)\nСпасибо за вашу поддержку 💖", reply_markup=LANGUAGES[message.text])
    not_full = types.InlineKeyboardMarkup(keyboard=[[LANGUAGES[message.text].keyboard[0][0]]])
    for i in range(1, len(LANGUAGES[message.text].keyboard[0])):
        not_full.keyboard[0].append(types.InlineKeyboardButton(f"❌ {LANGUAGES[message.text].keyboard[0][i].text}", callback_data="need_subscription"))
    bot.reply_to(message, "У вас открыты не все ссылки :(\nДля их открытия оплатите подписку", reply_markup=not_full)


@bot.message_handler(func=lambda message: message.text == '✏️ Курс')
def course_response(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) выбирает язык для курса")
    bot.reply_to(message, "Выберите язык:", reply_markup=LANGUAGES_MENU)


@bot.message_handler(func=lambda message: message.text == '◀️ Вернуться')
def return_response(message: types.Message):
    logger.debug(f"{message.from_user.full_name} ({message.from_user.id}) вернулся в главное меню")
    bot.reply_to(message, "Возращаемся в главное меню...", reply_markup=GLOBAL_MENU)


@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message):
    # TEST print
    payment = message.successful_payment
    print(payment.currency, payment.order_info, payment.invoice_payload, payment.total_amount, payment.telegram_payment_charge_id, payment.provider_payment_charge_id, payment.shipping_option_id, sep='\n')
    try:
        if not db.isPurchased(message.from_user.id):
            db.insertUser(message.from_user.id)
        logger.warning(f"{message.from_user.full_name} ({message.from_user.id}) приобрел подписку! 🟢")
    except Exception as e:
        logger.error(f"{message.from_user.full_name} ({message.from_user.id}) получил ошибку во время приобретения подписки\n{e}")


@bot.callback_query_handler(func=lambda call: call.data == "need_subscription")
def subscription_suggestion(call: types.CallbackQuery):
    full_version_response(call.message)


bot.infinity_polling(0)
