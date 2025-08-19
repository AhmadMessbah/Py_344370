from model.repository.person_repository import PersonRepository


class PersonService:
    def __init__(self):
        self.repo = PersonRepository()

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

    def find_by_name_and_family(self, name,family):
        return self.repo.find_by_name_and_family(name,family)