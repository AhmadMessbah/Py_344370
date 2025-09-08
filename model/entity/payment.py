from sqlalchemy import Integer,String,Column
from model.entity.base import Base

class Payment(Base):
    __tablename__="payments"

    id=Column(Integer, primary_key=True, autoincrement=True)
    person_id=Column(Integer, nullable=False)
    title=Column(String(30), nullable=False)
    amount=Column(Integer, nullable=False)
    pay_date=Column(String(15))
    payment_type=Column(String(10),nullable=False)
    description=Column(String(30))




    def __init__(self, person_id, title, amount,pay_date, payment_type, description):
        self.person_id = person_id
        self.title = title
        self.amount = amount
        self.pay_date = pay_date
        self.payment_type = payment_type
        self.description = description