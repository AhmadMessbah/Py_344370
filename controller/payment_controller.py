from model.entity.payment import Payment
from model.service.payment_service import PaymentService
import re


class PaymentController:
    def __init__(self):
        self.service = PaymentService()

    def save(self, person_id, title, amount, pay_date, payment_type, description):
        try:
            if re.match(r"^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$", pay_date):
                payment = Payment(None, person_id, title, amount, pay_date, payment_type, description)
                return True, self.service.save(payment)
            else:
                raise ValueError("Invalid Date!!!")
        except Exception as e:
            return False, f"Error !!! {e}"

    def edit(self, id, person_id, title, amount, pay_date, payment_type, description):
        try:
            if re.match(r"^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$", pay_date):
                payment = Payment(id, person_id, title, amount, pay_date, payment_type, description)
                return True, self.service.edit(payment)
            else:
                raise ValueError("Invalid Date!!!")
        except Exception as e:
            e.with_traceback()
            return False, f"Error !!! {e}"

    def delete(self, id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_id(self, id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_payment_type(self, payment_type):
        try:
            return True, self.service.find_by_payment_type(payment_type)
        except Exception as e:
            return False, f"Error: {e}"
