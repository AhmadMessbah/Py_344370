import re
from model.tools.date_validation import *
from model.entity.base import Base
from sqlalchemy import *


class DriverLicence(Base):
    __tablename__ = "driver_licence"

    id = Column(Integer, primary_key=True , autoincrement=True)
    person_id = Column(String(30) , nullable=False , unique=True )
    serial = Column(String(30) , nullable=False , unique=True )
    licence_type = Column(String(30) , nullable=False )
    city = Column(String(30) , nullable=False )
    registered_date = Column(String(30) , nullable=False )
    expired_date = Column(String(30) , nullable=False)         #Date?



    def __init__(self, person_id, serial, licence_type, city, registered_date, expired_date):
        self.person_id = person_id
        self.serial = serial
        self.licence_type = licence_type
        self.city = city
        self.registered_date = registered_date
        self.expired_date = expired_date


    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        if re.match(r"^[a-zA-Z0-9\s]{3,30}$", value):
            self._person_id = value

        else:
            raise ValueError("!! invalid Person id !!")


    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        if re.match(r"^[a-zA-Z0-9\-\s]{3,30}$", value):
            self._serial = value

        else:
            raise ValueError("!! invalid Serial !!")


    @property
    def licence_type(self):
        return self._licence_type

    @licence_type.setter
    def licence_type(self, value):
        if re.match(r"^[a-zA-Z0-9\-\s]{3,30}$", value):
            self._licence_type = value

        else:
            raise ValueError("!! invalid licence type !!")


    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if re.match(r"^[a-zA-Z0-9\s]{3,30}$", value):
            self._city = value

        else:
            raise ValueError("!! invalid city name !!")


    @property
    def registered_date(self):
        return self._registered_date

    @registered_date.setter
    def registered_date(self, value):
        if date_validation(value):
            self._registered_date = value

        else:
            raise ValueError("!! invalid registered date !!")


    @property
    def expired_date(self):
        return self._expired_date


    @expired_date.setter
    def expired_date(self, value):
        if date_validation(value):
            self._expired_date = value

        else:
            raise ValueError("!! invalid expired date !!")
