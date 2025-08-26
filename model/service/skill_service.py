from model.repository.skill_repository import  SkillRepository

class SkillService:
    def __init__(self):
        self.repo = SkillRepository()

    def save(self, skill):
        if skill.score<=12:
            raise ValueError("نمره زیر 12 مناسب ثبت نام نیست")

        if skill.score>20:
            raise ValueError("نمره بالای 20 مناسب ثبت نام نیست")

        return self.repo.save(skill)

    def edit(self, skill):
        skill=self.repo.find_by_id(id)
        if skill:
            if skill.score<=12:
                raise ValueError("نمره زیر 12 مناسب ثبت نام نیست")

            if skill.score > 20:
                raise ValueError("نمره بالای 20 مناسب ثبت نام نیست")

            return self.repo.edit(skill)
        else:
            raise ValueError("فردی با چنین کدی پیدا نشد !!!")

    def delete(self,id):
        skill = self.repo.find_by_id(id)
        if skill:
            return self.repo.delete(id)
        else:
            raise ValueError("فردی با چنین کدی پیدا نشد !!!")

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self,id):
        return self.repo.find_by_id(id)

    def find_by_title_and_institute(self,title,institute):
        return self.repo.find_by_title_and_institute(title,institute)