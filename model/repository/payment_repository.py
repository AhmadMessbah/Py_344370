from model.repository.database_manager import transaction_manager


class PaymentRepository:
    def save(self, payment):
        return transaction_manager(
            "insert into payments (person_id, title, amount, pay_date, payment_type, description) values (?,?,?,?,?,?)",
            [payment.person_id, payment.title, payment.amount, payment.pay_date, payment.payment_type,
             payment.description],
            commit=True
        )

    def edit(self, payment):
        return transaction_manager(
            "update payments set person_id=?, title=?, amount=?, pay_date=?, payment_type=?, description=? where id=?",
            [payment.person_id, payment.title, payment.amount, payment.pay_date, payment.payment_type,
             payment.description],
            commit=True
        )

    def delete(self, id):
        return transaction_manager(
            "delete from payments where id=?",
            [id],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from payments",
        )

    def find_by_id(self, id):
        return transaction_manager(
            "select * from payments where id=?",
        )

    def find_by_payment_type(self, payment_type):
        return transaction_manager(
            "select * from payments where payment_type like ?",
            [payment_type + "%"],
        )
