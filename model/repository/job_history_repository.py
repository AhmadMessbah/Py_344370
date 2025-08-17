from model.repository.database_manager import transaction_manager




def save(person_id, organisation, job_title, start_date, end_date, description):
    return transaction_manager(
        "insert into jobs(person_id, organisation, job_title, start_date, end_date, description) "
        "values(?,?,?,?,?,?)",
        [person_id, organisation, job_title, start_date, end_date, description],
        commit=True
    )

def edit(id, person_id, organisation, job_title, start_date, end_date, description):
    return transaction_manager(
        "update jobs set person_id=?, organisation=?, job_title=?, start_date=?, end_date=?, description=? where id=?",
        [person_id, organisation, job_title, start_date, end_date, description, id],
        commit=True
    )

def remove(id):
    return transaction_manager(
        "delete from jobs where id=?",
        [id],
        commit=True
    )

def find_all():
    return transaction_manager(
        "select * from jobs"
    )

def find_by_id(id):
    pass

def find_by_title(title):
    pass
