import re

from model.service import skill_service

def save(person_id,title,institute,duration,register_date,score):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$",title) and re.match(r"^[a-zA-Z\s]{3,30}$",institute):
            skill_service.save(person_id,title,institute,duration,register_date,score)
            return True, "Info : Employee Saved Successfully"
        else:
            raise ValueError("عنوان/موسسه معتبر نیست !!!")
    except Exception as e:
        return False, f"Error : {e}"

def edit(id,person_id, title, institute,duration,register_date,score):
    try:
        if re.match(r"^[a-zA-Z\s]{3,30}$",title) and re.match(r"^[a-zA-Z\s]{3,30}$",institute):
            skill_service.edit(id,person_id,title,institute,duration,register_date,score)
            return True, "Info : Employee Edited Successfully"
        else:
            raise ValueError("عنوان/موسسه معتبر نیست !!!")
    except Exception as e:
        return False, f"Error : {e}"

def remove(id):
    try:
        skill_service.remove(id)
        return True, "Info : Employee Removed Successfully"
    except Exception as e:
        return False, f"Error : {e}"

def find_all():
    try:
        return True, skill_service.find_all()
    except Exception as e:
        return False, f"Error : {e}"

def find_by_id(id):
    try:
        skill = skill_service.find_by_id(id)
        if not skill:
            raise ValueError("فرد مورد نظر یافت نشد !!!")
        return True, skill
    except Exception as e:
        return False, f"Error : {e}"

def find_by_title_and_institute(title,institute):
    try:
        return True, skill_service.find_by_title_and_institute(title,institute)
    except Exception as e:
        return False, f"Error : {e}"