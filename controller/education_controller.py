from model.entity.education import Education
from model.service.education_service import EducationService
from model.tools.decorators import exception_handling


class EducationController:

    def __init__(self):
        self.service = EducationService()

    @exception_handling
    def save(self, person_id, university, grade, average, start_date, end_date):
        education = Education(None, person_id, university, grade, average, start_date, end_date)
        return self.service.save(education)

    @exception_handling
    def edit(self, id, person_id, university, grade, average, start_date, end_date):
        education = Education(id, person_id, university, grade, average, start_date, end_date)
        return self.service.edit(education)

    @exception_handling
    def delete(self, id):
        return self.service.delete(id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self, id):
        user = self.service.find_by_person_id(id)
        return user

    @exception_handling
    def find_by_person_id(self, person_id):
        return self.service.find_by_person_id(person_id)
