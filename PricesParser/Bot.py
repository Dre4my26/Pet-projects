"""
Code for @YetAnotherPriceCheckerBot
"""

import telebot
from telebot import types
from bs4_test import parser_price, cartSaver

bot = telebot.TeleBot(
    "5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])  # for commands 'start' and 'help'
def start(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет! Я - бот для парсинга цен и их суммирования. Моя прелесть состоит в "
                                          "том, что я могу <i>суммировать цены на товары с разных сайтов</i>. Для"
                                          " парсинга цены с какого-либо сайта введи команду <b>/price</b>."
                                          "<i>\nУвы, я не умею парсить Ozon, все остальное в Вашем распоряжении!</i>",
                         parse_mode="html")


@bot.message_handler(commands=['cart'])
def cart(message):
    cartSaver(message.chat.id)


@bot.message_handler(commands=['price'])
def get_user_price(message):
    msg = bot.send_message(message.chat.id, 'Введите ссылку на товар:')
    bot.register_next_step_handler(msg, get_user_text)


def get_user_text(message):
    if 'http' in message.text:
        bot.send_message(message.chat.id, parser_price(message.text))

    else:
        bot.reply_to(message, "Ссылка невалидна!")


@bot.message_handler(commands=['help'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # created user buttons
    start_user_command = types.KeyboardButton('/start')
    cart_user_command = types.KeyboardButton('/cart')

    markup.add(start_user_command)
    markup.add(cart_user_command)
    bot.send_message(message.chat.id, 'Глянь на это!', reply_markup=markup)


@bot.message_handler(content_types=['url'])
def url(message):
    bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)
