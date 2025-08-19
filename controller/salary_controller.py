import re

from model.service.salary_service import *


def save(person_id, weekly_hours, pay_for_hours, end_date, employment_type):
    try:
        if re.match(r"^[0-9]{4}$", person_id):
            salary_repository.save(person_id, weekly_hours, pay_for_hours, end_date, employment_type)
            return True, "info: saved successfully"
        else:
            raise ValueError("Invalid person id")
    except Exception as e:
        return False, "error: {e}"


def edit(id, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
    try:
        if re.match(r"^[0-9]{4}$", person_id):
            salary_repository.edit(id, person_id, weekly_hours, pay_for_hours, end_date, employment_type)
            return True, "info: edit successfully"
        else:
            raise ValueError("Invalid person id")
    except Exception as e:
        return False, "error: {e}"


def delete(id):
    try:
        salary_repository.delete(id)
        return True, "info: delete successfully"

    except Exception as e:
        return False, "error: {e}"


def find_all():
    try:
        return True, salary_repository.find_all()
    except Exception as e:
        return False, "error: {e}"


def find_by_id(person_id):
    try:
        salary = salary_repository.find_by_id()
        if not salary:
            raise ValueError("کارمندی یافت نشد")
        return True, salary_repository.find_by_id()
    except Exception as e:
        return False, "error: {e}"


def find_by_person_id(person_id):
    try:
        return True, salary_repository.find_by_person_id(person_id)
    except Exception as e:
        return False, "error: {e}"


def find_by_employment_type(employment_type):
    try:
        return True, salary_repository.find_by_employment_type(employment_type)
    except Exception as e:
        return False, "error: {e}"
