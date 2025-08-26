from model.repository.lesson_repository import LessonRepository

class LessonService:
    def __init__(self):
        self.repo= LessonService





    def save(self,person_id, title, code, teacher, unit, class_number):
        return self.repo.save(person_id, title, code, teacher, unit, class_number)


    def edit(self,id, person_id, title, code, teacher, unit, class_number):
         return  self.repo.edit(id, person_id, title, code, teacher, unit, class_number)


    def delete(self,id):
        return self.repo.delete(id)


    def find_by_all(self):
         return self.repo.find_all()


    def find_by_id(self,id):
        return self.repo.find_by_id(id)


    def find_by_title(self,title):
         return self.repo.find_by_title(title)

    def find_by_teacher(self,teacher):
        return self.repo.find_by_teacher(teacher)