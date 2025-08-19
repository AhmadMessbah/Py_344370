from model.repository import payment_repository


def save(person_id, title, amount, pay_date, payment_type, description):
    if 500 > amount:
        raise ValueError("Payment Is Less Than The Allowed Limit !!!")
    return payment_repository.save(person_id, title, amount, pay_date, payment_type, description)


def edit(id, person_id, title, amount, pay_date, payment_type, description):
    pay = payment_repository.find_by_id(id)
    if pay:
        if 500 > amount:
            raise ValueError("Payment Is Less Than The Allowed Limit !!!")
        return payment_repository.edit(id, person_id, title, amount, pay_date, payment_type, description)
    else:
        raise ValueError("Invalid ID !!!")


def remove(id):
    pay = payment_repository.find_by_id(id)
    if pay:
        return payment_repository.find_by_id(id)
    else:
        raise ValueError("Invalid ID !!!")


def find_all():
    return payment_repository.find_all()


def find_by_id(id):
    return payment_repository.find_by_id(id)


def find_by_payment_type(payment_type):
    return payment_repository.find_by_payment_type(payment_type)
