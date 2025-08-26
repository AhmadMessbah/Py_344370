from model.repository.marriage_repository import MarriageRepository


class MarriageService:
    def __init__(self):
        self.repo = MarriageRepository()

    def save(self, marriage):
        return self.repo.save(marriage)

    def edit(self, marriage):
        return self.repo.edit(marriage)

    def delete(self, id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    def find_by_name_and_family(self,name,family):
        return self.repo.find_by_name_and_family(name,family)
