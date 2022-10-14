import json
import time
import schedule

from babypark.spiders.price import main as parser
from google_sheets.quickstart import GoogleSheet
from b_soup.main import main as bs_parser


def worker():
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


def main():
    print('Worker waiting')
    # schedule.every().day.at("15:00").do(worker)
    # schedule.every().day.at("20:21").do(worker)
    # schedule.every().day.at("20:23").do(worker)
    schedule.every(3).hours.do(worker)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
