# from model.repository.medical_repository import MedicalRepository
from model.repository import *
from model.entity.medical import Medical


class MedicalService:
    def __init__(self):
        self.repo = Repository(Medical)


    def save (self,medical):
        return self.repo.save(medical)


    def edit(self,medical):
        return self.repo.edit(medical)


    def delete(self,id):
        return self.repo.delete(id)


    def find_all(self):
        return self.repo.find_all()


    def find_by_id(self,id):
        return self.repo.find_by_id(id)


    def find_by_person_id(self,person_id):
        return self.repo.find_by_person_id(person_id)