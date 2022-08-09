from task1.db.base import Base
from sqlalchemy import Column, String, Date, Integer, Float
from sqlalchemy.ext.declarative import declarative_base


class Table1Model(Base):
    __tablename__ = 'Table1'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    en_latter = Column(String)
    ru_letter = Column(String)
    int_numbers = Column(Integer)
    float_numbers = Column(Float)

    def __init__(self, date, en_latter, ru_letter, int_numbers, float_numbers):
        self.date = date
        self.en_latter = en_latter
        self.ru_letter = ru_letter
        self.int_numbers = int_numbers
        self.float_numbers = float_numbers

    def __repr__(self):
        return "<Table1(date='%s', en_latter='%s', ru_letter='%s', int_numbers='%s', float_numbers='%s')>" % \
               (self.date, self.en_latter, self.ru_letter, self.int_numbers, self.float_numbers)
