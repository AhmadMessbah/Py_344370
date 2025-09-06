from model.repository.skill_repository import  SkillRepository

class SkillService:
    def __init__(self):
        self.repo = SkillRepository()

    def save(self, skill):
        return self.repo.save(skill)

    def edit(self, skill):
        return self.repo.edit(skill)

    def delete(self,id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_title_and_institute(self,title,institute):
        return self.repo.find_by_title_and_institute(title,institute)