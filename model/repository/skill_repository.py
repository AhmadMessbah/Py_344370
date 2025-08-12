from model.repository.database_manager import transaction_manager



def save(name,family,age):
    return transaction_manager(
        "insert into skill (person_id,title,institute,duration,register_date,score) values (?,?,?,?,?,?)",
        [person_id,title,institute,duration,register_date,score],
        commit=True
    )

def edit():
    pass
    # return transaction_manager(
    #     "update skill set id=?,person_id=?,title=?,institute=?,duration=?,register_date=?,score=?",
    #     [person_id, title, institute, duration, register_date, score,id],
    #     commit=True
    # )

def remove():
    pass

def find_all():
    pass

def find_by_id():
    pass

def find_by_title_and_institute():
    pass