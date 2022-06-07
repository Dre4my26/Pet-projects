from bs4 import BeautifulSoup
import requests
import doctest

"""
That is more or less working way to parse prices from sites different from Ozon, Yandex Market, e.t.c.
"""
"""
Links for testing:
https://market.yandex.ru/product--gliukozamin-khondroitinovyi-kompleks-kaps-60-fpsh-bad/1422663471?glfilter=17796083%3A60~60_227830179&cpa=1&cpc=lZmv57Na288TBs1Tttutnc1YjZf9faNzBI4hLcp_qkHdJ_2MB_ht3v_IvsvCNnPjt227wqsZtyT9tXfE2H81y4LU6b0BiLVqHyqeFANorUro3CU-XOXtc-u04Pe9myttLi6ckPjrb4DI4QSvp9W0Z49YW2-TKztTdCDgRnpFFCv679FjMtt4Gw%2C%2C&sku=227830179&offerid=d3a7F99_kwSRondon6hY0w
https://sbermegamarket.ru/catalog/details/besprovodnye-naushniki-xiaomi-redmi-airdots-2-cn-black-600002233402/
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
    """This func returns the Title of an item

    >>> parser_desc("https://sbermegamarket.ru/catalog/details/besprovodnye-naushniki-xiaomi-redmi-airdots-2-cn-black-\
600002233402")
    'Беспроводные наушники Xiaomi '
    >>> parser_desc("https://market.yandex.ru/product--gliukozamin-khondroitinovyi-kompleks-kaps-60-fpsh-bad/142266347\
1?glfilter=17796083%3A60~60_227830179&cpa=1&cpc=lZmv57Na288TBs1Tttutnc1YjZf9faNzBI4hLcp_qkHdJ_2MB_ht3v_IvsvCNnPjt227wq\
sZtyT9tXfE2H81y4LU6b0BiLVqHyqeFANorUro3CU-XOXtc-u04Pe9myttLi6ckPjrb4DI4QSvp9W0Z49YW2-TKztTdCDgRnpFFCv679FjMtt4Gw%2C%2C\
&sku=227830179&offerid=d3a7F99_kwSRondon6hY0w")
    'Глюкозамин-хондроитиновый комплекс капс. '
    """

    r = requests.get(link).content
    soup = BeautifulSoup(r, "html.parser")
    title = soup.title.text
    title_list = title.split(" ")
    title_short = title_list[:3]
    title_fin = ''
    for i in range(len(title_short)):
        title_fin += title_short[i] + ' '

    return title_fin


def cartSaver(chat_id):
    chat = []
    chat.append(chat_id)
    for chat[chat_id] in chat:
        cart = {'name': parser_desc(), 'price': parser_price()}

    return cart


if __name__ == "__main__":
    doctest.testmod()
