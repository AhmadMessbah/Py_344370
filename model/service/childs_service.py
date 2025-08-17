from model.repository import child_repository


def save_child(id, person_id, name, family, birth_date, is_alive, status):
    if birth_date >= 1997
        raise ValueError("your child is too old")
    return child_repository.save(id, person_id, name, family, birth_date, is_alive, status)


def edit_child(id, person_id, name, family, birth_date, is_alive, status):

    child = child_repository.find_by_id()
    if birth_date:




def delet(id):
    child= child_repository.find_by_id()
    if child:
        return child.delete()
    else:
        raise ValueError("child does not exist")

def find_all():
    return child_repository.find_by_id()

def find_by_name_and_family(name, family):
    return child_repository.find_by_name_and_family(name,family)

