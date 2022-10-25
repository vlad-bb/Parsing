import datetime
import os
import pickle
import random
import re
from time import sleep, time
from bs4 import BeautifulSoup
import requests
import json
import csv
from repository.ddl import add_good, add_link, add_prices, add_good_baby, add_link_baby, add_price_baby
from repository.dml import get_price_list

""" Парсер для роботи з сайтом babypark """

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}
cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")


def get_category_links():  # збирає посилання на усіх категорії сайту
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

    with open(f"babypark/draft/goods_urls_set_{cur_time}.bin", "wb") as file_set:
        pickle.dump(goods_urls_set, file_set)
        print(
            f'[INFO]Goods links were collect.\nAmount {len(goods_urls_set)}.\nCheck file babypark/draft/goods_urls_set_{cur_time}.bin')


def feed_data(filename):  # парсить сайт за допомогою лінків, за записує в БД інформацію про товар, лінк, та ціну
    with open(filename, 'rb') as file:
        goods_urls_set = pickle.load(file)
    limit = 20
    total = len(goods_urls_set)
    counter = 0
    problem_links = []
    for url in goods_urls_set:
        limit -= 1
        if limit == 0:
            break
        # print(url)
        # print(f'[INFO] Parsing link {limit}')
        response = requests.get(url, headers=HEADERS).text
        # with open(f"babypark/draft/good_{limit}.html", "w") as fh:
        #     fh.write(response)
        # with open(f"babypark/draft/good_{limit}.html") as fh:
        #     response = fh.read()
        soup = BeautifulSoup(response, 'lxml')
        counter += 1
        print(f"[INFO] Scaning page: {counter}/{total}")
        try:
            tables = soup.find('table', class_='data table additional-attributes').find_all('td', class_="col data")
            title_ = soup.title.text.split('|')
            content = soup.find_all('meta')
            for table in tables:
                ean = table.text.strip()
                if ean.isdigit() and len(ean) == 13:
                    title = title_[0].strip()
                    add_good_baby(ean, title)
                    sleep(random.randrange(1, 2))
                    add_link_baby(url, ean)
                    for row in content:
                        try:
                            if 'product:price:amount' == row['property']:
                                price_ = float(row['content'])
                                add_price_baby(price_, ean)
                        except KeyError:
                            continue
        except Exception as err:
            print(err)
            problem_links.append(url)
            continue
    # if len(problem_links) > 0:
    #     with open(f'babypark/draft/problem_links_{cur_time}.json', 'a') as jf:
    #         json.dump(problem_links, jf, indent=4)


def get_csv():  # Функція отримання csv файлу цін з БД
    price_list = get_price_list()
    total = len(price_list)
    with open(f'data/price_list_{cur_time}.csv', 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['Title', 'EAN number', 'price EUR']
        writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in price_list:
            writer.writerow(row)
    print(f'[INFO] CSV was created. Items {total} in table.')


if __name__ == '__main__':
    timer = time()
    # get_category_links()
    # get_goods_link() # Результат 4600 посилань, за 2000 секунд
    # feed_data('babypark/draft/goods_urls_set.bin')
    # get_csv()

    print(f'Work time {round(time() - timer, 4)} sec')
