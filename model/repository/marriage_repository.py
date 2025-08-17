from model.repository.database_manager import  transaction_manager


def save(person_id, name, family, marriage_date, is_alive, childes):
    return transaction_manager(
        "insert into marriages (person_id, name, family, marriage_date, is_alive, childes) values (?,?,?,?,?,?)",
        [person_id, name, family, marriage_date, is_alive, childes],
        commit=True
    )


def edit(id, person_id, name, family, marriage_date, is_alive, childes):
    return transaction_manager(
        "UPDATE marriages SET NAME=?,FAMILY=?,MARRIAGE_DATE=?,IS_ALIVE=?, childes=? WHERE ID=?",
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
    return transaction_manager(
        "SELECT * FROM marriages WHERE ID=?",
        [id]
    )

def find_by_id(id):
    return transaction_manager(
        "SELECT * FROM marriages WHERE ID=?",
        [id]
    )

def find_by_name_and_family(family,name):
    return transaction_manager(
        "SELECT * FROM marriages WHERE NAME=? AND FAMILY=?",
        [family + "%"]
    )
