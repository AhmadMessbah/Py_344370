from model.repository import medical_repository


class MedicalService:
    def __init__(self):
        self.repo = medical_repository


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


def find_by_name_and_family(self,name,family):
    return self.repo.find_by_name_and_family(name,family)