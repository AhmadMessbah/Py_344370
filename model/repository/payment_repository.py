from model.repository.database_manager import transaction_manager
from model.entity.payment import Payment


class PaymentRepository:
    def save(self, payment):
        transaction_manager(
            "insert into payments (person_id, title, amount, pay_date, payment_type, description) values (?,?,?,?,?,?)",
            [payment.person_id, payment.title, payment.amount,payment.pay_date, payment.payment_type,
             payment.description],
            commit=True
        )
        return payment

    def edit(self, payment):
        transaction_manager(
            "update payments set person_id=?, title=?, amount=?, payment_type=?, description=? where id=?",
            [payment.person_id, payment.title, payment.amount, payment.payment_type,
             payment.description, payment.id],
            commit=True
        )
        return payment

    def delete(self, id):
        transaction_manager(
            "delete from payments where id=?",
            [id],
            commit=True
        )
        return id

    def find_all(self):
        payment_list = transaction_manager(
            "select * from payments",
        )
        if payment_list:
            payment_list = list(map(lambda payment: Payment(*payment), payment_list))
            return payment_list

    def find_by_id(self, id):
        payment = transaction_manager(
            "select * from payments where id like ?",
            [id]
        )
        if payment:
            payment = Payment(*payment[0])
            return payment

    def find_by_payment_type(self, payment_type):
        payment_list = transaction_manager(
            "select * from payments where payment_type like ? ",
            [payment_type + "%"],
        )
        if payment_list:
            payment_list = list(map(lambda payment: Payment(*payment), payment_list))
            return payment_list
