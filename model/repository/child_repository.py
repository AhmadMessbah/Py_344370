from model.repository.database_manager import transaction_manager



def save(id, person_id, name, family, birth_date, is_alive, status):
    return transaction_manager(
        "insert into child (id, person_id, name, family, birth_date, is_alive, status) values (?,?,?,?,?,?,?)",
        [id, person_id, name, family, birth_date, is_alive, status],
        commit=True
    )


def edit(id, person_id, name, family, birth_date, is_alive, status):
    return transaction_manager(
        "update child set person_id=?,name=?,family=?,birth_date=?,is_alive=?,status=? where id=?",
        [person_id, name, family, birth_date, is_alive, status , id],
        commit=True
    )

def remove(person_id, name, family, birth_date, is_alive, status):
    return transaction_manager(
        "delete from childs where id=?",
        [person_id, name, family, birth_date, is_alive, status ],
        commit=True
    )

def find_all():
    return transaction_manager(
        "select * from childs"
    )

def find_by_id():
    childs_list=transaction_manager(
        "select * from childs")
    return childs_list

def find_by_person_id():
    return transaction_manager(
        "select * from childs where id = ? ",
        [id]
    )

def find_by_name_and_family():
    return transaction_manager(
        "select * from childs where name = ? ",
        [name,family]
    )
