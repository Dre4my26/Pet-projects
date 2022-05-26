from bs4 import BeautifulSoup
import requests

"""
That is more or less working way to parse prices from sites different from Ozon, Yandex Market, e.t.c.
"""


def parser(link):
    price = 0
    #print("please, insert the link:")
    #link = str(input())
    if "www.ozon.ru" in link:
        price = "Прости, я пока не умею узнавать цены с озона("
    else:
        r = requests.get(link).text
        soup = BeautifulSoup(r, "html.parser")
        soup = soup.text
        text_from_site = str(soup)
        text_from_site = text_from_site.split(" ")
        for i in range(len(text_from_site)):
            if text_from_site[i] == "Цена" or text_from_site[i] == "цена":
                price = int(text_from_site[i + 1])

    return price
