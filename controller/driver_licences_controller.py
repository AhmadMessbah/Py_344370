from model.service import driver_licences_service

def save(person_id,serial,licence_type ,city,registered_date,expired_date):
    try:
        driver_licences_service.save(person_id, serial, licence_type, city, registered_date, expired_date)
        return True,"info : person saved successfully"

    except Exception as e:
        return False,f"Error:{e}"

def edit(id,person_id,licence_type ,city,registered_date,expired_date):
    try:
        person=driver_licences_service.find_by_id(id)
        if person:
            driver_licences_service.edit(person_id, licence_type, city, registered_date, expired_date, id)
            return True,"info : person edited successfully"
        else:
            raise ValueError ("person not found")

    except Exception as e:
        return False,f"Error:{e}"

def remove(id):
    try:
        person = driver_licences_service.find_by_id(id)
        driver_licences_service.remove(id)
        if person:
            return True,"info : person removed successfully"
        else:
            raise ValueError("person not found")

    except Exception as e:
        return False,f"Error:{e}"

def find_all():
    try:
        return True,driver_licences_service.find_all()

    except Exception as e:
        return False,f"Error:{e}"

def find_by_id(id):
    try:
        person = driver_licences_service.find_by_id(id)
        if person:
            return True,driver_licences_service.find_by_id(id)
        else:
            raise ValueError("person not found")

    except Exception as e:
        return False,f"Error:{e}"

def find_by_serial(serial):
    return True,driver_licences_service.find_by_serial(serial)


