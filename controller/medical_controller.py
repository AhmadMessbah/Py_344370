from model.service import medical_service
import re

def save(person_id,disease,medicine,doctor,visit_date,status):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$", doctor):
            medical_service.save(person_id, disease, medicine, doctor, visit_date,status)
            return True, "Info : Student Saved Successfully"
        else:
            raise ValueError("نام دکتر معتبر نیست !!!")
    except Exception as e:
        return False, f"Error : {e}"

def edit(id,person_id,disease,medicine,doctor,visit_date,status):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$",doctor) and re.match(r"^[a-zA-Z\s]{3,30}$",doctor):
            medical_service.edit(id,person_id,disease,medicine,doctor,visit_date,status)
            return True, "Info : Edited Successfully"
        else:
            raise ValueError("نام دکتر معتبر نیست !!!")
    except Exception as e:
        return False, f"Error : {e}"

def delete(id):
    try:
        medical_service.delete(id)
        return True, "Info :  Removed Successfully"
    except Exception as e:
        return False, f"Error : {e}"

def find_all():
    try:
        return True, medical_service.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def find_by_id(id):
    try:
        person = medical_service.find_by_id(id)
        if not person:
            raise ValueError("فرد مورد نظر یافت نشد !!!")
        return True, person
    except Exception as e:
        return False, f"Error : {e}"

def find_by_name_and_family():
    pass