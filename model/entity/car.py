from sqlalchemy import Column, Integer, String

from model.entity.base import Base


class Car(Base):
    __tablename__ = "car_table"


    id = Column(Integer, primary_key=True)
    name = Column(String(30))