import telebot

bot = telebot.TeleBot("5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Чем я могу тебе помочь?")

bot.polling(none_stop=True, interval=0)