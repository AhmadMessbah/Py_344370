from model.repository.database_manager import transaction_manager
from model.repository.lesson import Lesson


class LessonRepository:
  def save(self, title, code, teacher, unit, class_number):
     return transaction_manager(
        "insert into lessons (code,class_number,teacher,units,title) values(?,?,?,?,?)",
        [Lesson.person_id, Lesson.title, Lesson.code, Lesson.teacher, Lesson.unit, Lesson.class_number],
        commit=True

     )


  def edit(self,id, person_id, title, code, teacher, unit, class_number):
    return transaction_manager(
        "",
        [person_id, title, code, teacher, unit, class_number, id],
        commit=True
    )


  def delete(self,id):
    return transaction_manager(
        "delete from Lessons where id=?",
        [id]
        ,
        commit=True
    )


  def find_all(self):
    return transaction_manager(
        "select * from Lessons",
    )


  def find_by_id(self,id):
     return transaction_manager(
         "select * from Lessons where id=?",
      )


  def find_by_title(self,title):
      return transaction_manager(
         "select * from Lessons where title=?",
      )


  def find_by_teacher(self,teacher):
     return transaction_manager(
         "select * from Lessons where teacher=?",
      )

