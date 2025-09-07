from model.repository import *
from model.entity.person import Person



class PersonService:
    def __init__(self):
        self.repo = Repository(Person)

    def save(self, person):
        return self.repo.save(person)

    def edit(self, person):
        return self.repo.edit(person)

    def delete(self, id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    def find_by_family(self,family):
        return self.repo.find_by(Person.family.like(family+"%"))

    def find_by_name_and_family(self, name, family):
        return self.repo.find_by(and_(Person.name.like(name+"%"), Person.family.like(family+"%")))
