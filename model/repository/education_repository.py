from model.entity.education import Education
from model.repository.database_manager import transaction_manager


class EducationRepository:
    def save(self, education):
        transaction_manager(
            'insert into educations (person_id ,university, grade, average, start_date, end_date) values (?,?,?,?,?,?)',
            [education.person_id, education.university, education.grade, education.average, education.start_date,
             education.end_date],
            commit=True
            )
        return education

    def edit(self, education):
        transaction_manager(
            'update educations set person_id=?, university=?, grade=?, average=?, start_date=?, end_date=? where id=?',
            [education.person_id, education.university, education.grade, education.average,
            education.start_date, education.end_date, education.id],
            commit=True
            )
        return education

    def delete(self, id):
        transaction_manager(
            'delete from educations where id =?',
            [id],
            commit=True
            )
        return id

    def find_all(self):
        education_list = transaction_manager(
            'select * from educations'
        )
        if education_list:
            education_list = list(map(lambda education:Education(*education),education_list))
            return education_list

    def find_by_id(self, id):
        education = transaction_manager('select * from educations where id = ?', [id + "%"])
        if education:
            education = Education(*education[0])
            return education

    def find_by_person_id(self, person_id):
        education_list = transaction_manager('select * from educations where person_id = ?', [person_id + "%"])
        if education_list:
            education_list=list(map(lambda education:Education(*education),education_list))
            return education_list
