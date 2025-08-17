import re
from model.service import education_service

def save(person_id, university, grade, average, start_date, end_date):
    if re.match(r"^[a-zA-Z\s]{3,30}$",university) :

def edit(id, person_id, university, grade, average, start_date, end_date):
    pass
def remove(id):
    pass
def find_all():
    pass
def find_by_id(id):
    pass