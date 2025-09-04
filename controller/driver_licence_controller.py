from model.entity.driver_licence import DriverLicence
from model.service.driver_licence_service import DriverLicenceService
from model.tools.decorators import *


class DriverLicenceController:
    def __init__(self):
        self.driver_licence_service = DriverLicenceService()


    @exception_handling
    def save(self, person_id, serial, licence_type, city, registered_date, expired_date):
        driver_licence = DriverLicence(None, person_id, serial, licence_type, city, registered_date, expired_date)
        return self.driver_licence_service.save(driver_licence)


    @exception_handling
    def edit(self, id, person_id, serial, licence_type, city, registered_date, expired_date):
        driver_licence = DriverLicence(id, person_id, serial, licence_type, city, registered_date, expired_date)
        return self.driver_licence_service.edit(driver_licence)


    @exception_handling
    def delete(self, id):
        return self.driver_licence_service.delete(id)


    @exception_handling
    def find_by_id(self, id):
        return self.driver_licence_service.find_by_id(id)


    @exception_handling
    def find_by_serial(self, serial):
        return self.driver_licence_service.find_by_serial(serial)


    @exception_handling
    def find_all(self):
            return self.driver_licence_service.find_all()







