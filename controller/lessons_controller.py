import re
from model.service.lessons_service import save_lesson

def save(code,class_number,teacher,units,title):
    try:
        if re.match(r"^1[\d]{5}$",code):
            return save_lesson(code,class_number,teacher,units,title)
        else:
            return "error"
    except Exception as e:
        return "error{e}"

