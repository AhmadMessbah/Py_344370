from model.repository.database_manager import transaction_manager


def save( person_id,card_serial,licence_type,city,organisation,duration):
    return transaction_manager(
        "insert into person (person_id, card_serial,licence_type,city,organisation,duration) values (?,?,?,?,?,?)"
    [person_id,card_serial,licence_type,city,organisation,duration],
        commit=True
    )
def edit():
    return transaction_manager(

    )
def remove():
    pass
def find_all():
    pass

def find_by_id():
    pass
