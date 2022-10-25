"""
Файл для команд DML - маніполювання данними
"""

import sqlalchemy
from sqlalchemy import and_

from repository.db import session
from repository.model import Competitor, Good, Link, Price


class ExceptError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        try:
            return self.func(*args)
        except sqlalchemy.exc.IntegrityError:
            print('Key already exists')


def get_ean_by_id(id_):
    result = session.query(Good.ean).filter(Good.id == id_).first()
    if result:
        print(result[0])
    print('None')


def check_unique_ean(ean_):
    result = session.query(Good.ean).filter(Good.ean == ean_).first()
    return result


def check_unique_link(link_):
    result = session.query(Link.link).filter(Link.link == link_).first()
    return result


def get_price_list():
    price_list = []
    results = session.query(Good, Price).join(Price).filter(Good.id == Price.good_id).order_by(
        Price.good_id).distinct(Price.good_id).all()
    for good, price in results:
        item = {'Title': good.title, 'EAN number': good.ean, 'price EUR': price.price}
        price_list.append(item)
    return price_list


if __name__ == '__main__':
    get_price_list()
