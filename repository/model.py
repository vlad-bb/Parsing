from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from db import Base


class Competitor(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    link = relationship('Link', back_populates='competitor')
    price = relationship('Price', back_populates='competitor')


class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    ean = Column(Integer, unique=True, nullable=False)
    link = relationship('Link', back_populates='good')
    price = relationship('Price', back_populates='good')


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    link = Column(String(120), unique=True, nullable=False)
    competitor_id = Column('competitor_id', ForeignKey('competitors.id', ondelete='CASCADE'), nullable=False)
    good_id = Column('good_id', ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    competitor = relationship('Competitor', back_populates='link')
    good = relationship('Good', back_populates='link')


class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    created = Column(DateTime, default=datetime.now())
    competitor_id = Column('competitor_id', ForeignKey('competitors.id', ondelete='CASCADE'), nullable=False)
    good_id = Column('good_id', ForeignKey('goods.id', ondelete='CASCADE'), nullable=False)
    competitor = relationship('Competitor', back_populates='price')
    good = relationship('Good', back_populates='price')
