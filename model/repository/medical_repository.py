from model.repository.database_manager import transaction_manager



def save(person_id,disease,medicine,doctor,visit_date,status):
    return transaction_manager(
        "insert into medical (person_id,disease,medicine,doctor,visit_date,status) values (?,?,?,?,?,?)",
        [person_id,disease,medicine,doctor,visit_date,status],
        commit=True
    )

def edit():
    return transaction_manager(
        "update medical (person_id,disease,medicine,doctor,visit_date,status) values (?,?,?,?,?,?)",
        [person_id, disease, medicine, doctor, visit_date, status],
        commit=True
    )

def remove():
    pass

def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass