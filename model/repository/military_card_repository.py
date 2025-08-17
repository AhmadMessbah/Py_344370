from model.repository.database_manager import transaction_manager


def save(person_id, card_serial, licence_type, city, organisation, duration):
    return transaction_manager(
        "insert into military_cards (person_id, card_serial,licence_type,city,organisation,duration) values (?,?,?,?,?,?)",
        [person_id, card_serial, licence_type, city, organisation, duration],
        commit=True
    )


def edit(id, person_id, card_serial, licence_type, city, organisation, duration):
    return transaction_manager("update military_cards set person_id=?, card_serial=?, licence_type=?, city=?, organisation=?, duration=? where id=?",
                               [person_id, card_serial, licence_type, city, organisation, duration, id],
                               commit=True
                               )


def remove(id):
    return transaction_manager("delete from military_cards where id=?", [id], commit=True)


def find_all():
    military_cards = transaction_manager("select * from military_cards")
    return military_cards


def find_by_id(id):
    person_id=transaction_manager("select * from military_cards where id=?", [id], commit=True)
    return person_id

def find_by_card_serial(card_serial):
    military_cards = transaction_manager("select * from military_cards where card_serial=?", [card_serial], commit=True)
    return military_cards
