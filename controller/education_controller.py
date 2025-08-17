import re
from model.service import education_service

def save(person_id, university, grade, average, start_date, end_date):
    if re.match(r"^[a-zA-Z\s]{3,30}$",university) :
        pass

def edit(id, person_id, university, grade, average, start_date, end_date):
    pass
def remove(id):
    pass
def find_all():
    pass
def find_by_id(id):
    pass

def find_by_person_id(person_id):
    pass