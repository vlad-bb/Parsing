"""
Файл для команд DDL - наповення БД данними
"""
from db import session
from model import Competitor, Good, Link, Price


def add_competitor(name):  # функція додавання в БД нового конкурента
    competitor = Competitor(name=name)
    session.add(competitor)
    session.commit()


def add_good(ean):  # функція додавання в БД нових товарів
    good = Good(ean=ean)
    session.add(good)
    session.commit()


# def add_link(link):
#     link = Link(link=link)
#     session.add(link)
#     session.commit()


if __name__ == '__main__':
    pass
