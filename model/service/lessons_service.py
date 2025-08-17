from model.repository import lesson_repository


def save(person_id, title, code, teacher, unit, class_number):
    lesson_repository.save(person_id, title, code, teacher, unit, class_number)


def edit(id, person_id, title, code, teacher, unit, class_number):
    return lesson_repository.edit(id, person_id, title, code, teacher, unit, class_number)


def delete(id):
    return lesson_repository.delete(id)


def find_by_all():
    return lesson_repository.find_all()


def find_by_id(id):
    return lesson_repository.find_by_id(id)


def find_by_title(title):
    return lesson_repository.find_by_title(title)

def find_by_teacher(teacher):
    return lesson_repository.find_by_teacher(teacher)