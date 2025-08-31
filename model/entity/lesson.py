class Lesson:
    def __init__(self,id, person_id, title, code, teacher, unit, class_number):
        self.id = id
        self.person_id = person_id
        self.title = title
        self.code = code
        self.teacher = teacher
        self.unit = unit
        self.class_number = class_number
    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.title, self.code, self.teacher, self.unit, self.class_number))