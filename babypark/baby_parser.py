import datetime
import os
import pickle
import random
from time import sleep, time
from bs4 import BeautifulSoup
import requests
import json
import csv
from repository.ddl import add_good, add_link, add_prices
from repository.dml import get_price_list

""" Парсер для роботи з сайтом babypark """

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}


def get_category_links():  # збирає посилання на усі категорії з сайту
    response = requests.get('https://www.babypark.de/overig', headers=HEADERS).text
    # if not os.path.exists("babypark/draft"):
    #     os.mkdir("babypark/draft")
    #
    # with open("babypark/draft/page_1.html", "w") as file:
    #     file.write(response)
    #
    # with open("babypark/draft/page_1.html") as file:
    #     response = file.read()

    soup = BeautifulSoup(response, 'lxml')
    urls_set = set()
    links = soup.find('ul', class_="submenu").find_all('a')
    for link in links:
        url = link['href']
        urls_set.add(url)
    with open("babypark/draft/category_urls_set.bin", "wb") as file:
        pickle.dump(urls_set, file)
    print('[INFO] Category links were collect. Check file babypark/draft/category_urls_set.bin')


def get_goods_link():  # Збирає посилання на товар зі списку категорій
    filename = 'babypark/draft/category_urls_set.bin'
    with open(filename, 'rb') as file:
        urls_set = pickle.load(file)
        total = len(urls_set)
        counter = 0
        goods_urls_set = set()
        for url in urls_set:
            response = requests.get(url, headers=HEADERS).text
            # with open(f"babypark/draft/category_{limit}.html", "w") as fh:
            #     fh.write(response)
            # with open(f"babypark/draft/category_0.html") as fh:
            #     response = fh.read()
            soup = BeautifulSoup(response, 'lxml')
            links = soup.find_all(class_="product details product-item-details")
            for link in links:
                try:
                    link_ = link.find('a', class_="product-item-link")
                    url = link_['href']
                    goods_urls_set.add(url)
                except Exception as err:
                    print(err)
                    continue
            counter += 1
            print(f"[INFO] Scaning page: {counter}/{total}")
            sleep(random.randrange(2, 4))
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"babypark/draft/goods_urls_set_{cur_time}.bin", "wb") as file_set:
        pickle.dump(goods_urls_set, file_set)
        print(
            f'[INFO]Goods links were collect.\nAmount {len(goods_urls_set)}.\nCheck file babypark/draft/goods_urls_set.bin')


if __name__ == '__main__':
    timer = time()
    # get_category_links()
    # get_goods_link() # Результат 4600 посилань, за 2000 секунд
    print(f'Work time {round(time() - timer, 4)} sec')
