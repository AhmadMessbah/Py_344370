import re

from model.entity.salary import Salary
from model.service.salary_service import SalaryService


class SalaryController:
    def __init__(self):
        self.salary_service = SalaryService()

    def save(self, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        try:
            if re.match(r"^[0-9]{4}$", str(person_id)):
                salary = Salary(None, person_id, weekly_hours, pay_for_hours, end_date, employment_type)

                self.salary_service.save(salary)
                return True, "info: saved successfully"
            else:
                raise ValueError("Invalid person id")
        except Exception as e:
            return False, f"error: {e}"

    def edit(self, id, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        try:
            if re.match(r"^[0-9]{4}$", str(person_id)):
                salary = Salary(id, person_id, weekly_hours, pay_for_hours, end_date, employment_type)
                self.salary_service.edit(salary)
                return True, "info: edit successfully"
            else:
                raise ValueError("Invalid person id")
        except Exception as e:
            e.with_traceback()
            return False, f"error: {e}"

    def delete(self, id):
        try:
            self.salary_service.delete(id)
            return True, "info: delete successfully"
        except Exception as e:
            return False, f"error: {e}"

    def find_all(self):
        try:
            return True, self.salary_service.find_all()
        except Exception as e:
            return False, f"error: {e}"

    def find_by_id(self, id):
        try:
            salary = self.salary_service.find_by_id(id)
            if not salary:
                raise ValueError("کارمندی یافت نشد")
            return True, salary
        except Exception as e:
            return False, f"error: {e}"

    def find_by_person_id(self, person_id):
        try:
            return True, self.salary_service.find_by_person_id(person_id)
        except Exception as e:
            return False, f"error: {e}"

    def find_by_employment_type(self, employment_type):
        try:
            return True, self.salary_service.find_by_employment_type(employment_type)
        except Exception as e:
            return False, f"error: {e}"
