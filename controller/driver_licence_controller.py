from model.entity.driver_licence import DriverLicence
from model.service.driver_licence_service import DriverLicenceService

class DriverLicenceController:
    def __init__(self):
        self.service = DriverLicenceService()


    def save(self, person_id, serial, licence_type, city, registered_date, expired_date):
        try:
            driver_licence = DriverLicence(None, person_id, serial, licence_type, city, registered_date, expired_date)
            return True, self.service.save(driver_licence)

        except Exception as e:
            return False, f"Error! : {e}"


    def edit(self, id, person_id, serial, licence_type, city, registered_date, expired_date):
        try:
            driver_licence = DriverLicence(id, person_id, serial, licence_type, city, registered_date, expired_date)
            return True, driver_licence

        except Exception as e:
            return False, f"Error! : {e}"


    def delete(self, id):
        try:
            return True, self.service.delete(id)

        except Exception as e:
            return False, f"Error! : {e}"


    def find_by_id(self, id):
        try:
            licence_info = self.service.find_by_id(id)
            if licence_info:
                return True, licence_info
            else:
                raise ValueError("id not found")

        except Exception as e:
            return False, f"Error! : {e}"


    def find_by_serial(self, serial):
        try:
            licence_info = self.service.find_by_serial(serial)
            if licence_info:
                return True, licence_info
            else:
                raise ValueError("serial not found")

        except Exception as e:
            return False, f"Error! : {e}"


    def find_all(self):
        try:
            return True, self.service.find_all()


        except Exception as e:
            return False, f"Error! : {e}"





