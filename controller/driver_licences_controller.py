from model.service.driver_licences_service import *
import re


class DriverLicencesController:
    def __init__(self):
        self.service = DriverLicencesService()

    def save(self, person_id, serial, license_type, city, register_date, expire_date):
        try:
            if re.match(r"^[a-z\s]{3,30}$", city, re.I):
                driver_licence = DriverLicence(None, person_id, serial, license_type, city, register_date, expire_date)
                return True, self.service.save(driver_licence)
            else:
                raise ValueError("letters not correct for city")

        except Exception as e:
            return False, f"Error!!:{e}"

    def edit(self, id, person_id, serial, license_type, city, register_date, expire_date):
        try:
            if re.match(r"^[a-z\s]{3,30}$", city, re.I):
                driver_licence = DriverLicence(id, person_id, serial, license_type, city, register_date, expire_date)
                return True, self.service.edit(driver_licence)
            else:
                raise ValueError("letters not correct for city")

        except Exception as e:
            return False, f"Error!!:{e}"

    def delete(self, id):
        try:
            return self.service.delete(id)

        except Exception as e:
            return False, f"Error!!:{e}"

    def find_by_id(self, id):
        try:
            licence_info = self.service.find_by_id(id)
            if licence_info:
                return True, licence_info
            else:
                raise ValueError("licence information for this id not found")

        except Exception as e:
            return False, f"Error!!:{e}"

    def find_by_serial(self, serial):
        try:
            licence_info = self.service.find_by_serial(serial)
            if licence_info:
                return True, licence_info
            else:
                raise ValueError("licence information for this serial not found")

        except Exception as e:
            return False, f"Error!!:{e}"

    def find_by_all(self):
        try:
            licence_info = self.service.find_all()
            if licence_info:
                return True, licence_info
            else:
                raise ValueError("licence information for this licence not found")

        except Exception as e:
            return False, f"Error!!:{e}"

