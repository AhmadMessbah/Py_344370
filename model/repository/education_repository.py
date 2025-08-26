from model.entity.education import Education
from model.repository.database_manager import transaction_manager


class EducationRepository:
    def save(self, education):
        return transaction_manager(
            'insert into educations (person_id ,university, grade, average, start_date, end_date) values (?,?,?,?,?,?)',
            [education.person_id, education.university, education.grade, education.average, education.start_date,
             education.end_date],
            commit=True
            )

    def edit(self, education):
        return transaction_manager('update educations set person_id=?, university=?,'
                                   ' grade=?, average=?, start_date=?, end_date=? where id=?',
                                   [education.person_id, education.university, education.grade, education.average,
                                    education.start_date, education.end_date, education.id],
                                   commit=True
                                   )

    def delete(self, id):
        return transaction_manager('delete from educations where id =?',
                                   [id],
                                   commit=True
                                   )

    def find_all(self):
        education_list = transaction_manager(
            'select * from educations'
        )
        education_list = list(map(lambda education:Education(*education),education_list))
        return education_list

    def find_by_id(self, id):
        education = transaction_manager('select * from educations where id = ?', [id])
        education = Education(*education)
        return education

    def find_by_person_id(self, person_id):
        education_list = transaction_manager('select * from educations where person_id = ?', [person_id])
        education_list=list(map(lambda education:Education(*education),education_list))
        return education_list
