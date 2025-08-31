from model.entity.driver_licence import DriverLicence
from model.service import driver_licence_service
from model.service.driver_licence_service import DriverLicenceService

class DriverLicenceController:
    def __init__(self):
        self.driver_licence_service = DriverLicenceService()


    def save(self, person_id, serial, licence_type, city, registered_date, expired_date):
        try:
            driver_licence = DriverLicence(None, person_id, serial, licence_type, city, registered_date, expired_date)
            return True, self.driver_licence_service.save(driver_licence)

        except Exception as e:
            return False, f"Error! : {e}"


    def edit(self, id, person_id, serial, licence_type, city, registered_date, expired_date):
        try:
            driver_licence = DriverLicence(id, person_id, serial, licence_type, city, registered_date, expired_date)
            return True, self.driver_licence_service.edit(driver_licence)

        except Exception as e:
            return False, f"Error! : {e}"


    def delete(self, id):
        try:
            return True, self.driver_licence_service.delete(id)

        except Exception as e:
            return False, f"Error! : {e}"


    def find_by_id(self, id):
        try:
            #licence_info = self.driver_licence_service.find_by_id(id)
            #if licence_info:
                return True, self.driver_licence_service.find_by_id(id)
            #else:
                #raise ValueError("id not found")

        except Exception as e:
            return False, f"Error! : {e}"


    def find_by_serial(self, serial):
        try:
            #licence_info = self.driver_licence_service.find_by_serial(serial)
            #if licence_info:
                return True, self.driver_licence_service.find_by_serial(serial)
            #else:
                #raise ValueError("serial not found")

        except Exception as e:
            return False, f"Error! : {e}"


    def find_all(self):
        try:
            return True, self.driver_licence_service.find_all()


        except Exception as e:
            return False, f"Error! : {e}"





