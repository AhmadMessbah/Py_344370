from model.repository.database_manager import transaction_manager
from model.entity.skill import Skill

class SkillRepository:
    def save(self,skill):
        return transaction_manager(
            "insert into skills (person_id,title,institute,duration,register_date,score) values (?,?,?,?,?,?)",
            [skill.person_id,skill.title,skill.institute,skill.duration,skill.register_date,skill.score],
            commit=True
        )

    def edit(self,skill):
        return transaction_manager(
            "update skills set person_id=?,title=?,institute=?,duration=?,register_date=?,score=? where id=?",
            [skill.person_id, skill.title, skill.institute,skill.duration,skill.register_date,skill.score,skill.id],
             commit=True
         )

    def delete(self,id):
        return transaction_manager(
            "delete from skills where id=?",
            [id],
            commit=True
        )

    def find_all(self):
        skill_list = transaction_manager("select * from skills")
        skill_list= list(map(lambda skill: Skill(*skill), skill_list))
        return skill_list

    def find_by_id(self,id):
        skill=transaction_manager(
            "select * from skills where id=?",
        )
        skill =  Skill(*skill)
        return skill

    def find_by_title_and_institute(self,title,institute):
        skill_list=transaction_manager(
            "select * from skills where title like ? and institute like ?",
            [title+"%", institute + "%"])
        return skill_list