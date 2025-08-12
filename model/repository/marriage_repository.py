from model.repository.database_manager import transaction_manager


def save(person_id, name, family, marriage_date, is_alive, childes):
    return transaction_manager(
        "insert into marriages (person_id, name, family, marriage_date, is_alive, childs) values (?,?,?,?,?,?)",
        [person_id, name, family, marriage_date, is_alive, childes],
        commit=True
    )


def edit(id, person_id, name, family, marriage_date, is_alive, childes):
    return transaction_manager(
        "",
        [person_id, name, family, marriage_date, is_alive, childes, id],
        commit=True
    )


def remove(id):
    return transaction_manager(
        "",
        [id],
        commit=True
    )

def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass
