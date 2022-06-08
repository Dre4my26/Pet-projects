"""
Code for @YetAnotherPriceCheckerBot
"""

import telebot
from telebot import types
from bs4_test import parser_desc, parser_price, cartSaver

bot = telebot.TeleBot(
    "5320442299:AAG0L8KCm5zTVeU66taTDM-TTi3BkeARFYY")  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])  # for commands 'start' and 'help'
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start_user_button = types.KeyboardButton("/start")
    price_user_button = types.KeyboardButton("/price")

    markup.add(start_user_button)
    markup.add(price_user_button)

    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет! Я - бот для парсинга цен и их суммирования. Моя прелесть состоит в "
                                          "том, что я могу <i>суммировать цены на товары с разных сайтов</i>. Для"
                                          " парсинга цены с какого-либо сайта введи команду <b>/price</b>."
                                          "<i>\nУвы, я не умею парсить Ozon, все остальное в Вашем распоряжении!</i>",
                         parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=['cart'])
def get_user_cart(message):
    msg = bot.send_message(message.chat.id, "Вот Ваша корзина:")


@bot.message_handler(commands=['price'])
def get_user_price(message):
    msg = bot.send_message(message.chat.id, 'Введите ссылку на товар:')
    bot.register_next_step_handler(msg, get_user_text)


def get_user_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    yes_add_to_cart = types.KeyboardButton("Да")
    no_add_to_cart = types.KeyboardButton("Нет")

    markup.add(yes_add_to_cart, no_add_to_cart)

    if 'http' in message.text:
        msg = bot.send_message(message.chat.id, str(parser_price(message.text)) + '\n' +
                               'Хотите добавить товар в корзину?', reply_markup=markup)
        bot.register_next_step_handler(msg, add_to_cart)
    elif ('127.0.0.1' in message.text) or ('localhost' in message.text):
        bot.send_message(message.chat.id, 'Ах ты хитрый пентестиришко, иди в жопу, ты в бане.')
    else:
        bot.reply_to(message, "Ссылка невалидна!")


def add_to_cart(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # yes_add_to_cart = types.KeyboardButton("Да")
    # no_add_to_cart = types.KeyboardButton("Нет")
    #
    # markup.add(yes_add_to_cart)
    # markup.add(no_add_to_cart)
    # bot.send_message(message.chat.id, 'Хотите добавить товар в корзину?', reply_markup=markup)
    if message.text == "Да":
        bot.reply_to(message, "Товар добавлен в корзину!")
    elif message.text == "Нет":
        bot.reply_to(message, "Понял-понял, вычёркиваю.")
    else:
        bot.reply_to(message, 'Прости, я тебя не понял, попробуй нажимать на кнопки, которые появляются снизу экрана \
или просто написать "Да" или "Нет".')


@bot.message_handler(content_types=['url'])
def url(message):
    bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)
