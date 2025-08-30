from model.repository.medical_repository import MedicalRepository


class MedicalService:
    def __init__(self):
        self.repo = MedicalRepository


    def save (self,medical):
        return self.repo.save(medical)


    def edit(self,medical):
        return self.repo.edit(medical)


    def remove(self,id):
        return self.repo.remove(id)


    def find_all(self):
        return self.repo.find_all()


    def find_by_id(self,id):
        return self.repo.find_by_id(id)


    def find_by_person_id(self,person_id):
        return self.repo.find_by_person_id(person_id)