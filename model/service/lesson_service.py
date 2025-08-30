from model.repository.lesson_repository import LessonRepository

class LessonService:
    def __init__(self):
        self.repo=LessonRepository()

    def save(self,lesson):
        return self.repo.save(lesson)

    def edit(self,lesson):
        return self.repo.edit(lesson)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_title_and_teacher(self,title,teacher):
        return self.repo.find_by_title_and_teacher(title,teacher)