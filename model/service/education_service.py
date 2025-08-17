from model.repository import education_repository

def save(person_id, university, grade, average, start_date, end_date):
    if 15>=average :
        raise ValueError("معدل زیر 15 مناسب نیست")
    return education_repository.save(person_id, university, grade, start_date, end_date)

def edit(id, university, grade, average, start_date, end_date):
    student= education_repository.find_by_id(id)
    if student :
        if 15 >= average:
            raise ValueError("معدل زیر 15 مناسب نیست")
        return education_repository.edit(id, university, grade, start_date, end_date)
def delete(id):
    student= education_repository.find_by_id(id)
    if student :
        return
def find_all():
    pass
def find_by_id(id):
    pass