from sqlalchemy import Column, Integer, String
from model.entity.base import Base


class Person(Base):
    # class(Base)
    # __tablename__
    # field --> Column
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    age = Column(Integer)

    def __init__(self, name, family,  age):
        self.name = name
        self.family = family
        self.age = age


