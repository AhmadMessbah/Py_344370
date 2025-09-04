import re
from datetime import datetime


class Payment:
    def __init__(self, id, person_id, title, amount,pay_date, payment_type, description):
        self.id = id
        self.person_id = person_id
        self.title = title
        self.amount = amount
        self.pay_date = pay_date
        self.payment_type = payment_type
        self.description = description


    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        if re.match(r"^[0-9]{1-10}$", value):
            self._person_id = value
        else:
            raise ValueError("Invalid Person ID !!!")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if re.match(r"^[a-zA-Z\s]{5-20}$", value):
            self._title = value
        else:
            raise ValueError("Wrong Title !!!")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value >= 100:
            self._amount = value
        else:
            raise ValueError("Amount Less Than The Limit !!!")

    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        if re.match(r"^(cash|card|online)$", value, re.IGNORECASE):
            self._payment_type = value.lower()
        else:
            raise ValueError("Invalid Payment Type! Allowed: cash , card , online")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if re.match(r"^[a-zA-Z\s]{5-50}$", value):
            self._description = value
        else:
            raise ValueError("Wrong Description !!!")

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.person_id, self.title, self.amount, self.pay_date, self.payment_type, self.description))
