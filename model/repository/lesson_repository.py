from model.entity.lesson import Lesson
from model.repository.database_manager import transaction_manager

class LessonRepository:
    def save(self, lesson):
        return transaction_manager(
            "insert into lessons ( person_id,title, code, teacher, unit, class_number) values (?,?,?,?,?)",
            [lesson.person_id,lesson.title, lesson.code, lesson.teacher, lesson.unit,lesson.class_number],
            commit=True



        )
    def edit(self, lesson):
        return transaction_manager(
            "update lessons set  person_id=? ,title=? , code=? , teacher=? , unit=? , class_number=? where id=?",
            [lesson.person_id,lesson.title, lesson.code, lesson.teacher, lesson.unit,lesson.class_number],
            commit=True



        )
    def delete(self,id):
        return transaction_manager(
            "delete from lessons where id=?",
            [id],
            commit=True
        )
    def find_all(self,id):
        lesson_list= transaction_manager(
            "select * from lessons",


        )
        lesson_list=list(map(lambda lesson:Lesson(*lesson),lesson_list))
        return lesson_list


    def find_by_id(self,id):
        lesson=transaction_manager(
            "select * from lessons where id=?",
            [id]

        )
        lesson= Lesson(*lesson)
        return lesson

    def find_by_title_and_teacher(self,title,teacher):
        lesson_list=transaction_manager(
            "select * from lessons where title like ? and teacher like ?",
            [title+"%",teacher+"%"],


        )
        lesson_list=list(map(lambda lesson:Lesson(*lesson),lesson_list))
        return lesson_list
