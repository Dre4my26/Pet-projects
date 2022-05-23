import telebot

bot = telebot.TeleBot(
    "5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет! Чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Я пока не умею помогать((")

@bot.message_handler(func= lambda message:True)
def echo_all(message):
    bot.reply_to(message, "Прости, я тебя не понимаю, попробуй написать /help ")

bot.polling(none_stop=True, interval=0)
