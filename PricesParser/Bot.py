"""
Code for @YetAnotherPriceCheckerBot
"""

import telebot
from telebot import types

bot = telebot.TeleBot(
    "5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])  # for commands 'start' and 'help'
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет! Чем я могу тебе помочь?")


"""
@bot.message_handler(func=lambda message: True) #for gibberish messages
def echo_all(message):
    bot.reply_to(message, "Прости, я тебя не понимаю, попробуй написать /help ")
"""

"""
@bot.message_handler(content_types=['text'])  # for other text messages user sends
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Прости, я тебя не понимаю, попробуй написать /help ", parse_mode='html')
"""


@bot.message_handler(content_types=['photo'])  # for photos user sends
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()  # created in-text buttons
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://vk.com/dreamy26"))
    bot.send_message(message.chat.id, 'Глянь на это!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # created user buttons
    website_user_command = types.KeyboardButton('/website')
    start_user_command = types.KeyboardButton('/start')

    markup.add(website_user_command, start_user_command)
    bot.send_message(message.chat.id, 'Глянь на это!', reply_markup=markup)


bot.polling(none_stop=True)
