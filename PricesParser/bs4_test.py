from bs4 import BeautifulSoup
import requests

"""
That is more or less working way to parse prices from sites different from Ozon, Yandex Market, e.t.c.
"""


def parser_price(link):
    """This function returns the price of an item"""
    price = 'Error when attempted to get price'
    # print("please, insert the link:")
    # link = str(input())
    if "www.ozon.ru" in link:
        price = "Прости, я не умею узнавать цены с озона("
    else:
        r = requests.get(link).text
        soup = BeautifulSoup(r, "html.parser")
        soup = soup.text
        text_from_site = str(soup)
        text_from_site = text_from_site.split(" ")
        for i in range(len(text_from_site)):
            if text_from_site[i] == "Цена" or text_from_site[i] == "цена" or text_from_site[i] == "цене" or \
                    text_from_site[i] == "Цене":
                try:
                    price = int(text_from_site[i + 1])
                except ValueError:
                    price = 'Failed to find the price'
                    print('InvalidParseResultError occurred!')

    return price


def parser_desc(link):
    """This func returns the Title of an item"""
    r = requests.get(link).text
    soup = BeautifulSoup(r, "html.parser")
    title = soup.title.text

    return title


def cartSaver(chat_id):
    chat = []
    chat.append(chat_id)
    for chat[chat_id] in chat:
        cart = {'name': parser_desc(), 'price': parser_price()}
