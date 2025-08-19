from model.repository import medical_repository

def save (person_id,disease,medicine,doctor,visit_date,status):
    if status == "bad" :
        raise ValueError("حالتون مساعد نیست")
    return medical_repository.save(person_id, disease, medicine, doctor, visit_date, status)

def edit():
    medical = medical_repository.find_by_id(id)
    if medical:
        if status == "khob":
            raise ValueError("درمان بیماری")

        return medical_repository.edit(id, person_id, disease, medicine, doctor, visit_date,status)
    else:
        raise ValueError("درمان کامل نیست")

def delete(id):
    medical = medical_repository.find_by_id(id)
    if medical:
        return medical_repository.remove(id)
    else:
        raise ValueError("فردی با چنین کدی پیدا نشد !!!")

def find_all():
    return medical_repository.find_all()

def find_by_id():
    return medical_repository.find_by_id(id)

def find_by_name_and_family():
    pass