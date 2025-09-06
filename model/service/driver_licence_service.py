from model.repository.driver_licence_repository import *

class DriverLicenceService:
    def __init__(self):
        self.driver_licence_repo = DriverLicenceRepository()


    def save(self,driver_licence):
        return self.driver_licence_repo.save(driver_licence)


    def edit(self,driver_licence):
        return self.driver_licence_repo.edit(driver_licence)


    def delete(self,id):
        return self.driver_licence_repo.delete(id)


    def find_by_id(self,id):
        return self.driver_licence_repo.find_by_id(id)


    def find_by_serial(self,serial):
        return self.driver_licence_repo.find_by_serial(serial)


    def find_all(self):
        return self.driver_licence_repo.find_all()
