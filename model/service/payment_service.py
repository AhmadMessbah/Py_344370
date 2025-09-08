from model.repository import *
from model.entity.payment import Payment


class PaymentService:
    def __init__(self):
        self.repo = Repository(Payment)

    def save(self, payment):
        return self.repo.save(payment)

    def edit(self, payment):
        return self.repo.edit(payment)


    def delete(self, id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    def find_by_payment_type(self, payment_type):
        return self.repo.find_by(Payment.payment_type.like(payment_type+"%"))