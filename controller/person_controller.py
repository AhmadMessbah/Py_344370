import re

from model.entity.person import Person
from model.service.person_service import PersonService


class PersonController:
    def __init__(self):
        self.service = PersonService()

    def save(self, name, family, age):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family):
                person = Person( name, family, age)
                return True, self.service.save(person)
            else:
                raise ValueError("Invalid Name/Family")
        except Exception as e:
            return False, f"Error !!! {e}"

    def edit(self, id, name, family, age):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$", family):
                person = Person(name, family, age)
                person.id = id
                return True, self.service.edit(person)
            else:
                raise ValueError("Invalid Name/Family")
        except Exception as e:
            return False, f"Error !!! {e}"

    def delete(self, id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_id(self, id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_name_and_family(self, name, family):
        try:
            return True, self.service.find_by_name_and_family(name, family)
        except Exception as e:
            return False, f"Error !!! {e}"
