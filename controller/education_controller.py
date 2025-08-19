import re

from model.entity.education import Education
from model.service.education_service import EducationService

class EducationController:

    def __init__(self):
        self.service = EducationService()


    def save(self,person_id, university, grade, average, start_date, end_date):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", university):
                education=Education(person_id, university, grade, average, start_date, end_date)
                return True, self.service.save(education)
            else:
                raise ValueError("دانشگاه مورد قبول نیست!!")
        except Exception as e:
            return False, f"Error: {e}"


    def edit(self,id, person_id, university, grade, average, start_date, end_date):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", university):
                education = Education(id,person_id, university, grade, average, start_date, end_date)
                return True, self.service.edit(education)
            else:
                raise ValueError("دانشگاه مورد قبول نیست!!")
        except Exception as e:
            return False, f"Error: {e}"


    def delete(self,id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error: {e}"


    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error: {e}"


    def find_by_id(self,id):
        try:
            user = self.find_by_person_id(id)
            if not user:
                raise ValueError("کاربر مورد نظر یافت نشد!!")
            return True, user
        except Exception as e:
            return False, f"Error: {e}"


    def find_by_person_id(self,person_id):
        try:
            return True, self.find_by_person_id(person_id)
        except Exception as e:
            return False, f"Error: {e}"
