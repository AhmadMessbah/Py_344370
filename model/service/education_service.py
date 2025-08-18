from model.repository import education_repository


def save(person_id, university, grade, average, start_date, end_date):
    if 15 >= average:
        raise ValueError("معدل زیر 15 مناسب نیست")
    return education_repository.save(person_id, university, grade, average, start_date, end_date)


def edit(id, person_id, university, grade, average, start_date, end_date):
    student = education_repository.find_by_id(id)
    if student:
        if 15 >= average:
            raise ValueError("معدل زیر 15 مناسب نیست")
        return education_repository.edit(id, person_id, university, grade, average, start_date, end_date)
    else:
        raise ValueError("کاربری با این کد پیدا نشد!!")

def delete(id):
    student = education_repository.find_by_id(id)
    if student:
        return education_repository.remove(id)
    else:
        raise ValueError("کاربری با این کد پیدا نشد!!")

def find_all():
    return education_repository.find_all()


def find_by_id(id):
    return education_repository.find_by_id(id)

def find_by_person_id(person_id):
    return education_repository.find_by_person_id(person_id)
