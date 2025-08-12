import re

from model.service.person_service import save_person


def save(name, family, age):
    print("Person Controller - (exception handling/validation/request...response)")
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family):
            return save_person(name, family, age)
        else:
            return "Error : Invalid Name/Family"
    except Exception as e:
        return f"Error !!! {e}"
