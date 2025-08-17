import re
from model.service import education_service

def save(person_id, university, grade, average, start_date, end_date):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$",university) :
            education_service.save(person_id, university, grade, average, start_date, end_date)
            return True, "Info: User Saved Successfully"
        else:
            raise ValueError("دانشگاه مورد قبول نیست!!")
    except Exception as e:
        return False, f"Error: {e}"

def edit(id, person_id, university, grade, average, start_date, end_date):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$", university):
            education_service.edit(person_id, university, grade, average, start_date, end_date)
            return True, "Info: User Edited Successfully"
        else:
            raise ValueError("دانشگاه مورد قبول نیست!!")
    except Exception as e:
        return False, f"Error: {e}"

def delete(id):
    try:
        education_service.delete(id)
        return True, "Info: User Deleted Successfully"
    except Exception as e:
        return False, f"Error: {e}"


def find_all():
    try:
        return True, education_service.find_all()
    except Exception as e:
        return False, f"Error: {e}"

def find_by_id(id):
    try:
        user=education_service.find_by_id(id)
        if not user:
            raise ValueError("کاربر مورد نظر یافت نشد!!")
        return True, user
    except Exception as e:
        return False, f"Error: {e}"

def find_by_person_id(person_id):
    try:
        return True, education_service.find_by_person_id(person_id)
    except Exception as e:
        return False, f"Error: {e}"






