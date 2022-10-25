from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from repository.db import Base


class Competitor(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    link = relationship('Link', back_populates='competitor')
    price = relationship('Price', back_populates='competitor')


class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    ean = Column(String(20), unique=True, nullable=False)
    title = Column(String(200), nullable=False)
    link = relationship('Link', back_populates='good')
    price = relationship('Price', back_populates='good')

    # def __repr__(self):
    #     return f'{self.ean}'


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    link = Column(String(200), unique=True, nullable=False)
    competitor_id = Column('competitor_id', ForeignKey('competitors.id', ondelete='CASCADE'), nullable=False)
    good_id = Column('good_id', ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    competitor = relationship('Competitor', back_populates='link')
    good = relationship('Good', back_populates='link')

    # def __repr__(self):
    #     return f'{self.link}'


class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    created = Column(DateTime, default=datetime.now())
    change = Column(Boolean, default=False)
    competitor_id = Column('competitor_id', ForeignKey('competitors.id', ondelete='CASCADE'), nullable=False)
    good_id = Column('good_id', ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    competitor = relationship('Competitor', back_populates='price')
    good = relationship('Good', back_populates='price')

    # def __repr__(self):
    #     return f'{self.id}, {self.price}, {self.created}, {self.change}'
