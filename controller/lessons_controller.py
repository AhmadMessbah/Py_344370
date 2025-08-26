import re
from model.entity.lesson import Lesson
from model.service.lessons_service  import LessonService

class LessonController:
    def __init__(self):
        self.service = LessonService()

    def save(self,  person_id, title, code, teacher, unit, class_number):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", title) and re.match(r"^[a-zA-Z\s]{3,30}$", teacher):
                Lessons = Lesson(None, id, person_id, title, code, teacher, unit, class_number)
                return True, self.service.save(Lessons)
            else:
                raise ValueError("Invalid title/teacher")
        except Exception as e:
            return False, f"Error !!! {e}"

    def edit(self, id, person_id, title, code, teacher, units, class_number):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$", title) and re.match(r"^[a-zA-Z\s]{3,30}$", teacher):
                lessons = Lesson(id, person_id, title, code, teacher, units, class_number)
                return True, self.service.edit(lessons)
            else:
                raise ValueError("Invalid title/teacher")
        except Exception as e:
            return False, f"Error !!! {e}"

    def delete(self, id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_id(self, id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"Error !!! {e}"

    def find_by_title_and_teacher(self, title, teacher):
        try:
            return True, self.service.find_by_title_and_teacher(title, teacher)
        except Exception as e:
            return False, f"Error !!! {e}"






































