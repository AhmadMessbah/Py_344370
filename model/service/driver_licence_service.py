from model.repository.driver_licence_repository import *

class DriverLicenceService:
    def __init__(self):
        self.repo = DriverLicenceRepository()


    def save(self,driver_licence):
        return self.repo.save(driver_licence)


    def edit(self,driver_licence):
        driver_licence = self.repo.find_by_id(driver_licence)
        if driver_licence :
            return self.repo.edit(driver_licence)
        else :
            raise ValueError ("id not found to edit !")


    def delete(self,driver_licence):
        driver_licence = self.repo.find_by_id(driver_licence)
        if driver_licence :
            return self.repo.delete(driver_licence)
        else :
            raise ValueError ("id not found to delete !")


    def find_by_id(self,id):
        return self.repo.find_by_id(id)


    def find_by_serial(self,serial):
        return self.repo.find_by_serial(serial)


    def find_all(self):
        return self.repo.find_all()
