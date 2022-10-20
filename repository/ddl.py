"""
Файл для команд DDL - наповення БД данними
"""
import re

import requests
import sqlalchemy
from typing import List

from sqlalchemy.dialects.postgresql import psycopg2
from bs4 import BeautifulSoup
from repository.db import session
from repository.model import Competitor, Good, Link, Price
from repository.dml import check_unique_ean, check_unique_link


class ExceptError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except sqlalchemy.exc.IntegrityError as err:
            print(err)
        except sqlalchemy.exc.PendingRollbackError as err:
            print(err)
        except psycopg2.errors.UniqueViolation as err:
            print(err)


def add_competitor(name):  # функція додавання в БД нового конкурента
    competitor = Competitor(name=name)
    session.add(competitor)
    session.commit()


@ExceptError
def add_good(data: List[list]):  # функція додавання в БД нових товарів
    for row in data:
        ean = row[1]
        if ean:
            if not check_unique_ean(int(ean)):
                good = Good(ean=int(ean))
                session.add(good)
    session.commit()
    print('EAN was added')


def add_link(data: List[list]):
    for row in data:
        link = row[5]
        ean_number = row[1]
        if ean_number != '' and link != '9':
            if not check_unique_link(link):
                good_id = session.query(Good.id).filter(Good.ean == int(ean_number)).first()
                link = Link(link=link,
                            competitor_id=1,
                            good_id=good_id[0])
                session.add(link)
    session.commit()
    print('Links were added')


def add_prices():
    results = session.query(Good, Link).join(Link).filter(Good.id == Link.good_id).limit(5).all()
    for good, link in results:
        ean = good.ean
        link = link.link
        print(link)
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find_all('meta')
        for row in content:
            try:
                if 'product:price:amount' == row['property']:
                    price = row['content']
                    print(price, type(price))
            except KeyError:
                continue


if __name__ == '__main__':
    pass
