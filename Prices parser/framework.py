from bs4 import BeautifulSoup
import requests
from price_parser import Price

currencies = "₽$"

print("please, insert the link:")
link = str(input()) # https://fast-anime.ru/Copybooks/originalnaya-tetrad-smerti/
r = requests.get(link).text
soup = BeautifulSoup(r, "html.parser")
soup = soup.text
soup = str(soup)
soup = soup.split(' ')
for i in soup:
    if i.isnumeric():
        print(i, "- numeric", end=" ")
    if i in currencies:
        print("Currency is:", i, end=" ")

print(soup)
price = Price.fromstring(soup)
print(price)
