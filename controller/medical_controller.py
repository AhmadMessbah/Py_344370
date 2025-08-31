from model.entity.medical import Medical
from model.service.medical_service import MedicalService
import re


class MedicalController:
    def __init__(self):
        self.service = MedicalService()

    def save(self,person_id,disease,medicine,doctor,visit_date,status):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", doctor):
                medical = Medical(None, person_id, disease,medicine,doctor,visit_date,status )
                return True, self.service.save(medical)
            else:
                raise ValueError("نام دکتر معتبر نیست !!!")
        except Exception as e:
            return False, f"Error : {e}"

    def edit(self,id,person_id,disease,medicine,doctor,visit_date,status):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$",doctor) and re.match(r"^[a-zA-Z\s]{3,30}$",doctor):
               medical = Medical(id,person_id,disease,medicine,doctor,visit_date,status)
               return True, self.service.edit(medical)
            else:
                raise ValueError("نام دکتر معتبر نیست !!!")
        except Exception as e:
            return False, f"Error : {e}"

    def delete(self,id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error : {e}"

    def find_all(self):
        try:
            return self.service.find_all()
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_id(self,id):
        try:
            user = self.service.find_by_id(id)
            if not user:
                raise ValueError("کاربر مورد نظر یافت نشد!!")
            return True,user

        except Exception as e:
            return False, f"Error : {e}"

    def find_by_person_id(self,person_id):
        try:
            return True,self .service.find_by_person_id(person_id)
        except Exception as e:
            return False, f"Error: {e}"