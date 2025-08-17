from model.repository.database_manager import transaction_manager


def save(person_id, university, grade, average, start_date, end_date):
    transaction_manager('insert into education (person_id ,university, grade, average, start_date, end_date) values (?,?,?,?,?,?)',
                        [person_id, university, grade, average, start_date, end_date],
                        commit=True)


def edit(id, person_id, university, grade, average, start_date, end_date):
    transaction_manager('update education set person_id=?, university=?,'
                        ' grade=?, average=?, start_date=?, end_date=? where id=?',
                        [person_id, university, grade, average, start_date, end_date,id],
                        commit=True)


def remove(id):
    transaction_manager('delete from education where id =?',
                        [id],
                        commit=True)

def find_all():
    education_list = transaction_manager(
        'select * from education')
    return education_list


def find_by_id(id):
    education = transaction_manager('select * from education where id = ?',[id])
    return education

def find_by_person_id(person_id):
    person = transaction_manager('select * from education where person_id = ?',[person_id])
    return person