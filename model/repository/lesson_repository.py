from model.repository.database_manager import transaction_manager
from model.repository.database_manager import transaction_manager


class LessonRepository:
  def save(self,lesson):
     return transaction_manager(
        "insert into lessons (None,person_id,title,code,teacher,unit,class_number) values(?,?,?,?,?,?)",
        [lesson.person_id,lesson.title,lesson.code,lesson.teacher,],
        commit=True

     )


  def edit(self,id, person_id, title, code, teacher, unit, class_number):
    return transaction_manager(
        "update lessons set ",
        [person_id, title, code, teacher, unit, class_number, id],
        commit=True
    )


  def delete(self,id):
    return transaction_manager(
        "delete from lessons where id=?",
        [id]
        ,
        commit=True
    )


  def find_all(self):
    return transaction_manager(
        "select * from lessons",
    )


  def find_by_id(self,id):
     return transaction_manager(
         "select * from lessons where id=?",
      )


  def find_by_title(self,title):
      return transaction_manager(
         "select * from lessons where title=?",
      )


  def find_by_teacher(self,teacher):
     return transaction_manager(
         "select * from lessons where teacher=?",
      )

