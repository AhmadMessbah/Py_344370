from model.service import payment_service
import re


def save(person_id, title, amount, pay_date, payment_type, description):
    try:
        if re.match(r"^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$", pay_date):
            payment_service.save(person_id, title, amount, pay_date, payment_type, description)
            return True, "Info : Payment Saved Successfully"
        else:
            raise ValueError("Invalid Date !!!")
    except Exception as e:
        return False, f"Error : {e}"


def edit(id, person_id, title, amount, pay_date, payment_type, description):
    try:
        if re.match(r"^(?:19|20)\d\d-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$", pay_date):
            payment_service.edit(id, person_id, title, amount, pay_date, payment_type, description)
            return True, "Info : Payment Saved Successfully"
        else:
            raise ValueError("Invalid Date !!!")
    except Exception as e:
        return False, f"Error: {e}"


def remove(id):
    try:
        payment_service.remove(id)
        return True, "Info: User Removed Successfully"
    except Exception as e:
        return False, f"Error: {e}"


def find_all():
    try:
        return True, payment_service.find_all()
    except Exception as e:
        return False, f"Error: {e}"


def find_by_id(id):
    try:
        pay = payment_service.find_by_id(id)
        if not pay:
            raise ValueError("Payment Not Found !!!")
        return True, pay
    except Exception as e:
        return False, f"Error: {e}"


def find_by_payment_type(payment_type):
    try:
        return True, payment_service.find_by_payment_type(payment_type)
    except Exception as e:
        return False, f"Error: {e}"
