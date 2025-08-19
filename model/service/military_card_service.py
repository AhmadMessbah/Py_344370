from model.repository import military_card_repository


def save(person_id, card_serial, licence_type, city, organisation, duration):
    if duration < 2:
        raise ValueError(" under 2 years duration")
    return military_card_repository.save(person_id, card_serial, licence_type, city, organisation, duration)


def edit(id, person_id, card_serial, licence_type, city, organisation, duration):
    military_card = military_card_repository.find_by_id(id)
    if military_card:
        if duration < 2:
            raise ValueError(" under 2 years duration")
        return military_card_repository.save(person_id, card_serial, licence_type, city, organisation, duration)

    else:
        raise ValueError("military  with this id not found")


def remove(id):
    military_card = military_card_repository.find_by_id(id)
    if military_card:
        return military_card_repository.remove(id)
    else:
        raise ValueError("military  with this id not found")


def find_all():
    return military_card_repository.find_all()


def find_by_id():
    return military_card_repository.find_by_id(id)


def find_by_card_serial(card_serial):
    return military_card_repository.find_by_card_serial(card_serial)
