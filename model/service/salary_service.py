from model.repository.salary_repository import SalaryRepository



class SalaryService:
    def __init__(self):
        self.repository = SalaryRepository()

    def save(self, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        if person_id is None:
            raise ValueError('person_id cannot be None')
        if weekly_hours is None:
            raise ValueError('weekly_hours cannot be None')
        #salary_repository.save(person_id, weekly_hours, pay_for_hours, end_date, employment_type)

    def edit(self,person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        if person_id is None:
            raise ValueError('person_id cannot be None')
        if weekly_hours is None:
            raise ValueError('weekly_hours cannot be None')
        # salary_repository.edit(person_id, weekly_hours, pay_for_hours, end_date, employment_type)

    def delete(self,id):
        return self.repository.delete(id)

        #salary = salary_repository.find_by_id(id)
        #if salary:
            #return salary_repository.delete(id)
        #else:
            #raise ValueError('این کد وجود ندارد')

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self,person_id):
        return self.repository.find_by_id(person_id)

    def find_by_person_id(self,person_id):
        return self.repository.find_by_person_id(person_id)

    def find_by_employment_type(self,employment_type):
        return self.repository.find_by_employment_type(employment_type)