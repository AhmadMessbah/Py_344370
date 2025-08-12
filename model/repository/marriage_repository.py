from model.repository.database_manager import transaction_manager



def save(name,family,marriage_dae,person_id,is_alive,childs):
    return transaction_manager(
        "insert into persons (name,family,marriage_dae,person_id,is_alive,childs) values (?,?,?)",
        [name,family,marriage_dae,person_id,is_alive,childs],
        commit=True
    )

def edit():
    return transaction_manager(
        insert into persons (name,family,marriage_dae,person_id,is_alive,childs)

    )

def remove():
    pass

def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass