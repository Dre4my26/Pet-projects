import telebot

bot = telebot.TeleBot("5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def get_text_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")


bot.polling(none_stop=True, interval=0)
