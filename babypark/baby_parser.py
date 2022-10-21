import os

from bs4 import BeautifulSoup
import requests
import json
from time import time
import csv
from repository.ddl import add_good, add_link, add_prices
from repository.dml import get_price_list

""" Парсер для роботи з сайтом babypark """


def get_category_links():  # збирає посилання на усі категорії з сайту
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
    # }
    # response = requests.get('https://www.babypark.de/overig', headers=headers)
    # if not os.path.exists("babypark/draft"):
    #     os.mkdir("babypark/draft")
    #
    # with open("babypark/draft/page_1.html", "w") as file:
    #     file.write(response.text)

    with open("babypark/draft/page_1.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    links = soup.find_all('div', class_="submenu")
    print(links)


if __name__ == '__main__':
    get_category_links()
