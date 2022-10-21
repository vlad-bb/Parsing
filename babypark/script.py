import json
from time import time
import csv

from babypark.spiders.price import main as parser
from google_sheets.quickstart import GoogleSheet
from b_soup.main import main as bs_parser
from repository.ddl import add_good, add_link, add_prices
from repository.dml import get_price_list


def worker():  # функція читання/запису цін в/з google sheets
    data_list = []
    gs = GoogleSheet()
    table_value = gs.get_values()
    print("Start reading from table")
    for index, row in enumerate(table_value):
        index += 3
        ean_number = row[1]
        link = row[5].replace('https://www.babypark.de/', '/')
        try:
            price = row[6]
        except IndexError:
            price = 0.00
        # print(f'Index {index} EAN {ean_number} LINK {link} PRICE {price}')
        if ean_number != '' and link != '9':
            data = {'index': index, 'ean_number': ean_number, 'link': link, 'price_old': price}
            data_list.append(data)
    print("Start parsing")
    if bs_parser(data_list):
        with open('b_soup/data.json', "r", encoding='utf-8') as fd:
            parse_data = json.load(fd)

        print("Start writing in table")
        for pd in parse_data:
            if pd['price_new'] != pd['price_old']:
                flag = 'True'
            else:
                flag = 'False'
            price = pd['price_new']
            index = pd['index']
            range_cell = f'table!G{index}:H{index}'
            values = [[price, flag]]
            time.sleep(1.2)
            gs.update_cell(range_cell, values)
    print('Table was updated')


def feed_goods():  # функція наповнення товарів з google sheets
    gs = GoogleSheet()
    table_value = gs.get_values()
    add_good(table_value)


def feed_links():  # функція наповнення посилань з google sheets
    gs = GoogleSheet()
    table_value = gs.get_values()
    add_link(table_value)


def feed_prices():  # функція наповлення цінами за допомогою парсера сайта
    add_prices()


def get_csv(file):  # Функція отримання csv файлу цін з БД
    price_list = get_price_list()
    with open(file, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['EAN number', 'price EUR']
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in price_list:
            writer.writerow(row)
    print(f'CSV is ready, check {file}')



def main():
    print('Worker waiting')
    # schedule.every().day.at("15:00").do(worker)
    # schedule.every().day.at("20:21").do(worker)
    # schedule.every().day.at("20:23").do(worker)
    # schedule.every(3).hours.do(worker)
    # worker()
    # feed_goods()
    # feed_links()
    # feed_prices()
    get_csv('data/babypark_price.csv')

    # while True:
    #     schedule.run_pending()


if __name__ == '__main__':
    timer = time()
    main()
    print(f'Work time {round(time() - timer, 4)}')
