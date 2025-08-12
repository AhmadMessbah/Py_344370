from model.repository.person_repository import save_to_db


def save_person(name, family, age):
    print("Person Service - (Business Logic)")
    if 20 < age < 40:
        return save_to_db(name, family, age)
    else:
        raise Exception("Age is not ok !!!")
