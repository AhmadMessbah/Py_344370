from model.repository import driver_licences_repository

def save(person_id,serial,licence_type ,city,registered_date,expired_date):
    return driver_licences_repository.save(
        person_id,serial,licence_type,city,registered_date,expired_date )

def edit(id,person_id,serial,licence_type,city,registered_date,expired_date):
    person = driver_licences_repository.find_by_id(id)
    if person:
        return driver_licences_repository.edit(
               person_id,serial,licence_type,city,registered_date,expired_date,id )
    else:
        raise ValueError("Person not foud")

def remove(id):
    person = driver_licences_repository.find_by_id(id)
    if person:
        return driver_licences_repository.remove(id)
    else:
        raise ValueError("Person not foud")

def find_all():
    return driver_licences_repository.find_all()

def find_by_id(id):
    return driver_licences_repository.find_by_id(id)

def find_by_serial(serial):
    return driver_licences_repository.find_by_serial(serial)


