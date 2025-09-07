import re

from model.entity.person import Person
from model.service.person_service import PersonService
from model.tools.decorators import exception_handling


class PersonController:
    def __init__(self):
        self.service = PersonService()

    @exception_handling
    def save(self, name, family, age):
        person = Person(name, family, age)
        return self.service.save(person)

    @exception_handling
    def edit(self, id, name, family, age):
        person = Person(name, family, age)
        person.id = id
        return self.service.edit(person)

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
