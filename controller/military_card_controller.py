import re

from model.entity.military_card import MilitaryCard
from model.service.military_card_service import MilitaryCardService


class MilitaryCardController:
    def __init__(self):
        self.service = MilitaryCardService()

    def save(self, person_id, card_serial,licence_type,city,organisation,duration):
        try:
            if re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", person_id) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",card_serial) and re.match(
                r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", licence_type) and re.match(r"^[a-zA-Z\s]{3,30}$", city) and re.match(
                r"^[a-zA-Z\s]{3,30}$", organisation) and re.match(r"^[1-9]{4}/[1-9]{2}/[1-9]{2}$", duration):
                military_card = MilitaryCard(None, person_id, card_serial, licence_type, city, organisation, duration)
                return True, self.service.save(MilitaryCard)
            else:
                raise ValueError("Invalid person_id/card_serial/licence_type/city/organisation/duration")
        except Exception as e:
            return False,f"Error !!! {e}"

    def edit(self, id,person_id, card_serial,licence_type,city,organisation,duration):
        try:
            if re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", person_id) and re.match(r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$",card_serial) and re.match(
                r"^[a-zA-Z\s]{1,10}[1-9]{1,10}$", licence_type) and re.match(r"^[a-zA-Z\s]{3,30}$", city) and re.match(
                r"^[a-zA-Z\s]{3,30}$", organisation) and re.match(r"^[1-9]{4}/[1-9]{2}/[1-9]{2}$", duration):
                military_card = MilitaryCard(None, person_id, card_serial, licence_type, city, organisation, duration)
                return True, self.service.edit(MilitaryCard)
            else:
                raise ValueError("Invalid person_id/card_serial/licence_type/city/organisation/duration")
        except Exception as e:
            return False,f"Error !!! {e}"

    def delete(self, id):
        try:
            return True,self.service.delete(id)
        except Exception as e:
            return False,f"Error !!! {e}"

    def find_all(self):
        try:
            return True,self.service.find_all()
        except Exception as e:
            return False,f"Error !!! {e}"

    def find_by_id(self, id):
        try:
            return True,self.service.find_by_id(id)
        except Exception as e:
            return False,f"Error !!! {e}"

    def find_by_card_serial(self,card_serial):
        try:
            return True,self.service.find_by_card_serial(card_serial)
        except Exception as e:
            return False,f"Error !!! {e}"
