import re

from model.entity.skill import Skill
from model.service.skill_service import SkillService


class SkillController:
    def __init__(self):
        self.service = SkillService()

    def save(self,person_id,title,institute,duration,register_date,score):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$",title) and re.match(r"^[a-zA-Z\s]{3,30}$",institute):
                skill = Skill(None,person_id,title,institute,duration,register_date,score)
                return True, "Info : Employee Saved Successfully",self.service.save(skill)
            else:
                raise ValueError("عنوان/موسسه معتبر نیست !!!")
        except Exception as e:
            return False, f"Error : {e}"

    def edit(self,id,person_id, title, institute,duration,register_date,score):
        try:
            if re.match(r"^[a-zA-Z\s]{3,30}$",title) and re.match(r"^[a-zA-Z\s]{3,30}$",institute):
                skill = Skill(id,person_id,title,institute,duration,register_date,score)
                return True, "Info : Employee Edited Successfully",self.service.edit(skill)
            else:
                raise ValueError("عنوان/موسسه معتبر نیست !!!")
        except Exception as e:
            return False, f"Error : {e}"

    def delete(self,id):
        try:
            return True, "Info : Employee Removed Successfully",self.service.delete(id)
        except Exception as e:
            return False, f"Error : {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_id(self,id):
        try:
            skill = self.service.find_by_id(id)
            if not skill:
                raise ValueError("فرد مورد نظر یافت نشد !!!")
            return True, skill
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_title_and_institute(self,title,institute):
        try:
            return True, self.service.find_by_title_and_institute(title,institute)
        except Exception as e:
            return False, f"Error : {e}"