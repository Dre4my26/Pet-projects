from bs4 import BeautifulSoup
import requests


def getter_and_summarizer():
    summ = 0
    print("insert amount of sites:")
    am_sites = int(input())
    for i in range(am_sites):
        print("insert link:")
        link = str(input())
        r = requests.get(link).text
        soup = BeautifulSoup(r, 'html.parser')
        # the first site and price of the good
        price1 = soup.find('p', class_="price title is-size-3 has-text-primary")
        price1 = price1.text
        price1 = price1[3:-5]
        price1 = int(price1)
        summ += price1

    return summ


print(getter_and_summarizer())
