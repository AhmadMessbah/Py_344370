from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from model.tools.decorators import exception_handling


class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    @exception_handling
    def save(self, person_id, title, amount,pay_date, payment_type, description):
        payment = Payment(None, person_id, title, amount,pay_date, payment_type, description)
        return self.service.save(payment)

    @exception_handling
    def edit(self, id, person_id, title, amount,pay_date ,payment_type, description):
        payment = Payment(id, person_id, title, amount,pay_date, payment_type, description)
        return self.service.edit(payment)

    @exception_handling
    def delete(self, id):
        return self.service.delete(id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, id):
        return self.service.find_by_id(id)

    @exception_handling
    def find_by_payment_type(self, payment_type):
        return self.service.find_by_payment_type(payment_type)
