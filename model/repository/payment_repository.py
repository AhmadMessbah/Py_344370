from model.repository.database_manager import transaction_manager


def save(person_id, title, amount, pay_date, payment_type, description):
    transaction_manager(
        'insert into payments (person_id, title, amount, pay_date, payment_type, description) values (?,?,?,?,?,?)',
        [person_id, title, amount, pay_date, payment_type, description],
        commit=True
        )


def edit(id, person_id, title, amount, pay_date, payment_type, description):
    transaction_manager('update payments set person_id=?, title=?,'
                        ' amount=?, pay_date=?, payment_type=?, description=? where id=?',
                        [person_id, title, amount, pay_date, payment_type, description, id],
                        commit=True
                        )


def remove(id):
    transaction_manager('delete from payments where id =?',
                        [id],
                        commit=True)


def find_all():
    return transaction_manager("select * from payments")


def find_by_id(id):
    return transaction_manager(
        "select * from payments where id = ? ",
        [id]
    )


def find_by_payment_type(payment_type):
    return transaction_manager(
        "select * from payments where payment_type = ? ",
        [payment_type]
    )