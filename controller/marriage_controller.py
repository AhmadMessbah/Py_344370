import re
from model.service.marriage_service import save_marriage

def save(person_id, name, family, marriage_date, is_alive, childes):
    print("marriage controller")
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family):
            return save_marriage(name, family)
        else:
            return "Error : Invalid Name/Family"
    except Exception as e:
        return f"Error !!! {e}"