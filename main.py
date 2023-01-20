import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

user = fake_useragent.UserAgent().random

url = 'https://allo.ua/ua/roboty-pylesosy/'

headers = {'user-agent': fake_useragent.UserAgent().random}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

products = soup.find("div", class_='products-layout__container products-layout--grid')

all_products = products.find_all("div", class_='product-card')

for product in all_products:
    name_pr = product.find("a", class_='product-card__title')
    price_pr = product.find("div", class_='v-pb')
    print(name_pr.text)
    print(price_pr.text)
    with open("products.txt", 'a', encoding='utf-8') as file:
        file.write(f'{name_pr.text}\n')
        file.write(f'{price_pr.text}\n')
