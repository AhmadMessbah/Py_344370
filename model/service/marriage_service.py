from model.repository.marriage_repository import *


def save_marriage(person_id, name, family, marriage_date, is_alive, childes):
    print("marriage service - (marriage)")
    if is_alive:
        return save(person_id, name, family, marriage_date, is_alive, childes)
    else:
        raise Exception("error")

