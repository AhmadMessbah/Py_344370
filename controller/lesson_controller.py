import re

from model.entity.lesson import Lesson
from model.service.lesson_service import LessonService

class LessonController:
    def __init__(self):
        self.lesson=LessonService()

    def save(self,person_id, title, code, teacher, unit, class_number):
        try:
            if re.match("^[a-zA-Z]+$",title) and re.match("^[a-zA-Z]+$",teacher):
                lesson=Lesson(None,person_id,title,code,teacher,unit,class_number)
                return True, self.lesson.save(lesson)
            else:
                raise ValueError("Invalid title or teacher")
        except Exception as e:
            return False, f"Failed to save lesson: {e}"

    def edit(self,id,person_id,title,code,teacher,unit,class_number):
        try:
            if re.match ("^[a-zA-Z]+$",title) and re.match("^[a-zA-Z]+$",teacher):
                lesson=Lesson(id,person_id,title,code,teacher,unit,class_number)
                return True, self.lesson.edit(lesson)
            else:
                raise ValueError("Invalid title or teacher")
        except Exception as e:
            return False, f"Failed to edit lesson: {e}"

    def delete(self,id):
        try:
            return True,self.service.delete(id)
        except Exception as e:
            return False, f"Failed to delete lesson: {e}"

    def find_all(self,):
        try:
            return True, self.sevice.find_all()
        except Exception as e:
            return False, f"Failed to find lesson: {e}"
    def find_by_id(self,id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"Failed to find lesson: {e}"

    def find_by_title_and_teacher(self,title,teacher):
        try:
            return True,self.service.find_by_title_and_teacher(title,teacher)
        except Exception as e:
            return False, f"Failed to find lesson: {e}"









