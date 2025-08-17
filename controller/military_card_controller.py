import re

from model.service.military_card_service import save_military
def save_military(person_id, card_serial, licence_type, city, organisation, duration):
    print("military_card controller")
    try:
        if re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",person_id) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",card_serial) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",licence_type) and re.match(r"^[a-zA-Z\s]{3,30}$",city) and re.match(r"^[a-zA-Z\s]{3,30}$",organisation) and re.match(r"^[1-9]{4}/[1-9]{2}/[1-9]{2}$",duration):
            return save_military(person_id, card_serial, licence_type, city, organisation, duration)
        else:
            return "Error : Invalid"
    except Exception as e:
        return f"Error!!!{e}"