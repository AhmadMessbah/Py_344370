from model.repository.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repo = PaymentRepository()

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
        return self.repo.find_by_payment_type(payment_type)