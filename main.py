from telebot import types
from constans import *
from copy import deepcopy


# Приветствие
@bot.message_handler(commands = ['start'])
def start_command(message: types.Message):    
    bot.reply_to(message, f"Привет, *{message.from_user.full_name}*! Выбери действие:", reply_markup=GLOBAL_MENU)


# Обработка о соцсетях
def social_response(message: types.Message):
    bot.reply_to(message, "Наши соцсети:", reply_markup=SOCIAL_MENU)


# Обработка о курсах
def choose_course_version_response(message):
    bot.reply_to(message, "Какую версию выбираете?\n*Пробная версия* - это доступ только к половине курсов\n*Полная версия* - это полный доступ ко всему курсу", reply_markup=VERSIONS)


# Обработка о боте
def about_bot_response(message: types.Message):
    bot.reply_to(message, ABOUT_BOT)


# Платная версия
def full_version_response(message: types.Message):
    if not db.isPurchased(message.from_user.id):
        bot.send_invoice(message.chat.id, title="Оплатите подписку", description="Данная подписка дает вам полный доступ к курсам",
                        invoice_payload=f"fullversion_{message.from_user.id}", currency="RUB", provider_token=PAYLOAD_TOKEN,
                        prices=[types.LabeledPrice("Подписка", PRICE * 100)], reply_to_message_id=message.id
        )
    else:
        bot.reply_to(message, "Спасибо за вашу поддержку 💖. У вас уже открыта полная версия")


# Обработка языков
def language_response(message: types.Message, language_markup: types.InlineKeyboardMarkup):
    if db.isPurchased(message.from_user.id):
        bot.reply_to(message, "У вас открыты все ссылки :)\nСпасибо за вашу поддержку 💖.", reply_markup=language_markup)
    else:
        not_full = types.InlineKeyboardMarkup(keyboard=[[language_markup.keyboard[0][0]]])
        for i in range(1, len(language_markup.keyboard[0])):
            not_full.keyboard[0].append(types.InlineKeyboardButton(f"❌ {language_markup.keyboard[0][i].text}", callback_data="need_subscription"))
        bot.reply_to(message, "У вас открыты не все ссылки :(\nДля их открытия оплатите подписку", reply_markup=not_full)

# Меню курса
def course_response(message: types.Message):
    bot.reply_to(message, "Выберите язык:", reply_markup=LANGUAGES_MENU)


# Обработки кнопки обратно
def return_response(message: types.Message):
    bot.reply_to(message, "Возращаемся в главное меню...", reply_markup=GLOBAL_MENU)


# Обработка кнопок
@bot.message_handler(content_types = ['text'])
def button_handler(message: types.Message):
    if message.text == '📃 О боте':
        about_bot_response(message)
    elif message.text == '📈 Курсы':
        choose_course_version_response(message)
    elif message.text == '🌐 СоцСети':
        social_response(message) 
    elif message.text == '🪙 Подписка':
        full_version_response(message)
    elif message.text == '✏️ Курс':
        course_response(message)
    elif message.text == '💻 C#':
        language_response(message, CSHARP_RESOURCES)
    elif message.text == '💻 Javascript':
        language_response(message, JAVASCRIPT_RESOURCES)
    elif message.text == '💻 Python':
        language_response(message, PYTHON_RESOURCES)
    elif message.text == '◀️ Вернуться':
        return_response(message)


# Обработка успешной оплаты
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message: types.Message):
    # TEST print
    payment = message.successful_payment
    print(payment.currency, payment.order_info, payment.invoice_payload, payment.total_amount, payment.telegram_payment_charge_id, payment.provider_payment_charge_id, payment.shipping_option_id, sep='\n')
    if not db.isPurchased(message.from_user.id):
        db.insertUser(message.from_user.id)


# Обработка нужна подписка
@bot.callback_query_handler(func=lambda _: True)
def subscription_suggestion(call: types.CallbackQuery):
    if call.data == "need_subscription":
        full_version_response(call.message)


bot.infinity_polling()
