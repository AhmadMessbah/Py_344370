from model.repository import marriage_repository

def save(person_id, name, family, marriage_date, is_alive, childes):
    return marriage_repository.save(person_id, name, family, marriage_date,is_alive,childes)


def edit(id, person_id, name, family, marriage_date, is_alive, childes):
    return marriage_repository.edit(id,person_id, name, family, marriage_date,is_alive,childes)


def remove(id):
    pass

def find_all():
    pass

def find_by_id(id):
    pass

def find_by_name_and_family(family,name):
    pass
