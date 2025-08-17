import re

from model.service import military_card_service


def save(person_id, card_serial, licence_type, city, organisation, duration):
    try:
        if re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",person_id) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",card_serial) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",licence_type) and re.match(r"^[a-zA-Z\s]{3,30}$",city) and re.match(r"^[a-zA-Z\s]{3,30}$",organisation) and re.match(r"^[1-9]{4}/[1-9]{2}/[1-9]{2}$",duration):
            military_card_service.save(person_id, card_serial, licence_type, city, organisation, duration)
            return True, "Info:military card saved successfully"
        else:
            raise ValueError("Error : Invalid")
    except Exception as e:
        return False, f"Error!!!{e}"


def edit(id, person_id, card_serial, licence_type, city, organisation, duration):
    try:
        if re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", person_id) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",
                                                                              card_serial) and re.match(
                r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", licence_type) and re.match(r"^[a-zA-Z\s]{3,30}$", city) and re.match(
                r"^[a-zA-Z\s]{3,30}$", organisation) and re.match(r"^[1-9]{4}/[1-9]{2}/[1-9]{2}$", duration):
            military_card_service.edit(id, person_id, card_serial, licence_type, city, organisation, duration)
            return True, "Info:military card edited successfully"
        else:
            raise ValueError("Error : Invalid")
    except Exception as e:
        return False, f"Error!!!{e}"


def remove(id):
    try:
        military_card_service.remove(id)
        return True, "Info:military card removed successfully"
    except Exception as e:
        return False, f"Error{e}"


def find_all():
    try:
        return True, military_card_service.find_all()
    except Exception as e:
        return False, f"Error:{e}"


def find_by_id(id):
    try:
        military_card = military_card_service.find_by_id(id)
        if not military_card:
            raise ValueError("military card not found")
        return True, military_card
    except Exception as e:
        return False, f"Error{e}"


def find_by_card_serial(card_serial):
    try:
        return True, military_card_service.find_by_card_serial(card_serial)
    except Exception as e:
        return False, f"Error{e}"
