from model.entity.skill import Skill
from model.service.skill_service import SkillService
from model.tools.decorators import exception_handling


class SkillController:
    def __init__(self):
        self.service = SkillService()

    @exception_handling
    def save(self,person_id,title,institute,duration,register_date,score):
        skill = Skill(None,person_id,title,institute,duration,register_date,score)
        return self.service.save(skill)

    @exception_handling
    def edit(self,id,person_id, title, institute,duration,register_date,score):
        skill = Skill(id,person_id,title,institute,duration,register_date,score)
        return self.service.edit(skill)

    @exception_handling
    def delete(self,id):
        return self.service.delete(id)

    @exception_handling
    def find_all(self):
        return self.service.find_all()

    @exception_handling
    def find_by_id(self,id):
        skill = self.service.find_by_id(id)
        return skill

    @exception_handling
    def find_by_title_and_institute(self,title,institute):
        return self.service.find_by_title_and_institute(title,institute)