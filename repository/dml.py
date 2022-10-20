"""
Файл для команд DML - маніполювання данними
"""

import sqlalchemy

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


if __name__ == '__main__':
    pass
