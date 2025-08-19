from model.repository import education_repository

class EducationService:

    def __init__(self):
        self.repo = education_repository

    def save(self,education):
        return self.repo.save(education)

    def edit(self,education):
        return self.repo.edit(education)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_person_id(self,person_id):
        return self.repo.find_by_person_id(person_id)
