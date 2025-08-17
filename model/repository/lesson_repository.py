from model.repository.database_manager import transaction_manager


def save(person_id, title, code, teacher, unit, class_number):
    return transaction_manager(
        "insert into lessons(code,class_number,teacher,units,title) values(?,?,?,?,?)",
        [person_id, title, code, teacher, unit, class_number],
        commit=True

    )


def edit(id, person_id, title, code, teacher, unit, class_number):
    return transaction_manager(
        "",
        [person_id, title, code, teacher, unit, class_number, id],
        commit=True
    )


def delete(id):
    return transaction_manager(
        "",
        [id]
        ,
        commit=True
    )


def find_all():
    pass


def find_by_id(id):
    pass


def find_by_title(title):
    pass


def find_by_teacher(teacher):
    pass
