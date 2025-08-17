from model.repository.military_card_repository import *
def save_military(person_id, card_serial, licence_type, city, organisation, duration):
    print("military service -(military)")
    if duration:
        return save_military(person_id, card_serial, licence_type, city, organisation, duration)
    else:
        raise Exception("ERROR")