from model.repository import salary_repository

def save(person_id, weekly_hours, pay_for_hours, end_date, employment_type):
    if person_id is None:
        raise ValueError('person_id cannot be None')
    if weekly_hours is None:
        raise ValueError('weekly_hours cannot be None')
    salary_repository.save(person_id, weekly_hours, pay_for_hours,end_date, employment_type)


def edit(person_id, weekly_hours, pay_for_hours, end_date, employment_type):
    if person_id is None:
        raise ValueError('person_id cannot be None')
    if weekly_hours is None:
        raise ValueError('weekly_hours cannot be None')
    salary_repository.edit(person_id, weekly_hours, pay_for_hours, end_date, employment_type)


def delete(id):
    salary= salary_repository.find_by_id(id)
    if salary:
        return salary_repository.delete(id)
    else:
        raise ValueError('این کد وجود ندارد')

def find_all():
    return salary_repository.find_all()

def find_by_id(person_id):
    return salary_repository.find_by_id(person_id)

def find_by_person_id(person_id):
    return salary_repository.find_by_person_id(person_id)

def find_by_employment_type(employment_type):
    return salary_repository.find_by_employment_type(employment_type)
