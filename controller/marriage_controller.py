import re
from model.service.marriage_service import save_marriage
from model.repository.database_manager import *

def save(person_id, name, family, marriage_date, is_alive, childes):
    print("marriage controller")
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family):
            return save_marriage(name, family)
        else:
            return "Error : Invalid Name/Family"
    except Exception as e:
        return f"Error !!! {e}"

def edit( person_id, name, family, marriage_date, is_alive, childes):
    return transaction_manager(
        "UPDATE marriages  SET (person_id,name,family,marriage_date,IS_ALIVE)=? WHERE ID=?",
        [person_id, name, family, marriage_date, is_alive, childes, id],
        commit=True
    )

def remove(id):
    return transaction_manager(
        "",
        [id],
        commit=True
    )

def find_all():
    return transaction_manager(
        "SELECT * FROM marriages WHERE ID=?",
        [id]
    )

def find_by_id(id):
    return transaction_manager(
        "SELECT * FROM marriages WHERE ID=?",
        [id]
    )

def find_by_name_and_family(family,name):
    return transaction_manager(
        "SELECT * FROM marriages WHERE NAME=? AND FAMILY=?",
        [family + "%"]
    )
