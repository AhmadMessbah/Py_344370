from model.repository import medical_repository

def save (person_id,disease,medicine,doctor,visit_date,status):
    if status == "bad" :
        raise ValueError("حالتون مساعد نیست")
    return medical_repository.save(person_id, disease, medicine, doctor, visit_date, status)

def edit():
    pass

def delete():
    pass

def find_all():
    pass

def find_by_id():
    pass

def find_by_name_and_family():
    pass