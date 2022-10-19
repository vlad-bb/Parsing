import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re

''' Парсер по сайту BABYPark, приймає список словників, ходить по посиланням і збирає ціну на товар, і додає в словник
Записує в json і повертає True
'''
base_url = 'https://www.babypark.de'


def main(data):
    for d in data:
        link = d['link']
        response = requests.get(base_url + link)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all('span', class_="price")
        try:
            price = content[0].text.replace('€', '').strip()
        except IndexError:
            price = content[0].text.replace('€', '').strip()
        if price == '0,00':
            price = content[1].text.replace('€', '').strip()
        d.update({'price_new': price})
    with open('b_soup/data.json', "w", encoding='utf-8') as fd:
        json.dump(data, fd, ensure_ascii=False)
    return True


if __name__ == '__main__':
    main()
