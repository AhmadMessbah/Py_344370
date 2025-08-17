from model.service import lessons_service
import re



def save(person_id, title, code, teacher, unit, class_number):
    try:
        if re.match(r"^1[\d]{5}$",code):
            return lessons_service.save(person_id,class_number,teacher,unit,title)
        else:
            return "error "
    except Exception as e:
        return False, f"error {e}"


def edit(id, person_id, title, code, teacher, unit, class_number):
    try:
        if re.match(r"^[\d]{5}$]"):
            return lessons_service.edit(id,person_id,title,code,teacher,unit,class_number)
        else:
            return "error"
    except Exception as e:
        return "errorEdit"


def delete(id):
    try:
        lessons_service.delete(id)
        return True,"Info: lesson deleted"
    except Exception as e:
        return False,f"error{e}"


def find_by_id(id):
    try:
        lesson=lessons_service.find_by_id(id)
        if not lesson:
            raise ValueError(f"lesson not found{id}")
        return True,lesson
    except Exception as e:
        return False,f"error{e}"



def find_by_all():
    try:
        return lessons_service.find_all()
    except Exception as e:
        return False,f"error{e}"



def find_by_title(title):
    try:
        return lessons_service.find_by_title(title)
    except Exception as e:
        return False,f"error{e}"


def find_by_teacher(teacher):
    try:
        return lessons_service.find_by_teacher(teacher)
    except Exception as e:
        return False,f"error{e}"
