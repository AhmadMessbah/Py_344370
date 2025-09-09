from model.entity.medical import Medical
from model.service.medical_service import MedicalService
from model.tools.decorators import exception_handling


class MedicalController:
    def __init__(self):
        self.service = MedicalService()


    @exception_handling
    def save(self,person_id,disease,medicine,doctor,visit_date,status):
        medical = Medical(person_id,disease,medicine,doctor,visit_date,status)
        return self.service.save(medical)


    def edit(self,id,person_id,disease,medicine,doctor,visit_date,status):
        medical = Medical(person_id,disease,medicine,doctor,visit_date,status)
        medical.id = id
        return self.service.edit(medical)



    def delete(self,id):
        return self.service.delete(id)


    def find_all(self):
        return self.service.find_all()



    def find_by_id(self,id):
        medical = self.service.find_by_id(id)
        return medical



    def find_by_person_id(self,person_id):
        pass

