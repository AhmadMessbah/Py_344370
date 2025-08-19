from model.repository.child_repository import ChildRepository


class ChildService:
    def __init__(self):
        self.repository = ChildRepository()

    def save(self, child):
        return self.repository.save(child)

    def edit(self, child):
        return self.repository.save(child)

    def delete(self, child):
        return self.repository.delete(child)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_person_id(self, personal_id):
        return self.repository.find_by_person_id(person_id)

    def find_by_name_and_family(self, name, family):
        return self.repository.find_by_name_and_family(name, family)