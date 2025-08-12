from model.repository.database_manager import transaction_manager



def save(name,family,age):
    transaction_manager(
        "insert into persons (name,family,age) values (?,?,?)",
        [name,family,age],
        commit=True
    )

def edit():
    pass

def remove():
    pass

def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass