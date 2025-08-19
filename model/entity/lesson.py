from model.repository.database_manager import transaction_manager
from view.job_history_view import person_id
from view.lesson_view import*


class Lesson:
    def __init__(self, id,person_id,code,class_number,teacher,unit):
        self.id = id
        self.person_id = person_id
        self.code = code
        self.class_number = class_number
        self.teacher = teacher
        self.unit = unit

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.person_id, self.code, self.class_number, self.teacher, self.unit)

